import sys
import os
''' 
    This function returns if the statement passed to the function is valid SQL Statement or not 

    Input:
    statement: String expected with full SQL Statement

    Output:
        Success as a string or Errors which were raised while validating.
''' 
SourceFolder = os.getcwd() 

def ValidateSQLStatement(statement):
    ValidationFile = SourceFolder  + "\\"+ 'Request.sql'
    fhandle = open(ValidationFile, 'w')
    fhandle.write(statement)
    fhandle.close()
    result = os.system(SourceFolder + "\\TSQLParser\\TSQLParser.exe " + ValidationFile)
    return result

