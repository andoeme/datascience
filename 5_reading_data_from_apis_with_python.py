from urllib.request import urlopen
import json

# Read JSON Data from API and store into CSV file

# Open URL
url = 'https://data.qld.gov.au/api/action/datastore_search?resource_id=0ca6f77c-4088-4d77-8c88-beae2b57ce14&limit=20'
fileobj = urlopen(url)

# Save json data in variable
rawData = fileobj.read()
fileobj.close()

# Parse JSON data to string
jsonData = json.loads(rawData)
jsonString = json.dumps(jsonData)

# Store the wanted values from the JSON data
govRecords = []

# Loop through the 5 results in jsonData and store in array govRecords
for records in jsonData['result']['records']:    
    govRecords.append([records['_id'],
                       records['TIMESTAMP'],
                       records['DCS_ABSSpd_Avg'],
                       records['DCS_Direction_Avg']])

# Open (create if not existing already) file goverment_data.csv
with open('goverment_data.csv', "w", encoding="utf-8") as f:
    f.write('Id, Date Time, Speed, Average Direction\n')

    # Add data to a comma seperated string govdata
    for datasets in govRecords:
        govData = ''
        for data in datasets:
            govData += ', ' + str(data)

        # Format and write to file
        govData = govData[1:]
        govData += '\n'
        f.write(govData)
        
# Close file
f.close()


########################################################################
########################################################################
###############                                             ############
           # Read JSON Data from API and store into CSV file

from bs4 import BeautifulSoup as soup # Parser
from bs4 import element

url = 'https://data.qld.gov.au/dataset/161e4c2b-7ab8-42a5-9db1-109116143cba/resource/4c11f459-5084-4bb5-9fbd-8de6c7440916/download/20140326__qcs_community-service-work-performed-court-ordered_community-service-work-performed-ja.xml'
fileobj = urlopen(url)

# Save xml data in variable
rawData = fileobj.read()
fileobj.close()

parsedXML = soup(rawData, 'xml')
#print(parsedXML)

govXMLData = []

for datasets in parsedXML.find_all('table1_Group1'):    
    for tableData in datasets.find_all('table1_Group2'):
        #print(datasets['Region_Short_nme'], datasets['Completed_Hrs_3'])
        #print(tableData['District_Short_nme'], tableData['Completed_Hrs_2'])
        govXMLData.append([tableData['District_Short_nme'],
                           tableData['Completed_Hrs_2']])
#print(govXMLData)

# Open (create if not existing already) file goverment_data.csv
with open('goverment_xml_data.csv', "w", encoding="utf-8") as f:
    f.write('District Short Name, Completed HRS 2\n')
            
    # Add data to a comma seperated string govXMLData
    for arrays in govXMLData:
        govData = ''
        
        for data in arrays:
            govData += ', ' + str(data)
        
        # Format and write to file
        govData = govData[1:]
        govData += '\n'
        f.write(govData)
        
# Close file
f.close()
    
