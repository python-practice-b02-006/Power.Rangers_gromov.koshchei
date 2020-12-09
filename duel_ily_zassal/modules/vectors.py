class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __matmul__(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __rmul__(self, other):
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

if __name__ == "__main__":
    print("This module is not for direct call!")
