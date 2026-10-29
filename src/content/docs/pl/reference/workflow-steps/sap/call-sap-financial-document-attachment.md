---
title: Call SAP Financial Document Attachment (krok)
description: Pobieraj załączniki dokumentów finansowych SAP z kroku przepływu pracy PlaidCloud, aby zautomatyzować wyodrębnianie i przetwarzanie dokumentów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Opis



Dołącza plik do określonego dokumentu FI (Financial Accounting) w SAP ECC / S/4HANA za pomocą RFC (Remote Function Call). Przydatne do księgowania dokumentacji uzupełniającej — zeskanowanych faktur, przepływów zatwierdzania, kopii umów — obok zapisów finansowych, które ona potwierdza.

Wymaga poświadczeń SAP RFC skonfigurowanych w konektorze SAP oraz numeru docelowego dokumentu FI (kod spółki, numer dokumentu, rok obrotowy).


## Co jest sprawdzane przy zapisie

Krok odczytuje ścieżkę każdego pliku z kolumny `relative_file_path` wśród kolumn wyjściowych na karcie **Wybór danych tabeli**, a ta kolumna musi być tekstowa. Zapis jest odrzucany, gdy jej brakuje — *The output columns must include relative_file_path, the path of each file to attach.* — lub gdy ma inny typ — *The relative_file_path column must be text, not integer.*

Zapis z wybraną tabelą źródłową, ale bez kolumn źródłowych lub docelowych, wypełnia pustą stronę na podstawie źródła, tak jak zrobiłaby to opcja **Wypełnij obie tabele mapowania**.


## Przykłady


### Parametry RFC


Wybierz opcję Agent do użycia. Wybierz Katalog docelowy z listy rozwijanej i poniżej przejdź do właściwego folderu podrzędnego dla pliku. Następnie nadaj odpowiednią nazwę w polu „Target File Name”. W sekcji „Function Call Information” wprowadź funkcję i Parametr wartości zwracanej oraz wybierz parametry.



W sekcji parametrów możesz wybrać Wstaw wiersz lub Dołącz wiersz, a także nazwać parametry i nadać im wartości. Wybierz liczbę w polu Maks. liczba równoległych żądań i zaznacz opcję Wait for RFC to Complete. Kliknij „Zapisz i uruchom”.
