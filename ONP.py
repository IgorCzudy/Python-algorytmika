wyrazenie_ONP = input().split()
stos = []
operatory = ['AND', '&', '∧','OR', '|', '∨','IFF', '↔','XOR', '⊕','IMPLIES','→']
kwantyfikatory =['FORALL','EXISTS','∃']
zmienne = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','R','S','T','W','X','Y','Z']
negacja=['NOT', '~', '¬']
for i in wyrazenie_ONP:
    if len(i)==3:
        i.split('/')
        c = i[0]+'('
        for j in range(int(i[2])):
            if j == int(i[2])-1:
                a = stos.pop()
                c+=a
            else:
                a = stos.pop()
                c+=a+' ,'
        c+=')'
        stos.append(c)
    elif i in kwantyfikatory:
        a = stos.pop()
        b=stos.pop()
        c ='( '+ i + ' '+b+' '+a+' )'
        stos.append(c)
    elif i in  operatory:
        a = stos.pop()
        b = stos.pop()
        c = '( '+b+' '+i+' '+a+' )'
        stos.append(c)
    elif i in negacja:
        a = stos.pop()
        b = '( '+i+' '+a+' )'
        stos.append(b)
    else:
        stos.append(i)

print(stos)
