---
name: chronicle
description: Erstelle ein neues Prosa-Kapitel aus einer vorbereiteten Session (Storyboard, Szenen, Entwürfe, Kapitel). Setzt ein fertiges Transkript voraus.
argument-hint: "[session-pfad, z.B. sessions/2026-03-07_session-17]"
---

# Chronicle Pipeline

Erstelle ein neues Prosa-Kapitel aus einer vorbereiteten Session.

## Voraussetzungen

Der Session-Ordner existiert bereits mit abgeschlossener Transkription:

```
$ARGUMENTS/
  notes.md
  transcriptions/
    transkript_YYYY-MM-DD.txt   ← muss vorhanden sein
```

Falls das Transkript noch fehlt, weise den Benutzer auf `/transcribe` hin und brich ab.

## Pipeline-Überblick

Die Pipeline besteht aus 3 Schritten. **Jeder Schritt** durchläuft denselben Review-Zyklus:

1. Claude erstellt das Artefakt
2. Claude führt ein Self-Review durch und überarbeitet das Ergebnis
3. Claude präsentiert das Ergebnis dem Benutzer mit einer kurzen Zusammenfassung
4. Der Benutzer gibt Feedback oder sein Go → bei Feedback: überarbeiten und erneut vorlegen; bei Go: weiter zum nächsten Schritt

**Wichtig:** Nach jedem Self-Review und nach jeder Überarbeitung auf Benutzerfeedback: **warte auf explizite Freigabe** bevor du zum nächsten Schritt weitergehst.

---

## Schritt 1: Storyboard und Szenen

**Ziel:** Ein Storyboard und daraus abgeleitete Szenen-Dateien.

### 1a: Storyboard erstellen

**Eingabe:** `notes.md` + `transkript_YYYY-MM-DD.txt`
**Ausgabe:** `chronicle/storyboard/session-NN-storyboard.md`

Erstelle ein Storyboard mit folgender Struktur:

```markdown
# Storyboard – Session NN

## Szene 1: [Kurztitel]

**Ort:** [Schauplatz]
**Beteiligte:** [Charaktere]
**Perspektive:** [Erzählperspektive, z.B. "Ganden (begrenzt allwissend)"]
**Kernhandlung:**
- [Bullet-Punkte der wesentlichen Handlung]

**Stimmung/Ton:** [z.B. "angespannt, verhörartig"]
**Wichtige Details aus dem Transkript:**
- [Konkrete Details, Dialoge, Würfelergebnisse aus dem Transkript, die in die Prosa einfließen sollen]

## Szene 2: [Kurztitel]
...
```

Leitlinien für das Storyboard:
- Orientiere dich an den Szenen-Unterteilungen in `notes.md` (dort oft als "Szene 1", "Szene 2" etc. markiert).
- Identifiziere sinnvolle Szenengrenzen anhand von Ortswechseln, Zeitsprüngen oder thematischen Brüchen.
- Extrahiere konkrete spielmechanische Details (Würfelergebnisse, Skill-Checks) aus den Notizen – diese geben Hinweise auf den Ausgang von Aktionen.
- Notiere spezifische Details, Formulierungen und Dialogfetzen aus dem Transkript, die in die Prosa einfließen können.

**Self-Review:** Prüfe das Storyboard gegen `notes.md` auf Vollständigkeit – fehlen Handlungspunkte? Stimmt die Reihenfolge? Dann vorlegen und auf Freigabe warten.

### 1b: Szenen ableiten

**Eingabe:** Storyboard + Transkript
**Ausgabe:** `chronicle/szenen/session-NN-szene-01.md`, `session-NN-szene-02.md`, ...

Erstelle pro Szene eine Datei mit folgender Struktur:

```markdown
# Szene NN: [Titel aus dem Storyboard]

## Szenenbeschreibung

**Ort:** [Schauplatz]
**Beteiligte:** [Charaktere]
**Perspektive:** [Erzählperspektive]

## Handlungsablauf

[Detaillierter Ablauf der Szene als strukturierte Beschreibung – mehr Detail als das Storyboard, aber noch keine Prosa. Beschreibe was passiert, wer was sagt/tut, welche Emotionen und Reaktionen es gibt.]

## Transkript-Auszug

[Relevanter Abschnitt des Transkripts für diese Szene – die Zeitstempel-Bereiche aus dem Gesamttranskript, die zu dieser Szene gehören. Vollständig kopiert, nicht zusammengefasst.]
```

Leitlinien für die Szenen:
- Jede Szene soll den entsprechenden Transkript-Abschnitt enthalten, damit beim späteren Schreiben der Prosa alle Originalinformationen direkt verfügbar sind.
- Der Handlungsablauf soll deutlich detaillierter sein als das Storyboard, aber noch keine ausformulierte Prosa.
- Dialoge aus dem Transkript, die wörtlich oder sinngemäß in die Prosa übernommen werden können, hervorheben.

**Self-Review:** Prüfe jede Szene: Ist der Transkript-Auszug vollständig und korrekt zugeordnet? Deckt der Handlungsablauf alle Details aus Storyboard und Transkript ab? Dann vorlegen und auf Freigabe warten.

---

## Schritt 2: Szenen-Entwürfe (Prosa)

**Eingabe:** Szenen-Dateien aus `chronicle/szenen/`
**Ausgabe:** `chronicle/entwuerfe/kapitel-NN-szene-01-entwurf.md`, `kapitel-NN-szene-02-entwurf.md`, ...

Schreibe für jede Szene einen Prosa-Entwurf. **Jede Szene einzeln als eigene Datei**, damit sie unabhängig reviewt werden kann.

### Stilrichtlinien

Orientiere dich am Stil der bestehenden Kapitel in `chronicle/kapitel/`. Wesentliche Merkmale:

- **Sprache:** Deutsch, gehobener aber flüssiger Erzählstil. Keine übertriebene Poetik, sondern klare, bildhafte Prosa.
- **Perspektive:** Dritte Person, begrenzt allwissend – typischerweise aus der Perspektive eines der Spielercharaktere, kann zwischen Szenen wechseln.
- **Dialoge:** Wörtliche Rede in Anführungszeichen. Dialoge sollen sich natürlich anfühlen und den Charakter der Sprecher widerspiegeln. Orientiere dich an Formulierungen aus dem Transkript, aber übersetze sie in den Erzählstil.
- **Spielmechanik:** Würfelergebnisse und Regelmechaniken werden **nie** explizit erwähnt, sondern narrativ umgesetzt (z.B. ein hoher Investigation-Wurf wird zu einer detaillierten, scharfsinnigen Beobachtung).
- **Charakterstimmen:**
  - Ganden: kultiviert, analytisch, manipulativ-charmant, "der Professor"
  - Ghalrixtho: kühl, präzise, wenige Worte, raubtierhafte Präsenz
  - Komaru: pragmatisch, direkt, körperlich-dominant, trockener Humor
  - G4-X: mechanisch, pflichtbewusst
  - Varnira: klinisch, sachlich, kompetent
- **Atmosphäre:** Star-Wars-typisch – imperiale Bedrohung, Unterwelt-Flair, Frontier-Stimmung auf Lothal. Technische Details (Blaster, Repulsoren, Holoprojektoren) natürlich einstreuen.
- **Länge:** Szenen sollen ausführlich genug sein, um die Handlung lebendig zu machen, aber nicht aufgebläht. Orientierung: die bestehenden Kapitel haben ca. 1500–3000 Wörter.

**Self-Review pro Szene:** Prüfe auf:
- Konsistenz mit den Quellen (Notizen, Transkript, Storyboard) – werden alle wesentlichen Handlungspunkte abgedeckt?
- Stilkonsistenz mit bestehenden Kapiteln
- Charakterstimmen – klingt jeder Charakter wie er selbst?
- Unnötige Redundanz oder Fülltext
- Überarbeite den Entwurf basierend auf dem Self-Review.

Dann vorlegen und auf Freigabe warten. **Jede Szene einzeln vorlegen** – nicht alle auf einmal.

---

## Schritt 3: Kapitel zusammenführen

**Eingabe:** Alle freigegebenen Szenen-Entwürfe
**Ausgabe:** `chronicle/kapitel/kapitel-NN.md`

1. Füge alle Szenen-Entwürfe in der richtigen Reihenfolge zu einem Kapitel zusammen.
2. Ergänze Übergänge zwischen den Szenen, wo nötig (Zeitsprünge, Ortswechsel).
3. Erstelle den Kapitel-Header:

```markdown
# Kapitel NN – [Titel]

[Prosa-Text]

---

[← Kapitel NN-1](kapitel-NN-1.md)
```

4. Aktualisiere die Navigation im vorherigen Kapitel (füge Vorwärts-Link hinzu, falls nicht vorhanden).
5. Aktualisiere `chronicle/kapitel/README.md` – neuen Eintrag in die Inhaltsverzeichnis-Tabelle einfügen.

**Kapitel-Titel:** Leite einen kurzen, stimmungsvollen Titel ab, der das zentrale Thema oder Ereignis der Session einfängt (Beispiele: "Kollateralschäden", "Atmosphärische Störungen", "Letzte Nacht auf Lothal").

**Self-Review:** Lies das gesamte Kapitel am Stück. Prüfe:
- Lesen sich die Szenenübergänge flüssig?
- Gibt es Widersprüche oder Wiederholungen zwischen Szenen?
- Stimmt der Gesamtbogen?
- Sind die Links korrekt (vorheriges Kapitel, README)?

Dann vorlegen und auf finale Freigabe warten.

---

## Nach Abschluss

Wenn das Kapitel final freigegeben ist:
- Bestätige, welche Dateien erstellt/geändert wurden.
- Schlage einen Commit vor (aber führe ihn nicht eigenständig aus).
