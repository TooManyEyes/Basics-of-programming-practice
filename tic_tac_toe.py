import random


class TicTacToe:
    def __init__(self, first_player, second_player, ):
        self.field = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']
        ]
        players = [first_player, second_player]
        random.shuffle(players)
        self.x_player, self.o_player = players
        self.step = self.x_player
        self.end_status = False
        self.winner = False
        self.steps_counter = 0
        print("Начата новая партия, первым ходит:", self.x_player)

    def check_step(self):
        return self.step

    def show_field(self):
        displaying_field = [' '.join(line) for line in self.field]
        return '\n'.join(displaying_field)

    def check_game_end(self):
        if self.end_status:
            return self.end_status
        else:
            return 'игра ещё не закончилась'

    def check_winner(self):
        if self.steps_counter == 9:
            self.end_status = True
            return 'ничья!'
        for i in range(3):
            if self.field[0][i] == self.field[1][i] == self.field[2][i] and self.field[0][i] != '*':
                self.winner = self.x_player if self.field[0][i] == 'X' else self.o_player
                self.end_status = True
        for i in range(3):
            if len(set(self.field[i])) == 1 and self.field[i][0] != '*':
                self.winner = self.x_player if self.field[i][0] == 'X' else self.o_player
                self.end_status = True
        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != '*':
            self.winner = self.x_player if self.field[0][0] == 'X' else self.o_player
            self.end_status = True
        if self.field[0][2] == self.field[1][1] == self.field[2][1] and self.field[0][2] != '*':
            self.winner = self.x_player if self.field[0][2] == 'X' else self.o_player
            self.end_status = True
        if self.winner:
            return self.winner
        else:
            return 'победитель не определен'

    def place_nought(self, x_cord, y_cord):
        if self.step == self.o_player:
            if self.field[x_cord][y_cord] == '*':
                self.field[x_cord][y_cord] = 'O'
                self.step = self.x_player
                self.steps_counter += 1
            else:
                return 'клетка уже занята!'
        else:
            print('Вы не можете ходить! Сейчас ход игрока {0}'.format(self.x_player))

    def place_cross(self, x_cord, y_cord):
        if self.step == self.x_player:
            if self.field[x_cord][y_cord] == '*':
                self.field[x_cord][y_cord] = 'X'
                self.step = self.o_player
                self.steps_counter += 1
            else:
                return 'клетка уже занята!'
        else:
            print('Вы не можете ходить! Сейчас ход игрока {0}'.format(self.o_player))

    def restart(self):
        self.field = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']
        ]
        self.steps_counter = 0


first_game = TicTacToe('Зузанна', 'Милош')
first_game.place_cross(0, 0)
first_game.place_cross(1, 1)
first_game.place_nought(2, 2)
first_game.place_cross(1, 1)
first_game.place_nought(1, 2)
first_game.place_cross(1, 0)
first_game.place_nought(0, 2)
print(first_game.show_field())
print('Победитель:', first_game.check_winner())


print('\nПерезапустим игру и протестируем ход на клетку, в которой уже что-то стоит')
first_game.restart()
first_game.place_cross(1, 0)
first_game.place_nought(1, 0)
first_game.place_nought(1, 1)
print(first_game.show_field())


print('\nТеперь давай попробуем сыграть в ничью')
first_game.restart()
first_game.place_cross(0,1)
first_game.place_nought(0, 2)
first_game.place_cross(0,0)
first_game.place_nought(1,0)
first_game.place_cross(1,2)
first_game.place_nought(1,1)
first_game.place_cross(2,0)
first_game.place_nought(2,1)
first_game.place_cross(2,2)
print(first_game.show_field())
print(first_game.check_winner())
