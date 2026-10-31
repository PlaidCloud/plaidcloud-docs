---
title: Call SAP General Ledger Posting (krok)
description: Wywołuje SAP ECC / S/4HANA Remote Function Call (RFC) służące do zaksięgowania zapisu dziennika wraz z odpowiednimi podatkami VAT i podatkiem u źródła.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## Opis


Wywołuje SAP ECC / S/4HANA Remote Function Call (RFC) służące do zaksięgowania zapisu dziennika wraz z odpowiednimi podatkami VAT i podatkiem u źródła. Może działać także w trybie testowym, który przeprowadza proces księgowania, ale go nie kończy. Pozwala to zebrać wykrywalne błędy, takie jak zamknięte konto lub nieistniejący klient w podanym kodzie spółki. Sprawdzanie błędów jest rozbudowane i umożliwia zwrócenie wielu wykrytych błędów w jednym teście.


## Przykłady


### Parametry RFC


Wybierz opcję Agent do użycia. Wybierz Katalog docelowy z listy rozwijanej i poniżej przejdź do właściwego folderu podrzędnego dla pliku. Następnie nadaj odpowiednią nazwę w polu „Target File Name”. W sekcji „Function Call Information” wprowadź funkcję i Parametr wartości zwracanej oraz wybierz parametry. 



W sekcji parametrów możesz wybrać Wstaw wiersz lub Dołącz wiersz, a także nazwać parametry i nadać im wartości. Wybierz liczbę w polu Maks. liczba równoległych żądań i zaznacz opcję Wait for RFC to Complete. Kliknij „Zapisz i uruchom”.
