# Data Science
This project is an exploratory data analysis of a Banking Dataset using Python. It covers 18 case questions on client demographics and campaign details. Each question is analysed using descriptive statistics and visualisations such as histograms, and boxplots with a correlation heatmap to identify key features related to term deposit subscription.

# Banking Dataset – Exploratory Data Analysis

A Python-based EDA project using a Banking Dataset to analyse client information and term deposit subscription.

## 📌 Overview

This project answers **18 questions** using a dataset with **45,211 client records** from a Portuguese bank's marketing campaigns (May 2008 – Nov 2010).

Each question is analysed using:

* 📊 Descriptive statistics such as counts, proportions, mean, median and standard deviation
* 📈 Visualisations such as histograms, boxplots and count plots

The project also includes a **correlation heatmap** to identify features related to term deposit subscription (`y`).

## 📂 Dataset

* **File:** `banking_data.csv`
* **Rows:** 45,211
* **Columns:** 18
* **Target:** `y` — subscribed to term deposit? (yes/no)

## ❓ Questions Answered

| #  | Question                               |
| -- | -------------------------------------- |
| 1  | Distribution of age among clients      |
| 2  | Variation of job type                  |
| 3  | Marital status distribution            |
| 4  | Level of education                     |
| 5  | Proportion with credit in default      |
| 6  | Distribution of average yearly balance |
| 7  | Clients with housing loans             |
| 8  | Clients with personal loans            |
| 9  | Communication types used               |
| 10 | Distribution of last contact day       |
| 11 | Variation of last contact month        |
| 12 | Distribution of last contact duration  |
| 13 | Contacts performed during the campaign |
| 14 | Days since previous campaign contact   |
| 15 | Contacts before the current campaign   |
| 16 | Outcomes of previous campaigns         |
| 17 | Subscription distribution (yes vs no)  |
| 18 | Correlations with subscription         |

## 🛠️ Tech Stack

* Python
* pandas
* NumPy
* matplotlib
* seaborn

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib seaborn
python "Case Project 1.py"
```
