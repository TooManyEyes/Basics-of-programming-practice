class Calculator:

    def __repr__(self):
        return "value: {0}, \nattributes: {1}".format(self.value, self.__dict__)

    def __init__(self, init_value=0):
        self.value = init_value
        self.iter_flag = False

    def __add__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value + value)

    def __sub__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value - value)

    def __mul__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value * value)

    def __pow__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        return Calculator(self.value ** value)

    def __truediv__(self, other):
        value = other.value if isinstance(other, Calculator) else other
        self.value /= value
        return self

    def __setattr__(self, key, value):
        if len(self.__dict__) < 12:
            self.__dict__[key] = value

    def power(self, *args):  # последовательное возведение в степень
        for x in args:
            self.value **= x
        return self

    def root(self, *args):  # последовательное извлечение корней из числа
        for x in args:
            self.value **= (1 / x)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter_flag:
            self.iter_flag = False
            raise StopIteration
        else:
            self.iter_flag = True
            return self.value


if __name__ == '__main__':
    calculator = Calculator(6)
    calculator.z = '33'
    calculator.ff = 44
    for i in calculator:
        print(i)
