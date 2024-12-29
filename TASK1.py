#task_1_screen_1
def re_list(lst):
    return lst[::-1]
r_list = [1,2,3,4,5]
r_list = re_list(r_list)
print(r_list)

#task_2_screen_1
def change(lst):
    lst[0],lst[-1] =  lst[-1], lst[0]
    return lst
print(change([1,2,3,4,5]))

#task_3_screen_1
def to_list(*args):
    return list(args)
print(to_list(1,2,3,4,5))

#task_4_screen_1
def useless(s):
    return max(s)/len(s)
print(useless([1,2,3,4,5]))

#task_5_screen_1
def list_sort(lst):
    for x in range(len(lst)-1):
        for y in range(len(lst)-1):
            if abs(lst[y]) < abs(lst[y+1]):
                f = lst[y]
                l = lst[y+1]
                lst[y] = l
                lst[y+1] = f
    return lst
print(f"Список в порядке убывания абсолютного значения чисел{list_sort([-1,-3,78,-12,2,-56,44,56])}")

#task_6_screen_1
def all_eq(lst):
    max_str = lst[0]
    for i in lst:
        if len(i) > len(max_str):
            max_str = i
    for i, word in enumerate(lst):
        if len(word) < len(max_str):
            add = len(max_str) - len(word)
            for y in range(add):
                lst[i] += "_"
    return lst
print(all_eq(["puppy","array","beautiful","car"]))

#task_1_screen_2
def to_float(num):
    if num != int(num):
        return "Невозможно преобразовать"
    return float(num)
print(to_float(55))

#task_2_screen_2
def avg_5(a,b,c,d):
    return round((a*b*c*d)/4, 5)
print(avg_5(1.11,7.3,6.7,3.4))

#task_3_screen_2
def mul_to_int(a,b):
    if a*b%1 == 0:
        return int(a*b)
    return a*b
print(mul_to_int(1.4,2))

#task_4_screen_2
def find_r(v):
    return ((3*v)/(4*3.14))**(1/3)
print(find_r(523.33))

#task_1_screen_3
def dislike_6(a):
    if a == 6:
        return "Только не 6"
    return True
print(dislike_6(5))
print(dislike_6(6))

#task_2_screen_3
def help_bool(letter):
    letter = letter.upper()
    if letter == "к":
        return "Коммутативность — свойство бинарной операции «», заключающееся в возможности перестановки аргументов: для любых элементов."
    elif letter == "а":
        return "Ассоциати́вность — свойство бинарной операции, заключающееся в возможности осуществлять последовательное применение формулы в произвольном порядке к элементам."
    elif letter == "д":
        return "Дистрибути́вность — свойство согласованности двух бинарных операций, определённых на одном и том же множестве."
    elif letter == "м":
        return "правило де Мо́ргана — логические правила, связывающие пары логических операций при помощи логического отрицания."
    else:
        return "к - коммутативность\nа - ассоциативность\nд - дистрибутивность\nм - правило де Моргана"
print(help_bool("м"))

#task_1_screen_4
#смотреть task_1_screen_1

#task_2_screen_4
#смотреть task_2_screen_1

#task_3_screen_4
#смотреть task_3_screen_1

#task_4_screen_4
#смотреть task_4_screen_1

#task_1_screen_5
#смотреть task_5_screen_1

#task_2_screen_5
#смотреть task_6_screen_1

#task_1_screen_6
def to_dict(lst):
    dt = {}
    for i in lst:
        dt[i] = i
    return dt
print(to_dict(["s","fig"]))

#task_2_screen_6
my_dict = {"first_one": "we can do it"}
def biggest_dict(**kwargs):
    global my_dict
    my_dict.update(**kwargs)
    return my_dict
print(biggest_dict(dog="Brock", cat="r"))

#task_3_screen_6
from collections import Counter
def count_it(sequence):
    counter_top3 = Counter(sequence).most_common(3)
    counter_top3 = dict(counter_top3)
    new_dict = {}
    for key, value in counter_top3.items():
        new_dict[int(key)] = value
    return new_dict
print(count_it("184709064732"))

#task_4_screen_6
dct = {"word": "red", "item": "box", "pizza": "pipironiki", "school": "teacher", "car": "BMW"}
first = list(dct.values())[0]
second = list(dct.values())[-1]
dct[list(dct.keys())[0]] = second
dct[list(dct.keys())[-1]] = first
del(dct[list(dct.keys())[1]])
dct["new_key"] = "new_value"
print(dct)

#task_1_Строки_1
def search_substr(subst,st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"
print(search_substr("world", "hello world"))

#task_2_Строки_1
def first_last(letter, st):
    turp = (st.find(letter), st.rfind(letter))
    return turp
print(first_last("w","eww"))

#task_3_Строки_1
#from collections import Counter уже вызывал
def top3(st):
    count3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {i}' for letter, i in count3])
print(top3("ajkfjahfghagfwya wduwjadhawndga"))

#task_4_Строки_1
def camel(st):
    st = st.lower()
    st = list(st)
    lst_i = []
    lst_l = []
    for i in range(len(st)):
        if st[i] == "," or st[i] == "." or st[i] == "!" or st[i] == " " or st[i] == ":" or st[i] == "-":
            lst_i.append(i)
            lst_l.append(st[i])
            st[i] = "#"
    st = "".join(st).replace("#","")
    st = list(st)
    for i in range(len(st)):
        if i % 2 == 0:
            st[i] = st[i].upper()
    st = "".join(st)
    for i in range(len(lst_i)):
        st = st[:lst_i[i]] + lst_l[i] + st[lst_i[i]:]
    return st
print(camel("Привет мой друг"))

#task_1_Строки_2
def shortener(st):
    while "(" in st or ")" in st:
        left_s = st.rfind("(")
        right_s = st.find(")", left_s)
        st = st.replace(st[left_s:right_s + 1], "")
    return st
print(shortener("ка(кк(акаы)пкы)пу(а)с((в)а)тка)"))

#task_2_Строки_2
def cleaned_str(st):
    clean_lst = []
    for s in st:
        if s != '@':
            clean_lst.append(s)
        elif s == '@' and clean_lst:
            clean_lst.pop()
    return ''.join(clean_lst)
print(cleaned_str("сварка@@@@@лоб@ну@"))