'''
This script provides generic input that will be provided to the 
different modules created in this repository
'''

from querycreator import indicatorCaseStatements
from createTables import createIndTab
from insertTables import InsertIndQuery

''' 
Columns will be a map that will be created as:
    columns = {'<NameofAttributeTobeDelivered>': 
                     {'Dependencies':[<ListOfColumnsThatAreRequiredToBuildIndicator>], 
                        'Versions':[<DifferentVersionsInWhichToExist]}}
                        
''' 


columns = {'AnyCustContact': {'Dependencies': 'CustContact', 'Versions': [3,6,12,24,-1], 'Type': 'Indicator'},
           'AnySales': {'Dependencies': 'Sales', 'Versions': [3,6,9,12,24], 'Type': 'Indicator'} }
## Ok I see issues here is two maps have the same keys; 
## Perhaps it is better to have specific in/out related keys. 
indata = {'inschema': 'inSchema', 'intable': 'INtable'}
outdata = {'outschema': 'outSchema', 'outtable': 'OUTtable'}
primarycols = [('CustID', 'varchar (255)'), ('TimePeriod', 'int')]

#print(indicatorCaseStatements(columns))
#print(createIndTab(outdata, primarycols, columns))
print(InsertIndQuery(indata, outdata, primarycols, columns))
