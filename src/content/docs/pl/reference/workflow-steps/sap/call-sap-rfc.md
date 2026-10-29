---
title: Call SAP RFC (krok)
description: Wywołuj moduły funkcyjne SAP RFC z kroku przepływu pracy PlaidCloud, aby zintegrować się bezpośrednio z systemami SAP ECC i S/4HANA.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## Opis


Wywołuje SAP ECC / S/4HANA Remote Function Call (RFC) i pobiera dane w postaci tabelarycznej. Dane te są następnie dostępne dla procesów transformacji w PlaidCloud.


## Miejsce docelowe danych

Zapisz wynik RFC jako plik lub w tabeli.

Opcja **Plik** zapisuje wynik w formacie **JSON**, **Rozdzielany przecinkami**, **Rozdzielany tabulatorami**, **Rozdzielany znakiem potoku** lub **Parquet**. Plik Parquet zachowuje te same typy kolumn co tabela.

Opcja **Tabela** zapisuje wynik w **Tabeli docelowej**, z typami określonymi na podstawie własnych definicji pól funkcji RFC:

| Typ pola SAP | Zapisywany jako |
|---|---|
| Data | Data. Pusta lub początkowa data jest zapisywana jako pusta. Nieprawidłowa data jest zapisywana jako pusta, a krok kończy się ostrzeżeniem wskazującym kolumnę. |
| Liczba dziesiętna spakowana | Dokładna liczba dziesiętna. Więcej niż 10 miejsc po przecinku lub 28 cyfr części całkowitej jest zapisywane zamiast tego jako tekst, a krok kończy się ostrzeżeniem wskazującym kolumnę. |
| Liczba całkowita | Liczba całkowita. |
| `FLOAT` | Double. |
| Dziesiętna zmiennoprzecinkowa | Dokładny tekst. |
| `NUMC`, `CHAR` | Tekst, z zachowaniem zer wiodących. |
| Czas | Tekst w formacie `HH:MM:SS`. |
| Surowe bajty | Tekst szesnastkowy. |
| `UTCLONG` | Tekst. |

Jeśli SAP nie może opisać pól funkcji, liczby dziesiętne są zapisywane jako dokładny tekst.

Gdy SAP opisuje funkcję, każdy parametr jest konwertowany na oczekiwany typ: daty na `YYYYMMDD`, czasy na `HHMMSS`, liczby całkowite i dziesiętne na liczby, pola tekstowe na tekst, a parametry struktur i tabel pole po polu. Wartość, której nie można przekonwertować na parametr całkowity lub dziesiętny, powoduje niepowodzenie kroku.

## Przykłady


### Parametry RFC


Wybierz opcję Agent do użycia. Wybierz Katalog docelowy z listy rozwijanej i poniżej przejdź do właściwego folderu podrzędnego dla pliku. Następnie nadaj odpowiednią 
nazwę w polu „Target File Name”. W sekcji „Function Call Information” wprowadź funkcję i Parametr wartości zwracanej oraz wybierz parametry.

W sekcji parametrów możesz wybrać Wstaw wiersz lub Dołącz wiersz, a także nazwać parametry i nadać im wartości. Wybierz liczbę w polu Maks. liczba równoległych żądań 
i zaznacz opcję Wait for RFC to Complete. Kliknij „Zapisz i uruchom”.



### Zaawansowana iteracja wartości


Możesz wybrać „No Iterators” u góry tej karty, a następnie kliknąć Zapisz i uruchom, jeśli chcesz, albo możesz określić iteratory.


Tutaj możesz wybrać „Specify Argument Values” w polu Iteruj po i utworzyć argumenty, a następnie przejść do Wartości iteracji.


Obok pola Wybierz argument iteratora, aby edytować wartości dostępne są opcje Wstaw wiersz, Dołącz wiersz, Usuń wiersz, Przenieś w dół oraz Przenieś na koniec. 
Poniżej możesz wybrać Iteratory zakresu za pomocą tego samego menu rozwijanego. Ostatnia sekcja nosi tytuł „Exclusions for Selected Range Iteration” 
i oferuje te same opcje dla każdego wiersza, takie jak dodawanie czy usuwanie. Wykluczone wartości można wprowadzić poniżej. Kliknij Zapisz i uruchom.
