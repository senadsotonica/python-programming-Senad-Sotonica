import math

print("uppgift a")
a = 3                                               # katet a
b = 4                                               # katet b
c = math.hypot(a,b)                                 # returnerar svaret på sqrt(a*a, b*b)
print("Hypotenusan är : ", c)                                            # printar hypotenusans längd

print("uppgift b")
c = 7                                               # hypotenusan
a = 5                                               # katet a
b = math.sqrt(math.pow(7, 2) - math.pow(5, 2))      # katet b = roten ur ( c*c - a*a )
b = round(b, 2)                                     # avrundar till 1 decimal, märker att round inte returnerar som man förväntar sig, 
                                                    # men behåller den då jag når önskvärt resultat
print("Kateten är : ", b)                           # printar b