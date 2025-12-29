import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 1. Setup the Data
data = {
    'Pair': [f'P{i}' for i in range(1, 12)],
    'Name': [
        'Burnout/Depr', 'Phono/Letter', 'Hyper/Sleep', 'Efficacy/Partic', 'Motiv/Score',
        'FASD-GenEF', 'FASD-Behav', 'FASD-Emot', 'FASD-Audit', 'FASD-Inhib', 'FASD-Shift'
    ],
    'Meta_g': [0.90, 0.11, -0.46, 0.93, 0.82, 0.21, 0.18, 0.01, 0.06, 0.04, 0.04],
    'ANM_Score': [0.5049, 0.00, 0.00, 0.88, 0.00, 0.03, 0.03, 0.04, 0.17, 0.12, 0.27],
    'IGCI_Score': [-0.08, -0.70, 0.98, 1.85, 2.02, -0.22, -0.14, -0.18, -0.49, -0.34, -0.15],
}

df = pd.DataFrame(data)

# --- Pre-processing for Scaling and Correct Plotting ---
df['Abs_g'] = df['Meta_g'].abs()
# Normalize IGCI to 0-1 scale for visual comparison
df['Abs_IGCI_Scaled'] = df['IGCI_Score'].abs() / df['IGCI_Score'].abs().max()

# Set global visual style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 11, 'figure.autolayout': True})

# =================================================================
# PLOT 1: Meta-Analytic Ground Truth (The "Input" Data)
# =================================================================
plt.figure(figsize=(12, 6))
# Color points by magnitude
colors = ['#e74c3c' if abs(x) > 0.5 else '#3498db' for x in df['Meta_g']]

plt.hlines(y=df['Name'], xmin=0, xmax=df['Meta_g'], color='gray', alpha=0.3, linewidth=1)
plt.scatter(df['Meta_g'], df['Name'], s=150, color=colors, edgecolors='white', zorder=3)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1.2)

plt.title('Figure 1: Meta-Analytic Ground Truth Effect Sizes (Hedges\' g)', fontsize=15, weight='bold', pad=20)
plt.xlabel('Standardized Effect Size (g)', fontsize=12)
plt.ylabel('Causal Relationship Pair', fontsize=12)
plt.show()

# =================================================================
# PLOT 2: Algorithmic Confidence Comparison (ANM vs IGCI)
# =================================================================
# Reshape data for a grouped bar chart
comparison_df = df.melt(id_vars='Name', value_vars=['ANM_Score', 'Abs_IGCI_Scaled'],
                        var_name='Algorithm', value_name='Confidence')
comparison_df['Algorithm'] = comparison_df['Algorithm'].replace(
    {'ANM_Score': 'ANM (Normalized)', 'Abs_IGCI_Scaled': 'IGCI (Scaled)'})

plt.figure(figsize=(12, 7))
sns.barplot(data=comparison_df, x='Confidence', y='Name', hue='Algorithm', palette='muted')

plt.title('Figure 2: Algorithmic Confidence Comparison', fontsize=15, weight='bold', pad=20)
plt.xlabel('Inference Confidence / Magnitude (0.0 - 1.0)', fontsize=12)
plt.ylabel('')
plt.legend(loc='lower right', frameon=True)
plt.show()

# =================================================================
# PLOT 3: Magnitude Concordance (The "Validation" Plot)
# =================================================================
plt.figure(figsize=(14, 9))  # Wider format for readable labels

# Regression plot
sns.regplot(
    x='Abs_g',
    y='Abs_IGCI_Scaled',
    data=df,
    scatter_kws={'s': 200, 'alpha': 0.6, 'color': '#2ecc71', 'edgecolor': 'white'},
    line_kws={'color': '#27ae60', 'lw': 3, 'label': 'IGCI Magnitude Trend'},
    ci=None
)

# Manual label positioning logic to avoid edges and overlapping
for i, txt in enumerate(df['Name']):
    # Base offsets
    x_offset = 12 if df['Abs_g'][i] < 0.8 else -100
    y_offset = 5

    # --- MANUAL JITTER FOR OVERLAPPING NAMES ---
    if txt == 'FASD-Inhib':
        y_offset = -18  # Move down
    elif txt == 'FASD-Shift':
        y_offset = 15  # Move up
        x_offset = -60  # Move significantly to the left
    elif txt == 'FASD-Emot':
        y_offset = -30  # Move down
        x_offset = -10
    elif txt == 'FASD-Audit':
        y_offset = 12  # Move up

    plt.annotate(
        txt,
        (df['Abs_g'][i], df['Abs_IGCI_Scaled'][i]),
        xytext=(x_offset, y_offset),
        textcoords='offset points',
        fontsize=9,
        weight='bold',
        color='#2c3e50',
        alpha=0.9
    )

plt.title('Figure 3: Magnitude Concordance\n(Experimental Effect Size vs. Algorithmic Confidence)',
          fontsize=16, weight='bold', pad=25)
plt.xlabel('Ground Truth Effect Magnitude (|g|)', fontsize=13, labelpad=12)
plt.ylabel('Normalized IGCI Magnitude (0.0 - 1.0)', fontsize=13, labelpad=12)

# Set axes limits with padding for text
plt.xlim(-0.05, 1.2)
plt.ylim(-0.1, 1.1)

plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()