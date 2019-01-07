class Permutacao:
    def __init__(self):
        self.lista = []
    
    def p1(self, start, end):
        if start == end:
            print(self.lista)
        else:
            for i in range(start, end):
                self.lista[start], self.lista[i] = \
                self.lista[i], self.lista[start]
                self.p1(start + 1, end)
                self.lista[start], self.lista[i] = \
                self.lista[i], self.lista[start]
    def p2(self, lista):
        if len(lista) == 0:
            return lista
        if len(lista) == 1:
            return [lista]
        l = []

        for i in range(len(lista)):
            m = lista[i]

            remLst = lista[:i] + lista[i + 1:]

            for p in self.p2(remLst):
                l.append([m] + p)
        return l

    def melhor(self, lista):
        l = []
        permutation = self.p2(lista)
        maior = permutation[0][0]
        for i in range(len(permutation[0]) - 1):
            if maior < permutation[0][i+1]:
                maior = permutation[0][i+1]
        for e in permutation:
            l.append(0)
            for i in range(1, len(e)):
                if e[0] == maior:
                    l[len(l) - 1] = e[-1]
                    break
                elif e[0] < e[i]:
                    l[len(l) - 1] = e[i]
                    break
                else:
                    l[len(l) - 1] = e[0]
        pm = 0
        for e in l:
            if e == maior:
                pm += 1
        return pm/len(l)

            


lista = [1,2,3,4,5,6,7,8,9,10,11,12]
permutacao = Permutacao()
# print(permutacao.p2(lista))
print(permutacao.melhor(lista))