# Data Download Instructions

## Dataset Source

**Kaggle Stroke Prediction Dataset**

Download URL: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

## How to Download

1. Go to the Kaggle dataset page
2. Click "Download" button (requires Kaggle account)
3. Extract the ZIP file
4. Copy `healthcare-dataset-stroke-data.csv` to this folder

## Required File

| Filename | Description |
|----------|-------------|
| healthcare-dataset-stroke-data.csv | Patient health and stroke data |

## Dataset Information

- **Records:** 5,110 patients
- **Features:** 12 columns
- **Target:** stroke (0 = No, 1 = Yes)

## Features Description

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Patient identifier |
| gender | String | Male, Female, Other |
| age | Float | Patient age |
| hypertension | Integer | 0 = No, 1 = Yes |
| heart_disease | Integer | 0 = No, 1 = Yes |
| ever_married | String | Yes, No |
| work_type | String | children, Govt_job, Never_worked, Private, Self-employed |
| Residence_type | String | Rural, Urban |
| avg_glucose_level | Float | Average glucose level in blood |
| bmi | Float | Body Mass Index |
| smoking_status | String | formerly smoked, never smoked, smokes, Unknown |
| stroke | Integer | 0 = No stroke, 1 = Had stroke |

## Notes

- BMI column has some missing values (marked as "N/A")
- Dataset is imbalanced (more non-stroke cases)
- All data is anonymized
