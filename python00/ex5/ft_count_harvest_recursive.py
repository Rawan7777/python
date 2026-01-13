def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(day, max_day):
        if day > max_day:
            return
        print(f"Day {day}")
        count(day + 1, max_day)

    count(1, days)
    print("Harvest time!")
