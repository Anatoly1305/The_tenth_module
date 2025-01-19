import time
import threading
from random import randint

class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            random_value = randint(50, 500)
            self.balance += random_value
            print(f"Пополнение: {random_value}. Баланс: {self.balance}.")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_value = randint(50, 500)
            print(f'Запрос на {random_value}.')
            if random_value <= self.balance:
                self.balance -= random_value
                print(f"Снятие: {random_value}. Баланс: {self.balance}.")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target = Bank.deposit, args = (bk,))
th2 = threading.Thread(target = Bank.take, args = (bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')