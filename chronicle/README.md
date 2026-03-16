# Chronicle Workbench

Arbeitsordner für die Erstellung der Prosa-Chronik.

## Workflow

1. **[sessions/](../sessions/)** – Rohnotizen aus der Sitzung (`notes.md`)
2. **[01-storyboard/](01-storyboard/)** – Grobe Szenenstruktur: welche Szenen, welche Reihenfolge, Perspektive
3. **[02-szenen/](02-szenen/)** – Ausgearbeitete Einzelszenen-Entwürfe
4. **[03-entwuerfe/](03-entwuerfe/)** – Kapitelentwürfe vor Finalisierung
5. **[04-kapitel/](04-kapitel/)** – Finales Kapitel (`kapitel-NN.md`)

## Automatisierte Pipeline

Die Pipeline ist in zwei Claude Code Slash-Commands aufgeteilt:

1. **[`/transcribe`](../.claude/skills/transcribe/SKILL.md)** — Audio-Transkription (~30 Min.), erzeugt `transkript_YYYY-MM-DD.txt`
2. **[`/chronicle`](../.claude/skills/chronicle/SKILL.md)** — Storyboard → Szenen → Entwürfe → Kapitel (setzt fertiges Transkript voraus)

## Dateibenennung

| Ordner | Muster | Beispiel |
|--------|--------|---------|
| 01-storyboard/ | `session-NN-storyboard.md` | `session-17-storyboard.md` |
| 02-szenen/ | `session-NN-szene-NN.md` | `session-17-szene-03.md` |
| 03-entwuerfe/ | `kapitel-NN-szene-NN-entwurf.md` | `kapitel-16-szene-02-entwurf.md` |
