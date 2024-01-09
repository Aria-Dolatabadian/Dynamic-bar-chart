import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Sample data (replace this with your actual data)
countries = ['USA', 'China', 'Russia', 'Germany', 'France',
             'UK', 'India', 'Spain', 'Poland', 'Australia']

years = np.arange(1970, 2020)
num_countries = len(countries)

# Read data from CSV
wheat_production = pd.read_csv('production_data.csv', index_col='Year').values.T

# Create a colormap for different colors
colors = plt.cm.viridis(np.linspace(0, 1, num_countries))

# Load country flags (f'type/the/actual/path/to/your/flag/images/{country}.png') 
flag_images = [plt.imread(f'{country}.png') for country in countries]

# Set a fixed height for the flags
flag_height = 100

# Create the initial bar chart
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(countries, wheat_production[:, 0], color=colors)

# Set the Y-axis limit to 1000
ax.set_ylim(0, 1000)

# Add labels and title
ax.set_ylabel('Production')
ax.set_title(f'Production in 10 Countries - Year {years[0]}')

# Add flags to each bar at the same height
for bar, flag_image, country in zip(bars, flag_images, countries):
    imagebox = OffsetImage(flag_image, zoom=0.05, resample=True)
    ab = AnnotationBbox(imagebox, (bar.get_x() + bar.get_width() / 2, flag_height),
                        boxcoords="data", frameon=False, pad=0.5, clip_path=None)
    ax.add_artist(ab)

# Update function for the animation
def update(frame):
    for bar, h, color in zip(bars, wheat_production[:, frame], colors):
        bar.set_height(h)
        bar.set_color(color)
    ax.set_title(f'Production in 10 Countries - Year {years[frame]}')

# Create the animation
animation = FuncAnimation(fig, update, frames=len(years), interval=500, repeat=False)

# Save the dynamic bar chart as a GIF
animation.save('Production_animation_with_flags.gif', writer='imagemagick')

# Display the dynamic bar chart
plt.show()
