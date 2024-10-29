

class YourClass(object):
    classy = 10 # Class variable

    def set_val(self):
        self.insty = 100 # Attribute set in instance

dd = YourClass()

dd.set_val()
print(dd.classy)
print(dd.insty)



class MyClass(object):
    classy = 'class value!'

aa = MyClass()
print(aa.classy) # class value!
aa.classy = 'inst value!'
print(aa.classy) # inst value!
del aa.classy
print(aa.classy) # class value!