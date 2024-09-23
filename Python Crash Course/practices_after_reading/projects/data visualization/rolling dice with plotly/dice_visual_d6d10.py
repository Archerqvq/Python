import plotly.express as px

from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_resule = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_resule + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of rolling a D6 and a D10 50,000 times."
lables = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=lables)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.show()
# Replac the call to fig.show() with a call to fig.write_html() to save a chart as an HTML file.
fig.write_html("./dice_visual_d6d10.html")