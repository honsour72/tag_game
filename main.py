from random import shuffle


class Game:
    def __init__(self):
        self.working = True
        self.node_parts = ["╔════╗", "║ {} ║", "╚════╝"]
        self.nums = [str(x) for x in range(1, 16)] + [" "]
        # shuffle(self.nums)
        self.empty_x, self.empty_y = 0, 0
        self.counter = 0
        self.win_message = "╔═══════════════════════════╗\n" \
                           "║ ПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ! ║\n" \
                           "╚═══════════════════════════╝\nКоличество ходов: {}"

    def show_current_map(self):
        for row in range(4):
            for part in self.node_parts:
                for column in range(4):
                    if part == "║ {} ║":
                        if len(self.nums[row * 4 + column]) == 1:
                            value = part.format(self.nums[row * 4 + column] + " ")
                        else:
                            value = part.format(self.nums[row * 4 + column])
                        if value == '║    ║':
                            self.empty_x = row + 1
                            self.empty_y = column + 1
                        print(value, end="")
                    else:
                        print(part, end="")
                print()
        return

    def play(self):
        while self.working:
            self.show_current_map()
            number = input("Сделайте шаг: введите цифру для того что бы она заполнила пустоую клетку:\n>>> ")
            self.analyze_step(number)
            self.is_win()

    def analyze_step(self, number):
        if self.is_number_exist(number):
            self.counter += 1
            number_x, number_y = self.get_node_pos(number)
            # если введенное число в одной строке с пустой ячейкой
            # if abs(number_x - self.empty_x) == 0:
            distance_x, distance_y = abs(number_x - self.empty_x), abs(number_y - self.empty_y)
            if distance_x == 1 and distance_y == 0 or distance_y == 1 and distance_x == 0:
                self.nums[self.nums.index(number)] = "  "
                self.nums[self.nums.index(" ")] = number
                self.nums[self.nums.index("  ")] = " "
                # print(self.nums)
                # return "Движ выполнен"
                # return self.swap_nodes(number_x, number_y)
            else:
                # return "Движ невозможен"
                return self.show_mistake()
        else:
            return self.show_mistake()

    def get_node_pos(self, number):
        return self.nums.index(number) // 4 + 1, self.nums.index(number) % 4 + 1

    def is_number_exist(self, number):
        return 1 if number in self.nums else 0

    @staticmethod
    def show_mistake():
        print("Невозможный ход!\nВведите другой!")

    def is_win(self):
        if self.nums == [str(x) for x in range(1, 16)] + [" "] or \
                self.nums == ["1", "5", "9", "13", "2", "6", "10", "14", "3", "7", "11", "15", "4", "8", "12", " "]:
            self.show_current_map()
            print(self.win_message.format(self.counter))
            self.working = False


def main():
    Game().play()


if __name__ == "__main__":
    main()
