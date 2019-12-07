import objects

def testCharge():
    electron_class = objects.Charge
    electron1 = electron_class('1')
    electron1.print()

def testGetCharges():
    Box = objects.Box
    Charge = objects.Charge
    pos1=(10,10)
    pos2=(50,50)
    charges = [
        Charge('1',pos1),
        Charge('2',pos2)
    ]

    box = Box(charges)
    charge_dict = box.get_charges()
    print(charge_dict.keys())
    for q in charge_dict.values():
        q.print()

if __name__ == '__main__':
#    testCharge()
    testGetCharges()
