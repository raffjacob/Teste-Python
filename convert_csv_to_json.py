import csv, json, codecs

csvDir = '.\intern-python-test-main\csv\shopping.csv'
jsonDir = '.\intern-python-test-main\gerados\convertido.json'

dados = {}
order = {}

# Leitura do arquivo CSV
with open(csvDir, 'r') as CsvFile:
    csvReader = csv.DictReader(CsvFile, delimiter = "|")
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
CsvFile.close

# Criação do arquivo JSON
with open(jsonDir, 'w', encoding="utf-8") as JsonFile:
    JsonFile.write(json.dumps(order, indent=4))
JsonFile.close