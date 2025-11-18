#сначала мы принимаем текст требующийся для редатикования
text = input()

#теперь я буду искать текст в скобках и буду удалять его вместе со скобками
while True:
    #я нахожу открытие скобок
    st_br_pos = text.find("(")
    #и их закрытие
    end_dr_pos = text.find(")")
    #если в тексте найдены отрытие и закрытие скобок значит наверняка есть и текст в скобках
    if st_br_pos != -1 and end_dr_pos != -1:
        #но так как нам надо удалять именно текст в скобках то я буду проверять в правильно ли расположэно скобки так как
        #если у нас скобки расположэны так ")!*;№"!(" это не правильное расположэние скобок и текст в них я удалять не буду
        # a удалю только скобки
        if st_br_pos > end_dr_pos:
            # удаляю открытие и закрытие
            text = text.replace(text[end_dr_pos], "")
            text = text.replace(text[st_br_pos], "")
        else:
            text = text.replace(text[st_br_pos:end_dr_pos + 1], "")
    elif st_br_pos == -1 and end_dr_pos == -1:
        break
    elif st_br_pos != -1:
        text = text.replace(text[st_br_pos], "")
    elif end_dr_pos != -1:
        text = text.replace(text[end_dr_pos], "")

print(text)
