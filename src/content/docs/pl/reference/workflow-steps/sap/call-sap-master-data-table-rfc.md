---
title: Call SAP Master Data Table RFC (krok)
description: Wywołuje SAP ECC / S/4HANA Remote Function Call (RFC) służące do dostępu do tabel danych podstawowych i pobiera dane w postaci tabelarycznej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## Opis


Wywołuje SAP ECC / S/4HANA Remote Function Call (RFC) służące do dostępu do tabel danych podstawowych i pobiera dane w postaci tabelarycznej. Dane te są następnie dostępne dla procesów transformacji w PlaidCloud. Krok umożliwia też wyeksportowanie struktury tabeli danych podstawowych do osobnego pliku zawierającego nazwy kolumn, typy danych i kolejność kolumn.


## Przykłady


### Parametry RFC


Wybierz opcję Agent do użycia. Wybierz Katalog docelowy z listy rozwijanej i poniżej przejdź do właściwego folderu podrzędnego dla pliku. Następnie nadaj odpowiednią nazwę w polu „Target File Name”. W sekcji „Function Call Information” wprowadź funkcję i Parametr wartości zwracanej oraz wybierz parametry.



W sekcji parametrów możesz wybrać Wstaw wiersz lub Dołącz wiersz, a także nazwać parametry i nadać im wartości. Wybierz liczbę w polu Maks. liczba równoległych żądań i zaznacz opcję Wait for RFC to Complete. Kliknij „Zapisz i uruchom”.
