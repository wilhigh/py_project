import urllib.request as request
import json
import pandas as pd
from base64 import b64encode
from urllib.parse import urlencode
from urllib.request import urlopen, Request

user, password = 'SQQA', 'SQQA'
data = urlencode(dict(From='+17035551212', To='+17035551212', Body='test')).encode('ascii')
headers = {'Authorization': b'Basic ' + b64encode((user + ':' + password).encode('utf-8'))}

#"http://174.100.29.236:9050/sonarqube/api/issues/search?componentKeys=ssg_SI_CRM-MBS&ps=500&p=1&statuses=OPEN,TO_REVIEW"

api_url = "http://174.100.29.236:9050/sonarqube/api/issues/search?componentKeys=ssg_SI_SI-ERP-LIVE&ps=500&p=1&statuses=OPEN,TO_REVIEW"
api_response = urlopen(Request(api_url, data, headers)).read().decode()

output = json.loads(api_response)
print(output)
print(type(output))
text=json.dumps(output)
print(type(text))
print(text)

for item in output["issues"]:
     print(item["component"])
    #  print(item["type"])
    #  print(item["rule"])
    #  print(item["severity"])
    #  print(item["message"])
    #  print()

df = pd.json_normalize(output["issues"])

#C:/Users/SSG/result_ssg_SI_CRM-CMS_220816.csv

df.to_csv("D:/##개발품질_SonarQube/위반목록전달/위반건json/result_ssg_SI_SI-ERP-LIVE_220817.csv", index=False, encoding="utf-8-sig")
