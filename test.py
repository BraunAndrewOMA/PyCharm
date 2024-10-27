#Encapsulation

class MyClass(object):
    def set_val(self, val): # Setter method
        self.value = val

    def get_val(self): # Getter method
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

a.value = 'hello'

print(a.get_val())
print(b.get_val())