# Repository Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Repository-Struktur von Google-Drive-Archiv zu sauberem GitHub-Markdown-Repository migrieren.

**Architecture:** Neues sessions/-Verzeichnis bündelt alle Sitzungsdaten. Background-Dateien werden nach Markdown konvertiert und aufgeteilt. Prosa-Chronik in Einzelkapitel zerlegt. uv ersetzt die manuelle venv.

**Tech Stack:** Python/uv, Whisper-ctranslate2, GitHub Markdown

---

## Vorab: Zur uv-Migration auf Windows

Ja, uv funktioniert problemlos unter Windows. Migration von `$HOME\whisper-env`:

```powershell
# Installation (einmalig)
winget install --id=astral-sh.uv
# oder:
irm https://astral.sh/uv/install.ps1 | iex

# Im Projektverzeichnis
cd C:\Users\asante\werkbank\pnp-sw5e
uv init --no-readme          # erzeugt pyproject.toml
uv add whisper-ctranslate2   # trägt Dependency ein + erstellt .venv
uv run python scripts/transcribe_merge_sync.py --help  # Test
```

Das erzeugte `.venv` liegt im Projektordner. Die alte `$HOME\whisper-env` kann danach gelöscht werden.

---

## Task 1: uv Setup

**Files:**
- Create: `pyproject.toml`
- Create: `.python-version`
- Modify: `.gitignore`

**Step 1: pyproject.toml erstellen**

```toml
[project]
name = "pnp-sw5e"
version = "0.1.0"
description = "Star Wars 5e PnP Kampagnen-Tools"
requires-python = ">=3.11"
dependencies = [
    "whisper-ctranslate2",
]

[tool.uv]
dev-dependencies = []
```

**Step 2: .python-version erstellen**

```
3.11
```

**Step 3: .gitignore erweitern** – `.venv/` und `uv.lock` hinzufügen:

```gitignore
# uv
.venv/
# uv.lock wird committed (reproduzierbare Builds)
```

**Hinweis:** `uv.lock` SOLL committed werden für reproduzierbare Umgebungen.

**Step 4: Commit**

```bash
git add pyproject.toml .python-version .gitignore
git commit -m "chore: add uv project setup for whisper-ctranslate2"
```

---

## Task 2: Sessions-Ordner anlegen – notes.md pro Session

**Quelle:** `background/notizen.txt`
**Ziel:** `sessions/<ordnername>/notes.md` für alle 17 Sessions

### Konvertierungsregel für Markdown

| notizen.txt Format | notes.md Format |
|---|---|
| `o Siebzehnte Runde` | `# Session 17 – Siebzehnte Runde` |
| `[2026-03-07::20:50, ]` | `**Datum:** 2026-03-07  **Startzeit:** 20:50` |
| `\t* Text` | `- Text` |
| `\t\t* Text` | `  - Text` |
| `\t\t\t* Text` | `    - Text` |

### Zu erstellende Dateien (Ordnername → Quell-Abschnitt in notizen.txt)

| Ordner | Inhalt aus notizen.txt |
|--------|----------------------|
| `sessions/2025-06-24_session-01/notes.md` | `o Erste Runde` |
| `sessions/2025-07-03_session-02/notes.md` | `o Zweite Runde` |
| `sessions/2025-07-17_session-03/notes.md` | `o Dritte Runde` |
| `sessions/2025-07-27_session-04/notes.md` | `o Vierte Runde` |
| `sessions/session-05/notes.md` | `o Fünfte Runde` (kein Datum) |
| `sessions/2025-10-13_session-06/notes.md` | `o Sechste Runde` |
| `sessions/2025-10-23_session-07/notes.md` | `o Siebte Runde` |
| `sessions/2025-11-14_session-08/notes.md` | `o Achte Runde` |
| `sessions/2025-11-20_session-09/notes.md` | `o Neunte Runde` |
| `sessions/2025-12-01_session-10/notes.md` | `o Zehnte Runde` |
| `sessions/2025-12-18_session-11/notes.md` | `o Elfte Runde` |
| `sessions/2025-12-27_session-12/notes.md` | `o Zwölfte Runde` (Datum unsicher) |
| `sessions/2026-01-15_session-13/notes.md` | `o Dreizehnte Runde` |
| `sessions/2026-01-22_session-14/notes.md` | `o Vierzehnte Runde` |
| `sessions/2026-01-29_session-15/notes.md` | `o Fünfzehnte Runde` |
| `sessions/2026-02-18_session-16/notes.md` | `o Sechzehnte Runde` |
| `sessions/2026-03-07_session-17/notes.md` | `o Siebzehnte Runde` |

Außerdem: `sessions/ghalrixtho-charaktererschaffung/notes.md` aus dem Abschnitt `o Ghalrixtho Charaktererschaffung`.

**Beispiel notes.md** (Session 17):

```markdown
# Session 17 – Siebzehnte Runde

**Datum:** 2026-03-07  **Startzeit:** 20:50

## Notizen

- Wir machen genau da weiter, wo wir letztes Mal aufgehört haben: wir fahren mit dem Gleiter in die Turbot rein
- Szene 1 in der Turbot
  - Ganden führt Daro Fel erstmal in die Kombüse, Fel scheint sich zu beruhigen
  - ...
```

**Step: Commit**

```bash
git add sessions/
git commit -m "feat: add per-session notes.md files from notizen.txt"
```

---

## Task 3: Transkriptions-Dateien in Session-Ordner verschieben

**Quelle:** `transcriptions/aufnahme_2026-02-18/` und `transcriptions/aufnahme_2026-03-07/`
**Ziel:** `sessions/<ordner>/transcriptions/`

### Zu verschiebende Dateien

**Session 16:**
```
transcriptions/aufnahme_2026-02-18/*.tsv
transcriptions/aufnahme_2026-02-18/transkript_2026-02-18.txt
transcriptions/aufnahme_2026-02-18/transkript_2026-02-18-unoptimized.txt
→ sessions/2026-02-18_session-16/transcriptions/
```

**Session 15** (falls der bereits bereinigte Ordner noch existiert):
```
transcriptions/aufnahme_2026-01-29/transkript_2026-01-29.txt  (o.ä.)
→ sessions/2026-01-29_session-15/transcriptions/
```

**Session 17:**
```
transcriptions/aufnahme_2026-03-07/*.tsv
transcriptions/aufnahme_2026-03-07/transkript_2026-03-07.txt
→ sessions/2026-03-07_session-17/transcriptions/
```

**Hinweis:** Die `.aac`/`.wav`/`.zip` Dateien sind gitignored und müssen lokal manuell verschoben werden – im Commit tauchen sie nicht auf. Den leeren `transcriptions/`-Ordner danach löschen.

**Step: Commit**

```bash
git add sessions/ transcriptions/
git commit -m "refactor: move transcription files into session folders"
```

---

## Task 4: Charakterbögen aufteilen

**Quelle:** `background/charakterbuch.txt`
**Ziel:** `background/charaktere/<name>.md`

### Trennstellen in charakterbuch.txt

| Datei | Abschnitt (Zeile beginnt mit) |
|-------|------------------------------|
| `background/charaktere/ghalrixtho.md` | `# Ghalrixtho` (Zeile 1) bis kurz vor `# Ganden` |
| `background/charaktere/ganden.md` | `# Ganden` bis kurz vor `# Komaru` |
| `background/charaktere/komaru.md` | `# Komaru` bis kurz vor `# G4-X` |
| `background/charaktere/g4-x.md` | `# G4-X` bis kurz vor `# Varnira` |
| `background/charaktere/varnira.md` | `# Varnira` bis Ende |

**Format-Korrekturen:**
- `** ` (doppelt) → `## ` (H2)
- `*** ` (dreifach) → `### ` oder Listen-Eintrag je nach Kontext
- `**** ` → `#### ` oder tiefere Liste

**Beispiel ghalrixtho.md Header:**

```markdown
# Ghalrixtho

**Spieler:** Friedrich (Fritze, Fritz)
**Voller Name:** Erighal'rix'tholiris

## Aussehen
...

## Hintergrund
...

## Charakterbogen

| Attribut | Wert |
|----------|------|
| Klasse | Operative Level 3 |
...
```

**Step: Commit**

```bash
git add background/charaktere/
git commit -m "feat: split charakterbuch into per-character markdown files"
```

---

## Task 5: Bekannter-Hintergrund konvertieren

**Quelle:** `background/bekannter-hintergrund.txt`
**Ziel:** `background/bekannter-hintergrund.md`

**Format-Korrekturen:**
- `* Text` → `## Text` wenn Überschrift, sonst `- Text`
- `** Text` → `- Text`

**Ziel-Format:**

```markdown
# Bekannter Hintergrund

## Die Turbot

- ein paar Stunden außerhalb von Capital City
- wir haben dort zur Tarnung eine archäologische Ausgrabungsstelle eingerichtet
- ...

## Der "geliehene" Speeder

- ...
```

**Step: Commit**

```bash
git add background/bekannter-hintergrund.md
git rm background/bekannter-hintergrund.txt
git commit -m "feat: convert bekannter-hintergrund to markdown"
```

---

## Task 6: Prosa-Chronik in Einzelkapitel aufteilen

**Quelle:** `story/geschichte.txt` (37800 Tokens – in Chunks lesen!)
**Ziel:** `story/kapitel-13.md` bis `story/kapitel-17.md`

### Trennstellen (Zeilen in geschichte.txt)

| Datei | Von Zeile | Bis Zeile |
|-------|-----------|-----------|
| `story/kapitel-13.md` | 1 | 100 |
| `story/kapitel-14.md` | 101 | 199 |
| `story/kapitel-15.md` | 200 | 338 |
| `story/kapitel-16.md` | 339 | 505 |
| `story/kapitel-17.md` | 506 | Ende |

**Ziel-Format pro Kapitel:**

```markdown
# Kapitel 13 – Kollateralschäden

[Prosa-Text aus geschichte.txt]

---

← [Kapitel 14](kapitel-14.md)
```

(Navigation unten, kein Kapitel davor für Kapitel 13)

**Step: Commit**

```bash
git add story/kapitel-*.md
git commit -m "feat: split chronicle into per-chapter markdown files"
```

---

## Task 7: story/README.md – Opener und Inhaltsverzeichnis

**Ziel:** `story/README.md`

```markdown
# Die Chronik – Star Wars 5e Kampagne

*Lothal, 4 BBY. Eine Gruppe Außenseiter, die aus verschiedensten Gründen zusammenfand,
navigiert durch die Machenschaften des Imperiums, des Kobalt Kartells und dunklerer Mächte.*

---

## Charaktere

| Charakter | Spieler | Klasse |
|-----------|---------|--------|
| [Ganden Arvang](../background/charaktere/ganden.md) | Andreas | Tactician Scholar |
| [Ghalrixtho](../background/charaktere/ghalrixtho.md) | Friedrich | Operative |
| [Komaru](../background/charaktere/komaru.md) | Martin | Scout |
| [G4-X](../background/charaktere/g4-x.md) | Stefan | Fighter |
| [Varnira Sesh](../background/charaktere/varnira.md) | Heike | Engineer |

---

## Kapitel

> Kapitel 1–12 sind noch nicht als Prosa verfasst. Die Sitzungsnotizen findest du im
> [sessions/-Ordner](../sessions/).

| Kapitel | Titel | Session |
|---------|-------|---------|
| [Kapitel 13](kapitel-13.md) | Kollateralschäden | [Session 13](../sessions/2026-01-15_session-13/) |
| [Kapitel 14](kapitel-14.md) | Hinterlassenschaften | [Session 14](../sessions/2026-01-22_session-14/) |
| [Kapitel 15](kapitel-15.md) | Atmosphärische Störungen | [Session 15](../sessions/2026-01-29_session-15/) |
| [Kapitel 16](kapitel-16.md) | Echo der Tiefe | [Session 16](../sessions/2026-02-18_session-16/) |
| [Kapitel 17](kapitel-17.md) | Letzte Nacht auf Lothal | [Session 17](../sessions/2026-03-07_session-17/) |
```

**Step: Commit**

```bash
git add story/README.md
git commit -m "feat: add story index with table of contents"
```

---

## Task 8: Chronicle-Ordner für Generierungs-Zwischendaten

**Ziel:** Strukturierter Arbeitsordner für den Chronik-Schreibprozess

```
chronicle/
  README.md
  storyboard/
    .gitkeep
  szenen/
    .gitkeep
  entwuerfe/
    .gitkeep
```

**chronicle/README.md:**

```markdown
# Chronicle Workbench

Arbeitsordner für die Erstellung der Prosa-Chronik.

## Workflow

1. **sessions/*/notes.md** – Rohnotizen aus der Sitzung
2. **chronicle/storyboard/** – Grobe Szenenstruktur (welche Szenen, welche Reihenfolge)
3. **chronicle/szenen/** – Ausgearbeitete Einzelszenen-Entwürfe
4. **chronicle/entwuerfe/** – Kapitelentwürfe vor Finalisierung
5. **story/kapitel-NN.md** – Finales Kapitel

## Dateibenennung

- Storyboard: `session-NN-storyboard.md`
- Szene: `session-NN-szene-01.md`
- Entwurf: `kapitel-NN-entwurf-v1.md`
```

**Step: Commit**

```bash
git add chronicle/
git commit -m "feat: add chronicle workbench folder structure"
```

---

## Task 9: Cleanup und README.md aktualisieren

**Files to delete:**
- `background/notizen.txt` (Inhalt in sessions/*/notes.md migriert)
- `background/charakterbuch.txt` (Inhalt in background/charaktere/ migriert)
- `background/bekannter-hintergrund.txt` (ersetzt durch .md)
- `story/geschichte.txt` (aufgeteilt in kapitel-*.md)
- `transcriptions/` (leer nach Task 3)

**README.md aktualisieren:**

```markdown
# pnp-sw5e – Star Wars 5e Kampagnen-Chronik

## Repository-Struktur

- **[sessions/](sessions/)** – Sitzungsnotizen und Transkriptionen
- **[story/](story/)** – Prosa-Chronik der Kampagne
- **[background/](background/)** – Charaktere und Spielwelt-Hintergrund
- **[chronicle/](chronicle/)** – Arbeitsordner für die Chronik-Erstellung
- **[scripts/](scripts/)** – Transkriptions-Tools

## Transkriptions-Workflow

```bash
# Setup (einmalig)
uv sync

# Transkription einer Sitzung
cd sessions/YYYY-MM-DD_session-NN/
uv run python ../../scripts/transcribe_merge_sync.py \
  --audio transcriptions/andreas.aac transcriptions/benjamin.aac \
  --output transcriptions/transkript_DATUM.txt
```
```

**Step: Final Commit**

```bash
git add README.md
git rm background/notizen.txt background/charakterbuch.txt background/bekannter-hintergrund.txt story/geschichte.txt
git commit -m "chore: remove migrated source files, update README"
```
