# scripts/

Hilfsskripte für die Kampagnen-Infrastruktur.

---

## transcribe_merge.py

Transkribiert Audio-Spuren einer Session mit `whisper-ctranslate2` und fügt die Einzel-TSVs zu einem chronologischen Gesamttranskript zusammen.

### Voraussetzungen

```bash
uv sync   # installiert whisper-ctranslate2 in .venv
```

Benötigt eine NVIDIA-GPU (CUDA). Verwendet Modell `large-v3`, Sprache Deutsch, Compute-Typ `bfloat16`.

### Typischer Workflow

Die Audio-Dateien werden **nicht** per git versioniert (`.gitignore`). Vor der Transkription die Dateien manuell in den Session-Ordner legen:

```
sessions/YYYY-MM-DD_session-NN/transcriptions/
  andreas.aac
  benjamin.aac
  martin.aac
  friedrich.aac
```

Dann aus dem `transcriptions/`-Ordner heraus ausführen:

```bash
cd sessions/2026-03-07_session-17/transcriptions

uv run python ../../../scripts/transcribe_merge.py \
  --audio andreas.aac benjamin.aac martin.aac friedrich.aac
```

Das erzeugt `transkript_YYYY-MM-DD.txt` (Datum des Ausführungstages) und löscht die TSVs danach automatisch.

Mit explizitem Ausgabenamen (empfohlen, falls das Datum der Session vom Ausführungstag abweicht):

```bash
uv run python ../../../scripts/transcribe_merge.py \
  --audio andreas.aac benjamin.aac martin.aac friedrich.aac \
  --output transkript_2026-03-07.txt
```

### Nur TSVs zusammenführen (ohne erneute Transkription)

```bash
uv run python ../../../scripts/transcribe_merge.py \
  --merge-only andreas.tsv benjamin.tsv martin.tsv friedrich.tsv \
  --output transkript_2026-03-07.txt
```

### Alle Optionen

| Flag | Kurz | Beschreibung |
|------|------|--------------|
| `--audio` | `-a` | Audio-Dateien transkribieren und mergen |
| `--merge-only` | `-M` | Nur vorhandene TSVs zusammenführen, keine Transkription |
| `--output` | `-o` | Ausgabedatei (Standard: `transkript_YYYY-MM-DD.txt` mit heutigem Datum) |
| `--model` | `-m` | Whisper-Modell (Standard: `large-v3`) |
| `--keep-tsvs` | `-k` | TSV-Dateien nach dem Merge behalten (Standard: werden gelöscht) |

### Ausgabeformat

```
[00:00:12] Andreas: Ich würde sagen, wir gehen links.
[00:00:15] Martin: Links? Da war doch der Droide.
[00:00:18] Friedrich: Ich scanne den Korridor zuerst.
```

Sprecher werden aus dem Dateinamen abgeleitet und groß geschrieben (`andreas.aac` → `Andreas`).
