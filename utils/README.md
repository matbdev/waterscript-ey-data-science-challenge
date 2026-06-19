# 🛠️ Reusable Utilities & Modules

This directory contains utility modules and shared constants to prevent code duplication across the data engineering and modeling notebooks.

## 📁 Directory Contents

* **`functions.py`**: Common utility functions including:
  * `save_df`: Saves a Pandas DataFrame locally as a CSV and uploads it to a Snowflake stage.
  * `get_catalog`: Authenticates and loads Planetary Computer collections via the STAC client.
  * `combine_datasets`: Performs spatial-temporal left joins to merge extracted features.
  * `padronize_keys`: Standardizes dates and rounds coordinate precisions to ensure exact spatial matches.
* **`variables.py`**: Holds global configurations, shared variables, paths, database schemas, and parameters used throughout the project lifecycle.
