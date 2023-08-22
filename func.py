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
    Делаем выборку из словаря по EXECUTED,
    Возвращаем словать.
    '''
    operation_executed = []
    for operation in operations:
        if 'state' in operation and operation['state'] =='EXECUTED':
            operation_executed.append(operation)
    return operation_executed

def sort_date(operation_executed):
    '''
    Делаем сортировку по дате,
    последние на первом месте(reverse).
    '''
    datelist = []
    for oper in operation_executed:
        if 'date' in oper:
            datelist.append(oper['date'])
    datelist.sort(reverse = True)
    return datelist

def last_five_operations(last_five_times,operation_executed):
    '''
    Делаем словарь из 5 полседних операций.
    '''
    result = {}
    for oper in operation_executed:
        if 'date' in oper and oper['date'] in last_five_times:
            result[last_five_times.index(oper['date'])] = oper
    return result

def create_message(operation):
    '''
    Формируем вывод сообщения в нужной форме.
    '''
    return f'''{operation['date'][:10]} {operation['description']}
{create_from(operation)} -> {create_to(operation)}
{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']} 
'''

def create_from(operation):
    '''
    Маскируем номер счета и номер карты,
    в операции от кого.
    '''
    result = ''
    number = ''
    if 'from' not in operation:
        return "cash"
    card_list = operation['from'].split()
    for item in card_list:
        if item.isalpha():
            result += item + " "
        else:
            number += item
    if 'Счет' in operation['from']:
        result += '**' + number[-4:]
    else:
        result += number[:4] + ' ' + number[4:6] + '** **** ' + number[-4:]
    return result