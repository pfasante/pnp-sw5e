# $HOME\whisper-env\Scripts\Activate.ps1

import argparse
import subprocess
import os
import csv
import datetime
import shutil

# --- Voreinstellungen ---
DEFAULT_MODEL = "large-v3"
DEFAULT_LANGUAGE = "German"
DEFAULT_OUTPUT = "star_wars_session_transcript.txt"

INITIAL_PROMPT = (
    "Das ist ein Transkript unserer Star Wars 5e Pen and Paper Rollenspiel Kampagne. "
    "Es wird jeweils die Audiospur eines Mitspielers transkribiert. Die Spieler Charaktere "
    "heißen Ganden Arvang, Komaru und Ghalrixtho, weitere auftauchende Charaktere sind "
    "Kaelum, G4-X, Varnira Sesh, Daro Fel und Rax Vonn. Korrigiere ggfs undeutlich "
    "ausgesprochene Namen dieser Charaktere."
)

def transcribe_file(audio_file, model):
    """Führt whisper-ctranslate2 für eine einzelne Datei aus."""
    print(f"\n[+] Transkribiere {audio_file} mit Modell '{model}'...")
    
    cmd = [
        "whisper-ctranslate2", audio_file,
        "--model", model,
        "--language", DEFAULT_LANGUAGE,
        "--output_format", "tsv",
        "--device", "cuda",
        "--compute_type", "bfloat16",  # Die Geheimwaffe für moderne RTX-Karten
        "--vad_filter", "True",
        "--condition_on_previous_text", "False",
        "--initial_prompt", INITIAL_PROMPT
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Transkription von {audio_file} abgeschlossen.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Fehler bei der Transkription von {audio_file}: {e}")
        raise

def merge_tsvs(tsv_files, output_file):
    """Führt die TSV-Dateien chronologisch zusammen."""
    print(f"\n[+] Füge folgende Spuren zusammen: {', '.join(tsv_files)}")
    all_lines = []

    for file in tsv_files:
        if not os.path.exists(file):
            print(f"[-] Warnung: Datei {file} nicht gefunden. Wird übersprungen.")
            continue
            
        speaker = os.path.splitext(os.path.basename(file))[0].capitalize()
        
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            for row in reader:
                # whisper-ctranslate2 kann start in ms oder sekunden (als float) ausgeben. 
                # Wir parsen es sicherheitshalber robust in Millisekunden.
                start_val = row['start']
                if '.' in start_val:
                    start_ms = int(float(start_val) * 1000)
                else:
                    start_ms = int(start_val)
                
                text = row['text'].strip()
                if text: # Leere Zeilen ignorieren
                    all_lines.append({
                        'start': start_ms, 
                        'speaker': speaker,
                        'text': text
                    })

    # Chronologisch sortieren
    all_lines.sort(key=lambda x: x['start'])

    with open(output_file, 'w', encoding='utf-8') as out:
        for line in all_lines:
            seconds = line['start'] // 1000
            hh = seconds // 3600
            mm = (seconds % 3600) // 60
            ss = seconds % 60
            timestamp = f"[{hh:02}:{mm:02}:{ss:02}]"
            out.write(f"{timestamp} {line['speaker']}: {line['text']}\n")
            
    print(f"[+] Zusammengeführtes Transkript gespeichert unter: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Star Wars 5e Transcription & Chronicle CLI")
    
    # Argumente definieren
    parser.add_argument('-a', '--audio', nargs='+', help="Liste der zu transkribierenden Audio-Dateien (z.B. benjamin.aac martin.aac)")
    parser.add_argument('-m', '--model', type=str, default=DEFAULT_MODEL, help=f"Whisper Modell (Standard: {DEFAULT_MODEL})")
    parser.add_argument('-M', '--merge-only', nargs='+', help="Überspringt Transkription und mergt nur die angegebenen TSV-Dateien")
    parser.add_argument('-o', '--output', type=str, default=DEFAULT_OUTPUT, help="Name der finalen Textdatei lokal")
    parser.add_argument('-c', '--cleanup', action='store_false', help="Löscht die TSV-Dateien nach erfolgreichem Zusammenfügen")

    args = parser.parse_args()

    tsv_files_to_merge = []

    # Schritt 1: Transkription (falls Audio-Dateien angegeben)
    if args.audio:
        for audio_file in args.audio:
            if os.path.exists(audio_file):
                transcribe_file(audio_file, args.model)
                base_name = os.path.splitext(audio_file)[0]
                tsv_files_to_merge.append(f"{base_name}.tsv")
            else:
                print(f"[-] Audio-Datei {audio_file} nicht gefunden.")
    
    # Oder: Nur Mergen (falls TSV-Dateien direkt angegeben wurden)
    elif args.merge_only:
        tsv_files_to_merge = args.merge_only
    
    else:
        print("[-] Weder Audio-Dateien (--audio) noch TSV-Dateien (--merge-only) angegeben. Nutze -h für Hilfe.")
        return

    # Schritt 2: Zusammenfügen
    if tsv_files_to_merge:
        merge_tsvs(tsv_files_to_merge, args.output)

    # Schritt 3: Cleanup
    if args.cleanup and tsv_files_to_merge:
        print("\n[+] Räume auf...")
        for tsv in tsv_files_to_merge:
            if os.path.exists(tsv):
                os.remove(tsv)
                print(f"    - Gelöscht: {tsv}")

if __name__ == "__main__":
    main()