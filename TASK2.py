#Screen 10
def xy (x,y):
    lst_xy = []
    for i in range(len(x)):
        tr = (x[i], y[i])
        lst_xy.append(tr)
    return lst_xy
print(xy([3,2,1],[1,2,3]))

#Screen 11
def hello(lst):
    for i in range(len(lst)):
        print(f"Привет {lst[i]}")
hello(["Миша", "Петя", "Маша"])

#Screen 12
def double(st):
    for i in range(len(st)):
        if st[i].lower() == st[i+1].lower():return True
    return 0
print(double("Деревянный"))

#Screen 13
def without_space(st):
    st = list(st)
    if st[0] == " ":
        st[0] = ""
    if st[-1] == " ":
        st[-1] = ""
    st.append("0")
    for i in range(len(st)-1):
        if st[i] == " " and st[i] == st[i+1]:
            st[i] = ""
        if st[i] == " " and st[i+1] == "." or st[i+1] == "," or st[i+1] == ":" or st[i+1] == "!":
            st[i] = ""
    st.pop()
    return "".join(st)
print(without_space(" Привет мой   друг   ,       ты капуста  . "))

#Screen 14
def m(h, r):
    return round(3.14*(r**2)*h*1000,2)
print(m(0.15,0.05))

#Screen 15
def s(st):
    st = st.split(", ")
    sum = 1
    for i in range(len(st)):
        sum *= int(st[i])
    return sum
print(s("1, 2, 3"))

#Screen 16
def v(n):
    s = 0
    for i in range(n):
        x = int(input(f"Введите длину коробки {i+1} "))
        y = int(input(f"Введите ширину коробки {i + 1} "))
        z = int(input(f"Введите высоту коробки {i + 1} "))
        s += x*y*z
    return s
#print(v(3))

#Screen 17
def length(a,b):
    return round(abs(((b["x"] - a["x"])**2 + (b["y"] - a["y"])**2)**0.5), 3)
print(length({"x": 2, "y": 1},{"x": 3, "y": 4}))

#Screen 18
def language(st):
    st = st.replace("е", "3")
    st = st.replace("Е", "3")
    st = st.replace("а", "4")
    st = st.replace("А", "4")
    return st
print(language("Афигеть язык хакера!"))

#Screen 19
def up(lst):
    ls = []
    for i in range(len(lst)):
        ls.append(sum(lst[:i]) + lst[i])
    return ls
print(up([1,2,3,4,5,6]))

#Screen 20
def up_down(lst):
    return "Возрастает" if lst[0] < lst[-1] else "Убывает"
print(up_down([1,2,3,4,5]))

#Screen 21
def med(lst):
    lst.sort()
    l = len(lst)
    if l % 2 == 0:
        return (lst[l//2] + lst[l//2-1]) / 2
    else:
        return lst[l//2]
print(med([2,2,6,8,2,10,3]))

#Screen 7
def device():
    al = {1: "А", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I",
          10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S",
          20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
    st = input("Введите слово с помощью клавиши 1 ")
    st = st.split(" ")
    for i in range(len(st)):
        st[i] = al[len(st[i])]
    return "".join(st)
#print(device())

#Screen 8
def remake(st):
    st = list(st)
    for i in range(len(st)):
        if st[i] == st[i].lower():
            st[i] = st[i].upper()
        else:
            st[i] = st[i].lower()
    st = st[::-1]
    return "".join(st)
print(remake(".гурД йоМ тевирП"))

#Screen 9
def i_am_not_have_enemi(lst, enem):
    for i in range(len(enem)):
        if enem[i] in lst:
            lst.remove(enem[i])
    return lst
print(i_am_not_have_enemi(["Ваня", "Таня", "Маша", "Нина", "Миша", "Вика"], ["Ваня", "Маша"]))