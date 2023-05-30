import pywhatkit

tel = str(input("Phone"))
msg = str(input("Enter messege"))
hours = int(input("enter hours"))
minutes = int(input("enter minutes"))

pywhatkit.sendwhatmsg("+1" + tel , msg , hours , minutes, 4 , True, 4 )

