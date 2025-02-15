"результат операции: 42"
"результат операции: 514"
"результат операции: 9"


result_operation = input("Please enter any of the lines listed above: ")
num = ""
for number in result_operation:
    if number in "1234567890":
        num += number
    else:
        number = number
if num in result_operation:
    result_num = result_operation[result_operation.index(num):].strip('"')
    print(int(result_num) + 10)
