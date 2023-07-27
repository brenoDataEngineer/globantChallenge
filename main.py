from historicalData import extractAndLoad
from restoreBackuo import restoreBackup
from backupTables import backupTables
from apiInteractPost import apiInteractPost

def main():
    print("Welcome to the Data Processing Challenge!")
    while True:
        print("\nSelect an option:")
        print("1. Move historical data into SQL database")
        print("2. Post JSON data into API")
        print("3. Backup tables to AVRO")
        print("4. Restore Backups from AVRO")
        print("5. Exit")

        choice = input("Enter the number corresponding to your choice: ")

        if choice == "1":
            # Move historical csv data into SQL database.
            extractAndLoad('jobs.csv', 'globant_jobs')
            extractAndLoad('hired_employees.csv', 'globant_hired_employees')
            extractAndLoad('departments.csv', 'globant_departments')
        elif choice == "2":
            # Post JSON 1000 into API
            apiInteractPost()
        elif choice == "3":
            # Backup tables to AVRO
            backupTables('jobs.csv', 'jobs.avro', 'globant_jobs')
            backupTables('hired_employees.csv', 'hired_employees.avro', 'globant_hired_employees')
            backupTables('departments.csv', 'departments.avro', 'globant_departments')
        elif choice == "4":
            # Restore Backup
            restoreBackup('jobs.avro', 'globant_jobs')
            restoreBackup('hired_employees.avro', 'globant_hired_employees')
            restoreBackup('departments.avro', 'globant_departments')
        elif choice == "5":
            print("Process ended.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()