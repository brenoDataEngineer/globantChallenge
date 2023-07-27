import csv
from faker import Faker

# Iniciar a instância da biblioteca.
fake = Faker()

# Definir o número de linhas que queremos em nossa amostragem
num_rows = 30

# Definir os campos do arquivo CSV.
field_names = ['id','job']

# Gera os dados e salva no arquivo CSV
with open('files/jobs.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()

    for _ in range(num_rows):
        id = fake.unique.random_int(min=10, max=10000)
        job = fake.word()

        writer.writerow({
            'id': id,
            'job': job

        })

print("Data generated and saved to 'sample_data.csv'.")
