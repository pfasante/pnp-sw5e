# Star Wars: Echoes of the Empire – Kampagnen-Repository

Pen-&-Paper-Kampagne nach den Regeln von [SW5e](https://sw5e.com), gespielt auf [Roll20](https://app.roll20.net/campaigns/details/19743219/star-wars-echoes).

Dieses Repository enthält Session-Notizen, Audio-Transkriptionen, Charakterdaten und die ausgearbeitete Prosa-Chronik der Kampagne.

---

## Kampagnen-Stand

- **Erstes Abenteuer "Rauhnacht" abgeschlossen** mit Session 18. Die Kapitel 13–18 liegen als Prosa-Chronik in `chronicle/04-kapitel/`.
- **Session 19** (2026-05-14) eröffnet das zweite Abenteuer an Bord der *Turbot*: Aufbruch von Lothal, Hyperraum-Zwischenfall bei den Iego-Wolken.
- **Spielleiter-Wechsel ab Session 19:** Andreas übernimmt von Benjamin. Benjamin spielt jetzt den neuen Charakter **Kaelum** — den jungen Padawan, den die Crew in Session 18 aus Inquisitor-Gefangenschaft befreit hat.

---

## Repository-Struktur

```
sessions/
  YYYY-MM-DD_session-NN/
    notes.md                 ← manuelle Bullet-Notizen zur Session
    transcriptions/          ← .tsv pro Sprecher + zusammengeführtes .txt
                               (Audio-Dateien .aac/.wav sind gitignored)

background/
  bekannter-hintergrund.md   ← spieler-seitig bekannte Lore
  charaktere/
    ghalrixtho.md            ← Friedrich (Chiss Operative)
    ghalrixtho-short.md      ← Kurzfassung für den GM (PDF-Quelle)
    ganden.md                ← Andreas (ab S19 Spielleiter)
    komaru.md                ← Martin (Togorian Scout)
    g4-x.md                  ← Stefan (Droid Fighter)
    varnira.md               ← Heike (Devaronian Engineer)
    kaelum.md                ← Benjamin/Benni (Padawan, ab S19)

chronicle/
  README.md                  ← Pipeline-Doku
  01-storyboard/             ← grobe Handlungsgerüste
  02-szenen/                 ← Szenenstruktur und Übergänge
  03-entwuerfe/              ← Rohentwürfe der Kapitel
  04-kapitel/                ← fertige Prosa-Kapitel
    README.md                ← Inhaltsverzeichnis der Chronik
    kapitel-NN.md

scripts/
  transcribe_merge.py        ← Whisper-Transkription und Zusammenführung
  whisper-corrections.md     ← bekannte Falschvarianten (über Sessions pflegen)
  README.md                  ← Skript-Doku

pyproject.toml               ← uv-Projektdatei
```

---

## Pro Session: konkreter Ablauf

Aufnahme und Erst-Transkription laufen auf der **Windows-Maschine** (NVIDIA-GPU), Korrektur und Chronik-Ausarbeitung auf dem **Laptop**.

### 1. Aufnahme-Maschine (Windows)

1. **Discord-Aufnahme abrufen.** Der [Craig Bot](https://craig.chat/) liefert ein ZIP mit einer Audiospur pro Spieler.
2. **ZIP entpacken** und die Einzelspuren manuell auf die kanonischen Spieler-Dateinamen umbenennen: `andreas.aac`, `benjamin.aac`, `friedrich.aac`, `martin.aac` (und weitere, falls vorhanden).
3. **Audio einsortieren** in `sessions/YYYY-MM-DD_session-NN/transcriptions/`.
4. **Transkription starten** mit `-k`, damit die Einzel-TSVs für spätere Diagnose erhalten bleiben:

   ```bash
   cd sessions/2026-05-14_session-19/transcriptions
   uv run python ../../../scripts/transcribe_merge.py \
     -a andreas.aac benjamin.aac friedrich.aac martin.aac \
     -k
   ```

   Erzeugt `transkript_YYYY-MM-DD.txt` (heutiges Datum) plus die TSVs. Wenn das Session-Datum vom Ausführungstag abweicht, mit `-o transkript_<session-datum>.txt` überschreiben.
5. **Session-Notizen** in `notes.md` ergänzen — Stichworte, wichtige Entscheidungen, offene Hooks.
6. **Commit & Push:** Einzel-TSVs, gemergtes `.txt` und `notes.md` versionieren. Audio-Dateien sind über `.gitignore` ausgeklammert und sollen nicht eingecheckt werden.

### 2. Laptop (Korrektur & Chronik)

7. **`git pull`** — die frischen Transkripte holen.
8. **Transkript korrigieren** anhand von [`scripts/whisper-corrections.md`](scripts/whisper-corrections.md). Whisper fehlerkennt Charakter- und NPC-Namen systematisch; diese Datei pflegt alle bisher beobachteten Falschvarianten. Beim Korrekturlauf neu auftauchende Varianten **dort eintragen**, damit der Korpus über die Kampagne wächst.
9. **`/chronicle`-Skill in Claude Code starten.** Die Pipeline durchläuft vier Stufen — Storyboard → Szenen → Entwürfe → Kapitel — jeweils mit Self-Review durch Claude und expliziter Freigabe durch den Autor. Zwischenprodukte landen in `chronicle/01-*` bis `chronicle/03-*`, das fertige Kapitel in `chronicle/04-kapitel/kapitel-NN.md`.
10. **Commit & Push** des fertigen Kapitels samt Zwischenprodukten.

---

## Werkzeug-Übersicht

### Skripte

[`scripts/transcribe_merge.py`](scripts/transcribe_merge.py) ruft `whisper-ctranslate2` (Modell `large-v3`, Sprache Deutsch, CUDA `bfloat16`) auf und fügt die Einzel-TSVs zu einem chronologischen `.txt`-Transkript zusammen. Ausgabe-Format:

```
[00:00:12] Andreas: Ich würde sagen, wir gehen links.
[00:00:15] Martin: Links? Da war doch der Droide.
[00:00:18] Friedrich: Ich scanne den Korridor zuerst.
```

Optionen siehe [`scripts/README.md`](scripts/README.md): `-a` (Audio), `-M` (nur Merge), `-o` (Ausgabename), `-k` (TSVs behalten), `-m` (Whisper-Modell).

### Claude-Code-Skills

| Skill | Zweck |
|-------|-------|
| `/transcribe` | Wrapper um `transcribe_merge.py` mit Skill-UI — Alternative zum manuellen Aufruf in Schritt 4 |
| `/chronicle` | vierstufige Pipeline für die Prosa-Ausarbeitung (Schritt 9) |

### Python-Umgebung

Abhängigkeiten werden mit [uv](https://docs.astral.sh/uv/) verwaltet.

```bash
# Abhängigkeiten installieren / .venv anlegen
uv sync

# Skript ausführen (ohne vorher venv zu aktivieren)
uv run python scripts/transcribe_merge.py --help
```

`.venv/` ist gitignored, `uv.lock` wird versioniert für reproduzierbare Builds.
