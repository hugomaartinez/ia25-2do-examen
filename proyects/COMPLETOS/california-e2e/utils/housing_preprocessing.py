import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.cluster import KMeans

RANDOM_STATE = 42


cat_pipeline = make_pipeline( # Pipeline for categorical features
    SimpleImputer(strategy="most_frequent"),  # Impute missing values with the most frequent value
    OneHotEncoder(handle_unknown="ignore")    # Encode categorical features
)

class ClusterSimilarity(BaseEstimator, TransformerMixin):
    """
    Transformer that calculates the similarity between each instance and cluster centroids
    using an RBF (Radial Basis Function) kernel.
    """
    def __init__(self, n_clusters=10, gamma=1.0, random_state=None):
        self.n_clusters = n_clusters  # Number of clusters
        self.gamma = gamma            # RBF kernel bandwidth
        self.random_state = random_state
        
    def fit(self, X, y=None, sample_weight=None):
        self.kmeans_ = KMeans(self.n_clusters, n_init=10, 
                             random_state=self.random_state)
        self.kmeans_.fit(X, sample_weight=sample_weight)
        return self
        
    def transform(self, X):
        # Calculate RBF similarity between each instance and cluster centroids
        return rbf_kernel(X, self.kmeans_.cluster_centers_, gamma=self.gamma)
    
    def get_feature_names_out(self, names=None):
        return [f"Cluster {i} similarity" for i in range(self.n_clusters)]


def column_ratio(X):
    """Calculate the ratio between the first and second column"""
    return X[:, [0]] / X[:, [1]]

def ratio_name(function_transformer, feature_names_in):
    """Function to name the ratio output columns"""
    return ["ratio"]

def ratio_pipeline():
    """Pipeline that creates new features by dividing two columns"""
    return make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(column_ratio, feature_names_out=ratio_name),
        StandardScaler()
    )

log_pipeline = make_pipeline( # Pipeline for logarithmic transformation
    SimpleImputer(strategy="median"),
    FunctionTransformer(np.log, feature_names_out="one-to-one"),
    StandardScaler()
)

default_num_pipeline = make_pipeline( # Default pipeline for numerical features
    SimpleImputer(strategy="median"),
    StandardScaler()
)

def get_preprocessing_pipeline(n_clusters, gamma=1.0):
    """
    Returns a preprocessing pipeline configured for housing data

    Args:
        n_clusters: Number of clusters for geospatial similarity. Uses by default
            the value that gave best results in hyperparameter search.
        gamma: RBF kernel parameter

    Returns:
        ColumnTransformer: Complete preprocessing pipeline
    """
    cluster_simil = ClusterSimilarity(n_clusters=n_clusters, gamma=gamma, random_state=RANDOM_STATE)

    return ColumnTransformer([
        # Ratios (new features)
        ("bedrooms", ratio_pipeline(), ["total_bedrooms", "total_rooms"]),        # ratio between bedrooms and rooms
        ("rooms_per_house", ratio_pipeline(), ["total_rooms", "households"]),     # ratio between rooms and households
        ("people_per_house", ratio_pipeline(), ["population", "households"]),     # ratio between population and households

        # Logarithmic transformation to normalize skewed distributions
        ("log", log_pipeline, ["total_bedrooms", "total_rooms", "population",
                              "households", "median_income"]),

        # Geospatial features using clustering
        ("geo", cluster_simil, ["latitude", "longitude"]),

        # Categorical features
        ("cat", cat_pipeline, make_column_selector(dtype_include=object)),
    ],
    remainder=default_num_pipeline)  # Remaining columns: housing_median_age


def scale_target(y_train, y_val, y_test):
    """
    Scale target variables using StandardScaler.
    
    Args:
        y_train: Training target values
        y_val: Validation target values  
        y_test: Test target values
        
    Returns:
        tuple: (scaled training data, scaled validation data, scaled test data, scaler)
    """
    y_scaler = StandardScaler()
    y_train_scaled_np = y_scaler.fit_transform(y_train.values.reshape(-1, 1))
    y_val_scaled_np = y_scaler.transform(y_val.values.reshape(-1, 1))
    y_test_scaled_np = y_scaler.transform(y_test.values.reshape(-1, 1))
    
    return y_train_scaled_np, y_val_scaled_np, y_test_scaled_np, y_scaler