def jotaz(numero):
    lusta = []
    for x in range(numero+1):
        y = 2*x
        lusta.append(y)
        print(y)
    return lusta

en = jotaz(10)

print(en)
