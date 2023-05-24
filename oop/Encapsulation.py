class Encap:

    def __init__(self):
        self.__maxvalue = 800
        self.__minvalue = 600

    def sellData(self):
        print("selling price of maximum products: {}".format(self.__maxvalue))
        print("selling price of minimum products: {}".format(self.__minvalue))

    def setMaxPrice(self, maxprice):
        self.__maxvalue = maxprice

    def setMinPrice(self, minprice):
        self.__minvalue = minprice

obj = Encap()
obj.sellData()

#change value
obj.setMaxPrice(900)
obj.setMinPrice(100)
obj.sellData()
