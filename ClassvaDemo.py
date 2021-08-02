class Korean:
    country = "Korea" # class변수(누구나 공유)

    def __init__(self, name, age, address): #객체변수(따로따로 사용)
        self.name = name
        self.age = age
        self.address = address

man = Korean("홍길동",35,'서울') # 객체 생성
woman = Korean("정유미",34,'부산')

print(man.name) # 객체 변수 호출
print(Korean.country) # class 변수 호출
print(man.country)
print(woman.age)
