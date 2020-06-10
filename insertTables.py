''' 
For insert statements, we need a different treatment of the 
tuples and dictionaries that we use. 

These will be handled here in separate functions.
''' 
import pdb 

def primNames(primcols):
    return [name[0] for name in primcols]


def InsertIndQuery(indata_connection, outdata_connection, primcols, columns):
    primaryNames = primNames(primcols)

    insertDict = {'primcols': ', \n'.join(primaryNames), 'collist': ', \n'.join(columns.keys())}

    insertStatement = '''INSERT INTO {outschema}.{outtable}
    SELECT {primcols}, 
           {collist}
    FROM {inschema}.{intable}
    '''.format(**insertDict, **outdata_connection, **indata_connection)

    return insertStatement