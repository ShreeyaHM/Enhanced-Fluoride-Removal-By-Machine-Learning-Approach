
# 🔬 Enhanced Fluoride Removal by Machine Learning Approach

### An End-to-End Machine Learning Framework for Predicting Fluoride Removal Efficiency

<p align="center">

  🧪 Environmental Science &nbsp; | &nbsp; 🤖 Machine Learning &nbsp; | &nbsp; 📊 Predictive Modeling

</p>

---

## 🌿 1. Project Overview

Excessive fluoride concentration in groundwater is a major environmental and public health concern. Long-term exposure to elevated fluoride levels can lead to dental and skeletal fluorosis.

Adsorption is considered an effective and economically viable approach for fluoride removal from aqueous solutions.

This project presents an **end-to-end Machine Learning framework** for modeling, evaluating, and predicting fluoride removal efficiency using experimental adsorption data.

The framework compares five machine learning regression algorithms to identify the most suitable predictive model.

The models are optimized using **5-Fold Cross-Validation with GridSearchCV** and evaluated using standard regression performance metrics.

### 🎯 Project Objectives

- Develop machine learning models to predict fluoride removal efficiency.
- Investigate the relationship between experimental parameters and fluoride adsorption.
- Compare the predictive performance of five regression algorithms.
- Optimize model hyperparameters using cross-validation.
- Identify the best-performing model based on testing performance.
- Provide a reproducible workflow for data preprocessing, model training, and evaluation.

---

## 🧪 2. Dataset Description

The dataset contains **23,100 experimental observations** representing different fluoride adsorption operating conditions.

### Input Features

The models use four physicochemical parameters as input variables.

| Parameter | Description | Unit |
|:---|:---|:---|
| Initial Fluoride Concentration | Initial concentration of fluoride in the aqueous solution | mg/L |
| pH | Acidity or alkalinity of the solution | - |
| Adsorbent Dose | Quantity of adsorbent used during treatment | g/100 mL |
| Contact Time | Duration of interaction between adsorbent and fluoride solution | min |

### Target Variable

**Result (%) – Fluoride Removal Efficiency**

The target variable represents the percentage of fluoride removed from the aqueous solution.

### Dataset Split

| Dataset | Percentage | Number of Observations |
|:---|:---:|---:|
| Training Set | 80% | 18,480 |
| Testing Set | 20% | 4,620 |
| **Total** | **100%** | **23,100** |

The training dataset is used to develop and optimize the models, while the testing dataset is reserved for evaluating their predictive performance.

---

## ⚙️ 3. Machine Learning Workflow

The project follows a systematic machine learning pipeline.

```text
          📁 Experimental Dataset
                    |
                    ▼
             Data Loading
                    |
                    ▼
           Data Preprocessing
                    |
                    ▼
          Train-Test Splitting
              (80:20)
                    |
                    ▼
          Feature Standardization
             StandardScaler
                    |
                    ▼
          Machine Learning Models
                    |
          ┌─────────┼──────────┐
          ▼         ▼          ▼
         SVR      XGBoost    Random Forest
          │         │          │
          └─────────┼──────────┘
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
    Gradient Boosting     Ridge Regression
          │                    │
          └─────────┬──────────┘
                    ▼
          Hyperparameter Tuning
              GridSearchCV
           (5-Fold CV)
                    |
                    ▼
            Model Evaluation
                    |
                    ▼
          Performance Comparison
                    |
                    ▼
          Prediction & Analysis
```

### Key Processing Steps

**1. Data Preprocessing**

Loads the experimental dataset and prepares the input features and target variable.

**2. Train-Test Splitting**

Divides the dataset into 80% training data and 20% testing data.

**3. Feature Standardization**

Uses `StandardScaler` to standardize input features where appropriate.

**4. Model Development**

Trains five different regression algorithms to learn the relationship between experimental conditions and fluoride removal efficiency.

**5. Hyperparameter Optimization**

Uses `GridSearchCV` with 5-fold cross-validation to identify suitable model configurations.

**6. Model Evaluation**

Compares the optimized models using R² Score, RMSE, and MAE.

---

## 🤖 4. Machine Learning Algorithms

Five regression algorithms are implemented and compared.

### 1. Support Vector Regression (SVR)

SVR is a supervised machine learning algorithm that predicts continuous numerical values.

The RBF (Radial Basis Function) kernel is used to capture nonlinear relationships between experimental parameters and fluoride removal efficiency.

### 2. XGBoost Regressor

XGBoost (Extreme Gradient Boosting) is an ensemble learning algorithm based on gradient-boosted decision trees.

It builds trees sequentially, with each new tree helping to correct errors made by previous trees.

### 3. Random Forest Regressor

Random Forest combines multiple decision trees to generate predictions.

It reduces the influence of individual tree errors by averaging predictions from multiple trees.

### 4. Gradient Boosting Regressor

Gradient Boosting develops an ensemble of decision trees sequentially, where each successive tree attempts to improve the predictions of the existing model.

### 5. Ridge Regression

Ridge Regression is a linear regression technique that uses L2 regularization to reduce overfitting and control model complexity.

It provides a useful linear baseline for comparison with nonlinear algorithms.

---

## 🔍 5. Hyperparameter Optimization

Model optimization is performed using:

**GridSearchCV with 5-Fold Cross-Validation**

GridSearchCV systematically evaluates different combinations of hyperparameters to identify the best-performing configuration according to the selected cross-validation scoring metric.

### What is 5-Fold Cross-Validation?

The training dataset is divided into five approximately equal parts.

- Four parts are used for training.
- One part is used for validation.
- This process is repeated five times, with a different validation fold each time.

The validation scores are then combined to assess each hyperparameter configuration.

This helps reduce dependence on a single validation split.

### Why use StandardScaler?

Experimental variables have different numerical scales.

For example:

- Fluoride concentration may be measured in tens or hundreds of mg/L.
- pH typically ranges from 0 to 14.
- Contact time may range from minutes to hours.

StandardScaler transforms numerical features to a common scale.

When implemented inside a Scikit-learn Pipeline, scaling is fitted independently within each training fold, helping prevent data leakage during cross-validation.

---

## 📊 6. Model Performance Benchmark

All five models were evaluated using the same training-testing split.

The following table summarizes their reported performance.

| Model | Train R² | Test R² | Test RMSE | Test MAE |
|:---|---:|---:|---:|---:|
| **SVR** | **1.0000** | **1.0000** | **0.0140** | **0.0077** |
| **XGBoost** | 0.9998 | 0.9997 | 0.3441 | 0.2613 |
| **Random Forest** | 0.9999 | 0.9996 | 0.3990 | 0.2718 |
| **Gradient Boosting** | 0.9996 | 0.9995 | 0.4560 | 0.3429 |
| **Ridge Regression** | 0.8258 | 0.8148 | 8.7795 | 6.7863 |

### 🏆 Key Findings

- **SVR** achieved the best reported performance, with a test R² score of 1.0000.
- XGBoost achieved a test R² score of 0.9997.
- Random Forest achieved a test R² score of 0.9996.
- Gradient Boosting achieved a test R² score of 0.9995.
- Ridge Regression achieved a comparatively lower test R² score of 0.8148.

The nonlinear regression algorithms demonstrated substantially better predictive performance than the linear Ridge Regression model on this dataset.

**Important:** The exceptionally high SVR score should be interpreted carefully. Before drawing conclusions about generalization, check for duplicate or highly similar experimental observations across the train-test split, possible data leakage, and independent experimental validation.

---

## 📈 7. Visualizations and Results

The project includes graphical visualizations to help interpret model performance and prediction accuracy.

### Model Comparison

**File:** `model_comparison.png`

Provides a comparative overview of the performance of all five regression algorithms.

### Prediction and Error Analysis

**File:** `Figure_1.png`

Contains parity and error distribution plots for evaluating the relationship between actual and predicted values.

### Additional Prediction Results

**File:** `all_model_predictions.csv`

Contains the model predictions and corresponding error residuals on the test dataset.

These outputs help assess prediction accuracy and compare the behavior of different regression algorithms.

---

## 📂 8. Repository Structure

```text
Enhanced-Fluoride-Removal-By-Machine-Learning-Approach/
│
├── 📁 extras/
│   └── Experimental plans, methodology documents
│       and supporting literature.
│
├── 📄 data.csv
│   └── Experimental adsorption dataset (23,100 rows).
│
├── 📓 fluride.ipynb
│   └── Main Jupyter Notebook containing data
│       preprocessing, model development and evaluation.
│
├── 📄 convert_xl_to_csv.py
│   └── Converts experimental Excel files into CSV.
│
├── 📊 model_comparison.png
│   └── Comparative model performance visualization.
│
├── 📊 Figure_1.png
│   └── Parity and error distribution plots.
│
├── 📄 all_model_predictions.csv
│   └── Predictions and error residuals for all models.
│
├── 📄 requirements.txt
│   └── Required Python dependencies.
│
├── 📄 .gitignore
│   └── Excludes unnecessary files from version control.
│
└── 📄 README.md
    └── Project documentation.
```

---


# 🚀 9. Installation and Setup – Google Colab

### STEP 1 – Open Google Colab
Visit https://colab.research.google.com/ and sign in using your Google account.

### STEP 2 – Open the Project Notebook
Open the GitHub repository, select `fluride.ipynb`, and open it in Google Colab using File → Open notebook → GitHub.

### STEP 3 – Upload the Dataset
Click the Files icon on the left sidebar and upload `data.csv` from your downloaded project folder.

### STEP 4 – Install Dependencies
Create a code cell and execute:

```python
!pip install pandas numpy scikit-learn xgboost matplotlib openpyxl
```

### STEP 5 – Run the Notebook
Click **Runtime → Run all** to execute the complete machine learning workflow, including preprocessing, model training, optimization, and evaluation.

### STEP 6 – Download the Results
From the Files panel, download the generated `model_comparison.png`, `Figure_1.png`, and `all_model_predictions.csv` files to your computer.

**Note:** Google Colab uses a temporary cloud environment. Download important files before the session ends.

---

# 🛠️ 10. Troubleshooting – Common Errors

| Error | Solution |
|:---|:---|
| FileNotFoundError | Upload `data.csv` and verify its file path. |
| No module named pandas/xgboost | Run the dependency installation command again. |
| Runtime Disconnected | Reconnect and rerun the notebook cells. |
| NameError | Execute the notebook cells from the beginning. |
| Slow Execution | Allow GridSearchCV sufficient time to complete. |
| Excel File Error | Upload the Excel file and install `openpyxl`. |

### 🎉 Ready to Get Started!

Open Google Colab, upload the dataset, run the notebook, and explore machine learning-based fluoride removal predictions!

**No complicated installation. Just upload, run, and explore!** 🔬


## 🧰 11. Technologies and Libraries

| Technology | Application |
|:---|:---|
| Python | Programming language |
| Pandas | Dataset processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and evaluation |
| XGBoost | Gradient boosting algorithm |
| Matplotlib | Visualization |
| Jupyter Notebook | Interactive development |

---

## 🔬 12. Scientific Significance

This project demonstrates how machine learning can be applied to environmental engineering and water treatment research.

By learning relationships between operating conditions and fluoride removal efficiency, regression models can support:

- Analysis of adsorption behavior.
- Prediction of fluoride removal efficiency.
- Comparison of different modeling approaches.
- Identification of potentially suitable operating conditions.
- Further investigation of adsorption process optimization.

**Research consideration:** Machine learning predictions are computational estimates based on the available experimental data. They should be validated against independent experimental observations before being used to make practical treatment decisions.

---

## 📚 13. Citation and Acknowledgments

If you use this project, its methodology, or dataset in your research or academic work, please acknowledge this repository.

**GitHub Repository:**

https://github.com/ShreeyaHM/Enhanced-Fluoride-Removal-By-Machine-Learning-Approach

For formal academic citation, use the repository's publication or DOI information if one is available.

---

## ⭐ 14. Final Note

Thank you for exploring the **Enhanced Fluoride Removal by Machine Learning Approach** project!

This repository aims to make machine learning applications in environmental science more accessible to researchers, students, and beginners.

**Explore. Experiment. Predict. Improve.** 🔬

---
