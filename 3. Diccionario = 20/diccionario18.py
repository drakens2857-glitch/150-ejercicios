dic = {'a': 2, 'b': 4, 'c': 3, 'd': 5}
claves_a_eliminar = [k for k, v in dic.items() if v > 3]
for k in claves_a_eliminar:
    del dic[k]
print(dic)
