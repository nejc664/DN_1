prvi_value = int(input("Vnesite prvo celoštevilsko vrednost: "))
drugi_value = int(input("Vnesite drugo celoštevilsko vrednost: "))
tretji_value = int(input("Vnesite tretjo celoštevilsko vrednost: "))


print("Prva vrednost:", prvi_value, "Tip:", type(prvi_value))
print("Druga vrednost:", drugi_value, "Tip:", type(drugi_value))
print("Tretja vrednost:", tretji_value, "Tip:", type(tretji_value))


if drugi_value == prvi_value and tretji_value <= prvi_value:
    print("Druga vrednost je enaka prvi, tretja pa je manjša ali enaka prvi.")
else:
    print("Poskusi ponovno.")