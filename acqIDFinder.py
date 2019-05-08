from lxml import objectify
import sys
from glob import glob

#obj = objectify.fromstring(open(sys.argv[1]).read())
obj = objectify.fromstring(open(sys.argv[1]).read())


passid = obj.downloading.passID
Lista = []

if len(obj.rasReport.descendantpaths()) == 1:
    print str(passid) + ",EMPTY"
elif len(obj.rasReport.descendantpaths()) > 1:
        for i in obj.rasReport.vc:
            for j in i.rasSummary.ras:
                if len(Lista) == 0:
                    Lista.append(j.acqID)
                elif j.acqID not in Lista:
                    Lista.append(j.acqID)

nomArch = "acqIDList " + str(passid)
acqIDList = open(nomArch, 'w')
for i in Lista:
    acqIDList.write(str(i) + '\n')

acqIDList.close()
print "Lista: ", Lista
