---
title: Zarządzanie tabelami i widokami
description: Zarządzaj tabelami i widokami w projektach PlaidCloud, w tym ich tworzeniem, konfiguracją, uprawnieniami i organizacją obiektów danych.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud umożliwia organizowanie tabel i zarządzanie nimi, także za pomocą etykiet. Tabele są dostępne dla wszystkich przepływów pracy w projekcie i oferują wiele narzędzi oraz opcji.


Oprócz tabel PlaidCloud oferuje również widoki oparte na danych tabel. Widoki zapewniają natychmiastową aktualizację po zmianach w tabelach źródłowych oraz oszczędzają miejsce w magazynie danych.



Dostępne opcje:


* Ta sama tabela może istnieć na wielu ścieżkach w hierarchii (hierarchie alternatywne)
* Tabele można oznaczać tagami, aby łatwiej je wyszukiwać i uwzględniać w procesach PlaidCloud
* Tabele mogą mieć wersje
* Tabele można opublikować, aby były dostępne dla wizualizacji pulpitów

PlaidCloud używa do organizowania tabel systemu opartego na ścieżkach, podobnego do tego, którego używasz do poruszania się po folderach, co pozwala na bardziej elastyczną i logiczną organizację tabel. W tym systemie tabele można przenosić w obrębie hierarchii albo tworzyć wiele odwołań do jednej tabeli z różnych miejsc hierarchii (hierarchie alternatywne). Możliwość zarządzania tabelami w ten sposób pozwala, by struktura odzwierciedlała potrzeby operacyjne, raportowanie i kontrolę.



## Wyszukiwanie tabel


Użyj pola filtru w lewym dolnym rogu hierarchii, aby przeszukiwać nazwy i etykiety tabel. Dopasowania są wyświetlane w hierarchii powyżej.


### Według przepływu pracy

Folder **By Workflow** na końcu karty **Tabele** grupuje tabele pod każdym przepływem pracy, który je odczytuje lub zapisuje. Otwórz przepływ pracy, aby zobaczyć jego tabele. Folder jest widokiem tych samych tabel, więc nie możesz z niego niczego przenosić ani kopiować.


### Według kolumny

Wpisz nazwę kolumny w polu wyszukiwania kolumn na karcie **Tabele**, aby pokazać tylko tabele, które mają kolumnę o tej nazwie. Wybierz **Zawiera**, aby dopasować część nazwy kolumny zamiast całej nazwy. Wyczyść pole, aby ponownie pokazać wszystkie tabele. Długie wyszukiwanie może zwracać wyniki stronami, a wiersz stanu informuje, kiedy wyszukiwanie wciąż trwa lub może być niekompletne.

Wybierz **Column Tree**, aby wyszukiwać w osobnym oknie. Każda tabela, która ma tę kolumnę, rozwija się do dwóch list:

* **Fed by** — tabele, które dostarczają kolumnę
* **Feeds** — tabele, do których kolumna trafia dalej

Asystent AI połączony przez MCP znajduje te same tabele za pomocą `table_find(column=...)`, dopasowując całą nazwę lub jej część.


### Wyszukiwanie wartości

Aby znaleźć, które tabele zawierają daną wartość, wybierz **Search Values** na karcie **Tabele** albo kliknij tabelę prawym przyciskiem myszy i wybierz **Search Value**, aby szukać tylko w tej tabeli. Wpisz wartość, wybierz **Zawiera**, aby dopasować część wartości, i wybierz **Szukaj**. Każda tabela zawierająca wartość jest wymieniona wraz z kolumnami, w których się pojawia, i kilkoma pasującymi wartościami.

Zanim zaczniesz wyszukiwanie, pamiętaj, że:

* Widzisz tylko wiersze, które i tak mógłbyś otworzyć. Do każdego wyszukiwania stosują się zabezpieczenia na poziomie wierszy.
* Historia zapytań Twojego magazynu danych zapisuje wartości, których szukasz.
* Wyszukiwanie obejmuje kolumny tekstowe tabel. Tabele, które nie zostały zbudowane, są pomijane i wymienione w ostrzeżeniu.
* Wyniki są zwracane stronami. Gdy wiersz stanu informuje, że wyszukiwanie zakończyło się wcześniej, wybierz **Search more**, aby kontynuować dla tabel, które nie zostały jeszcze przeszukane.

Asystent AI połączony przez MCP używa `table_value_search`. Zwraca on tabele i kolumny zawierające wartość, nigdy same wartości. Gdy prosisz asystenta AI w projekcie o znalezienie wartości, Weave wysyła nazwy pasujących tabel i kolumn do dostawcy modelu językowego.



## Importuj plik CSV

**Aby zamienić plik CSV w nową tabelę w tym projekcie:**

1. Przeciągnij plik z komputera na listę **Tabele** projektu albo wybierz **Nowy** > **Tabela z pliku CSV** na pasku narzędzi i upuść plik w polu lub kliknij **Wybierz plik CSV**.
2. PlaidCloud przesyła plik na Twój **Personal Temp Drive** albo, jeśli go nie masz, na **Temp Drive** obszaru roboczego i importuje go do nowej tabeli na najwyższym poziomie listy, nazwanej od pliku: `Sales Data.csv` staje się `sales_data`. Jeśli projekt ma już tabelę o takiej nazwie, nowa otrzymuje numer, na przykład `sales_data_2`.
3. Lista odświeża się z zaznaczoną nową tabelą, a panel **Twoje dane w skrócie** otwiera się dla niej. To, co pokazuje panel, opisuje [Zacznij od własnego pliku CSV](/pl/get-started/quickstart/#zacznij-od-własnego-pliku-csv).

Akceptowane są tylko pliki z rozszerzeniem `.csv`. Potrzebujesz uprawnień do tworzenia tabel i zapisu w magazynie dokumentów, a zablokowany projekt nie przyjmie pliku CSV, dopóki nie zostanie odblokowany. Jeśli import się nie powiedzie, okno podaje przyczynę, a projekt pozostaje w stanie sprzed importu. PlaidCloud usuwa przesłany plik z dysku tymczasowego po zakończeniu importu, niezależnie od tego, czy się powiódł; jeśli to się nie uda, dysk tymczasowy usuwa go po dobie.

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

*Uwaga: możesz też wymusić usunięcie tabel. Wymuszone usunięcie pozostawi uszkodzone odwołania, dlatego należy z niego korzystać oszczędnie.*


### Ostatni odczyt

Okno usuwania pokazuje, kiedy tabela była ostatnio odczytywana, na przykład **Last read 3 days ago by** osoba lub krok, dzięki czemu odróżnisz tabelę, której nikt nie używa, od takiej, która nadal jest w użyciu. PlaidCloud pobiera tę informację z własnej historii zapytań Twojego magazynu danych i pomija odczyty wykonane przez jego własne zadania porządkowe.

| Magazyn danych | Co jest potrzebne |
| --- | --- |
| Snowflake | Odczyty pochodzą z Access History, które Snowflake rejestruje z opóźnieniem do około 3 godzin. Rola połączenia potrzebuje roli bazy danych `SNOWFLAKE.GOVERNANCE_VIEWER` (działa też `IMPORTED PRIVILEGES` na bazie danych `SNOWFLAKE`). Edycja Snowflake Standard nie ma Access History. |
| Databricks | Odczyty pochodzą z tabeli lineage, którą Databricks również rejestruje z opóźnieniem, więc niedawny odczyt może jeszcze się nie pojawić. Tożsamość połączenia potrzebuje `USE CATALOG` na `system`, `USE SCHEMA` na `system.access` oraz `SELECT` na `system.access.table_lineage`. |
| PlaidCloud Lakehouse | Historia odczytów nie jest jeszcze dostępna. Okno pokazuje **Read history incomplete**. |

Gdy łączysz swój magazyn danych, [sprawdzenie połączenia](/pl/guides/connections/external-lakehouse/#3-sprawdź-a-następnie-użyj) zaleca każde z tych uprawnień, którego brakuje, wraz z instrukcją do uruchomienia. Są one zalecane, a nie wymagane: bez nich magazyn danych łączy się, a okno pokazuje **Read history incomplete**.

Gdy PlaidCloud nie może odczytać całej historii, wiersz informuje **Read history incomplete** i nigdy nie zgłasza w jego miejsce „brak odczytów”. Każdy, kto ma bezpośredni dostęp SQL do Twojego magazynu danych, może ustawić znacznik sesji, który zmienia sposób oznaczania jego własnych odczytów.

Asystent AI połączony przez MCP uzyskuje tę samą odpowiedź z `table_describe(include=['last_read'])`.



## Sprawdzanie, gdzie tabela jest używana


Zaznaczenie tabeli otwiera jej panel szczegółów, który wymienia kroki przepływu pracy, które jej dotyczą:


* **Tabela utworzona przez** — kroki, które zapisują do tabeli
* **Tabela wnosi wkład do** — kroki, które z niej odczytują
* **Może odwoływać się do tej tabeli** — kroki, które docierają do tabeli przez zmienną, której nie można rozstrzygnąć. Ta sekcja pojawia się tylko wtedy, gdy istnieją takie kroki.


Krok może wskazywać tabelę wprost albo docierać do niej przez ścieżkę zawierającą zmienną, taką jak `/Periods/{period}/Sales`. Gdy zmienna ma bieżącą wartość, krok pojawia się w pierwszych dwóch listach z ikoną informacji obok. Najedź kursorem na wiersz, aby zobaczyć ścieżkę w postaci, w jakiej krok ją przechowuje.


Traktuj te wiersze jako słabszą odpowiedź, którą są. Opisują to, czego dotknęłoby uruchomienie rozpoczęte teraz — a nie wszystko, co kiedykolwiek dotykało tabeli. Zmień zmienną, a zostanie odczytana inna tabela.


Niektórych zmiennych nie można rozstrzygnąć. Albo nic nie ustawiło zmiennej, albo wartość używana przez uruchomienie nie pochodzi z tego, co jest zapisane — Worklow Loop pobiera swoje zmienne z danych w trakcie iteracji, krok Set Variable przypisuje je w trakcie uruchomienia, makro otrzymuje zmienne od kroku, który je wywołuje, a uruchomienie rozpoczęte przez czujnik niesie własne szczegóły tego czujnika. W każdym z tych przypadków to, co jest zapisane między uruchomieniami, jest pozostałością po ostatnim z nich, a nie wartością, której można ufać. Zamiast rozstrzygać je do tabeli, która może być niewłaściwa, PlaidCloud wymienia kroki z nazwy w sekcji **Może odwoływać się do tej tabeli**, razem ze zmienną, której nie mógł rozstrzygnąć, abyś mógł je otworzyć i sprawdzić.


Krok, którego Twoja rola nie może zobaczyć, jest nadal wymieniony, abyś wiedział, że tabela jest używana, ale bez jego nazwy i przepływu pracy, i nie możesz go otworzyć. Wlicza się on również przy usuwaniu tabeli. Krok, który możesz zobaczyć, jest wymieniony bez przepływów pracy ukrytych przed Twoją rolą. Przed Architektem nic nie jest ukryte.


*Uwaga: gdy usuwasz tabele z listy **Tabele**, krok, który dociera do tabeli przez ścieżkę, ze zmienną lub bez niej, liczy się jako jej użycie, nawet gdy jego zmiennej nie można rozstrzygnąć. Okno usuwania wymienia ten krok, a usunięcie przebiega tylko wtedy, gdy je wymusisz.*



## Tworzenie nowej struktury katalogów


**Aby dodać nowy folder:**


1. Kliknij przycisk **Nowy folder** na pasku narzędzi

**Aby dodać folder do istniejącego folderu:**


1. Kliknij folder prawym przyciskiem myszy
2. Wybierz **Nowy folder**


## Wyświetlanie danych (Eksplorator tabel)


Dane tabeli wyświetla się za pomocą Eksploratora danych. Eksplorator danych udostępnia widok siatki danych oraz podsumowanie wartości i statystyk kolumna po kolumnie. Dostępne jest filtrowanie metodą wskaż i kliknij oraz eksport do znanych formatów plików. Wybrane filtry można również zapisać jako krok Extract do użycia w przepływie pracy.



## Publikowanie tabeli na potrzeby raportowania


Wizualizacje pulpitów są celowo ograniczone do tabel, które zostały opublikowane. Podczas publikowania tabeli możesz podać unikatową nazwę, która pomoże odróżnić dane. Może to być przydatne, gdy tabela ma mniej czytelną nazwę w części przepływu pracy, który ją wygenerował, a osoby budujące pulpity potrzebują jaśniejszej nazwy.


Opublikowane tabele nie mają przypisanych ścieżek. Pojawiają się jako lista tabel do użycia w obszarze pulpitów.



## Oznaczanie tabeli na potrzeby ról widoczności


Widocznością tabel dla poszczególnych ról można sterować, klikając pola wyboru Eksplorator lub Menedżer. Jeśli trzeba zaktualizować wiele tabel, zaznacz je w hierarchii i wybierz żądaną rolę widoczności z menu Akcje na górnym pasku narzędzi.



## Notatki opisujące zawartość tabeli


Dodaj do tabeli notatkę, aby łatwiej zrozumieć dane.



## Wyświetlanie kształtu, rozmiaru i czasu ostatniej aktualizacji tabeli


Liczba wierszy, kolumn i rozmiar danych każdej tabeli są pokazane w hierarchii tabel. W przypadku bardzo dużych tabel (wiele milionów wierszy) liczba wierszy może być szacowana i wyświetlany jest wskaźnik przybliżonej liczby wierszy.



## Wyświetlanie dodatkowych atrybutów tabeli


**Aby wyświetlić i edytować inne atrybuty tabeli:**


1. Zaznacz tabelę
2. Kliknij widok formularza kontekstu tabeli po prawej stronie.


## Duplikowanie tabeli


**Aby zduplikować tabelę:**


1. Zaznacz tabelę
2. Kliknij przycisk duplikowania na górnym pasku narzędzi.


## Tworzenie edytora danych z tabeli


Możesz zamienić tabelę w skonfigurowany edytor danych w jednym kroku — zaznacz tabelę i wybierz **Utwórz edytor danych z tabeli** z menu **Nowy** albo z menu prawego przycisku myszy. PlaidCloud analizuje kolumny tabeli i wstępnie buduje kontrolki wejściowe edytora. Szczegóły opisuje [Tworzenie edytora danych z tabeli](/pl/guides/projects/managing-data-editors/#tworzenie-edytora-danych-z-tabeli).
