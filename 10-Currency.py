#peso, soles, roles

co =int(input("quede en peso: "))
pe =int(input("quede en soles: "))
br =int(input("quede en reales: "))

source = co * 0.0578
source = pe * 0.2800
source = br * 0.2140
usd = co + pe + br
print(usd)