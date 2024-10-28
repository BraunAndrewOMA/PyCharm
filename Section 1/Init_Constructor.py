


class MyNum(object):
    def __init__(self, value=3):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val += 1

dd = MyNum()
dd.increment()
dd.increment()
print(dd.val)

cc = MyNum(5)
cc.increment()
cc.increment()
print(cc.val)

ee = MyNum('Hello')
ee.increment()
print(ee.val)