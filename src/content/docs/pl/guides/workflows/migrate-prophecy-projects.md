---
title: Migracja projektów Prophecy
description: Skonwertuj eksport projektu Prophecy na przepływy pracy PlaidCloud z poziomu aplikacji Analyze, REST API lub agenta AI połączonego przez MCP, powiąż jego zbiory danych i połączenia oraz przeczytaj raport z konwersji.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

PlaidCloud jest bezpośrednim zamiennikiem Prophecy. Każdy gem Prophecy jest konwertowany na natywne kroki przepływu pracy PlaidCloud, które wykonują pracę gema: konwerter tworzy jeden przepływ pracy dla każdego potoku Spark i jeden dla projektu SQL, mapuje każdy gem na krok przepływu pracy, zmienną projektu lub obiekt na kanwie, zachowuje oryginalny graf i zwraca raport z konwersji. Nieliczne zachowania, których skonwertowany przepływ pracy nie odtwarza samodzielnie, są wymienione w sekcji [Przypadki brzegowe](#przypadki-brzegowe).

Konwersja odczytuje wyłącznie eksport, który wskażesz. Nigdy nie łączy się z systemem, z którego zbiór danych Prophecy odczytuje dane lub do którego je zapisuje, i nigdy nie uruchamia kodu projektu.

Konwersja jest jednorazowym krokiem. Ponowna konwersja tego samego projektu tworzy nowe przepływy pracy i tabele, a zmiany wprowadzone w PlaidCloud nigdy nie są scalane z późniejszym eksportem.

## Co tworzy PlaidCloud

- Każdy gem Prophecy staje się odpowiednim krokiem przepływu pracy, z zachowaniem relacji nadrzędnych i podrzędnych.
- Parametry Prophecy stają się zmiennymi projektu, a odwołania do nich w ustawieniach gemów są przepisywane na składnię zmiennych PlaidCloud. Wartości parametrów możesz nadpisać podczas konwersji.
- Każdy zbiór danych odczytywany przez gem staje się krokiem importu lub odczytuje istniejącą tabelę albo dokument, zależnie od sposobu powiązania.
- Każdy job Prophecy lub harmonogram potoku SQL staje się [zaplanowanym zdarzeniem](/pl/administration/scheduled-events/) w skonwertowanym przepływie pracy, włączonym, jeśli jest włączony w Prophecy. Zobacz [Harmonogramy](#usługi-i-sterowanie).
- Skrypty, instrukcje SQL, makra i inny kod projektu trafiają do kroków, które ten kod zawierają. Zobacz [Kod projektu w krokach](#kod-projektu-w-krokach).
- Gem niestandardowy, w tym gem z Gem Builder, uruchamia kod, który eksport dla niego zawiera, w kroku Python. Zobacz [Kod projektu w krokach](#kod-projektu-w-krokach).
- Gem Pivot z warunkiem HAVING lub kolumną ze wszystkimi wartościami jest konwertowany, podobnie jak typy sortowania i Deduplicate oferowane przez Prophecy.
- Wyrażenia są konwertowane przy założeniu zachowania Spark SQL w zakresie obsługi wartości null, dzielenia całkowitoliczbowego i niejawnych rzutowań. Sprawdź wyniki tam, gdzie różnią się one na Twoim silniku PlaidCloud.

## Zanim zaczniesz

1. Wyeksportuj projekt z Prophecy jako plik `.zip` albo wyeksportuj pojedynczy potok, model lub podgraf jako plik `.json`.
2. Prześlij plik na [konto dokumentów](/pl/guides/documents/adding-accounts/), które możesz odczytać.
3. Wybierz projekt PlaidCloud, który ma otrzymać przepływy pracy. Potrzebujesz do niego uprawnień do zapisu.
4. Zdecyduj, skąd będą odczytywane pliki dla niepowiązanych zbiorów danych. Wybierz konto dokumentów i folder bazowy.

## Konwersja projektu

Konwertuj z aplikacji Analyze, przez REST API lub z katalogu narzędzi MCP. Wszystkie trzy przyjmują te same pola.

### Aplikacja Analyze

1. Otwórz **Analyze** i wybierz **Tools → Importuj projekt Prophecy**.
2. Wybierz **Projekt docelowy**, **Projekt Prophecy (.zip lub .json)** przesłany na konto dokumentów oraz **Lokalizacja plików źródłowych**, czyli konto dokumentów i folder bazowy, z których odczytywane są pliki niepowiązanych zbiorów danych.
3. W sekcji **Nazwy obiektów i opcje** możesz opcjonalnie ustawić prefiksy przepływów pracy, kroków i tabel, wybrać **Typ przepływu pracy** oraz zdecydować, czy importować nieskonwertowane komponenty jako zastępcze kroki przekazujące dane bez zmian.
4. W sekcji **Powiązania źródeł i parametry** możesz opcjonalnie powiązać zbiór danych z istniejącą tabelą, wpisując nazwę zbioru danych i identyfikator tabeli, oraz nadpisać parametry Prophecy według nazwy. Aby powiązać połączenia, użyj REST API lub narzędzia MCP. Zobacz [Wiązanie połączeń](#wiązanie-połączeń).
5. Wybierz **Importuj**.

Okno pokazuje postęp odczytu projektu, analizy potoków, mapowania ich na operacje PlaidCloud oraz tworzenia przepływów pracy, tabel i kroków. Po zakończeniu okno pokazuje raport z konwersji: liczbę kroków według pewności, ostrzeżenia, konwersje częściowe, nieskonwertowane elementy zastępcze, pominięte komponenty i pliki źródłowe do przesłania.

### Pola

REST API i narzędzie MCP przyjmują te pola.

| Pole | Wymagane | Co robi |
| --- | --- | --- |
| `source_account_id` | Tak | Konto dokumentów zawierające eksport Prophecy. |
| `source_file_path` | Tak | Ścieżka pliku `.zip` projektu albo pojedynczego pliku `.json` potoku, modelu lub podgrafu na tym koncie. |
| `project_id` | Tak | Projekt, w którym tworzone są przepływy pracy. |
| `document_account_id` | Tak | Konto dokumentów, z którego odczytywane są niepowiązane zbiory danych. |
| `document_account_path` | Tak | Folder bazowy na tym koncie dla niepowiązanych zbiorów danych. Pusta wartość lub `/` oznacza katalog główny konta, a początkowy `/` jest ignorowany. Ścieżki z `..` lub segmentami zaczynającymi się od kropki, nawiasami klamrowymi, literą dysku lub schematem URL albo znakami sterującymi są odrzucane. |
| `workflow_prefix` | Nie | Prefiks dodawany do nazw przepływów pracy. |
| `step_prefix` | Nie | Prefiks dodawany do nazw kroków. |
| `table_prefix` | Nie | Prefiks dodawany do nazw tabel. Domyślnie jest to nazwa samego przepływu pracy. Prefiks, który użyłby ponownie istniejącej nazwy tabeli, jest odrzucany, zanim cokolwiek zostanie utworzone. Użyty prefiks jest zwracany w raporcie z konwersji. |
| `workflow_type` | Nie | `advanced` (domyślnie) układa graf na kanwie DAG. `standard` tworzy szeregową listę kroków. |
| `source_bindings` | Nie | Wiąże zbiory danych i operacje z istniejącymi danymi. Zobacz [Wiązanie źródeł](#wiązanie-źródeł). |
| `connection_bindings` | Nie | Wiąże bazy danych, magazyny plików, API REST i pocztę, do których sięga projekt, z połączeniami PlaidCloud i kontami dokumentów. Zobacz [Wiązanie połączeń](#wiązanie-połączeń). |
| `parameters` | Nie | Nadpisuje parametry Prophecy. Zobacz [Parametry](#parametry). |
| `allow_unconverted_placeholders` | Nie | Określa, co robi krok zastępczy w czasie wykonania. Zobacz [Kroki zastępcze dla nieskonwertowanych gemów](#kroki-zastępcze-dla-nieskonwertowanych-gemów). |

### REST

Wyślij pola jako treść JSON pod adres:

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

Potrzebujesz roli `analyze.workflow.write`.

### MCP

Agent AI połączony przez MCP wywołuje narzędzie `prophecy_convert` z tymi samymi polami. Informacje o łączeniu agenta znajdziesz w [agentach AI (MCP)](/pl/integrations/ai-coding-agents/). Narzędzie zmienia Twój projekt, więc przejrzyj wywołanie, zanim je zatwierdzisz.

## Wiązanie źródeł

Eksport Prophecy opisuje, skąd pochodzą jego dane, ale nie zawiera danych ani poświadczeń. Użyj `source_bindings`, aby połączyć każdy zbiór danych z danymi, które już masz w PlaidCloud. Kluczem jest nazwa zbioru danych, tak jak wymienia ją raport z konwersji. Wartością jest:

- Identyfikator `analyzetable_` tabeli w projekcie docelowym. Skonwertowany przepływ pracy odczytuje tę tabelę bezpośrednio.
- Obiekt z polami `account`, `path` i opcjonalnie `sheet`, aby odczytać plik z konta dokumentów.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Powiązanie, którego nie możesz odczytać, jest odrzucane. Klucz, który nie pasuje do żadnego zbioru danych, jest zgłaszany jako ostrzeżenie. Okno Analyze wiąże zbiory danych z tabelami; aby powiązać zbiór danych z plikiem dokumentu, użyj REST API lub narzędzia MCP.

### Niepowiązane zbiory danych

Zbiór danych bez powiązania staje się krokiem importu bez danych, a raport z konwersji zawiera dla niego ostrzeżenie. Krok odczytuje dane z:

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Prześlij plik pod tę ścieżkę i uruchom przepływ pracy. Dopóki pliku nie ma, krok importu kończy się z ostrzeżeniem i tworzy pustą tabelę, a przepływ pracy jest kontynuowany. Raport wymienia każdą ścieżkę w sekcji **Pliki źródłowe do przesłania**.

### Wiązanie operacji na tabelach i plikach

Gemy zmieniające tabele lub pliki, takie jak Table Operations (update, delete, drop) i File Operation (copy), działają tylko na danych utworzonych przez konwersję. Aby jeden z nich mógł działać na danych, które już istnieją, powiąż je kluczem w postaci `operation:<pipeline>/<id>`, gdzie `<pipeline>` to nazwa potoku, a `<id>` to identyfikator gema. Raport z konwersji podaje klucz dla każdego takiego gema.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

Destrukcyjna operacja na tabeli lub pliku jest uruchamiana tylko wtedy, gdy ją powiążesz. Bez powiązania gem Table Operations działa na tabeli zapisanej przez inny gem tego samego projektu, a w przeciwnym razie staje się krokiem zastępczym, który podaje swój klucz. File Operation kopiuje ze swojego własnego folderu tymczasowego. Nic poza tabelami i folderami samej konwersji nie jest zmieniane, dopóki tego nie powiążesz.

## Wiązanie połączeń

Projekt Prophecy sięga do baz danych, magazynów plików, API REST i serwerów poczty przez połączenia. Eksport zawiera nazwy połączeń, ale nie zawiera poświadczeń, więc użyj `connection_bindings`, aby wskazać każdemu z nich istniejące połączenie PlaidCloud lub konto dokumentów. Raport z konwersji wymienia każdy klucz w sekcji powiązań.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

Kluczem jest jedno z:

| Klucz | Co wiąże | Wartość |
| --- | --- | --- |
| `connection:<name>` | Połączenie Prophecy, które nazywa gem lub zbiór danych bazy danych. Jedno powiązanie obsługuje każdy gem na tym połączeniu. Gem, który nie nazywa połączenia, używa `connection:<pipeline>/<gem id>`, a zbiór danych bazy danych używa `connection:<dataset name>`. | Identyfikator połączenia PlaidCloud: połączenie z bazą danych (w tym BigQuery i SAP HANA), połączenie MongoDB lub Apache Kafka, połączenie Salesforce dla odczytów i zapisów Salesforce, połączenie Tableau dla gema Tableau, połączenie REST dla Azure Cosmos DB, Pinecone, Power BI oraz zapisów Smartsheet i Slack lub połączenie oparte na Singer dla odczytów Smartsheet, Slack i Iceberg. Identyfikator konta dokumentów dla gema File Storage lub Directory. |
| `operation:<pipeline>/<gem id>` | Gem REST wysyłający cokolwiek poza GET, HEAD lub OPTIONS oraz każdy gem Email. | Identyfikator połączenia. Dla REST jest to połączenie REST przechowujące poświadczenie. |

Powiązanie jest Twoją zgodą dla gemów, które zmieniają rzeczy poza konwersją:

- Żądanie REST, które może zmienić dane przechowywane przez API, oraz e-mail docierający do prawdziwych osób są konwertowane na działające kroki tylko wtedy, gdy powiążesz ich klucz `operation:`. Bez powiązania gem jest krokiem zastępczym, który podaje klucz.
- Konto dokumentów powiązane z gemem File Storage lub Directory pozwala krokom tego gema zapisywać, usuwać lub przenosić pliki na tym koncie.
- Żądanie GET, HEAD lub OPTIONS jest wysyłane tak, jak wysyła je gem. Bez powiązania nie ma poświadczenia, dopóki nie wybierzesz połączenia REST w skonwertowanym kroku.

Zbiór danych bazy danych lub gem External Table bez powiązania jest konwertowany na krok, który podaje swój klucz i czeka, aż wybierzesz połączenie, a raport zawiera ostrzeżenie. Skonwertuj ponownie z powiązanym kluczem albo wybierz połączenie w kroku. Powiązanie, którego identyfikator wskazuje niewłaściwy rodzaj magazynu dla jego gemów lub którego nie możesz użyć, jest odrzucane. Klucz, który nie pasuje do niczego, jest zgłaszany jako ostrzeżenie.

## Parametry

`parameters` nadpisuje parametry Prophecy podczas konwersji:

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` nazywa instancję konfiguracji. `values` to tekst, liczby lub wartości logiczne. Wpis potoku nadpisuje wartości całego projektu dla tego potoku. Raport wymienia użyte parametry oraz te, którym zmieniono nazwy, aby pasowały do nazw zmiennych PlaidCloud.

## Czytanie raportu z konwersji

Odpowiedź zawiera raport z konwersji. Przeczytaj go przed uruchomieniem przepływów pracy.

| Sekcja | Co mówi |
| --- | --- |
| Podsumowanie | Ile kroków zostało skonwertowanych z wysoką, średnią lub niską pewnością i ile nie zostało skonwertowanych. |
| Ostrzeżenia | Wszystko, co konwerter założył, przybliżył lub pominął, w tym niepowiązane zbiory danych i klucze powiązań, które do niczego nie pasują. |
| Konwersje częściowe | Kroki, które są konwertowane, ale różnią się od gema w jakimś trybie lub opcji. Każdy zawiera uwagę, co sprawdzić. |
| Nieskonwertowane elementy zastępcze | Gemy bez odpowiednika w PlaidCloud, wraz z powodem. |
| Pominięte komponenty | Gemy, które nie wykonują własnej pracy, takie jak znaczniki granic przepływu sterowania, oraz krok, który każdy z nich wchłonął. |
| Pliki źródłowe do przesłania | Ścieżka dokumentu, z której odczytywany jest każdy niepowiązany zbiór danych. |
| Przepływy pracy | Przepływ pracy utworzony dla każdego potoku, w kolejności uruchamiania. Potok odrzucony przez konwerter jest oznaczony. |

Raport podaje także użyty prefiks tabel i zastosowane parametry. Krok, co do którego konwerter nie ma pewności, jest konwertowany według najbardziej prawdopodobnej interpretacji i zawiera uwagę w raporcie. Sprawdź te kroki względem wyników z Prophecy.

## Kod projektu w krokach

Projekty Prophecy zawierają kod: gemy Script, instrukcje SQL, makra, dynamiczne wejścia, wywołania procedur składowanych i gemy niestandardowe. Konwerter nie uruchamia tego kodu. Umieszcza go w kroku:

- SQL jest tłumaczony na dialekt SQL Twojego tenanta i umieszczany w kroku SQL, a dane wejściowe gema są dostępne pod nazwami, pod którymi odczytuje je zapytanie.
- Skrypty Python są umieszczane w kroku Python, z przepisanym dostępem do tabel. Skrypt wywołujący metody ramek danych Spark zachowuje te wywołania i uruchamia je w kroku.
- Gem niestandardowy, w tym gem z Gem Builder, uruchamia w kroku Python kod PySpark, który eksport jego potoku dla niego zawiera.
- Makro ze znanego pakietu dbt staje się standardowymi krokami, które robią to, co makro. Makro w Twoim własnym projekcie lub w pakiecie zawartym w eksporcie jest również odczytywane i konwertowane, w tym bloki if i for, set, filtry, zagnieżdżone makra i adapter dispatch.
- Zdefiniowana przez użytkownika funkcja agregująca w Pythonie w gemie Aggregate jest uruchamiana w kroku Python dla każdej grupy.

Każdy krok zawierający kod projektu otrzymuje ostrzeżenie, podobnie jak przetłumaczony SQL. Przejrzyj kod w każdym takim kroku przed uruchomieniem przepływu pracy. Konwerter wstrzymuje wszystko, co przypomina poświadczenie, w ciągach znaków i komentarzach kodu, więc dodawaj poświadczenia do połączenia, a nie do kodu.

## Kroki zastępcze dla nieskonwertowanych gemów

Gem, którego konwerter nie potrafi odtworzyć, jest tworzony jako krok zastępczy noszący nazwę gema. Przykłady to gem niestandardowy, którego kodu nie ma w eksporcie, oraz gem zmieniający dane poza konwersją, taki jak żądanie REST mogące zmienić dane, Email albo operacja na tabeli lub pliku, gdy nie powiązałeś jego klucza `operation:`. Zbiór danych bazy danych lub External Table bez powiązanego połączenia nie jest krokiem zastępczym: jest konwertowany na krok, który czeka, aż wybierzesz połączenie. Domyślnie krok zastępczy kończy się niepowodzeniem, gdy przepływ pracy do niego dotrze, więc uruchomienie nie może zgłosić sukcesu dla pracy, która nigdy nie została wykonana.

Ustaw `allow_unconverted_placeholders` na `true` (w oknie: **Importuj nieskonwertowane komponenty jako zastępcze kroki przekazujące dane bez zmian**), aby zaimportować każdy krok zastępczy jako krok przekazujący dane bez zmian. Uruchomienie jest wtedy kontynuowane za nim, a wynik kroku zastępczego jest jego wejściem. Raport zlicza kroki zastępcze przekazujące dane i wymienia ich kroki. Odbuduj tę funkcjonalność za pomocą natywnego kroku, gdy jej wynik ma znaczenie.

## Uruchamianie skonwertowanych przepływów pracy

1. Otwórz nowe przepływy pracy w projekcie. Raport wymienia je w kolejności uruchamiania.
2. Ustaw wszystkie zmienne projektu pochodzące z parametrów Prophecy.
3. Prześlij pliki dla niepowiązanych zbiorów danych pod ścieżki podane w raporcie.
4. Przejrzyj kroki zawierające kod projektu.
5. Uruchom przepływy pracy i przejrzyj tabelę wyjściową każdego kroku.

Zaplanowane zdarzenia utworzone z harmonogramów Prophecy są włączone, jeśli były włączone w Prophecy, więc zaczynają uruchamiać skonwertowane przepływy pracy zgodnie z harmonogramem. Aby najpierw przejrzeć przepływy pracy, wyłącz zdarzenia w sekcji [Zaplanowane zdarzenia](/pl/administration/scheduled-events/) i włącz je, gdy będziesz gotowy.

## Co jest konwertowane

Każdy gem Prophecy jest konwertowany w pełni na natywne kroki, zmienne projektu, zaplanowane zdarzenia lub obiekty na kanwie, wraz z oferowanymi opcjami. [Macierz konwersji Prophecy](/pl/reference/prophecy-conversion-matrix/) wymienia każdy gem wraz z krokiem PlaidCloud, którym się staje, a [Przypadki brzegowe](#przypadki-brzegowe) wymieniają nieliczne zachowania do sprawdzenia; raport z konwersji wskazuje każde z nich tam, gdzie występuje.

### Przenoszenie danych

| Możliwość | Jak jest konwertowana |
| --- | --- |
| Tryby zapisu | Docelowe tryby zapisu są konwertowane na kroki platformy: SCD2 ze strategiami check i timestamp (strategia timestamp datuje każdą wersję na podstawie kolumny wskazanej przez `scd2.updatedAtColumn` gema), merge, `replaceWhere` i `insertInto`. Merge stosuje wyrażenia SET dla poszczególnych kolumn z klauzul matched-update i not-matched-insert; klauzula, która nie ustawia żadnej kolumny, bierze każdą kolumnę z wiersza przychodzącego. Pierwsze uruchomienie na pustym celu zapisuje każdy wiersz, tak jak robią to dbt i Delta. Pierwsze uruchomienie nie wymaga wcześniej utworzonej tabeli, także dla potoku, który odczytuje zbiór danych, który również zapisuje, chyba że eksport nie podaje, jakie kolumny ma ten zbiór danych: wtedy utwórz tabelę przed pierwszym uruchomieniem. Kolejne uruchomienia stosują filtr przyrostowy lub warunek merge. Tryby `error` i `ignore` sprawdzają za pomocą [warunku istnienia tabeli](/pl/guides/workflows/step-conditions/#warunki-istnienia-tabeli). |
| Time travel | Źródło tabeli Delta lub katalogu, które odczytuje wcześniejszą wersję swojej tabeli, przez `versionAsOf` lub `timestampAsOf`, odczytuje tę wersję z Databricks przez powiązane przez Ciebie połączenie. |
| Strumieniowanie | Źródła i cele strumieniowe działają jako zaplanowana partia. Ujście strumieniowe zastępuje swoją tabelę zamiast dołączać dane, więc ponowne uruchomienie nigdy nie duplikuje wierszy. Zaplanuj przepływ pracy, aby pobierał nowo nadeszłe dane. |
| Bazy danych | Gemy JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA i External Table odczytują i zapisują przez powiązane przez Ciebie połączenie PlaidCloud. Zbiór danych BigQuery jest odczytywany za pomocą [Importuj SQL](/pl/reference/workflow-steps/import/import-sql/) i zapisywany za pomocą [Export External Database Tables](/pl/reference/workflow-steps/export/export-external-tables/) na [połączeniu BigQuery](/pl/reference/connectors/google/big-query/). Tabela SAP HANA zapisywana w dowolnym z trybów merge gema HANA, w tym SCD2 i trybach usuwania, jest umieszczana obok celu i scalana z nim według klucza głównego celu lub kolumn merge gema; brakujący cel jest najpierw tworzony. |
| MongoDB i Kafka | Zbiór danych MongoDB jest odczytywany za pomocą [Importuj MongoDB](/pl/reference/workflow-steps/import/import-mongodb/), wraz z jego filtrem lub potokiem agregacji, a odczyt, który nie deklaruje kolumn, bierze je z pierwszych dokumentów, tak jak robi to konektor Spark. Zapis używa [Eksportuj MongoDB](/pl/reference/workflow-steps/export/export-mongodb/) w odpowiednim trybie zapisu: `update` aktualizuje pola pasującego dokumentu lub wstawia nowy, `ignore` zapisuje tylko wtedy, gdy kolekcja nie zawiera żadnego dokumentu, a `error` zatrzymuje uruchomienie, gdy go zawiera. Źródło Kafka odczytuje swoje tematy między offsetami początkowym i końcowym za pomocą [Importuj Kafka](/pl/reference/workflow-steps/import/import-kafka/), a cel Kafka wysyła każdy wiersz za pomocą [Eksportuj Kafka](/pl/reference/workflow-steps/export/export-kafka/). Zbiór danych Kafka, który loguje się przez `OAUTHBEARER`, używa [logowania OAuth](/pl/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) powiązanego przez Ciebie połączenia Kafka, ponieważ eksport nie zawiera poświadczeń. |
| Azure Cosmos DB | Odczyt wysyła zapytanie zbioru danych albo odczytuje każdy dokument za pomocą [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) na połączeniu REST z uwierzytelnianiem Cosmos DB i podąża za nagłówkiem kontynuacji od strony do strony. Zapis wysyła jedno żądanie dla każdego wiersza według strategii zapisu gema: overwrite, append, delete lub patch. Wiersz niosący ETag swojego dokumentu jest zastępowany lub usuwany tylko wtedy, gdy dokument nie zmienił się od tego czasu, a wiersz odrzucony przez kontener z tego powodu albo z powodu brakującego lub istniejącego dokumentu jest pomijany, tak jak robi to konektor Spark. Tryb `ignore` zapisuje tylko wtedy, gdy kontener nie zawiera żadnego dokumentu. |
| Salesforce | Odczyt używa [Salesforce: zapytanie o obiekt](/pl/reference/workflow-steps/salesforce/query-salesforce-object/), wraz z usuniętymi i zarchiwizowanymi rekordami, gdy gem o nie prosi. Zapis wstawia, aktualizuje, wykonuje upsert lub usuwa, z jednym żądaniem na wiersz; upsert dopasowuje według pola zewnętrznego identyfikatora gema, a gdy żadnego nie nazywa, według `Id`. |
| Smartsheet, Slack i Pinecone | Odczyt Smartsheet nazwanego arkusza ze zadeklarowanymi kolumnami pobiera arkusz przez Twoje połączenie REST i zapisuje wiersz dla każdego wiersza arkusza, kolumnę dla każdej zadeklarowanej kolumny. Inne odczyty Smartsheet oraz odczyty Slack i Iceberg używają [Import Singer Source](/pl/reference/workflow-steps/import/import-singer/). Zapis Smartsheet dodaje wiersze do nazwanego arkusza, a overwrite najpierw usuwa wiersze arkusza. Zapis Slack publikuje jedną wiadomość dla każdego wiersza, a wiadomość odrzucona przez Slack powoduje niepowodzenie kroku. Indeks Pinecone jest odczytywany jako jego wektory i ich metadane, a zapis wykonuje upsert wierszy jako wektorów. |
| Tableau i Power BI | Tableau i Tableau Write publikują dane wejściowe jako ekstrakt Hyper za pomocą [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/) na powiązanym przez Ciebie połączeniu Tableau. Power BI Write wysyła dane wejściowe do zbioru danych push Power BI przez połączenie REST z OAuth 2.0, znajdując obszar roboczy według nazwy i tworząc zbiór danych, gdy jest nowy. |
| Formaty plików | CSV, JSON, Parquet, Avro, Excel, XML, o stałej szerokości oraz ORC przez [Importuj ORC](/pl/reference/workflow-steps/import/import-orc/). Opcje formatu są mapowane lub oznaczane jako neutralne, gdy nie zmieniają żadnego wiersza: okno czasu modyfikacji odczytu Avro, kodowanie EBCDIC pliku o stałej szerokości, rekordy nagłówka i stopki oraz rekordy bez podziałów wierszy, mapa arkuszy i hasło odczytu Excela, opcje cudzysłowów zapisu CSV oraz zapis Excela z jednym arkuszem dla każdej wartości. Skompresowane pliki tekstowe są odczytywane i zapisywane za pomocą gzip, Deflate (zlib), Zstandard, LZ4, Snappy i LZO; skompresowany plik jest odczytywany, gdy jego nazwa kończy się rozszerzeniem jego kodeka. Zaszyfrowane pliki są deszyfrowane i szyfrowane w miejscu. Zobacz [Zaszyfrowane pliki](#zaszyfrowane-pliki). |
| File Operation | Copy i Move są konwertowane na [Dokument: kopiuj plik](/pl/reference/workflow-steps/document/copy-document-file/) lub Copy Directory na powiązanym przez Ciebie folderze, zachowując tylko pliki, których nazwa pasuje do `filenameRegex` gema, i zachowując ścieżkę każdego pliku poniżej folderu źródłowego, gdy gem działa rekurencyjnie. |
| Directory | Wyświetla pliki powiązanego folderu dokumentów za pomocą [Lista katalogu](/pl/reference/workflow-steps/document/directory-listing/), w kolumnach gema. Z włączoną opcją nazwy arkusza każdy skoroszyt Excela daje jeden wiersz na arkusz i jego `sheet_name`; inne pliki dają jeden wiersz z pustym `sheet_name`. |

### Kolumny i wiersze

| Gem lub funkcja | Jak jest konwertowana |
| --- | --- |
| Surrogate Key | Klucze są kontynuowane z tabeli, która przechowuje ostatni wydany klucz, tak jak robi to plik kluczy gema. Każdy gem, który nazywa ten sam plik kluczy, współdzieli tę tabelę, więc ich klucze nigdy się nie nakładają. Uruchomienie bez wierszy pozostawia ją bez zmian, a klucze zaczynają się od wartości początkowej, zanim jakiekolwiek uruchomienie wyda pierwszy klucz. |
| Column Parser, XML Parse, parsowanie JSON | Tekst XML i JSON jest parsowany za pomocą kroków [Analiza XML](/pl/reference/workflow-steps/tables/table-xml-parse/) i [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/), odczytując każde pole z tekstu elementu, atrybutu lub elementu podrzędnego. XML parsowany bez schematu bierze typ każdego pola z danych, tak jak robi to `schema_of_xml` w Spark. |
| Business rules | Reguła biznesowa projektu wywołana w wyrażeniu jest konwertowana na te same warunki, jeden `CASE` dla każdej kolumny, którą ustawia. |
| Casts | Rzutowanie tekstu na liczbę dziesiętną lub long jest zgodne ze Spark co do joty: spacje i znaki sterujące wokół liczby są przycinane, liczba dziesiętna jest zaokrąglana w górę od połowy do swojej skali, a tekst, który nie jest liczbą, lub wartość spoza zakresu daje null. |
| Daty i godziny | Formaty daty i godziny są zapisywane dla silnika Twojego obszaru roboczego, w tym Databend, a `window()` umieszcza każdy znacznik czasu w jego oknie tumbling, wyrównanym tak, jak wyrównuje je Spark. |
| Wyniki iteratorów | Table Iterator lub While Iterator, których kolumny wyjściowe są znane dopiero w czasie wykonania, zbiera wiersze każdego przejścia według pozycji za pomocą [Tabela: suma wszystkich](/pl/reference/workflow-steps/tables/table-union-all/#dopasowanie-kolumn), z każdą kolumną rozszerzoną do typu, do którego pasuje każde przejście, tak jak Prophecy układa przejścia jedno na drugim. |
| Data Encoder/Decoder AES | Działa na każdym silniku. Klucz, a także wektor inicjujący i dane dodatkowe, gdy gem je nazywa, pochodzą ze zmiennych przepływu pracy `aes_key`, `aes_iv` i `aes_aad`, które ustawiasz. |
| Data Masking hash | Oblicza te same wartości co `hash()` w Spark. |
| Buffer, Simplify, Heat Map | Buffer rysuje zaokrąglony narożnik z taką samą liczbą segmentów jak Prophecy, Simplify usuwa te same wierzchołki, a Heat Map sumuje ciepło w sześciokątach H3 w rozdzielczości gema, przy czym dziesiętne ciepło pozostaje dziesiętne. |

### Usługi i sterowanie

| Gem | Jak jest konwertowany |
| --- | --- |
| Pipeline | Uruchamia potok, który nazywa, za pomocą [Workflow Loop](/pl/reference/workflow-steps/workflow-control/workflow-loop/), raz dla każdego wiersza wejściowego (raz, gdy nie ma wejścia, nigdy dla braku wierszy), z każdym parametrem ustawianym ze stałej, kolumny wiersza lub wyrażenia na jego podstawie. Każde uruchomienie jest wykonywane, nawet gdy wcześniejsze się nie powiedzie, a wynik gema zawiera jeden wiersz dla każdego uruchomienia z jego statusem, komunikatem i czasami, tak jak rejestruje je Prophecy. |
| Harmonogramy | Job Prophecy lub harmonogram potoku SQL staje się [zaplanowanym zdarzeniem](/pl/administration/scheduled-events/) o nazwie `Prophecy <name>` w skonwertowanym przepływie pracy, włączonym, chyba że jest wyłączony w Prophecy. Job Spark jest konwertowany w ten sposób, gdy uruchamia jeden skonwertowany potok bez nadpisań konfiguracji ani warunków uruchomienia. |
| Script | Skrypt Python jest umieszczany w kroku Python. Wartość ustawiona przez skrypt w `Config` staje się zmienną przepływu pracy, którą odczytują późniejsze kroki, resetowaną do wartości potoku na początku każdego uruchomienia, tak jak `Config` w Prophecy. |
| REST API, REST API Enrich | Kroki [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/), jedno żądanie dla każdego wiersza wejściowego, z zachowaniem odpowiedzi z błędem, tak jak robi to Prophecy. Enrich odczytuje także status, powód i końcowy adres URL. Żądanie, które czeka na wynik asynchroniczny, odpytuje, dopóki odpowiedź nie powie, że jest gotowe. |
| Stored Procedure | Gem przekazujący argumenty wywołuje swoją procedurę za pomocą [Zdalne wykonanie: SQL](/pl/reference/workflow-steps/agent/agent-remote-execution-of-sql/#uruchamianie-instrukcji-raz-na-wiersz) raz dla każdego wiersza wejściowego, z każdym argumentem powiązanym ze swojej kolumny jako parametr. Gem bez argumentów wywołuje ją raz przez Agenta. Wybierz połączenie lub agenta w skonwertowanym kroku. |
| Email, Email Data | [Notify Via Email](/pl/reference/workflow-steps/notifications/notify-via-email/) z Cc, Bcc, Reply-To i jedną wiadomością dla każdego wiersza, gdy pole jest odczytywane z kolumny. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/pl/reference/workflow-steps/text-documents/nlp-ai/) na połączeniu LLM Twojego obszaru roboczego. Osadzenia OpenAI i Bedrock używają zadania Embed, które wymaga połączenia zgodnego z OpenAI lub Azure OpenAI; połączenie Anthropic jest odrzucane. |
| Pinecone Lookup | Żądanie REST dla każdego wiersza. |
| Data Quality Check, Deequ, Soda | Sprawdzenia działają w hurtowni danych i zapisują tabelę wyników. Data Quality Check zatrzymuje uruchomienie tylko wtedy, gdy gem ustawia `minFailedChecks` lub akcję końcową `fail_pipeline`; w przeciwnym razie tabela wyników wymienia niepowodzenia. Deequ i Soda nigdy nie zatrzymują uruchomienia. Sprawdzenie minimalnej lub maksymalnej długości na kolumnie liczbowej mierzy liczbę jako tekst. Sprawdzenia Soda są konwertowane z YAML projektu, w tym brakujące, nieprawidłowe i prawidłowe wartości, statystyki, długości, percentyle, duplikaty w kolumnach, aktualność, nieudane wiersze i Twoje własne zapytania metryk. |
| ToDo | Zgłasza błąd, który podaje oryginalne narzędzie i komunikat, gdy uruchomienie do niego dotrze. |

### Zaszyfrowane pliki

Gem File Storage, który odczytuje zaszyfrowany plik, jest konwertowany na [Dokument: odszyfrowanie pliku](/pl/reference/workflow-steps/document/encrypt-decrypt-file/), który odszyfrowuje plik do własnego folderu, zanim import go odczyta; odszyfrowana kopia jest potem usuwana. Gem, który zapisuje zaszyfrowany plik, eksportuje do tego folderu, a następnie szyfruje plik na miejscu za pomocą Dokument: szyfrowanie pliku. Obsługiwane są pliki AES i Blowfish oraz skoroszyty Excela chronione hasłem.

Eksport nigdy nie zawiera klucza, więc skonwertowane kroki odczytują go ze zmiennej przepływu pracy: `aes_key` dla klucza AES lub Blowfish i `xlsx_password` dla hasła skoroszytu. Ustaw zmienną przed uruchomieniem przepływu pracy i nadaj jej klucz przeznaczony wyłącznie dla tych plików. Pola klucza i hasła przyjmują wyłącznie odwołanie do zmiennej, więc klucz nigdy nie jest wpisywany w kroku.

## Przypadki brzegowe

To zachowania, których skonwertowany przepływ pracy nie odtwarza samodzielnie. Raport z konwersji wskazuje każde z nich tam, gdzie występuje.

- **Kod lub dane, których nie ma w eksporcie**: Gem z Gem Builder lub inny gem niestandardowy, którego kodu nie ma w eksporcie, oraz wywołanie makra pakietu dbt, który eksport pomija, stają się krokiem, który podaje, czego brakuje; wyeksportuj projekt wraz z kodem potoku i pakietami dbt albo odbuduj logikę w kroku Python lub SQL. Gemy Ab Initio Error Detection i MTime przekazują swoje dane wejściowe bez zmian, ponieważ reguła, którą stosują, nie jest zawarta w eksporcie. Sprawdzenia Soda odczytywane z pliku spoza projektu oraz sprawdzenia Soda, które porównują z wcześniejszymi skanami lub z innym zbiorem danych albo testują format nazwany przez Soda, nie mają wiersza w tabeli wyników; oblicz je w późniejszym kroku.
- **Wyniki znane dopiero podczas uruchomienia potoku**: Gem REST API, który spłaszcza swoją odpowiedź, umieszcza całą odpowiedź w jednej kolumnie, gdy nic nie deklaruje nazw pól, co ujawnia dopiero uruchomienie; wyodrębnij potrzebne pola w późniejszym kroku. Makro dbt, które odpytuje hurtownię danych podczas kompilacji dbt, staje się krokiem, który je nazywa; zastąp zapytanie wartościami, które zwraca. Gem Spark StoredProcedure działa, ale jego wartości OUT nie są zwracane; wynikiem są kolumny przekazywane bez zmian. `input_file_name()` zwraca pusty ciąg dla źródła tabeli lub Delta, które nie ma pliku do nazwania, a `hash()` / `xxhash64()` wewnątrz agregatu, okna lub gema z kilkoma wejściami są obliczane przez hurtownię danych, więc mogą różnić się od wyników Spark.
- **Wartości zapisane w kroku podczas konwersji projektu**: Wartość parametru zawierająca cudzysłów, ukośnik odwrotny lub nawias klamrowy, wartość potoku odczytywana przez krok SQL oraz baza danych, którą operacja na tabeli Delta nazywa przez konfigurację, są zapisywane w kroku jako stałe wartości, więc zmiana zmiennej przepływu pracy ich nie zmienia; edytuj krok, gdy zmienia się konfiguracja.
- **Kod Scala**: Skrypt Scala, wyrażenie Scala oraz zdefiniowana przez użytkownika funkcja Scala lub funkcja agregująca stają się krokiem, który je nazywa; przepisz je w SQL lub Python.
- **Logowanie Kerberos w Kafka**: Źródło lub cel Kafka, który loguje się przez Kerberos (GSSAPI), jest konwertowany bez nazwy usługi Kerberos i mechanizmu logowania; ustaw je w połączeniu PlaidCloud.
- **Strumieniowanie**: Źródła, cele i potoki strumieniowe działają jako przepływy pracy wsadowe na danych obecnych w chwili uruchomienia; zaplanuj uruchamianie przepływu pracy tak często, jak potrzebujesz.
- **Komponenty jobów**: Job Spark konwertuje swój jeden potok i harmonogram; jego pozostałe komponenty, warunki uruchomienia i nadpisania konfiguracji nie są konwertowane.
- **Nietypowe wywołania**: Zdefiniowana przez użytkownika funkcja agregująca wywołana z rollup lub okna oraz makro dbt używające Jinja poza if, for, set i typowymi filtrami stają się krokiem, który nazywa gem; wywołaj funkcję z gema Aggregate albo wstaw makro w miejscu.

## Powiązane przewodniki

- [Migracja analiz Savant](/pl/guides/workflows/migrate-savant-analyses/)
- [Migracja przepływów pracy Alteryx](/pl/guides/workflows/migrate-alteryx-workflows/)
- [Dodawanie kont dokumentów](/pl/guides/documents/adding-accounts/)
- [Zarządzanie zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/)
- [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/)
