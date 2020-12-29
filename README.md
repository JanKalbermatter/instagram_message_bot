# instagram_message_bot

## Anwendung 
Die beiden Python Skripts sind dafür verantwortlich eine Liste mit Benutzernamen zu generieren und diese in einer JSON Datei zu speichern.
Die beiden TypeScript Skripts lesen diese Daten anschliessend aus und senden jedem dieser Benutzer eine Nachricht.

Python Version 3.5 oder höher muss installiert sein. 
pip muss installiert sein. 
Aktualle Node und npm version muss installiert sein.

Kontrollieren mit: 
```console
pip --version 
python --version
node --version
npm --version
```

Folgende Befehle ausführen bevor dem starten (im Ordner "instagram_message_bot"): 
```console
npm install
pip install instaloader
```

### Config
Die Datei config.json muss wie folgt aufgebaut sein. Die Werte müssen vor dem Benutzen angepasst werden
MessageDelay = Wartezeit zwischen dem senden von Nachrichten. Damit kann limitiert werden wie viele Nachrichten pro Zeit gesendet werden. Zeitangabe in ms.

```json
{
    "InstaUser": "Benutzername Instagram",
    "InstaPassword": "Password Instagram",
    "MessageHashtag": "Nachricht, welche bei Hashtag gesendet wird",
    "MessageUsername": "Nachricht, welche bei Username gesendet wird",
    "MessageDelay": 0
}
```

### Hashtag
```console
python hashtag.py <Hashtag> <Anzahl Posts>
```

Hashtag ohne # schreiben, nur Text
Default Wert für Anzahl Posts ist 10

Alle gefundenen Benutzer erhalten die gleichen Nachricht zugesendet

### Username
```console
python user.py <username> <Anzahl follower>
```

Anzahl Follower schränkt ein, wie viele Follower angeschaut werden. Default Wert ist 100

Alle gefundenen Benutzer erhalten die gleichen Nachricht zugesendet

### Custom
Es besteht auch die möglichkeit eine eigene Liste mit Benutzernamen anzugeben. Dazu einfach ein Array in korrektem JSON Format in die Datei "users.json" speichern und einen der beiden folgenden Befehlen in der Console ausführen: 
```console
node messageUsersByHashtag.ts
node messageUsersByName.ts
```
messageUsersByHashtag.ts benutzt die Nachricht aus MessageHashtag in der Config
messageUsersByName.ts benutzt die Nachricht aus MessageUsername in der Config

## Other
Weiss nicht wie viele User ich maximal pro Stunden finden kann, müsste man noch genauer ausprobieren.
Ich glaube mit allen Befehlen unter "Anwendung" sollte es funktionieren, bin mir aber nicht 100% sicher (Habe keinen anderen PC zum testen)

Die Datei "messagedUsers.json" muss existieren, kann aber leer sein (Datei sollte eigentlich im Repository sein)
In dieser Datei befinden sich die Benutzernamen aller User welche bereits einmal angeschrieben wurden (doppeltes Anschreiben verhindern)

