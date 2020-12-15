import random
import datetime

MIN_MONTH = 1
MAX_MONTH = 12
MIN_YEAR = 1980
MAX_YEAR = 2020
NUMBER_OF_MONTHS = 12

month = random.randint(MIN_MONTH, MAX_MONTH)
year = random.randint(MIN_YEAR, MAX_YEAR)

difference_month = datetime.date.today().month - month
difference_year = datetime.date.today().year - year

if difference_month < 0:
    difference_month += NUMBER_OF_MONTHS
    difference_year -= 1

print(str(difference_month) + "/" + str(difference_year))
