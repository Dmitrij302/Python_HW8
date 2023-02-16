import view

# main_dct = {'FI':{'MATH':[6, 3, 4], 'PHISC':[2, 3, 2]}, 'FI':...}
main = {}
stud_name = []
lesson = []
def start():
    while True:
        oper = view.get_op()
        if oper == 1:
            stud = view.in_student()
            if stud not in stud_name:
                main[stud] = {}
                stud_name.append(stud)
                if lesson:
                    for les in lesson:
                        main[stud][les] = []
        elif oper == 2:
            les = view.in_lesson()
            lesson.append(les)
            for name in stud_name:
                main[name][les]=[]
        elif oper == 3:
            name, les, mar = view.input_mark()
            main[name][les].append(mar)
        elif oper == 4:
            print(main)
        elif oper == 5:
            name == view.get_name_to_show()
            print(f'Оценки студента {name}: {main[name]}')




        if oper == 6:
            break

    print(main)


