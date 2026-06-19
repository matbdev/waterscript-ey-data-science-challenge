# 💧 Optimizing South Africa's Clean Water Supply — EY AI & Data Challenge 2026

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Snowflake-29B5F6?style=for-the-badge&logo=snowflake&logoColor=white" alt="Snowflake" />
  <img src="https://img.shields.io/badge/Microsoft-Planetary%20Computer-0078D4?style=for-the-badge&logo=microsoft&logoColor=white" alt="Planetary Computer" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebooks" />
  <img src="https://img.shields.io/badge/License-Apache%202.0-green?style=for-the-badge" alt="License" />
</p>

---

## Introduction

### The Problem
Access to clean water is one of the most critical challenges of our time. In South Africa, managing and predicting water quality across sprawling, geographically diverse river systems is essential to optimizing the clean water supply and protecting ecosystems. 

Traditionally, monitoring water quality requires expensive, manual ground-level sampling that lacks spatial and temporal continuity. By bridging the gap between sporadic physical water sampling and continuous satellite/climate observation, machine learning can offer a scalable, cost-effective, and robust solution to predict and manage water resources.

### Program & Project Description
This repository contains a full-scale machine learning and data engineering solution built for the **EY AI & Data Challenge 2026**. 

The core objective is to **develop a machine learning model capable of forecasting three key water quality parameters** across various river locations in South Africa:
1. **Total Alkalinity**
2. **Electrical Conductance** (Salinity/Conductivity)
3. **Dissolved Reactive Phosphorus** (Phosphate levels)

The dataset spans from **2011 to 2015** across approximately **200 river locations**. To build a model that generalizes well, the solution must predict these parameters for a separate validation dataset containing river locations from entirely different regions not present in the training set. 

To achieve high-accuracy predictions, this project leverages a multi-modal data pipeline that enriches physical water samples with:
- **Satellite Imagery (Landsat)**: Extracted via the Microsoft Planetary Computer STAC API to capture surface reflectance and turbidity.
- **Climate & Weather Datasets (TerraClimate)**: Providing historical monthly meteorological and water balance data.

---

## Technology Stack

This project leverages a modern data-science and cloud data warehouse stack designed for massive scalability:

- **Core Language**: Python (3.10+)
- **Cloud Data Warehouse & Platform**: **Snowflake** (leveraging Snowpark ML, Snowflake Notebooks on Container Runtime, and external access integrations for remote API requests).
- **Satellite Data Catalog**: Microsoft Planetary Computer STAC API (`pystac_client`, `planetary_computer`).
- **Data Engineering & Geospatial**: `rioxarray`, `geopandas`, `xarray`, `rasterio`, `shapely`, `netCDF4`, `zarr`, `dask`.
- **Machine Learning & Modeling**: `scikit-learn`, `xgboost`, `optuna` (for hyperparameter tuning).
- **Visualization**: `matplotlib`, `seaborn`.

---

## Key Features Implemented

Unlike standard baseline models, this implementation goes far beyond the benchmark to incorporate advanced machine learning and data engineering workflows:

### 1. Advanced Feature Engineering & Remote Sensing
We extract and calculate physical, chemical, and climate indices directly from Landsat satellite imagery and TerraClimate models:
* **Water & Moisture Indices**: 
  - **MNDWI** (Modified Normalized Difference Water Index) to highlight open water features.
  - **NDMI** (Normalized Difference Moisture Index) to measure moisture profiles.
  - **NDVI** (Normalized Difference Vegetation Index) to detect nearby riparian vegetation.
* **Water Quality & Chemical Proxies**:
  - **NDTI** (Normalized Difference Turbidity Index) to estimate water cloudiness/turbidity.
  - **NDSSI** (Normalized Difference Suspended Sediment Index) to detect thin river sediments.
  - **Chlorophyll Proxy** ($NIR / Green$) to capture biological productivity.
  - **Red/Blue Ratio** and **SI** (Salinity Index) to infer alkalinity and mineral dissolution.
* **Climate & Catchment Interactions**:
  - **Water Balance & Water Deficit** ($PPT - PET$).
  - **Runoff Ratio** and **Soil Wash Potential** (capturing sediment transport potential).
  - **Rain vs. Vegetation Interaction** (modeling the riparian filtering/sponge effect).

### 2. Optuna-Optimized Gradient Boosting
* **XGBoost Estimator**: Utilizes a robust `XGBRegressor` that natively handles missing values and complex non-linear interactions without requiring scale-normalization.
* **Automated Hyperparameter Optimization**: Leverages **Optuna** with Tree-structured Parzen Estimators (TPE) across 150 trials to tune tree depth, learning rates, subsampling ratios, L1/L2 regularization (`reg_alpha`, `reg_lambda`), and min child weights.
* **Spatial Leakage Protection**: Implements a `GroupKFold` split based on unique location IDs, guaranteeing that validation folds represent completely unseen rivers to simulate true out-of-region generalization.

### 3. Multi-Source Integrations
* High-resolution spatial extraction via **Microsoft Planetary Computer STAC Client**.
* Sandbox exploration and initial code for **SoilGrids** (soil property mapping) and **Open-Meteo** (hourly historical climate extractions).

---

## 📂 Repository Structure

The project is organized logically into data-engineering, data-science, and setup pipelines:

```bash
.
├── data/                      # Multi-stage data directory
│   ├── raw/                   # Original training samples and submission template
│   ├── intermediate/          # Extracted base features from Landsat/TerraClimate
│   └── processed/             # Fully joined and engineered training & validation datasets
├── data-engineering/          # Extract, Transform, and Load (ETL) notebooks
│   ├── landsat_extraction.ipynb      # Planetary Computer Landsat STAC query/download
│   ├── terraclimate_extraction.ipynb # TerraClimate NetCDF data processing
│   └── feature_engineering.ipynb     # Geospatial joins & final dataset preparation
├── data-science/              # Machine learning and predictive modeling
│   └── benchmark_model.ipynb  # Baseline modeling using Snowpark / Scikit-Learn
├── exploration/               # Pre-modeling exploratory data analysis (EDA)
│   └── check_data_quality.py  # Data quality check and sanity-checking script
├── demo/                      # Code-free visual and setup demonstrations
│   ├── landsat_demo.ipynb     # Demonstration notebook for Landsat API queries
│   └── terraclimate_demo.ipynb# Demonstration notebook for TerraClimate queries
├── setup/                     # Cloud environment and Snowflake staging scripts
│   ├── snowflake_setup.sql    # Snowflake stage & integration configurations
│   └── getting_started_notebook.ipynb # Environment validation notebook
├── utils/                     # Utility Python modules and reusable scripts
│   ├── functions.py           # Core functions (saving to Snowflake, spatial joins, etc.)
│   └── variables.py           # Environment parameters and shared constants
├── requirements.txt           # Python package dependencies
├── LICENSE                    # Apache 2.0 License file
└── LEGAL.md                   # Snowflake service terms and disclaimer
```

---

## Getting Started & Execution Workflow

Follow this step-by-step workflow to reproduce the entire data engineering and model training pipeline.

### Step 1: Environment Setup
1. Configure your Snowflake Account (or a 120-day trial account).
2. Execute the setup script in **`setup/snowflake_setup.sql`** to configure external access integrations, stages, and custom schemas.
3. Verify your environment by running the validation notebook: **`setup/getting_started_notebook.ipynb`**.
4. Install local/notebook dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Data Extraction & Feature Engineering
1. **Landsat Data Extraction**: Open and run **`data-engineering/landsat_extraction.ipynb`** to query the Microsoft Planetary Computer and extract surface reflectance data matching the training/validation geographic coordinates and dates.
2. **TerraClimate Data Extraction**: Open and run **`data-engineering/terraclimate_extraction.ipynb`** to pull climate features (temperature, precipitation, vapor pressure, etc.).
3. **Feature Engineering**: Run **`data-engineering/feature_engineering.ipynb`** to join the raw training samples with Landsat and TerraClimate features into unified training (`train_features.csv`) and validation (`val_features.csv`) sets.

### Step 3: Model Training & Prediction
1. Run **`data-science/benchmark_model.ipynb`** to train machine learning models for total alkalinity, electrical conductance, and dissolved reactive phosphorus.
2. The notebook will automatically yield predictions for the validation dataset and generate a compliant CSV in **`submissions/`**.

---

## Future Steps & Improvements

- [ ] **Ensemble Blending**: Combine XGBoost predictions with other architectures like LightGBM or CatBoost to minimize variance.
- [ ] **Temporal Lags**: Build rolling temporal aggregations to capture antecedent water balance conditions.
- [ ] **Fine-tune Optuna Search Space**: Further restrict or expand search boundaries based on initial study convergence parameters.

---

## Copyright & License

The contents of this repository are Copyright 2026 EY, except the contents of the `setup/` and `utils/` folders, which are Copyright 2026 Snowflake Inc. under the Apache 2.0 License. See the [LICENSE](file:///home/mateusbrambilla/GitHub/waterscript-ey-data-science-challenge/LICENSE) file for more details.
