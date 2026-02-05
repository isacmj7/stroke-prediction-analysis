"""
Data processing for stroke prediction analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path


def load_stroke_data(filepath=None):
    """Load the stroke dataset."""
    if filepath is None:
        project_root = Path(__file__).parent.parent
        filepath = project_root / "data" / "healthcare-dataset-stroke-data.csv"
    
    df = pd.read_csv(filepath)
    print(f"Loaded stroke data: {len(df)} rows, {len(df.columns)} columns")
    return df


def clean_stroke_data(df):
    """Clean and preprocess the stroke data."""
    df_clean = df.copy()
    
    # Handle BMI missing values (marked as 'N/A')
    df_clean['bmi'] = pd.to_numeric(df_clean['bmi'], errors='coerce')
    
    # Fill missing BMI with median
    bmi_median = df_clean['bmi'].median()
    df_clean['bmi'] = df_clean['bmi'].fillna(bmi_median)
    
    # Remove 'Other' gender (only 1 record)
    df_clean = df_clean[df_clean['gender'] != 'Other']
    
    print(f"Cleaned data: {len(df_clean)} rows")
    return df_clean


def get_age_groups(df):
    """Create age groups for analysis."""
    df_copy = df.copy()
    
    bins = [0, 18, 30, 45, 60, 75, 100]
    labels = ['0-18', '19-30', '31-45', '46-60', '61-75', '75+']
    
    df_copy['age_group'] = pd.cut(df_copy['age'], bins=bins, labels=labels, include_lowest=True)
    return df_copy


def get_bmi_category(df):
    """Create BMI categories."""
    df_copy = df.copy()
    
    def categorize_bmi(bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Normal'
        elif bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'
    
    df_copy['bmi_category'] = df_copy['bmi'].apply(categorize_bmi)
    return df_copy


def get_glucose_category(df):
    """Create glucose level categories."""
    df_copy = df.copy()
    
    def categorize_glucose(glucose):
        if glucose < 100:
            return 'Normal'
        elif glucose < 126:
            return 'Pre-diabetic'
        else:
            return 'Diabetic'
    
    df_copy['glucose_category'] = df_copy['avg_glucose_level'].apply(categorize_glucose)
    return df_copy


def get_stroke_stats(df):
    """Calculate basic stroke statistics."""
    total = len(df)
    stroke_cases = df['stroke'].sum()
    no_stroke = total - stroke_cases
    
    return {
        'total_patients': total,
        'stroke_cases': int(stroke_cases),
        'no_stroke_cases': int(no_stroke),
        'stroke_rate': round(stroke_cases / total * 100, 2)
    }


def get_stats_by_column(df, column):
    """Get stroke statistics grouped by a column."""
    grouped = df.groupby(column).agg({
        'stroke': ['sum', 'count']
    }).reset_index()
    
    grouped.columns = [column, 'stroke_count', 'total_count']
    grouped['no_stroke_count'] = grouped['total_count'] - grouped['stroke_count']
    grouped['stroke_rate'] = round(grouped['stroke_count'] / grouped['total_count'] * 100, 2)
    
    return grouped


def get_risk_factor_summary(df):
    """Summarize stroke rates by risk factors."""
    summary = {}
    
    # Hypertension
    hypertension_stats = get_stats_by_column(df, 'hypertension')
    summary['hypertension'] = hypertension_stats
    
    # Heart disease
    heart_stats = get_stats_by_column(df, 'heart_disease')
    summary['heart_disease'] = heart_stats
    
    # Smoking
    smoking_stats = get_stats_by_column(df, 'smoking_status')
    summary['smoking'] = smoking_stats
    
    return summary


def export_for_tableau(df, output_dir=None):
    """Export processed data for Tableau visualization."""
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "tableau"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(exist_ok=True)
    
    # Add categories
    df_export = get_age_groups(df)
    df_export = get_bmi_category(df_export)
    df_export = get_glucose_category(df_export)
    
    # Main data export
    df_export.to_csv(output_dir / "stroke_data_tableau.csv", index=False)
    
    # Age group summary
    age_summary = get_stats_by_column(df_export, 'age_group')
    age_summary.to_csv(output_dir / "age_group_tableau.csv", index=False)
    
    # Gender summary
    gender_summary = get_stats_by_column(df, 'gender')
    gender_summary.to_csv(output_dir / "gender_tableau.csv", index=False)
    
    # Hypertension summary
    hyper_summary = get_stats_by_column(df, 'hypertension')
    hyper_summary.to_csv(output_dir / "hypertension_tableau.csv", index=False)
    
    # Heart disease summary
    heart_summary = get_stats_by_column(df, 'heart_disease')
    heart_summary.to_csv(output_dir / "heart_disease_tableau.csv", index=False)
    
    # Smoking summary
    smoking_summary = get_stats_by_column(df, 'smoking_status')
    smoking_summary.to_csv(output_dir / "smoking_tableau.csv", index=False)
    
    # Work type summary
    work_summary = get_stats_by_column(df, 'work_type')
    work_summary.to_csv(output_dir / "work_type_tableau.csv", index=False)
    
    # Residence summary
    residence_summary = get_stats_by_column(df, 'Residence_type')
    residence_summary.to_csv(output_dir / "residence_tableau.csv", index=False)
    
    # BMI category summary
    bmi_summary = get_stats_by_column(df_export, 'bmi_category')
    bmi_summary.to_csv(output_dir / "bmi_category_tableau.csv", index=False)
    
    # Glucose category summary
    glucose_summary = get_stats_by_column(df_export, 'glucose_category')
    glucose_summary.to_csv(output_dir / "glucose_category_tableau.csv", index=False)
    
    print(f"Exported {10} files to {output_dir}")


if __name__ == "__main__":
    df = load_stroke_data()
    df_clean = clean_stroke_data(df)
    
    stats = get_stroke_stats(df_clean)
    print(f"\nStroke Statistics: {stats}")
