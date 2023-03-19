class Point3D_Ts:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_Q(self):
        return (self.x, self.y, self.z)


class Point3D_Qs:
    def __init__(self, x1, y1, z1):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

    def get_Q(self):
        return (self.x1, self.y1, self.z1)

    def get_Q(self):
        return ((self.x, self.y, self.z) + (self.x1, self.y1, self.z1))




R1 = Point3D_Ts(1, 2, 2)
R2 = Point3D_Qs(5, 7, 1)

print("Координаты 1-ой точки:", R1.get_Q())
print("Координаты 2-ой точки:", R2.get_Q())
print(get_Q)
