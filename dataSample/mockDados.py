import csv
from faker import Faker

# Iniciar a instância da biblioteca.
fake = Faker()

# Definir o número de linhas que queremos em nossa amostragem
num_rows = 1000

# Definir os campos do arquivo CSV.
field_names = ['company_id', 'project_id', 'project_name', 'floor_id', 'activity_name',
               'floor_name', 'start_at', 'end_at', 'totalProjectCost', 'basic_team_id',
               'activity_id', 'progress_date', 'realized', 'updateDate', 'base',
               'productivity', 'unit_name', 'total_effort', 'work_type', 'work_id', 'quantity',
               'material_resource_name', 'material_resource_id']

# Gera os dados e salva no arquivo CSV
with open('sample_histograma.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()

    for _ in range(num_rows):
        company_id = fake.random_int(min=1, max=1000)
        project_id = fake.random_int(min=1, max=1000)
        project_name = fake.company()
        floor_id = fake.random_int(min=1, max=100000)
        activity_name = fake.job()
        floor_name = fake.word()
        start_at = fake.date()
        end_at = fake.date()
        totalProjectCost = fake.pyfloat(left_digits=6, right_digits=2, positive=True)
        basic_team_id = fake.random_int(min=1, max=100000)
        activity_id = fake.random_int(min=1, max=100000)
        progress_date = fake.date()
        realized = fake.pyfloat(left_digits=1, right_digits=5, positive=True)
        updateDate = fake.date()
        base = fake.pyfloat(left_digits=1, right_digits=5, positive=True)
        productivity = fake.pyfloat(left_digits=1, right_digits=1, positive=True)
        unit_name = fake.word()
        total_effort = fake.pyfloat(left_digits=1, right_digits=1, positive=True)
        work_type = fake.job()
        work_id = fake.random_int(min=1, max=1000000)
        quantity = fake.random_int(min=1, max=100)
        material_resource_name = fake.word()
        material_resource_id = fake.random_int(min=1, max=10000)

        writer.writerow({
            'company_id': company_id,
            'project_id': project_id,
            'project_name': project_name,
            'floor_id': floor_id,
            'activity_name': activity_name,
            'floor_name': floor_name,
            'start_at': start_at,
            'end_at': end_at,
            'totalProjectCost': totalProjectCost,
            'basic_team_id': basic_team_id,
            'activity_id': activity_id,
            'progress_date': progress_date,
            'realized': realized,
            'updateDate': updateDate,
            'base': base,
            'productivity': productivity,
            'unit_name': unit_name,
            'total_effort': total_effort,
            'work_type': work_type,
            'work_id': work_id,
            'quantity': quantity,
            'material_resource_name': material_resource_name,
            'material_resource_id': material_resource_id
        })

print("Data generated and saved to 'sample_data.csv'.")
