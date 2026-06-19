# 📂 Data Directory

This directory stores the multi-stage dataset files used throughout the project. The data is partitioned into raw, intermediate, and processed stages to ensure a clean, reproducible engineering pipeline.

## 📁 Directory Structure

```bash
data/
├── raw/
│   ├── water_quality_training_dataset.csv # Raw historical water measurements
│   └── submission_template.csv            # Blank validation template for submissions
├── intermediate/
│   ├── landsat_train_features_base.csv    # Extracted Landsat training features
│   ├── landsat_val_features_base.csv      # Extracted Landsat validation features
│   ├── terraclimate_train_features_base.csv # Extracted TerraClimate training features
│   ├── terraclimate_val_features_base.csv   # Extracted TerraClimate validation features
│   └── deprecated/                         # Legacy/unused intermediate files
└── processed/
    ├── train_features.csv                  # Merged & cleaned training dataset
    └── val_features.csv                    # Merged & cleaned validation dataset
```

## 📊 Dataset Descriptions

### 1. `raw/`
* **`water_quality_training_dataset.csv`**: Contains physical water samples collected from river locations across South Africa between 2011 and 2015. Key columns include `Latitude`, `Longitude`, `Sample Date`, and the three targets: `Total Alkalinity`, `Electrical Conductance`, and `Dissolved Reactive Phosphorus`.
* **`submission_template.csv`**: The target validation locations and dates. You must fill in the predicted values for the three water parameters.

### 2. `intermediate/`
* Stores the base features extracted directly from satellite catalogs (Landsat STAC) and climate sources (TerraClimate). This separates the expensive download/extraction step from the downstream feature preparation.

### 3. `processed/`
* **`train_features.csv` & `val_features.csv`**: The final datasets used for machine learning. Created by running `data-engineering/feature_engineering.ipynb`, these files represent the unified data containing the target water quality parameters and all aligned environmental features.
