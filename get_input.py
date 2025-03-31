
def get_input():
    ticket_type = input("What kind of ticket? (1) AAA, (2) BBB, (3) CCC ")
    count = input("How many tickets: ")
    return ticket_type, count


def main():
    get_input()


if __name__ == "__main__":
    main()