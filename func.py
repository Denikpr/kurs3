import json

def load_operation():
    with open('operations.json', encoding='utf-8') as file:
        operations = json.load(file)
    return operations

