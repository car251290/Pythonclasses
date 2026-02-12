def func():
    print("Hello students!")

    def count_up_to(limit):
        counter = 1

        while counter <= limit:
            print(counter)
            counter += 1

    count_up_to(5)

    def count_down_from(limit):
        counter = limit

        while counter > 0:
            print(counter)
            counter -= 1

    count_down_from(5)
if __name__ == "__main__":
    func()