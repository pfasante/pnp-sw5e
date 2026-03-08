---
name: transcribe
description: Transkribiere die Audio-Dateien einer Session mit whisper-ctranslate2. Erzeugt ein zusammengeführtes Transkript.
argument-hint: "[session-pfad, z.B. sessions/2026-03-07_session-17]"
---

# Transkription

Transkribiere die Audio-Dateien einer Session.

## Voraussetzungen

Der Session-Ordner existiert bereits mit Audio-Dateien:

```
$ARGUMENTS/
  notes.md
  transcriptions/
    *.aac   (gitignored, lokal vorhanden)
```

## Ablauf

1. Lies `notes.md` im Session-Ordner, um das Session-Datum zu ermitteln.
2. Liste die `.aac`-Dateien im `transcriptions/`-Unterordner auf.
3. Führe das Transkriptionsskript aus:

```bash
cd $ARGUMENTS/transcriptions
uv run python ../../../scripts/transcribe_merge.py \
  --audio <alle .aac-Dateien> \
  --output transkript_YYYY-MM-DD.txt
```

4. Prüfe, ob die Ausgabedatei erzeugt wurde und lies die ersten Zeilen zur Bestätigung.
5. Melde dem Benutzer: Transkription abgeschlossen, Dateigröße, Anzahl Zeilen.

**Hinweis:** Die Transkription dauert ca. 30 Minuten. Das Skript gibt Fortschrittsmeldungen aus.
