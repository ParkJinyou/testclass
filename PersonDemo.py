class Person :
    def who_am_i(self,name,age,tel,address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person() # 객체 생성

boy.who_am_i('john',15,'123-1234','toronto')


print(boy.name)

print(boy.address)
print(boy.tel)