import json

filename = 'operations.json'

def load_operation():
    with open(filename, encoding='utf-8') as file:
        load_operations = json.load(file)
    operations = []
    for load_operation in load_operations:
        operations.append(load_operation)
    return operations