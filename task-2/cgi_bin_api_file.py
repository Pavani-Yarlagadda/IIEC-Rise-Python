
import cgi
import subprocess
print("content-type: text/html")
print()
mydata = cgi.FieldStorage()
myx=mydata.getvalue("command")
name=mydata.getvalue("pavani")
passw=mydata.getvalue("pavs")
if(name=='<Enter a valid username>' and passw=='<Enter a valid password>'):
  output=subprocess.getstatusoutput('sudo'+' '+myx)
  status=output[0]
  out=output[1]
  print(status)
  print(out)
else:
  print("Not the correct user")
