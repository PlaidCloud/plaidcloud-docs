---
title: Krok Convert Document Encoding to UTF-16
description: Konwertuj kodowanie pliku dokumentu na UTF-16 w kroku przepływu pracy PlaidCloud, aby obsługiwać wielobajtowe zestawy znaków i tekst Unicode.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## Opis

Zapisuje plik tekstowy od nowa w UTF-16. Przydatne, gdy system docelowy wymaga UTF-16 lub gdy źródło miesza kodowania, które odrzucają inne narzędzia.

## Dane wejściowe

- **Plik lub katalog wejściowy** — plik tekstowy lub folder plików tekstowych do konwersji.
- **Miejsce docelowe** — miejsce, w którym zapisywany jest przekonwertowany plik.
- **Kompresja** — Bez kompresji, Zip, GZip lub BZip2 dla danych wyjściowych.
- **Kolejność bajtów (endianness)** — Little endian lub Big endian.
- **Include BOM** — zaznacz, aby plik zaczynał się znacznikiem kolejności bajtów (`FF FE` dla little endian, `FE FF` dla big endian). Pozostaw niezaznaczone, aby nie dodawać znacznika.

## Jak to działa

- Wykrywane jest kodowanie źródła. Plik UTF-8 jest odczytywany jako UTF-8, a znaki Windows wklejone do takiego pliku — na przykład zakrzywione cudzysłowy z Worda lub Excela — są zachowywane bez zmian, niezależnie od ich liczby. Plik w innym kodowaniu jest odczytywany w kodowaniu wykrytym na podstawie jego pierwszej części, która nie jest poprawnym UTF-8.
- Tekst jest zapisywany bez zmian — litery z akcentami, symbole i inne znaki są zachowane dokładnie tak, jak były.
- Plik, którego kodowania nie można wykryć, powoduje niepowodzenie kroku z podaniem pliku.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.
- W przypadku folderu każdy plik jest konwertowany i zapisywany w miejscu docelowym pod własną nazwą. Pliki z podfolderów są zapisywane bezpośrednio w miejscu docelowym, a nie w odpowiadających podfolderach.

## Przykłady

Wybierz plik wejściowy i wskaż plik w tej lokalizacji. Wybierz żądaną lokalizację wyjściową, wybierz kolejność bajtów i zaznacz **Include BOM**, jeśli system odbierający tego oczekuje. Zapisz i uruchom.
