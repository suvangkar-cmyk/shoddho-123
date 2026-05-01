class vehicle:
    def _init_(self,max_speed,millage):
        self.max_speed = max_speed
        self.millage = millage
mode1x =vehicle(240, 18)
print("Model Max_Speed",mode1x.max_speed)
print("Model Millage:",mode1x.millage)