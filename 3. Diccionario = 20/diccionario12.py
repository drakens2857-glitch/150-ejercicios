dic = {'a': 1, 'b': 2, 'c': 3}
while dic:
    clave = next(iter(dic))
    del dic[clave]
print(dic)
