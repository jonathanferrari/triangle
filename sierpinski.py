import plotly.graph_objects as go
import random
import webbrowser
import os

# Define the vertices of the triangle
TOP = (0, 400)
BOTTOM_LEFT = (-400, -400)
BOTTOM_RIGHT = (400, -400)

# Function to calculate the midpoint between two points in 2D
def midpoint_2d(p1, p2):
    return (
        (p1[0] + p2[0]) / 2,
        (p1[1] + p2[1]) / 2,
    )

# Generate points for the Sierpinski Triangle
def generate_sierpinski_points_2d(n):
    points = []
    point = (0, 0)  # Initial point
    vertices = [TOP, BOTTOM_LEFT, BOTTOM_RIGHT]
    
    for _ in range(n):
        vertex = random.choice(vertices)
        point = midpoint_2d(point, vertex)
        points.append(point)
    return points

# Generate 50,000 points
points = generate_sierpinski_points_2d(250_000)

# Extract x, y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Create the 2D scatter plot using Plotly
fig = go.Figure(
    data=[
        go.Scatter(
            x=x_coords,
            y=y_coords,
            mode="markers",
            marker=dict(size=2, color="blue", opacity=0.8),  # Single color for all points
        )
    ]
)

# Set layout to ensure equal aspect ratio and hide axes
fig.update_layout(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    title="2D Sierpinski Triangle",
    plot_bgcolor="white",  # Clean white background
    xaxis_scaleanchor="y",  # Lock aspect ratio
)

# File path for the HTML output
output_file = "sierpinski_2d.html"

# Export the plot as an interactive HTML file
fig.write_html(output_file)

# Automatically open the file in the default browser
webbrowser.open(f"file://{os.path.abspath(output_file)}")

print(f"Sierpinski Triangle saved as '{output_file}' and opened in the browser.")
