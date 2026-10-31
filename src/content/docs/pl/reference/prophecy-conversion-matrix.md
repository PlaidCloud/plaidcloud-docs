---
title: Macierz konwersji Prophecy
description: Jak PlaidCloud konwertuje potoki i projekty SQL Prophecy na natywne kroki zaawansowanych przepływów pracy, ze statusem obsługi każdego gemu.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud konwertuje potoki Spark i projekty SQL Prophecy na natywne
zaawansowane przepływy pracy. Importer mapuje każdy gem Prophecy na krok przepływu pracy,
zmienną projektu lub obiekt kanwy, dzięki czemu skonwertowany przepływ pracy działa natywnie w chmurze,
a nie jako emulacja.

Każdy gem, konektor i struktura projektu podlega konwersji: **Pełny** oznacza, że gem
staje się natywnym krokiem, zmienną lub obiektem kanwy PlaidCloud, który wykonuje
pracę gemu. Nieliczne zachowania, których skonwertowany przepływ pracy nie odtwarza
samodzielnie, wymieniono w sekcji [Znane przypadki brzegowe](#znane-przypadki-brzegowe), każde wraz z tym, co
należy zrobić.

Aby przeprowadzić konwersję, zobacz [Migracja projektów Prophecy](/pl/guides/workflows/migrate-prophecy-projects/).

## Gemy potoków Spark

### Źródło/cel

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Lookup | Pełny | [Tabela: wyszukiwanie](/pl/reference/workflow-steps/tables/table-lookup/) | Każde wywołanie lookup staje się krokiem wyszukiwania w kroku, który go używa; klucz bez dopasowania zwraca NULL, a zduplikowany klucz zwraca jeden ze swoich wierszy. |
| Source | Pełny | Krok importu wybrany według formatu zbioru danych (zobacz [Konektory](#konektory)) | Każdy Source staje się krokiem importu do tabeli nazwanej od zbioru danych; format nierozpoznany przez konwerter jest odczytywany jako plik CSV przesłany do folderu dokumentów przepływu pracy, z ostrzeżeniem. |
| Streaming Source | Pełny | Ten sam import co dla wsadowego Source | Źródła strumieniowe konwertują się na jednorazowy import wsadowy z ostrzeżeniem. |
| Streaming Target | Pełny | Wsadowe ładowanie z dołączaniem | Cele strumieniowe konwertują się na wsadowe dołączanie z ostrzeżeniem. |
| Target | Pełny | Krok eksportu/ładowania tabeli wybrany według formatu zbioru danych i writeMode | Każdy Target staje się krokiem ładowania lub eksportu tabeli w trybie zapisu gemu: append, overwrite, merge z wyrażeniami SET, upsert, SCD2, replaceWhere i insertInto. |

### Przygotowanie

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Data Cleansing | Pełny | Wyrażenia kolumn w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Konwertuje opcje wypełniania wartości null, przycinania i wielkości liter na wyrażenia kolumn; oczyszczone kolumny przechodzą na koniec. |
| Sequence | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem numeru wiersza | Dodaje kolumnę sekwencji na podstawie wartości początkowej i przyrostu. |
| Surrogate Key Generator | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem numeru wiersza | Dodaje klucz sekwencyjny od wartości początkowej; klucze są kontynuowane między uruchomieniami z tabeli przechowującej ostatnio wydany klucz. |

### Transformacja

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Aggregate | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z agregacją; krok [Pivot](/pl/reference/workflow-steps/tables/table-pivot/), gdy gem wykonuje pivot | Grupuje i agreguje, stosuje warunek HAVING oraz obraca do jednej kolumny na wartość pivot; propagate-all przenosi wszystkie pozostałe kolumny wejściowe. |
| Bulk Column Expressions | Pełny | Rozwinięcie do jednego wyrażenia na kolumnę w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Jedno wyrażenie na każdą wymienioną kolumnę w kroku Table Extract; konwersja ostrzega, że przyjęto układ gemu. |
| Bulk Column Rename | Pełny | Zmiana nazwy kolumny w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Jedna zmiana nazwy na każdą wymienioną kolumnę w kroku Table Extract; konwersja ostrzega, że przyjęto układ gemu. |
| Deduplicate | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z distinct lub filtrem numeru wiersza | Zachowuje jeden wiersz na klucz: distinct, pierwszy lub ostatni według kolejności sortowania, dowolny albo tylko klucze występujące raz. |
| Dynamic Replace | Pełny | Transformacja dynamic replace, konfigurowana ręcznie | Konwertuje na reguły zamiany w transformacji dynamic replace; konwersja ostrzega, że przyjęto układ gemu. |
| Dynamic Select | Pełny | Wybór kolumn w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) rozstrzygany według typu | Rozstrzyga kolumny według typu w czasie konwersji do jawnego wyboru. |
| Filter | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem filtru | Konwertuje na krok Table Extract z wyrażeniem filtru; warunki NULL odrzucają wiersz. |
| Flatten Schema | Pełny | Kroki [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/) i [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Spłaszcza zagnieżdżone pola do kolumn nazwanych z użyciem separatora gemu i rozwija tablice do jednego wiersza na element. |
| Fuzzy Match | Pełny | Kroki [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) i [User Defined Transform](/pl/reference/workflow-steps/general/user-defined-transform/) | Łączy rekordy w pary, ocenia każde pole dopasowania metodą gemu, uśrednia oceny i zachowuje pary na poziomie progu lub powyżej niego. |
| Group By Rollup | Pełny | Suma zbiorów kroków agregacji [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) dla każdego poziomu rollup | Rozwija rollup do jednej agregacji na poziom grupowania, połączonych sumą zbiorów z podsumami NULL. |
| Limit | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z limitem wierszy | Konwertuje na limit wierszy; odwołania do konfiguracji stają się zmiennymi projektu. |
| Normalize | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem rozwijającym | Powtarza każdy rekord zgodnie z wyrażeniem długości, oblicza kolumny wyjściowe dla każdego indeksu i zatrzymuje się na pierwszym indeksie, przy którym spełniony jest warunek zakończenia. |
| Order By | Pełny | Sortowanie w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Konwertuje na sortowanie z tymi samymi kluczami, kierunkiem i położeniem wartości null. |
| Reformat | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniami kolumn | Konwertuje na krok Table Extract z jednym wyrażeniem na kolumnę wyjściową; kolumny niewymienione są odrzucane. |
| Sample Rows | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z limitem wierszy lub próbką losową | Zachowuje losowy ułamek lub liczbę wierszy; wybrane wiersze różnią się od uruchomienia Spark, ponieważ próbkowanie jest losowe. |
| Schema Transform | Pełny | Łańcuch kroków [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) stosowanych po kolei | Stosuje każdą operację po kolei: dodanie lub zastąpienie kolumny, usunięcie, zmiana nazwy, dodanie w razie braku z wartością domyślną oraz dodanie reguły biznesowej projektu. |
| Set Operation | Pełny | [Tabela: suma wszystkich](/pl/reference/workflow-steps/tables/table-union-all/); [Złączenie anty](/pl/reference/workflow-steps/tables/table-anti-join/) dla except; [Złączenie wewnętrzne](/pl/reference/workflow-steps/tables/table-inner-join/) dla intersect | Union all układa wejścia jedno na drugim; except all i intersect all zachowują właściwą liczbę zduplikowanych wierszy. |
| TransposeAgg | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z agregacją | Konwertuje grupowanie, agregacje i pivot gemu jako Aggregate, z ostrzeżeniem o konieczności przeglądu. |
| Unpivot | Pełny | Krok [Melt](/pl/reference/workflow-steps/tables/table-melt/) | Układa wybrane kolumny w kolumny nazwy i wartości. |
| Watermark | Pełny | Krok niepotrzebny | Pominięty: uruchomienie wsadowe odczytuje wszystkie obecne dane, więc nie ma progu odcięcia dla spóźnionych danych. |
| Window Function | Pełny | Wyrażenia okna w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Dodaje kolumny okna z partycją, kolejnością i ramką gemu, wierszami lub zakresem, z granicami nieograniczonymi, bieżącego wiersza lub z przesunięciem. |

### Złączenie/podział

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Compare Columns | Pełny | Pełne złączenie zewnętrzne plus agregaty dla każdej kolumny | Porównuje kolumny przez pełne złączenie zewnętrzne danych po unpivot, z liczbą zgodnych i niezgodnych. |
| Join | Pełny | [Złączenie wewnętrzne](/pl/reference/workflow-steps/tables/table-inner-join/), [Złączenie wielu tabel](/pl/reference/workflow-steps/tables/table-multi-table-join/), [Złączenie anty](/pl/reference/workflow-steps/tables/table-anti-join/) lub [Złączenie krzyżowe](/pl/reference/workflow-steps/tables/table-cross-join/) | Buduje złączenie każdego typu — inner, left, right, full, semi, anti, cross i natural — na dowolnym warunku złączenia, stosuje klauzulę where i zapisuje listę select. |
| Repartition | Pełny | Krok niepotrzebny | Pominięty: PlaidCloud zarządza partycjonowaniem, więc następny krok odczytuje tabelę nadrzędną bezpośrednio. |
| Row Distributor | Pełny | Jeden filtr [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) na wyjście | Konwertuje na jeden filtr na wyjście; wiersze mogą trafić do wielu wyjść. |

### Analiza składniowa

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Column Parser | Pełny | [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/) / [Analiza XML](/pl/reference/workflow-steps/tables/table-xml-parse/) | Konwertuje na analizę JSON lub XML nazwanej kolumny; konwersja ostrzega, że przyjęto układ gemu. |

### Niestandardowe

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Pełny | Krok [User Defined Transform](/pl/reference/workflow-steps/general/user-defined-transform/) uruchamiający wygenerowany kod gemu | Wygenerowany kod PySpark gemu z eksportu potoku działa w kroku Python, z ostrzeżeniem o konieczności przeglądu. |
| CustomReformatBitbucket | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Konwertuje się jako Reformat, którego wyrażenia niesie gem, z ostrzeżeniem o konieczności przeglądu. |
| Data Quality Check | Pełny | [Tabela: suma wszystkich](/pl/reference/workflow-steps/tables/table-union-all/) po jednym wierszu wyniku na sprawdzenie; [Zgłoś błąd przepływu pracy](/pl/reference/workflow-steps/workflow-control/raise-workflow-error/), aby zatrzymać przy niepowodzeniach | Ocenia każde sprawdzenie na danych wejściowych i zapisuje jeden wiersz wyniku na sprawdzenie wraz ze statusem i komunikatem. Dane przechodzą dalej, a uruchomienie zatrzymuje się po osiągnięciu progu niepowodzeń gemu. |
| Deequ | Pełny | Sprawdzenia w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Przekazuje dane dalej i buduje tabelę wyników ograniczeń dla reguł isComplete, isUnique, isNonNegative i isContainedIn. |
| Delta Table Operations | Pełny | Kroki [Table In-Place Delete](/pl/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/pl/reference/workflow-steps/tables/table-update/), [Table Drop](/pl/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/pl/reference/workflow-steps/tables/table-restore-timestamp/) | Usuwanie, aktualizacja, porzucenie i przywrócenie do znacznika czasu mapują się na kroki tabel; optimize, vacuum i restore według wersji przekazują dane dalej z ostrzeżeniem. |
| Directory | Pełny | [Lista katalogu](/pl/reference/workflow-steps/document/directory-listing/) | Wyświetla pliki powiązanego folderu dokumentów w kolumnach gemu; przy opcji nazwy arkusza każdy skoroszyt daje jeden wiersz na arkusz. Brakujący folder daje zero wierszy. |
| Email | Pełny | Krok [Notify Via Email](/pl/reference/workflow-steps/notifications/notify-via-email/) | Wysyła wiadomość e-mail, z opcjonalnym załącznikiem z danymi, przez powiązane połączenie e-mail. |
| Email Data | Pełny | Krok [Notify Via Email](/pl/reference/workflow-steps/notifications/notify-via-email/) | Wysyła wiersze wejściowe e-mailem jako tabelę i przekazuje dane wejściowe bez zmian. |
| File Operation | Pełny | Krok [Copy Document File](/pl/reference/workflow-steps/document/copy-document-file/) lub [Copy Document Directory](/pl/reference/workflow-steps/document/copy-document-directory/) | Kopiuje, przenosi lub synchronizuje pliki z powiązanego folderu dokumentów do folderu dokumentów skonwertowanego przepływu pracy; przeniesienie usuwa pliki źródłowe. |
| Log | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Zapisuje wiersz zdarzenia gemu (czas, nazwa gemu, typ zdarzenia i tekst) w jego tabeli wyjściowej. |
| REST API Enrich | Pełny | [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Wywołuje API raz na wiersz i dodaje kolumny odpowiedzi. |
| Script | Pełny | Krok Python z przepisaniem dostępu do ramki | Osadza treść skryptu w kroku python, z przepisanym dostępem do ramki danych; treści w Scala są przenoszone z adnotacją. |
| Soda Data Quality Check | Pełny | Sprawdzenia w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Buduje tabelę wyników sprawdzeń na podstawie sprawdzeń Soda. |
| SQL Statement | Pełny | Krok SQL na każdą kartę wyjściową, tekst przetłumaczony na dialekt tenanta | Osadza każdą kartę jako krok SQL z wejściami powiązanymi jako tabele tymczasowe; przetłumaczone na dialekt tenanta. |
| Todo | Pełny | [Zgłoś błąd przepływu pracy](/pl/reference/workflow-steps/workflow-control/raise-workflow-error/) lub krok [Notify via Log](/pl/reference/workflow-steps/notifications/notify-via-log/) | Oznacza logikę, która ma jeszcze zostać napisana: komunikat dziennika, gdy nic go nie odczytuje, albo krok zatrzymujący uruchomienie z komunikatem gemu, gdy zależy od niego późniejszy krok. |

### Raport

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Tableau | Pełny | Krok [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/) | Zapisuje wyodrębnienie Hyper i publikuje je w powiązanym połączeniu Tableau. |

### ML/AI

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Bedrock | Pełny | Krok [Text NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) | Osadza kolumnę tekstową przez połączenie AI obszaru roboczego. |
| OpenAI | Pełny | Krok [Text NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) | Odpowiada na pytania lub osadza tekst przez połączenie AI obszaru roboczego. |
| Pinecone Lookup | Pełny | [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odpytuje indeks Pinecone dla każdego wiersza i dodaje kolumny pinecone_matches i pinecone_error. |
| SageMaker Endpoint | Pełny | Krok [Text NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) | Odpowiada na pytania przez połączenie AI obszaru roboczego. |
| Text Processing | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) do dzielenia na fragmenty; [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) do pobierania ze stron internetowych | Dzielenie na fragmenty staje się wyrażeniem fragmentów znakowych; pobieranie ze stron internetowych pobiera adres URL każdego wiersza i dołącza zawartość strony z powrotem do wiersza. |

### Podgraf/sterowanie

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Control Flow Input | Pełny | Pominięty (tylko znacznik granicy) | Pominięty; oznacza jedynie granicę wejścia podprzepływu pracy iteratora. |
| Control Flow Output | Pełny | Pominięty (tylko znacznik granicy) | Pominięty; oznacza jedynie granicę wyjścia podprzepływu pracy iteratora. |
| Subgraph (Basic) | Pełny | Kontener kanwy / zagnieżdżony przepływ pracy z procesów wbudowanych | Konwertuje wbudowany graf wewnętrzny na zagnieżdżony przepływ pracy (lub wbudowane kroki) z parametrami tabel wejściowych/wyjściowych. |
| Table Iterator | Pełny | Krok [Workflow Loop](/pl/reference/workflow-steps/workflow-control/workflow-loop/) | Uruchamia treść pętli raz na wiersz wejściowy, ustawiając każdą wartość konfiguracji z jego kolumny, do maxIteration. |
| While Iterator | Pełny | Krok [Workflow Loop](/pl/reference/workflow-steps/workflow-control/workflow-loop/) | Uruchamia treść pętli raz na przebieg, przekazując numer iteracji, aż treść zwróci zero wierszy lub zostanie osiągnięte maksimum gemu. |

## Gemy SQL / Analyst

### Źródło/cel

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Pełny | Krok importu/eksportu danych zewnętrznych z odpowiednim połączeniem z bazą danych | Odczytuje lub zapisuje tabelę w zewnętrznej bazie danych przez połączenie PlaidCloud. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Pełny | Kroki importu/eksportu plików względem konta dokumentów (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Odczytuje lub zapisuje pliki w magazynie chmurowym/SFTP z opcjami sumy zbiorów z symbolami wieloznacznymi, wyzwalacza, usuwania/przenoszenia i szyfrowania. |
| Model | Pełny | Tabela wyjściowa kroku nadrzędnego | Odczytuje inny model jako tabelę wytworzoną przez wskazany krok nadrzędny. |
| Seed | Pełny | [Import: CSV](/pl/reference/workflow-steps/import/import-csv/) | Plik Seed CSV jest importowany do tabeli PlaidCloud. |
| Source | Pełny | Krok importu wybrany według formatu zbioru danych (zobacz [Konektory](#konektory)) | Każdy Source staje się krokiem importu do tabeli nazwanej od zbioru danych; format nierozpoznany przez konwerter jest odczytywany jako plik CSV przesłany do folderu dokumentów przepływu pracy, z ostrzeżeniem. |
| Target Model / Table (Target) | Pełny | Kroki [Table Extract](/pl/reference/workflow-steps/tables/table-extract/), [Upsert](/pl/reference/workflow-steps/tables/table-upsert/), [Kopiuj tabelę](/pl/reference/workflow-steps/tables/table-copy/) i [Tabela: suma wszystkich](/pl/reference/workflow-steps/tables/table-union-all/) | Zapisuje końcowy select modelu do tabeli PlaidCloud jako replace, append, upsert, delete-and-insert, SCD2 lub replace by predicate. |
| Upload Files | Pełny | [Import: CSV](/pl/reference/workflow-steps/import/import-csv/) | Przesłane pliki lokalne stają się tabelą przez krok importu. |

### Przygotowanie

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Data Cleansing | Pełny | Wyrażenia kolumn w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Konwertuje opcje wypełniania wartości null, przycinania i wielkości liter na wyrażenia kolumn; oczyszczone kolumny przechodzą na koniec. |
| Data Masking | Pełny | Wyrażenia kolumn do maskowania znaków lub haszowania | Maskuje lub haszuje wybrane kolumny tekstowe w miejscu albo jako nowe kolumny. |
| Find Duplicates | Pełny | Wyrażenie okna z numerem wiersza plus filtr | Zwraca wiersze unikatowe, zduplikowane lub wybrane według liczby/pozycji dla każdego klucza. |
| Generate Rows | Pełny | Tabela sekwencji złączona i filtrowana dla każdego wiersza wejściowego | Generuje wiersze dla każdego wiersza wejściowego na podstawie wyrażeń init, condition i loop. |
| Imputation | Pełny | Agregacja plus złączenie zwrotne i wyrażenie kolumny | Zastępuje wartości null lub wartości wskaźnikowe średnią, medianą, dominantą lub stałą wartością. |
| Multi-Column Edit | Pełny | Wyrażenia dla każdej kolumny rozwinięte z szablonu | Stosuje jeden szablon wyrażenia do każdej wybranej kolumny. |
| Multi-Column Rename | Pełny | Mapowanie zmiany nazw kolumn w kroku select | Zmienia nazwy wybranych kolumn według prefiksu, sufiksu lub wyrażenia nazwy. |
| Record ID | Pełny | Wyrażenie kolumny z numerem wiersza lub uuid | Dodaje kolumnę identyfikatora rekordu typu UUID lub sekwencyjną. |
| Sample | Pełny | Limit wierszy lub opcja próbki w kroku extract | Pobiera pierwsze/ostatnie/losowe/co N-te/procentowe wiersze ogółem lub dla każdej grupy. |
| Tile | Pełny | Wyrażenia okna dla numeru kafla i sekwencji | Przypisuje numery kafli według równej sumy, liczby, pasm odchylenia standardowego, wartości różnych lub ręcznych odcięć. |

### Transformacja

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Aggregate | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z agregacją; krok [Pivot](/pl/reference/workflow-steps/tables/table-pivot/), gdy gem wykonuje pivot | Grupuje i agreguje, stosuje warunek HAVING oraz obraca do jednej kolumny na wartość pivot; propagate-all przenosi wszystkie pozostałe kolumny wejściowe. |
| Count Records | Pełny | Krok agregacji z funkcjami zliczania | Zwraca łączną liczbę, liczbę niepustych lub różnych jako jeden wiersz. |
| Data Encoder/Decoder | Pełny | Wyrażenia kolumn do kodowania i dekodowania base64/hex | Koduje lub dekoduje wybrane kolumny; AES tylko w Databricks. |
| Deduplicate | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z distinct lub filtrem numeru wiersza | Zachowuje jeden wiersz na klucz: distinct, pierwszy lub ostatni według kolejności sortowania, dowolny albo tylko klucze występujące raz. |
| Dynamic Select | Pełny | Wybór kolumn w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) rozstrzygany według typu | Rozstrzyga kolumny według typu w czasie konwersji do jawnego wyboru. |
| Filter | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem filtru | Konwertuje na krok Table Extract z wyrażeniem filtru; warunki NULL odrzucają wiersz. |
| Finance | Pełny | Wyrażenie kolumny implementujące funkcję finansową | Dołącza wynik funkcji finansowej (FV, PV, NPV, IRR, ...) jako nową kolumnę. |
| Flatten Schema | Pełny | Kroki [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/) i [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Spłaszcza zagnieżdżone pola do kolumn nazwanych z użyciem separatora gemu i rozwija tablice do jednego wiersza na element. |
| Fuzzy Match | Pełny | Kroki [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) i [User Defined Transform](/pl/reference/workflow-steps/general/user-defined-transform/) | Łączy rekordy w pary, ocenia każde pole dopasowania metodą gemu, uśrednia oceny i zachowuje pary na poziomie progu lub powyżej niego. |
| Limit | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z limitem wierszy | Konwertuje na limit wierszy; odwołania do konfiguracji stają się zmiennymi projektu. |
| Order By | Pełny | Sortowanie w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Konwertuje na sortowanie z tymi samymi kluczami, kierunkiem i położeniem wartości null. |
| Pivot | Pełny | Krok [Pivot](/pl/reference/workflow-steps/tables/table-pivot/) | Zamienia wybrane wartości pivot na kolumny agregatów; lista wartości trybu Simple pobrana podczas projektowania jest konwertowana jako wymienione wartości. |
| Reformat | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniami kolumn | Konwertuje na krok Table Extract z jednym wyrażeniem na kolumnę wyjściową; kolumny niewymienione są odrzucane. |
| Running Total | Pełny | Kolumna z wyrażeniem okna sumy skumulowanej | Dołącza sumy skumulowane dla każdej wybranej kolumny. |
| Snowflake Unpivot (third-party) | Pełny | Krok [Melt](/pl/reference/workflow-steps/tables/table-melt/) | Wykonuje unpivot kolumn przez Snowflake UNPIVOT. |
| Transpose | Pełny | Krok [Melt](/pl/reference/workflow-steps/tables/table-melt/) | Układa kolumny danych w kolumny nazwy i wartości tekstowej. |
| TransposeAgg | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z agregacją | Konwertuje grupowanie, agregacje i pivot gemu jako Aggregate, z ostrzeżeniem o konieczności przeglądu. |
| Unpivot | Pełny | Krok [Melt](/pl/reference/workflow-steps/tables/table-melt/) | Układa kolumny danych w kolumny nazwy i wartości. |
| Weighted Average | Pełny | Krok agregacji z wyrażeniem średniej ważonej | Oblicza średnią ważoną ogółem lub dla każdej grupy. |
| Window Function | Pełny | Wyrażenia okna w kroku [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Dodaje kolumny okna z partycją, kolejnością i ramką gemu, wierszami lub zakresem, z granicami nieograniczonymi, bieżącego wiersza lub z przesunięciem. |

### Złączenie/podział

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Except | Pełny | [Złączenie anty](/pl/reference/workflow-steps/tables/table-anti-join/) po wszystkich kolumnach plus krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z distinct | Zachowuje wiersze pierwszego wejścia, które nie występują w żadnym z pozostałych wejść. |
| Intersect | Pełny | [Złączenie wewnętrzne](/pl/reference/workflow-steps/tables/table-inner-join/) po wszystkich kolumnach plus Distinct | Zachowuje wiersze obecne w każdym wejściu. |
| Join | Pełny | [Złączenie wewnętrzne](/pl/reference/workflow-steps/tables/table-inner-join/), [Złączenie wielu tabel](/pl/reference/workflow-steps/tables/table-multi-table-join/), [Złączenie anty](/pl/reference/workflow-steps/tables/table-anti-join/) lub [Złączenie krzyżowe](/pl/reference/workflow-steps/tables/table-cross-join/) | Buduje złączenie każdego typu — inner, left, right, full, semi, anti, cross i natural — na dowolnym warunku złączenia, stosuje klauzulę where i zapisuje listę select. |
| Union | Pełny | [Tabela: suma wszystkich](/pl/reference/workflow-steps/tables/table-union-all/) | Układa wejścia według pozycji, usuwając duplikaty, gdy gem ich nie zachowuje. |
| Union By Name | Pełny | [Tabela: suma wszystkich](/pl/reference/workflow-steps/tables/table-union-all/) | Staje się krokiem Union All, który wyrównuje kolumny według nazwy i uzupełnia brakujące wartościami null. |

### Analiza składniowa

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| JSON Parse | Pełny | [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/) | Przetwarza kolumnę tekstową JSON na pola ustrukturyzowane. |
| Regex | Pełny | Wyrażenia regex w kroku Table Extract / Transform | Zastępuje, analizuje, dopasowuje lub dzieli na tokeny kolumnę tekstową za pomocą wyrażenia regularnego. |
| Text To Columns | Pełny | Kroki podziału kolumny / rozwinięcia z separatorem w postaci wyrażenia regularnego | Dzieli kolumnę rozdzielaną na kolumny lub wiersze przy użyciu separatora w postaci wyrażenia regularnego. |
| XML Parse | Pełny | [Analiza XML](/pl/reference/workflow-steps/tables/table-xml-parse/) | Przetwarza kolumnę tekstową XML na pola ustrukturyzowane. |

### Niestandardowe

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Directory | Pełny | [Lista katalogu](/pl/reference/workflow-steps/document/directory-listing/) | Wyświetla pliki powiązanego folderu dokumentów w kolumnach gemu; przy opcji nazwy arkusza każdy skoroszyt daje jeden wiersz na arkusz. Brakujący folder daje zero wierszy. |
| DynamicInput | Pełny | Krok SQL dla szablonów zapytań; pętla przepływu pracy dla trybu wielu plików | Tryb szablonu zapytania osadza szablon jako krok SQL; tryb wielu plików mapuje się z założeniami. |
| Email | Pełny | Krok [Notify Via Email](/pl/reference/workflow-steps/notifications/notify-via-email/) | Wysyła wiadomość e-mail, z opcjonalnym załącznikiem z danymi, przez powiązane połączenie e-mail. |
| RestAPI | Pełny | [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Wysyła jedno żądanie na wiersz wejściowy z Twoim adresem URL, nagłówkami, zapytaniem, treścią i ponowieniami, zachowuje odpowiedź i odpytuje żądanie asynchroniczne do jego zakończenia. Poświadczenia pochodzą z powiązanego połączenia. |
| Script | Pełny | Krok Python z przepisaniem dostępu do ramki | Osadza treść skryptu w kroku python, z przepisanym dostępem do ramki danych; treści w Scala są przenoszone z adnotacją. |
| SQL Statement | Pełny | Krok SQL na każdą kartę wyjściową, tekst przetłumaczony na dialekt tenanta | Osadza każdą kartę jako krok SQL z wejściami powiązanymi jako tabele tymczasowe; przetłumaczone na dialekt tenanta. |
| StoredProcedure | Pełny | Krok [Agent Remote Execution of SQL](/pl/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Wywołuje procedurę w jej magazynie przez wybrane połączenie: raz na wiersz wejściowy z każdym argumentem powiązanym z jego kolumny albo raz, gdy nie przyjmuje argumentów. Kolumny wejściowe przechodzą dalej. |
| Table Operations | Pełny | Kroki [Table In-Place Delete](/pl/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/pl/reference/workflow-steps/tables/table-update/), [Table Drop](/pl/reference/workflow-steps/tables/table-drop/) | Aktualizacja, usuwanie i porzucenie mapują się na kroki tabel; vacuum i optimize stają się optymalizacją tabeli lub brakiem operacji z ostrzeżeniem. |
| ToDo | Pełny | [Zgłoś błąd przepływu pracy](/pl/reference/workflow-steps/workflow-control/raise-workflow-error/) lub krok [Notify via Log](/pl/reference/workflow-steps/notifications/notify-via-log/) | Oznacza logikę, która ma jeszcze zostać napisana: komunikat dziennika, gdy nic go nie odczytuje, albo krok zatrzymujący uruchomienie z komunikatem gemu, gdy zależy od niego późniejszy krok. |

### Przestrzenne

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Buffer | Pełny | Krok [Spatial Buffer](/pl/reference/workflow-steps/spatial/spatial-buffer/) | Powiększa każdą geometrię o skonfigurowaną odległość w milach lub kilometrach. |
| CreatePoint | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) z `geom_point` | Buduje geometrię punktu z kolumn długości i szerokości geograficznej. |
| Distance | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Oblicza odległość, kierunek świata i azymut między dwoma punktami WKT. |
| FindNearest | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) ze złączeniem krzyżowym | Znajduje N najbliższych punktów docelowych dla każdego punktu źródłowego w maksymalnej odległości. |
| HeatMap | Pełny | [Heat Map (macro)](/pl/reference/workflow-steps/macros/macro-heat-map/) | Grupuje punkty w sześciokąty H3 w rozdzielczości gemu, rozprowadza ciepło na odległość siatki z jego zanikiem i podaje gęstość oraz obrys każdego sześciokąta. |
| PolyBuild | Pełny | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) i krok Python | Buduje WKT wielokąta lub linii łamanej z uporządkowanych punktów dla każdej grupy. |
| Simplify | Pełny | Krok [Spatial Generalize](/pl/reference/workflow-steps/spatial/spatial-generalize/) | Upraszcza geometrie WKT z tolerancją w milach/km. |
| SpatialMatch | Pełny | [Dopasowanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-match/) | Dopasowuje geometrie źródłowe i docelowe według intersects/contains/within/touches/envelope. |

### Raport

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| PowerBIWrite | Pełny | [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Tworzy zbiór danych Power BI i przesyła wiersze przez interfejs REST API Power BI. |
| TableauWrite | Pełny | Krok [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/) | Zapisuje wyodrębnienie Hyper i publikuje je w powiązanym połączeniu Tableau. |
| Visualize | Pełny | [Kopiuj tabelę](/pl/reference/workflow-steps/tables/table-copy/) | Przekazuje wiersze dalej bez zmian; wykres zbuduj jako pulpit PlaidCloud na tej samej tabeli. |

### Podgraf/sterowanie

| Gem | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Condition | Pełny | [Złączenie krzyżowe](/pl/reference/workflow-steps/tables/table-cross-join/) i krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) | Ocenia warunki na całym wejściu i kieruje każdy wiersz do pierwszego wyjścia, którego warunek jest spełniony, a w przeciwnym razie do ostatniego wyjścia. |
| Macro | Pełny | Krok SQL z rozwiniętą treścią makra | Osadza treść makra jako krok SQL przetłumaczony na dialekt tenanta, z wejściami powiązanymi jako tabele tymczasowe. |
| Pipeline (trigger) | Pełny | Krok [Workflow Loop](/pl/reference/workflow-steps/workflow-control/workflow-loop/) | Uruchamia nazwany potok raz na wiersz wejściowy z Twoimi parametrami i warunkiem wyzwalacza, kontynuuje po nieudanym uruchomieniu i zwraca jeden wiersz na uruchomienie. |
| Subgraph (Basic) | Pełny | Kontener kanwy / zagnieżdżony przepływ pracy z procesów wbudowanych | Konwertuje wbudowany graf wewnętrzny na zagnieżdżony przepływ pracy (lub wbudowane kroki) z parametrami tabel wejściowych/wyjściowych. |

## Konektory

Formaty zbiorów danych i konektory są ustawieniami źródła i celu gemu, a nie gemami. Każdy format konwertuje się na pokazany krok importu lub eksportu, a konwersja nigdy nie łączy się z systemem źródłowym ani docelowym.

| Format | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Avro | Pełny | Import: [Avro](/pl/reference/workflow-steps/import/import-avro/); Eksport: [Avro](/pl/reference/workflow-steps/export/export-to-avro/) | Odczytuje i zapisuje pliki Avro. |
| BigQuery | Pełny | Zewnętrzne połączenie z bazą danych z importem tabeli | Odczytuje i zapisuje przez połączenie. |
| Binary files | Pełny | [Lista katalogu](/pl/reference/workflow-steps/document/directory-listing/) z zawartością plików; [Wykonawca Alteryx](/pl/reference/workflow-steps/general/alteryx-executor/) do zapisu | Odczytuje każdy plik folderu wraz ze ścieżką, czasem modyfikacji, długością i zawartością; zapisuje zawartość każdego wiersza do pliku wskazanego przez jego ścieżkę. |
| Catalog table | Pełny | Powiązanie z istniejącą tabelą PlaidCloud | Wiąże się z tabelą według nazwy; odczyty i każdy tryb zapisu podlegają konwersji. |
| Cosmos DB | Pełny | Import i eksport: [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odczytuje i zapisuje dokumenty kontenera przez połączenie Cosmos DB. |
| CSV | Pełny | [Import: CSV](/pl/reference/workflow-steps/import/import-csv/); Eksport: CSV | Odczytuje i zapisuje pliki rozdzielane z opcjami nagłówka, separatora, cudzysłowu, znaku ucieczki i kodowania. |
| Data Generator | Pełny | Krok [Table Faker](/pl/reference/workflow-steps/tables/table-faker/) | Generuje kolumny zbioru danych z tymi samymi rodzajami danych fikcyjnych. |
| DataHub table | Pełny | [Importuj SQL](/pl/reference/workflow-steps/import/import-sql/) | Odczytuje tabelę wskazaną przez zbiór danych przez Twoje połączenie; zapis trafia do tabeli PlaidCloud. |
| Delta | Pełny | Powiązanie z istniejącą tabelą PlaidCloud | Odczytuje i zapisuje tabelę w każdym trybie zapisu; odczyt wcześniejszej wersji odbywa się przez powiązane połączenie Databricks. |
| Excel (XLSX) | Pełny | Import: Excel; Eksport: Excel | Odczytuje i zapisuje arkusze i zakresy skoroszytów. |
| Fixed format | Pełny | Import: [stała szerokość](/pl/reference/workflow-steps/import/import-fixed-width/); Eksport: [CSV](/pl/reference/workflow-steps/export/export-to-csv/) | Odczytuje pliki o stałej szerokości ułożone według szerokości kolumn zbioru danych; zapisuje plik rozdzielany. |
| Hive | Pełny | Import: [Importuj SQL](/pl/reference/workflow-steps/import/import-sql/); Eksport: [tabele zewnętrzne](/pl/reference/workflow-steps/export/export-external-tables/) | Odczytuje i zapisuje tabelę przez Twoje połączenie Hive. |
| Iceberg | Pełny | Powiązanie z istniejącą tabelą PlaidCloud | Odczytuje i zapisuje tabelę. |
| JDBC | Pełny | Zewnętrzne połączenie z bazą danych z importem tabeli | Odczytuje tabelę lub zapytanie i zapisuje w trybie replace lub append przez Twoje połączenie; instrukcja po zapisie jest uruchamiana po zapisie. |
| JSON | Pełny | [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/) | Ładuje rekordy i spłaszcza zagnieżdżone pola. |
| Kafka | Pełny | Import: [Importuj Kafka](/pl/reference/workflow-steps/import/import-kafka/); Eksport: [Eksportuj Kafka](/pl/reference/workflow-steps/export/export-kafka/) | Odczytuje temat jako jedną partię komunikatów i zapisuje wiersze jako komunikaty. |
| MongoDB | Pełny | Import: [MongoDB](/pl/reference/workflow-steps/import/import-mongodb/); Eksport: [MongoDB](/pl/reference/workflow-steps/export/export-mongodb/) | Odczytuje i zapisuje kolekcję przez Twoje połączenie MongoDB. |
| ORC | Pełny | Import: [ORC](/pl/reference/workflow-steps/import/import-orc/); Eksport: ORC | Odczytuje i zapisuje pliki ORC. |
| Parquet | Pełny | Import: Parquet; Eksport: Parquet | Odczytuje i zapisuje pliki Parquet. |
| Pinecone | Pełny | Import i eksport: [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odczytuje rekordy indeksu i wykonuje upsert wierszy jako wektorów przez interfejs REST API Pinecone. |
| Redshift | Pełny | Zewnętrzne połączenie z bazą danych z importem tabeli | Odczytuje i zapisuje przez połączenie. |
| Salesforce | Pełny | Import: [Query Salesforce Object](/pl/reference/workflow-steps/salesforce/query-salesforce-object/); Eksport: [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odczytuje obiekt lub zapytanie SOQL i zapisuje rekordy przez Twoje połączenie Salesforce. |
| Seed (inline) | Pełny | [Import: CSV](/pl/reference/workflow-steps/import/import-csv/) | Ładuje wiersze wbudowane jako tabelę. |
| Slack | Pełny | Import: [Singer](/pl/reference/workflow-steps/import/import-singer/); Eksport: [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odczytuje komunikaty kanału i publikuje każdy wiersz jako komunikat przez Twoje połączenie Slack. |
| Smartsheet | Pełny | Import i eksport: [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odczytuje i zapisuje wiersze arkusza przez Twoje połączenie Smartsheet. |
| Snowflake | Pełny | Zewnętrzne połączenie z bazą danych z importem tabeli | Odczytuje i zapisuje przez połączenie. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Pełny | Kroki importu i eksportu plików względem konta dokumentów | Odczytuje i zapisuje typ pliku; opcje bez odpowiednika w PlaidCloud są oznaczane. |
| Text | Pełny | [Import: CSV](/pl/reference/workflow-steps/import/import-csv/) jako pojedyncza kolumna | Odczytuje każdy wiersz jako jedną kolumnę. |
| Web page | Pełny | [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) | Odczytuje stronę pod adresem URL zbioru danych do tabeli. |
| XML | Pełny | [Analiza XML](/pl/reference/workflow-steps/tables/table-xml-parse/) | Ładuje rekordy według znacznika wiersza. |

## Wyrażenia i struktura projektu

| Obszar | Status | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Expressions | Pełny | Wyrażenia SQL Spark i magazynu danych tłumaczone funkcja po funkcji | Funkcje i operatory konwertują się na wyrażenia PlaidCloud; funkcja bez odpowiednika jest oznaczana nazwą. |
| Project and graph structure | Pełny | Program ładujący projekt | Każdy kształt eksportu Prophecy jest ładowany i normalizowany do jednego modelu. |

## Znane przypadki brzegowe

| Przypadek | Co się dzieje |
| --- | --- |
| Kod lub dane, których eksport nie zawiera | Gem Builder lub inny gem niestandardowy, którego kodu nie ma w eksporcie, oraz wywołanie makra pakietu dbt pominiętego w eksporcie stają się krokiem wskazującym, czego brakuje; wyeksportuj projekt wraz z kodem potoku i pakietami dbt albo odbuduj logikę w kroku Python lub SQL. Gemy Ab Initio Error Detection i MTime przekazują dane wejściowe dalej, ponieważ stosowanej przez nie reguły nie ma w eksporcie. Sprawdzenia Soda odczytywane z pliku spoza projektu oraz sprawdzenia Soda porównujące z wcześniejszymi skanami lub z innym zbiorem danych albo testujące format wskazany przez Soda nie mają wiersza w tabeli wyników; oblicz je w późniejszym kroku. |
| Wyniki znane dopiero po uruchomieniu potoku | Gem REST API, który spłaszcza swoją odpowiedź, umieszcza całą odpowiedź w jednej kolumnie, gdy nic nie deklaruje nazw pól, co ujawnia dopiero uruchomienie; wyodrębnij potrzebne pola w późniejszym kroku. Makro dbt, które odpytuje magazyn danych podczas kompilacji dbt, staje się krokiem wskazującym je; zastąp zapytanie zwracanymi przez nie wartościami. Gem Spark StoredProcedure działa, ale jego wartości OUT nie są zwracane; wyjściem są kolumny przekazywane dalej. `input_file_name()` zwraca pusty ciąg dla źródła tabeli lub Delta, które nie ma pliku do nazwania, a `hash()` / `xxhash64()` wewnątrz agregacji, okna lub gemu z wieloma wejściami są obliczane przez magazyn danych, więc mogą się różnić od Spark. |
| Wartości zapisywane w kroku podczas konwersji projektu | Wartość parametru zawierająca cudzysłów, ukośnik odwrotny lub nawias klamrowy, wartość potoku odczytywana przez krok SQL oraz baza danych wskazana przez operację tabeli Delta w konfiguracji są zapisywane w kroku jako wartości stałe, więc zmiana zmiennej przepływu pracy ich nie zmienia; edytuj krok, gdy zmienia się konfiguracja. |
| Kod Scala | Skrypt Scala, wyrażenie Scala albo funkcja zdefiniowana przez użytkownika lub funkcja agregująca w Scala staje się krokiem, który je wskazuje; przepisz go w SQL lub Python. |
| Logowanie Kerberos w Kafka | Źródło lub cel Kafka logujący się przez Kerberos (GSSAPI) konwertuje się bez nazwy usługi Kerberos i mechanizmu logowania; ustaw je w połączeniu PlaidCloud. |
| Strumieniowanie | Źródła, cele i potoki strumieniowe działają jako wsadowe przepływy pracy na danych obecnych w chwili uruchomienia; ustaw harmonogram przepływu pracy tak często, jak potrzebujesz. |
| Komponenty zadania | Zadanie Spark konwertuje się wraz ze swoim jednym potokiem i harmonogramem; jego pozostałe komponenty, warunki uruchomienia i nadpisania konfiguracji nie są konwertowane. |
| Rzadkie wywołania | Funkcja agregująca zdefiniowana przez użytkownika wywoływana z rollup lub okna oraz makro dbt używające Jinja poza if, for, set i typowymi filtrami stają się krokiem wskazującym gem; wywołaj funkcję z gemu Aggregate albo wbuduj makro. |

## Weryfikacja skonwertowanego przepływu pracy

Porównaj wynik skonwertowanego przepływu pracy z wynikiem własnego potoku Prophecy: schemat, liczbę wierszy i wartości wierszy. Pomiń kolejność wierszy, chyba że przepływ pracy od niej zależy.
