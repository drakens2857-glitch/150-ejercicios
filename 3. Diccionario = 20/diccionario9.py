dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
claves_a_eliminar = [k for k, v in dic.items() if v % 2 == 0]
for k in claves_a_eliminar:
    del dic[k]
print(dic)
