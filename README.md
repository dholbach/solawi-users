# Email-Adressen aus Nextcloud

## Vorbereitung

Vorher:

```cli
pip3 install --user -r requirements.txt
cp -i solawi/secrets.py.example solawi/secrets.py
```

Dann in `solawi/secrets.py` die Einträge `USER` und `PASSWORD` bearbeiten.

## Benutzung

Um eine Liste aller Email-Adressen aller in [solawi/mailinglists.py](solawi/mailinglists.py) definierter Gruppen angezeigt zu bekommen:

```cli
./list_members
```

Um den derzeitigen Nutzer-Stand abzuspeichern und nur die neuen Nutzer angezeigt zu bekommen:

```cli
./list_members --save
```

Dies könnte hilfreich in einem Cron-Job sein, der die List-Admins darüber informiert, wer neu dazu gekommen ist.
