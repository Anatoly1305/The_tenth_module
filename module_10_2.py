import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.remaining_enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.remaining_enemies > 0:
            self.days += 1
            daily_defense = min(self.power, self.remaining_enemies)
            self.remaining_enemies -= daily_defense
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.remaining_enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


if __name__ == "__main__":
    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight .start()

    first_knight.join()
    second_knight .join()

print("Все битвы закончились!")