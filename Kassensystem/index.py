answer = True

while answer == True:
    print(25*"-")
    print("Menü")
    print("1) Kasse einlesen")
    print("2) Kasse auslesen")
    print("3) Auswertung für ein bestimmtes Datum")
    print("B) eenden")

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
            geld = []
            iban = []
            name = []
            for i in range(0,len(textzeile),1):
                zeile = textzeile[i]
                zeiletext = zeile.split("/")
                datumapp = zeiletext[0]
                datum.append(datumapp)
                geldapp = zeiletext[1]
                geld.append(geldapp)
                ibanapp = zeiletext[2]
                iban.append(ibanapp)
                nameapp = zeiletext[3]
                rnameapp = nameapp.replace("_","").replace(";","")
                name.append(rnameapp)
        except:
            print("Datei konnte nicht gefunden werden")
            continue
    elif eingabe == "2":
        try:
            print("%-15s %-15s %-15s %-15s" % ("Datum:", "Geld:", "IBAN:", "Name:"))
            for i in range(0,len(textzeile),1):
                print("%-15s %-15s %-15s %-15s" % (datum[i], geld[i], iban[i], name[i]))
        except:
            print("Bitte geben Sie zuerst eine lesbare Datei ein.")
            continue
    elif eingabe == "3":
        print("Geben Sie ein Datum ein:")
        eingabed = input()
        datumline = []
        maxgeld = 0
        maxiban = ""
        maxname = ""
        try:
            for i in range(0,len(datum),1):
                if eingabed == datum[i]:
                    datumline.append(i)
            for i in datumline:
                if int(geld[i]) > maxgeld:
                    maxgeld = int(geld[i])
                    maxname = name[i]
                    maxiban = iban[i]
            print(25*"-")
            print("Höchste Einzahlung:", maxgeld)
            print("Name:", maxname)
            print("IBAN:", maxiban)
        except:
            print("Datum konnte nicht gefunden werden")
            continue

        
    elif eingabe == "b" or answer == "B":
        answer = False
        break
    else:
        continue
