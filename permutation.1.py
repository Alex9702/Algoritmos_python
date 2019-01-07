def memoize(func):
    cache = {}
    def wrapper(lista):
        if str(lista) in cache:
            return cache[str(lista)]
        result = func(lista)
        cache[result] = result
        return result
    return wrapper

def permutation(lista):
    if len(lista) == 0:
        return lista
    if len(lista) == 1:
        return [lista]
    l = []

    for i in range(len(lista)):
        m = lista[i]

        remLst = lista[:i] + lista[i + 1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l

print(len(permutation([1,2,3,4,5,6])))