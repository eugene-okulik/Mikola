#  результат операции: 42
#  результат операции: 54
#  результат работы программы: 504
#  результат: 2


#  It was!!!!!!
# result_operation = input("Please enter any of the lines listed above: ")
# num = ""
# for number in result_operation:
#   if number in "1234567890":
#       num += number
#   else:
#       number = number
# if num in result_operation:
#   result_num = result_operation[result_operation.index(num):].strip('"')
#   print(int(result_num) + 10)

# Has become!!!!!!
#  С использованием: index()
def search_number(text: str) -> int:
    index_numbers = text.index(':') + 1
    return int(text[index_numbers:]) + 10


print(search_number(input("Введите пожалуйста образец любого текста"
                          " напечатонного выше: ")))


#  С использованием: split()
def search_number2(text2):
    number = [num for num in text2.split() if num.isdigit()]
    return int(*number) + 10


print(search_number2(input("Введите пожалуйста образец любого"
                           " текста напечатонного выше: ")))
