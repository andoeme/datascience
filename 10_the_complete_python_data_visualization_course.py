import matplotlib.pyplot as plt 
import pickle # Opens file format pickle
import seaborn as sns 
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.palettes import Dark2_5 as palette
from bokeh.layouts import row, column, gridplot


# Open file fruit-sales.pickle
# rb = read binary data
with open('matplotlib\\fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)
    # [('Apples', 50), ('Grapefruits', 12), ('Pears', 43), ('Oranges', 38), ('Bananas', 37)]

# Split tuple into two separated tuples fruit and numberSold
fruit, numberSold = zip(*data)
fruit = list(fruit) # Convert tuple to list for Seaborn

# Specify x and y coordinates
#x = range(len(fruit)) # Numbers 1 to 5

# Plot a bar chart and display it

# Matplotlib
#plt.bar(fruit, numberSold, color='#49EB94')
#plt.xlabel('Type of Fruit')
#plt.ylabel('Number of Fruits in Millions')
#plt.title('Number of Fruits Sold in 2017')

# Seaborn
axes = sns.barplot(x=fruit, y=numberSold)
axes.set_ylabel('Number of Fruits in Millions')
axes.set_title('Number of Fruits Sold in 2017')

plt.show()

# Bokeh
plot = figure(x_range=fruit, y_axis_label='Fruit Sold in Millions', title='Fruit sold in 2017')
plot.vbar(x=fruit, top=numberSold, width=0.9) # Vertical Bar

show(plot) # Creates an html file that displays the chart



# Open Pickle file
with open('matplotlib\\coding-exp-by-dev-type.pickle', 'rb') as f:
    data = pickle.load(f)

# Split tuple data in two tuples
job, yearsExp = zip(*data)
job = list(job)
yearsExp = list(yearsExp)

# Plot and display a horizontal bar chart

# Matplotlib
#plt.barh(job, yearsExp)
#plt.xlabel('Experience in Years')
#plt.title('Job Experience in 2017')
#plt.tight_layout() # Fit chart and labels in window

# Seaborn
axes = sns.barplot(y=job, x=yearsExp)
axes.set_xlabel('Experience in Years')
axes.set_title('Job Experience in 2017')
plt.tight_layout() # Fit chart and labels in window

plt.show()

# Bokeh
# Save html in specifically named file
#output_file('bar.html')

# Tooltips
# Define where the tooltips are to be taken from
dataSource = ColumnDataSource(dict(job=job, yearsExp=yearsExp,))
# Initialize the tooltips
toolTips = [('Years of Experience', '@yearsExp')]
# Plot the Bar CHart with the tooltips
plot = figure(y_range=job, x_axis_label='years', title='Coding Experience', tools='hover', tooltips=toolTips)
# Set link to dataSource for tooltips
plot.hbar(y='job', right='yearsExp', height=0.9, source=dataSource)

show(plot)



# Open file
with open('matplotlib\\devs-outside-time.pickle', 'rb') as  f:
    data = pickle.load(f)

time, responses = zip(*data)

# Plot and display a pie chart
# autopct changes the format
# f is float, d is integer, e.g. '%d%%'
#plt.pie(responses, labels=time, autopct='%.2f%%')
#plt.axis('equal') # Make a circle if chart looks oval
#plt.title('Daily Time Developers Spent Outside')
#plt.show()

# No support of pie charts in Seaborn


# Open file prog-langs-popularity.pickle
with open('matplotlib\\prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)

# Unzip data
languages, rankings = zip(*data)

# Bokeh
fig = figure(x_axis_label='year', y_axis_label='rank', title='Ranking of Programming Languages by Year')

# Instead of unziping every tuple by hand
#java, jRanks = zip(*rankings[0])
#c, cRanks = zip(*rankings[1])
#cPlus, cPlusRanks = zip(*rankings[2])
#python, pythonRanks = zip(*rankings[3])

# Unzip multiple tuples using a for loop
for i in range(len(languages)):
    years, ranks = zip(*rankings[i])

    # Plot and display Line Chart mith multiple datasets/lines
    # Matplotlib
    #plt.plot(years, ranks)

    # Seaborn
    sns.lineplot(years, ranks)

    # Bokeh
    fig.line(years, ranks, line_width=2, legend=languages[i], color=palette[i])

# Hide and show lines via clicking on the legend entries
fig.legend.click_policy = 'hide'

show(fig)

# Format Pie Chart
plt.title('Programming Languages\' Rankings by Year')
plt.ylabel('Ranking')
plt.xlabel('Year')
plt.legend(languages)
plt.show() 



# Open file
with open('matplotlib\\iris.pickle', 'rb') as f:
    data = pickle.load(f)

# Select Sepal Length and Width from data (first values each)
# [:, 0] Everything from start to end with index 0
sepalLength = data['data'][:, 0] # index 0
sepalWidth = data['data'][:, 1] # index 1
petalLength = data['data'][:, 2] # index 0
petalWidth = data['data'][:, 3] # index 1
classes = data['target']

# Bokeh Scatter Plot
# Define classes
setosaSepalLength = sepalLength[classes == 0]
setosaSepalWidth = sepalWidth[classes == 0]
setosaPetalLength = petalLength[classes == 0]
setosaPetalWidth = petalWidth[classes == 0]

versicolorSepalLength = sepalLength[classes == 1]
versicolorSepalWidth = sepalWidth[classes == 1]
versicolorPetalLength = petalLength[classes == 1]
versicolorPetalWidth = petalWidth[classes == 1]

virginiaSepalLength = sepalLength[classes == 2]
virginiaSepalWidth = sepalWidth[classes == 2]
virginiaPetalLength = petalLength[classes == 2]
virginiaPetalWidth = petalWidth[classes == 2]

# Multiple Scatter Plots
fig1 = figure(x_axis_label='Sepal Length in cm', y_axis_label='Sepal Width in cm')
fig1.circle(setosaSepalLength, setosaSepalWidth, color=palette[0], legend='Setosa')
fig1.circle(versicolorSepalLength, versicolorSepalWidth, color=palette[1], legend='Versicolor')
fig1.circle(virginiaSepalLength, virginiaSepalWidth, color=palette[2], legend='Virginica')

# Linked panning: x axis of all plots move if the x axis is moved
# x_range=fig1.x_range
# Dependend on fig1s
fig2 = figure(x_axis_label='Petal Length in cm', y_axis_label='Petal Width in cm', x_range=fig1.x_range)
fig2.circle(setosaPetalLength, setosaPetalWidth, color=palette[0], legend='Setosa')
fig2.circle(versicolorPetalLength, versicolorPetalWidth, color=palette[1], legend='Versicolor')
fig2.circle(virginiaPetalLength, virginiaPetalWidth, color=palette[2], legend='Virginica')

fig3 = figure(x_axis_label='Sepal Length in cm', y_axis_label='Petal Length in cm')
fig3.circle(setosaSepalLength, setosaPetalLength, color=palette[0], legend='Setosa')
fig3.circle(versicolorSepalLength, versicolorPetalLength, color=palette[1], legend='Versicolor')
fig3.circle(virginiaSepalLength, virginiaPetalLength, color=palette[2], legend='Virginica')

fig4 = figure(x_axis_label='Sepal Width in cm', y_axis_label='Petal Width in cm', x_range=fig3.x_range)
fig4.circle(setosaSepalWidth, setosaPetalWidth, color=palette[0], legend='Setosa')
fig4.circle(versicolorSepalWidth, versicolorPetalWidth, color=palette[1], legend='Versicolor')
fig4.circle(virginiaSepalWidth, virginiaPetalWidth, color=palette[2], legend='Virginica')

# Make legend for plots
fig1.legend.click_policy = 'hide'
fig2.legend.click_policy = 'hide'
fig3.legend.click_policy = 'hide'
fig4.legend.click_policy = 'hide'

# row, column, gridplot layout options
show(gridplot([[fig1, fig2], [fig3, fig4]]))



# Seaborn plot scatter plot
axes = sns.scatterplot(sepalLength, sepalWidth, hue=classes, legend=False)
axes.set_ylabel('Sepal Width in cm')
axes.set_xlabel('Sepal Length in cm')
axes.set_title('Iris Dataset')

plt.show()



# Joint Plot
# kind='reg' Linear Regression
# kind='kde' Point Density
# kind='hex' Hexagon Distribution
axes = sns.jointplot(sepalLength, sepalWidth, kind='kde')
axes.set_axis_labels('Sepal Width in cm', 'Sepal Length in cm')
#axes.set_title('Iris Dataset')

plt.show()

# Joint Plot can't be used in a FacetGrid
# FacetGrid is Seaborns grid system for multiple displayed plots



# Plot a 2x2 grid to show multiple scatter charts
fig, axes = plt.subplots(2, 2)

# Sepal Length and width
#axes[0,0].scatter(sepalLength, sepalWidth, c=classes)
# Seaborn
sns.scatterplot(sepalLength, sepalWidth, hue=classes, legend=False, ax=axes[0,0])
axes[0,0].set_xlabel('Sepal Length in cm')
axes[0,0].set_ylabel('Sepal Width in cm')

# Petal length and width
#axes[0,1].scatter(petalLength, petalWidth, c=classes)
# Seaborn
sns.scatterplot(petalLength, petalWidth, hue=classes, legend=False, ax=axes[0,1])
axes[0,1].set_xlabel('Petal Length in cm')
axes[0,1].set_ylabel('Petal Width in cm')

# Sepal length and petal length
#axes[1,0].scatter(sepalLength, petalLength, c=classes)
# Seaborn
sns.scatterplot(sepalLength, petalLength, hue=classes, legend=False, ax=axes[1,0])
axes[1,0].set_xlabel('Sepal Length in cm')
axes[1,0].set_ylabel('Petal Length in cm')

# Sepal width and petal width
#axes[1,1].scatter(sepalWidth, petalWidth, c=classes)
# Seaborn
sns.scatterplot(sepalWidth, petalWidth, hue=classes, legend=False, ax=axes[1,1])
axes[1,1].set_xlabel('Sepal Width in cm')
axes[1,1].set_ylabel('Petal Width in cm')

fig.suptitle('Iris Dataset')
plt.tight_layout() # Fit chart and labels in window

plt.show()



