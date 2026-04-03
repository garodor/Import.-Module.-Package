from datetime import date
from application.salary import *
from application.db.people import *

#if __name__ == '__main__'
if __name__ == '__main__':
    print(f"Текущая дата (грязный способ): {date.today()}")
    calculate_salary()
    get_employees()