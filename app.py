import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

data = {
    "Category": ["Electronics", "Furniture", "Office Supplies", "Electronics", "Furniture", "Office Supplies"],
    "Region": ["North", "North", "North", "South", "South", "South"],
    "Sales": [20000, 15000, 12000, 18000, 13000, 14000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create a bar chart using Plotly Express
fig_express = px.bar(
    df,
    x="Category",
    y="Sales",
    color="Region",
    title="Sales by Category and Region",
    labels={"Sales": "Sales", "Category": "Category"},
    text="Sales"
)

# Initialize the app, add a dropdown and a graph
app = Dash()
app.layout = html.Div(children=[
    html.H1("Interactive Sales Dashboard"),
    dcc.Dropdown(
        ['North', 'South'],
        value=None,
        placeholder='Select Region',
        id='region-dropdown'
    ),
    dcc.Graph(figure=fig_express, id='sales-barchart')
])

# Build the interaction
@app.callback(
    Output('sales-barchart', 'figure'),
    Input('region-dropdown', 'value')
)

def update_graph(region_chosen):
    df_copy = df.copy(deep=True)
    if not region_chosen:
        title = "Sales by Category and Region: All Regions"
    else:
        df_copy = df[df['Region'] == region_chosen]
        title = f"Sales by Category and Region: {region_chosen}"

    new_fig = px.bar(
        df_copy,
        x="Category",
        y="Sales",
        color="Region",
        title=title,
        labels={"Sales": "Sales", "Category": "Category"},
        text="Sales"
    )
    return new_fig

if __name__ == '__main__':
    app.run_server(debug=True)
