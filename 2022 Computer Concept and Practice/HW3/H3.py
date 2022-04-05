f = open("HW03.txt", 'w')
data = [15, 20, 21, 42, 9, 27, 14, 23, 51]
for i in range(len(data)) :
    print(i+1,'번째 데이터는 %d입니다.'%data[i])
y = 0
for i in range(len(data)) :
    y += data[i]/len(data)
print(len(data),'개의 데이터의 평균은 %d 입니다.'%y)
f.close()

def Celsius_to_Fahrenheit(Celsius : float) -> float :
    Fahrenheit = (Celsius*1.8) + 32
    return Fahrenheit

class Terran(object) :
    def __init__(self, mineral) : #object의 값을 mineral에 assign
        self.scv = 4
        self.marine = 0
        self.medic = 0
        self.mineral = mineral
    def command(self, SCV=False) :
        self.mineral += 8*self.scv
        if SCV :
            self.scv += 1
            self.mineral -= 15
    def barrack(self, Marine=False, Medic=False) :
        self.mineral += 8*self.scv
        if Marine :
            self.marine += 1
            self.mineral -= 15
        if Medic :
            self.medic += 1
            self.mineral -= 20
    def check_source(self) :
        print("Mineral: "+str(self.mineral))

User = Terran(50)
###object가 50이므로 constructor에 의해서 mineral에 50이 assign 됨.
User.command(True)
###mineral에 4*8=32가 더해져서 82가 됨.SCV에 True가 assign 되므로 if loop가 실행되고, 
###Terran(50).scv에 1이 더해지면서 5가 됨. mineral에서 15가 빠지면서 67이 됨.
User.barrack(True, True)
###mineral에 5*8=40이 더해지면서 mineral이 67이 됨. Marine과 Medic이 둘다 True이므로
###if loop이 두 개가 다 돌아가고, Terran(50).marine은 1, Terran(50).medic도 1이 됨.
###mineral은 15와 20이 빼지므로 107-35인 72가 됨. 
User.check_source()
###mineral 값이 72이므로 "Mineral: 72"가 출력됨.

def sum(n : int) -> int :
    if n < 0 :
        return print("0보다 큰 수를 입력하세요")
    elif n == 0 :
        return 0
    else :
        return n+sum(n-1)
    

class rectangle :
    def __init__(self,x1,y1,x2,y2) :
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def area(self) :
        area = (self.x2-self.x1)*(self.y2-self.y1)
        return area
    
    def perimeter(self) :
        perimeter = 2*(self.x2-self.x1)+2*(self.y2-self.y1)
        return perimeter