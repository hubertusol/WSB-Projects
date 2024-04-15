import math

class RoundHole:
    def __init__(self, radius):
        self._radius = radius

    def getRadius(self):
        return self._radius

    def fits(self, peg):
        return self.getRadius() >= peg.getRadius()

class RoundPeg:
    def __init__(self, radius):
        self._radius = radius

    def getRadius(self):
        return self._radius

class SquarePeg:
    def __init__(self, width):
        self._width = width

    def getWidth(self):
        return self._width

class SquarePegAdapter(RoundPeg):
    def __init__(self, peg):
        self._peg = peg

    def getRadius(self):
        return self._peg.getWidth() * math.sqrt(2) / 2

hole = RoundHole(5)
rpeg = RoundPeg(5)
print(hole.fits(rpeg))  # True

small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)

small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

print(hole.fits(small_sqpeg_adapter))  # True
print(hole.fits(large_sqpeg_adapter))  # False
