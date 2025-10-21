list_of_distanse = []
in_m = input("Введите номер файла для открытия")
with open(f'{in_m}.ChaseData.txt', 'r') as file:
    text = file.readline()
    x, y = text.split()
    map_range = [int(x), int(y)]
    mov = {"C":[0, 0], "M":[0, 0], "D_M": 0, "D_C": 0}
    text = file.readline()
    an = []
    times_1 = {"M": True, "C":True}
    eveding = "Mouse evaded Cat"
    while text != "":
        sym = []
        sym = text.split()
        if len(sym) != 1:
            mov[sym[0]][0] += int(sym[1])
            if mov[sym[0]][0] <= 0:
                mov[sym[0]][0] = map_range[0] + mov[sym[0]][0]
            elif mov[sym[0]][0] > map_range[0]:
                mov[sym[0]][0] = mov[sym[0]][0] - map_range[0]
            mov[sym[0]][1] += int(sym[2])
            if mov[sym[0]][1] <= 0:
                mov[sym[0]][1] = map_range[1] + mov[sym[0]][1]
            elif mov[sym[0]][1] > map_range[1]:
                mov[sym[0]][1] = mov[sym[0]][1] - map_range[1]
            if not times_1[sym[0]]:
                mov[f"D_{sym[0]}"] += abs(int(sym[1])) + abs(int(sym[2]))
            else:
                times_1[sym[0]] = False
            if mov["M"] == mov["C"]:
                eveding = f"Mouse caught at: ({mov["M"][0]:>2},{mov["M"][1]:>2})"
                break
        else:
            pred_an = f""
            if mov["D_M"] == 0:
                pred_an = f"{mov["C"][0]:>2}, {mov["C"][1]:>2})     (?, ?)"
            elif mov["D_C"] == 0:
                pred_an = f"( ?, ?){"":>4}({mov["M"][0]:}, {mov["M"][1]:>2})"
            else:
                distans = abs(mov["C"][0] - mov["M"][0]) + abs(mov["M"][1] - mov["C"][1])
                pred_an = f"({mov["C"][0]:>2},{mov["C"][1]:>2}){'':>4}({mov["M"][0]:>2},{mov["M"][1]:>2}){distans:>6}"
            an.append(pred_an)
        text = file.readline()

print("Cat and Mouse \n Cat        Mouse    Distance \n------------------------------")
for i in range(0, len(an)):
    if i != len(an) -1:
        print(f"{an[i]}")
    else:
        print(an[i])
print("------------------------------\n\n")
print("Distance   Mouse    Cat")
print(f"{mov["D_M"]:>16}{mov["D_C"]:>7}\n")
print(eveding)