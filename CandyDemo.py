'''class Candy :
    def set_info(self,shape,color):
        self.shape = shape
        self.color = color
satang = Candy()
satang.set_info('circle','brown')
print(satang.shape,satang.color)'''


'''class Candy :
    def __init__(self,shape,color): # 생성자 (던더 이닛) >> 객체 생성할 때 자동으로 호출
        self.shape = shape
        self.color = color

satang = Candy('circle','brown')
print(satang.shape,satang.color)'''



'''class USB:
    def __init__(self,capacity):
        self.capacity = capacity

    def info(self):
        print("{}GB USB".format(self.capacity))
usb = USB(64)
usb.info()'''


class Service :
    def __init__(self,service):
        self.service = service
        print("{}Service가 시작되었습니다.".format(self.service))

    def __del__(self):
        print("{}Service가 종료되었습니다.".format(self.service))


s= Service('길안내')

