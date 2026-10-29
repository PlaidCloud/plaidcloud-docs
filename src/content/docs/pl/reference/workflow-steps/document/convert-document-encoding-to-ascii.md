---
title: Krok Convert Document Encoding to ASCII
description: Konwertuj kodowanie pliku dokumentu na ASCII w kroku przepływu pracy PlaidCloud, aby zapewnić zgodność z systemami wymagającymi tekstu ASCII.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-ascii.md
---

## Opis

Zapisuje plik tekstowy od nowa jako zwykły ASCII. Jest to szczególnie przydatne, gdy źródło informacji ma mieszane kodowania lub inne narzędzia nie obsługują niektórych kodowań.

## Jak to działa

- Wykrywane jest kodowanie źródła. Plik UTF-8 jest odczytywany jako UTF-8, a znaki Windows wklejone do takiego pliku — na przykład zakrzywione cudzysłowy z Worda lub Excela — są zachowywane bez zmian, niezależnie od ich liczby. Plik w innym kodowaniu jest odczytywany w kodowaniu wykrytym na podstawie jego pierwszej części, która nie jest poprawnym UTF-8.
- Litery z akcentami zachowują literę bazową (`café` staje się `cafe`), a znaki bez odpowiednika w ASCII są pomijane.
- Wiersz zawierający tylko cudzysłów jest dołączany do końca poprzedniego wiersza.
- Plik, którego kodowania nie można wykryć, powoduje niepowodzenie kroku z podaniem pliku.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.

## Przykłady

Wybierz plik wejściowy i wskaż plik w tej lokalizacji. Wybierz żądaną lokalizację wyjściową i wskaż w niej miejsce dla pliku. Zapisz i uruchom.
