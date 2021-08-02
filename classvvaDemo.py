class Korean:
    country = "Korea" # class변수(누구나 공유)

    @classmethod # 데코레이터
    def trip(cls,country): # self 자리에 cls
        if cls.country == country:
            print("국내여행입니다.")
        else :
            print('해외여행입니다.')

Korean.trip('Korea')
Korean.trip('USA')