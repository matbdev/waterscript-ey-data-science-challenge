# 🧪 Data Science & Machine Learning Modeling

This folder contains the core predictive models and validation workflows. 

## 📓 Notebooks & Workflows

### **`benchmark_model.ipynb`**
This notebook establishes the baseline performance for the EY AI & Data Challenge. It performs the following steps:
1. **Data Loading**: Loads the fully-engineered training and validation datasets (`train_features.csv`, `val_features.csv`) from Snowflake/local files.
2. **Preprocessing**: Handles any missing values, standardizes features, and handles outlier detection.
3. **Model Training**: Trains individual machine learning estimators (e.g., Random Forests, Linear Regressors, or Gradient Boosted Trees) for each of the three targeted water quality parameters:
   * **Total Alkalinity**
   * **Electrical Conductance**
   * **Dissolved Reactive Phosphorus**
4. **Validation & Evaluation**: Computes the $R^2$ coefficient of determination for each model to ensure strong regional generalization.
5. **Inference & Export**: Predicts values for the validation template and saves a valid submission CSV file inside `submissions/`.
