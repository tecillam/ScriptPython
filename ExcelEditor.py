import datetime
from datetime import date
import xlwt
from lxml import etree

archivo = raw_input("Nombre del archivo de entrada: ")
#archivo = raw_input("C:\Users\mtecilla\PycharmProjects\excelEditor\")
doc = etree.parse(archivo)

#raiz = doc.getroot()
#print raiz.tag

activPlan = doc.findall("sprDrivenMainActivityList/activity")
#print activPlan[0].find("timeSpec/startTime").text

style0 = xlwt.easyxf('font: name Times New Roman, colour black, bold off')
style1 = xlwt.easyxf('font: name Arial, colour blue, bold on')
# Escribiendo cabeceras
wb = xlwt.Workbook()
ws = wb.add_sheet('pruebas')
ws.write(0, 0, "SprId", style1)
ws.write(0, 1, "Start Time", style1)
ws.write(0, 2, "End Time", style1)
ws.write(0, 3, "ActivityType", style1)
ws.write(0, 4, "SPR Derived Activity Type", style1)
ws.write(0, 5, "Derived Start Time", style1)
ws.write(0, 6, "Derived End Time", style1)

#escribiendo filas
count = 1
for ref in activPlan:
    ws.write(count, 0, activPlan[count-1].find("supportedRequestList/sprId").text, style0)
    ws.write(count, 1, activPlan[count-1].find("timeSpec/startTime").text, style0)
    ws.write(count, 2, activPlan[count-1].find("timeSpec/endTime").text, style0)
    ws.write(count, 3, activPlan[count-1].find("activityType").text, style0)
    ws.write(count, 4, activPlan[count-1].find("sprDrivenDerivedActivityList/derivedActivity/activityType").text, style0)
    ws.write(count, 5, activPlan[count-1].find("sprDrivenDerivedActivityList/derivedActivity/timeSpec/startTime").text, style0)
    ws.write(count, 6, activPlan[count-1].find("sprDrivenDerivedActivityList/derivedActivity/timeSpec/endTime").text, style0)
    count = count + 1

wb.save('ActivityPlan'+ datetime.datetime.today().strftime('%m-%d-%Y %H%M%S') + '.xlsx')


#wb.save('ActivityPlan'+ date.today().strftime('%m-%d-%Y') + '.xlsx')
#wb.save('ActivityPlan.xlsx')


