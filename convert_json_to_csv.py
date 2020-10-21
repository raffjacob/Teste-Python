import csv, json

csvDir = '.\intern-python-test-main\gerados\convertido.csv'
jsonDir = '.\intern-python-test-main\json\shopping.json'

# Leitura do arquivo JSON
with open(jsonDir, "r") as jsonFile:
    dados = json.load(jsonFile)
jsonFile.close

# Escrita do arquivo CSV
with open(csvDir, "w") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter = "|")
    csvWriter.writerow(["id", "name", "description", "quantity", "value", "total"])
    total = 0
    for item in dados["order"]:
        # Cálculo de total e criação das linhas
        item['total'] = item['quantity'] * item['value']
        csvWriter.writerow([item['id'], item['name'], item['description'], item['quantity'], item['value'], item['total']])    
        total += item['total']
    csvWriter.writerow(["Total", "", "", "", "", total])
csvFile.close