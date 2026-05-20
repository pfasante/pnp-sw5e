# Whisper-Transkriptions-Korrekturen

Bekannte Falschvarianten der Charakter- und NPC-Namen, die
`whisper-ctranslate2` bei deutschen Audio-Spuren systematisch produziert.
Diese Liste wird über die Kampagne hinweg gepflegt — neue Falscherkennungen
aus jeder Session werden hier nachgetragen.

**Verwendung:** Nach `transcribe_merge.py` das gemergte Transkript gegen
diese Liste prüfen und durch Editor- oder `sed`-Replacement korrigieren.
Reihenfolge beachten (siehe unten).

---

## Spielercharaktere

### Ghalrixtho

| Falschvariante | Erstmals |
|----------------|----------|
| Galrixto | S19 |
| Galrix | S19 |
| Galrixo | S19 |
| Galrixus | S19 |
| Galrixtus | S19 |
| GALRIXO | S19 |
| Galrixdo | S19 |

Phrasen-Fehler (mehrere Tokens — exakte Phrase ersetzen, nicht
Einzelwort):

| Falsche Phrase | Korrekt | Erstmals |
|----------------|---------|----------|
| `Geil, Rickstu.` | `Ghalrixtho.` | S19 |
| `Kai Rixtho` | `Ghalrixtho` | S19 |

### Kaelum

| Falschvariante | Erstmals |
|----------------|----------|
| Calum | S19 |
| Kelum | S19 |
| Callum | S19 |
| Kalum | S19 |
| Kellum | S19 |
| Caelum | S19 |
| Herrlund | S19 |

### Komaru

| Falschvariante | Erstmals |
|----------------|----------|
| Komaro | S19 |

### Ganden

Hinweis: Eine einzelne `Ganten → Ganden`-Ersetzung deckt auch zusammen-
gesetzte Formen wie `Gantens`, `Gantenhirnwurf` automatisch ab, weil das
Suffix unverändert bleibt.

| Falschvariante | Erstmals |
|----------------|----------|
| Ganten | S19 |

### Varnira

| Falschvariante | Erstmals |
|----------------|----------|
| Warnira | S19 |
| Vanira | S19 |

### G4-X

**Vorsicht:** Diese kurzen Tokens können theoretisch auch legitime deutsche
Wörter / Eigennamen sein (Plural von "Gag" usw.). Vor Bulk-Replace stich-
probenartig die Kontexte prüfen, idealerweise auf GM-/Sprecher-Linien
beschränken.

| Falschvariante | Erstmals |
|----------------|----------|
| Gags | S19 |
| Gax | S19 |
| Gex | S19 |

---

## NPCs

### Daro Fel

| Falschvariante | Erstmals |
|----------------|----------|
| Darufell | S19 |

---

## Star-Wars-Setting-Begriffe

Eigennamen aus dem Star-Wars-Universum (keine Charaktere), die Whisper
systematisch zu deutsch klingenden Wörtern verschiebt.

### corellianisch (Adjektiv, von Corellia)

Beschreibt z.B. die Bauart der Turbot.

| Falschvariante | Erstmals |
|----------------|----------|
| koreanisch | S19 |

---

## Bulk-Replace: empfohlene Reihenfolge

1. **Mehr-Token-Phrasen zuerst** (z.B. `Geil, Rickstu.`) — wortgrenzen-
   übergreifende Fehler werden durch spätere Einzelersetzungen nicht
   gefunden.
2. **Längere Substrings vor kürzeren** (z.B. `Galrixtus` vor `Galrix`),
   sonst zerlegen kurze Ersetzungen die längeren in Müll.
3. **Case-Varianten beachten** — `GALRIXO` separat von `Galrixo` ersetzen,
   da Editor-`replace_all` standardmäßig case-sensitive arbeitet.
4. **Reste-Scan** zum Abschluss mit
   ```
   grep -niE "galrix|calum|kelum|callum|kalum|kellum|caelum|herrlund|komaro|ganten|warnira|vanira|gags|gax|gex|darufell"
   ```
   um Übersehenes zu erwischen.
5. **Breitsuche** auf Charakter-Stämme zur Erkennung von Halluzinationen:
   ```
   grep -oiE "\b[kc]a?e?l[lu]?u?m\w*"   # alle Kaelum-Varianten
   grep -oiE "\w*galrix\w*"             # alle Ghalrixtho-Varianten
   ```

## Neue Varianten dokumentieren

Wenn beim Korrekturlauf einer Session neue Whisper-Fails auftauchen:

- In die passende Tabelle eintragen, Session-Nummer als Quelle vermerken.
- Bei Phrasen-Fehlern (mehrere Tokens): die **exakte Wortfolge** als
  `vorher → korrekt` notieren, nicht nur Einzelwörter.
- Bei mehrdeutigen kurzen Tokens: explizit einen Vorsicht-Hinweis
  ergänzen.

## Verbindung zum Transkriptions-Skript

`scripts/transcribe_merge.py` reicht via `--initial_prompt` einen
Whisper-Prompt durch, der alle kanonischen Eigennamen mit Spezies-Hinweis
enthält (Konstante `INITIAL_PROMPT`). Dadurch sollte die Liste oben über
die Zeit *schrumpfen*, nicht wachsen.

**Wenn ein neuer Eigenname in die Kampagne kommt** (neuer PC, wichtiger
NPC), muss er an zwei Stellen ergänzt werden:

1. Hier in `whisper-corrections.md` — zumindest als Stub, sobald die
   erste Falschvariante auftaucht.
2. In der `INITIAL_PROMPT`-Konstante in `transcribe_merge.py` — bevor
   die nächste Session transkribiert wird, damit Whisper den Namen
   gleich richtig schreibt.
