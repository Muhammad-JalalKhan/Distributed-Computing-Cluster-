import time
from dask.distributed import Client
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib

if __name__ == "__main__":
    # 1. Connect to your active cluster (Ryzen IP)
    client = Client('tcp://10.90.20.76:8786')
    print(f"Cluster connected. Using workers: {client.scheduler_info()['workers'].keys()}")

    # 2. Create a "Heavy" Synthetic Dataset
    # 10,000 samples with 20 features - enough to stress the i5's RAM
    X, y = make_classification(n_samples=10000, n_features=20, random_state=42)

    # 3. Define the ML Model
    model = RandomForestClassifier()

    # 4. Define "Hyperparameters" to test
    # This creates 3 x 3 x 2 = 18 combinations. 
    # With 5-fold cross-validation, that's 90 total training sessions!
    param_grid = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }

    print("Starting Distributed Hyperparameter Tuning (90 Tasks)...")
    start_time = time.time()

    # 5. THE MAGIC LINE: Tell Scikit-Learn to use your Dask Cluster
    with joblib.parallel_backend('dask'):
        grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
        grid_search.fit(X, y)

    end_time = time.time()

    print("\n--- ML Project Results ---")
    print(f"Best Score: {grid_search.best_score_:.4f}")
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Total Distributed Training Time: {end_time - start_time:.2f} seconds")