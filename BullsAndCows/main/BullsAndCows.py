import random
import sys


class game:
    number = 0
    bulls = 0
    cows = 0

    def __init__(self):
        self.menu()

    def menu(self):
        self.change = int(input('Выберите режим игры \n"1" для одиночной игры \n"2" для совместной игры\n'))
        if self.change == 1 or self.change == 2:
            self.process()
            return "Всё!"
        else:
            print('Ты не понял условие. Пока!')
        
    def playerBot(self):
        BotNum = []
        
        while len(BotNum) < 4:
            a = random.randint(0, 9)
            if a in BotNum:
                continue
            else:
                BotNum.append(a)
        return BotNum
                 
    def player1(self):
        print("Первый игрок! Вводи своё число! ")
        self.secret = []
        chislo = (int(input()) for x in range(4))
        for i in chislo:
            if i > 9 or i < 0:
                print("Ай-ай, ошибка! \nВведи натуральное положительное число 0 - 9.")
                continue
            else:
                self.secret.append(i)

    def player2(self):
        print("Второй игрок! Твой черёд! Вводи решение! ")
        self.noSecret = []
        chislo = (int(input()) for x in range(4))
        for i in chislo:
            if i > 9 or i < 0:
                print("Ай-ай, ошибка! \nВведи натуральное положительное число 0 - 9.")
                continue
            else:
                self.noSecret.append(i)

    def process(self):
        if self.change == 1:
            zagadNumber = self.playerBot()
        elif self.change == 2:
            self.player1()   
            zagadNumber = self.secret

        change2 = int(input('Кто будет вторым игроком? \n"1" если игрок \n"2" если компьютер \n'))

        while True:
            self.number += 1 
            if change2 == 1:
                self.player2()
                razgadNumber = self.noSecret
            elif change2 == 2:
                razgadNumber = self.playerBot()
            self.bulls = 0
            self.cows = 0

            for i in range(4):
                if zagadNumber[i] == razgadNumber[i]:
                    self.bulls += 1
            for i in range(4):
                if zagadNumber[i] in razgadNumber:
                    self.cows += 1

            self.cows -= self.bulls
            print(f'Введённое число второго игрока: {razgadNumber}')
            print(f'Количество итераций : {self.number}, \nКоличество быков : {self.bulls}, \nКоличество коров : {self.cows}') 
           
            if self.bulls == 4:
                print('Поздравляю! \nИгра завершена')
                startAgain = int(input('Если хотите начать заново- нажмите 1 \nЕсли выйти- нажмите 2 \n'))
                if startAgain == 1:
                    self.menu()
                elif startAgain == 2:
                    break
                else:
                    print('Что ж, судя по всему, мы не поняли друг друга, амиго')
                    break

if __name__ == "__main__":
    a = game()
