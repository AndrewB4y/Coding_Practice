import csv
from operator import delitem

from numpy import c_


file_name = 'simple_copy.csv'

if '.csv' not in file_name:
    file_name += '.csv'

"""
dictionary blueprint

{
    "L1": {
        #cod_con#"1": {
            "val": 123,
            "sum_res": 0123,
        },
        "{cod_con}": {
            "val": 123,
            "sum_res": 0123,
        }
    },
    "L2": {
        #cod_con#"11": {
            "val": 123,
            "sum_res": 0123,
        },
        "{cod_con}": {
            "val": 123,
            "sum_res": 0123,
        }
    },
    "L4": {
        #cod_con#"1101": {
            "val": 123,
            "sum_res": 0123,
        },
        "{cod_con}": {
            "val": 123,
            "sum_res": 0123,
        }
    }
}
"""

# Preparing analysis structure
codes_dict = {}
all_levels = set()
original = []
with open(file_name, newline='', encoding='utf-8-sig') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quotechar='"')
    cols = next(lines)
    original.append(cols)
    for line in lines:
        original.append(line)
        c_num = line[0]
        all_levels.add(len(c_num))
        level = "L"+str(len(c_num))
        if not codes_dict.get(level):
            codes_dict[level] = {}

        if not codes_dict[level].get(c_num):
            codes_dict[level][c_num] = {
                "valor": int(line[2]),
                "claseConcepto": line[1],
                "sum_res": 0,
                "has_parent": True,
                "status": ""
            }
            if line[2] == '0':
                codes_dict[level][c_num]['status'] = "* Cuenta en cero // "
        else:
            val = codes_dict[level][c_num]
            val['status'] = val ['status'] + "* Cuenta repetida // "
            if line[2] == '0':
                val['status'] = val['status'] + "* Instancia repetida en 0 // "
            else:
                val['valor'] += int(line[2])

# print(codes_dict)
# Analysing data
all_levels = list(all_levels)
all_levels.sort(reverse=True)
# print(codes_dict)
for idx, level in enumerate(all_levels):
    if level == 1:
        break
    prev_level = all_levels[idx + 1]
    level_name = "L"+str(level)
    prev_level_name = "L"+str(all_levels[idx + 1])
    print(level_name)
    for code in codes_dict[level_name]:
        parent_code = code[:(prev_level - level)]
        if not codes_dict.get(prev_level_name).get(parent_code):
            codes_dict[level_name][code]["has_parent"] = False
            continue
        codes_dict[prev_level_name][parent_code]["sum_res"] += codes_dict[level_name][code]["valor"]

# print(codes_dict)
for idx, level in enumerate(all_levels):
    if idx == 0:
        continue
    level_name = "L"+str(level)
    print(level_name)
    for code in codes_dict[level_name]:
        val = codes_dict[level_name][code]
        if val['valor'] != val['sum_res']:
            val['status'] = val['status'] + "* [Error] Comparar sumatoria: " + str(val['sum_res'])
        else:
            val['status'] = val['status'] + "* Ok sumatoria: " + str(val['sum_res'])

# print(codes_dict)

output_file = 'resultado_analisis.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for idx, line in enumerate(original):
        if idx == 0:
            line.append('')
            writer.writerow(line)
            continue
        c_num = line[0]
        level = "L"+str(len(c_num))
        val = codes_dict[level][c_num]
        if not val['has_parent']:
            line.append("sin cuenta padre")
        else:
            if val.get('status'):
                line.append(val['status'])
            else:
                line.append('')
        writer.writerow(line)
