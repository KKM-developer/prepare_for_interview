#Написать функцию (несколько функций), реализующую вывод таблицы умножения размерностью AｘB.
#Первый и второй множитель должны задаваться в виде аргументов функции.


def multiplication_table(a, b):
    return [print(f'{i} x {n} = {i*n}') for i in range(1, a+1) for n in range(1, b+1)]

multiplication_table(3, 3)
print('-'*9)
multiplication_table(2, 2)
print('-'*9)
multiplication_table(1, 4)