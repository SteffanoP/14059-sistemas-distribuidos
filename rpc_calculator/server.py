import math
import rpyc
from rpyc.utils.server import ThreadedServer

@rpyc.service
class CalculatorService(rpyc.Service):


    @rpyc.exposed
    def sum(self, a,b):
        return a + b

    @rpyc.exposed
    def sub(self, a,b):
        return a - b

    @rpyc.exposed
    def mul(self, a,b):
        return a * b

    @rpyc.exposed
    def div(self, a,b):
        return a / b

    @rpyc.exposed
    def loge(self, a):
        return math.log(a)

    @rpyc.exposed
    def log10(self, a):
        return math.log10(a)

    @rpyc.exposed
    def pow(self, a, b):
        return math.pow(a,b)

    @rpyc.exposed
    def sin(self, a):
        return math.sin(a)

    @rpyc.exposed
    def cos(self, a):
        return math.cos(a)

    @rpyc.exposed
    def sqrt(self, a):
        return math.sqrt(a)

if __name__ == '__main__':
    print("Starting Server")
    server = ThreadedServer(CalculatorService, port=66666)
    server.start()