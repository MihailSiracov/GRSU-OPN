text = "ghbj) (22(33)44)uvhhjb("
st_br_pos = text.find("(")
st_poss = []

while st_br_pos != -1:
    st_poss.append(st_br_pos)
    text= text[:st_br_pos] + " "+text[st_br_pos+1:]
    st_br_pos = text.find("(")
    print( text)