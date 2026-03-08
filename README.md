# Star Wars: Echoes of the Empire – Kampagnen-Repository

Pen-&-Paper-Kampagne nach den Regeln von [SW5e](https://sw5e.com), gespielt auf [Roll20](https://app.roll20.net/campaigns/details/19743219/star-wars-echoes).

Dieses Repository enthält Session-Notizen, Audio-Transkriptionen, Charakterdaten und die ausgearbeitete Prosa-Chronik der Kampagne.

---

## Repository-Struktur

```
sessions/
  YYYY-MM-DD_session-NN/
    notes.md              ← Bullet-Notizen zur Session
    transcriptions/       ← .tsv pro Sprecher + zusammengeführtes .txt
                            (Audio-Dateien .aac/.wav sind gitignored)
background/
  bekannter-hintergrund.md  ← Spieler-seitig bekannte Lore
  charaktere/
    ghalrixtho.md / ganden.md / komaru.md / g4-x.md / varnira.md
story/
  README.md               ← Chronik-Übersicht und Inhaltsverzeichnis
  kapitel-NN.md           ← Ausgearbeitete Prosa-Kapitel
chronicle/
  README.md               ← Workflow-Dokumentation
  storyboard/             ← Grobe Handlungsgerüste
  szenen/                 ← Szenenstruktur und Übergänge
  entwuerfe/              ← Rohentwürfe der Kapitel
scripts/
  transcribe_merge_sync.py  ← Whisper-Transkription und Zusammenführung
pyproject.toml            ← uv-Projektdatei (Python-Abhängigkeiten)
```

---

## Workflow: Session → Transkription → Chronik

### 1. Aufnahme

Jeder Spieler nimmt seine eigene Spur auf (`.aac` oder `.wav`). Nach der Session werden die Dateien in ein Zip-Archiv gepackt und im Session-Ordner abgelegt. Audio-Dateien sind in git **nicht** versioniert (`.gitignore`).

### 2. Transkription

```bash
uv run python scripts/transcribe_merge_sync.py
```

Das Skript ruft `whisper-ctranslate2` auf (Modell `large-v3`, Sprache Deutsch, CUDA bfloat16) und erzeugt:
- eine `.tsv`-Datei pro Sprecher-Spur
- ein zusammengeführtes Transkript (`.txt`) mit Zeitstempeln und Sprecherzuordnung im Format `[HH:MM:SS] Sprecher: Text`

Ausgabe landet in `sessions/YYYY-MM-DD_session-NN/transcriptions/`.

### 3. Prosa-Ausarbeitung

*(Detaillierter Prozess wird noch ergänzt.)*

Die fertigen Kapitel kommen nach `story/kapitel-NN.md`. Zwischenschritte (Storyboard, Szenenstruktur, Rohentwürfe) liegen unter `chronicle/` – siehe [`chronicle/README.md`](chronicle/README.md).

---

## Python-Umgebung (uv)

Abhängigkeiten werden mit [uv](https://docs.astral.sh/uv/) verwaltet.

```bash
# Abhängigkeiten installieren / .venv anlegen
uv sync

# Skript ausführen (ohne vorher venv aktivieren)
uv run python scripts/transcribe_merge_sync.py
```

Die `.venv/` ist gitignored. `uv.lock` wird versioniert.
