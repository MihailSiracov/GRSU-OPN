list_of_distanse = []
in_m = input("Введите номер файла для открытия")
with open(f'inmap{in_m}.dat', 'r') as file:
    text = file.readlines(1)
    col, map_range = text[0].split()
    col = int(col)
    map_range = float(map_range)
    text = file.readlines()
    old_list_of_distanse = [float(item) for item in text]
    for i in range(0, col):
        list_of_distanse += text[i].split()
        list_of_distanse[i] = float(list_of_distanse[i]) * map_range
        list_of_distanse[i] = round(list_of_distanse[i], 1)

sum_d = 0

ans_1 = f"""Ширяков Михаил
Simple Map Distance Computations

Map Scale Factor: {map_range} miles per inch

        Map     Mileage 
        Measure Distance
=============================================="""
print(ans_1)

for i in  range(1, col + 1):
    print(f"""# {i}     {old_list_of_distanse[i - 1]}       {list_of_distanse[i - 1]}""")
    sum_d += list_of_distanse[i -1]

ans_2 = f"""==============================================
Total Distance: {sum_d} miles"""
print(ans_2)