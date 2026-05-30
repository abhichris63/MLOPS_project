import os

# ---------- DATA INGESTION ------------------
RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR,"raw.csv") # artifacts/raw/raw.csv
TRAIN_FILE_PATH = os.path.join(RAW_DIR,"train.csv") # artifacts/raw/train.csv
TEST_FILE_PATH = os.path.join(RAW_DIR,"test.csv") # artifacts/raw/test.csv

CONFIG_PATH = "config/config.yaml"

# ---------- DATA PREPROCESSING ------------------
PROCESSED_DIR = "artifacts/processed_data"
PROCESSED_TRAIN_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_train_data.csv") # artifacts/processed_data/processed_train_data.csv
PROCESSED_TEST_DATA_PATH = os.path.join(PROCESSED_DIR, "processed_test_data.csv") # artifacts/processed_data/processed_test_data.csv

# ---------- MODEL TRAINING ------------------
MODEL_OUTPUT_PATH = "artifacts/models/lg_model.pkl" # artifacts/models/lg_model.pkl