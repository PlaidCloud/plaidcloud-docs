---
title: Krok Convert Document Encoding to UTF-8
description: Konwertuj kodowanie pliku dokumentu na UTF-8 w kroku przepływu pracy PlaidCloud, aby zapewnić szeroką zgodność z nowoczesnymi systemami i aplikacjami.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## Opis

Zapisuje plik tekstowy od nowa w UTF-8. Jest to szczególnie przydatne, gdy źródło informacji ma mieszane kodowania lub inne narzędzia nie obsługują niektórych kodowań.

## Jak to działa

- Wykrywane jest kodowanie źródła. Plik UTF-8 jest odczytywany jako UTF-8, a znaki Windows wklejone do takiego pliku — na przykład zakrzywione cudzysłowy z Worda lub Excela — są zachowywane bez zmian, niezależnie od ich liczby. Plik w innym kodowaniu jest odczytywany w kodowaniu wykrytym na podstawie jego pierwszej części, która nie jest poprawnym UTF-8.
- Tekst jest zapisywany bez zmian — litery z akcentami, symbole i inne znaki są zachowane dokładnie tak, jak były.
- Plik, którego kodowania nie można wykryć, powoduje niepowodzenie kroku z podaniem pliku.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.

## Przykłady

Wybierz plik wejściowy i wskaż plik w tej lokalizacji. Wybierz żądaną lokalizację wyjściową, a następnie wskaż w niej miejsce dla pliku. Zapisz i uruchom.
