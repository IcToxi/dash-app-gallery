from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd 

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Analysis of the restaurant's revenue"),
        html.P("Select sepal length:"),
        dcc.Slider(id="slider-plots-x-sepal-length", min=5, max=8, value=5.1),
        dcc.Graph(id="slider-plots-x-graph"),
    ]
)


@app.callback(
    Output("slider-plots-x-graph", "figure"), Input("slider-plots-x-sepal-length", "value")
)
def display_graph(value):
    df = px.data.iris()  # replace with your own data source
    df = df.query(f"sepal_length <= {value}")
    data = pd.DataFrame(df.species.value_counts())
    fig = px.bar(
        data, y = "species", color="species", orientation="v",
    )
    fig.update_layout({
        "title": f"Iris species by sepal length from 5 to {value}",
        "yaxis": {"title": "Count"},
        "xaxis": {"title": "Species"},
    })

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
