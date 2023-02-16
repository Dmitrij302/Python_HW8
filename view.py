def get_op():
    op = int(input('1 - добавить студента, 2 - добавить предмет, 3 - добавить оценку, 4 - показать список студентов 5 - показать список оценок конкретного ученика, 6 - выйти\n'))
    return op

def in_student():
    names = input("Введите имя, фамилию студента: ")
    return names

def in_lesson():
    less = input('Введите название предмета: ')
    return less

def input_mark():
    name = input('Введите имя: ')
    less = input('Введите предмет: ')
    mark = input('Введите оценку: ')
    return name, less, mark

def get_name_to_show():
    name = input('Введите имя студента для просмотра его оценок: ')
    return name