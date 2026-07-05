import os
import argparse
import re

def parse_corrections(md_path):
    """Parses scripts/whisper-corrections.md and returns lists of (falsch, korrekt) replacements."""
    if not os.path.exists(md_path):
        print(f"[-] Korrekturdatei {md_path} nicht gefunden.")
        return [], []
        
    current_target = None
    replacements = []
    
    with open(md_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("### "):
                # Extract section target (e.g. "### Ghalrixtho")
                section_name = line[4:].strip()
                current_target = section_name.split('(')[0].strip()
            elif line.startswith("|") and line.endswith("|"):
                cells = [c.strip() for c in line.split('|')[1:-1]]
                if not cells:
                    continue
                # Skip separator/header lines
                if all(c.startswith("-") or c == "" for c in cells):
                    continue
                if any(h in cells[0].lower() for h in ["falschvariante", "falsche phrase"]):
                    continue
                    
                # Strip backticks
                cells = [c.replace('`', '') for c in cells]
                
                if len(cells) == 2:
                    falsch = cells[0]
                    if falsch and current_target:
                        replacements.append((falsch, current_target))
                elif len(cells) == 3:
                    falsch = cells[0]
                    korrekt = cells[1]
                    if falsch and korrekt:
                        replacements.append((falsch, korrekt))
                        
    # Separate phrases (containing space) and words (no space)
    phrases = []
    words = []
    for falsch, korrekt in replacements:
        if " " in falsch:
            phrases.append((falsch, korrekt))
        else:
            words.append((falsch, korrekt))
            
    # Sort by length of 'falsch' descending to avoid nested replacements breaking longer strings first
    phrases.sort(key=lambda x: len(x[0]), reverse=True)
    words.sort(key=lambda x: len(x[0]), reverse=True)
    
    return phrases, words

def apply_replacements(text, phrases, words):
    """Applies sorted phrase and word replacements to the text."""
    count = 0
    
    # 1. Phrases (multi-token)
    for falsch, korrekt in phrases:
        if falsch in text:
            occurrences = text.count(falsch)
            text = text.replace(falsch, korrekt)
            count += occurrences
            print(f"    [+] Ersetzt Phrase: '{falsch}' -> '{korrekt}' ({occurrences}x)")
            
    # 2. Words (single-token)
    for falsch, korrekt in words:
        if falsch in text:
            occurrences = text.count(falsch)
            text = text.replace(falsch, korrekt)
            count += occurrences
            print(f"    [+] Ersetzt Wort: '{falsch}' -> '{korrekt}' ({occurrences}x)")
            
    return text, count

def main():
    parser = argparse.ArgumentParser(description="Wendet Whisper-Namenskorrekturen auf ein Transkript an.")
    parser.add_argument('input', help="Pfad zum Eingabe-Transkript")
    parser.add_argument('-o', '--output', help="Pfad zum Ausgabe-Transkript (Standard: Eingabedatei überschreiben)")
    parser.add_argument('-c', '--corrections', default="scripts/whisper-corrections.md", help="Pfad zur Korrektur-Tabelle")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"[-] Eingabedatei nicht gefunden: {args.input}")
        return
        
    print(f"[+] Lade Korrekturen aus {args.corrections}...")
    phrases, words = parse_corrections(args.corrections)
    print(f"    - {len(phrases)} Phrasen geladen.")
    print(f"    - {len(words)} Wörter geladen.")
    
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
        
    print(f"\n[+] Wende Korrekturen auf {args.input} an...")
    corrected_content, total_changes = apply_replacements(content, phrases, words)
    
    output_path = args.output if args.output else args.input
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(corrected_content)
        
    print(f"\n[+] Korrektur abgeschlossen. {total_changes} Änderungen vorgenommen.")
    print(f"[+] Datei gespeichert unter: {output_path}")

if __name__ == "__main__":
    main()
