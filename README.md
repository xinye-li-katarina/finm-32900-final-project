# **FINM-32900 Final Project: Intermediary Asset Pricing Replication**

This repository contains our final project for replicating key results from the paper **"Intermediary Asset Pricing: New Evidence from Many Asset Classes."** Our objective is to **reproduce Tables 2 and 3** from the paper using **CRSP, Compustat, and Datastream data** and update these results with the latest available datasets.

---

## **Project Overview**

The paper suggests that **capital shocks to financial intermediaries** can explain cross-sectional differences in expected returns across asset classes, including **stocks, bonds, options, commodities, currencies, and credit default swaps.** Based on this premise, our project focuses on:

- **Replicating Table 2:**  
  - This table measures the **relative size of major market makers** by calculating monthly ratios of total assets, book debt, book equity, and market equity relative to different market groups, then averaging these over time.

- **Replicating Table 3:**  
  - This table measures the pairwise correlations between various capital ratios/factors and macroeconomic indicators over the sample period from Q1 1970 to Q4 2012, using data from NYFED, NIC, CRSP-Compustat, Datastream, and several macroeconomic databases.


---

## **Data & Methodology**

### **Data Sources**
- We **refined the primary dealer list** based on real data sources.
- The **`ticks.csv` file was updated** using the correct **GVKEY** mappings for accuracy.

### **Output Generation & Automation**
- All **tables are automatically generated** as LaTeX (`.tex`) files and stored in the `_output` directory.
- **detailed procedures of data generation** as `.ipynb` file exported to `.html` file and stored in the `_output` directory.
- Additional **statistical analysis**, including **descriptive statistics, correlation matrices, and trend visualizations**, was performed.
- The entire project workflow is **fully automated** using the `dodo.py` script.

---

## **Project Structure**

📂 **`notebooks`** – Jupyter notebooks for **data processing, ratio calculations, and table generation.**  
📂 **`combined_documents`** – **LaTex PDF** for **table result, summary statistics, and trend visualization.**  
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
  - Designed the **README structure.**  

- **Hang Yu**  
  - Created a **Jupyter Notebook** demonstrating data processing, ratio calculations, and table replication.
  - Replicated **Table 3**.
  - Integrated all results and generated **Letex**, **PDF** and **html** document.
  - Designed the **dodo.py** to automate the entire workflow.

We maintained **regular collaboration** to ensure all tasks were aligned with project objectives.

---

## **Setup & Usage**

1. **You should have TexLive (or another Latex distribution) which has latexmk for the Latex generation**

2. **Install Conda or Mamba**
   - If you haven't installed [Miniforge](https://github.com/conda-forge/miniforge) yet, please download and install it (using `mamba` is recommended for faster dependency installation).  
   - After installation, make sure the executable is added to your system's `PATH`.

3. **Create and Activate the Python Environment**
   ```bash
   conda create -n py311 python=3.11
   conda activate py311

4. **Install Project Dependencies**
   ```bash
   pip install -r requirements.txt
   
5. **Run the Project**
   ```bash
   python -m doit


## **Contact & Contributions**
For questions or contributions, feel free to:  
- **Open an issue** on GitHub.  

---

