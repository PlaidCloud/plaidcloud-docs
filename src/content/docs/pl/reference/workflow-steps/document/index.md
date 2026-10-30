---
title: Kroki dokumentów
description: Zarządzaj dokumentami w przepływach pracy PlaidCloud za pomocą kroków do konwersji, kopiowania, zmiany nazw i usuwania plików oraz operacji na PDF.
sidebar:
  label: Kroki dokumentów
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

Kroki przepływu pracy do operowania na plikach przechowywanych na kontach dokumentów. Używaj ich do przenoszenia, przekształcania i konwertowania dokumentów obok przepływów pracy z danymi.

## Operacje na plikach

- [Copy Document File (krok)](/pl/reference/workflow-steps/document/copy-document-file/) · [Copy Document Directory (krok)](/pl/reference/workflow-steps/document/copy-document-directory/)
- [Create Document Directory (krok)](/pl/reference/workflow-steps/document/create-document-directory/)
- [Delete Document File (krok)](/pl/reference/workflow-steps/document/delete-document-file/) · [Delete Document Directory (krok)](/pl/reference/workflow-steps/document/delete-document-directory/)
- [Lista katalogu](/pl/reference/workflow-steps/document/directory-listing/) — zapisz tabelę plików w folderze
- [Update Excel Cells (krok)](/pl/reference/workflow-steps/document/document-excel-update/) — zapisz wartości w wybranych komórkach skoroszytu lub sformatuj je
- [Fix File Extension (krok)](/pl/reference/workflow-steps/document/fix-file-extension/)
- [Rename Document File (krok)](/pl/reference/workflow-steps/document/rename-document-file/) · [Rename Document Directory (krok)](/pl/reference/workflow-steps/document/rename-document-directory/)

Kroki kopiowania i zmiany nazwy traktują brak źródła jako normalną sytuację. Gdy brakuje pliku albo folderu do skopiowania lub zmiany nazwy, albo folder jest pusty, krok nic nie robi, kończy się ostrzeżeniem ze wskazaniem ścieżki, a przepływ pracy jest kontynuowany. Zaplanowane uruchomienie na folderze, który danego dnia nie ma plików, już nie kończy się niepowodzeniem.

## Szyfrowanie

- [Encrypt File and Decrypt File (kroki)](/pl/reference/workflow-steps/document/encrypt-decrypt-file/) — AES, Blowfish lub hasło skoroszytu Excel

## Operacje na PDF

- [Compress PDF (krok)](/pl/reference/workflow-steps/document/compress-pdf/)
- [Convert Image to PDF (krok)](/pl/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or Image to JPEG (krok)](/pl/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFs (krok)](/pl/reference/workflow-steps/document/merge-multiple-pdfs/)

## Operacje na obrazach

- [Crop Image to Headshot (krok)](/pl/reference/workflow-steps/document/crop-image-to-headshot/)

## Operacje na tekście

- [Concatenate Files (krok)](/pl/reference/workflow-steps/document/concatenate-files/) — łączy wiele plików w jeden
- [Document Text Substitution (krok)](/pl/reference/workflow-steps/document/document-text-substitution/) — znajdź i zamień wewnątrz dokumentu

## Konwersja kodowania

- [Convert Document Encoding (krok)](/pl/reference/workflow-steps/document/convert-document-encoding/) — wybór kodowania docelowego
- [Convert Document Encoding to ASCII (krok)](/pl/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert Document Encoding to UTF-16 (krok)](/pl/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert Document Encoding to UTF-8 (krok)](/pl/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## Zobacz także

- [Convert Dashboard to PDF (krok)](/pl/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files (krok)](/pl/reference/workflow-steps/document/document-delete-old-files/)
- [Konta dokumentów](/pl/guides/documents/adding-accounts/) — połącz konta dokumentów przed użyciem tych kroków
- [Przewodnik po dokumentach](/pl/guides/documents/) — omówienia zadań dla tych samych operacji
