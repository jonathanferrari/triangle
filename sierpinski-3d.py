import plotly.graph_objects as go
import random
import webbrowser
import os

# Define the vertices of the tetrahedron
TOP = (0, 400, 0)
BOTTOM_FRONT_LEFT = (-400, -400, 400)
BOTTOM_FRONT_RIGHT = (400, -400, 400)
BOTTOM_BACK = (0, -400, -400)

# Function to calculate the midpoint between two points in 3D
def midpoint_3d(p1, p2):
    return (
        (p1[0] + p2[0]) / 2,
        (p1[1] + p2[1]) / 2,
        (p1[2] + p2[2]) / 2,
    )

# Generate points for the Sierpinski Tetrahedron
def generate_sierpinski_points(n):
    points = []
    point = (0, 0, 0)  # Initial point
    vertices = [TOP, BOTTOM_FRONT_LEFT, BOTTOM_FRONT_RIGHT, BOTTOM_BACK]
    
    for _ in range(n):
        vertex = random.choice(vertices)
        point = midpoint_3d(point, vertex)
        points.append(point)
    return points

# Generate 50,000 points
points = generate_sierpinski_points(500_000)

# Extract x, y, z coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]
z_coords = [p[2] for p in points]

# Create the 3D scatter plot using Plotly
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x_coords,
            y=y_coords,
            z=z_coords,
            mode="markers",
            marker=dict(size=2, color="blue", opacity=0.8),  # Single color for all points
        )
    ]
)

# Set layout to hide axes and grid and orient the top point upwards
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        camera=dict(
            up=dict(x=0, y=1, z=0),  # Set the Z-axis as the upward direction
            eye=dict(x=0, y=0, z=2),  # Position the camera directly above the Z-axis
        ),
    ),
    title="3D Sierpinski Tetrahedron",
)

# File path for the HTML output
output_file = "sierpinski_3d.html"

# Export the plot as an interactive HTML file
fig.write_html(output_file)

# Automatically open the file in the default browser
webbrowser.open(f"file://{os.path.abspath(output_file)}")

print(f"Sierpinski Tetrahedron saved as '{output_file}' and opened in the browser.")
