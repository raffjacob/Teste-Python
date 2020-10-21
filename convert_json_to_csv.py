import csv, json

csvDir = '.\intern-python-test-main\gerados\convertido.csv'
jsonDir = '.\intern-python-test-main\json\shopping.json'

# Leitura do arquivo JSON
with open(jsonDir, "r") as jsonFile:
    dados = json.load(jsonFile)
jsonFile.close

# Escrita do arquivo CSV
with open(csvDir, "w") as csvFile:
    csv_csvFile = csv.writer(csvFile, delimiter = "|")
    csv_csvFile.writerow(["id", "name", "description", "quantity", "value", "total"])
    total = 0
    for item in dados["order"]:
        # Cálculo de total e criação das linhas
        item['total'] = item['quantity'] * item['value']
        csv_csvFile.writerow([item['id'], item['name'], item['description'], item['quantity'], item['value'], item['total']])    
        total += item['total']
    csv_csvFile.writerow(["Total", "", "", "", "", total])
csvFile.close