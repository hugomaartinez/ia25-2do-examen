"""
Custom evaluation metrics for thyroid disease classification.

Exports:
    thyroid_disease_f2_score: Macro F2 score over the two disease classes.
    thyroid_scorer: Pre-built scorer for use with sklearn CV utilities.
"""

import numpy as np
from sklearn.metrics import make_scorer, fbeta_score


def thyroid_disease_f2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Calculate the Macro F2 Score for hyperthyroid and hypothyroid classes.
    
    This metric explicitly focuses on the minority "sick" classes, assigning
    twice as much weight to Recall as Precision. This mitigates the risk of a 
    trivial classifier that predicts everyone is sick just to maximize recall.
    
    Args:
        y_true: Ground truth labels (string or integer encoded).
        y_pred: Predicted labels (same encoding as y_true).
        
    Returns:
        Macro F2 Score of the disease classes (0.0 to 1.0).
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # Handle both string labels and integer-encoded labels safely
    if np.issubdtype(y_true.dtype, np.integer) or (len(y_true) > 0 and isinstance(y_true[0], (int, np.integer))):
        # Integer labels: assume standard LabelEncoder ordering
        # alphabetical: hyperthyroid=0, hypothyroid=1, negative=2
        hyper_label = 0
        hypo_label = 1
    else:
        # String labels
        hyper_label = 'hyperthyroid'
        hypo_label = 'hypothyroid'
    
    # Calculate Macro F2 score focusing ONLY on the disease labels
    # beta=2 weights recall as twice as important as precision
    return float(fbeta_score(
        y_true, 
        y_pred, 
        beta=2, 
        labels=[hyper_label, hypo_label], 
        average='macro', 
        zero_division=0
    ))

# Pre-built scorer for convenience with cross_val_score, GridSearchCV, etc.
thyroid_scorer = make_scorer(thyroid_disease_f2_score)