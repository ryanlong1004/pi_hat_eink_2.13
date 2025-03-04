import plotly.graph_objects as go


def create_gauge_image(value, filename="gauge.png"):
    """
    Generates a gauge chart and saves it as a PNG image.

    Args:
        value (float): The value to display on the gauge.
        filename (str): The name of the file to save the image to.
    """
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": "Gauge"},
            gauge={
                "axis": {"range": [0, 100]},
                "steps": [
                    {"range": [0, 25], "color": "red"},
                    {"range": [25, 75], "color": "yellow"},
                    {"range": [75, 100], "color": "green"},
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "thickness": 0.75,
                    "value": 90,
                },
            },
        )
    )
    fig.write_image(filename)


# Example usage:
create_gauge_image(
    65
)  # Creates a gauge image with value 65 and saves it as "gauge.png"
create_gauge_image(
    30, "my_gauge.png"
)  # Creates a gauge image with value 30 and saves it as "my_gauge.png"
