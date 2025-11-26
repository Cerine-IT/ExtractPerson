# ExtractPerson

This project extracts person names from a text file using a custom dictionary.

## How it works
- The script (`extract.py`) loads a dictionary of full names from `Person.dic`.
- It scans the input text (`80_jours.txt`) for patterns matching "Firstname Lastname".
- Only names present in the dictionary are kept (case-insensitive, no duplicates).
- Results are written to `result_UTF8BOM.txt` (UTF-8 BOM encoding).

## Usage
1. Place your text file as `80_jours.txt` in the project folder.
2. Make sure your dictionary file is named `Person.dic` and uses UTF-16 LE encoding.
3. Run the script:
   ```bash
   python extract.py
   ```
4. Check the results in `result_UTF8BOM.txt`.

## Files
- `extract.py` : Main extraction script
- `Person.dic` : Dictionary of valid person names (UTF-16 LE)
- `80_jours.txt` : Input text file (UTF-16 LE)
- `result_UTF8BOM.txt` : Output file with extracted names

## Requirements
- Python 3.x

## Notes
- The script is designed for French texts but can be adapted.
- Only names with exactly one space (Firstname Lastname) are extracted.
- The dictionary can be customized for other texts or languages.

## License
MIT
