# 📈 Pharmacokinetic (PK) Analysis in Python

This project performs a basic **pharmacokinetic (PK) analysis** on clinical trial data using Python. It demonstrates how to calculate core PK parameters like **Cmax**, **Tmax**, **AUC**, and **half-life**, and fit a **one-compartment PK model** with first-order absorption and elimination.

---

## 📂 Dataset

The analysis uses a dataset called `PONE.csv`, which contains simulated or real pharmacokinetic data with columns including:
- `ID`: subject identifier
- `TIME`: time of sample collection (hours)
- `DV`: drug concentration (µg/mL)
- `EVID`: event ID (0 = observation)

---

## 📊 Key Steps in the Analysis

### ✅ 1. Filter Observation Data
The script filters the dataset to include only **observation records** where `EVID == 0`.

### ✅ 2. Calculate Cmax and Tmax
For each subject:
- **Cmax**: maximum observed concentration
- **Tmax**: time at which Cmax occurs

Results are stored in a DataFrame.

### ✅ 3. Fit One-Compartment PK Model
For **Subject 1**:
- A **simple exponential decay model** is fitted to concentration-time data.
- The model estimates the **elimination rate constant (ke)**.
- **Half-life** is computed using the formula:  
  \[
  t_{1/2} = \frac{\ln(2)}{k_e}
  \]

### ✅ 4. Calculate AUC
The **Area Under the Curve (AUC)** is calculated using the **trapezoidal rule**.

### ✅ 5. Fit One-Compartment Model with Absorption
A more complex PK model with **first-order absorption (ka)** and **elimination (ke)** is fitted:
\[
C(t) = C_{max} \cdot \left(e^{-k_e t} - e^{-k_a t} \right)
\]

### ✅ 6. Plot the Time-Concentration Curve
The script plots the observed data and the fitted model for Subject 1 to visualize the goodness of fit.

---

## 📦 Dependencies

Make sure to install the following Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy
