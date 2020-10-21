import csv, json

csvDir = '.\intern-python-test-main\csv\shopping.csv'
jsonDir = '.\intern-python-test-main\gerados\convertido.json'

dados = {}
order = {}

# Leitura do arquivo CSV
with open(csvDir, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter = "|")
    calc = 0
    total = 0
    for linha in csvReader:
        ID = linha['ID']
        dados[ID] = linha
        # Cálculo do total
        calc = float(linha['Quantity'])*float(linha['Value'])
        total += calc
    dados["Total"] = total 
    order["order"] = dados    
csvFile.close

# Criação do arquivo JSON
with open(jsonDir, 'w', encoding="utf-8") as jsonFile:
    jsonFile.write(json.dumps(order, indent=4))
jsonFile.close