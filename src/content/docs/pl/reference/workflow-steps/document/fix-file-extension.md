---
title: Fix File Extension (krok)
description: Popraw rozszerzenia plików w kroku przepływu pracy PlaidCloud, wykrywając rzeczywisty typ pliku i zmieniając nazwę na właściwe rozszerzenie.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

Odczytuje, co plik faktycznie zawiera, i tam, gdzie przeczy to jego rozszerzeniu, zmienia nazwę na rozszerzenie, które zwykle nosi ten typ — plik PDF zapisany jako `.dat` staje się `.pdf`. Przydatne, gdy system źródłowy przekazuje pliki z błędnymi lub brakującymi rozszerzeniami.

## Dane wejściowe

- **Plik lub katalog wejściowy** — plik albo folder, którego pliki są sprawdzane po kolei, na koncie dokumentów. Nazwy plików są zmieniane w miejscu, więc nie ma lokalizacji wyjściowej.

## Jak to działa

Krok rozpoznaje typ każdego pliku na podstawie jego zawartości i zmienia nazwę pliku tylko wtedy, gdy jego obecnej nazwie brakuje rozszerzenia, ma rozszerzenie zastępcze (`.dat`, `.tmp` lub `.bin`) albo wskazuje inny typ, który krok rozpoznaje.

Rozpoznawane typy to PDF; obrazy JPEG, PNG, GIF, TIFF, BMP, WebP i HEIC; dokumenty Excel (`.xlsx`, `.xls`), Word (`.docx`, `.doc`) i PowerPoint (`.pptx`); archiwa ZIP i GZip oraz CSV, JSON, HTML, XML i zwykły tekst.

Plik zachowuje nazwę, gdy:

- jego rozszerzenie już pasuje do zawartości — `.jpg` i `.jpeg` pasują do JPEG, a `.tif` i `.tiff` do TIFF;
- jego rozszerzenie nie jest rozpoznawane przez krok, na przykład `.sql`, `.log` lub `.ai`, ponieważ sama zawartość nie pozwala odróżnić skryptu SQL od innego tekstu ani pliku Illustratora od PDF;
- zawiera zwykły tekst pod rozszerzeniem tekstowym, takim jak `.csv`, `.tsv` lub `.json`;
- zawiera jeden format tekstowy pod rozszerzeniem innego — XML w pliku `.html`, CSV w pliku `.json` — ponieważ zawartość nie pozwala wiarygodnie ich rozróżnić. Tylko plik `.txt` lub plik bez rozszerzenia albo z rozszerzeniem zastępczym otrzymuje nazwę w formacie tekstowym;
- jest plikiem ZIP nazwanym jak dokument pakietu Office, ponieważ pliki `.xlsx`, `.docx` i `.pptx` w środku są plikami ZIP;
- jego typu nie można ustalić, jak w przypadku pustego pliku.

Archiwum jest oceniane według własnej zawartości: jego elementy nie są otwierane ani przemianowywane. Pliki, których nazwy zaczynają się od `.`, są pomijane.

## Przykłady

| Plik | Zawartość | Wynik |
|---|---|---|
| `invoice.dat` | PDF | zmieniono nazwę na `invoice.pdf` |
| `photo.png` | JPEG | zmieniono nazwę na `photo.jpg` |
| `export.txt` | CSV | zmieniono nazwę na `export.csv` |
| `readme` | zwykły tekst | zmieniono nazwę na `readme.txt` |
| `query.sql` | zwykły tekst | bez zmian |
| `budget.xlsx` | ZIP | bez zmian |

## Uwagi

- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem ze wskazaniem ścieżki, niczego nie przetwarza, a przepływ pracy jest kontynuowany.

## Powiązane

- [Concatenate Files (krok)](/pl/reference/workflow-steps/document/concatenate-files/)
- [Przewodnik po dokumentach](/pl/guides/documents/)
