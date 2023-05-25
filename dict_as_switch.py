def one():
    print("one")


def two():
    print("two")


def bye():
    print("Bye!")
    exit()


commands = {
    "1": one,
    "2": two,
    "3": bye,
}


def main():
    while True:
        entry = input("command:")
        try:
            commands.get(entry)()
        except TypeError:
            print("unknown command")
            continue


if __name__ == '__main__':
    main()
