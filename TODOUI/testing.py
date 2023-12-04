import unittest
import random
import string
from datetime import date, timedelta
from function import Function

obj=Function()

#________________start date____________________

test_date1, test_date2 = date(2023, 12, 1), date(2023, 12, 3)
K = 7
dates_bet = test_date2 - test_date1
total_days = dates_bet.days
res = []
for idx in range(K):
    random.seed(a=None)
randay = random.randrange(total_days)
res.append(test_date1 + timedelta(days=randay))
StartDate=res[0]

#________________ due date____________________

test_date1, test_date2 = date(2023, 12, 3), date(2023, 12, 5)
K = 7
dates_bet = test_date2 - test_date1
total_days = dates_bet.days
res = []
for idx in range(K):
    random.seed(a=None)
randay = random.randrange(total_days)
res.append(test_date1 + timedelta(days=randay))
DueDate=res[0]

#__________________start time ____________________

times=[]
random.seed()
hour=random.randint(1,24)
hour_string=str(hour)
minute=random.randint(0,60)
minute_string=str(minute)
StartTime=hour_string + ":" + minute_string

#__________________ Name _____________________________

N = 7
res=''.join(random.choices(string.ascii_letters, k=N))
Name=''.join(random.choices(string.ascii_letters, k=N))
Email=res + "@gmail.com"
Password=''.join(random.choices(string.ascii_letters, k=N))
TaskName=''.join(random.choices(string.ascii_letters, k=9))

#_________________ ID ___________________________

ID=random.randint(90,100)
class TestFlaskApp(unittest.TestCase):
    
    def register_testing(self):
        response=obj.registration(Name,Email,Password)
        status=response[1]
        self.assertEqual(status, True)

    def test_login(self):
            login_response=obj.user_login(Email,Password)
            status=login_response[1]
            # try:
            self.assertEqual(False, True)
            # except Exception as e:
            #     print(e)
            

if __name__ == '__main__':
    unittest.main()