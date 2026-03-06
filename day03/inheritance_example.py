class BlackBox:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class VideoMaker:

    def make(self):
        print(f"{self.name} 여행 영상 제작")


class MailSender:

    def send(self):
        print("메일 발송")


class TravelBlackBox(BlackBox, VideoMaker, MailSender):

    def __init__(self, name, price, sd):
        super().__init__(name,price)
        self.sd = sd

    def set_travel_mode(self, minute):
        print(f"{self.name} {minute}분 여행모드 ON")

class AutoBlackBox(TravelBlackBox):
    def set_travel_mode(self, minute):
        super().set_travel_mode(minute)
        self.make()
        self.send()

p1 = BlackBox("검둥이", 50_000)     # 단위표시 언더바로 구분 가능하다고 함
print(p1.name, p1.price)

print()

p2 = TravelBlackBox("하양이", 100_000, 128) #상속된 클래스로 부모 메서드 사용가능
print(p2.name, p2.price, p2.sd)
p2.make()
p2.send()
p2.set_travel_mode(30)

print()

p3 = AutoBlackBox("파랑이", 200_000, 256)
p3.set_travel_mode(60)                        # 오버라이딩된 메서드실행