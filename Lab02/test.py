import matplotlib.pyplot as pltr
import numpy as np

plist = []
poke ={                                            # dictionary  pokemon
    "wdth" :   0.0,                                # width
    "lgth" :   0.0,                                # length
    "clss" :   0,                                  # class
}  
x=0
while x<10:
    poke["wdth"] = x
    poke["lgth"] = x
    poke["clss"] = x
    plist.append(poke.copy())
    x = x+1

mem = (filter(lambda p: (p["clss"]<5), plist))
flist = list(mem)
plot(lambda)
pltr.show()
print("run mf run")
print(plist)
print(flist)