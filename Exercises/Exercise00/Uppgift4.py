a = [ 4, 4]                         # koordinat x2, y2
b = [ 0, 1]                         # koordinat x1, y1

d1 = a[0] - b[0]                    # x2 - x1
d2 = a[1] - b[1]                    # -------   =   y
k = d2 / d1                         # y2 - y1

m = a[1] - (k * a[0])               # m = y - kx 

print("Resultat: k är ", k, " och m är ", m, " .")
print("Ekvationen är y = ",k ,"x + ", m," .")

