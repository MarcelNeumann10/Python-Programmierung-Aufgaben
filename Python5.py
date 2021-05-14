# Dictionaries

#Ändern Sie das Wörterbuch-Beispiel so, dass Sie anstelle der Listen Dictionaries verwenden.
#Mittels try/except soll die Abfrage nach nicht-existenten Begriffen fehlerfrei gestaltet werden,
#bzw. die wahlweise Eingabe von deutschen od. englischen Begriffen möglich sein.
#Ein Ergänzung bzw. das Löschen von Begriffen ist nicht gefordert.

woerterbuchDeutsch = {"Apfel": "apple", "Birne": "pear" , "Kirsche": "cherry", "Melone": "melon", "Marille": "apricot", "Pfirsich": "peach"}
woerterbuchEnglisch = {"apple": "Apfel", "pear": "Birne", "cherry": "Kirsche", "melon": "Melone", "apricot": "Marille", "peach": "Pfirsich"}
try:                                        #Hier wird zuerst die 1. Sektion probiert
    begriff = input("Begriff: ")
    print(woerterbuchDeutsch[begriff])      #wenn der Begriff richtig ist, wird das englische Wort aus dem Wörterbuch ausgegeben.
except:                                     #falls Begriff nicht richtig, wird der Fehler angenommen und das nächste Wörterbuch wird überprüft.
    try: 
        print(woerterbuchEnglisch[begriff]) #wenn der Begriff richtig ist, wird das deutsche Wort aus dem Wörterbuch ausgegeben.
    except:
        print("Wort existiert nicht")       #wird der Begriff trotzdem nicht gefunden, wird "Wort existiert nicht" ausgegeben.
    
    

while True:                                 #Eingabe bis Zahl eingegeben wurde
    try:
        stringA = input("Zahl: ")
        intb= int(stringA)                  #Umwanldung String to Int => nur ValueError möglich
        break
    except ValueError:
        print("ist keine Zahl")             #Wird keine Zahl eingegeben, wird "ist keine Zahl" ausgeben. 
print("ausgebrochen")