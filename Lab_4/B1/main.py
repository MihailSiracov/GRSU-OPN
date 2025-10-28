#выбор файла входных данных и так как похоже начинать отсчёт с нуля было лень если файл
# нулевой 0 из названия надо анегелировать для обнаружения файла
in_m = input("Введите номер файла для открытия")
if in_m == "0":
    in_m = ""

#это первая страка ответа ответа, дальше я буду либо добавлять в
#этот массив сторки либо вписывать их в ответ сразу но после вписывания массива
ans0_info = ["Programmer: Shyriakov Mihail\n"]

#это список для ошибок, а разделял я их для удобства поиска ошибок моеё программы при их наличии
ans1_errors = ["Error        Day        Line\n"]
line = 4

#подготовка всей ереси с месяцэм
max_days_in_month = {"January": [31],
    "February": [28, 29],
    "March":[31],
    "April":[30],
    "May":[31],
    "June":[30],
    "July":[31],
    "August":[31],
    "September":[30],
    "October":[31],
    "November":[30],
    "December":[31]}

#надеюсь говорящее название понятно, но на всякий:
# 0 елси не високосный (False), 1 високосный (True)
key_for_visokosn_yer_or_not = 0

#подготовка для основного ответа
ans2_data = {}

#подготовка для минимумa и максимумa и среднего количества осадков
mimimum = 10000000000000000000000000000000000000000000000000
maximum = 0
averege = 0
col_not_zero = 0

# начал очтения
with open(f'Precip{in_m}.txt', 'r') as file:
    #подготовка начала для выходного файла
    text = file.readline()
    ans0_info += text
    ans0_info += "\n"
    place_line = file.readline()
    month_line = file.readline()
    ans0_info += f"Precipitation report for {place_line[:-1]} during {month_line}"
    ans0_info += "\n"

    #проверка надобности и соответствующая проверка високосного года
    #если год високосный и месяц февраль то будет другое количество дней и
    #будет использоваться другое количесво максимума дней дял месяца
    month, yer = month_line.split()
    #анигиляция мешающей запятой
    month = month[:-1]
    if month == "February":
        if yer // 4 == yer / 4:
            if yer // 100 != yer / 100 or yer // 400 == yer / 400:
                key_for_visokosn_yer_or_not = 1

    #запоминаем максимальный день
    day_max = max_days_in_month[month][key_for_visokosn_yer_or_not]

    #подгатовка списка для дней что бы отслежиать повторы
    day_remembering = []
    #терерь провера дней и уровня столбика
    text = file.readline()


    while text != "":
        #так как после входных данных нам обещано отсутствие лишнего текста то я
        # просто буду брать строки до тех пор пока не закончаться,
        # возможно стоит добавить проверку на фактор человеческой ошибки, но я подумаю
        day, precipitation = text.split()
        day = int(day)
        precipitation = float(precipitation)

        #сначала праверка является ли данная ошибкой из условий
        #cначала наличае дня в месяцэ
        if 0 >= day or day > day_max:
            ans1_errors += f"Invalid{day:>9}{line:>12}\n"
        #теперь на повтор
        elif day in day_remembering:
            ans1_errors += f"Repeated{day:>8}{line:>12}\n"
        #если всё хорошо то вписываем в основной ответ и запоминаем день
        else:
            ans2_data[day] = precipitation
            day_remembering.append(day)

            # подсчёт минимума максимума и подготовка к посчёту среднего значения
            if maximum < precipitation:
                maximum = precipitation
            if mimimum > precipitation:
                mimimum = precipitation
            averege += precipitation
        #берём следующую строку и ведём посчёт для ошибок
        text = file.readline()
        line += 1


#ввод ответа в текстовый файл
with open("ans.txt", 'w', encoding='utf-8') as file:
    #вписываю инфу
    file.writelines(ans0_info)
    #вписываю ошибки
    file.writelines(ans1_errors)
    file.write("\n")
    #вписываю отсортированные данные
    file.write("Day Anount Graph\n")
    for i in range(1, day_max + 1):
        #ежели данных на день указано не было то try поможет нам не
        # сломаться а просто выведет что данных нет
        try:
            #это чтобы не кашмарить фызов словаря изза звёздочек
            precipitation_2 = ans2_data[i]

            #думаю самое время подсчитать звёздочки что бы не создавать
            # ещё по переменной на каждый день а просто редактировать 1 не константу
            min = 0.01
            max = 0.25
            stars = 0
            contining = True
            #за каждое деление в 0.25 я буду добавлять по звезде пока не выйду за рамку
            while contining:
                if min <= precipitation_2 and precipitation <= max:
                    stars += 1
                    min += 0.25
                    max += 0.25
                else:
                    contining = False
            #считаю количество переменных не равных 0
            if precipitation_2 > 0.00:
                col_not_zero += 1
            #и вписываю
            file.write(f"{i:>3}{f"{precipitation_2:.{2}f}":>7} {"*"*stars:<15}\n")
        except:
            file.write(f"{i:>3}{"NA":>7}\n")
    file.write("\n")

    #под конец вводим минимум максимум и считаем и вводим срденюю количества осадков
    file.write("Minimum     Maximum        Average\n")
    averege = round((averege / day_max), 2)
    file.write(f"{f"{mimimum:.{2}f}":>7}{maximum:>12}{averege:>15}")
    file.flush()
    file.close()


print("ВСЁ")