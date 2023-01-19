from tabulate import tabulate

def verschieben(vart, vort):
    global quad, artikel, A, B, C, D
    
    for i in range(0,len(quad)):
        if quad[i] == vart:
            quad[i] = vort
    
    A = ["A", "", "", "", ""]
    B = ["B", "", "", "", ""]
    C = ["C", "", "", "", ""]
    D = ["D", "", "", "", ""]

    for i in range(0,len(artikel)):
        if quad[i][0] == "A":
            for u in range(1,5):
                if quad[i][1] == str(u):
                    A[u] = artikel[i]
        elif quad[i][0] == "B":
            for u in range(1,5):
                if quad[i][1] == str(u):
                    B[u] = artikel[i]
        elif quad[i][0] == "C":
            for u in range(1,5):
                if quad[i][1] == str(u):
                    C[u] = artikel[i]
        elif quad[i][0] == "D":
            for u in range(1,5):
                if quad[i][1] == str(u):
                    D[u] = artikel[i]
        
    
    

data = open("data.txt", "r")
lines = data.readlines()
data.close()

quad = []
artikel = []

for i in range(0,len(lines)):
    split = lines[i].split(":")
    
    quad.append(split[0])
    artikel.append(split[1])

A = ["A", "", "", "", ""]
B = ["B", "", "", "", ""]
C = ["C", "", "", "", ""]
D = ["D", "", "", "", ""]

for i in range(0,len(artikel)):
    if quad[i][0] == "A":
        for u in range(1,5):
            if quad[i][1] == str(u):
                A[u] = artikel[i]
    elif quad[i][0] == "B":
        for u in range(1,5):
            if quad[i][1] == str(u):
                B[u] = artikel[i]
    elif quad[i][0] == "C":
        for u in range(1,5):
            if quad[i][1] == str(u):
                C[u] = artikel[i]
    elif quad[i][0] == "D":
        for u in range(1,5):
            if quad[i][1] == str(u):
                D[u] = artikel[i]


print(tabulate([A, B, C, D], ["", "1", "2", "3", "4"]))

while True:
    print("Menu")
    print()
    print("1) Ausgabe")

    if input("Ihre Eingabe:") == "1":
        vart = input("Welcher Artikel soll verschoben werden?")
        vort = input("Wohin soll er verschoben werden?")
        
        verschieben(vart,vort)
        print(tabulate([A, B, C, D], ["", "1", "2", "3", "4"]))
        
    else:
        print()
        print("Bitte wählen Sie eine der oben genannten Möglichkeiten aus!")
        
    

    
        
        