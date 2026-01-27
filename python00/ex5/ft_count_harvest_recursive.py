def ft_count_harvest_recursive():

    days = int(input("Days until harvest: "))

    def recursive_counter(day, max_day):

        if day > max_day:
            return

        print(f"Day {day}")
        recursive_counter(day + 1, max_day)

    recursive_counter(1, days)
    print("Harvest time!")
