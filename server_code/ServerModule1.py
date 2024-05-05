import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import pandas as pd

# Load the data
@anvil.server.callable
def load_data():
    return pd.read_csv(data_files['nocturia_df.csv'])

@anvil.server.callable
def get_age_distribution():
    df = load_data()
    return df['age'].tolist()

@anvil.server.callable
def get_bmi_distribution():
    df = load_data()
    return df['bmi'].tolist()

@anvil.server.callable
def get_sex_distribution():
    df = load_data()
    return df['sex'].value_counts().to_dict()

@anvil.server.callable
def get_nocturia_by_age():
    df = load_data()
    return df[['age', 'nocturia']].values.tolist()

@anvil.server.callable
def get_sleep_efficiency_by_age():
    df = load_data()
    return df[['age', 'sleep_efficiency']].values.tolist()

@anvil.server.callable
def get_alcohol_consumption():
    df = load_data()
    return df['alcohol'].tolist()

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
def get_odi_distribution():
    df = load_data()
    return df.groupby('age')['odi'].mean().reset_index().values.tolist()
