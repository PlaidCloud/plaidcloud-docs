---
title: Krok Call SAP Financial Document Attachment
description: Pobieraj załączniki dokumentów finansowych SAP z kroku przepływu pracy PlaidCloud na potrzeby zautomatyzowanej ekstrakcji i przetwarzania dokumentów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Opis



Dołącza plik do określonego dokumentu FI (Financial Accounting) w SAP ECC / S/4HANA za pomocą RFC (Remote Function Call). Przydatne do księgowania dokumentacji uzupełniającej — zeskanowanych faktur, przepływów zatwierdzania, kopii umów — razem z zapisami finansowymi, które ona wspiera.

Wymaga poświadczeń SAP RFC skonfigurowanych w łączniku SAP oraz numeru docelowego dokumentu FI (kod spółki, numer dokumentu, rok obrotowy).


## Co jest sprawdzane przy zapisie

Krok odczytuje ścieżkę każdego pliku z kolumny `relative_file_path` wśród kolumn wyjściowych na karcie **Kolumny** i ta kolumna musi być tekstowa. Zapis jest odrzucany, gdy jej brakuje — *Kolumny wyjściowe muszą zawierać relative_file_path, ścieżkę każdego pliku do dołączenia.* — lub gdy ma inny typ — *Kolumna relative_file_path musi być tekstowa, a nie integer.*

Zapis z wybraną tabelą źródłową, ale bez kolumn źródłowych lub docelowych, uzupełnia pustą stronę na podstawie źródła, tak jak zrobiłoby to **Wypełnij obie tabele mapowania**.


## Przykłady


### Parametry RFC


Wybierz **Agent do użycia**. Wybierz **Katalog docelowy** z listy rozwijanej i poniżej wskaż właściwy podrzędny folder docelowy dla pliku. Następnie odpowiednio nazwij „Target File Name”. W sekcji „Function Call Information” wprowadź funkcję i **Parametr wartości zwracanej** oraz wybierz parametry.



Możesz wybrać **Wstaw wiersz** lub **Dołącz wiersz** w sekcji Parametry, a także nazwać parametry i nadać im wartości. Wybierz liczbę w **Maks. liczba równoległych żądań** i zaznacz „Wait for RFC to Complete”. Zapisz i uruchom krok.
