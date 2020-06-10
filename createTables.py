from querycreator import AttributeNameCreator

def primarystatement(primcols):
    ''' 
        This function returns the statements used to create the primary columns;

        primcols is a list of tuples that holds the column names that are to be created 
        and the data type they should hold
        primcols = [('<colname1>', '<col1datatype>'), ('<colname2>', '<col2datatype>')]

        This function will return: 
            <colname1> <col1datatype> , \n <colname2> <col2datatype> 
    ''' 
    return ' , \n '.join(['{0} {1}'.format(y,z) for y,z in primcols])


    
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

    TO DO: 
        - Account for when the server and database name is also provided
        - Make the drop statement optional? 
    ''' 
    indicatorcols = AttributeNameCreator(columns)
    #indicatormap = {'collist': indicatorcols}
    indicatorstatement = ' bit, \n'.join(indicatorcols) + ' bit'
    if 'schema' not in outdata_connection.keys():
        print("Setting the schema to dbo")
        outdata_connection.update({'schema': 'dbo'}) 
    primstatement = primarystatement(primcols)
    cstatement = ''' 
        DROP TABLE IF EXISTS {outschema}.{outtable} \n
        create table {outschema}.{outtable}(
            {0},
            {1}
        )
    '''.format(primstatement, indicatorstatement,**outdata_connection)
    return cstatement.lstrip().rstrip()