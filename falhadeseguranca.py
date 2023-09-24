n = int(input())
lg = []
contador = 0

for i in range(n):
    ls = []
    senhas = input()
    for i in range(len(senhas)):
        ls.append(senhas[i])
    lg.append(ls)

cont = 0
guarda = ''
for i in range(n):
    for o in range(n):
        if len(lg[i]) < len(lg[o]):
            quant = len(lg[o]) - len(lg[i]) + 1
            for q in range(quant):
                for u in range(len(lg[i])):
                     if lg[i][u] == lg[o][u]:
                        cont = cont + 1
                    elif lg[i][u] != lg[o][u]:
                        guarda = lg[o]
                        del lg[o][0]
                lg[o] = guarda
                print(cont)
                if cont == len(lg[i]):
                    contador = contador +1
                    cont = 0
        elif  len(lg[i]) == len(lg[o]):  
            if lg[i] == lg[o]: 
                contador = contador+1
print(lg)
print(contador)
