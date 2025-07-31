# Pharmacokinetic (PK) Analysis in Python

This project performs a basic pharmacokinetic (PK) analysis on clinical trial data using Python. It demonstrates how to calculate key PK parameters such as Cmax, Tmax, AUC, and half-life, and fit a one-compartment PK model with first-order absorption and elimination.

---

## Dataset

The analysis uses a dataset named `PONE.csv`, which contains pharmacokinetic data with the following columns:
- `ID`: Subject identifier
- `TIME`: Time of sample collection (in hours)
- `DV`: Drug concentration (e.g., µg/mL)
- `EVID`: Event ID (0 = observation)

---

## Analysis Steps

### 1. Filter Observation Data
The script filters the dataset to include only observation records where `EVID == 0`.

### 2. Calculate Cmax and Tmax
For each subject:
- **Cmax**: Maximum observed concentration
- **Tmax**: Time at which Cmax occurs

The results are stored in a summary DataFrame.

### 3. Fit One-Compartment PK Model
For Subject 1, a simple exponential decay model is fit to the concentration-time data to estimate:
- Elimination rate constant (**ke**)
- Half-life using the formula:  
  \[
  t_{1/2} = \frac{\ln(2)}{k_e}
  \]

### 4. Calculate AUC
The area under the curve (AUC) is calculated using the trapezoidal rule.

### 5. Fit One-Compartment Model with Absorption
A more detailed model with first-order absorption and elimination is used:
\[
C(t) = C_{max} \cdot \left(e^{-k_e t} - e^{-k_a t} \right)
\]

Model parameters **ka**, **ke**, and **Cmax** are estimated from the data.

### 6. Plot the Time-Concentration Curve
A plot is generated for Subject 1 comparing observed drug concentrations with the fitted model curve.

---

## Dependencies

To run the script, you will need the following Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scipy
