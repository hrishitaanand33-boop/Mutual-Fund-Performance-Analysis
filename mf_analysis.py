import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('top_30_mutual_funds.csv')
print(df.head())
print(df.describe())
print(df['category'].unique())

print(df.isnull().sum())

mean_returns_3yr = df['returns_3yr'].mean()
mean_returns_5yr = df['returns_5yr'].mean()
df['returns_3yr'].fillna(mean_returns_3yr, inplace=True)
df['returns_5yr'].fillna(mean_returns_5yr, inplace=True)
print(df.isnull().sum())
print(mean_returns_3yr, mean_returns_5yr)

columns_to_normalize = ['expense_ratio', 'returns_1yr', 'returns_3yr', 'returns_5yr', 
                        'sharpe', 'sortino', 'alpha', 'beta']
df[columns_to_normalize] = df[columns_to_normalize].replace('-', pd.NA).apply(pd.to_numeric)

scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df[columns_to_normalize]), columns=columns_to_normalize)

# Adjust metrics where lower is better
df_normalized['expense_ratio'] = 1 - df_normalized['expense_ratio']
df_normalized['beta'] = 1 - df_normalized['beta']
print(df_normalized)

weights = {
    'expense_ratio': 0.2,
    'returns_1yr': 0.15,
    'returns_3yr': 0.15,
    'returns_5yr': 0.15,
    'sharpe': 0.1,
    'sortino': 0.1,
    'alpha': 0.1,
    'beta': 0.05
}

df_normalized['composite_score'] = sum(
    df_normalized[col] * weight for col, weight in weights.items()
)
df['composite_score'] = df_normalized['composite_score']

df['rank'] = df['composite_score'].rank(ascending=False)
df_sorted = df.sort_values(by='rank')
print(df_sorted)

df_top_30 = df_sorted.head(30)
df_top_30.to_csv('top_30_mutual_funds.csv', index=False)
print(df.columns.tolist())
print("Exported top 30 mutual funds to 'top_30_mutual_funds.csv'.")

# Plot 1: Top 10 Mutual Funds by Composite Score
top10 = df_sorted.head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x='composite_score', y='scheme_name', data=top10)
plt.title('Top 10 Mutual Funds by Composite Score')
plt.xlabel('Composite Score')
plt.ylabel('Fund Name')
plt.tight_layout()
plt.savefig('plot_top10_composite_score.png', dpi=300)
plt.show()

# Plot 2: Expense Ratio vs 5Y Returns by Category
plt.figure(figsize=(10, 6))
sns.scatterplot(x='expense_ratio', y='returns_5yr', hue='category', data=df_sorted)
plt.title('Expense Ratio vs 5Y Returns by Category')
plt.xlabel('Expense Ratio (in %)')
plt.ylabel('5-Year Returns (in %)')
plt.tight_layout()
plt.savefig('plot_expense_vs_returns5yr.png', dpi=300)
plt.show()

# Plot 3: Correlation Matrix of Performance Metrics
plt.figure(figsize=(10, 6))
corr = df[columns_to_normalize].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Performance Metrics')
plt.tight_layout()
plt.savefig('plot_correlation_matrix.png', dpi=300)
plt.show()

# Plot 4: Distribution of Mutual Fund Categories
plt.figure(figsize=(10, 6))
df_sorted['category'].value_counts().plot(kind='bar')
plt.title('Distribution of Mutual Fund Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('plot_category_distribution.png', dpi=300)
plt.show()

# Plot 5: Radar Chart for Best Fund
best_fund = df_normalized.loc[df['rank'].idxmin()]
metrics = list(weights.keys())
values = best_fund[metrics].values

angles = np.linspace(0, 2*np.pi, len(metrics), endpoint=False)
values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

plt.figure(figsize=(8, 8))
plt.polar(angles, values, marker='o')
plt.title('Risk–Return Radar Chart: Top Ranked Fund')
plt.fill(angles, values, alpha=0.3)
plt.savefig('plot_risk_return_radar.png', dpi=300)
plt.show()