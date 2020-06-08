'''
This script provides generic input that will be provided to the 
different modules created in this repository
'''

from querycreator import indicatorCaseStatements
from createTables import createIndTab

''' 
Columns will be a map that will be created as:
    columns = {'<NameofAttributeTobeDelivered>': 
                     {'Dependencies':[<ListOfColumnsThatAreRequiredToBuildIndicator>], 
                        'Versions':[<DifferentVersionsInWhichToExist]}}
''' 
columns = {'AnyCustContact': {'Dependencies': 'CustContact', 'Versions': [3,6,12,24,-1]},
           'AnySales': {'Dependencies': 'Sales', 'Versions': [3,6,9,12,24]} }

outdata = {'schema': 'schmtest', 'table': 'tabletest'}
primarycols = [('CustID', 'varchar (255)'), ('TimePeriod', 'int')]

print(indicatorCaseStatements(columns))
print(createIndTab(outdata, primarycols, columns))

