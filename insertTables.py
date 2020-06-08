
def InsertIndQuery(indata_connection, outdata_connection, primcols, columns):
    insertStatement = '''INSERT INTO {outschema}.{outtable}
    SELECT {primcols}, 
           {collist}
    FROM {inschema}.{intable}
    ''' 