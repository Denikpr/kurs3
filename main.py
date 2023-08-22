from func import load_operation, is_executed, sort_date, last_five_operations, create_message


operations = load_operation()

executed = is_executed(operations)

sorted = sort_date(executed)

last_operations = last_five_operations(sorted[:5], executed)

for item in range(5):
    print(create_message(last_operations[item]))
    