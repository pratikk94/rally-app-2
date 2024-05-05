from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objs as go


    


def plot_age_distribution():
    age_data = anvil.server.call('get_age_distribution')
    plt.hist(age_data, title="Age Distribution")

def plot_bmi_distribution():
    bmi_data = anvil.server.call('get_bmi_distribution')
    plt.hist(bmi_data, title="BMI Distribution")

def plot_sex_distribution():
    sex_data = anvil.server.call('get_sex_distribution')
    plt.pie(labels=sex_data.keys(), values=sex_data.values(), title="Sex Distribution")

def plot_nocturia_by_age():
    data = anvil.server.call('get_nocturia_by_age')
    plt.scatter(x=[x[0] for x in data if x[1] == 'Yes'], y=[1]*sum(x[1] == 'Yes' for x in data), title="Nocturia by Age")

def plot_sleep_efficiency_by_age():
    data = anvil.server.call('get_sleep_efficiency_by_age')
    plt.scatter(x=[x[0] for x in data], y=[x[1] for x in data], title="Sleep Efficiency by Age")

def plot_alcohol_consumption():
    alcohol_data = anvil.server.call('get_alcohol_consumption')
    plt.hist(alcohol_data, title="Alcohol Consumption")

def plot_smoking_status():
    smoking_data = anvil.server.call('get_smoking_status')
    plt.pie(labels=smoking_data.keys(), values=smoking_data.values(), title="Smoking Status")

def plot_hypertension_diabetes_prevalence():
    data = anvil.server.call('get_hypertension_diabetes_prevalence')
    plt.bar(x=data.keys(), y=[data['hypertension']['Yes'], data['diabetes']['Yes']], title="Hypertension and Diabetes Prevalence")

def plot_ahi_distribution():
    ahi_data = anvil.server.call('get_ahi_distribution')
    plt.hist(ahi_data, title="AHI Distribution")

def plot_odi_distribution():
    data = anvil.server.call('get_odi_distribution')
    plt.line(x=[x[0] for x in data], y=[x[1] for x in data], title="ODI by Age")


class Form1(Form1Template):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Call plotting functions to load plots on form initialization
        self.load_plots()

  def load_plots(self):
        # Age Distribution
        age_data = anvil.server.call('get_age_distribution')
        age_trace = go.Histogram(x=age_data)
        layout = go.Layout(title="Age Distribution", xaxis=dict(title="Age"), yaxis=dict(title="Frequency"))
        fig = go.Figure(data=[age_trace], layout=layout)
        self.plotAgeDistribution.figure = fig

        # BMI Distribution
        bmi_data = anvil.server.call('get_bmi_distribution')
        bmi_trace = go.Histogram(x=bmi_data)
        layout = go.Layout(title="BMI Distribution", xaxis=dict(title="BMI"), yaxis=dict(title="Frequency"))
        fig = go.Figure(data=[bmi_trace], layout=layout)
        self.plotBMIDistribution.figure = fig

        # More plots can be added similarly