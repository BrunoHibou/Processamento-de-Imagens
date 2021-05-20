import math


class intensity:

#: s = T(r), onde r e s denotam os níveis de cinza de f(x,y) e g(x,y) no ponto (x,y)
    def IntensityLog(array, rows, columns):
        #s = c log(1+r)
        aux_array = array
        for r in range(rows-1):
            for c in range(columns-1):
                aux_array[r][c] = 1*(math.log(1+array[r][c]))
        for p in aux_array:
            print(p)
        return aux_array
