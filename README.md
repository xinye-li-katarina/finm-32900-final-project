# **FINM-32900 Final Project: Intermediary Asset Pricing Replication**

This repository contains our final project for replicating key results from the paper **"Intermediary Asset Pricing: New Evidence from Many Asset Classes."** Our objective is to **reproduce Tables 2 and 3** from the paper using **CRSP, Compustat, and Datastream data** and update these results with the latest available datasets.

---

## **Project Overview**

The paper suggests that **capital shocks to financial intermediaries** can explain cross-sectional differences in expected returns across asset classes, including **stocks, bonds, options, commodities, currencies, and credit default swaps.** Based on this premise, our project focuses on:

- **Constructing Risk Factors** based on financial intermediaries' capital ratios.
- **Replicating Table 2:**  
  - This table measures the **relative size of major market makers** by calculating monthly ratios of total assets, book debt, book equity, and market equity relative to different market groups, then averaging these over time.
- **Replicating Table 3:**  
  - *Panel A:* Computes key ratios like the **Market Capital Ratio, Book Capital Ratio, and AEM Leverage Ratio** from 1970Q1 to 2012Q4 and examines their correlations with economic indicators (**E/P ratio, unemployment, GDP, financial conditions, and market volatility**).  
  - *Panel B:* Constructs **risk factors** using these ratios and analyzes their relationships with macroeconomic growth rates.

---

## **Data & Methodology**

### **Data Sources**
- We **refined the primary dealer list** based on real data sources.
- The **`ticks.csv` file was updated** using the correct **GVKEY** mappings for accuracy.

### **Methodological Adjustments**
- Adjusted **key ratio calculations**.
- Improved the **accuracy and stability** of Table 3 replication results through refined calculations.

### **Output Generation & Automation**
- All **tables are automatically generated** as LaTeX (`.tex`) files and stored in the `_output` directory.
- Additional **statistical analysis**, including **descriptive statistics, correlation matrices, and trend visualizations**, was performed.
- The entire project workflow is **fully automated** using the `dodo.py` script.

---

## **Project Structure**

📂 **`notebooks`** – Jupyter notebooks for **data processing, ratio calculations, and table generation.**  
📂 **`tests`** – Unit tests to **validate replication accuracy.**  
📂 **`output`** – Auto-generated **LaTeX tables and supplementary figures.**  
📂 **`config`** – Configuration files for **environment setup and automation.**  
📜 **`dodo.py`** – Automates the workflow **from data processing to table generation.**  
📜 **`.env.`** – Template for setting **data paths and output directories.**  

---

## **Work Division**

- **Xinye Li**
  - Refined the **primary dealer list** and updated **`ticks.csv`** with accurate GVKEY data.
  - Created a **Jupyter Notebook** demonstrating data processing, ratio calculations, and table replication.
  - Replicated **Table 2**.
  - Improved the **README structure.**  

- **Hang Yu**  
  - ...

We maintained **regular collaboration** to ensure all tasks were aligned with project objectives.

---

## **Setup & Usage**

...



## **Contact & Contributions**
For questions or contributions, feel free to:  
- **Open an issue** on GitHub.  

---

