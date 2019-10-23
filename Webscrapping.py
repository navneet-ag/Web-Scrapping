#Name		:Navneet Agarwal	
#Roll no.	:2018348	
#Section	:B	
#Group		:5

# function to get weather response
def weather_response(location, API_key):
	import urllib.request
	u = "http://api.openweathermap.org/data/2.5/forecast?"
	url = u + "q=" + location +"&APPID=" +API_key	
	response = urllib.request.urlopen(url)
	data=response.read()
	data=str(data) #conversion of bytes object to str
	l=len(data)
	data1=data[2:l-1]
	return(data1) 

# function name: to check for valid response 
def has_error(location,json) :
	length=len(location)
	index=json.index("name") #b is written as it accepts bytes or integer objects only
	lctn=json[index+7:index+7+length] 
	lctn=lctn.lower()
	location=location.lower()
	if lctn != location :	
		return(True)
	else:
		return(False)

# function to get attributes on nth day
def get_temperature (json, n=0 ,t="03:00:00"):
	if( n==3 or n==1 or n==2 or n==0 or n==4) and (t=="03:00:00" or t=="3:00" or t=="6:00" or t=="9:00" or t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"  or t=="06:00:00" or t=="09:00:00" or t=="12:00:00" or t=="15:00:00" or t=="18:00:00" or t=="21:00:00"):
		if (t=="3:00" or t=="6:00" or t=="9:00" ):
			time= "0" + t + ":00" 
		elif( t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00" ):
			time= t + ":00"	
		else:
			time=t
		import datetime
		dt_=datetime.date.today() + datetime.timedelta(days=n)#adding n days to date
		dt_=str(dt_)
		dt_time= dt_ + " " + time
		index=json.find(dt_time)
		index=json.rfind('\"temp\"',0,index)
		ind2=json.find(',',index+6)
		temp=json[index +7:ind2]
		temp=float(temp)	
		return(temp)
	else :
		return("")
		

def get_humidity(json, n=0,t="03:00:00"):
	if( n==3 or n==1 or n==2 or n==0 or n==4) and (t=="03:00:00" or t=="3:00" or t=="6:00" or t=="9:00" or t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00" or t=="06:00:00" or t=="09:00:00" or t=="12:00:00" or t=="15:00:00" or t=="18:00:00" or t=="21:00:00"):
		if (t=="3:00" or t=="6:00" or t=="9:00" ):
			time= "0" + t + ":00" 
		elif( t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"):
			time = t + ":00"	
		else:
			time=t
		import datetime
		dt_=datetime.date.today() + datetime.timedelta(days=n)
		dt_=str(dt_)
		dt_time= dt_ + " " + time
		index=json.find(dt_time)
		index=json.rfind('\"humidity\"',0,index)
		ind2=json.find(',',index+10)
		humid=json[index+11:ind2]
		humid=float(humid)
		return(humid)
	else :
		return("")
def get_pressure(json, n=0,t="03:00:00"):
	if( n==3 or n==1 or n==2 or n==0 or n==4) and (t=="03:00:00" or t=="3:00" or t=="6:00" or t=="9:00" or t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00" or t=="06:00:00" or t=="09:00:00" or t=="12:00:00" or t=="15:00:00" or t=="18:00:00" or t=="21:00:00"):
		if (t=="3:00" or t=="6:00" or t=="9:00"):
			time= "0" + t + ":00" 
		elif( t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"):
			time= t + ":00"	
		
		else:
			time=t
		import datetime
		dt_=datetime.date.today() + datetime.timedelta(days=n)
		dt_=str(dt_)
		dt_time= dt_ + " " + time
		index=json.find(dt_time)
		index=json.rfind('\"pressure\"',0,index)
		ind2=json.find(",",index+10)
		press=json[index+11:ind2]
		press=float(press)
		return(press)
	else :
		return("")		
def get_wind(json, n=0,t="03:00:00"):
	
	if( n==3 or n==1 or n==2 or n==0 or n==4) and (t=="03:00:00" or t=="06:00:00" or t=="09:00:00" or t=="12:00:00" or t=="15:00:00" or t=="18:00:00" or t=="21:00:00" or  t=="3:00" or t=="6:00" or t=="9:00" or t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"):
		if (t=="3:00" or t=="6:00" or t=="9:00" ):
			
			time= "0" + t + ":00" 
		elif( t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"):
			time= t + ":00"	
		else:
			time=t
		import datetime
		dt_=datetime.date.today() + datetime.timedelta(days=n)
		dt_=str(dt_)
		dt_time= dt_ + " " + time
		index=json.find(dt_time)
		index=json.rfind('\"wind\"',0,index)
		ind2=json.find(",",index+15)
		wind=json[index+16:ind2]
		wind=float(wind)
		return(wind)
	else :
		return("")
def get_sealevel(json, n=0,t="03:00:00"):
	if( n==3 or n==1 or n==2 or n==0 or n==4) and (t=="03:00:00" or t=="06:00:00" or t=="09:00:00" or t=="12:00:00" or t=="15:00:00" or t=="18:00:00" or t=="21:00:00" or t=="3:00" or t=="6:00" or t=="9:00" or t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"):
		if (t=="3:00" or t=="6:00" or t=="9:00" ):
			time= "0" + t + ":00" 
		elif( t=="12:00" or t=="15:00" or t=="18:00" or t=="21:00"):
			time = t + ":00"	
		else:
			time=t
		import datetime
		dt_=datetime.date.today() + datetime.timedelta(days=n)
		dt_=str(dt_)
		dt_time= dt_ + " " + time
		index=json.find(dt_time)
		index=json.rfind('\"sea_level\"',0,index)
		ind2=json.find(",",index+11)
		sea_level=json[index+12:ind2]
		sea_level=float(sea_level)	
		return(sea_level)
	else :
		return("")


		