from tabulate import tabulate

def minumr(minu):
    split = minu.split(":")
    #sekunden = int(int(split[1])+int(split[0]*60))
    sekunden = int(split[1])
    minsek = int(split[0])*60
    alles = sekunden+minsek
    return alles
    
    
    
    
def einlesen(text):
    data = open(text, "r")
    lines = data.readlines()
    
    datum = []
    name = []
    platzierung = []
    zeit = []
    
    for i in range(1,len(lines)):
        lines[i] = lines[i].replace("\n", "")
        split = lines[i].split(";")
        
        datum.append(split[0])
        name.append(split[1])
        platzierung.append(split[2])
        zeit.append(split[3])
    
    print("%-10s %-15s %-10s %-10s" % ("Datum", "Name", "Platzierung", "Zeit"))
    for i in range(1,len(lines)-1):
        print("%-10s %-15s %-10s %-10s" % (datum[i], name[i], platzierung[i], zeit[i]))
        
    return datum, name, platzierung, zeit
        
def prognose(pferde, datum, name, platzierung, zeit):
    realname = []
    rplatz = 0
    time = 0
    counter = 0
    for i in range(0, len(name)):
        for u in range(len(pferde)):
            if name[i] in pferde[u]:
                counter += 1
                pferde[u].append(platzierung[i])
                pferde[u].append(zeit[i])
    tabelle = []
    for obj in pferde:
        tabelle.append([obj[0]])
    for i in range(len(pferde)):
        for u in range(1,len(pferde[i])):
            if u % 2 != 0:
                rplatz += int(pferde[i][u])
            else:
                time += minumr(pferde[i][u])
        print(rplatz)
        tabelle[i].append(rplatz)
        tabelle[i].append(time)
    for i in range(len(tabelle)):
        print(25* "-")
        print("Name des Pferdes:", tabelle[i][0])
        print("Durchschnittliche Platzierung:", round((tabelle[i][1]/counter),2))
        print("Durchschnittliche Renndauer:", round((tabelle[i][2]/counter),2))
            
            
        
            
            
        

datum, name, platzierung, zeit = einlesen("data.csv")

while True:
    print()
    print("Menu")
    print("1) Pferd auswählen")
    print("2) Prognose")
    print()
    
    eingabe = input("Ihre Eingabe:")
    if eingabe == "1":
        onlyname = []
        for i in range(0,len(name)):
            if name[i] not in onlyname:
                onlyname.append(name[i])
        auswahl = []
        while True:
            i = 0
            for obj in onlyname:
                i+=1
                print(i, "-", obj)
            
            
            try:
                eingabe = int(input("Ihre Auswahl: (0 für ende der Auswahl)"))
                
                if eingabe == 0:
                    break
                else:
                    if ([onlyname[eingabe-1]]) in auswahl:
                        print("Bitte kein Pferd zweimal eingeben")
                    elif ([onlyname[eingabe-1]]) not in auswahl:
                        auswahl.append([onlyname[eingabe-1]])
                        print(onlyname[eingabe-1])
                        print(auswahl)
            except:
                print(25*"!")
                print("Falsche Eingabe!")
                print(25*"!")
                
            
            
            
                
    elif eingabe == "2":
        try:
            prognose(auswahl, datum, name, platzierung, zeit)
        except:
            print("Sie müssen vorher eine Auswahl treffen!")    