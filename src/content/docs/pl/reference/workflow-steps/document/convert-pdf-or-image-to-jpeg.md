---
title: Krok Convert PDF or Image to JPEG
description: Konwertuj strony PDF lub obrazy do formatu JPEG w kroku przepływu pracy PlaidCloud, aby uzyskać dane wyjściowe zgodne z siecią web i przetwarzać obrazy.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

Konwertuje plik PDF lub obraz na JPEG. Pierwsza strona pliku PDF staje się plikiem JPEG; obraz jest kodowany od nowa, a obraz z wieloma stronami lub klatkami, taki jak zeskanowany plik TIFF, jest konwertowany od pierwszej.

## Dane wejściowe

- **Plik lub katalog wejściowy** — plik PDF lub obraz (PNG, GIF, TIFF, JPEG lub HEIC) albo folder z nimi na koncie dokumentów.
- **Plik lub katalog wyjściowy** — miejsce, w którym zapisywany jest plik JPEG.

## Dane wyjściowe

Jeden plik JPEG na plik wejściowy. W przypadku folderu plik JPEG każdego pliku jest zapisywany w folderze nazwanym jak ścieżka wyjściowa, bez rozszerzenia, pod własną nazwą pliku źródłowego.

## Uwagi

- Plik dowolnego innego typu powoduje niepowodzenie kroku z wymienieniem akceptowanych typów.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.
- Ścieżka wyjściowa nie może być ścieżką wejściową.

## Typowe zastosowania

- Generowanie obrazów podglądu do wyświetlania w sieci web
- Tworzenie wersji plików PDF wyłącznie w postaci obrazów dla systemów, które nie obsługują PDF

## Powiązane

- [Krok Convert Image to PDF](/pl/reference/workflow-steps/document/convert-image-to-pdf/)
- [Krok Compress PDF](/pl/reference/workflow-steps/document/compress-pdf/)
- [Krok Crop Image to Headshot](/pl/reference/workflow-steps/document/crop-image-to-headshot/)
