# Stroke Prediction Analysis (India)

**Ishak Islam** | UMID28072552431 | Unified Mentor Internship

## About

Analysis of stroke risk factors and prediction patterns using healthcare data. This project explores patient demographics, medical history, and lifestyle factors that contribute to stroke occurrence. The dataset contains clinical and lifestyle data from patients, enabling comprehensive analysis of stroke risk factors in the Indian context.

## How to Run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_stroke_prediction_analysis.ipynb
```

Run all cells to see the analysis.

## Dataset

Download from: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

Place the downloaded CSV file in the `data/` folder:
- `healthcare-dataset-stroke-data.csv` - Patient health and lifestyle data

## Files

```
├── data/           # Put dataset file here
├── notebooks/      # Analysis notebook
├── scripts/        # Helper functions
├── visualizations/ # Charts
├── tableau/        # Tableau exports
└── docs/           # Documentation
```

## Results

- Age distribution analysis and stroke correlation
- Analysis of medical conditions (hypertension, heart disease)
- Lifestyle factors impact (smoking, BMI, glucose levels)
- Gender and marital status patterns
- Work type and residence analysis
- Data exports ready for Tableau dashboards

## Tableau Dashboard

**Live Interactive Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/ishak.islam/viz/StrokePredictionAnalysisIndia/Dashboard?publish=yes)

## Tech Stack

Python, Pandas, NumPy, Matplotlib, Seaborn, Tableau

## GitHub Repository

**Source Code:** [https://github.com/isacmj7/stroke-prediction-analysis](https://github.com/isacmj7/stroke-prediction-analysis)
