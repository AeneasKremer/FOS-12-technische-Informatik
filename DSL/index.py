import sys

def open_text(text):
    data = open(text)

    lines = data.readlines()


    mainline = []
    for i in range(2,len(lines),3):
        mainline.append(lines[i])

    monat = []
    tag = []
    uhr = []
    kbsent = []
    kbreceived =[]

    for i in range(0, len(mainline), 1):
        leer = mainline[i].split(" ")
        monat.append(leer[0])
        tag.append(int(leer[1]))
        uhr.append(leer[2])
        kbsent.append(float(leer[6]))
        kbreceived.append(float(leer[9]))
    return (monat, tag, uhr, kbsent, kbreceived, mainline)


def ausgabe(mainline):
    print("%5s %8s %5s %15s %15s %15s" % ("Nr.", "Monat", "Tag", "Uhrzeit", "KB gesendet", "KB empfangen"))
    for i in range(0,len(mainline)):
        print("%5d %8s %5d %15s %13.2f %13.2f" % (i+1, monat[i], tag[i], uhr[i], kbsent[i], kbreceived[i]))

def csv(monat, tag, uhr, kbsent, kbreceived):
    import csv
    name = 'example_csv.csv'
    with open(name, 'w') as file:
        for i in range(0,len(mainline)):
            writer = csv.writer(file)
            writer.writerow([i+1, monat[i], tag[i], uhr[i], kbsent[i], kbreceived[i]])
    return name
    
            
def open_export(name):
    import csv
    with open(name, 'r') as csv_datei:
        reader = csv.reader(csv_datei, delimiter=',')
        for zeile in reader:
            print(zeile)
            
def auswertung(kbsent, kbreceived, datum, tag, monat):
    dtemp = datum.split(" ")
    dmonat = dtemp[0]
    dtag = dtemp[1]
    for i in range(0,len(monat)):
        print(tag[i])
        if int(dtag) == int(tag[i]) and str(dmonat) == str(monat[i]):
            mbsentd = float(kbsent[i])/1000
            mbreceivedd = float(kbreceived[i])/1000
    return mbsentd, mbreceivedd

answer = True

while answer == True:
    print(25 * "-")
    print("Menu")
    print("1) DSL-log einlesen")
    print("2) Auswertung")
    print("3) Export")
    print("4) Laden der Export-Datei")
    print("5) Beenden")
    
    aeingabe = input("Eingabe:")
    
    if aeingabe == "1":
        print("Welche Datei wollen Sie einlesen?")
        text = input()
        try:
            monat, tag, uhr, kbsent, kbreceived, mainline = open_text(text)
            print("Datei wurde gelesen")
        except:
            print("Datei konnte nicht gelesen werden")
            continue
    elif aeingabe == "2":
        try:
            print("Welches Datum soll gesucht werden?")
            datum = input()
            mbsentd, mbreceivedd = auswertung(kbsent, kbreceived, datum, tag, monat)
            print(datum, ":", 17 * "-")
            print("Gesendet:", round(mbsentd, 2), "Mbit")
            print("Empfangen:", round(mbreceivedd, 2), "Mbit")
        except:
            ("Datei konnte nicht ausgewertet werden")
            continue
    elif aeingabe == "3":
        try:
            name = csv(monat, tag, uhr, kbsent, kbreceived)
        except:
            print("Datei konnte nicht exportiert werden")
            continue
    elif aeingabe == "4":
        try:
            open_export(name)
        except:
            print("Laden der Export Datei nicht möglich")
            continue
    elif aeingabe == "5":
        answer = False
        break


          