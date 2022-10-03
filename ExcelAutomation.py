
import openpyxl
import pandas as pd
import os 

os.chdir('/Users/wilhigh/Downloads/RPA를 이용한 업무자동화/UiPath')
wb = openpyxl.load_workbook('popbygender.xlsx')
sheet = wb['데이터']

popData = {} 
region = []
male = []
female = []
pop = [] 

for row in range(2,sheet.max_row):
    region.append(sheet['A'+str(row)].value)
    male.append(sheet['B'+str(row)].value)
    female.append(sheet['C'+str(row)].value)
    pop.append(sheet['B'+str(row)].value + sheet['C'+str(row)].value)

popData['region'] = region 
popData['male'] = male 
popData['female'] = female 
popData['pop'] = pop 

df = pd.DataFrame(popData)
df.to_excel('pop2020.xlsx')