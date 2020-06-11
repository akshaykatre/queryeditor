import sqlvalidator as sv
''' 
    This function returns if the statement passed to the function is valid SQL Statement or not 

    Input:
    statement: String expected with full SQL Statement

    Output:
        Success as a string or Errors which were raised while validating.
''' 
def ValidateSQLStatement(statement):
    s = sv.parse(statement)
    if not s.is_valid():
        return s.errors
    return 'Success'
