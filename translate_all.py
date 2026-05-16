#!/usr/bin/env python3
"""
Script para traducir archivos Markdown y Jupyter Notebooks de inglés a español
Preserva código, URLs, nombres de librerías y estructura
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple
from transformers import MarianMTModel, MarianTokenizer

# Modelo de traducción inglés -> español
MODEL_NAME = "Helsinki-NLP/Opus-MT-en-es"

class Translator:
    def __init__(self):
        print("🔄 Cargando modelo de traducción (puede tardar)...")
        self.tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        self.model = MarianMTModel.from_pretrained(MODEL_NAME)
        print("✓ Modelo cargado")
    
    def translate_text(self, text: str, batch_size: int = 10) -> str:
        """Traduce texto preservando URLs y código"""
        if not text or len(text.strip()) < 2:
            return text
        
        # Proteger URLs
        url_pattern = r'https?://[^\s)}\]`]*'
        urls = re.findall(url_pattern, text)
        text_protected = text
        for i, url in enumerate(urls):
            text_protected = text_protected.replace(url, f"__URL{i}__")
        
        # Proteger rutas de archivo con .ext
        path_pattern = r'[\w/.-]+\.[a-zA-Z0-9]+(?!["\'])'
        paths = re.findall(path_pattern, text_protected)
        for i, path in enumerate(paths):
            if not path.startswith('__URL'):
                text_protected = text_protected.replace(path, f"__PATH{i}__")
        
        # Dividir en oraciones y traducir
        sentences = re.split(r'(?<=[.!?])\s+', text_protected)
        translated_sentences = []
        
        for sentence in sentences:
            if len(sentence.strip()) < 2:
                translated_sentences.append(sentence)
                continue
            
            try:
                inputs = self.tokenizer.encode(sentence, return_tensors="pt")
                outputs = self.model.generate(inputs, max_length=512)
                translated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
                translated_sentences.append(translated)
            except Exception as e:
                print(f"⚠️ Error traduciendo: {e}")
                translated_sentences.append(sentence)
        
        result = " ".join(translated_sentences)
        
        # Restaurar URLs
        for i, url in enumerate(urls):
            result = result.replace(f"__URL{i}__", url)
        
        # Restaurar rutas
        for i, path in enumerate(paths):
            result = result.replace(f"__PATH{i}__", path)
        
        return result
    
    def translate_markdown(self, content: str) -> str:
        """Traduce markdown preservando código, URLs y estructura"""
        lines = content.split('\n')
        result = []
        in_code_block = False
        code_fence = None
        
        for line in lines:
            # Detectar bloques de código
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                code_fence = line
                result.append(line)
                continue
            
            if in_code_block:
                result.append(line)
                continue
            
            # Saltar líneas vacías
            if not line.strip():
                result.append(line)
                continue
            
            # Procesar diferentes elementos markdown
            if line.startswith('#'):
                # Títulos
                match = re.match(r'^(#+)\s+(.+)$', line)
                if match:
                    hashes, title = match.groups()
                    translated_title = self.translate_text(title)
                    result.append(f"{hashes} {translated_title}")
                else:
                    result.append(line)
            elif line.startswith('- ') or line.startswith('* '):
                # Listas
                match = re.match(r'^(-|\*)\s+(.+)$', line)
                if match:
                    bullet, text = match.groups()
                    translated = self.translate_text(text)
                    result.append(f"{bullet} {translated}")
                else:
                    result.append(line)
            elif line.startswith('> '):
                # Citas
                quote = line[2:]
                translated = self.translate_text(quote)
                result.append(f"> {translated}")
            elif re.match(r'^\d+\.\s+', line):
                # Listas numeradas
                match = re.match(r'^(\d+\.\s+)(.+)$', line)
                if match:
                    num, text = match.groups()
                    translated = self.translate_text(text)
                    result.append(f"{num}{translated}")
                else:
                    result.append(line)
            else:
                # Párrafos normales
                translated = self.translate_text(line)
                result.append(translated)
        
        return '\n'.join(result)
    
    def translate_notebook(self, notebook_path: str) -> Dict:
        """Traduce un notebook preservando código"""
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        for cell in nb.get('cells', []):
            if cell['cell_type'] == 'markdown':
                # Traducir celdas markdown
                source = ''.join(cell.get('source', []))
                translated = self.translate_markdown(source)
                cell['source'] = translated.split('\n')
            
            elif cell['cell_type'] == 'code':
                # Traducir solo comentarios en código
                source = ''.join(cell.get('source', []))
                translated = self.translate_code_comments(source)
                cell['source'] = translated.split('\n')
        
        return nb
    
    def translate_code_comments(self, code: str) -> str:
        """Traduce comentarios en código Python"""
        lines = code.split('\n')
        result = []
        
        for line in lines:
            # Encontrar comentarios
            if '#' in line:
                parts = line.split('#', 1)
                code_part = parts[0]
                comment_part = '#' + parts[1]
                
                # Traducir comentario
                comment_text = comment_part[1:].strip()
                if comment_text:
                    translated_comment = self.translate_text(comment_text)
                    line = code_part + '# ' + translated_comment
            
            result.append(line)
        
        return '\n'.join(result)

def main():
    # Lista de archivos a traducir
    files_to_translate = [
        # READMEs y docs
        'proyects/IES_Teis_AI_Triage/README.md',
        'proyects/IES_Teis_AI_Triage/challenge/answer/rag_2_0.md',
        'proyects/IES_Teis_AI_Triage/challenge/challenge.md',
        'proyects/IES_Teis_AI_Triage/docs/Librerias_Python/langchain-chroma.md',
        'proyects/IES_Teis_AI_Triage/docs/Librerias_Python/langchain-huggingface.md',
        'proyects/IES_Teis_AI_Triage/docs/Librerias_Python/langchain-ollama.md',
        'proyects/IES_Teis_AI_Triage/docs/Librerias_Python/langchain-text-splitters.md',
        'proyects/IES_Teis_AI_Triage/docs/Librerias_Python/langchain.md',
        'proyects/IES_Teis_AI_Triage/docs/Librerias_Python/sentence-transformers.md',
        'proyects/IES_Teis_AI_Triage/docs/RAG.md',
        'proyects/IES_Teis_AI_Triage/docs/RAG_2_0.md',
        'proyects/IES_Teis_AI_Triage/docs/chromaDB.md',
        'proyects/IES_Teis_AI_Triage/docs/ollama.md',
        'proyects/IES_Teis_AI_Triage/how_to_do_it/step#1_Ollama/Step#1_Ollama.md',
        'proyects/ai-chat-guardrails/README.md',
        'proyects/ai-chat-guardrails/docs/test_cases.md',
        'proyects/california-e2e/README.md',
        'proyects/california-e2e/types_estimators.md',
        'proyects/computer-vision/README.md',
        'proyects/king-county/README.md',
        
        # Notebooks
        'proyects/IES_Teis_AI_Triage/challenge/answer/implementation.ipynb',
        'proyects/IES_Teis_AI_Triage/how_to_do_it/step#2_RAG/Step#2_RAG.ipynb',
        'proyects/IES_Teis_AI_Triage/how_to_do_it/step#3_Agent/Step#3_Agent.ipynb',
        'proyects/california-e2e/e2e010_framing.ipynb',
        'proyects/california-e2e/e2e020_eda.ipynb',
        'proyects/california-e2e/e2e025_train_test.ipynb',
        'proyects/california-e2e/e2e030_feature_engineering.ipynb',
        'proyects/california-e2e/e2e041_missing.ipynb',
        'proyects/california-e2e/e2e042_categorical.ipynb',
        'proyects/california-e2e/e2e043_scaling.ipynb',
        'proyects/california-e2e/e2e050_pipelines.ipynb',
        'proyects/california-e2e/e2e051_custom_transformers.ipynb',
        'proyects/california-e2e/e2e060_spatial_clustering.ipynb',
        'proyects/california-e2e/e2e070_model_evaluation.ipynb',
        'proyects/california-e2e/e2e080_hyperparameters.ipynb',
        'proyects/california-e2e/e2e081_hyperparameters2.ipynb',
        'proyects/california-e2e/e2e090_neural_network.ipynb',
        'proyects/computer-vision/chromadb_intro.ipynb',
        'proyects/computer-vision/face_recognition_pipeline.ipynb',
        'proyects/computer-vision/opencv/opencv_fundamentals.ipynb',
        'proyects/computer-vision/opencv/opencv_image_processing.ipynb',
        'proyects/computer-vision/opencv/opencv_video.ipynb',
        'proyects/computer-vision/vectors_and_embeddings.ipynb',
        'proyects/computer-vision/yolo/object_detection_and_yolo.ipynb',
        'proyects/computer-vision/yolo/yolo_custom_training.ipynb',
        'proyects/king-county/01-eda.ipynb',
        'proyects/king-county/02-repeated_ids.ipynb',
        'proyects/king-county/03-temporal_leakage.ipynb',
        'proyects/king-county/04a-preprocessing-step-by-step.ipynb',
        'proyects/king-county/04b-preprocessing-pipeline.ipynb',
        'proyects/king-county/05-modeling.ipynb',
        'proyects/king-county/06-deep-learning.ipynb',
        'proyects/thyroid/01_data_preparation.ipynb',
        'proyects/thyroid/02_metrics_deep_dive.ipynb',
        'proyects/thyroid/03_baseline_models.ipynb',
        'proyects/thyroid/04_xgboost.ipynb',
        'proyects/thyroid/05_neural_network.ipynb',
    ]
    
    translator = Translator()
    total = len(files_to_translate)
    success = 0
    failed = []
    
    for idx, file_path in enumerate(files_to_translate, 1):
        if not os.path.exists(file_path):
            print(f"[{idx}/{total}] ⚠️  No existe: {file_path}")
            failed.append(file_path)
            continue
        
        try:
            print(f"[{idx}/{total}] 🔄 Traduciendo: {file_path}")
            
            if file_path.endswith('.md'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                translated = translator.translate_markdown(content)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(translated)
            
            elif file_path.endswith('.ipynb'):
                notebook = translator.translate_notebook(file_path)
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(notebook, f, ensure_ascii=False, indent=1)
            
            print(f"    ✓ Completado")
            success += 1
        
        except Exception as e:
            print(f"    ✗ Error: {e}")
            failed.append(file_path)
    
    print(f"\n{'='*60}")
    print(f"Resumen: {success}/{total} archivos traducidos")
    if failed:
        print(f"Fallidos: {len(failed)}")
        for f in failed:
            print(f"  - {f}")

if __name__ == '__main__':
    main()
