import privateData
from html.parser import HTMLParser
from datetime import datetime, timedelta

class MyHTMLParser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    HTMLParser.unwanted_tag = ['div','i','a','br']
    HTMLParser.lectuteInWeek = []
    HTMLParser.day = 0

  def GetLectuteInWeek(self, HTMLtext):
    for i in range(0,7):
      HTMLParser.lectuteInWeek.append([])
      parser.feed(HTMLtext[i])
      HTMLParser.day += 1
    return HTMLParser.lectuteInWeek
  
  def handle_data(self, data):
    HTMLParser.lectuteInWeek[HTMLParser.day].append(data)

parser = MyHTMLParser()

