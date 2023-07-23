from historicalData import extractAndLoad
from restoreBackuo import restoreBackup
from backupTables import backupTables

def fullProcessChallenge():
    
    #Move historical csv data into SQL database.
    extractAndLoad('jobs.csv', 'jobs')
    extractAndLoad('hired_employees.csv', 'hired_employees')
    extractAndLoad('departments.csv', 'departments')
  
    #Post JSON 1000 into API


    #Backup tables to AVRO
    backupTables('jobs.csv', 'jobs')
    backupTables('hired_employees.csv', 'hired_employees')
    backupTables('departments.csv', 'departments')

    #Restore Backup
    restoreBackup('jobs.csv', 'jobs')
    restoreBackup('hired_employees.csv', 'hired_employees')
    restoreBackup('departments.csv', 'departments')

    return


fullProcessChallenge()