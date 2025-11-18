
num_for_open = int(input())

data_map = []
with open(f"sequences.{num_for_open}.txt", "r") as text:
    name = text.readline()
    code = text.readline()
    while name != "":
        end_1th_name = name.find("\t")
        otstup = 1
        if end_1th_name == -1:
            end_1th_name = name.find("   ")
            otstup = 3
        name1 = name.replace(name[end_1th_name:], "")
        name2 = name.replace(name[:end_1th_name + otstup], "")
        data_map.append([name1, name2, code])
        name = text.readline()
        code = text.readline()
num_com = 0
with open("ans.txt", "w") as file:
    with open(f"commands.{num_for_open}.txt", "r") as text:
        command = text.readline().split()
        while len(command) != 0:
            num_com += 1
            if command[0] == "search":
                file.write(f"{num_com:>3}    {command[0]}    {command[1]}\n")
                file.write("organism                        protein\n")
                ans = ""
                need_find = command[1]
                for data in data_map:
                    gen_cod = data[2]
                    if gen_cod.find(need_find) != -1:
                        ans += f"{data[1]:>16} {data[0]}"
                        file.write(ans)
            command = text.readline().split()



        command = text.readline().split()
