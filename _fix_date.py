import re
print "***********Using fix date function**********"

'''
Different test cases
To check machine learning change first date in date_in string
To check for error proof make changes in any of the dates in string or in console input
Note: if once hint format is NOT None then it will format all the next dates in the same format example in 1994/12/3 is returned as 3-1994-12 since the previous string 13/1/1998 sets hint as MM-DD-YYYY
'''

date_in ='''1:1:2014
2/16/1995
13/1/1998
20/7/19950
1994/12/3
12:2:1997
34-2-2014
ab:12:1995
'''

# ********************* implemention based on recommended changes ****************************
'''
This helper function converts random date into  standard format YYYY-MM-DD

'''
def _fix_date_day(hint,d0,d1,d2):
	format_date = ''
	if hint =='YYYY-?-?':
		year = d0				  #assigning first string as year
		if int(d1)>12 and int(d1)<31:		  # check if second string is a day
			day = d1
			month = d2
			format_date = year +'-'+ month +'-'+ day
			format_hint = 'YYYY-DD-MM'
		elif int(d2)>12 and int(d2)<31: 	  # check if third string is a day
			day = d2
			month = d1
			format_date = year +'-'+ month +'-'+ day
			format_hint = 'YYYY-MM-DD'
		else:					# default assume it in  YYYY-MM--DD for d1<12 and and d2<12
			day = d2
			month = d1
			format_date = year +'-'+ month +'-'+ day
			format_hint = None
	elif hint =='?-?-YYYY':
		year = d2				#assing last sting as year
		if int(d0)>12 and int(d0)<31:           #assisning first string as day
			day = d0
			month = d1
			format_date = year +'-'+ month +'-'+ day
			format_hint = 'DD-MM-YYYY'
		elif int(d1)>12 and int(d1)<31:
                        day = d1
                        month = d0
                        format_date = year +'-'+ month +'-'+ day
			format_hint = 'MM-DD-YYYY'
		else:  					 # default assume it in  DD-MM-YYYY for d1<12 and and d2<12
                        day = d0
                        month = d1
                        format_date = year +'-'+ month +'-'+ day
			format_hint = None

	else:
		print "No such hint exit  exit"
	
	return format_date,format_hint
'''
This function checks whether given date is valid or not
This function converts random date in format date

'''

def _fix_date(date_in_random_format,format_hint):
	format_date = ''
	regx = re.compile('[-/:]')
	d0,d1,d2 = regx.split(date_in_random_format)
	if not (d0.isdigit() and d1.isdigit() and d2.isdigit()): # check if all are in digit only
		print "Error date time must be in digit"
		return None,None
	if not (len(d0)==4 or len(d1)==4 or len(d2)==4): # check if year exist
		print "Error year not given"
		return None,None	
	if ((int(d0)>31 and int(d1)>31) or (int(d1)>31 and int(d2)>31) or (int(d0)>31 and int(d2)>31)): 
		print "Error wrong date and month"
		return None,None
	if len(date_in_random_format)<=10: # to check if in date format
		counter=0
		for st in date_in_random_format:
			if st == '-':
				counter+=1
			elif st == '/':
				counter+=1
			elif st == ':':
				counter+=1
		if counter!=2:
			print "Error  date should have two - or / or :"
	
		if format_hint =='DD-MM-YYYY':		# check if hint given from last string
			day = d0
			month = d1
			year = d2
			format_date = year +'-'+ month +'-' + day
		elif format_hint == 'MM-DD-YYYY':
			day = d1
			month = d0
			year =d2
			format_date = year +'-'+ month +'-' + day
		
		elif format_hint == 'YYYY-MM-DD':
			day = d2
			month = d1
			year =d0
			format_date = year +'-'+ month +'-' + day

		elif format_hint == None:
			if len(d0)==4:		# identifying the format 'YYYY-MM-DD'
				hint = 'YYYY-?-?'
				format_date,format_hint = _fix_date_day(hint,d0,d1,d2)
					
			elif len(d2)==4:	# format is ?-?-YYYY
				hint = '?-?-YYYY'
				format_date,format_hint = _fix_date_day(hint,d0,d1,d2)
				
	else: 	
		print "Length of string should be less than equal to ten"
	
	return format_date,format_hint 

format_hint = None
'''
To choose for any type of input from string or console
'''

select = raw_input("Select choice enter \n 'y' for string \n 'n' for raw input: ")
if select.lower()=='y':
	for date_in_random_format in date_in.splitlines():
		print "Input date %s:" % date_in_random_format
                (date_in_fixed_format,latest_hint) = _fix_date(date_in_random_format,format_hint)
                if latest_hint:
                        format_hint = latest_hint
                print "Formated date %s:" % date_in_fixed_format

else:
	# for a given imput one at time in console
	console_input = raw_input("Enter date in appropriate format: ")
	for date_in_random_format in console_input.splitlines():
		print "Input date %s:" % date_in_random_format
		(date_in_fixed_format,latest_hint) = _fix_date(date_in_random_format,format_hint)
		if latest_hint:
			format_hint = latest_hint
		print "Formated date %s:" % date_in_fixed_format

		

