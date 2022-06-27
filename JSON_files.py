"""
JSON File (fisiere JSON)
JSON - format usor de interschimbare a datelor
     - un standard derivat de JavaScript
     - JavaScript Object Notation (notatia Javascript)

Modulul json permite lucrul cu tipul de fisiere JSON(bilt-in in Python)
Documentatie oficiala:
    https://docs.python.org/3/library/json.html#encoders-and-decoders
JSON: https://www.json.org/json-ro.html
JSON: este contruit pe baza a doua structuri:
1. o colectie de perechi nume/ valoare (obiect)
2. o lista de valori (un tablou/ array)

Lucrul cu fisiere JSON presupune:
1. Citirea / Deserializare / Decodare
    - conversie a unui fisier JSON intr-un obiect din Python
    (dict/ list)
    Metoda json.load(file_handler)
2. Scrierea / Serializare / Codificare
    - conversia unui obiect din Python intr-un fisier JSON
    - obiectele Python sunt transformate intr-o serie de bytes (caractere
    UNICODE) pentru a fi salvate si transmise in retea
    Metoda json.dump(object, file_handler)

Serializarea se poate realiza si cu conversia in string
string_variable = json.dumps(object)

Deserializarea se poate realiza si pe baza unui string:
    Object - json.loads(string_JSON)
"""

import json
import os

# with open('data\data.json', 'r') as f:
with open(os.path.join('data', 'data.json'), 'r') as f:
    data = json.load(f)
    print(f'Tipul de datelor: {type(data)}')
    print(f'Deserializare JSON: {data}')

with open('data/employees.json', 'r') as f:
    employees_data = json.load(f)
    print(type(employees_data))
    print(f'Datele din json deserializate: {employees_data}')

employees_data['employees'][1]['salary'] = 9000
with open('data/new_employees.json', 'w') as f:
    json.dump(employees_data, f, indent=2)

# serialization into string object
employees_string = json.dumps(employees_data, indent=2)
print(employees_string)

languages = """
    {
        "Python": 3.8,
        "JavaSCript": "ES6",
        "PHP": 7.4
    }
    """
languages_dict = json.loads(languages)
print(f'Deserializarea stringului: {languages_dict}')
print(type(languages_dict))
