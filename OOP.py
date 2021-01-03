class circle:
    def __init__(self):
        self.__r = 0

    def read(self):
        radius = float(input('Enter the radius'))
        if radius < 0:
            print('error')
        else:
            self.__r=radius

    def getArea(self):
        return 3.14 * self.__r ** 2

    def getPerimiter(self):
        return 3.14 * self.__r * 2

    def getCharastristics(self):
        print("area = " , self.getArea())
        print('perimeter = ' , self.getPerimiter())