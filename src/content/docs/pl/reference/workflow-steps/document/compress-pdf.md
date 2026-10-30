---
title: Krok Compress PDF
description: Kompresuj pliki PDF w kroku przepływu pracy PlaidCloud, aby zmniejszyć rozmiar pliku przy zachowaniu jakości dokumentu i oszczędności miejsca.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

Zmniejsza rozmiar pliku PDF przechowywanego na koncie dokumentów. Przydatne do zmniejszania dużych zeskanowanych dokumentów przed archiwizacją, dołączeniem do powiadomień lub przeniesieniem między kontami dokumentów.

## Dane wejściowe

- **Plik lub katalog wejściowy** — plik PDF lub folder z plikami PDF na koncie dokumentów.
- **Plik lub katalog wyjściowy** — miejsce, w którym zapisywany jest skompresowany plik PDF.

## Jak to działa

Plik PDF jest zapisywany od nowa, a jego obrazy są zmniejszane do rozdzielczości ekranowej (72 dpi), natomiast czcionki są osadzane jako podzbiory, co może radykalnie zmniejszyć zeskanowane dokumenty; tekst pozostaje ostry. Strony są dopasowywane do rozmiaru US Letter.

## Dane wyjściowe

Skompresowany plik PDF w ścieżce wyjściowej. W przypadku folderu każdy plik PDF jest zapisywany poniżej ścieżki wyjściowej, z zachowaniem swojego położenia względem folderu wejściowego.

## Uwagi

- Ścieżka wyjściowa nie może być ścieżką wejściową, więc źródło nigdy nie jest nadpisywane.
- Jeśli ścieżka wejściowa nie istnieje lub nie zawiera plików, krok kończy się ostrzeżeniem wskazującym ścieżkę, nic nie przetwarza, a przepływ pracy jest kontynuowany.
- Plik PDF, którego nie można skompresować, powoduje niepowodzenie kroku z podaniem pliku i przyczyny.

## Typowe zastosowania

- Zmniejszanie zeskanowanych faktur, paragonów lub umów przed długoterminowym przechowywaniem
- Zmniejszanie rozmiaru plików PDF przed wysłaniem e-mailem lub dołączeniem do powiadomień
- Przygotowanie dokumentów do przesłania do systemów docelowych o ograniczonym rozmiarze

## Powiązane

- [Krok Convert PDF or Image to JPEG](/pl/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Krok Merge Multiple PDFs](/pl/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Przewodnik po dokumentach](/pl/guides/documents/)
