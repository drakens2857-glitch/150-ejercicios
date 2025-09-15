dic = {'batman': 1, 'superman': 2, 'batgirl': 3, 'flash': 4}
claves_a_eliminar = [k for k in dic if k.startswith('b')]
for k in claves_a_eliminar:
    del dic[k]
print(dic)
