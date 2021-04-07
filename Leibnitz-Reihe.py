#Erstellen Sie ein Python-Programm, das unter Verwendung der Leibniz-Reihe den Wert der Zahl Pi näherungsweise berechnet.
#Dabei soll es für den/die BenutzerIn möglich sein, die Anzahl der Iterationen bei Programmbeginn einzugeben.
#Am Ende des Programmlaufs soll der Näherungswert für Pi ausgegeben werden,
#optional können auch die Zwischenwerte und Iterationsstufen zur Ausgabe gelangen.


obererTerm = 1
pi_4 = 0
zahl1 = input("Geben Sie die Anzahl der Iterationen ein")
zahl1 = int (zahl1)
for k in range(0,zahl1) :
    pi_4 += obererTerm / (2*k+1)
    obererTerm = obererTerm * (-1)
print(pi_4*4)
