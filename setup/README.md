# ⚙️ Environment Setup & Integration

This folder contains the SQL and Python scripts required to initialize the workspace environment on the Snowflake cloud data platform.

## 📁 Directory Contents

* **`snowflake_setup.sql`**: A setup SQL script to execute in your Snowflake Console. It configures:
  * External access integrations (allowing secure HTTP outbound calls from Python to Planetary Computer STAC APIs).
  * Data storage stages to load/unload CSV files.
  * Custom databases, schemas, and warehouses.
* **`getting_started_notebook.ipynb`**: A verification notebook designed to confirm that the Snowflake runtime has correctly loaded external libraries and can connect to external remote catalogs.
