def s(num,sis):
    f=[]
    while num>0:
        f = [num%sis] + f
        num//=sis
    return f


def bea(l):
    t = ""
    for i in l:
        t += str(i)
    return t

def num_to_let(l):
    alf = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fin=""
    for num in l:
        fin += (alf[num])
    return fin

def plus(f1s,f2s,s1):
    f1s = f1s[::-1]
    f2s = f2s[::-1]
    dl1 = len(f1s)
    dl2 = len(f2s)
    final = []
    dop = 0
    for ind in range(max(dl1,dl2)):
        num1 = f1s[ind] if ind < dl1 else 0
        num2 = f2s[ind] if ind < dl2 else 0
        fnum = num1 + num2 + dop
        final.append(fnum % s1)
        dop = fnum // s1

    if dop:
        final.append(dop)

    return final[::-1]


def delenie(f1s, f2s, s1):
    n1 = int("".join(str(d) for d in f1s), s1)
    n2 = int("".join(str(d) for d in f2s), s1)
    if n2 == 0:
        raise ValueError("деление на ноль")

    nn1, nn2 = divmod(n1, n2)

    return s(nn1, s1), s(nn2, s1)

def minus(f1s, f2s, s1):
    n1 = int("".join(str(d) for d in f1s), s1)
    n2 = int("".join(str(d) for d in f2s), s1)
    if n1 < n2:
        raise ValueError("не, второе больше первого")
    
    f1s = f1s[::-1]
    f2s = f2s[::-1]
    dl1 = len(f1s)
    dl2 = len(f2s)
    final = []
    dop = 0

    for i in range(max(dl1, dl2)):
        num1 = f1s[i] if i < dl1 else 0
        num2 = f2s[i] if i < dl2 else 0
        razn = num1 - num2 - dop

        if razn < 0:
            razn += s1
            dop = 1
        else:
            dop = 0

        final.append(razn)

    while len(final) > 1 and final[-1] == 0:
        final.pop()

    return final[::-1]

def umn(f1s, f2s, s1):
    f1s = f1s[::-1]
    f2s = f2s[::-1]
    final = [0]

    for shift, d2 in enumerate(f2s):
        temp = []
        dop = 0
        for d1 in f1s:
            mul = d1 * d2 + dop
            temp.append(mul % s1)
            dop = mul // s1
        if dop:
            temp.append(dop)
        temp = [0]*shift + temp
        temp = temp[::-1]
        final = plus(final, temp, s1)

    return final

f1 = int(input("Первое число "))
znak = input("Что делаем? ")
f2 = int(input("Второе число "))
s1 = int(input("Система: "))
f1s = (s(f1,s1))
f2s = (s(f2,s1))
print(f"Start\n1list: {f1s}\n2list: {f2s}\n___________")
if znak == "+":
    ans = plus(f1s,f2s,s1)
    print(ans, num_to_let(ans))
elif znak == "-":
    ans = minus(f1s,f2s,s1)
    print(ans, num_to_let(ans))
elif znak == "/":
    full, ost = delenie(f1s,f2s,s1)
    print("Частное:", full, num_to_let(full))
    print("Остаток:", ost, num_to_let(ost))
elif znak == "*":
    ans = umn(f1s, f2s, s1)
    print(ans, num_to_let(ans))
