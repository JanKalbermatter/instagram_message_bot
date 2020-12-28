# instagram_message_bot

## Config Date
In der Datei "config.json" alle werte setzen
Die zu versendende Nachricht kann hier auch angepasst werden

## Anwendung 
Python Version 3 oder höher muss installiert sein

### Config
Die Datei config.json muss wie folgt aufgebaut sein. Die Werte müssen vor dem Benutzen angepasst werden
MessageDelay = Wartezeit zwischen dem senden von Nachrichten. Damit kann limitiert werden wie viele Nachrichten pro Zeit gesendet werden. Zeitangabe in ms.

```json
{
    "InstaUser": "Benutzername Instagram",
    "InstaPassword": "Password Instagram",
    "Message": "Nachricht, welche gesendet wird",
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


## Other
Weiss nicht wie viele User ich maximal pro Stunden finden kann, müsste man noch genauer ausprobieren

Die Datei "messagedUsers.json" muss existieren, kann aber leer sein (im lazy :))
In dieser Datei befinden sich die Benutzernamen aller User welche bereits einmal angeschrieben wurden (doppeltes Anschreiben verhindern)

