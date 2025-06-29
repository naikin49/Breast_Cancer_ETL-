import json
import joblib
import os

def save_all(model, metrics, output_dir="results"):
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(model, f"{output_dir}/model.pkl")
    with open(f"{output_dir}/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
