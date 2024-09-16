import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return  f"Vector3D({self.x},{self.y},{self.z})"

    def setVal(self):
        self.x = int(input("set x:"))
        self.y = int(input("set y:"))
        self.z = int(input("set z:"))

    def showVal(self):
        print(f"Vector3D({self.x},{self.y},{self.z})")

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return Vector3D(self.x * other, self.y * other, self.z * other)
    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    def cross(self, other):
        return Vector3D(self.y * other.z - self.z * other.y , self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    @staticmethod
    def are_orthogonal(v1, v2):
        if v1.dot(v2) == 0.0 :
            return True
        return False

vector = Vector3D(1,2,3)
vector2 = Vector3D(2,3,4)
print(vector)
#vector.setVal()
vector.showVal()
print(vector.norm())
v3 = vector + vector2
print(v3)
v4 = vector2 - vector
print(v4)
v5 = vector * 2
print(v5)
v6=vector.dot(vector)
print(v6)
v7=vector.cross(vector)
print(v7)
print(Vector3D.are_orthogonal(vector,vector))
