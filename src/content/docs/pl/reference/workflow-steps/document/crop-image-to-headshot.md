---
title: Krok Crop Image to Headshot
description: Przycinaj obrazy do kwadratowego zdjęcia portretowego w kroku przepływu pracy PlaidCloud, aby ujednolicić portrety w katalogach i identyfikatorach.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

Przycina obraz do wyśrodkowanego kwadratu i skaluje go do pliku JPEG o rozmiarze 500 × 500 pikseli. Przydatne do ujednolicania katalogów pracowników lub członków, w których zdjęcia źródłowe mają różne proporcje.

## Dane wejściowe

- **Plik lub katalog wejściowy** — obraz lub folder z obrazami na koncie dokumentów.
- **Plik lub katalog wyjściowy** — miejsce, w którym zapisywane jest zdjęcie portretowe.

## Dane wyjściowe

Plik JPEG 500 × 500 przycięty ze środka źródła. W przypadku folderu zdjęcie portretowe każdego pliku jest zapisywane w folderze nazwanym jak ścieżka wyjściowa, bez rozszerzenia.

## Uwagi

- Kadr jest brany ze środka obrazu; krok nie wyszukuje twarzy, więc kadruj zdjęcia źródłowe tak, aby fotografowana osoba znajdowała się pośrodku.
- Plik, którego nie można odczytać jako obrazu, jest kopiowany do danych wyjściowych bez zmian, zamiast powodować niepowodzenie kroku.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.
- Ścieżka wyjściowa nie może być ścieżką wejściową.

## Typowe zastosowania

- Ujednolicanie zdjęć w katalogu pracowników
- Generowanie spójnych awatarów dla wewnętrznego portalu
- Przycinanie zdjęć do identyfikatorów i poświadczeń

## Powiązane

- [Krok Convert PDF or Image to JPEG](/pl/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Krok Fix File Extension](/pl/reference/workflow-steps/document/fix-file-extension/)
