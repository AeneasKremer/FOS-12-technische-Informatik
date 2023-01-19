programm = True

while programm == True:
    print(25 * "-")
    print("Menü")
    print("(E)inlesen")
    print("(B)eenden")
    eingabe = input()
    print(25 * "-")
    
    if eingabe == "E" or eingabe == "e":
        print("Geben Sie eine Dateipfad ein:")
        deingabe = input()
        data = open(deingabe,"r")
        text = data.read()
        a = 0
        e = 0
        i = 0
        o = 0
        u = 0
        ae = 0
        oe = 0
        ue = 0
        leer = 0
        for p in range(0,len(text),1):
            if text[p] == "A" or text[p] == "a":
                a += 1
            elif text[p] == "E" or text[p] == "e":
                e += 1
            elif text[p] == "I" or text[p] == "i":
                i += 1
            elif text[p] == "O" or text[p] == "o":
                o += 1
            elif text[p] == "U" or text[p] == "u":
                u += 1
            elif text[p] == "Ä" or text[p] == "ä":
                ae += 1
            elif text[p] == "Ö" or text[p] == "ö":
                oe += 1
            elif text[p] == "Ü" or text[p] == "ü":
                ue += 1
            elif text[p] == " " or text[p] == "." or text[p] == "!" or text[p] == "?":
                leer += 1
            
        gesamt = len(text)-leer
        prozenta = round(float(a/gesamt*100),0)
        prozente = round(float(e/gesamt*100),0)
        prozenti = round(float(i/gesamt*100),0)
        prozento = round(float(o/gesamt*100),0)
        prozentu = round(float(u/gesamt*100),0)
        prozentae = round(float(ae/gesamt*100),0)
        prozentoe = round(float(oe/gesamt*100),0)
        prozentue = round(float(ue/gesamt*100),0)
            
        print("Gesamt:", gesamt)
        print("%-5s %-5s %-5s %-5s %-5s %-5s %-5s %-5s" % ("A", "E", "I", "O", "U", "Ä", "Ö", "Ü"))
        print("%-2d %-2s %-2d %-2s %-2d %-2s %-2d %-2s %-2d %-2s %-2d %-2s %-2d %-2s %-2d %-2s" % (prozenta, "%", prozente, "%", prozenti, "%", prozento, "%", prozentu, "%", prozentae, "%", prozentoe, "%", prozentue, "%"))

    elif eingabe == "B" or eingabe == "b":
        programm = False