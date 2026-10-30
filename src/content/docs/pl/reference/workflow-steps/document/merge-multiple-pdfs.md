---
title: Merge Multiple PDFs (krok)
description: Scal wiele plików PDF w jeden dokument w kroku przepływu pracy PlaidCloud, aby składać i konsolidować raporty.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

Łączy pliki PDF z folderu w jeden plik PDF. W odróżnieniu od kroku [Concatenate Files (krok)](/pl/reference/workflow-steps/document/concatenate-files/) ten krok rozumie format PDF i tworzy poprawny scalony dokument.

## Dane wejściowe

- **Katalog wejściowy** — folder, którego pliki PDF są scalane, na koncie dokumentów. Można podać zamiast tego pojedyncze archiwum, takie jak plik ZIP z plikami PDF, a scalane są pliki PDF w jego wnętrzu.
- **Wyjściowy plik scalony** — miejsce zapisu scalonego pliku PDF.

## Jak to działa

- Pliki PDF są scalane w kolejności ich ścieżek, z liczbami traktowanymi według wartości — `page2.pdf` jest przed `page10.pdf` — więc numeruj je, aby sterować kolejnością. Każdy zachowuje własne strony w ich kolejności.
- Scalane są tylko pliki o nazwie `.pdf`. Wszystko inne w folderze jest pomijane, a archiwum w folderze nie jest otwierane.
- Pliki w podfolderach są uwzględniane tam, gdzie konto dokumentów je wyświetla: konta S3, Wasabi i Google Cloud Storage wyświetlają całe drzewo folderów, a konta OneDrive, SFTP i Azure tylko najwyższy poziom.
- Scalanych jest co najwyżej 100 plików PDF; więcej powoduje niepowodzenie kroku.

## Dane wyjściowe

Pojedynczy plik PDF pod ścieżką wyjściową, zawierający każdą stronę każdego scalonego pliku PDF.

## Uwagi

- Folder bez plików PDF lub taki, który nie istnieje, kończy krok ostrzeżeniem ze wskazaniem folderu, niczego nie scala, a przepływ pracy jest kontynuowany.
- Ścieżka wyjściowa nie może być ścieżką wejściową.

## Typowe zastosowania

- Składanie miesięcznych raportów z pojedynczych plików PDF raportów
- Łączenie strony tytułowej, treści i załączników w jeden dokument do dostarczenia
- Grupowanie wygenerowanych faktur w archiwum na klienta lub na okres

## Powiązane

- [Compress PDF (krok)](/pl/reference/workflow-steps/document/compress-pdf/) — zmniejsz scalony wynik
- [Convert Image to PDF (krok)](/pl/reference/workflow-steps/document/convert-image-to-pdf/) — zamień obrazy na pliki PDF przed scaleniem
