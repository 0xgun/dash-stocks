import dash
from dash import dcc
from dash import html
from datetime import date


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.Div(
            [
                html.P("Welcome to the Stock Dash App!", className="start"),
                html.Div(
                    [
                        # stock code input
                        html.P("Input the stock code:"),
                        dcc.Input(
                            id="input-code",
                        ),
                       html.Button("Submit"),
                        # Date range picker input
                        html.Div(
                            [
                                dcc.DatePickerRange(
                                    id="date-picker-range",
                                    start_date_placeholder_text="Start date",
                                    end_date=date(2022, 3, 16),
                                )
                            ]
                        ),
                    ]
                ),
                html.Div(
                    [
                        # Stock price button
                        html.Button("Stock Price"),
                        # Indicators button
                        html.Button("Indicators"),
                        # Number of days of forecast input
                        dcc.Input(id="input-box", type="text"),
                        # Forecast button
                        html.Button("Forecast"),
                    ]
                ),
            ],
            className="nav",
        ),
        html.Div(
            [
                html.Div(
                    [  # Logo
                        # Company Name
                    ],
                    className="header",
                ),
                html.Div(  # Description
                    id="description", className="decription_ticker"
                ),
                html.Div(
                    [
                        # Stock price plot
                    ],
                    id="graphs-content",
                ),
                html.Div(
                    [
                        # Indicator plot
                    ],
                    id="main-content",
                ),
                html.Div(
                    [
                        # Forecast plot
                    ],
                    id="forecast-content",
                ),
            ],
            className="content",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
