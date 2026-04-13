import requests
response=requests.get("https://www.thescipub.com/pdf/ajassp.2015.382.402.pdf")
f=open("file2.pdf","wb")
f.write(response.raw.data)
f.close()

