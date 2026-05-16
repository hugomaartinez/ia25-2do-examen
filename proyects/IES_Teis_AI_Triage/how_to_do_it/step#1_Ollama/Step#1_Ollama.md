# INSTALAR LLAMA3 CON OLLAMA

## INSTALAR OLLAMA EN LINUX

Ollama tiene un guión de instalación oficial que hace todo el trabajo. Abre un terminal y ejecuta el siguiente comando:

curl -fsSL https://ollama.com/install.sh  sh`

**Nota: Este comando descargará e instalará Ollama, y lo configurará como un servicio en segundo plano.**


### DESCARGAR Y EJECUTAR LLAMA3

Una vez que la instalación de Ollama termina, se puede descargar y emitir Llama 3 directamente. 
En la misma terminal, escriba:

«ollama run llama3»


- Ollama descargará los pesos del modelo (la versión de 8B parámetros pese unos 4.7 GB, así que tarderá un poco dependiente de tu conexión). 
- Una vez descargado, verás un prompt en la terminal donde ya puedes chatear con Llama 3 para probar que funciona.
- Para salir de ese chat en la terminal, simplemente escriba /bye o proposición Ctrl + D. Ollama seguirá ejecutándose en segundo plano.

### DETENER EL SERVICIO DE OLLAMA POR COMPLETO

El script que usamos en el paso anterior instalado Ollama como un servicio de tu sistema Linux. Para añadirlo totalmente y liberar todos los recursos de tu PC antes de cerrar la terminal, ejecuta este comando:

«sudo systemctl stop ollama»

### COMANDOS EXTRA QUE TE SERÁN MUY ÚTILES

> #Para encenderlo de nuevo:
>
«sudo systemctl start ollama»
>
> #Para ver si está encendido o apagado:
>
«sudo systemctl status ollama»
> #(pulsa la tecla q para salir de esa pantalla).
>
> #Para reiniciarlo (si alguna vez se queda saqueado):
>
«sudo systemctl reiniciar ollama»


### DESACTIVAR EL ARRANQUE AUTOMÁTICO

Abre tu terminal y ejecuta el siguiente comando:

«sudo systemctl deshabilitar ollama»

Al ejecutar esto, el sistema eliminará el enlace que hace que Ollama se encienda solo al arrancar Linux. Tranquilo, esto no desinstala ni borra nada, solo le dice al sistema: "no entiendas esto hasta que yo te lo pida". A partir de ahora, cada vez que entiendas tu PC, Ollama estará alojado por defecto. Cuando quieras volver a charlar con Llama 3, solo tendrás que hacer este paso previo en la terminal:

«sudo systemctl start ollama»

### CREEAR ACCESOS DIRECTOS PARA INICIAR Y DETENER OLLAMA (LINUX MINT)

Como el comando para iniciar Ollama requiere permisos de administrador (usamos sudo), si creamos un acceso directo normal, fallaría siempre debido a que no tendría dónde pedirte la contraseña. Para resolverlo, usamos un comando llamado pkexec, que hace que Linux Mint te muestre una venta gráfica pidiendo tu contraseña, igual que cuando instalas un programa nuevo.

Aquí tienen los pasos para crear el lanzador en Cinnamon:
#### CREAR EL LANZADOR EN EL ESCRITORIO PARA INICIAR OLAMA

Ve al escrito de tu Linux Mint, haz clic derecho en cualquier espacio vacío y selección Crear un nuevo lanzador aquí... (o Crear un nuevo lanzador aquí...).

Se abrirá una ventana con las propiedades del lanzador. Rellénalo con estos datos:

Nombre: Iniciar Ollama
    
Comando: pkexec systemctl start ollama
    
Comentario: Encierde el motor de IA local.
    
(Opcional) Si haces clic en el icono del cohete a la izquierda, puedes elegir el icono que más te guste de la galería de Linux Mint (por ejemplo, un cerebro, un chip o un crecimiento).
    
Haz clic en Aceptar.

#### CREAR EL LANZADOR EN EL ESCRITORIO PARA APAGAR OLLAMA

Ya que tienen un botón para encenderlo, lo ideal es tener otro para apagarlo y liberar la memoria cuando terminas. 
Puedes repetir exactamente los mismos pasos de arriba, pero cambiando los datos a este:

Nombre: Apagar Ollama

Comando: pkexec systemctl stop ollama

Comentario: Apaga el motor de IA local.

## INSTALAR OLLAMA EN WINDOWS

Instalar Llama 3 usando Ollama en Windows 11 es un proceso muy directo, ya que Ollama cuenta con un instalador nativo que hace casi todo el trabajo pesado. 

Aquí tienes el paso a paso destacado:

### Paso 1: Descargar Ollama
1. Abre tu navegador web y ve a la página oficial: **[__PATH0_/download](https://ollama.com/download_)**.
2. Haz clic en el botón grande que dados **"Download for Windows"**. Esto descargará un archivo llamado `OllamaSetup.exe`.

### Paso 2: Instalar el programa
1. Ve a tu alfombra de Descargas y haz doble clic en **`OllamaSetup.exe_**.
2. Haz clic en **"Install"** y espera a que termine el proceso. No te pedirás configuraciones completas.
3. Una vez instalado, es posible que veas el icono de Ollama (una pequeña llama) en la banda del sistema, en la esquina inferior derecha de la barra de áreas. Esto indica que el motor de Ollama se está ejecutando en segundo plano.

### Paso 3: Abrir la terminal de Windows
Para indicarle a Ollama qué modelo queremos, necesitamos usar la línea de comandos.
1. Haz clic en el menú **Inicio** de Windows 11.
2. Escriba **`cmd`** o **`PowerShell`** y proposición la tecla Enter para abrir la consola.

### Paso 4: Descargar y expulsar Llama 3
1. En la ventana negra o azul que se acaba de abrir, escriba el siguiente comando y premisa Enter:
   ```bash
   ollama run llama3
   ```
2. **Espera a que se descargue:** Como es la primera vez que ejecutas este modelo, Ollama empezará a descargarlo. La versión estádar de Llama 3 (de 8 millones de millones de parámetros) pesa alrededor de **__PATH0_ GB**, por lo que tardará unos minutos dependiendo de la velocidad de tu conexión a internet.

### Paso 5: ¡Empieza un charlatán!
1. Una vez finalizada la descarga, verás que en la pantalla aparece algo como . Ese es el indicador de que Llama 3 está listo para escucharte.
2. Escribe cualquier pregunta o instrucción (en español o inglés) y premisa Enter. La IA te responderá directamente en la consola.
3. Cuando quieres cerrar el chat y salir, escribes simplemente **`/bye`** y condiciones Enter.

## CREEAR ACCESO DIRECTOS PARA INICIAR Y DETENER OLAMA (WINDOWS)

En Windows, Ollama se instala por defecto como una aplicación en segundo plano que se inicia automáticamente al encender el ordenador (aparece en la banda del sistema, junto al recuerdo). 

Si quieres tener el control total y abrir o cerrar Ollama solo cuando lo necesites para ahorar memoria RAM, puedes crear dos accesos directos muy sencillos en tu escritorio.

Aquí tienen los pasos exactos:

### 1. Crear el acceso directo para DETENER Ollama

Para parar Ollama, necesitamos un comando que cierra la aplicación de forma segura.

1. Haz clic derecho en un espacio vacío de tu Escritor.
2. Selecciona **Nuevo** > **Acceso directo**.
3. En la casilla de "Escribe la ubicación del elemento", copia y pega exactamente el siguiente comando:
   ```cmd
   taskkill /F /IM "ollama app.exe" /IM "ollama.exe"
   ```
4. Haz clic en **Siguiente**.
5. Ponle un nombre fácil de reconocer, por ejemplo: **`Detener Ollama`**.
6. Haz clic en **Finalizar**.

### 2. Crear el acceso directo para INICIAR Ollama

Para volver a iniciarlo, solo necesitamos añadir al archivo ejecutable de la aplicación.

1. Haz clic derecho en un espacio vacío de tu Escritor.
2. Selecciona **Nuevo** > **Acceso directo**.
3. En la casilla de ubicación, copia y pega la ruta estándar de instalación de Ollama en Windows:
   ```cmd
   %LOCALAPPDATA%\Programs\Ollama\ollama app.exe
   ```
4. Haz clic en **Siguiente**.
5. Ponle un nombre, por ejemplo: **`Iniciar Ollama`**.
6. Haz clic en **Finalizar**.

---

### Consejo extra: Evitar que Ollama se inicia con Windows
Si vas a usar estos robots manuales, lo ideal es evitar que Ollama arranque solo cada vez que enciendes el PC. Para hacerlo:

1. Busca el icono de Ollama (la llamita) en la banda del sistema (esquina inferior derecha de tu pantalla, quizá dentro de la flechita de iconos ocultos).
2. Haz clic derecho sobre el icono.
3. Desmarca la opción **"Ejecutar al inicio"** (Ejecutar al inicio).
4. A partir de ahora, Ollama estará completamente alojado al encender tu PC, y solo consumirá recursos cuando haya doble clic en tu nuevo acceso directo de **Iniciar Ollama**.

---

## Nota sobre el resentimiento

Para que la versión esté de Llama 3 funciona con fluidez, lo ideal es tener al menos **8 GB de memoria RAM** (recomendable 16 GB). Si tienes una tarjeta gráfica dedicada (NVIDIA o AMD), Ollama la detectará automáticamente para generar las respuestas mucho más rápido.

Se puede utilizar un modelo más ligero si no se dispone de los recursos necesarios cmo por ejemplo qwen2.5:3b. Para él, se puede utilizar el siguiente comando:

> ollama ejecutar qwen2.5:3b

- Se descargará aproximadamente 1.9 GB (que es el tamaño del modelo cuantificado para 3B).

- Se verificará la integridad del archivo.

- Y por último levantará un chat interactivo inmediato para que pueda probarlo.

**Comandos adicionales**

- Ver modelos instalados: Si quieres ver cómo espacio ocupado o qué otros modelos tienen.

> lista de ollama

- Borrar modelos sobres: Para liberar RAM y espacio en disco.

> ollama rm llama3 (o el nombre exacto que aparece en tu lista).

- Actualizar: Los modelos reciben mejores mejoras frecuentemente. 

> ollama tirar qwen2.5:3b








