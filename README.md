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
chronicle/
  README.md               ← Workflow-Dokumentation
  01-storyboard/          ← Grobe Handlungsgerüste
  02-szenen/              ← Szenenstruktur und Übergänge
  03-entwuerfe/           ← Rohentwürfe der Kapitel
  04-kapitel/             ← Fertige Prosa-Kapitel
    README.md             ← Chronik-Übersicht und Inhaltsverzeichnis
    kapitel-NN.md
scripts/
  transcribe_merge.py  ← Whisper-Transkription und Zusammenführung
pyproject.toml            ← uv-Projektdatei (Python-Abhängigkeiten)
```

---

## Workflow: Session → Transkription → Chronik

### 1. Aufnahme

Die Sessions werden über Discord gespielt. Der [Craig Bot](https://craig.chat/) nimmt automatisch eine separate Audiospur pro Spieler auf (`.aac`). Nach der Session werden die Dateien als Zip-Archiv heruntergeladen und im Session-Ordner abgelegt. Audio-Dateien sind in git **nicht** versioniert (`.gitignore`).

### 2. Transkription

```bash
uv run python scripts/transcribe_merge.py
```

Das Skript ruft `whisper-ctranslate2` auf (Modell `large-v3`, Sprache Deutsch, CUDA bfloat16) und erzeugt:
- eine `.tsv`-Datei pro Sprecher-Spur
- ein zusammengeführtes Transkript (`.txt`) mit Zeitstempeln und Sprecherzuordnung im Format `[HH:MM:SS] Sprecher: Text`

Ausgabe landet in `sessions/YYYY-MM-DD_session-NN/transcriptions/`.

### 3. Prosa-Ausarbeitung

Die Prosa-Chronik wird mit Hilfe von [Claude Code](https://claude.ai/code) erstellt. Der Prozess ist als mehrstufige Pipeline implementiert, bei der Claude als Co-Autor agiert und der menschliche Autor an jedem Schritt Feedback gibt und Korrekturen vornimmt.

Die Pipeline ist in zwei [Claude Code Skills](https://docs.anthropic.com/en/docs/claude-code/skills) aufgeteilt:

1. **`/transcribe`** — Startet die Whisper-Transkription der Audio-Dateien einer Session (~30 Min. Laufzeit, erfordert NVIDIA GPU mit CUDA).

2. **`/chronicle`** — Verwandelt eine fertige Transkription in ein Prosa-Kapitel. Die Pipeline durchläuft vier Stufen, jeweils mit Self-Review durch Claude und expliziter Freigabe durch den Autor:
   - **Storyboard** — Grobe Szenenstruktur aus Notizen und Transkript
   - **Szenen** — Detaillierte Szenenbeschreibungen mit Transkript-Auszügen
   - **Entwürfe** — Prosa-Entwurf pro Szene (einzeln reviewbar)
   - **Kapitel** — Zusammenführung aller Szenen mit Übergängen und Navigation

Die Zwischenprodukte jeder Stufe werden in `chronicle/` versioniert (siehe [`chronicle/README.md`](chronicle/README.md)), sodass der gesamte Entstehungsprozess eines Kapitels nachvollziehbar bleibt. Die fertigen Kapitel landen in `chronicle/04-kapitel/kapitel-NN.md`.

---

## Python-Umgebung (uv)

Abhängigkeiten werden mit [uv](https://docs.astral.sh/uv/) verwaltet.

```bash
# Abhängigkeiten installieren / .venv anlegen
uv sync

# Skript ausführen (ohne vorher venv aktivieren)
uv run python scripts/transcribe_merge.py
```

Die `.venv/` ist gitignored. `uv.lock` wird versioniert.
