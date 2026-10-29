---
title: Run SAP PCM Hyper Loader (krok)
description: Uruchom SAP PCM Hyper Loader z kroku przepływu pracy PlaidCloud, aby wykonać szybkie masowe ładowanie danych do modeli PCM.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## Opis


Ładuje model SAP Profitability and Cost Management (PCM) za pomocą bezpośrednich załadunków tabel. Ten proces jest znacznie szybszy niż Databridge. Hyper Loader obsługuje praktycznie wszystkie bieżące tabele danych, przypisań i struktur PCM.


Poniżej znajduje się aktualna lista dostępnych celów ładowania:


* Aliasy działań
* Hierarchia wymiarowa działań
* Aliasy nośników kosztów działań
* Hierarchia wymiarowa nośników kosztów działań
* Wartość nośnika kosztów działania
* Domyślny skład BOM
* Zewnętrzna stawka jednostkowa BOM
* Skład BOM
* Wolumen produkcji BOM
* Sprzedane jednostki BOM
* Aliasy obiektu kosztów 1
* Hierarchia wymiarowa obiektu kosztów 1
* Aliasy obiektu kosztów 2
* Hierarchia wymiarowa obiektu kosztów 2
* Aliasy obiektu kosztów 3
* Hierarchia wymiarowa obiektu kosztów 3
* Aliasy obiektu kosztów 4
* Hierarchia wymiarowa obiektu kosztów 4
* Aliasy obiektu kosztów 5
* Hierarchia wymiarowa obiektu kosztów 5
* Przypisanie obiektu kosztów
* Nośnik kosztów obiektu kosztów
* Aliasy pozycji
* Aliasy szczegółów pozycji
* Hierarchia wymiarowa szczegółów pozycji
* Wartość szczegółów pozycji
* Hierarchia wymiarowa pozycji
* Bezpośrednie przypisanie pozycji do działania
* Przypisanie pozycji do nośnika kosztów zasobów
* Wartość pozycji
* Aliasy okresów
* Hierarchia wymiarowa okresów
* Aliasy nośników kosztów zasobów
* Hierarchia wymiarowa nośników kosztów zasobów
* Podział nośnika kosztów zasobów
* Wartość nośnika kosztów zasobów
* Aliasy ośrodków odpowiedzialności
* Hierarchia wymiarowa ośrodków odpowiedzialności
* Przychody
* Aliasy przychodów
* Hierarchia wymiarowa przychodów
* Aliasy usług
* Hierarchia wymiarowa usług
* Aliasy rozkładu
* Hierarchia wymiarowa rozkładu
* Wartość rozkładu
* Aliasy wersji
* Hierarchia wymiarowa wersji
* Aliasy arkusza 1
* Hierarchia wymiarowa arkusza 1
* Aliasy arkusza 2
* Hierarchia wymiarowa arkusza 2
* Wartość arkusza

## Nasze kwalifikacje


PlaidCloud jest oficjalnym partnerem SAP i preferowanym dostawcą usług związanych z projektowaniem i wdrażaniem modeli SAP PCM.


## Co jest sprawdzane przy zapisie

Każde źródło na karcie **Kroki ładowania** jest przygotowywane w tabeli ładowania wybranej jako jego **Docelowa tabela ładowania**, z dopasowaniem według nazw kolumn. Zapis jest odrzucany, ze wskazaniem źródła, gdy:

- Źródło nie ma docelowej tabeli ładowania albo ma tabelę, która nie jest tabelą ładowania PCM — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- Kolumny źródła nie pasują do jego tabeli ładowania: brakuje kolumny tabeli ładowania, ma ona inny typ niż w tabeli ładowania albo nie ma źródła, wyrażenia ani stałej — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* Opcja **Zresetuj kolumny docelowe do schematu** ponownie wypełnia kolumny docelowe źródła na podstawie jego tabeli ładowania.
- Dwa źródła mają tę samą nazwę. Każde źródło jest eksportowane do pliku nazwanego jego nazwą, więc jedno nadpisałoby drugie — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## Przykłady


Wybierz opcję Agent do użycia z listy rozwijanej. Wprowadź nazwę modelu i wybierz lokalizację ścieżki magazynu pakietu ładowania, a następnie wybierz w niej żądany folder podrzędny. Użyj poniższej sekcji Wybór danych tabeli, aby wybrać tabelę źródłową modelu i docelową tabelę ładowania. Sprawdzenie źródła>>propagacja obu stron tabeli ujawni dane. Gdy dane są wprowadzone i dodano wszystkie wyrażenia, kliknij „Zapisz i uruchom”.
