from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objs as go

class Form1(Form1Template):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Call plotting functions to load plots on form initialization
        self.load_plots()

  def load_plots(self):
        # Age Distribution
        self.plot_age_distribution()
        self.plot_ahi_distribution()
        self.plot_alcohol_consumption()
        self.plot_bmi_distribution()
        self.plot_hypertension_diabetes_prevalence()
        self.plot_nocturia_by_age()
        self.plot_odi_distribution()
        self.plot_sex_distribution()
        self.plot_sleep_efficiency_by_age()
        #self.plot_smoking_status()
  
  def plot_age_distribution(self):
      age_data = anvil.server.call('get_age_distribution')
      fig = go.Figure(data=[go.Histogram(x=age_data)])
      fig.update_layout(title='Age Distribution')
      self.plotAgeDistribution.figure = fig  # 'plotAgeDistribution' is the name of the Plot component on your form

  def plot_bmi_distribution(self):
      bmi_data = anvil.server.call('get_bmi_distribution')
      fig = go.Figure(data=[go.Histogram(x=bmi_data)])
      fig.update_layout(title='BMI Distribution')
      self.plotBMIDistribution.figure = fig

  def plot_sex_distribution(self):
      sex_data = anvil.server.call('get_sex_distribution')
      fig = go.Figure(data=[go.Pie(labels=list(sex_data.keys()), values=list(sex_data.values()))])
      fig.update_layout(title='Sex Distribution')
      self.plotSexDistribution.figure = fig
  
  def plot_nocturia_by_age(self):
      data = anvil.server.call('get_nocturia_by_age')
      fig = go.Figure(data=[go.Scatter(x=[item[0] for item in data], y=[item[1] for item in data], mode='markers')])
      fig.update_layout(title='Nocturia by Age', xaxis_title='Age', yaxis_title='Nocturia')
      self.plotNocturiaByAge.figure = fig
  
  def plot_sleep_efficiency_by_age(self):
      data = anvil.server.call('get_sleep_efficiency_by_age')
      fig = go.Figure(data=[go.Scatter(x=[item[0] for item in data], y=[item[1] for item in data], mode='markers')])
      fig.update_layout(title='Sleep Efficiency by Age')
      self.plotSleepEfficiencyByAge.figure = fig
  
  def plot_alcohol_consumption(self):
      alcohol_data = anvil.server.call('get_alcohol_consumption')
      fig = go.Figure(data=[go.Histogram(x=alcohol_data)])
      fig.update_layout(title='Alcohol Consumption')
      self.plotAlcoholConsumption.figure = fig
  
  # def plot_smoking_status(self):
  #     smoking_data = anvil.server.call('get_smoking_status')
  #     fig = go.Figure(data=[go.Pie(labels=list(smoking_data.keys()), values=list(smoking_data.values()))])
  #     fig.update_layout(title='Smoking Status')
  #     self.plotSmokingStatus.figure = fig
  
  def plot_hypertension_diabetes_prevalence(self):
      data = anvil.server.call('get_hypertension_diabetes_prevalence')
      fig = go.Figure(data=[
          go.Bar(name='Hypertension', x=list(data['hypertension'].keys()), y=list(data['hypertension'].values())),
          go.Bar(name='Diabetes', x=list(data['diabetes'].keys()), y=list(data['diabetes'].values()))
      ])
      fig.update_layout(title='Hypertension and Diabetes Prevalence', barmode='group')
      self.plotHypertensionDiabetesPrevalence.figure = fig
  
  def plot_ahi_distribution(self):
      ahi_data = anvil.server.call('get_ahi_distribution')
      fig = go.Figure(data=[go.Histogram(x=ahi_data)])
      fig.update_layout(title='AHI Distribution')
      self.plotAHIDistribution.figure = fig
  
  def plot_odi_distribution(self):
      odi_data = anvil.server.call('get_odi_distribution')
      fig = go.Figure(data=[go.Scatter(x=[item[0] for item in odi_data], y=[item[1] for item in odi_data], mode='lines')])
      fig.update_layout(title='ODI Distribution')
      self.plotODIDistribution.figure = fig

  def plotBMIDistribution_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass
      