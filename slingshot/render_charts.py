import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 75,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Progress"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "green"},
        'steps' : [
             {'range': [0, 50], 'color': "red"},
             {'range': [50, 80], 'color': "yellow"},
             {'range': [80, 100], 'color': "green"}],
        'threshold' : {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 90}}))

fig.write_image("gauge_chart.png")