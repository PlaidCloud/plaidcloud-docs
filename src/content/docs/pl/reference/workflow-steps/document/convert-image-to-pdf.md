---
title: Krok Convert Image to PDF
description: Konwertuj pliki obrazów na dokumenty PDF w kroku przepływu pracy PlaidCloud, aby uzyskać ujednolicone dane wyjściowe i formaty gotowe do archiwizacji.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

Zamienia obraz (PNG, GIF, TIFF, JPEG lub HEIC) w jednostronicowy plik PDF albo dopasowuje istniejący plik PDF do standardowego rozmiaru strony.

## Dane wejściowe

- **Plik lub katalog wejściowy** — obraz lub plik PDF albo folder z nimi na koncie dokumentów.
- **Miejsce docelowe** — miejsce, w którym zapisywany jest plik PDF.
- **Rozmiar strony** — US Letter, US Legal, A3, A4 lub A5.
- **Kompresja** — **Lossy** zmniejsza obrazy do rozdzielczości ekranowej i może radykalnie zmniejszyć plik; **Lossless**, wartość domyślna, zachowuje dane obrazu dokładnie.

## Jak to działa

- Obraz jest umieszczany na stronie wybranego rozmiaru i skalowany tak, aby mieścił się na niej bez zmiany proporcji. Obraz z wieloma stronami lub klatkami, taki jak zeskanowany plik TIFF, jest konwertowany od pierwszej.
- Przy **Lossy** wynik jest następnie kompresowany, a wejściowy plik PDF jest dopasowywany do wybranego rozmiaru strony podczas kompresji.
- Przy **Lossless** wejściowy plik PDF jest przekazywany bez zmian i zachowuje własny rozmiar strony.

## Dane wyjściowe

Jeden plik PDF na plik wejściowy. W przypadku folderu plik PDF każdego pliku jest zapisywany w folderze nazwanym jak miejsce docelowe, bez rozszerzenia, pod własną nazwą pliku źródłowego. Aby połączyć kilka plików w jeden dokument, użyj po tym kroku [kroku Merge Multiple PDFs](/pl/reference/workflow-steps/document/merge-multiple-pdfs/).

## Uwagi

- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.
- Miejsce docelowe nie może być ścieżką wejściową.

## Typowe zastosowania

- Ujednolicanie obrazów paragonów lub faktur do formatu archiwalnego
- Przygotowanie materiałów obrazowych dla systemów, które przyjmują tylko pliki PDF

## Powiązane

- [Krok Convert PDF or Image to JPEG](/pl/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Krok Compress PDF](/pl/reference/workflow-steps/document/compress-pdf/)
- [Krok Merge Multiple PDFs](/pl/reference/workflow-steps/document/merge-multiple-pdfs/)
