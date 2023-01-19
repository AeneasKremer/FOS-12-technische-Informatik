answer = True

while answer == True:
    print(25*"-")
    print("Menü")
    print("1) Verkehrszählung einlesen")
    print("2) Verkehrszählung anzeigen")
    print("3) Auswertung für ein bestimmtes Datum")
    print("B)eenden")

    eingabe = input()

    if eingabe == "1":
        answer = True
        print("Bitte geben Sie den Dateinamen ein:")
        deingabe = input()
        try:
            data = open(deingabe, "r")
            text = data.read()
            ntext = text.replace(":", "/")
            nntext = ntext.replace(" ", "_")
            textzeile = nntext.split()
            datum = []
            lkw = []
            pkw = []
            ort = []
            for i in range(0,len(textzeile),1):
                zeile = textzeile[i]
                zeiletext = zeile.split("/")
                datumapp = zeiletext[0]
                datum.append(datumapp)
                lkwapp = zeiletext[1]
                lkw.append(lkwapp)
                pkwapp = zeiletext[2]
                pkw.append(pkwapp)
                ortapp = zeiletext[3]
                rortapp = ortapp.replace("_","").replace(";","")
                ort.append(rortapp)
        except:
            print("Datei konnte nicht gefunden werden")
            continue
    elif eingabe == "2":
        try:
            print("%-15s %-15s %-15s %-15s" % ("Datum:", "LKW:", "PKW:", "Ort:"))
            for i in range(0,len(textzeile),1):
                print("%-15s %-15s %-15s %-15s" % (datum[i], lkw[i], pkw[i], ort[i]))
        except:
            print("Bitte geben Sie zuerst eine lesbare Datei ein.")
            continue
    elif eingabe == "3":
        print("Geben Sie ein Datum ein:")
        eingabed = input()
        datumline = []
        maxpkw = 0
        maxlkw = 0
        maxpkwort = ""
        maxlkwort = ""
        try:
            for i in range(0,len(datum),1):
                if eingabed == datum[i]:
                    datumline.append(i)
            for i in datumline:
                if int(pkw[i]) > maxpkw:
                    maxpkw = int(pkw[i])
                    maxpkwort = ort[i]
                if int(lkw[i]) > maxlkw:
                    maxlkw = int(lkw[i])
                    maxlkwort = ort[i]
            print("Maximale Pkw Anzahl:", maxpkw)
            print("An dem Ort:", maxpkwort)
            print(25*"-")
            print("Maximale LKW Anzahl:", maxlkw)
            print("An dem Ort:", maxlkwort)
        except:
            print("Datum konnte nicht gefunden werden")
            continue

        
    else:
        answer = False
        break