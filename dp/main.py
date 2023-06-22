class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
        print('hello')

class ElectricCar():
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year =year
        self.battry = Battery()


ele = ElectricCar(10,12,13)
ele.battry.describe_battery()

