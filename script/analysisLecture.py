from datetime import datetime, timedelta

subjectName = ["ESC", "COM" , "KOS" , "AUT", "BIO", "ACT"]
subjectNameSpace = ["ESC ", "COM " , "KOS " , "AUT ", "BIO ", "ACT "]

class lecture:
  def __init__(self, day=-1 , start=-1, end=-1, subject="none"):
    self.day = day
    self.start = start
    self.end = end
    self.subject = subject


timenow = datetime.utcnow() + timedelta(hours=7)
timenow = timenow + timedelta(days = 0) 
if(timenow.weekday() != 6) : 
  timenow = timenow + timedelta(days= - (timenow.weekday()+ 1)   )
timenow = datetime(timenow.year, timenow.month, timenow.day)

def getTime(dayInWeek, start, end):
  startTime = timenow + timedelta(days = dayInWeek) + timedelta(hours=int(start[0:2])) + timedelta(minutes=int(start[3:5]))
  endTime = timenow + timedelta(days = dayInWeek) + timedelta(hours=int(end[0:2])) + timedelta(minutes=int(end[3:5]))
  return startTime, endTime

def analyseLecture(exampleOfLecture) :
  lectureData = []
  for dayInWeek in range(0,7):
    temp = exampleOfLecture[dayInWeek].copy()
    i=0
    while i< len(temp): 
      subject = "sample"
      className =  "sample"
      
      # School Close
      if temp[i] == "School Closed":
        lectureData.append(lecture(dayInWeek, "08:00" , "16:00", "School Closed"))
        i=i+1
        continue
      
      # M6 Elective subject (7XX)
      if (temp[i][0:4] == "ESC7"):  
        subject = temp[i]
        className = "วิชาเลือก"

      # Common class
      if (temp[i][0:4] in subjectNameSpace and temp[i][0:5] != "ESC 7"):  
        subject = temp[i][0:3] + temp[i][4:7]

        # class name
        if ( i == len(temp)-1 or (temp[i+1][0:3] in subjectName)) :
          className = ""
        else :
          className = temp[i+1]

      # get time
      try :    ## Check if this value NOT the class name
        timeIndex = temp.index(subject) +1 
        time = temp[timeIndex]
        start = time[0:5]
        end = time[-5:]
        startTime, endTime = getTime(dayInWeek, start, end)
      except :
        i=i+1
        continue
    
      #append data
      lectureData.append(lecture(dayInWeek,startTime,endTime,subject+" "+className))

      # remove read class
      temp.remove(subject)
      temp.remove(time)

      #noname class not have class name, index will be -1
      if(className == ""):
        i=i-1

      continue
  return lectureData