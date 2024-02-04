class Temperature(float):
    def __new__(cls, value, scale):
        instance = super().__new__(cls, value)
        instance.scale = scale
        return instance

    def to_celsius(self):
        if self.scale.lower() == "f":
            return (self - 32) * 5 / 9
        return self

    def to_fahrenheit(self):
        if self.scale.lower() == "c":
            return (self * 9 / 5) + 32
        return self



t_1 = Temperature(32, 'c')
print(t_1.to_fahrenheit()) # 89.6

t_2 = Temperature(89.6, 'f')
print(t_2.to_celsius()) # 32.0


