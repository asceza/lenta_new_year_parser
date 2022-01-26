from datetime import datetime
import csv
from time import sleep
from random import choice
from one_link_cost_parser import get_html_by_requests


first_url = 0

current_date ="{:%d.%m.%Y}".format(datetime.now())

INPUT_FILENAME = "blank_23.01.2022.csv"
OUTPUT_FILENAME = f"blank_{current_date}.csv"

sleep_time = [0.3, 0.4, 0.5]



def copy_first_row_and_add_date():
    with open(INPUT_FILENAME, "r+", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            row.append(current_date)
            with open(OUTPUT_FILENAME, "a", encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(row)
            break  # после одной итерации - выход из цикла



def add_cost_to_csv():
    with open(INPUT_FILENAME, "r+", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        header_row = next(reader)  # пропускаем заголовок
        n = first_url
        if n > 0:  # в цикле пропускаем необходимое число строк
            for i in range(n):
                next(reader)
        for row in reader:
            sleep(choice(sleep_time))

            useragents = open("useragent.txt").read().split("\n")
            useragents = useragents[0:-1]  # убираем последний элемент (строку), в котором содержится "\n"
            useragent = {"User-Agent": choice(useragents)}

            cost = get_html_by_requests(row[1], useragent)
            row.append(cost)
            with open(OUTPUT_FILENAME, "a", encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(row)



if __name__ == '__main__':
    copy_first_row_and_add_date()
    add_cost_to_csv()
