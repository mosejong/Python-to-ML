class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.")
        else:
            self.balance -= amount

    def transfer(self, other, amount): #수업 외적으로 이런 기능 해봐라 해서 직접 생각해본 함수
        if self.balance < amount:
            print("잔액이 부족하여 송금이 불가능합니다.")
        else:
            self.withdraw(amount)   # 초안은 단순 내 계좌에서 ' - ' 를 사용해서 빼고    .withdraw = 빼다
            other.deposit(amount)   # 상대 계좌에 +기를 했었다.                         .deposit = 사전적의미 (예치 보증금 등) 두다
                                    # 같이 풀어보면서 이러한 방법이 있어서 다시 작성해보고 이해했다.

me = BankAccount(1223334444,50000)
you = BankAccount(567891011,100000)

print("계좌 세팅 결과")
print("내 계좌:", me.balance)
print("너의 계좌:", you.balance)

me.deposit(30000)
me.withdraw(40000)

me.transfer(you,30000)

print("내 계좌:", me.balance)
print("너의 계좌:", you.balance)