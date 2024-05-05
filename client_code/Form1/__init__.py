from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objs as go

class Form1(Form1Template):
  def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        
        # Call plotting functions to load plots on form initialization
        # self.load_plots()

  def button_plot_age_distribution_click(self, **event_args):
        # Get the minimum and maximum age from the text inputs
        min_age = int(self.min_age.text)
        max_age = int(self.max_age.text)

        # Call the server function with the specified age range
        age_data = anvil.server.call('get_age_distribution', min_age, max_age)
        
        # Create the histogram plot
        fig = go.Figure(data=[go.Histogram(x=age_data)])
        fig.update_layout(title='Age Distribution', xaxis_title='Age', yaxis_title='Frequency')

        # Display the plot in the Plot component
        self.plotAgeDistribution.figure = fig

  def button_plot_bmi_distribution_click(self, **event_args):
        # Get the minimum and maximum BMI from the text inputs
        min_bmi = float(self.min_age.text)
        max_bmi = float(self.max_age.text)

        # Call the server function with the specified BMI range
        bmi_data = anvil.server.call('get_bmi_distribution', min_bmi, max_bmi)
        
        # Create the histogram plot
        fig = go.Figure(data=[go.Histogram(x=bmi_data)])
        fig.update_layout(title='BMI Distribution', xaxis_title='BMI', yaxis_title='Frequency')

        # Display the plot in the Plot component
        self.plotBMIDistribution.figure = fig

  def plot_sex_distribution(self):
      sex_data = anvil.server.call('get_sex_distribution')
      fig = go.Figure(data=[go.Pie(labels=list(sex_data.keys()), values=list(sex_data.values()))])
      fig.update_layout(title='Sex Distribution')
      self.plotSexDistribution.figure = fig
  
  def button_plot_nocturia_by_age_click(self, **event_args):
        # Get the minimum and maximum age from user inputs
        min_age = int(self.min_age.text)
        max_age = int(self.max_age.text)

        # Call the server function with the specified age range
        data = anvil.server.call('get_nocturia_by_age', min_age, max_age)
        
        # Create the scatter plot
        fig = go.Figure(data=[go.Scatter(x=[item[0] for item in data], 
                                         y=[1 if item[1] == 'Yes' else 0 for item in data], # Assuming 'nocturia' is a Yes/No field
                                         mode='markers')])
        fig.update_layout(title='Nocturia by Age', xaxis_title='Age', yaxis_title='Nocturia')

        # Display the plot in the Plot component
        self.plotNocturiaByAge.figure = fig
  
  def button_plot_sleep_efficiency_click(self, **event_args):
        # Get the minimum and maximum age from the text inputs
        min_age = int(self.min_age.text)
        max_age = int(self.max_age.text)

        # Call the server function with the specified age range
        data = anvil.server.call('get_sleep_efficiency_by_age', min_age, max_age)
        
        # Create the scatter plot
        fig = go.Figure(data=[go.Scatter(x=[item[0] for item in data], y=[item[1] for item in data], mode='markers')])
        fig.update_layout(title='Sleep Efficiency by Age', xaxis_title='Age', yaxis_title='Sleep Efficiency')

        # Display the plot in the Plot component
        self.plotSleepEfficiencyByAge.figure = fig
  
  def button_plot_alcohol_consumption_click(self, **event_args):
        # Get the minimum and maximum age from user inputs
        min_age = int(self.min_age.text)
        max_age = int(self.max_age.text)

        # Call the server function with the specified age range
        alcohol_data = anvil.server.call('get_alcohol_consumption', min_age, max_age)
        
        # Create the histogram
        fig = go.Figure(data=[go.Histogram(x=alcohol_data)])
        fig.update_layout(title='Alcohol Consumption', xaxis_title='Alcohol Units', yaxis_title='Frequency')

        # Display the plot in the Plot component
        self.plotAlcoholConsumption.figure = fig
  
  # def plot_smoking_status(self):
  #     smoking_data = anvil.server.call('get_smoking_status')
  #     fig = go.Figure(data=[go.Pie(labels=list(smoking_data.keys()), values=list(smoking_data.values()))])
  #     fig.update_layout(title='Smoking Status')
  #     self.plotSmokingStatus.figure = fig
  
  def button_plot_hypertension_diabetes_prevalence_click(self, **event_args):
        # Get the minimum and maximum age from user inputs
        min_age = int(self.min_age.text)  # Assuming there's an input for min age
        max_age = int(self.max_age.text)  # Assuming there's an input for max age

        # Call the server function with the specified age range
        data = anvil.server.call('get_hypertension_diabetes_prevalence', min_age, max_age)
        
        # Create the bar plot
        fig = go.Figure(data=[
            go.Bar(name='Hypertension', x=list(data['hypertension'].keys()), y=list(data['hypertension'].values())),
            go.Bar(name='Diabetes', x=list(data['diabetes'].keys()), y=list(data['diabetes'].values()))
        ])
        fig.update_layout(title='Hypertension and Diabetes Prevalence', barmode='group', xaxis_title='Condition', yaxis_title='Count')

        # Display the plot in the Plot component
        self.plotHypertensionDiabetesPrevalence.figure = fig
  
  def button_plot_ahi_distribution_click(self, **event_args):
        # Get the minimum and maximum age from user inputs
        min_age = int(self.min_age.text)  # Assuming there's an input for min age
        max_age = int(self.max_age.text)  # Assuming there's an input for max age

        # Call the server function with the specified age range
        ahi_data = anvil.server.call('get_ahi_distribution', min_age, max_age)
        
        # Create the histogram
        fig = go.Figure(data=[go.Histogram(x=ahi_data)])
        fig.update_layout(title='AHI Distribution', xaxis_title='AHI', yaxis_title='Frequency')

        # Display the plot in the Plot component
        self.plotAHIDistribution.figure = fig
  
  def button_plot_odi_distribution_click(self, **event_args):
        # Get the minimum and maximum age from user inputs
        min_age = int(self.min_age.text)  # Assuming 'text_input_min_age' is your input component for minimum age
        max_age = int(self.max_age.text)  # Assuming 'text_input_max_age' is your input component for maximum age

        # Call the server function with the specified age range
        odi_data = anvil.server.call('get_odi_distribution', min_age, max_age)
        
        # Create the line plot
        fig = go.Figure(data=[go.Scatter(x=[item[0] for item in odi_data], y=[item[1] for item in odi_data], mode='lines')])
        fig.update_layout(title='ODI Distribution', xaxis_title='Age', yaxis_title='Average ODI')

        # Display the plot in the Plot component
        self.plotODIDistribution.figure = fig


  def set_age_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_plot_sleep_efficiency_click(**event_args)
    self.button_plot_bmi_distribution_click(**event_args)
    self.plotSexDistribution_click(**event_args)
    self.button_plot_age_distribution_click(**event_args)
    self.button_plot_odi_distribution_click(**event_args)
    self.button_plot_nocturia_by_age_click(**event_args)
    self.button_plot_alcohol_consumption_click(**event_args)
    self.button_plot_ahi_distribution_click(**event_args)
    self.button_plot_hypertension_diabetes_prevalence_click(**event_args)
    pass

  def plotSexDistribution_click(self, **event_args):
       # Get the minimum and maximum age from the text inputs
        min_age = int(self.min_age.text)
        max_age = int(self.max_age.text)

        # Call the server function with the specified age range
        sex_data = anvil.server.call('get_sex_distribution', min_age, max_age)
        
        # Create the pie chart
        labels = list(sex_data.keys())
        values = list(sex_data.values())
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title='Sex Distribution by Age Range')

        # Display the plot in the Plot component
        self.plotSexDistribution.figure = fig
        pass
      