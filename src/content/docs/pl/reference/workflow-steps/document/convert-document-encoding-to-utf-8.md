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
- Plik skompresowany — na przykład plik zip, gzip lub bzip2 — jest najpierw rozpakowywany, a każdy znajdujący się w nim plik jest konwertowany.
- W przypadku folderu każdy plik jest konwertowany i zapisywany w miejscu docelowym pod własną nazwą. Zaznacz **Zachowaj podfoldery**, aby zamiast tego zapisać plik z podfolderu w odpowiadającym mu podfolderze miejsca docelowego; zawartość pliku skompresowanego trafia wtedy do podfolderu, w którym znajdował się ten plik skompresowany.
- Jeśli dwa pliki miałyby zostać zapisane w tym samym miejscu docelowym, krok kończy się niepowodzeniem przed zapisaniem drugiego, zamiast pozwolić mu zastąpić pierwszy. Komunikat podaje oba pliki, lub plik skompresowany, z którego pochodzą oba, oraz to miejsce; jeśli zaznaczenie **Zachowaj podfoldery** zapisałoby je w osobnych miejscach, komunikat o tym informuje.

## Przykłady

Wybierz plik wejściowy i wskaż plik w tej lokalizacji. Wybierz żądaną lokalizację wyjściową, a następnie wskaż w niej miejsce dla pliku. Zapisz i uruchom.
