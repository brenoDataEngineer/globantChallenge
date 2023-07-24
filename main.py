from historicalData import extractAndLoad
from restoreBackuo import restoreBackup
from backupTables import backupTables
from apiInteractPost import apiInteractPost

def fullProcessChallenge():
    
   
    #Move historical csv data into SQL database.
    extractAndLoad('jobs.csv', 'globant_jobs')
    extractAndLoad('hired_employees.csv', 'globant_hired_employees')
    extractAndLoad('departments.csv', 'globant_departments')
   
    #Post JSON 1000 into API
    apiInteractPost()
    
    #Backup tables to AVRO
    backupTables('jobs.csv', 'jobs.avro', 'globant_jobs')
    backupTables('hired_employees.csv', 'hired_employees.avro', 'globant_hired_employees')
    backupTables('departments.csv', 'departments.avro', 'globant_departments')
    
    #Restore Backup
    restoreBackup('jobs.avro', 'globant_jobs')
    restoreBackup('hired_employees.avro', 'globant_hired_employees')
    restoreBackup('departments.avro', 'globant_departments')

    return 'Processo encerrado'


fullProcessChallenge()