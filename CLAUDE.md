# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **pen-and-paper campaign repository** for a Star Wars 5e (SW5e) campaign called "Echoes of the Empire." It contains session notes, audio transcriptions, character sheets, and a prose chronicle — all in German. There is minimal code; the primary content is structured Markdown.

## Repository Structure

- `sessions/YYYY-MM-DD_session-NN/` — Per-session notes (`notes.md`) and transcriptions (`.tsv` per speaker + merged `.txt`)
- `chronicle/` — Prose chronicle workbench with pipeline: `01-storyboard/` → `02-szenen/` → `03-entwuerfe/` → `04-kapitel/` (final chapters)
- `background/` — Player-known lore (`bekannter-hintergrund.md`) and character sheets in `charaktere/`
- `scripts/` — Python tooling (currently just `transcribe_merge.py`)

## Commands

```bash
# Install dependencies (requires uv)
uv sync

# Transcribe audio files (requires NVIDIA GPU with CUDA)
cd sessions/YYYY-MM-DD_session-NN/transcriptions
uv run python ../../../scripts/transcribe_merge.py \
  --audio andreas.aac benjamin.aac martin.aac friedrich.aac \
  --output transkript_YYYY-MM-DD.txt

# Merge existing TSVs only (no re-transcription)
uv run python ../../../scripts/transcribe_merge.py \
  --merge-only andreas.tsv benjamin.tsv martin.tsv friedrich.tsv \
  --output transkript_YYYY-MM-DD.txt
```

## Key Technical Details

- **Python ≥ 3.11**, managed with [uv](https://docs.astral.sh/uv/). No pip/venv — always use `uv sync` and `uv run`.
- **`uv.lock` is committed** for reproducible builds. `.venv/` is gitignored.
- Audio files (`.aac`, `.wav`, `.zip`) are **gitignored** — never commit them.
- The transcription script uses `whisper-ctranslate2` with model `large-v3`, language German, CUDA `bfloat16`.
- TSV files are deleted after merge by default; use `--keep-tsvs` to retain them.

## Content Conventions

- All prose and notes are written in **German**.
- Session folders follow the naming pattern `YYYY-MM-DD_session-NN/`.
- Chronicle chapters: `chronicle/04-kapitel/kapitel-NN.md`. Chapters 1–12 are not yet written as prose; the chronicle starts at chapter 13.
- Chronicle workbench file naming: `session-NN-storyboard.md`, `session-NN-szene-NN.md`, `kapitel-NN-szene-NN-entwurf.md`.
- Player characters: Ghalrixtho (Chiss Operative), Ganden Arvang (Human Tactician Scholar), Komaru (Togorian Scout), G4-X (Droid Fighter), Varnira Sesh (Devaronian Engineer).
