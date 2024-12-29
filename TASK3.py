#Screen 1
def rock_paper_shears(p1, p2):
    if p1 == "Камень" and p2 == "Ножницы": return "Первый игрок выйграл"
    elif p1 == "Ножницы" and p2 == "Бумага": return "Первый игрок выйграл"
    elif p1 == "Бумага" and p2 == "Камень": return "Первый игрок выйграл"
    elif p1 == p2: return "Ничья"
    else: return "Второй игрок выйграл"
print(rock_paper_shears("Бумага", "Ножницы"))

#Screen 10
def can_or_not(lst_coins):
    if len(lst_coins) % 3 == 0: return "Получится"
    return "Не получится"
print(can_or_not(["coin", "coin", "coin", "coin", "coin"]))

#Screen 2
def do_not_shout(st):
   st = list(st)
   ind = []
   r = []
   for i in range(len(st)):
       if st[i] == "!" or st[i] == "?":
           for y in range(len(st)-i):
               if st[y+i] != "?" or st[y+i] != "?":
                   break
           ind.append(i)
   for i in range(len(ind)-1):
       if ind[i] + 1 != ind[i+1]:
           ind[i] = 0
           r.append(i)
   ind = ind[r[-1]+1:]
   st = "".join(st)
   if ("?" in st[ind[0]:] and not "!" in st[ind[0]:]) or ("!" in st[ind[0]:] and not "?" in st[ind[0]:]):
       if st[ind[0]:].find("?") > st[ind[0]:].find("!"):
           st = st[:ind[0]] + "?"
       elif st[ind[0]:].find("?") < st[ind[0]:].find("!"):
           st = st[:ind[0]] + "!"
   if "?" in st[ind[0]:] and "!" in st[ind[0]:]:
       if st[ind[0]:].find("?") < st[ind[0]:].find("!"):
           st = st[:ind[0]] + "?!"
       elif st[ind[0]:].find("?") > st[ind[0]:].find("!"):
           st = st[:ind[0]] + "!?"
   return st
print(do_not_shout("При?вет ??!мой друг?!!!!"))

#Screen 3
def black_jack(lst):
    return True if sum(lst) > 21 else False
print(black_jack([11, 10]))

#Screen 4
def plus_in_str(st):
    s = 0
    n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ss = []
    for i in range(len(st)):
        if st[i] in n:
            ss.append(st[i])
        else:
            ss.append("0")
    ss = "".join(ss)
    ss = ss.split("0")
    for i in range(len(ss)):
        if ss[i] == "":
            ss[i] = "0"
    for i in range(len(ss)):
        s += int(ss[i])
    return s
print(plus_in_str("абвгд7ап67фдрвц891офал1"))

#Screen 5
def l(st):
    s = st.replace("+", "")
    ll = 0
    for i in range(1, len(st)-1):
        if st[i] != "+" and st[i-1] == "+" and st[i+1] == "+":
            ll += 1
    return True if len(s) == ll else False
print(l("+а+б+в+г++д++"))

#Screen 6
def to_24(t):
    if "pm" in t:
        t = t.replace(" pm", "")
        time = t.split(":")
        t = t.split(":")
        if int(time[0]) + 12 == 24:
            x = "00"
        else:
            x = str(int(time[0]) + 12)
        t[0] = x
        return ":".join(t)
    else:
        t = t.replace("am", "")
    return t
print(to_24("12:34 pm"))

#Screen 7
def check_pass(p):
    ad = 0
    is_number = False
    is_letter = False
    is_upper = False
    if len(p) >= 8:
        ad += 1
    if "@" in p or "_" in p or "*" in p or "&" in p or "#" in p:
        ad += 1
    for item in p:
        try:
            if int(item) in range(0,10):is_number = True
        except ValueError:
            if item == item.upper(): is_upper = True
            is_letter = True
    if is_number: ad += 1
    if is_letter: ad += 1
    if is_upper: ad += 1
    return f"{ad} балла"
print(check_pass("kfr_12yT"))

#Screen 8
def from_int_to_str(integer):
    length = len(str(integer))
    nums = {"1": "один", "2": "два", "3": "три", "4": "четыре", "5": "пять", "6": "шесть", "7": "семь", "8": "восемь", "9": "девять",
            "10": "десять", "11": "одиннадцать", "12": "двенадцать", "13": "тринадцать", "14": "четырнадцать", "15": "пятнадцать", "16": "шестнадцать", "17": "семнадцать", "18": "восемнадцать", "19": "девятнадцать",
            "20": "двадцать", "30": "тридцать", "40": "сорок", "50": "пятьдесят", "60": "шестьдесят", "70": "семьдесят", "80": "восемьдесят", "90": "девяносто",
            "100": "сто", "200": "двести", "300": "триста", "400": "четыреста", "500": "пятьсот", "600": "шестьсот", "700": "семьсот", "800": "восемьсот", "900": "девятьсот"}
    name = ""
    if str(integer) in nums:
        return nums[str(integer)]
    if integer == 0:
        return "0"
    if len(str(integer)) == length:
        name += f"{nums[str(int(str(integer)[0])*(10**(length - 1)))]} "
        integer = int(integer) % (10**(length - 1))
        if str(integer) in nums:
            name += nums[str(integer)]
        else:
            name += f"{nums[str(int(str(integer)[0]) * 10)]} "
            integer = int(integer) % 10
            name += nums[str(integer)]
    return name
print(from_int_to_str(109))

#Screen 9
def luck(n):
    val = 0
    for i in range(10**(n-1), 10**n):
        lst = []
        for n in str(i):
            lst.append(int(n))
        if len(lst) % 2 != 0:
            q = len(lst) // 2
            if sum(lst[:q]) == sum(lst[q+1:]):
                val += 1
        else:
            q = len(lst) // 2
            if sum(lst[:q]) == sum(lst[q:]):
                val += 1
    return val
print(luck(4))