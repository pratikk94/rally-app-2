import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import pandas as pd

# Load the data
@anvil.server.callable
def load_data():
    return pd.read_csv(data_files['noctoria_df.csv'])

@anvil.server.callable
def get_age_distribution(min_age, max_age):
    df = load_data()  # Load the dataset
    # Filter the dataframe for the specified age range
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)]
    return filtered_df['age'].tolist()

@anvil.server.callable
def get_bmi_distribution(min_bmi, max_bmi):
    df = load_data()  # Load the dataset
    # Filter the dataframe for the specified BMI range
    filtered_df = df[(df['bmi'] >= min_bmi) & (df['bmi'] <= max_bmi)]
    return filtered_df['bmi'].tolist()

@anvil.server.callable
def get_sex_distribution(min_age, max_age):
    df = load_data() # Load the data, ensuring the path is correct
    # Filter the dataframe for the specified age range
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)]
    return filtered_df['sex'].value_counts().to_dict()

@anvil.server.callable
def get_nocturia_by_age(min_age, max_age):
    df = load_data()  # Ensure this path is correct
    # Filter the dataframe for the specified age range
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)]
    return filtered_df[['age', 'nocturia']].values.tolist()

@anvil.server.callable
def get_sleep_efficiency_by_age(min_age, max_age):
    df = load_data()  # Ensure this path is correct
    # Filter the data based on age range
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)]
    return filtered_df[['age', 'sleep_efficiency']].values.tolist()

@anvil.server.callable
def get_alcohol_consumption(min_age, max_age):
    df = load_data()  # Ensure this path is correct
    # Filter the dataframe for the specified age range
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)]
    return filtered_df['alcohol'].tolist()

@anvil.server.callable
def get_smoking_status():
    df = load_data()
    return df['smoking'].value_counts().to_dict()

@anvil.server.callable
def get_hypertension_diabetes_prevalence():
    df = load_data()
    return df[['hypertension', 'diabetes']].apply(pd.Series.value_counts).fillna(0).astype(int).to_dict()

@anvil.server.callable
def get_ahi_distribution():
    df = load_data()
    return df['ahi'].tolist()

@anvil.server.callable
def get_odi_distribution(min_age, max_age):
    df = load_data()  # Ensure this path is correct
    # Filter data based on the provided age range
    filtered_df = df[(df['age'] >= min_age) & (df['age'] <= max_age)]
    return filtered_df.groupby('age')['odi'].mean().reset_index().values.tolist()
