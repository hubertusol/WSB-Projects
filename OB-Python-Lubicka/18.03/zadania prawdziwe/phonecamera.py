class Camera:
    def __init__(self):
        pass
    def take_picture(self):
        print("Pstryk!")
class MobilePhone:
    def __init__(self,memory):
        self.memory=memory
class CameraPhone(Camera,MobilePhone):
    def __init__(self,memory):
        Camera.__init__(self)
        MobilePhone.__init__(self,memory)
Scamsung12=CameraPhone('200MB')
Scamsung12.take_picture()
print(Scamsung12.memory)