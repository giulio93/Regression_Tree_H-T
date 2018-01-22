import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import unicodecsv as csv
from datetime import datetime
import calendar



#Set variables

day_from = 1
month_to = 4
year     = 2016












with open("wheather_2017_3.csv",'w') as csvfile:

	#[u'Time (CET)', u'Temp.', u'Windchill', u'Dew Point', u'Humidity', u'Pressure', u'Visibility', u'Wind Dir', u'Wind Speed', u'Gust Speed', u'Precip', u'Events', u'Conditions']

	
	fieldnames = ["Time (CET)","Temp.","Windchill","Dew Point","Humidity","Pressure","Visibility","Wind Dir","Wind Speed","Gust Speed","Precip","Events","Conditions"]

	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	for month in range(1,month_to):
	
		for day in range(day_from,calendar.monthrange(year,month)[1]+1):
			
			br = mechanize.Browser()
			br.open("https://www.wunderground.com/history/")

			response = br.response()

			print response.geturl() # URL of the page we just opened
			 
			def select_form(form):
			  return form.attrs.get('id', None) == 'trip'

			br.select_form(predicate=select_form)

			br.form['code'] = 'Castelfranco Veneto'
			br.form['month'] = [str(month)]
			br.form['day'] = [str(day)]
			br.form['year'] = [str(year)]
			br.submit()
		
			soup = BeautifulSoup(br.response().read(),"lxml")

			header_fields = soup.find_all('thead')

			header_fields2 = [element.text for element in header_fields[2].find_all('th')]

		
			all_rows = soup.find_all('tr')

			print "==========="+str(day)+" - "+str(month)+" - "+str(year)+"============================="	

			for x in all_rows:
				

				a =  x.attrs
	
				for f in a:
					if(a['class']== ['no-metars']):
			
		
						data = [element.text for element in x.find_all('td')]

						i=0
						for appo in data:
							data[i] = data[i].replace('\n','')
							if(appo.find("-")>0):
								data[i] = "0"
							i=i+1
						
						dict_row = {}						
						i=0
						j=0
						for k in range(0,len(header_fields2)):
							if(header_fields2[i] == fieldnames[j]):
								#print header_fields2[i]
								#print fieldnames[j]
								#print header_fields2[i] == fieldnames[j]
								dict_appo = {fieldnames[j]:data[i].encode('utf-8')}
								
								dict_row.update(dict_appo)
								i=i+1
								j=j+1
								
							else:
								print header_fields2[i]
								print fieldnames[j]
								dict_appo = {fieldnames[j]:"0"}
								dict_row.update(dict_appo)
								j=j+1
								
							
								
									
								
									
							
						#writer.writerow({fieldnames[0]:data[0], fieldnames[1]:data[1],fieldnames[2]:data[2],fieldnames[3]:data[3],fieldnames[4]:data[4],
								#fieldnames[5]:data[5],fieldnames[6]:data[6],fieldnames[7]:data[7],fieldnames[8]:data[8],
								#fieldnames[9]:data[9],fieldnames[10]:data[10],fieldnames[11]:data[11],fieldnames[12]:data[12]})
		
			
						#print dict_row
						writer.writerow(dict_row)


			









