import csv
import datetime

# https://docs.google.com/spreadsheets/d/e/2PACX-1vQxq9zcIq21gygle-H6AqPf4TaTsMFnuGBMIyquEVbdx_lz-w0rD6MgBhik5NkfSwGbTsW1WscN-lRi/pub?gid=0&single=true&output=csv
month = 1
day   = 1


#
# Convert string to date if possible
#
def toDate(text):

    date_formats=['%B %d %Y','%d %B %Y']

    if text == '' : return ""
    for i, fmt in enumerate(date_formats):

        try:
            return datetime.datetime.strptime(text,fmt)
        except:
            c=1

    return text


#
# Create a pretend date
#

def fakeDate():

    global month
    global day
    d=datetime.datetime(2022, month, day)
    day=day+1
    if day > 28 :
        day = 1
        month = month +1

    return d

#
# Convert data into a blog post entry file
# file name comes from  even date or week date
# or is manufactored
#
def toFile(data):

    print data
    if 'group' not in data: return
    if data['group']=='': return

    filedate=fakeDate()
    data['format']='world_tour'
    data['layout']='event'
    data['type']='live'
    data['title']=data['group']


    if 'time' in data:
          t=data['time']
          if isinstance(t, str):
             t=t.replace(':', '')
             if t=='TBD' : t=""
             data['time']=t

    if 'date' in data:
     date=data['date']
     date=toDate(date)
     if isinstance(date,datetime.datetime):
         filedate=date
         data['date']=date.strftime("%Y-%m-%d")
     else:
         del data['date']

     if 'week' in data:
      week=data['week']
      week=toDate(week)
      if isinstance(week,datetime.datetime):
          data['week']=week.strftime("%Y-%m-%d")
          if filedate=='' : filedate=week
      else:
          del data['week']



    group=data['group']

    filename="../_events/world_tour/"+filedate.strftime("%Y-%m-%d") +'-'+group+ '-world-tour.md'
    print "file ",filename

    md= open(filename, 'w')
    md.write("---\n")
    separator = '","'
    for i,(k,v) in enumerate(data.items()):
      #v=list(set(v)) #list(set(v))
      line=k+' : '+v
      md.write(line+'\n')

    md.write("---\n")
    md.close()


    # for i,(k,v) in enumerate(data.items()):
      # print k,"->",v


#return d.strftime("%Y-%m-%d") + '-worldtour.md'


file   = open('tour.csv', 'r')
reader = csv.reader(file, delimiter=',', quotechar='"')

#organiser	week	date	time	zone	area	jug	_	_	_	language	presenter1	presenter2	presenter3	notes	_	link
#fields = ["_","_","week","date","time","zone","area","group","notes","_","leader","_","Language","presenters","presenters","presenters","notes","contacts","link","_","_"]


for i, row in enumerate(reader):

  if i == 0 : fields = row
  if i > 3 :
      # data
      results={}
      print "======"
      for c, cell in enumerate(row):
          key = fields[c]
          cell=cell.strip()
          if cell !="" and key !="_":
              cell = cell.replace("\n",' ')
              cell = cell.replace('"','')
              cell = cell.replace("'",'')
              cell = cell.replace('(','')
              cell = cell.replace(')','')
              cell = cell.replace(',',' ')
              cell = cell.replace('1st','1')
              cell = cell.replace('2nd','2')
              cell = cell.replace('3rd','3')
              cell = cell.replace('4th','4')
              cell = cell.replace('5th','5')
              cell = cell.replace('6th','6')
              cell = cell.replace('7th','7')
              cell = cell.replace('8th','8')
              cell = cell.replace('confirmed','')
              value=results.get(key,"")
              value=value+cell
              results[key]=value
              #print key,"==",value




      toFile(results)

file.close()
