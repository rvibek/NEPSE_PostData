import requests  
from pattern import web

postdata= {  
    'topTenBased' : '58', #value from Select menu (NEPSE)
    'Submit' : 'Submit'
    }
# r = requests.post('http://www.nepalstock.com/datanepse/Indices.php', data=postdata)  
r = requests.post('http://www.nepalstock.com/indices', data=postdata)
dom = web.Element(r.text)

#Working with local file
# r = open('Indices.htm')
#dom = web.Element(r.read())

#creating DOM and getting the Title corresponding to topTenBased value
# data = dom.by_tag('table.dataTable')[1]  
data = dom.by_class('table')[0]

title = data.by_tag('td')[1].content  
title = title.partition(' ')[0] #title of the table


#Iteration and storing data in array 
def content (idx):  
    mydata = []
    for i in range(0, idx):
        ad=d.by_tag('td')[i].content
        mydata.append(ad)
    mydata.append(title)
    print mydata


for d in data.by_tag('tr'):  
    idx = len(d.by_tag('td'))
    content(idx)