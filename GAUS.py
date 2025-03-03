
my_A_rows = int(input("введите число строк матрицы коэфициентов: "))

print("введите матрицу коэфициентов (по строкам, пробелы между коэффициентами")
myA = [list(map(int, (input(f"строка {i + 1}: ").split())))
       for i in range(my_A_rows)]




def kef_one(myA):
    for i in range(len(myA)):
        if (myA[i][0] == 1):
            listDop = myA[0]
            myA[0] = myA[i]
            myA[i] = listDop
    return myA


def  Zero_add(myA):
    i = 1;
    for i in range(len(myA)):

        for j in range( i +1 ,len(myA)):
            kef = myA[j][i ] /myA[i][i]

            result = list(map(lambda x, y: x - y* kef, myA[j], myA[i]))
            myA[j] = result
    return myA


def found_korn(myA):
    ln = len(myA)
    for i in range(ln - 1, -1, -1):
        for j in range(i + 1, ln):
            myA[i][ln] -= myA[i][j]
        y = myA[i][ln]
        b = myA[i][i]
        x = myA[i][ln] / myA[i][i]
        for j in range(0, ln - 1):
            myA[j][i] = x * myA[j][i]
        print(f"x{i}: ",x)
    return myA


def matric(mas, num, my_A_rows):
    for i in range(num + 1, my_A_rows):
        mas[len(mas) - 1] = mas[len(mas) - 1] + mas[i]
    return mas[len(mas) - 1] / mas[num]


def minor(mass):
    lenghtMass = len(mass)

    if (lenghtMass == 2):
        return (mass[0][0] * mass[1][1] - mass[0][1] * mass[1][0])

    opred = 0

    for i in range(lenghtMass):
        mass_dop = mass[:]
        num = mass[0][i]
        mass_dop = mass_dop[1:]
        for j in range(len(mass_dop)):
            mass_dop[j] = mass_dop[j][:i] + mass_dop[j][i + 1:]

        opred += num * minor(mass_dop) * pow(-1, i)

    return opred


korn = [my_A_rows]
opred = minor(myA[0:len(myA)-1])
print("Определитель: ",opred)
if opred == 0:
    print("Нет однозначного решения матрицы, либо его нет.")
else:
    myA = kef_one(myA)
    Zero_add(myA)
    myA = found_korn(myA)
