from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import emoji

if __name__ == '__main__':
    calculate_salary()
    get_employees()

    print('==========================================')
    print(datetime.strftime(datetime.now(), '%d/%m/%Y'))
    print('==========================================')

    print(emoji.emojize('Python is :thumbs_up:'))