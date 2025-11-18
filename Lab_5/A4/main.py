
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
    file.write("Dwight Barnette\nGenetic Searching\n")
    file.write("--------------------------------------------------------------------------\n")
    with open(f"get_command.{num_for_open}.txt", "r") as text:
        stroka_command = text.readline()
        pos_razdel_dannyh_in_str = stroka_command.find("\t")
        command = stroka_command.replace(stroka_command[pos_razdel_dannyh_in_str:],"")
        dannye = stroka_command.replace(stroka_command[:pos_razdel_dannyh_in_str + 1],"")
        get_command = [command, dannye]
        while len(command) != 0:
            num_com += 1
            num_com_for_out = str(num_com / 1000)[-3:]
            if get_command[0] == "search":
                file.write(f"{num_com_for_out}    {get_command[0]}    {get_command[1]}")
                file.write("organism                        protein\n")
                ans = ""
                need_find = get_command[1][:-1]
                no_one = True
                for data in data_map:
                    gen_cod = data[2]
                    if gen_cod.find(need_find) != -1:
                        ans += f"{data[1][:-1]:<31} {data[0]}\n"
                        file.write(ans)
                        no_one = False
                if no_one:
                    ans = "NOT FOUND\n"
                    file.write(ans)
            elif get_command[0] == "diff":
                pos_razdel_name = get_command[0]

                name1 =


            stroka_command = text.readline()
            pos_razdel_dannyh_in_str = stroka_command.find("\t")
            command = stroka_command.replace(stroka_command[pos_razdel_dannyh_in_str:], "")
            dannye = stroka_command.replace(stroka_command[:pos_razdel_dannyh_in_str + 1], "")
            get_command = [command, dannye]
