import csv
import random
from datetime import date, timedelta

column_headers = ['Bedrag', 'Leen_Donatie','Leeftijd', 'Datum']
num_rows = 150

# Generate random data for each row
data = []
for _ in range(num_rows):
    bedrag = random.randint(50, 2000)
    leen_donatie = random.choice(['leen', 'donatie'])
    leef_tijd = random.randint(18, 100)
    start_date = date.today() + timedelta(days=1)
    end_date = date(date.today().year, 8, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    datum = random_date.strftime('%Y-%m-%d')
    data.append([bedrag, leen_donatie, leef_tijd, datum])

# Write data to a CSV file
filename = 'random_data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(column_headers)
    writer.writerows(data)

print(f"CSV file '{filename}' has been generated with {num_rows} rows.")