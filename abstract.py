

class Descriptor:
    def __init__(self, number):
        self.number = number

    def __set__(self, instance, value):
        self.number = value * 2

    def __get__(self, instance, owner):
        return self.number

    def __del__(self):
        pass


class DescriptorReadOnly:
    def __init__(self, number):
        self.number = number

    def __get__(self, instance, owner):
        return self.number

    def __set__(self, instance, value):
        pass


class MyClass:
    param = Descriptor(5)
    read_only = DescriptorReadOnly(5)

    def __init__(self, *args, **kwargs):
        self.d = []

    def __add__(self, other):
        print('HERE', other)

    def __iadd__(self, other):
        pass

    @property
    def value(self):
        return self.d

    @value.setter
    def value(self, value):
        self.d.append(value)

    @value.getter
    def value(self):
        return self.d * 2

    @value.deleter
    def value(self):
        self.d = []

    def __getitem__(self, item):
        print('HERE', self.d)
        return self.d[item]

    def __setitem__(self, key, value):
        self.d.insert(key, value)

    def __bool__(self):
        return bool(self.d)


m = MyClass()
print(m.d)
print(m.value)
m.value = 1
m.value = 1
m.value = 1
m.value = 1
m.value = 1
m.value = 1
print(m.value)
print(m.value)
m.read_only = 10
print(m.read_only)
print(m[0])
m[0] = 123
print(m.value)
print(m[0])






