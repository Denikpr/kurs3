import json

filename = 'operations.json'

def load_operation():
    '''
    Загружаем данные из json файла
    Возвращаем словарь.
    '''
    with open(filename, encoding='utf-8') as file:
        load_operations = json.load(file)
    operations = []
    for load_operation in load_operations:
        operations.append(load_operation)
    return operations

def is_executed(operations):
    '''
    Делаем выборку из словаря по EXECUTED
    Возвращаем словать.
    '''
    operation_executed = []
    for operation in operations:
        if 'state' in operation and operation['state'] =='EXECUTED':
            operation_executed.append(operation)
    return operation_executed
