# ⚙️ Data Engineering Pipeline

This folder contains the notebooks responsible for retrieving, processing, and merging the multi-modal geospatial and climate datasets used in this project.

## 📝 Pipeline Notebooks

| Notebook | Purpose | Input | Output |
| :--- | :--- | :--- | :--- |
| **`landsat_extraction.ipynb`** | Queries the Microsoft Planetary Computer STAC API to extract surface reflectance satellite bands matching training coordinates and dates. | Geospatial coordinates | `landsat_*_features_base.csv` |
| **`terraclimate_extraction.ipynb`** | Pulls Monthly Climate Water Balance features from the TerraClimate collection on Azure/Planetary Computer. | Geospatial coordinates | `terraclimate_*_features_base.csv` |
| **`feature_engineering.ipynb`**| Combines raw water samples with the extracted Landsat and TerraClimate intermediate datasets via spatial-temporal joins. | Base files & intermediate CSVs | `train_features.csv`, `val_features.csv` |

## 📂 Deprecated / Experimental Extractions
Inside the `deprecated/` folder, you can find experimental data extractions:
* **`open_meteo_extraction.ipynb`**: Draft code for fetching fine-grained hourly meteorological data.
* **`soilgrids_extraction.ipynb`**: Experimental scripts to fetch ground-level soil texture and properties.
