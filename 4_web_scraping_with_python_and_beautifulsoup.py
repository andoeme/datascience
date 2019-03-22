# BeautifulSoup for WebScraping
# Documentation at https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# pip install beautifulsoup4

from bs4 import BeautifulSoup as soup # Parser
from bs4 import element
from urllib.request import urlopen # Open and read from URLs
import re

url = 'https://en.wikipedia.org/wiki/Genome'
data = urlopen(url) # Open connection 
htmlData = data.read() # Read URL
data.close() # Close opened connection

# Parse data into readable HTML file
parsedHtml = soup(htmlData, 'html.parser')

with open('genome.html', "w", encoding="utf-8") as f:
    f.write(str(parsedHtml))
    f.close()

# Open file
# file = open(filename)

# Get all tables on the website with specified class
genomeTable = parsedHtml.findAll('table', {'class': 'wikitable'})
genomeTable = genomeTable[0]

# Length of a variabel
# len(genomeTable)

# Get all table headers
headers = genomeTable.findAll('th', {})

# Loop through headers and store in headerTexts
headerTexts = []

for header in headers:
    # Append headers to array and cut of \n at the end of the line
    headerTexts.append(header.text[:-1])
    
# ['Organismus\n', 'Genomgröße1\n', 'Gene\n', 'Gendichte2\n']
# [:-1] => ['Organismus', 'Genomgröße1', 'Gene', 'Gendichte2']

#print("Header texts\n", headerTexts)

# Get all table rows with tr
allRows = genomeTable.findAll('tr', {})
rowData = allRows[1:] # Cut first header row off

# Loop through rows and store in separate array in array tableRows
tableRows = []

for rows in rowData:
    rowText = []

    for text in rows:
        if type(text) is element.Tag:
            rowText.append(text.text[:-1])
    
    if type(rows) is element.Tag:
        tableRows.append(rowText)

#print(headerTexts)

# Loop through arrays in arrays tableRows
#for i in range(len(tableRows)):
    #print(tableRows[i])

# Write data into csv sheet
headersString = ''

# Loop through arrays and add values as string to headersString
for title in headerTexts:
    headersString += str(title) + ','
    
headersString = headersString[:-1] # Remove last ,
headersString = headersString + '\n' # Add line

#print(headersString)

# Write to file genome.csv
with open('genome.csv', "w", encoding="utf-8") as f:
    f.write(headersString)

    # Loop through rowTexts
    for rows in tableRows:
        rowsString = ''

        # Store array values as string into rwsString
        for column in rows:
            column = column.replace(',', '.') # Replace comme with period
            column = re.sub(r'\[\d+\]', '', column) # Remove [29]
            rowsString += str(column) + "," # Separate by commas
        
        rowsString = rowsString[:-1] # Remove last comma
        rowsString +=  '\n'
        #print(rowsString)

        # Write fromatted string to csv file
        f.write(rowsString)

# Close file
f.close()
print("Success!")

references = parsedHtml.findAll('div', {'class': 'reflist'})

refLinks = []

for link in references:
    links = link.findAll('a', {'class': 'external text'})
    
    for a in links:
        refLinks.append(a.text)
print(refLinks)
