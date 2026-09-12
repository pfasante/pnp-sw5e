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
| Galrixtor | S20 |
| Galrix | S19 |
| Galrixo | S19 |
| Galrixus | S19 |
| Galrixtus | S19 |
| GALRIXO | S19 |
| Galrixdo | S19 |
| Gal Rigstow | S20 |
| Geirikstu | S20 |
| Pascal Rix | S20 |
| Garrixo | S20 |
| Gerrixo | S20 |
| Ghalrixtho 2 | S20 |
| Galeristo | S20 |
| galeristo | S20 |
| Rexo | S22 |
| rexo | S22 |
| Garrixto | S23 |
| Grixo | S23 |
| Rixxo | S23 |
| Rixlos | S23 |
| Rixlo | S23 |
| Garrix | S23 |
| Ghalrixthothor | S23 |
| Galerikstow | S23 |
| Karikso | S23 |

Phrasen-Fehler (mehrere Tokens — exakte Phrase ersetzen, nicht
Einzelwort):

| Falsche Phrase | Korrekt | Erstmals |
|----------------|---------|----------|
| `Geil, Rickstu.` | `Ghalrixtho.` | S19 |
| `Kai Rixtho` | `Ghalrixtho` | S19 |
| `Karl Rixlo` | `Ghalrixtho` | S23 |
| `der Rixlos` | `von Ghalrixtho` | S23 |
| `Karl-Rix Tog` | `Ghalrixtho` | S23 |
| `geil, Rexto` | `geil, Ghalrixtho` | S23 |
| `Karl Ghalrixtho` | `Ghalrixtho` | S23 |

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
| Kelloman | S23 |
| Kalium | S23 |
| Carolyn | S23 |

### Komaru

| Falschvariante | Erstmals |
|----------------|----------|
| Komaro | S19 |
| Komago | S22 |
| komago | S22 |
| Komaho | S23 |

### Dr. Rath

| Falschvariante | Erstmals |
|----------------|----------|
| Amok Rath | S20 |
| Dr. Rathbun | S20 |
| Dr. Raab | S20 |
| Dr. Raph | S23 |
| Dr. Rapp | S23 |
| Dr. Raff | S23 |
| Doktor Rat | S23 |

### Ganden

Hinweis: Eine einzelne `Ganten → Ganden`-Ersetzung deckt auch zusammen-
gesetzte Formen wie `Gantens`, `Gantenhirnwurf` automatisch ab, weil das
Suffix unverändert bleibt.

| Falschvariante | Erstmals |
|----------------|----------|
| Ganten | S19 |
| Dr. Havang | S20 |
| Gampens | S20 |
| Gundon | S23 |
| Ganon | S23 |
| Skandin | S23 |
| Gantons | S23 |
| Ganzen | S23 |

### Varnira

| Falschvariante | Erstmals |
|----------------|----------|
| Warnira | S19 |
| Vanira | S19 |
| Vanya | S20 |
| Dr. Sash | S20 |
| Sash | S23 |
| Varnierer | S20 |
| Warnierer | S20 |
| Vanirer | S20 |
| vanirer | S20 |
| Vanir | S23 |

| Falsche Phrase | Korrekt | Erstmals |
|----------------|---------|----------|
| `die Baronierin` | `die Devaronierin` | S23 |

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

### Captain Cassandra Nero

| Falschvariante | Erstmals |
|----------------|----------|
| Captain Arrow | S23 |
| Captain Eroar | S23 |

---

## Star-Wars-Setting-Begriffe

Eigennamen aus dem Star-Wars-Universum (keine Charaktere), die Whisper
systematisch zu deutsch klingenden Wörtern verschiebt.

### corellianisch (Adjektiv, von Corellia)

Beschreibt z.B. die Bauart der Turbot.

| Falschvariante | Erstmals |
|----------------|----------|
| koreanisch | S19 |
| korinianische | S20 |
| korallianischen | S20 |

### huttisch (Adjektiv, von Hutten)

| Falschvariante | Erstmals |
|----------------|----------|
| ruttischer | S20 |

### Iego (Planet)

| Falschvariante | Erstmals |
|----------------|----------|
| Jego | S20 |
| IEGO | S20 |

### Turbot (Schiff)

| Falschvariante | Erstmals |
|----------------|----------|
| Turbid | S20 |
| Turbid-Extraktion | S20 |
| Törwort | S20 |

### die Brill (Schiff)

| Falschvariante | Erstmals |
|----------------|----------|
| Debril | S20 |

### Xandus (Flugwesen)

| Falschvariante | Erstmals |
|----------------|----------|
| Xandos | S20 |
| Xandros | S20 |

### Klippenhorst (Ort)

| Falschvariante | Erstmals |
|----------------|----------|
| Clipmores | S23 |
| Flippenhorst | S23 |

### Lothal (Planet)

| Falschvariante | Erstmals |
|----------------|----------|
| Lothar | S23 |

### Arkania (Planet)

| Falschvariante | Erstmals |
|----------------|----------|
| Arcanes | S23 |

### Korriban (Planet)

| Falschvariante | Erstmals |
|----------------|----------|
| Korribanen | S23 |

### Ausrüstung & Spielbegriffe

| Falschvariante / Phrase | Korrekt | Erstmals |
|-------------------------|---------|----------|
| `Sleißer-Skate` | `Slicer-Kit` | S23 |
| `Libro-Klinge` | `Vibro-Klinge` | S23 |
| `Libro-Dagger` | `Vibro-Dagger` | S23 |
| `Eight of Hand` | `Sleight of Hand` | S23 |
| `Tag Override` | `Tech Override` | S23 |
| `Sturzzeichen` | `Schriftzeichen` | S23 |
| `Kuhien` | `Kojen` | S23 |

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
