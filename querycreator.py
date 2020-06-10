def indicatorCaseStatements(columns):
    attrCase = '' 
    for outAttribute in columns:
        AttName = columns[outAttribute]['Dependencies']
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
            '''.format(**{'attribute': AttName, 'val':mversion, 'outputname': outName})
    return attrCase.rstrip()[:-1].lstrip().rstrip()

def AttributeNameCreator(columns):
    ''' 
    This function returns the name of the attribute with a suffix of:
        _XM where X is the Version number
        When X = -1, then this suffix is _Ever
    ''' 
    return [x+"_"+str(y)+"M" if y!= -1 else x+"_"+"Ever" for x in columns for y in columns[x]['Versions']]




__author__ = 'Akshay Katre'
__copyright__ = 'Copyright 2020, Query Builder'
__credits__ = ['Akshay Katre']
__version__ = '0.1'
#__maintainer__ = '{maintainer}'
__email__ = 'akshaykatre@gmail.com'
#__status__ = '{dev_status}'