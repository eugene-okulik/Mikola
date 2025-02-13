return_result_one = 'результат операции: 42'
return_result_two = 'результат операции: 514'
return_result_three = 'результат операции: 9'

print(int(return_result_one[return_result_one.index('42'):]) + 10)
print(int(return_result_two[return_result_two.index('514'):]) + 10)
print(int(return_result_three[return_result_three.index('9'):]) + 10)
