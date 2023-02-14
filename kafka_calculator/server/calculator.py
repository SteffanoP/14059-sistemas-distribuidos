import math

class Calculator():

    def __init__(self, operation, a, b=None):
        self.operation = operation
        self.a = int(a)
        if b is not None:
            self.b = int(b)

    def result(self):
        match self.operation:
            case 'sum':
                return self.sum(self.a, self.b)
            case 'sub':
                return self.sub(self.a, self.b)
            case 'mul':
                return self.mul(self.a, self.b)
            case 'div':
                return self.div(self.a, self.b)
            case 'loge':
                return self.loge(self.a)
            case 'log10':
                return self.log10(self.a)
            case 'pow':
                return self.pow(self.a, self.b)
            case 'sin':
                return self.sin(self.a)
            case 'cos':
                return self.cos(self.a)
            case 'sqrt':
                return self.sqrt(self.a)

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def loge(self, a):
        return math.log(a)

    def log10(self, a):
        return math.log10(a)

    def pow(self, a, b):
        return math.pow(a, b)

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)

    def sqrt(self, a):
        return math.sqrt(a)
