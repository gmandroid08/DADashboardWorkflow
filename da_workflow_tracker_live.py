import pandas as pd
import streamlit as st
import gspread
from gspread_dataframe import get_as_dataframe
from oauth2client.service_account import ServiceAccountCredentials
from st_aggrid import AgGrid, GridOptionsBuilder

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('552a127af3fd6b0745a86084f1d51bd4ad73e79f', scope)
gc = gspread.authorize(credentials)

sheet = gc.open('Sample_DA_WorkflowDashboard').sheet1
df = get_as_dataframe(sheet).dropna()

st.title('DA Live Workflow Tracker')
st.markdown('**Hover or click on names to see current workflow**')

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, editable=False)
gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, enable_enterprise_modules=False, theme='streamlit')
