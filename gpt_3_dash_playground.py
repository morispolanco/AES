"""**SQL Query generation**"""

# Preset 01: Generate SQL Queries
def run_preset_01(query):
  
  response = openai.Completion.create(
    # The engine, or model, which will generate the completion. Some engines are suitable for natural language tasks, others specialize in code  
    engine="code-davinci-001",
    # the query to be completed in natural language. i.e. prompt="### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT",
    prompt=query,
    # The temperature controls the randomness of the answer. 0.0 is the most deterministic and repetitive value
    temperature=0,
    # The maximum number of tokens to generate
    max_tokens=150,
    # Controls diversity via nucleus sampling. 0.5 means all of all likeliwood-weighted options are considered
    top_p=1.0,
    # Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
    frequency_penalty=0.0,
    # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
    presence_penalty=0.0,
    # Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.
    stop=["#", ";"]
  )

  return response.choices[0].text

"""**AWS S3 Buckets code**"""

# Preset 02: AWS S3 Buckets Code
def run_preset_02(query):
  
  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="generate a python code that prints my S3 buckets list then create a new bucket named 'test'",
    prompt=query,
    temperature=0,
    max_tokens=150,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["#", ";"]
  )

  return response.choices[0].text

"""**AWS CloudWatch Alarm generation**"""

# Preset 03: AWS CloudWatch Alarm generation
def run_preset_03(query):
  
  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="###Generate a python code that creates an AWS CloudWatch Alarm named 'test_alarm_osy' which triggers when server CPU exceeds 70%",
    prompt=query,
    temperature=0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["#", ";"]
  )

  return response.choices[0].text

"""**AWS User profile creation**"""

# Preset 04: AWS User Profile creation
def run_preset_04(query):
  
  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="Generate a python code that creates an AWS user named 'osadey' with password 'abcde'",
    prompt=query,
    temperature=0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["#", ";"]
  )

  return response.choices[0].text

"""**Python AI Code that predict salary with Random Forest Algorithm**"""

# Preset 05: Python AI Code generation
def run_preset_05(query):
  
  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="#predict the salary with criteria like age, position, experience, using random forest algorithm",
    prompt=query,
    temperature=0.0,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    ##stop=["#", ";"]
  )

  return response.choices[0].text

"""**Simple ReactJS Code Generation**"""

# Preset 06: ReactJS code generation
def run_preset_06(query):

  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="/* generate a ReactJS code with a button that displays a message 'Hello GPT-3' when the user clicks on it */",
    prompt=query,
    temperature=0.0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    ##stop=["/*"]
  )

  return response.choices[0].text

"""**Simple Java Class generation**"""

# Preset 07: Java Code generation
def run_preset_07(query):
  
  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="/* A Java class used to represent a person with name, age and gender attributs */\npublic class Person",
    prompt=query,
    temperature=0,
    max_tokens=300,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["/*"]
  )

  return response.choices[0].text

"""**Python Developper Task List**"""

# Preset 08: Python Developper Task list
def run_preset_08(query):
 
  response = openai.Completion.create(
    engine="code-davinci-001",
    # i.e. prompt="\"\"\"\n1. Create a list of first names\n2. Create a list of last names\n3. Combine them randomly into a list of 100 full names\n\"\"\"",
    prompt=query,
    temperature=0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].text

"""**Summerize a text**"""

# Preset 09: Summerize a text
def run_preset_09(query):

  response = openai.Completion.create(
    engine="text-davinci-001",
    # i.e. prompt="Summarize the following text:\nOne month after the United States began what has become a troubled rollout of a national COVID vaccination campaign, the effort is finally gathering real steam. Close to a million doses -- over 951,000, to be more exact -- made their way into the arms of Americans in the past 24 hours, the U.S. Centers for Disease Control and Prevention reported Wednesday. That's the largest number of shots given in one day since the rollout began and a big jump from the previous day, when just under 340,000 doses were given, CBS News reported. That number is likely to jump quickly after the federal government on Tuesday gave states the OK to vaccinate anyone over 65 and said it would release all the doses of vaccine it has available for distribution. Meanwhile, a number of states have now opened mass vaccination sites in an effort to get larger numbers of people inoculated, CBS News reported.\n",
    prompt=query,
    temperature=0.7,
    max_tokens=150,
    top_p=0.90,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    ##stop=["\n"]
  )

  return response.choices[0].text

"""**Simplify a text**"""

# Preset 10: Simplify a text
def run_preset_10(query):

  response = openai.Completion.create(
    engine="text-davinci-001",
    # i.e. prompt="My ten-year-old asked me what this passage means:\n\"\"\"\nA neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\n\"\"\"\n\nI rephrased it for him, in plain language a ten-year-old can understand:\n\"\"\"\n",
    prompt=query,
    temperature=1,
    max_tokens=64,
    top_p=0.88,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\"\"\""]
  )

  return response.choices[0].text

"""**Main Dash Web Application**"""

##!pip uninstall dash jupyter_dash
## Temporary usage of Dash 2.0 due to a bug on 2.1

from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


# Build App
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H5("GPT-3 Playground"),
    dcc.Dropdown(
        id='dropdown-preset',
        options=[
            {'label': 'Generate an SQL query', 'value': '01'},
            {'label': 'Print my current AWS S3 buckets then create a new bucket', 'value': '02'},
            {'label': 'Create an AWS CloudWatch Alarm', 'value': '03'},
            {'label': 'Create an AWS user', 'value': '04'},
            {'label': 'Predict the salary with criteria like age, position, experience', 'value': '05'},
            {'label': 'ReactJS code with a simple button', 'value': '06'},
            {'label': 'A simple Java Class', 'value': '07'},
            {'label': 'Developer Task List', 'value': '08'},
            {'label': 'Summarize a text', 'value': '09'},
            {'label': 'Simplify a text', 'value': '10'}
        ],
        placeholder="Load a preset"
    ),
    dcc.Textarea(
          id='textarea-query',
          value='',
          placeholder="Type a query in natural language or select a preset above",
          style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-query-output', style={'whiteSpace': 'pre-line', 'padding-top': '10px'}),
    html.Button('Generate', id='button-generate',n_clicks=0),
    html.Div(id='div-output-results', style={'padding-top': '10px'}),
    html.Pre(
        id='div-output-results2',
        style={
          'height': 200, 
          'overflow': 'auto',
          'font-family': 'courier new',
          'font-weight': 'bold',
          'color': 'white',
          'background-color': 'LightSlateGrey',
          'padding': '10px',
          'font-size': '100%',
          'border': 'solid 1px #A2B1C6'
          }

        ),
    
], style={
        'border': 'solid 1px #A2B1C6',
        'border-radius': '5px',
        'padding': '20px',
        'margin-top': '10px'
    })

##
## Called when Preset dropdown is selected
##
@app.callback(
    Output(component_id='textarea-query', component_property='value'),
    Input(component_id='dropdown-preset', component_property='value'),
)
def update_output(dropdown):
    ##return 'You have selected query "{}"'.format(get_query_from_preset(dropdown))
    return get_query_from_preset(dropdown)


def get_query_from_preset(preset):
  query = '' 
  if preset == '01':
        query = '### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\nSELECT'
  elif preset == '02':
        query = "generate a python code that prints my S3 buckets list then create a new bucket named 'test\'"
  elif preset == '03':
        query = "###Generate a python code that creates a CloudWatch Alarm named 'test_alarm_osy' which triggers when server CPU exceeds 70%"
  elif preset == '04':      
        query = "#Generate a python code that creates a user named 'osadey' with password 'abcde'\nimport boto3"
  elif preset == '05': 
        query = "predict the salary with criteria like age, position, experience, using random forest algorithm"
  elif preset == '06': 
        query = "/* generate a ReactJS code with a button that displays a message 'Hello GPT-3' when the user clicks on it */"
  elif preset == '07': 
        query = "/* A Java class used to represent a person with name, age and gender attributs */\npublic class Person"
  elif preset == '08': 
        query = "1. Create a list of first names\n2. Create a list of last names\n3. Combine them randomly into a list of 100 full names\n4. Print the full names in a nicely formatted way\n5. Print the number of full names that contain a 'K'"
  elif preset == '09': 
        query = "Summarize the following text:\nOne month after the United States began what has become a troubled rollout of a national COVID vaccination campaign, the effort is finally gathering real steam. Close to a million doses -- over 951,000, to be more exact -- made their way into the arms of Americans in the past 24 hours, the U.S. Centers for Disease Control and Prevention reported Wednesday. That's the largest number of shots given in one day since the rollout began and a big jump from the previous day, when just under 340,000 doses were given, CBS News reported. That number is likely to jump quickly after the federal government on Tuesday gave states the OK to vaccinate anyone over 65 and said it would release all the doses of vaccine it has available for distribution. Meanwhile, a number of states have now opened mass vaccination sites in an effort to get larger numbers of people inoculated, CBS News reported.\n"
  elif preset == '10': 
        query = "My ten-year-old asked me what this passage means:\n\"A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\"\n\nI rephrased it for him, in plain language a ten-year-old can understand:"
  return query

##
## Called when the Button 'Generate' is pushed
##
@app.callback(
    Output(component_id='div-output-results2', component_property='children'),
    State(component_id='textarea-query', component_property='value'),
    State(component_id='dropdown-preset', component_property='value'),
    Input('button-generate', 'n_clicks')
)
def update_output2(textarea, preset, n_clicks):


    if n_clicks is None or n_clicks == 0:
        return '(nothing generated yet)'
    else:
        ## Execute dynamically the 'run_preset_nn' function (where 'nn' is the preset number)
        results = globals()['run_preset_%s' % preset](textarea)       
        return results



# Run app and display result inline in the notebook
app.run_server(debug=False)
