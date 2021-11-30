class Figure:
    def __init__(self, fig_type, position_x, position_y):
        self.type = fig_type
        self.x, self.y = position_x, position_y


class Game:
    def __init__(self):
        self.pole = [[" ", "A", "B", "C", "D", "E", "F", "G", "H", " "],
                     ["1", "R", "N", "B", "Q", "K", "B", "N", "R", "2"],
                     ["2", "P", "P", "P", "P", "P", "P", "P", "P", "2"],
                     ["3", "•", "•", "•", "•", "•", "•", "•", "•", "3"],
                     ["4", "•", "•", "•", "•", "•", "•", "•", "•", "4"],
                     ["5", "•", "•", "•", "•", "•", "•", "•", "•", "5"],
                     ["6", "•", "•", "•", "•", "•", "•", "•", "•", "6"],
                     ["7", "p", "p", "p", "p", "p", "p", "p", "p", "7"],
                     ["8", "r", "n", "b", "q", "k", "b", "n", "r", "8"],
                     [" ", "A", "B", "C", "D", "E", "F", "G", "H", " "],
                     ]
        self.letter_index = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        self.playing = True
        self.current_player = 1

    def show_pole(self):
        for row in self.pole[::-1]:
            print(" ".join(row))

    def play(self):
        while self.playing:
            self.show_pole()
            if self.current_player:
                message = "White POWER!!!\nInput your step like a: B2-B4\n>>> "
            else:
                message = "It's blacks time, let's do this job, nigga\n>>> "
            step = input(message)
            self.analyze_step(step)
            self.update_game()

    def analyze_step(self, step):
        # analyze correct input data
        start_position = step.split('-')[0]
        finish_position = step.split('-')[1]
        is_figure = self.analyze_figure(start_position)
        if is_figure:
            if self.current_player and is_figure.isupper() or not self.current_player and is_figure.islower():
                if start_position[0] in self.letter_index.keys() and 0 < int(start_position[1]) < 9:
                    if finish_position[0] in self.letter_index.keys() and 0 < int(finish_position[1]) < 9:
                        # analyze figure's available moves
                        available_moves = self.get_figures_available_moves(is_figure, start_position)
                        print("available_moves:", available_moves)
                        # analyze figure's opportunity to do this step
                        if finish_position in available_moves:
                            self.change_places(is_figure, start_position, finish_position)
                            if self.current_player == 1:
                                self.current_player = 0
                            else:
                                self.current_player = 1
                        else:
                            error_message = "Данный ход для выбранной фигуры недоступен или список доступных ходов пуст"
                            self.show_error(error_message)
                    else:
                        error_message = f"{finish_position} - недопустимая (несуществующая) конечная позиция для хода"
                        self.show_error(error_message)
                else:
                    error_message = f"{start_position} - недопустимая (несуществующая) исходная позиция для хода"
                    self.show_error(error_message)
            else:
                error_message = "Сейчас время сходить другому игроку"
                self.show_error(error_message)
        else:
            error_message = "На выбранной Вами клетке нет фигуры чтобы сделать ход"
            self.show_error(error_message)

    def change_places(self, figure: str, start: str, finish: str) -> None:
        """
        Replace figures in pole-list
        :param figure:
        :param start:
        :param finish:
        :return:
        """
        start_col = self.letter_index[start[0]]
        start_row = int(start[1])
        finish_col = self.letter_index[finish[0]]
        finish_row = int(finish[1])
        self.pole[start_row][start_col] = "•"
        self.pole[finish_row][finish_col] = figure
        return

    def get_figures_available_moves(self, figure: str, start_position: str) -> list:
        """
        Define current figure available psotions
        :param figure: string a-figure-type
        :param start_position: string
        :return: list of available positions
        """
        available_moves = []
        if figure == "P" or figure == 'p':
            if self.current_player:
                if start_position[1] == "2":
                    all_moves = [start_position[0] + str(int(start_position[1])+1),
                                       start_position[0] + str(int(start_position[1])+2)]
                else:
                    left_diag = self.pole[int(start_position[1])+1][self.letter_index[start_position[0]] - 1]
                    right_diag = self.pole[int(start_position[1])+1][self.letter_index[start_position[0]] + 1]
                    print("Left diagonal:", left_diag)
                    print("Right diagonal:", right_diag)
                    front_position = start_position[0] + str(int(start_position[1]) + 1)
                    if self.is_node_empty(front_position):
                        all_moves = [front_position]
                    else:
                        all_moves = []
                    if left_diag != "•" and not left_diag.isdigit():
                        all_moves.append(
                            list(self.letter_index.keys())[
                                list(self.letter_index.keys()).index(start_position[0]) - 1
                            ] + str(int(start_position[1]) + 1)
                        )
                    if right_diag != "•" and not right_diag.isdigit():
                        all_moves.append(
                            list(self.letter_index.keys())[
                                list(self.letter_index.keys()).index(start_position[0]) + 1
                            ] + str(int(start_position[1]) + 1)
                        )
            else:
                if start_position[1] == "7":
                    all_moves = [start_position[0] + str(int(start_position[1])-1),
                                       start_position[0] + str(int(start_position[1])-2)]
                else:
                    left_diag = self.pole[int(start_position[1])-1][self.letter_index[start_position[0]] - 1]
                    right_diag = self.pole[int(start_position[1])-1][self.letter_index[start_position[0]] + 1]
                    print("Left diagonal:", left_diag)
                    print("Right diagonal:", right_diag)
                    front_position = start_position[0] + str(int(start_position[1]) - 1)
                    if self.is_node_empty(front_position):
                        all_moves = [front_position]
                    else:
                        all_moves = []
                    if left_diag != "•" and not left_diag.isdigit():
                        all_moves.append(
                            list(self.letter_index.keys())[
                                list(self.letter_index.keys()).index(start_position[0]) - 1
                            ] + str(int(start_position[1]) - 1)
                        )
                    if right_diag != "•" and not right_diag.isdigit():
                        all_moves.append(
                            list(self.letter_index.keys())[
                                list(self.letter_index.keys()).index(start_position[0]) + 1
                            ] + str(int(start_position[1]) - 1)
                        )
            available_moves = all_moves

        # for move_position in all_moves:
        #     if move_position != all_moves[-1]:
        #         if self.is_node_empty(move_position):
        #             available_moves.append(move_position)
        #     else:
        #         available_moves.append(move_position)

        return available_moves

    def is_node_empty(self, position: str) -> bool:
        """
        Define node value
        :param position: string <B2>
        :return: True if node is empty and there is no figure on it else False
        """
        node = self.pole[int(position[1])][self.letter_index[position[0]]]
        if node == "•":
            return True
        else:
            return False

    def analyze_figure(self, position):
        figure_type = self.pole[int(position[1])][self.letter_index[position[0]]]
        if figure_type == "P":
            return "P"
        elif figure_type == "p":
            return "p"
        elif figure_type == "R":
            return "R"
        elif figure_type == "r":
            return "r"
        elif figure_type == "N":
            return "N"
        elif figure_type == "n":
            return "n"
        elif figure_type == "B":
            return "B"
        elif figure_type == "b":
            return "b"
        elif figure_type == "Q":
            return "Q"
        elif figure_type == "q":
            return "q"
        elif figure_type == "K":
            return "K"
        elif figure_type == "k":
            return "k"
        else:
            return False

    def update_game(self):
        pass

    def show_error(self, error):
        print(error)


def main():
    Game().play()


if __name__ == "__main__":
    main()