# Install needed packages
# pip install streamlit pandas gspread gspread_dataframe streamlit-aggrid oauth2client

import pandas as pd
import streamlit as st
import gspread
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from st_aggrid import AgGrid, GridOptionsBuilder

# Set up credentials and access Google Sheet
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('dalivedashboard-552a127af3fd.json', scope)
gc = gspread.authorize(credentials)

# Open Google Sheet by URL
spreadsheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1T6HbMBJRHgsZFWJiVqwJeEHUE-oVKQ0BvZTRyfPN964/edit?usp=sharing')
worksheet = spreadsheet.sheet1  # Assuming data is on the first sheet
df = get_as_dataframe(worksheet).dropna()

# Build Streamlit app
st.set_page_config(page_title="DA Workflow Tracker", page_icon=":clipboard:", layout="wide")
st.title('Data Associate Live Workflow Tracker')

st.markdown('**Hover or click on DA names to view their current workflow assignment.**')

# Build interactive table
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=False)
gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=False, theme='streamlit')

st.caption('Built by Gugan L. | GitHub: https://github.com/gmandroid08/DADashboardWorkflow')
