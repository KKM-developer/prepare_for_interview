'''
2. Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она
отвечает сообщением, целое оно или дробное. Если дробное — необходимо далее выполнить
сравнение чисел до и после запятой. Если они совпадают, программа должна возвращать значение True, иначе False.

3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None. Значения,
которым не хватило ключей, необходимо отбросить.
'''
def int_or_float(number):
    try:
        int(number)
        return f'Число целое'
    except:
        try:
            float(number)
            print('число дробное')
            number = number.split('.')
            if number[0] == number[1]:
                return True
            else:
                return False
        except:
            return f'Вы ввели не число'

def get_dict(key_list, value_list):
    res = {}
    for key in range(len(key_list)):
        try:
            res[key_list[key]] = value_list[key]
        except:
            res[key_list[key]] = None
    return res

print(int_or_float(input('Введите число ')))

print(get_dict([1, 2, 3], ['sdd', 12]))