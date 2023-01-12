import pprint
class ToDict(object):
    
    def to_dict(self):
        temp = {}
        for key, value in self.__dict__.items():
            if isinstance(value, ToDict):
                temp[key] = value.to_dict()
            else:
                temp[key] = value
        
        return temp

class PrintableObject(ToDict):

    def __str__(self):
        return "__str__\n" + pprint.pformat(self.to_dict())

    def __repr__(self):
        return "__repr__\n" + pprint.pformat(self.to_dict())

class A_Object(PrintableObject):
    def __init__(self):
        self.a_str = "A"
        self.a_int = 1
        self.a_dict = {"A_dict": 1}
        self.a_list = ["a1", "a5", "a8"]

class B_Object(PrintableObject):
    def __init__(self, a_object):
        self.b_str = "B"
        self.b_int = 2
        self.b_dict = {"B_dict": 2}
        self.b_list = ["b1", "b3", "b5"]
        self.a_object = a_object

CO = ToDict()
CO2 = ToDict()
print(isinstance(CO, object))
print(isinstance(CO2, ToDict))

a_object = A_Object()
b_object = B_Object(a_object=a_object)
print(a_object)
print(b_object)