def queryCaseStatements(columns):
    attrCase = '' 
    for outAttribute in columns:
        AttName = outAttribute
        ## Loop over versions required of the column 
        for mversion in columns[outAttribute]['Versions']:
            outName = outAttribute + '_' + str(mversion) + "_M" if mversion != -1 else outAttribute + '_Ever' + "_M"
            ## You subtract from 1 because you include the current time period 
            mversion = mversion-1 if mversion != -1 else 'UNBOUNDED'

            attrCase += '''
            CASE WHEN SUM(Convert(INT, {attribute})) OVER (PARTITION BY FACILITYID ORDER BY MEASUREMENTPERIODID ROWS {val}) >= 1 
            THEN 1
            ELSE 0 
            END AS {outputname},
            '''.format(**{'attribute': outAttribute, 'val':mversion, 'outputname': outName})
    return attrCase.rstrip()[:-1]

def AttributeNameCreator(columns):
    ''' 
    This function returns the name of the attribute with a suffix of:
        _XM where X is the Version number
        When X = -1, then this suffix is _Ever
    ''' 
    return [x+"_"+str(y)+"M" if y!= -1 else x+"_"+"Ever" for x in columns for y in columns[x]['Versions']]

def createIndTab(outdata_connection, primcols, columns):
    ''' 
    This is to create a table that will be used for fields that are indicators i.e. data type bit; 

    To create a table, we need the following information:
        - List of columns that are the identifiers/ primary keys of the table
        - The name and schema of the table; the server and database information is optional
        - The list of columns that will be created are already available

    outdata_connection is a dict with information about the output data, it has the 
    following format
        outdata_connection = {'server': <servername>, 
                              'database': <dbname>,
                              'schema': <schemaname>,
                              'table': <tablename>}

    primcols is a list of tuples that holds the column names that are to be created 
    and the data type they should hold
        primcols = [('<colname1>', '<col1datatype>'), ('<colname2>', '<col2datatype>')]
    ''' 
    indicatorcols = AttributeNameCreator(columns)
    #indicatormap = {'collist': indicatorcols}
    indicatorstatement = ' bit, \n'.join(indicatorcols) + ' bit'
    if 'schema' not in outdata_connection.keys():
        print("Setting the schema to dbo")
        outdata_connection.update({'schema': 'dbo'}) 
    primstatement = ' , \n '.join(['{0} {1}'.format(y,z) for y,z in primcols])
    cstatement = ''' 
        DROP TABLE IF EXISTS {schema}.{table} \n
        create table {schema}.{table}(
            {0},
            {1}
        )
    '''.format(primstatement, indicatorstatement,**outdata_connection)
    return cstatement



__author__ = 'Akshay Katre'
__copyright__ = 'Copyright 2020, Query Builder'
__credits__ = ['Akshay Katre']
__license__ = 'MIT License'
__version__ = '0.1'
#__maintainer__ = '{maintainer}'
__email__ = 'akshaykatre@gmail.com'
#__status__ = '{dev_status}'