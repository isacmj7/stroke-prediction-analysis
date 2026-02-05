"""
Visualizations for stroke prediction analysis.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Set style (compatible with different matplotlib versions)
try:
    plt.style.use('seaborn-v0_8-whitegrid')
except OSError:
    try:
        plt.style.use('seaborn-whitegrid')
    except OSError:
        pass  # Use default style if seaborn styles not available

try:
    sns.set_palette("husl")
except Exception:
    pass  # Use default palette if seaborn not configured properly


def save_fig(fig, filename, output_dir=None):
    """Save figure to file."""
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "visualizations"
    else:
        output_dir = Path(output_dir)
    
    output_dir.mkdir(exist_ok=True)
    filepath = output_dir / filename
    fig.savefig(filepath, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Saved: {filepath}")
    plt.close(fig)


def plot_stroke_distribution(df):
    """Plot stroke case distribution."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    stroke_counts = df['stroke'].value_counts()
    labels = ['No Stroke', 'Stroke']
    colors = ['#2ecc71', '#e74c3c']
    
    bars = ax.bar(labels, stroke_counts.values, color=colors, edgecolor='black')
    
    for bar, count in zip(bars, stroke_counts.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                f'{count:,}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_title('Distribution of Stroke Cases', fontsize=14, fontweight='bold')
    ax.set_ylabel('Number of Patients', fontsize=12)
    ax.set_xlabel('Stroke Status', fontsize=12)
    
    save_fig(fig, '01_stroke_distribution.png')


def plot_age_distribution(df):
    """Plot age distribution by stroke status."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    stroke_no = df[df['stroke'] == 0]['age']
    stroke_yes = df[df['stroke'] == 1]['age']
    
    ax.hist(stroke_no, bins=30, alpha=0.6, label='No Stroke', color='#2ecc71')
    ax.hist(stroke_yes, bins=30, alpha=0.6, label='Stroke', color='#e74c3c')
    
    ax.set_title('Age Distribution by Stroke Status', fontsize=14, fontweight='bold')
    ax.set_xlabel('Age', fontsize=12)
    ax.set_ylabel('Number of Patients', fontsize=12)
    ax.legend()
    
    save_fig(fig, '02_age_distribution.png')


def plot_age_group_stroke_rate(df, age_column='age_group'):
    """Plot stroke rate by age group."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    age_stats = df.groupby(age_column)['stroke'].agg(['sum', 'count']).reset_index()
    age_stats['stroke_rate'] = age_stats['sum'] / age_stats['count'] * 100
    
    bars = ax.bar(age_stats[age_column].astype(str), age_stats['stroke_rate'], 
                  color='#3498db', edgecolor='black')
    
    for bar, rate in zip(bars, age_stats['stroke_rate']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                f'{rate:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_title('Stroke Rate by Age Group', fontsize=14, fontweight='bold')
    ax.set_xlabel('Age Group', fontsize=12)
    ax.set_ylabel('Stroke Rate (%)', fontsize=12)
    
    save_fig(fig, '03_age_group_stroke_rate.png')


def plot_gender_analysis(df):
    """Plot stroke analysis by gender."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gender distribution
    gender_counts = df['gender'].value_counts()
    axes[0].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
                colors=['#3498db', '#e74c3c'], startangle=90)
    axes[0].set_title('Gender Distribution', fontsize=12, fontweight='bold')
    
    # Stroke rate by gender
    gender_stroke = df.groupby('gender')['stroke'].agg(['sum', 'count']).reset_index()
    gender_stroke['stroke_rate'] = gender_stroke['sum'] / gender_stroke['count'] * 100
    
    bars = axes[1].bar(gender_stroke['gender'], gender_stroke['stroke_rate'],
                       color=['#3498db', '#e74c3c'], edgecolor='black')
    
    for bar, rate in zip(bars, gender_stroke['stroke_rate']):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                     f'{rate:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    axes[1].set_title('Stroke Rate by Gender', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Gender', fontsize=11)
    axes[1].set_ylabel('Stroke Rate (%)', fontsize=11)
    
    plt.tight_layout()
    save_fig(fig, '04_gender_analysis.png')


def plot_medical_conditions(df):
    """Plot stroke rate by medical conditions."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Hypertension
    hyper_stats = df.groupby('hypertension')['stroke'].agg(['sum', 'count']).reset_index()
    hyper_stats['stroke_rate'] = hyper_stats['sum'] / hyper_stats['count'] * 100
    
    labels = ['No Hypertension', 'Hypertension']
    bars1 = axes[0].bar(labels, hyper_stats['stroke_rate'], color=['#2ecc71', '#e74c3c'], edgecolor='black')
    
    for bar, rate in zip(bars1, hyper_stats['stroke_rate']):
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                     f'{rate:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    axes[0].set_title('Stroke Rate by Hypertension Status', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Stroke Rate (%)', fontsize=11)
    
    # Heart Disease
    heart_stats = df.groupby('heart_disease')['stroke'].agg(['sum', 'count']).reset_index()
    heart_stats['stroke_rate'] = heart_stats['sum'] / heart_stats['count'] * 100
    
    labels = ['No Heart Disease', 'Heart Disease']
    bars2 = axes[1].bar(labels, heart_stats['stroke_rate'], color=['#2ecc71', '#e74c3c'], edgecolor='black')
    
    for bar, rate in zip(bars2, heart_stats['stroke_rate']):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                     f'{rate:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    axes[1].set_title('Stroke Rate by Heart Disease Status', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Stroke Rate (%)', fontsize=11)
    
    plt.tight_layout()
    save_fig(fig, '05_medical_conditions.png')


def plot_smoking_analysis(df):
    """Plot stroke rate by smoking status."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    smoking_stats = df.groupby('smoking_status')['stroke'].agg(['sum', 'count']).reset_index()
    smoking_stats['stroke_rate'] = smoking_stats['sum'] / smoking_stats['count'] * 100
    smoking_stats = smoking_stats.sort_values('stroke_rate', ascending=False)
    
    colors = ['#e74c3c', '#f39c12', '#3498db', '#95a5a6']
    bars = ax.barh(smoking_stats['smoking_status'], smoking_stats['stroke_rate'], color=colors, edgecolor='black')
    
    for bar, rate in zip(bars, smoking_stats['stroke_rate']):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'{rate:.2f}%', ha='left', va='center', fontsize=10, fontweight='bold')
    
    ax.set_title('Stroke Rate by Smoking Status', fontsize=14, fontweight='bold')
    ax.set_xlabel('Stroke Rate (%)', fontsize=12)
    ax.set_ylabel('Smoking Status', fontsize=12)
    
    save_fig(fig, '06_smoking_analysis.png')


def plot_bmi_analysis(df, bmi_column='bmi_category'):
    """Plot stroke rate by BMI category."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bmi_order = ['Underweight', 'Normal', 'Overweight', 'Obese']
    df_bmi = df[df[bmi_column].isin(bmi_order)]
    
    bmi_stats = df_bmi.groupby(bmi_column)['stroke'].agg(['sum', 'count']).reset_index()
    bmi_stats['stroke_rate'] = bmi_stats['sum'] / bmi_stats['count'] * 100
    
    # Sort by BMI order
    bmi_stats[bmi_column] = pd.Categorical(bmi_stats[bmi_column], categories=bmi_order, ordered=True)
    bmi_stats = bmi_stats.sort_values(bmi_column)
    
    colors = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c']
    bars = ax.bar(bmi_stats[bmi_column], bmi_stats['stroke_rate'], color=colors, edgecolor='black')
    
    for bar, rate in zip(bars, bmi_stats['stroke_rate']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{rate:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_title('Stroke Rate by BMI Category', fontsize=14, fontweight='bold')
    ax.set_xlabel('BMI Category', fontsize=12)
    ax.set_ylabel('Stroke Rate (%)', fontsize=12)
    
    save_fig(fig, '07_bmi_analysis.png')


def plot_glucose_analysis(df, glucose_column='glucose_category'):
    """Plot stroke rate by glucose category."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    glucose_order = ['Normal', 'Pre-diabetic', 'Diabetic']
    df_glucose = df[df[glucose_column].isin(glucose_order)]
    
    glucose_stats = df_glucose.groupby(glucose_column)['stroke'].agg(['sum', 'count']).reset_index()
    glucose_stats['stroke_rate'] = glucose_stats['sum'] / glucose_stats['count'] * 100
    
    # Sort by glucose order
    glucose_stats[glucose_column] = pd.Categorical(glucose_stats[glucose_column], categories=glucose_order, ordered=True)
    glucose_stats = glucose_stats.sort_values(glucose_column)
    
    colors = ['#2ecc71', '#f39c12', '#e74c3c']
    bars = ax.bar(glucose_stats[glucose_column], glucose_stats['stroke_rate'], color=colors, edgecolor='black')
    
    for bar, rate in zip(bars, glucose_stats['stroke_rate']):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f'{rate:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_title('Stroke Rate by Glucose Level Category', fontsize=14, fontweight='bold')
    ax.set_xlabel('Glucose Category', fontsize=12)
    ax.set_ylabel('Stroke Rate (%)', fontsize=12)
    
    save_fig(fig, '08_glucose_analysis.png')


def plot_work_type_analysis(df):
    """Plot stroke rate by work type."""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    work_stats = df.groupby('work_type')['stroke'].agg(['sum', 'count']).reset_index()
    work_stats['stroke_rate'] = work_stats['sum'] / work_stats['count'] * 100
    work_stats = work_stats.sort_values('stroke_rate', ascending=True)
    
    colors = sns.color_palette("RdYlGn_r", len(work_stats))
    bars = ax.barh(work_stats['work_type'], work_stats['stroke_rate'], color=colors, edgecolor='black')
    
    for bar, rate in zip(bars, work_stats['stroke_rate']):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'{rate:.2f}%', ha='left', va='center', fontsize=10, fontweight='bold')
    
    ax.set_title('Stroke Rate by Work Type', fontsize=14, fontweight='bold')
    ax.set_xlabel('Stroke Rate (%)', fontsize=12)
    ax.set_ylabel('Work Type', fontsize=12)
    
    save_fig(fig, '09_work_type_analysis.png')


def plot_residence_analysis(df):
    """Plot stroke rate by residence type."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Residence distribution
    residence_counts = df['Residence_type'].value_counts()
    axes[0].pie(residence_counts, labels=residence_counts.index, autopct='%1.1f%%',
                colors=['#3498db', '#2ecc71'], startangle=90)
    axes[0].set_title('Residence Type Distribution', fontsize=12, fontweight='bold')
    
    # Stroke rate by residence
    residence_stroke = df.groupby('Residence_type')['stroke'].agg(['sum', 'count']).reset_index()
    residence_stroke['stroke_rate'] = residence_stroke['sum'] / residence_stroke['count'] * 100
    
    bars = axes[1].bar(residence_stroke['Residence_type'], residence_stroke['stroke_rate'],
                       color=['#3498db', '#2ecc71'], edgecolor='black')
    
    for bar, rate in zip(bars, residence_stroke['stroke_rate']):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                     f'{rate:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    axes[1].set_title('Stroke Rate by Residence Type', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Residence Type', fontsize=11)
    axes[1].set_ylabel('Stroke Rate (%)', fontsize=11)
    
    plt.tight_layout()
    save_fig(fig, '10_residence_analysis.png')


def plot_correlation_heatmap(df):
    """Plot correlation heatmap of numeric features."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Select numeric columns
    numeric_cols = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'stroke']
    df_numeric = df[numeric_cols].copy()
    
    # Calculate correlation
    corr = df_numeric.corr()
    
    # Plot heatmap
    sns.heatmap(corr, annot=True, cmap='RdYlBu_r', center=0,
                fmt='.2f', linewidths=0.5, ax=ax)
    
    ax.set_title('Correlation Heatmap of Features', fontsize=14, fontweight='bold')
    
    save_fig(fig, '11_correlation_heatmap.png')


def create_all_visualizations(df):
    """Generate all visualizations."""
    print("Creating visualizations...")
    
    plot_stroke_distribution(df)
    plot_age_distribution(df)
    
    # Check if age_group column exists
    if 'age_group' in df.columns:
        plot_age_group_stroke_rate(df)
    
    plot_gender_analysis(df)
    plot_medical_conditions(df)
    plot_smoking_analysis(df)
    
    # Check if bmi_category column exists
    if 'bmi_category' in df.columns:
        plot_bmi_analysis(df)
    
    # Check if glucose_category column exists
    if 'glucose_category' in df.columns:
        plot_glucose_analysis(df)
    
    plot_work_type_analysis(df)
    plot_residence_analysis(df)
    plot_correlation_heatmap(df)
    
    print("All visualizations created!")


if __name__ == "__main__":
    from data_processing import load_stroke_data, clean_stroke_data, get_age_groups, get_bmi_category, get_glucose_category
    
    df = load_stroke_data()
    df_clean = clean_stroke_data(df)
    df_clean = get_age_groups(df_clean)
    df_clean = get_bmi_category(df_clean)
    df_clean = get_glucose_category(df_clean)
    
    create_all_visualizations(df_clean)
