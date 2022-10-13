# coding a class in python
# defining methods within
# overriding __repr__
# making it possible to print an object of the class


class Converter:
    def __init__ (self, value: float) -> None:
        self.value = value
    
    @property
    def value(self) -> float:
        print("property")
        return self._value

    @value.setter
    def value(self, value) -> None:
        print("setter ", value)
        self._value = value

    @value.getter
    def value(self) -> float:
        print("getter")
        return self._value

    def inch_to_cm(self) -> float:
        return self._value * 2.54

    def foot_to_meters(self) -> float:
        return self.value * 0.3048

    def pound_to_kg(self) -> float: 
        return self.value * 0.453592

    def __repr__(self):
        return f'\n {self.value} in = {self.inch_to_cm()} cm \n {self.value} ft. = {self.foot_to_meters()} m \n {self.value} Lb = {self.pound_to_kg()} kg'
#        return f'("{self.value}")'
#     
#    def __str__(self):
#        return f'({self.value})'


units = Converter(0)
inmat = input("type units :")

units.value = float(inmat)

 

#print(units._value)
print(units)

#print(f"{repr(units)} in = {units.inch_to_cm()} cm")
#print(f"{units} ft. = {units.foot_to_meters()} m")
#print(f"{units.value} Lb = {units.pound_to_kg()} kg")