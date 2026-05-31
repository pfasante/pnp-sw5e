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

## Kampagnen-Daten

### Spieler ↔ Charakter-Mapping

Die Sprecher-Tags im Transkript sind **Spielernamen**, nicht Charakternamen. Beim Lesen des Transkripts immer übersetzen:

| Spieler | Charakter |
|---------|-----------|
| Andreas | Spielleiter (vormals Spieler von Ganden, ab Session 19 GM) |
| Friedrich | Ghalrixtho |
| Martin | Komaru |
| Benjamin | Kaelum (ab Session 19 Spieler-Charakter, davor war Benjamin Spielleiter) |
| Heike | Varnira Sesh |
| Stefan | G4-X |

Bei Sessions vor Session 19 war Benjamin der Spielleiter und Ganden wurde von Andreas gespielt. Mapping bei alten Sessions entsprechend anpassen.

## Hintergrundmaterial

Lies zu Beginn der Pipeline die Dateien im `background/`-Ordner, um den Kontext der Kampagne zu verstehen:

- **`background/bekannter-hintergrund.md`** – Spieler-seitig bekannte Lore (Schiff, Speeder, Umgebung). Wird im Lauf der Kampagne erweitert.
- **`background/charaktere/*.md`** – Charakterbögen der Spielercharaktere (Fähigkeiten, Hintergrund, Persönlichkeit). Beachte besonders den Abschnitt **"In der Kampagne bekannt"** — er regelt, was die anderen Spielercharaktere über jeden Charakter wissen dürfen.

Diese Informationen sind wichtig für:
- Korrekte Beschreibung von Ausrüstung, Fahrzeugen und Orten (z.B. der Speeder ist ein Brett mit angeschweißtem Düsentriebwerk, kein normales Fahrzeug)
- Charakterstimmen und Verhaltensmuster, die über die Kurzprofile in den Stilrichtlinien hinausgehen
- Konsistenz mit etablierter Kampagnen-Lore

**Vor dem Lesen des Transkripts:** Prüfe, ob die Whisper-Falscherkennungen aus [`scripts/whisper-corrections.md`](../../../scripts/whisper-corrections.md) bereits korrigiert wurden (Stichprobe mit `grep -iE "calum|galrix|ganten|komaro"` auf das Transkript). Falls noch Restvarianten gefunden werden, Benutzer darauf hinweisen, bevor die Pipeline weiterläuft. Neu entdeckte Falscherkennungen ans Ende der Pipeline notieren und in `whisper-corrections.md` ergänzen lassen.

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

**Eingabe:** `notes.md` + `transkript_YYYY-MM-DD.txt` + `background/`-Ordner (Lore, Charakterbögen)
**Ausgabe:** `chronicle/01-storyboard/session-NN-storyboard.md`

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
- Orientiere dich an den Szenen-Unterteilungen in `notes.md`, falls sinnvoll.
- Identifiziere sinnvolle Szenengrenzen anhand von Ortswechseln, Zeitsprüngen oder thematischen Brüchen.
- Extrahiere konkrete spielmechanische Details (Würfelergebnisse, Skill-Checks) aus den Notizen – diese geben Hinweise auf den Ausgang von Aktionen.
- Notiere spezifische Details, Formulierungen und Dialogfetzen aus dem Transkript, die in die Prosa einfließen können.

**Self-Review:** Prüfe das Storyboard gegen `notes.md` auf Vollständigkeit – fehlen Handlungspunkte? Stimmt die Reihenfolge? Dann vorlegen und auf Freigabe warten.

### 1b: Szenen ableiten

**Eingabe:** Storyboard + Transkript
**Ausgabe:** `chronicle/02-szenen/session-NN-szene-01.md`, `session-NN-szene-02.md`, ...

Erstelle pro Szene eine Datei mit folgender Struktur:

```markdown
# Szene NN: [Titel aus dem Storyboard]

## Szenenbeschreibung

**Ort:** [Schauplatz]
**Beteiligte:** [Charaktere]
**Perspektive:** [Erzählperspektive]
**Stimmung:** [tonale Färbung, übernommen aus dem Storyboard, ggf. präzisiert]

## Handlungsablauf

[Detaillierter Ablauf der Szene als strukturierte Beschreibung – mehr Detail als das Storyboard, aber noch keine Prosa. Beschreibe was passiert, wer was sagt/tut, welche Emotionen und Reaktionen es gibt.]

## Transkript-Auszug

[Relevanter Abschnitt des Transkripts für diese Szene – die Zeitstempel-Bereiche aus dem Gesamttranskript, die zu dieser Szene gehören. Vollständig kopiert, nicht zusammengefasst.]
```

Leitlinien für die Szenen:
- Jede Szene soll den entsprechenden Transkript-Abschnitt enthalten, damit beim späteren Schreiben der Prosa alle Originalinformationen direkt verfügbar sind.
- Der Handlungsablauf soll deutlich detaillierter sein als das Storyboard, aber noch keine ausformulierte Prosa.
- Dialoge aus dem Transkript, die wörtlich oder sinngemäß in die Prosa übernommen werden können, hervorheben.
- **Lore-Sprache bereits hier:** Der Handlungsablauf wird in Lore-Prosa formuliert, nicht in Regel-Sprech. Keine Game-Klassen ("Operative", "Slicer", "Scout", "Tactician-Scholar", "Engineer", "Fighter", "Padawan-Klasse" etc.), keine Skill-/Feat-Namen ("Crawl-Speed", "Sneak Attack", "Kampfmeditation", "Athletics-Wurf" etc.), keine Würfelbegriffe ("Wurf", "W20", "DC", "Saving Throw", "Schadenspunkte") und keine GM-Attributionen ("Andreas verlangt", "Andreas — als GM — bestätigt"). Würfel-Ergebnisse, Skill-Erfolge und Verletzungs-Mengen werden direkt narrativ übersetzt (hoher Wurf → präzise Beobachtung; X Schaden → konkrete Wunde). Die Originalsprache des GM bleibt nur im **Transkript-Auszug** stehen.
- **Keine Spekulation über Motive:** Beschreibe nur, was im Transkript explizit gesagt oder durch konkrete Handlungen gezeigt wird. Erfindete Hintergründe, Audienzen, Verbindungen oder dreifache "tiefe Bedeutungen" eines Satzes haben in der Szene nichts verloren — sie gehören in den Charakter-Hintergrund, nicht in den Sessions-Bericht.
- **Konsistenz mit Vorszene:** Die Position und der Zustand der Charaktere am Ende einer Szene sind der Startzustand der nächsten. Wenn Komaru in Szene 1 ins Cockpit kommt, ist er in Szene 2-4 bereits dort — er "kommt nicht nochmal hinzu".
- **Spieler-Meta vs. Charakter-Rede:** Im Transkript stehen die **Spielernamen** (Andreas, Benjamin, Friedrich, Martin) als Sprecher-Tags, nicht die Charakternamen. Spielernamen-Aussagen sind oft eine Mischung aus Meta-Beschreibung ("ich mache jetzt einen Wurf"), Charakter-Handlung ("ich klettere zum Turm") und wörtlicher Charakter-Rede. Wörtliche Zitate im Handlungsablauf nur dort, wo der Spieler eindeutig im Charakter spricht. Player-Meta in Lore-Beschreibung umformulieren.
- **TODO statt Erfinden:** Wenn ein Detail aus den Quellen nicht klar ist, mit `TODO AI: <frage>` markieren und vom Benutzer klären lassen, statt zu spekulieren.
- **Länge dynamisch:** Der Handlungsablauf einer Szene skaliert mit der Anzahl der Szenen einer Session. Faustregel: das Gesamtkapitel zielt auf ~2000–3500 Wörter Prosa; der Szenen-Handlungsablauf darf etwa **das 1,5-fache der zu erwartenden Prosa-Länge pro Szene** sein (Detail-Reserve für Schritt 2). Bei 4–5 Szenen pro Session also ~600–900 Wörter Handlungsablauf je Szene; bei 8–10 Szenen eher ~400–600. Wenn deutlich darüber, prüfen auf Doppelung oder unnötige Detail-Tiefe — die Grenze ist nicht starr, aber als Selbstkontrolle nützlich.

**Self-Review:** Prüfe jede Szene:
- Ist der Transkript-Auszug vollständig und korrekt zugeordnet?
- Deckt der Handlungsablauf alle Details aus Storyboard und Transkript ab?
- Sind alle Regel-Sprech-Begriffe (siehe oben) aus dem Handlungsablauf entfernt?
- Ist die Crew-Position konsistent mit der Vorszene?
- Wird Spekulation vermieden (keine erfundenen Motive, Hintergründe, "tiefen Bedeutungen")?

Dann vorlegen und auf Freigabe warten.

---

## Schritt 2: Szenen-Entwürfe (Prosa)

**Eingabe:** Szenen-Dateien aus `chronicle/02-szenen/`
**Ausgabe:** `chronicle/03-entwuerfe/kapitel-NN-szene-01-entwurf.md`, `kapitel-NN-szene-02-entwurf.md`, ...

Schreibe für jede Szene einen Prosa-Entwurf. **Jede Szene einzeln als eigene Datei**, damit sie unabhängig reviewt werden kann.

### Stilrichtlinien

Die bestehenden Kapitel in `chronicle/04-kapitel/` können als grobe Tonalitäts-Referenz dienen, aber jede neue Session darf ihren eigenen Ton finden — bitte nicht sklavisch imitieren. Wesentliche Merkmale, die durchgehalten werden sollen:

- **Sprache:** Deutsch, gehobener aber flüssiger Erzählstil. Keine übertriebene Poetik, sondern klare, bildhafte Prosa. Vorsicht mit Anglizismen — *devastierend* → *verheerend*, *automatisiert* sparsam einsetzen. Idiom-Akkuratesse: *in den Raum stellen* (nicht *legen*), *im Dunklen bleiben* (nicht *liegen*). Bei zeitlich realer Vergangenheit Indikativ statt Konjunktiv (*als sie noch gedacht hatten*, nicht *gedacht hätten*).
- **Perspektive:** Dritte Person, begrenzt allwissend – typischerweise aus der Perspektive eines der Spielercharaktere, kann zwischen Szenen wechseln.
- **Dialoge:** Wörtliche Rede in deutschen Anführungszeichen `„..."`. Dialoge sollen sich natürlich anfühlen und den Charakter der Sprecher widerspiegeln. Orientiere dich an Formulierungen aus dem Transkript, aber übersetze sie in den Erzählstil.
- **Keine Markdown-Formatierung im Roman-Text:** Italics (`*Wort*`) und Fettdruck (`**Wort**`) gehören nicht in die Prosa — sie passen nicht zum Roman-Satz. Konkret:
  - **Bildschirm-/Funk-Ausgaben** (Warnmeldungen, Datenbank-Anzeigen, automatisierte Durchsagen): in deutsche Anführungszeichen `„..."`, weil sie als zitierter Text Sinn machen.
  - **Telepathische Stimme / fremde Gedanken im Kopf:** ebenfalls in `„..."`, weil sie wie Rede behandelt werden.
  - **Innere Wahrnehmung / Gedanken:** als plain prose integriert, ohne typografische Auszeichnung. Beispiel: *„Tödliche Natur, hörte er in sich, nicht für Lebewesen geschaffen."* statt mit Italics.
  - **Akzent-Hervorhebungen einzelner Wörter:** ersatzlos streichen. Der Satzbau muss die Betonung tragen, nicht die Typografie. *„Eines hatten sie gekapert."* statt *„Sie *hatten* eines gekapert."*
- **Lesefluss: keine rückblickenden Meta-Sätze.** Wenn ein Satz erklärt, was der vorherige Satz schon gezeigt hat, ist er überflüssig. Cut-Kandidaten:
  - **Erklärungs-Satz nach Beschreibung:** *„Hinter der Silhouette stieg ein sonnenhelles Aufleuchten auf."* (die Reaktor-Explosion ist schon klar — ein nachfolgendes *„Der Reaktor war explodiert"* erklärt nur)
  - **Schlussfolgerung nach Dialog:** *„Mehr sagte Kaelum nicht. Aber es reichte, damit jeder im Schiff begriff..."* — Leser begreift selbst
  - **Bridge-Satz vor Action:** *„Er wusste sofort, was es bedeutete."* vor der Aktion streichen
  - **Closing-Coda am Szenenende:** *„Damit endete diese Nacht. Wo es sie hintragen würde, blieb offen."* — Szene endet bei Handlung/Bild, nicht bei Reflexion
  - **Einzelwort-Punktuation als Bridge:** *„Da."*, *„Endlich:"*, *„Zack."* — alles raus
  
  Erlaubt sind hingegen evokative Kurz-Sätze, die *vorwärts* treiben oder ein Bild setzen (*„Eine Schlacht."*, *„Eine Fliege zwischen zwei Titanen."*, *„Sie reagierte nicht."*). Faustregel: Wenn der Satz **erklärt**, raus. Wenn der Satz **zeigt**, bleibt.
- **Sensorische Erfahrung statt technischer Vermessung:** *„kaum mehr als schulterbreit"* statt *„1,30 bis 1,50 Meter breit"*. Konkrete Maße wirken im Roman wie Reisebericht. Wo immer möglich die erlebte Wirkung beschreiben (Enge, Höhe, Distanz als Körpergefühl), nicht den Zahlenwert.
- **Spielmechanik:** Würfelergebnisse und Regelmechaniken werden **nie** explizit erwähnt, sondern narrativ umgesetzt (z.B. ein hoher Investigation-Wurf wird zu einer detaillierten, scharfsinnigen Beobachtung). Das gilt auch für:
  - **Schadenspunkte:** Nie als Zahlen nennen ("19 Schadenspunkte"), sondern Wunden beschreiben ("drei Blastereinschläge brannten sich tief in seine Brust")
  - **Fähigkeitsnamen:** Nie Skill-/Feat-Namen wie "Critical Analysis", "Sneak Attack", "Evasive Footwork" verwenden, sondern das Verhalten narrativ beschreiben ("Ganden analysierte die Schwachstellen des Gegners", "Ghalrixtho nutzte die Ablenkung für einen präzisen Stich")
  - **Spielbegriffe:** Begriffe wie "Infiltrator", "NPC", "Hit Dice", "Saving Throw" gehören nicht in die Prosa. Verwende stattdessen narrative Beschreibungen ("schwer gerüsteter Soldat", "der Gepanzerte", "der Schütze")
- **Charakter-Hintergründe:** Die Charakterbögen in `background/charaktere/` enthalten Hintergrundwissen, das die Spielercharaktere **noch nicht voneinander kennen** (z.B. Gandens ISB-Vergangenheit). Solche Details dürfen in der Prosa nur dann auftauchen, wenn sie in einer Session explizit offenbart wurden. Im Zweifel: nicht erwähnen. Prüfe `background/charaktere/*.md` auf den Abschnitt "In der Kampagne bekannt" für bereits enthüllte Informationen.
- **Keine Species-Generalisierungen als Charakter-Begründung.** *„Devaronier waren klinisch — Varnira trug ihr Medpack wie eine zweite Haut"* ist schlecht, weil eine ganze Spezies pauschalisiert wird, um eine einzelne Figur zu erklären. Stattdessen das individuelle Verhalten zeigen: *„Varnira trug es immer bei sich, mit der Sorgfalt einer Frau, die mit dem Schlimmsten rechnete."*
- **Subtext statt Spoiler:** Wenn ein Charakter aus einer Perspektive geschrieben wird, dessen Hintergrund tiefer reicht als die Mitspieler-Charaktere ahnen, gilt: durch *Gewicht* andeuten, nicht durch *Inhalt* offenbaren. Beispiel: "Iego hat ihn geformt" — gut. "Er las das Vornesk-Dossier" — schlecht. Der Leser darf spüren, dass mehr dahinter steckt, ohne dass die Crew es erfahren würde. Die Tiefe wird durch Beziehung-zur-Sache vermittelt (Erinnerung, Reflex, Schweigen), nicht durch faktische Details.
- **Charakterstimmen:**
  - Ganden: kultiviert, analytisch, manipulativ-charmant, "der Professor"
  - Ghalrixtho: kühl, präzise, wenige Worte, raubtierhafte Präsenz
  - Komaru: pragmatisch, direkt, körperlich-dominant, trockener Humor
  - G4-X: mechanisch, pflichtbewusst
  - Varnira: sachlich, kompetent, vorbereitet
  - Kaelum: schweigsam, jung, brüchige Stimme bei emotionalen Auslösern; Anaxes als offene Wunde, die jederzeit aufbrechen kann; ringt um Kontrolle und scheitert manchmal; spürt Macht-Phänomene als zweite Schicht der Wirklichkeit
- **Atmosphäre:** Star-Wars-typisch – imperiale Bedrohung, Unterwelt-Flair, Frontier-Stimmung auf Lothal. Technische Details (Blaster, Repulsoren, Holoprojektoren) natürlich einstreuen.
- **Länge:** Szenen sollen ausführlich genug sein, um die Handlung lebendig zu machen, aber nicht aufgebläht. Orientierung: die bestehenden Kapitel liegen bei ca. 2500–5000 Wörtern (je nach Action-Dichte der Session); eine Einzelszene zielt grob auf 500–900 Wörter Prosa. Bei action-dichten Sessions mit 8+ Szenen kann das Kapitel deutlich länger werden — die Grenze ist nicht starr.

**Self-Review pro Szene:** Prüfe auf:
- Konsistenz mit den Quellen (Notizen, Transkript, Storyboard) – werden alle wesentlichen Handlungspunkte abgedeckt?
- Charakterstimmen – klingt jeder Charakter wie er selbst?
- **Markdown-Reste:** Italics (`*…*`) oder Bold (`**…**`) im Text? Sollte nicht vorhanden sein (außer als Cut-Kennzeichnung in TODOs).
- **Meta-Sätze:** Erklärt ein Satz, was der vorherige bereits gezeigt hat? Schneiden.
- **Einzelwort-Punktuation:** *„Da."*, *„Endlich:"*, *„Zack."* — schneiden.
- **Closing-Coda am Szenenende** (Reflexion, Aussicht, Zusammenfassung): schneiden — Szene endet bei Handlung/Bild.
- **Technische Vermessungen** statt sensorischer Erfahrung: umformulieren.
- **Species-Generalisierungen** als Charakter-Begründung: auf individuelles Verhalten umformulieren.
- **Anglizismen** (*devastierend*, *automatisiert*-überdosis): wo möglich durch deutsches Wort ersetzen.
- Überarbeite den Entwurf basierend auf dem Self-Review.

Dann vorlegen und auf Freigabe warten. **Jede Szene einzeln vorlegen** – nicht alle auf einmal.

---

## Schritt 3: Kapitel zusammenführen

**Eingabe:** Alle freigegebenen Szenen-Entwürfe
**Ausgabe:** `chronicle/04-kapitel/kapitel-NN.md`

1. Füge alle Szenen-Entwürfe in der richtigen Reihenfolge zu einem Kapitel zusammen.
2. Ergänze Übergänge zwischen den Szenen, wo nötig (Zeitsprünge, Ortswechsel).
3. **Doppelungen an Szenen-Grenzen straffen:** Beim getrennten Schreiben der Szenen rutschen oft Wiederholungen rein — z.B. eine Bedrohung, die am Ende von Szene N etabliert wird, taucht zu Beginn von Szene N+1 nochmal als Setup auf. Beim Mergen solche Doppelungen entfernen.
4. Erstelle den Kapitel-Header:

```markdown
# Kapitel NN – [Titel]

[Prosa-Text]

---

[← Kapitel NN-1](kapitel-NN-1.md)
```

5. Aktualisiere die Navigation im vorherigen Kapitel (füge Vorwärts-Link hinzu, falls nicht vorhanden).
6. Aktualisiere `chronicle/04-kapitel/README.md` – neuen Eintrag in die Inhaltsverzeichnis-Tabelle einfügen.

**Kapitel-Titel:** Leite einen kurzen, stimmungsvollen Titel ab, der das zentrale Thema oder Ereignis der Session einfängt (Beispiele: "Kollateralschäden", "Atmosphärische Störungen", "Letzte Nacht auf Lothal").

**Self-Review:** Lies das gesamte Kapitel am Stück. Prüfe:
- Lesen sich die Szenenübergänge flüssig?
- Gibt es Widersprüche oder Wiederholungen zwischen Szenen?
- Stimmt der Gesamtbogen?
- Hält die Prosa die Stilrichtlinien aus Schritt 2 durch (keine Markdown-Reste, keine Meta-Sätze, keine Game-Klassen)? Beim Mergen rutscht manchmal etwas durch, weil mehrere Szenen jetzt nebeneinanderstehen.
- Sind die Links korrekt (vorheriges Kapitel, README)?

Dann vorlegen und auf finale Freigabe warten.

---

## Nach Abschluss

Wenn das Kapitel final freigegeben ist:
- Bestätige, welche Dateien erstellt/geändert wurden.
- **Neue Lore-Elemente identifizieren:** Wenn in der Session neue Welt-Elemente, NPCs, Schauplätze, Technologien oder Setting-Konzepte eingeführt wurden, die bisher nicht in `background/bekannter-hintergrund.md` stehen (z.B. neuer Planet, neue Fraktion, neuer wichtiger NPC, neue Schiffs-Eigenschaft), liste sie dem Benutzer auf und schlage vor, sie in `bekannter-hintergrund.md` zu ergänzen — damit künftige Sessions die Lore-Konsistenz wahren können.
- **Neu entdeckte Whisper-Falschvarianten:** Falls beim Lesen des Transkripts Eigennamen-Falschschreibungen aufgetaucht sind, die noch nicht in `scripts/whisper-corrections.md` stehen, dem Benutzer dort eintragen vorschlagen.
- Schlage einen Commit vor (aber führe ihn nicht eigenständig aus).
