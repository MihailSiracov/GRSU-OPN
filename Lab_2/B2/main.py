import math
in_m = input("Введите номер файла для открытия ")
with open(f'{in_m}.WCData.txt', 'r') as file:
    text = file.readlines()
    ans = []
    sred = 0
    for i in range(0, len(text)):
        if i == 0:
            ans.append('    Time     WC temp     WC Effect\n')
        elif i == 1:
            ans.append(text[i])
        else:

            pred_ans = []
            pred_ans += text[i].split()
            TWS = round(35.74 + (0.6125 * float(pred_ans[1])) + ((0.4275 * float(pred_ans[1])) - 35.75) * float(pred_ans[2]) ** 0.16, 1)
            sred += TWS
            WCE = round(TWS - float(pred_ans[1]), 1)
            pre_ans = f"""{pred_ans[0]}       {TWS}       {WCE}\n"""
            ans.append(pre_ans)
print(*ans)
print('----------------------------------')
w = round(sred / (len(text) - 2), 5)
n = round(sred / (len(text) - 2), 1)
if round((w - n) * -100, 0) == 5:
    aw = round(sred / (len(text) - 2), 1) - 0.1
else:
    aw = round(sred / (len(text) - 2), 1)
an = f"""The average adjusted temperature, based on {len(text) - 2} observations, was {aw}"""
print(an)