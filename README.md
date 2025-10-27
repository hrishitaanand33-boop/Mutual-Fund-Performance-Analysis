# Mutual Fund Performance Analysis & Dashboard

This project provides a comprehensive analysis of top mutual funds in India using quantitative performance indicators and visual analytics. It includes automated data processing, risk-return profiling, and an interactive Power BI dashboard to support investment decision-making.

---

## 📊 Project Overview

The objective of this project is to identify high-performing mutual funds by analyzing:

• Return metrics (1Y, 3Y, 5Y CAGR)
• Risk indicators such as Beta, Standard Deviation, and Sharpe Ratio
• Expense structure and fund size
• Fund category distribution
• Composite scoring and ranking for comparison

Insights are delivered using both Python-based visualizations and a Power BI dashboard.

---

## ✅ Key Features

• Automated data cleaning and feature extraction from real-world mutual fund datasets
• Performance analysis using statistical and risk-adjusted metrics
• Ranking model based on composite scoring
• Power BI dashboard for visual insights and filtering
• Exportable visual plots for presentations and reporting

---

## 🛠️ Tech Stack

| Component      | Tools                      |
| -------------- | -------------------------- |
| Data Analysis  | Python (Pandas, NumPy)     |
| Visualization  | Matplotlib / Seaborn       |
| Dashboard      | Microsoft Power BI (.pbix) |
| Source Control | Git & GitHub               |

---

## 📂 Repository Structure

```
📁 Mutual-Fund-Performance-Analysis
│
├── mf_analysis.py                        # Main script for data processing and analysis
├── Mutual Fund Dashboard.pbix            # Power BI Dashboard
├── top_30_mutual_funds.csv               # Dataset used in analysis
│
├── plot_category_distribution.png        # Fund type distribution chart
├── plot_correlation_matrix.png           # Correlation heatmap of key metrics
├── plot_expense_vs_returns5yr.png        # Expense ratio vs 5Y returns
├── plot_risk_return_radar.png            # Risk-return radar visualization
├── plot_top10_composite_score.png        # Best funds by ranking score
│
└── README.md                             # Project documentation
```

---

## 📈 Methodology

1. Data extraction and validation
2. Feature engineering with risk-return metrics
3. Ranking model using composite scoring
4. Insight generation and visualization
5. Report building in Power BI

---

## 🧠 Insights Extracted

• Categories with stronger long-term performance
• Relationship between expense ratio and returns
• Risk-adjusted return leaders (Sharpe, Sortino)
• Top ranked funds based on multi-factor scoring

---

## 🚀 Future Enhancements

• Live data ingestion from APIs
• Portfolio optimization using Modern Portfolio Theory
• Deployment of dashboard to Power BI Service
• Automated monthly updates
If you want, a section for installation instructions can also be added (Python requirements, etc.). Would you like the README to include badges or a project logo for a more polished GitHub look?
