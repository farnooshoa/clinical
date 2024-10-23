import matplotlib.pyplot as plt
import pandas as pd


df= pd.read_csv('PONE.csv')


# Filter for observation events (EVID == 0)
observation_data = df[df['EVID'] == 0]

# Display first few rows to ensure the data is clean
observation_data.head()
# Calculate Cmax and Tmax for each subject
Cmax_list = []
Tmax_list = []

for subject_id in observation_data['ID'].unique():
    subject_data = observation_data[observation_data['ID'] == subject_id]
    Cmax = subject_data['DV'].max()
    Tmax = subject_data.loc[subject_data['DV'].idxmax(), 'TIME']
    Cmax_list.append(Cmax)
    Tmax_list.append(Tmax)

# Combine results into a DataFrame
pk_parameters_df = pd.DataFrame({
    'Subject_ID': observation_data['ID'].unique(),
    'Cmax': Cmax_list,
    'Tmax': Tmax_list
})
import numpy as np
from scipy.optimize import curve_fit

# Define a simplified one-compartment PK model
def one_compartment_model(t, ke, Cmax):
    return Cmax * np.exp(-ke * t)

# Fit the model to data and calculate half-life for one subject
subject_data = observation_data[observation_data['ID'] == 1]
time_data = subject_data['TIME'].values
concentration_data = subject_data['DV'].values

# Initial guess for ke and Cmax
initial_guess = [0.1, subject_data['DV'].max()]

# Fit the model
popt, _ = curve_fit(one_compartment_model, time_data, concentration_data, p0=initial_guess)
ke_fitted = popt[0]  # Elimination rate constant
half_life = np.log(2) / ke_fitted

half_life
# Using trapezoidal rule to calculate AUC
AUC = np.trapz(concentration_data, time_data)
AUC
# Define a one-compartment PK model with absorption and elimination
def pk_model(t, ka, ke, Cmax):
    return Cmax * (np.exp(-ke * t) - np.exp(-ka * t))

# Fit the model to subject data
initial_params = [0.5, 0.1, max(concentration_data)]
popt, _ = curve_fit(pk_model, time_data, concentration_data, p0=initial_params)

# Extract fitted parameters
ka_fitted, ke_fitted, Cmax_fitted = popt
import matplotlib.pyplot as plt

# Plot the time-concentration curve for one subject
plt.figure(figsize=(8, 6))
plt.plot(time_data, concentration_data, 'bo', label='Observed Data')
plt.plot(time_data, pk_model(time_data, ka_fitted, ke_fitted, Cmax_fitted), 'r-', label='Fitted PK Model')
plt.title('Time-Concentration Profile for Subject 1')
plt.xlabel('Time (hours)')
plt.ylabel('Concentration (µg/mL)')
plt.legend()
plt.grid(True)
plt.show()
