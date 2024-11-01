#Encapsulation 2

class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def increment_val(self):
        self.val = self.val + 1

i = MyInteger()
i.set_val(9)
print(i.get_val())

i.val = 'hi'
print(i.get_val())
print(i.increment_val())