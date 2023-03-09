import privateData
import analysisData
import analysisLecture
import googleCalendarFunc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Open Chrome
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.headless = True

try :
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
except :
  driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
#driver = webdriver.Chrome("/usr/bin/chromium", options=options)
#driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

driver.get(privateData.destination)
print(driver.title)

#login
username_input = driver.find_element("xpath",privateData.X_path_login_username)
username_input.send_keys(privateData.gibbon_username)

password_input = driver.find_element("xpath",privateData.X_path_login_password)
password_input.send_keys(privateData.gibbon_password)

login_box = driver.find_element("xpath",privateData.X_path_login_submitButton)
login_box.submit()

# Go to 'Student' page
driver.find_element('xpath',privateData.Xpath_of_learn_button)
timetable_page = driver.find_element('xpath',privateData.Xpath_of_timetable_button).get_property("href")

# define searching & scraping function
def searching(classroom) :
  driver.get(timetable_page)
  driver.find_element('xpath',privateData.Xpath_of_search_box).clear()
  driver.find_element('xpath',privateData.Xpath_of_search_box).send_keys(classroom)
  driver.find_element('xpath',privateData.Xpath_of_search_submit_button).submit()
  driver.find_element('xpath',privateData.Xpath_of_View_detail_button).click()

def scaping():
  lecture = []
  for i in range(0,7):
    get_div = driver.find_element('xpath','//*[@id="ttWrapper"]/table/tbody/tr[2]/td[' + str(i+2) + ']')
    lecture.append(get_div.get_attribute('innerHTML'))
  parser = analysisData.MyHTMLParser()
  lectureInWeek = parser.GetLectuteInWeek(lecture)
  return lectureInWeek

def GIBBIN()  :
  for classroom in privateData.ESCK_Class :
    searching(classroom)   #goToPages
    CALENDAR_ID = privateData.calendar_id[classroom]
    exampleOfLecture = scaping()  #getData
    analysedLecture = analysisLecture.analyseLecture(exampleOfLecture) #analyseData to day / str /end / subject
    service = googleCalendarFunc.build("calendar", "v3", credentials=googleCalendarFunc.credentials)
    googleCalendarFunc.clearEvent(CALENDAR_ID)
    for item in analysedLecture:
      googleCalendarFunc.add_event_to_calendar(CALENDAR_ID,item.subject, item.start, item.end)
    print("DONE "+classroom)

attempts = 0
success = False
while attempts < 4 and not success:
    try:
        GIBBIN()
        success = True
    except:
        attempts += 1
        if attempts == 4:
            break

        try :
          driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        except :
          driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
        
        driver.get(privateData.destination)

        username_input = driver.find_element("xpath",privateData.X_path_login_username)
        username_input.send_keys(privateData.gibbon_username)

        password_input = driver.find_element("xpath",privateData.X_path_login_password)
        password_input.send_keys(privateData.gibbon_password)

        login_box = driver.find_element("xpath",privateData.X_path_login_submitButton)
        login_box.submit()

if attempts == 4 :
  f = open("log.txt", "a")
  f.write("failed " + (datetime.utcnow()+timedelta(hours=7)).strftime('%Y-%m-%dT%H:%M:%S'))
  f.close()
else :
  f = open("log.txt", "a")
  f.write("suscessed " + (datetime.utcnow()+timedelta(hours=7)).strftime('%Y-%m-%dT%H:%M:%S'))
  f.close()