from datetime import datetime

now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
orario = now.strftime("%H:%M:%S")
print("date and time =", orario)

fascia1 = "00:00:00"
fascia2 = "06:00:00"
fascia3 = "08:00:00"
fascia4 = "13:00:00"
fascia5 = "16:00:00"
fascia6 =  "23:00:00"

#verifica fascia 1

if (orario >= fascia1 and orario < fascia2 ):
	print ("fascia1")
if (orario >= fascia2 and orario < fascia3 ):
	print ("fascia2")
if (orario >= fascia3 and orario < fascia4 ):
	print ("fascia3")
if (orario >= fascia4 and orario < fascia5 ):
	print ("fascia4")
if (orario >= fascia5 and orario < fascia6 ):
	print ("fascia5")
if (orario >= fascia6 and orario < fascia1 ):
	print ("fascia6")




 
