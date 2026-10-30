---
title: Zarządzanie tabelami i widokami
description: Zarządzaj tabelami i widokami w projektach PlaidCloud, w tym ich tworzeniem, konfiguracją, uprawnieniami i organizacją obiektów danych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud umożliwia organizowanie tabel i zarządzanie nimi, w tym etykietami. Tabele są dostępne dla wszystkich przepływów pracy w projekcie i mają wiele narzędzi oraz opcji.


Oprócz tabel PlaidCloud oferuje także widoki oparte na danych tabel. Użycie widoków pozwala na natychmiastowe aktualizacje, gdy zmienią się tabele źródłowe, oraz oszczędza miejsce w magazynie danych.



Opcje obejmują:


* Ta sama tabela może istnieć w wielu ścieżkach hierarchii (hierarchie alternatywne)
* Tabele można oznaczać tagami, aby łatwiej je wyszukiwać i uwzględniać w procesach PlaidCloud
* Tabele mogą mieć wersje
* Tabele można opublikować, aby były dostępne dla wizualizacji pulpitów

PlaidCloud używa systemu opartego na ścieżkach do organizowania tabel, podobnie jak przy poruszaniu się po serii folderów, co pozwala na bardziej elastyczną i logiczną organizację tabel. Dzięki temu systemowi tabele można przenosić w obrębie hierarchii albo tworzyć wiele odwołań do jednej tabeli z różnych miejsc hierarchii (hierarchie alternatywne). Możliwość zarządzania tabelami tą metodą pozwala, aby struktura odzwierciedlała potrzeby operacyjne, raportowanie i kontrolę.



## Wyszukiwanie tabel


Użyj pola filtra w lewym dolnym rogu hierarchii, aby przeszukiwać nazwy i etykiety tabel. Dopasowania są pokazywane w hierarchii powyżej.


### Według przepływu pracy

Folder **Według przepływu pracy** na końcu karty **Tabele** grupuje tabele pod każdym przepływem pracy, który je odczytuje lub zapisuje. Otwórz przepływ pracy, aby zobaczyć jego tabele. Folder jest widokiem tych samych tabel, więc nie możesz niczego z niego przenosić ani kopiować.


### Według kolumny

Wpisz nazwę kolumny w polu wyszukiwania kolumn na karcie **Tabele** i naciśnij Enter albo wybierz lupę obok niego, aby pokazać tylko tabele, które mają kolumnę o tej nazwie. Wyszukiwanie odczytuje nazwy kolumn, a nie dane, więc jest szybkie. Wybierz **Zawiera**, aby dopasować część nazwy kolumny zamiast całej nazwy. Wyczyść pole, aby ponownie pokazać wszystkie tabele. Długie wyszukiwanie może zwracać wyniki stronami, a wiersz stanu informuje, kiedy wyszukiwanie wciąż trwa lub może być niekompletne.

Wybierz **Drzewo kolumn**, aby wyszukiwać z osobnego okna. Każda tabela, która ma tę kolumnę, otwiera się na dwie listy:

* **Zasilana przez** — tabele, które dostarczają kolumnę
* **Zasila** — tabele, które kolumna dalej zasila

Asystent AI połączony przez MCP znajduje te same tabele za pomocą `table_find(column=...)`, dopasowując całą nazwę lub jej część.


### Wyszukiwanie wartości

Aby znaleźć tabele zawierające daną wartość, wybierz **Szukaj wartości w danych… (wolne)** z menu **Akcje** na karcie **Tabele** albo kliknij tabelę prawym przyciskiem myszy i wybierz tę opcję, aby szukać tylko w tej tabeli. Wpisz wartość, wybierz **Zawiera**, aby dopasować część wartości, i wybierz **Search**. Każda tabela zawierająca wartość jest wymieniona wraz z kolumnami, w których występuje, i kilkoma pasującymi wartościami. Kliknij tabelę dwukrotnie lub naciśnij na niej Enter, aby otworzyć ją w Eksploratorze tabel. Kolumna otwiera tabelę przefiltrowaną do pasujących wierszy. Jeśli pole wyszukiwania kolumn zawiera tekst, wypełnia on wartość do znalezienia.

Przed wyszukiwaniem należy wiedzieć, że:

* Wyszukiwanie odczytuje każdy wiersz każdej przeszukiwanej tabeli, więc może być bardzo wolne i zużywać dużo zasobów hurtowni danych. Okno ostrzega o tym, a przyciski wyszukiwania pozostają wyłączone do zakończenia wyszukiwania.
* Widzisz tylko wiersze, które mogłeś już otworzyć. Zabezpieczenia na poziomie wierszy obowiązują w każdym wyszukiwaniu.
* Historia zapytań Twojej hurtowni danych rejestruje wyszukiwane wartości.
* Wyszukiwanie obejmuje kolumny tekstowe tabel. Tabele, które nie zostały zbudowane, są pomijane i wymienione w ostrzeżeniu.
* Wyniki są zwracane stronami. Gdy wiersz stanu informuje, że wyszukiwanie zatrzymało się wcześniej, wybierz **Szukaj dalej**, aby kontynuować z tabelami, które nie zostały jeszcze przeszukane.

Asystent AI połączony przez MCP używa `table_value_search`. Zwraca tabele i kolumny zawierające wartość, nigdy same wartości. Gdy prosisz asystenta AI w projekcie o znalezienie wartości, Weave wysyła nazwy pasujących tabel i kolumn do dostawcy modelu językowego.



## Importowanie pliku CSV

**Aby zamienić plik CSV w nową tabelę w tym projekcie:**

1. Przeciągnij plik z komputera na listę **Tabele** projektu albo wybierz na pasku narzędzi **Nowy** > **Tabela z pliku CSV** i upuść plik na pole lub kliknij **Wybierz plik CSV**.
2. PlaidCloud przesyła plik na Twój **Personal Temp Drive** albo, jeśli go nie masz, na **Temp Drive** obszaru roboczego i importuje go do nowej tabeli na najwyższym poziomie listy, nazwanej od pliku: `Sales Data.csv` staje się `sales_data`. Jeśli projekt ma już tabelę o tej nazwie, nowa dostaje numer, na przykład `sales_data_2`.
3. Lista odświeża się z zaznaczoną nową tabelą, a **Twoje dane w skrócie** otwiera się dla niej. Zobacz [Zacznij od własnego pliku CSV](/pl/get-started/quickstart/#zacznij-od-własnego-pliku-csv), aby dowiedzieć się, co pokazuje panel.

Akceptowane są tylko pliki z rozszerzeniem `.csv`. Potrzebujesz uprawnienia do tworzenia tabel i zapisu w magazynie dokumentów, a zablokowany projekt nie przyjmuje pliku CSV do czasu odblokowania. Jeśli import się nie powiedzie, okno podaje powód, a projekt pozostaje taki, jaki był. PlaidCloud usuwa przesłany plik z dysku tymczasowego po zakończeniu importu, niezależnie od tego, czy się udał; jeśli się to nie uda, dysk tymczasowy usuwa go po dniu.

## Przenoszenie


**Aby przenieść tabelę:**


1. Przeciągnij ją do folderu, w którym ma się znajdować

## Zmiana nazwy


**Aby zmienić nazwę tabeli:**


1. Kliknij tabelę prawym przyciskiem myszy
2. Wybierz opcję zmiany nazwy
3. Wpisz nową nazwę i zapisz ją
4. Tabela ma teraz nową nazwę, ale zachowuje swój pierwotny unikatowy identyfikator.

## Czyszczenie


**Aby wyczyścić tabelę:**


1. Zaznacz tabele w hierarchii ‘
2. Kliknij przycisk czyszczenia na górnym pasku narzędzi.

*Uwaga: możesz wyczyścić jedną tabelę lub wiele tabel*



## Usuwanie


**Aby usunąć tabelę:**


1. Zaznacz tabele w hierarchii
2. Kliknij przycisk usuwania na górnym pasku narzędzi
3. Operacja usuwania sprawdzi, czy tabela jest używana przez kroki przepływu pracy lub widoki. Jeśli tak, zostaniesz poproszony o usunięcie tych powiązań, zanim usunięcie będzie możliwe.

*Uwaga: możesz też wymusić usunięcie tabel. Wymuszone usunięcie tabel pozostawi uszkodzone odwołania, więc należy z niego korzystać oszczędnie.*


### Ostatni odczyt

Okno usuwania pokazuje, kiedy tabela była ostatnio odczytywana, na przykład **Last read 3 days ago by** osoba lub krok, aby można było odróżnić tabelę, z której nikt nie korzysta, od wciąż używanej. PlaidCloud pobiera to z własnej historii zapytań Twojej hurtowni danych i pomija odczyty wykonane przez własne czynności porządkowe.

| Hurtownia danych | Co jest potrzebne |
| --- | --- |
| Snowflake | Odczyty pochodzą z Access History, które Snowflake rejestruje z opóźnieniem do około 3 godzin. Rola połączenia potrzebuje roli bazy danych `SNOWFLAKE.GOVERNANCE_VIEWER` (działa także `IMPORTED PRIVILEGES` na bazie danych `SNOWFLAKE`). Wersja Snowflake Standard nie ma Access History. |
| Databricks | Odczyty pochodzą z tabeli lineage, którą Databricks również rejestruje z opóźnieniem, więc niedawny odczyt może jeszcze nie być widoczny. Tożsamość połączenia potrzebuje `USE CATALOG` na `system`, `USE SCHEMA` na `system.access` oraz `SELECT` na `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Historia odczytów nie jest jeszcze dostępna. Okno pokazuje **Read history incomplete**. |

Gdy łączysz hurtownię danych, [sprawdzenie połączenia](/pl/guides/connections/external-lakehouse/#3-sprawdź-a-następnie-użyj) zaleca każde z brakujących uprawnień, każde wraz z instrukcją do uruchomienia. Są zalecane, a nie wymagane: bez nich hurtownia danych się łączy, a okno pokazuje **Read history incomplete**.

Gdy PlaidCloud nie może odczytać całej historii, wiersz mówi **Read history incomplete** i nigdy nie podaje w jego miejsce „brak odczytów”. Każdy, kto ma bezpośredni dostęp SQL do Twojej hurtowni danych, może ustawić tag sesji, który zmienia sposób oznaczania jego własnych odczytów.

Asystent AI połączony przez MCP otrzymuje tę samą odpowiedź z `table_describe(include=['last_read'])`.



## Kolumny tabeli


Wybranie tabeli otwiera jej panel szczegółów. Sekcja **Kolumny** wymienia każdą kolumnę z jej **Typem** i **Opisem**, przy czym opis pochodzi z **Właściwości kolumny**. Wskaż wiersz, aby przeczytać długi opis w całości.

Tabela, której teraz nie ma w hurtowni danych, ponieważ jej dane wygasły lub żaden krok jej nie zbudował, nie ma kolumn do wyświetlenia. Sekcja o tym informuje i pokazuje, ile kolumn ma tabela. Uruchom krok, który zapisuje tabelę, aby je wyświetlić.


## Gdzie tabela jest używana


Wybranie tabeli otwiera jej panel szczegółów, który wymienia kroki przepływu pracy mające z nią związek:


* **Tabela utworzona przez** — kroki, które zapisują do tabeli
* **Tabela wnosi wkład do** — kroki, które z niej odczytują
* **Może odwoływać się do tej tabeli** — kroki, które docierają do tabeli przez zmienną, której nie można rozstrzygnąć. Ta sekcja pojawia się tylko wtedy, gdy są takie kroki.


Krok może nazwać tabelę wprost albo dotrzeć do niej przez ścieżkę zawierającą zmienną, na przykład `/Periods/{period}/Sales`. Gdy zmienna ma bieżącą wartość, krok pojawia się na dwóch pierwszych listach z ikoną informacji obok. Najedź na wiersz, aby zobaczyć ścieżkę w postaci, w jakiej przechowuje ją krok.


Traktuj te wiersze jako słabszą odpowiedź, którą są. Opisują to, czego dotknęłoby uruchomienie rozpoczęte teraz — a nie wszystko, co kiedykolwiek dotykało tabeli. Zmień zmienną, a zostanie odczytana inna tabela.


Niektórych zmiennych nie można rozstrzygnąć. Albo nic nie ustawiło zmiennej, albo wartość używana przez uruchomienie nie pochodzi z tego, co jest zapisane — krok Workflow Loop pobiera zmienne z danych w trakcie iteracji, krok ustawiający zmienną przypisuje je w trakcie uruchomienia, makro otrzymuje zmienne od tego kroku, który je wywołuje, a uruchomienie rozpoczęte przez sensor niesie własne szczegóły tego sensora. W każdym przypadku to, co jest zapisane między uruchomieniami, to pozostałość po ostatnim z nich, a nie wartość, której można ufać. Zamiast rozstrzygać je do tabeli, która może być niewłaściwa, PlaidCloud wymienia kroki z nazwy w sekcji **Może odwoływać się do tej tabeli**, wraz ze zmienną, której nie mógł rozstrzygnąć, abyś mógł je otworzyć i sprawdzić.


Krok, którego Twoja rola nie widzi, jest nadal wymieniony, abyś wiedział, że tabela jest używana, ale bez nazwy i przepływu pracy, i nie możesz go otworzyć. Nadal liczy się przy usuwaniu tabeli. Krok, który widzisz, jest wymieniony bez przepływów pracy ukrytych przed Twoją rolą. Przed Architektem nic nie jest ukryte.


*Uwaga: gdy usuwasz tabele z listy **Tabele**, krok, który dociera do tabeli przez ścieżkę, ze zmienną lub bez niej, liczy się jako jej użycie, nawet gdy jego zmiennej nie można rozstrzygnąć. Okno usuwania wymienia krok, a usunięcie jest kontynuowane tylko po wymuszeniu.*



## Tworzenie nowej struktury katalogów


**Aby dodać nowy folder:**


1. Kliknij przycisk Nowy folder na pasku narzędzi

**Aby dodać folder do istniejącego folderu:**


1. Kliknij folder prawym przyciskiem myszy
2. Wybierz Nowy folder


## Wyświetlanie danych (Eksplorator tabel)


Dane tabeli są wyświetlane za pomocą Eksploratora danych. Eksplorator danych udostępnia widok siatki danych oraz podsumowanie wartości i statystyk kolumna po kolumnie. Dostępne jest filtrowanie metodą wskaż i kliknij oraz eksportowanie do znanych formatów plików. Wybrane filtry można też zapisać jako krok wyodrębniania, którego można użyć w przepływie pracy.



## Publikowanie tabeli do raportowania


Wizualizacje pulpitów są celowo ograniczone do tabel, które zostały opublikowane. Podczas publikowania tabeli możesz podać unikatową nazwę, która może wyróżniać dane. Może to być przydatne, gdy tabela ma bardziej niejasną nazwę w części przepływu pracy, która ją wygenerowała, ale potrzebuje wyraźniejszej nazwy dla osób budujących pulpity.


Opublikowane tabele nie mają powiązanych ścieżek. Pojawiają się jako lista tabel do użycia w obszarze pulpitów.



## Oznaczanie tabeli dla ról przeglądających


Przeglądanie tabel przez różne role można kontrolować, klikając pola wyboru Eksplorator lub Menedżer. Jeśli trzeba zaktualizować wiele tabel, zaznacz tabele w hierarchii i wybierz żądaną rolę przeglądającą z menu Akcje na górnym pasku narzędzi.



## Notatki opisujące zawartość tabeli


Dodaj notatkę do tabeli, aby lepiej zrozumieć dane.



## Kształt, rozmiar i czas ostatniej aktualizacji tabeli


Liczba wierszy, kolumn i rozmiar danych każdej tabeli są pokazane w hierarchii tabel. W przypadku bardzo dużych tabel (wiele milionów wierszy) liczba wierszy może być szacowana i zostanie pokazany wskaźnik przybliżonej liczby wierszy.



## Wyświetlanie dodatkowych atrybutów tabeli


**Aby wyświetlić i edytować inne atrybuty tabeli:**


1. Zaznacz tabelę
2. Kliknij widok formularza kontekstu tabeli po prawej stronie.


## Duplikowanie tabeli


**Aby zduplikować tabelę:**


1. Zaznacz tabelę
2. Kliknij przycisk duplikowania na górnym pasku narzędzi.


## Tworzenie aplikacji Panel z tabeli


Zaznacz tabelę lub widok i wybierz **Utwórz aplikację Panel** z menu **Nowy** albo z menu prawego przycisku myszy. Otworzy się okno **Nowa aplikacja Studio** z już wybranym projektem i tabelą. Nazwij aplikację i wybierz **Utwórz**, a Panel Studio otworzy ją z Weave gotowym do zbudowania jej pierwszej strony. Polecenie jest dostępne, gdy zaznaczasz jedną tabelę lub widok, masz dostęp do edycji projektu, a projekt nie jest tylko do odczytu. Zobacz [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/#zacznij-od-tabeli).


## Co przechowują tabele


Lista **Tabele** pokazuje kolumny **Dane bieżące**, **Historia** i **Uwaga** obok rozmiaru każdej tabeli, a za nimi **Dni Time Travel**. Nad listą wiersz podaje sumę projektu: ile przechowuje i ile z tego to dane bieżące, a ile historia. Tabela, której PlaidCloud jeszcze nie zmierzył, nie ma rozmiarów.

Wybierz **Magazyn** na pasku narzędzi, aby otworzyć okno **Magazyn** projektu, z sugestiami dotyczącymi zwolnienia miejsca i ustawieniami time travel. Zobacz [Zarządzanie magazynem](/pl/guides/projects/managing-storage/#okno-magazyn-dla-projektu).


## Tworzenie edytora danych z tabeli


Możesz zamienić tabelę w skonfigurowany edytor danych w jednym kroku — zaznacz tabelę i wybierz **Utwórz edytor danych z tabeli** z menu **Nowy** albo z menu prawego przycisku myszy. PlaidCloud analizuje kolumny tabeli i z góry buduje kontrolki wejściowe edytora. Szczegóły zobacz w [Tworzenie edytora danych z tabeli](/pl/guides/projects/managing-data-editors/#tworzenie-edytora-danych-z-tabeli).
