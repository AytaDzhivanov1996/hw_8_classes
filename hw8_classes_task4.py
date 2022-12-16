class Meta(type):
    def __new__(mcs, name, bases, attrs):
        new_attrs = ((k, v) for k, v in attrs.items())
        new_attrs_upper = dict((k.upper(), v) for k, v in new_attrs)
        return type.__new__(mcs, name, bases, new_attrs_upper)


class Math(metaclass=Meta):
    pi = 3.141592653589793
    e = 2.718281828459045
    tau = 6.283185307179586
