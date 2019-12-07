import numpy as np

def find_E(point_charges):
    for q in point_charges:
        for pos in grid:
            E = q/()

class Box:
    def __init__(self,charges):
        self.grid = set()

        charge_list = {}
        for charge in charges:
            charge_list[charge.getName()] = charge
        self.charges = charge_list

        self.fields = dict()

#    def update_charges():
#        self.charges =

    def get_charges(self):
        return self.charges

class Charge:
    def __init__(self,name,pos):
        self.name = name
        self.mass = 1
        self.charge = 1
        self.pos = pos
        self.vel = (0,0)
        self.icon = None

    def getName(self):
        return self.name

    def print(self):
        print(self.name)

    def get_pos(self):
        return self.pos

class Field:

    def __init__(self,x_Size,y_Size):
        self.E_field = {}
        self.B_field = {}

    def force(q,v):
        v[0] = vx;  v[1] = vy
        Ex, Ey = self.E_field[0], self.E_field[1]
        B = self.B_field
        Fx = q* (Ex + B*vy)
        Fy = q* (Ey - B*vx)
        return (Fx, Fy)
