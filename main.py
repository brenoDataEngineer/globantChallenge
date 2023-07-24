from historicalData import extractAndLoad
from restoreBackuo import restoreBackup
from backupTables import backupTables
from apiInteractPost import apiInteractPost

def fullProcessChallenge():
    
    #Move historical csv data into SQL database.
    # extractAndLoad('jobs.csv', 'jobs')
    # extractAndLoad('hired_employees.csv', 'hired_employees')
    # extractAndLoad('departments.csv', 'departments')
  
    #Post JSON 1000 into API
    #apiInteractPost()

    #Backup tables to AVRO
    # backupTables('jobs.csv', 'jobs.avro', 'jobs')
    # backupTables('hired_employees.csv', 'hired_employees.avro', 'hired_employees')
    # backupTables('departments.csv', 'departments.avro', 'departments')

    #Restore Backup
    # restoreBackup('jobs.avro', 'jobs')
    # restoreBackup('hired_employees.avro', 'hired_employees')
    # restoreBackup('departments.avro', 'departments')

    return


fullProcessChallenge()