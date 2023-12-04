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

#________________ testing of register url ____________________

    def test_register(self):
        sent_Name=Name
        sent_Email=Email
        sent_Password=Password
        
        response=obj.registration(sent_Name,sent_Email,sent_Password)
        data=sent_Name,sent_Email,sent_Password
        
        verify_data=obj.verify_register(Name,Email,Password)
        
        verified_Name=verify_data.Name,
        verified_Email=verify_data.Email,
        verified_Password=verify_data.Password
        
        data_back=verified_Name,verified_Email,verified_Password
        
        # print("data in database : ",data_back)
        # print("data  we sent : ",data)
        
        if data==data_back:
            # self.assertEqual(data, data_back, "True")
            return response
        else:
            # self.assertEqual(data, data_back, "False")
            return "invalid"
        
#______________testing of login url___________________
            
    def test_login(self):
        login_response=obj.user_login(Email,Password)
        status=login_response[1]
        print(status,"========")
        result=False
        self.assertEqual(status, result)
        return login_response
    

    # def test_string(self):
    #     a = 'some'
    #     b = 'some'
    #     self.assertEqual(a, b)

    # def test_boolean(self):
    #     a = True
    #     b = True
    #     self.assertEqual(a, b)
    
    

# run=TestFlaskApp()
# run.test_register()
# run.test_login()

#__________________testing of logout url___________________

# def test_logout():
#     response=logout_user()
#     print(response)
    
# test_logout()
        

        
#___________________testing / (home) url_______________________

    # def test_home(self):
    #     response=self.app.get('/',follow_redirects=True)
    #     self.assertEqual(response.status_code,200)
        
#__________________testing addtask url________________________

    # def test_addtask(self):
    #     response=self.app.get('/addtask',obj.addtask(Name,StartDate,StartTime,DueDate),follow_redirects=True)
    #     self.assertEqual(response.status_code,200)
        
#__________________testing fetchtask url________________________

        
    # def test_fetchtask(self):
    #     response=self.app.get('/fetchtask/ID',follow_redirects=True)
    #     data=obj.fetchtask(ID)
    #     # print(data,"============")
    #     self.assertEqual(response.status_code,200)

# #__________________testing tasklist url________________________

        
    # def test_tasklist(self):
    #     response=self.app.get('/tasklist',follow_redirects=True)
    #     data=obj.taskilist()
    #     # print(data,"--------------------------")
    #     self.assertEqual(response.status_code,200)
        
#__________________testing deletetask url________________________

        
    # def test_deletetask(self):
    #     response=self.app.get('/deletetask/ID',follow_redirects=True)
    #     obj.DeleteTask(ID)
        
    #     self.assertEqual(response.status_code,200) 
    
#__________________testing updatetask url________________________

        
    # def test_updatetask(self):
    #     response=self.app.get('/updatetask',follow_redirects=True)
    #     obj.update_task(ID,TaskName,StartDate,StartTime,DueDate)
    #     self.assertEqual(response.status_code,200)
        
#__________________testing maketaskhistory url________________________

        
    # def test_maketaskhistory(self):
    #     response=self.app.get('/maketaskhistory/ID',follow_redirects=True)
    #     obj.makehistory(ID)
    #     self.assertEqual(response.status_code,200)
        
    
#__________________testing gettaskhistory url________________________

        
    # def test_gettaskhistory(self):
    #     response=self.app.get('/gettaskhistory',follow_redirects=True)
    #     data=obj.gettaskhistory(StartDate)
    #     print(data,"~~~~~~~~~~~~~~~~")
    #     self.assertEqual(response.status_code,200)
        


if __name__ == '__main__':
    unittest.main()
