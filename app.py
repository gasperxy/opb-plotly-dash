# app.py
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from Services.sales_service import SalesService 
from Presentation.layouts import create_layout
from Presentation.callbacks import register_callbacks 

# --- fetch data ---
service = SalesService()
df = service.prodaja_po_produktnih_linijah()

# --- prep dropdown options ---
branches = df['branch_name'].sort_values().unique()
dropdown_options = [
    {"label": pl, "value": pl}
    for pl in branches
]

# Usrvatimo dasj app
app = Dash(__name__, external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css"])

# Naredimo layout
app.layout = create_layout(
    dropdown_options=dropdown_options,
    default_value=branches[0]
)

# REgistriramo povratne klice
register_callbacks(app, df)


# --- run ---
if __name__ == "__main__":
    app.run(debug=True)
