from querycreator import queryCaseStatements, createIndTab

''' 
Columns will be a map that will be created as:
    columns = {'<NameofAttributeTobeDelivered>': 
                     {'Dependencies':[<ListOfColumnsThatAreRequiredToBuildIndicator>], 
                        'Versions':[<DifferentVersionsInWhichToExist]}}
''' 
columns = {'AnyRebTrigger': {'Dependencies': 'RebTrigger', 'Versions': [3,6,12,24,-1]},
           'AnySales': {'Dependencies': 'Sales', 'Versions': [3,6,9,12,24]} }

outdata = {'schema': 'schmtest', 'table': 'tabletest'}
primarycols = [('FacilityID', 'varchar (255)'), ('MeasurementPeriodID', 'int')]

print(queryCaseStatements(columns))
print(createIndTab(outdata, primarycols, columns))
