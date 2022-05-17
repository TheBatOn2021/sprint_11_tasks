class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.itemsM = []
        self.maximum = None
        self.size = 0

    def print_get_max(self):
        print("!", self.maximum)

    def push(self, item):
        if self.maximum is None:
            self.maximum = item
        if item >= self.maximum:
            self.itemsM.append(item)
            self.maximum = item
        else:
            self.itemsM.append(self.maximum)
        self.items.append(item)
        self.size += 1


    def pop(self):
        if self.size > 1:
            if self.maximum <= self.items[self.size - 1]:
                self.items.pop()
                self.itemsM.pop()
                self.size -= 1
            else:
                self.items.pop()
                self.itemsM.pop()
                self.size -= 1
            self.maximum = self.itemsM[self.size-1]
        elif self.size == 1:
                self.items.pop()
                self.itemsM.pop()
                self.size = 0
                self.maximum = None
        else:
            print('! error')


def main():
    queue = StackMaxEffective()
    commands = {
        'push': queue.push,
        'pop': queue.pop,
        'get_max': queue.print_get_max
    }
    count_command = int(input())
    for i in range(count_command):
        command = input()
        operation, *value = command.split()
        if value:
            try:
                commands[operation](int(*value))
            except:
                print('Bad error')
        else:
            try:
                commands[operation]()
            except:
                print('Bad error')


if __name__ == '__main__':
    main()
