import rpyc

connection = rpyc.connect('localhost', port=66666)

print(connection.root.sum(1,5))
print(connection.root.sub(7,1))
print(connection.root.mul(2,3))
print(connection.root.div(12,2))
print(connection.root.log10(1000000))