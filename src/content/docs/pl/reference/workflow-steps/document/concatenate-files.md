---
title: Krok Concatenate Files
description: Łącz wiele plików w jeden plik w kroku przepływu pracy PlaidCloud, aby scalać dane wyjściowe w formie tekstowej, CSV lub innych dokumentów.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

Łączy dwa lub więcej plików na koncie dokumentów w jeden plik wyjściowy. Działa bajt po bajcie — przydatne dla formatów tekstowych (CSV, pliki dziennika, JSON Lines), w których proste złączenie daje poprawny wynik.

## Dane wejściowe

- **Pliki źródłowe** — lista plików do połączenia, w kolejności
- **Ścieżka wyjściowa** — miejsce docelowe połączonego pliku
- **Separator** — opcjonalna sekwencja bajtów wstawiana między pliki źródłowe (zwykle znak nowego wiersza)

## Dane wyjściowe

Pojedynczy plik zawierający zawartość wszystkich plików źródłowych w podanej kolejności, połączoną skonfigurowanym separatorem.

Plik źródłowy, który nie istnieje, jest pomijany w połączonym pliku, a krok kończy się ostrzeżeniem wskazującym go, więc przepływ pracy jest kontynuowany.

## Typowe zastosowania

- Łączenie dziennych plików dziennika w archiwum miesięczne
- Scalanie plików CSV o tym samym schemacie (usuń nagłówki ze wszystkich poza pierwszym)
- Łączenie eksportów JSON Lines z wielu źródeł przed przetwarzaniem

## Nie nadaje się do

- Plików PDF — użyj zamiast tego [kroku Merge Multiple PDFs](/pl/reference/workflow-steps/document/merge-multiple-pdfs/)
- Formatów binarnych z nagłówkami (XLSX, ZIP, pliki obrazów) — łączenie bajtów nie da poprawnego pliku

## Powiązane

- [Krok Merge Multiple PDFs](/pl/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Przewodnik po dokumentach](/pl/guides/documents/)
