# 🔍 Exploratory Data Analysis & Quality Checks

This folder contains pre-modeling scripts to assess and guarantee the quality, distribution, and completeness of our data.

## 📁 Directory Contents

* **`check_data_quality.py`**: A diagnostic Python utility script that:
  * Counts missing/null values across both targets and features.
  * Checks for extreme outliers and physical/geospatial duplicates.
  * Validates coordinates to ensure they fall within the boundaries of South Africa.
  * Provides a baseline statistical summary of the raw water quality parameters.
