''' 
For insert statements, we need a different treatment of the 
tuples and dictionaries that we use. 

These will be handled here in separate functions.
''' 
import pdb 
from querycreator import indicatorCaseStatements 

def primNames(primcols):
    return [name[0] for name in primcols]


def InsertIndTabQuery(indata_connection, outdata_connection, primcols, columns):
    ''' 
    This function is primarily ONLY when you want to create a set of indicators with primary keys.

    TO DO: 
        - Create a more modular insert statement? One that takes indicators, sums, etc? In a different function?
    ''' 
    primaryNames = primNames(primcols)
    
    insertDict = {'primcols': ', \n'.join(primaryNames), 'collist': indicatorCaseStatements(columns)}

    insertStatement = '''INSERT INTO {outschema}.{outtable}
    SELECT {primcols}, 
           {collist}
    FROM {inschema}.{intable}
    '''.format(**insertDict, **outdata_connection, **indata_connection)

    return insertStatement