import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import csv
from datetime import datetime
import calendar



#Set variables

day_from = 1
month_to = 4
year     = 2016
n_sensor = 6



cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("http://rimms.dyndns.org/rimms/index.php")

br.select_form(nr=0)
br.form['Uid'] = 'castelfranco'
br.form['Pwd'] = 'castelfranco'
br.submit()



#Qui passo i 4 sensori

for i in range (1,n_sensor):
	#Apro un file per ogni sensore
	with open("cappella_"+str(i)+".csv", 'w') as csvfile:	

		#Scrivo su file
		fieldnames = ["Data","Umidita R.","Batteria","Temperatura"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()	


		for month in range (1,month_to):
		
			br.open("http://rimms.dyndns.org/rimms/Grafico.php")
			br.select_form(nr=0)	
		
			br.form['Stanza'] = ['Chiesa']

			cappella = 'Cappella ' + str(i)
			br.form['Sensore'] = [cappella]
			
			#StackOverflow MADNESS
			br.form.set_all_readonly(False)
			
			
			
			#giorno = str(day)
			#br.form['GgDay'] = [giorno]
			#br.form['MmDay'] = ['1']    
			#br.form['YyDay'] = ['2017']

			#br.find_control("ChkDay").items[0]="Periodico"
			br.find_control("ChkDay").items[1].selected = "True"

			str_start = str(day_from)
			br.form['GgFrom'] = [str_start]
			br.form['MmFrom'] = [str(month)]    
			br.form['YyFrom'] = [str(year)]
			
			str_end = str(calendar.monthrange(year,month)[1])
			br.form['GgTo'] = [str_end]
			br.form['MmTo'] = [str(month)]    
			br.form['YyTo'] = [str(year)]



	
			print "=============="+ cappella +"======================"

			submit_response = br.submit(name='MngGrf', label='Esporta Tabella')
			
			#print br.response().read()

			appo = br.response().read().replace("\n'", ";")	
			
			#print appo
	
	
	
			vect =  appo.split(";")
			##print vect
	
			k=12
			while (k<len(vect)-3):
				writer.writerow({fieldnames[0]:vect[k+1], fieldnames[1]:vect[k+2],fieldnames[2]:vect[k+3],fieldnames[3]:vect[k] })
				k=k+4
			
				
			
	
			









