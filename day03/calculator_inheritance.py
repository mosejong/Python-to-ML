class Calculator:               # 덧셈전용

    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val


class UpgradeCalculator(Calculator): # 상속 후 뺄셈 추가

    def minus(self,val):
        self.value -= val


class MaxLimitCalculator(Calculator):   # 한계치(100)가 있는 하자있는 계산기

    def add(self,val):
        self.value += val

        if self.value > 100:
            self.value = 100


cal = MaxLimitCalculator()

cal.add(50)
cal.add(60)

print(cal.value)