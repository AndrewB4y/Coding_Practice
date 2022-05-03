import json
import csv

"""
formato csv:

"name","description","keywords","sku_reference"
Camisa,"Tipo de condensador de polipropileno de clase trifásico para mejorar coeficiente de potencia con una potencia pasiva de 5kVAR, 15kVAR",,NODUP-50
Pintura Sofia,La mejor pintura para tu hogar,,SKUPRUEBA

"""

filename = "test.csv"

col_sep = ","

try:
    with open(filename) as f:
        pass
except IOError:
    print("[Fail] Filename not accesible")

file_dicts = []
with open(filename) as f:
    a_reader = csv.reader(f, delimiter=',', quotechar='"')
    cols = next(a_reader)
    for row in a_reader:
        file_dicts.append(json.dumps(dict(zip(cols, row))))

print(file_dicts)