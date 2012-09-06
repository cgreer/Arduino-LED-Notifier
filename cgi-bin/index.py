#!/usr/bin/env python
import cgi


STATUS_RGB = {}

#get current titles
myData = cgi.FieldStorage()
aData = myData['tText']
outData = aData.value

with open('gmail_text.txt', 'a') as f:
    if outData == "\"\"" or outData == "\"Gmail\"":
        pass
    else:
        f.write(outData + "\n")

     

print "Content-type: text/html"
print aData
