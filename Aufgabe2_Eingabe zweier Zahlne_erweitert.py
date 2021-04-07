#Aufgabe 2:
#Schreiben Sie ein Python-Programm, das
#1) den Benutzer gerüßt
#2) eine erste Zahl entgegen nimmt
#3) eine zweite Zahl entgegen nimmt
#4) die Summe der beiden Zahlen berechnet und ausgibt
#5) die Differenz der kleineren von der größeren Zahl berechnen
#6) das Produkt der beiden Zahlen berechnet und ausgibt
#7) den Qutient kleiner Zahl durch größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)

#1
print("Hallo Benutzer")

#2
zahl1 = input("Eingabe der ersten Zahl")
zahl1 = float (zahl1)   #float für Kommazahlen, int für ganze Zahlen

#3
zahl2 = input("Eingabe der zweiten Zahl")
zahl2 = float (zahl2)

#4
print("Die Summe lautet:" , zahl1+zahl2) 

#5
if zahl1 <= zahl2 :
    print("Die Differenz ist:" , zahl1 - zahl2)
elif zahl1 >= zahl2 :
    print("Die Differenz ist:" , zahl2 - zahl1)

#6
print("Das Produkt lautet:" , zahl1*zahl2)    

#7
if zahl1 <= zahl2 :
    print("Der Quotient ist:" , zahl1 / zahl2)
elif zahl1 >= zahl2 :
    print("Der Quotient ist:" , zahl2 / zahl1)
