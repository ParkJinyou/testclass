class Computer :
    def set_spec(self,cpu,ram,vga,ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print("CPU={}".format(self.cpu))
        print("RAM={}".format(self.ram))
        print("VGA={}".format(self.vga))
        print("SSD={}".format(self.ssd))

desktop= Computer()
desktop.set_spec('i7','16GB','GTX1060','512GB')
desktop.hardware_info()



notebook = Computer()
notebook.set_spec('i5','8GB','MX300','256GB')
notebook.hardware_info()



'''class Calculator :
    def input_expr(self):
        expr=input("수식을 입력하세요>>")
        self.expr=expr

    def calculate(self):
        return  eval(self.expr)

calc=Calculator()
calc.input_expr()
print("수식 결과는{}입니다.".format(calc.calculate()))'''