class Person :
    def who_am_i(self,name,age,tel,address): # self 중요!!!
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

boy = Person() # 객체 생성(self 자리에 boy가 간다)
girl = Person() # 객체 생성(self 자리에 girl이 간다)

boy.who_am_i('john',15,'123-1234','toronto')
girl.who_am_i('alice', 16,'1234-123','Busan')

print(boy.name,girl.name)
print(boy.age,girl.age)
print(boy.address,girl.address)
print(boy.tel,girl.tel)

