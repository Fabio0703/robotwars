# Intro

a = '''
██╗    ██╗██╗██╗     ██╗     ██╗  ██╗ ██████╗ ███╗   ███╗███╗   ███╗███████╗███╗   ██╗    ███████╗██╗   ██╗
██║    ██║██║██║     ██║     ██║ ██╔╝██╔═══██╗████╗ ████║████╗ ████║██╔════╝████╗  ██║    ╚══███╔╝██║   ██║
██║ █╗ ██║██║██║     ██║     █████╔╝ ██║   ██║██╔████╔██║██╔████╔██║█████╗  ██╔██╗ ██║      ███╔╝ ██║   ██║
██║███╗██║██║██║     ██║     ██╔═██╗ ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║     ███╔╝  ██║   ██║
╚███╔███╔╝██║███████╗███████╗██║  ██╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║ ╚████║    ███████╗╚██████╔╝
 ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝ 
                                                                                                           
    ██████╗  ██████╗ ██████╗  ██████╗ ████████╗    ██╗    ██╗ █████╗ ██████╗ ███████╗██╗                   
    ██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝    ██║    ██║██╔══██╗██╔══██╗██╔════╝██║                   
    ██████╔╝██║   ██║██████╔╝██║   ██║   ██║       ██║ █╗ ██║███████║██████╔╝███████╗██║                   
    ██╔══██╗██║   ██║██╔══██╗██║   ██║   ██║       ██║███╗██║██╔══██║██╔══██╗╚════██║╚═╝                   
    ██║  ██║╚██████╔╝██████╔╝╚██████╔╝   ██║       ╚███╔███╔╝██║  ██║██║  ██║███████║██╗                   
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝        ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝                            

'''

print (a)

import random

# Roboter initialisieren
def erstelle_roboter(spieler_nummer, verwendete_symbole):
    name = input(f"Spieler {spieler_nummer}, gib deinem Roboter einen Namen: ")
    symbol = waehle_symbol(spieler_nummer, verwendete_symbole)

    # Anfangswerte
    roboter = {
        "name": name,
        "symbol": symbol,
        "health": 1,
        "energy": 1,
        "shield": 1,
        "attack_damage": 1,
        "attack_range": 1,
        "damage_zone": 1,
        "accuracy": 1,
        "movement_range": 1,  # Beispielwert für Bewegungspunkte
        "x": 0,  # Startposition x
        "y": 0,  # Startposition y
        "ausrichtung": "oben",  # Anfangsausrichtung
        "items": []  # Gesammelte Items
    }

    # Skillpunkte verteilen
    skillpoints = 10
    while skillpoints > 0:
        print("\nAktuelle Werte:")
        for key, value in roboter.items():
            if key not in ["name", "symbol", "x", "y", "ausrichtung", "items"]:
                print(f"{key}: {value}")

        attribut = input("Welches Attribut möchtest du verbessern? (health, energy, shield, attack_damage, attack_range, damage_zone, accuracy, movement_range): ")
        punkte = int(input(f"Wieviele Punkte (max. 10) möchtest du auf {attribut} verteilen? "))

        if attribut in roboter and attribut not in ["name", "symbol", "x", "y", "ausrichtung", "items"] and punkte <= skillpoints:
            roboter[attribut] += punkte
            skillpoints -= punkte
            print(f"{attribut} wurde um {punkte} erhöht.")
        else:
            print("Ungültige Eingabe oder nicht genügend Skillpunkte.")

        # Übersicht nach der Änderung anzeigen
        print("\nÜbersicht nach der Änderung:")
        for key, value in roboter.items():
            if key not in ["name", "symbol", "x", "y", "ausrichtung", "items"]:
                print(f"{key}: {value}")

    print("Alle Skillpunkte wurden verteilt.")
    return roboter  # Roboter-Dictionary zurückgeben

def waehle_symbol(spieler_nummer, verwendete_symbole):
    if spieler_nummer == 1:
        symbole = ["⚙", "⚒", "⚡", "⚠", "⚛"]  # Zahnräder, Hammer, Blitz, Warnung, Atom
    else:
        symbole = ["☠", "☢", "♨", "⚔", "⛮"]  # Totenkopf, Radioaktiv, Heiße Quelle, Gekreuzte Schwerter, Rakete

    print(f"Spieler {spieler_nummer}, wähle ein Symbol für deinen Roboter:")
    for i, symbol in enumerate(symbole):
        if symbol not in verwendete_symbole:
            print(f"{i + 1}: {symbol}")

    auswahl = int(input("Gib die Nummer des gewünschten Symbols ein: "))
    if 1 <= auswahl <= len(symbole) and symbole[auswahl - 1] not in verwendete_symbole:
        return symbole[auswahl - 1]
    else:
        print("Ungültige Auswahl oder Symbol bereits verwendet. Bitte versuche es erneut.")
        return waehle_symbol(spieler_nummer, verwendete_symbole)

# Roboter für beide Spieler erstellen
verwendete_symbole = []
roboter1 = erstelle_roboter(1, verwendete_symbole)
verwendete_symbole.append(roboter1["symbol"])
roboter1["x"], roboter1["y"] = 0, 0  # Startposition für Spieler 1

roboter2 = erstelle_roboter(2, verwendete_symbole)
verwendete_symbole.append(roboter2["symbol"])
roboter2["x"], roboter2["y"] = 14, 9  # Startposition für Spieler 2

# Bestimmen, wer anfängt
if roboter1["movement_range"] > roboter2["movement_range"]:
    spieler = 1
elif roboter2["movement_range"] > roboter1["movement_range"]:
    spieler = 2
else:
    spieler = random.choice([1, 2])

print(f"Spieler {spieler} fängt an.")

# Spielfeldgröße
WIDTH = 15
HEIGHT = 10

# Spielfeld initialisieren
def initialisiere_spielfeld():
    return [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]

# Spielfeld anzeigen
def zeige_spielfeld(spielfeld):
    for reihe in spielfeld:
        print(" ".join(reihe))
    print()

# Roboter auf dem Spielfeld platzieren
def platziere_roboter(spielfeld, roboter):
    spielfeld[roboter["y"]][roboter["x"]] = roboter["symbol"]

# Items und Hindernisse initialisieren
def erstelle_item(x, y, typ):
    return {"x": x, "y": y, "typ": typ, "dauer": random.randint(1, 2)}

items = [erstelle_item(5, 5, "positiv"), erstelle_item(10, 3, "negativ")]

def erstelle_hindernis(x, y):
    return {"x": x, "y": y}

hindernisse = [erstelle_hindernis(7, 7), erstelle_hindernis(8, 8)]

# Items auf dem Spielfeld platzieren
def platziere_items(spielfeld, items):
    for item in items:
        spielfeld[item["y"]][item["x"]] = "I"

# Hindernisse auf dem Spielfeld platzieren
def platziere_hindernisse(spielfeld, hindernisse):
    for hindernis in hindernisse:
        spielfeld[hindernis["y"]][hindernis["x"]] = "H"

# Roboter bewegen
def bewegen(roboter, richtung, schritte, hindernisse):
    for _ in range(schritte):
        neuer_x, neuer_y = roboter["x"], roboter["y"]
        if richtung == "oben" and roboter["y"] > 0:
            neuer_y -= 1
        elif richtung == "unten" and roboter["y"] < HEIGHT - 1:
            neuer_y += 1
        elif richtung == "links" and roboter["x"] > 0:
            neuer_x -= 1
        elif richtung == "rechts" and roboter["x"] < WIDTH - 1:
            neuer_x += 1

        if not any(h["x"] == neuer_x and h["y"] == neuer_y for h in hindernisse):
            roboter["x"], roboter["y"] = neuer_x, neuer_y

# Überprüfen, ob das Ziel in Reichweite ist
def ist_in_reichweite(angreifer, ziel):
    entfernung = abs(angreifer["x"] - ziel["x"]) + abs(angreifer["y"] - ziel["y"])
    return entfernung <= angreifer["attack_range"]

# Überprüfen, ob der Roboter zum Ziel ausgerichtet ist
def ist_ausgerichtet(angreifer, ziel):
    if angreifer["ausrichtung"] == "oben" and angreifer["y"] > ziel["y"]:
        return True
    if angreifer["ausrichtung"] == "unten" and angreifer["y"] < ziel["y"]:
        return True
    if angreifer["ausrichtung"] == "links" and angreifer["x"] > ziel["x"]:
        return True
    if angreifer["ausrichtung"] == "rechts" and angreifer["x"] < ziel["x"]:
        return True
    return False

# Angriffsfunktion
def angreifen(angreifer, ziel, hindernisse):
    if ist_in_reichweite(angreifer, ziel) and ist_ausgerichtet(angreifer, ziel):
        if not any(h["x"] == ziel["x"] and h["y"] == ziel["y"] for h in hindernisse):
            if random.random() < angreifer["accuracy"]:
                print(f"{angreifer['name']} trifft {ziel['name']} und verursacht {angreifer['attack_damage']} Schaden!")
                ziel["health"] -= max(0, angreifer["attack_damage"] - ziel["shield"])
                return angreifer["attack_damage"]
            else:
                print(f"{angreifer['name']} verfehlt {ziel['name']}.")
                return 0
        else:
            print(f"Ein Hindernis blockiert den Angriff auf {ziel['name']}.")
            return 0
    else:
        print(f"{ziel['name']} ist außerhalb der Reichweite oder nicht ausgerichtet.")
        return 0

# Item-Effekt anwenden
def wende_item_an(roboter, item):
    eigenschaften = ["attack_damage", "attack_range", "movement_range"]
    eigenschaft = random.choice(eigenschaften)
    effekt = 1 if item["typ"] == "positiv" else -1
    roboter[eigenschaft] += effekt
    roboter["items"].append({"eigenschaft": eigenschaft, "effekt": effekt, "dauer": item["dauer"]})
    print(f"{roboter['name']} hat ein {'positives' if effekt == 1 else 'negatives'} Item gesammelt: {eigenschaft} {'+' if effekt == 1 else ''}{effekt} für {item['dauer']} Runden.")

# Item-Effekte aktualisieren
def aktualisiere_item_effekte(roboter):
    for item in roboter["items"]:
        item["dauer"] -= 1
        if item["dauer"] <= 0:
            roboter[item["eigenschaft"]] -= item["effekt"]
            print(f"{roboter['name']} verliert den Effekt: {item['eigenschaft']} {'+' if item['effekt'] == 1 else ''}{item['effekt']}")
    roboter["items"] = [item for item in roboter["items"] if item["dauer"] > 0]

# Spielschleife
roboter1["x"], roboter1["y"] = 0, 0
roboter2["x"], roboter2["y"] = WIDTH - 1, HEIGHT - 1

# Bestimmen, wer anfängt
if roboter1["movement_range"] > roboter2["movement_range"]:
    spieler = 1
elif roboter2["movement_range"] > roboter1["movement_range"]:
    spieler = 2
else:
    spieler = random.choice([1, 2])

print(f"Spieler {spieler} fängt an.")

while roboter1["health"] > 0 and roboter2["health"] > 0:
    spielfeld = initialisiere_spielfeld()
    platziere_roboter(spielfeld, roboter1)
    platziere_roboter(spielfeld, roboter2)
    platziere_items(spielfeld, items)
    platziere_hindernisse(spielfeld, hindernisse)
    zeige_spielfeld(spielfeld)

    # Sicherstellen, dass der richtige Spieler dran ist
    aktueller_roboter = roboter1 if spieler == 1 else roboter2
    print(f"Spieler {spieler} ist dran. {aktueller_roboter['name']} ist auf Position ({aktueller_roboter['x']}, {aktueller_roboter['y']}).")

    aktion = input("Bewegen (b), Angreifen (a) oder Ausrichten (r)? ")
    if aktion == "b":
        richtung = input("Richtung (oben, unten, links, rechts): ")
        schritte = int(input(f"Wieviele Schritte (1-{aktueller_roboter['movement_range']})? "))
        if 1 <= schritte <= aktueller_roboter["movement_range"]:
            bewegen(aktueller_roboter, richtung, schritte, hindernisse)
        else:
            print(f"Ungültige Anzahl von Schritten. Bitte wähle eine Zahl zwischen 1 und {aktueller_roboter['movement_range']}.")
    elif aktion == "a":
        ziel = roboter2 if spieler == 1 else roboter1
        angreifen(aktueller_roboter, ziel, hindernisse)
    elif aktion == "r":
        neue_ausrichtung = input("Neue Ausrichtung (oben, unten, links, rechts): ")
        aktueller_roboter["ausrichtung"] = neue_ausrichtung
    else:
        print("Ungültige Aktion.")

    # Item-Effekte aktualisieren
    aktualisiere_item_effekte(aktueller_roboter)

    # Spieler wechseln
    spieler = 2 if spieler == 1 else 1
    aktueller_roboter = roboter1 if spieler == 1 else roboter2

    # Spielfeld aktualisieren und anzeigen
    spielfeld = initialisiere_spielfeld()
    platziere_roboter(spielfeld, roboter1)
    platziere_roboter(spielfeld, roboter2)
    platziere_items(spielfeld, items)
    platziere_hindernisse(spielfeld, hindernisse)
    zeige_spielfeld(spielfeld)

    print(f"Spieler {spieler} ist dran. {aktueller_roboter['name']} ist auf Position ({aktueller_roboter['x']}, {aktueller_roboter['y']}).")

print("Spiel beendet!")