#Ändern bzw. erweitern Sie das Wörterbuch-Beispiel aus der LÜ vom 03.05.2021 so, dass Sie wahlweise englische oder deutsche Begriffe
#eingeben können und das Programm selbständig das jeweils korrespondierende Vokabel findet und, versehen mit einem Hinweis auf die Sprache,ausgibt.

#Bsp.:

#Eingabe: Apfel -> apple (EN)
#Eingabe: peach -> Pfirsich (DE)


woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

max = len(woerterbuch_deutsch)   #Ermittlung der Anzahl der Index im Wörterbuch

eingabe = input("Geben Sie den Begriff auf Deutsch oder Englisch ein und es wird automatisch übersetzt: ") 
index = 0   #Startwert für die Schleife

while index < max:   #Wenn der Startwert der Schleife kleiner ist als die Anzahl der Index im Wörterbuch...                                             
    if woerterbuch_deutsch[index].lower() == eingabe.lower():   #... wird das Wort mit dem dazugehörigen Index im deutschen Wörterbuch mit dem eigegebenen Wort verglichen...   
        print(woerterbuch_englisch[index] + "[EN]")   #...stimmen die beiden Wörter überein, wird das Englische Wort ausgegeben...                      
        break   #...und die Schleife wird abgebrochen
    index +=1
    
if index == max:   #wird jedoch kein Wort gefunden, und der Index ist gleich wie die Anzahl der Index im Wörterbuch...
    index = 0   #...wird der Index wieder 0 gesetzt und das Englische Wörterbuch wird überprüft. 
    while index < max:
        if woerterbuch_englisch[index].lower() == eingabe.lower():   
            print(woerterbuch_deutsch[index] + "[DE]")
            break
        index +=1
        
if index == max:    #wird jetzt wieder kein Wort gefunden, dann wird "nicht vorhanden" ausgegeben. 
    print("nicht vorhanden")
    