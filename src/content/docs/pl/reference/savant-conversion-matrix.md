---
title: Macierz konwersji Savant
description: Jak PlaidCloud konwertuje analizy Savant Labs na natywne zaawansowane przepływy pracy, z poziomem mapowania każdego agenta i kilkoma wymienionymi przypadkami szczególnymi.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud konwertuje analizy Savant Labs na natywne zaawansowane przepływy pracy. Importer mapuje każdego agenta Savant na krok przepływu pracy, zmienną projektu lub obiekt kanwy, dzięki czemu przekonwertowany przepływ pracy działa natywnie w chmurze.

Aby przeprowadzić konwersję, zobacz [Migracja analiz Savant](/pl/guides/workflows/migrate-savant-analyses/).

Każdy agent ma poziom mapowania. **Pełny** oznacza, że każda opcja agenta ma prawidłowe mapowanie na krok PlaidCloud. Konstrukcje odrzucane z nazwy są wymienione w sekcji Nazwane odrzucenia.

Konektory systemów zewnętrznych są **połączone, a nie konwertowane**. Zobacz [Łączenie z systemami zewnętrznymi](#łączenie-z-systemami-zewnętrznymi).

## Obsługa agentów

Wszystkich 33 agentów jest konwertowanych na poziomie Pełny.

| Agent | Poziom | Odpowiednik w PlaidCloud | Konwertuje |
| --- | --- | --- | --- |
| Adapter Agent (`adapter`) | Pełny | Krok wyboru i projekcji schematu | Zmienia nazwy, typy i kolejność pól. |
| API / Infer Agent (usługa starszego typu) (`service`) | Pełny | Tak samo jak API Agent lub Infer Agent, według serviceType | LLMService jest konwertowany jak Infer Agent, a APIService jak API Agent; brakujący lub błędnie zapisany serviceType jest odczytywany z kluczy węzła z ostrzeżeniem. |
| API Agent (`apiService`) | Pełny | Table Extract, [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) i złączenie lewostronne z powrotem | Jedno żądanie GET, POST, PUT, PATCH lub DELETE na wiersz wejściowy; surowa treść odpowiedzi trafia do kolumny tekstowej, błędy HTTP pozostają jako wiersze, każdy wiersz wejściowy jest zachowany, a limit na okres zamienia się na ułamkową liczbę żądań na sekundę. Względny adres URL jest łączony z bazowym adresem URL z api_bindings lub z hostem połączenia REST; host, port lub ścieżka z pola wiersza są podstawiane dla każdego wiersza; stronicowanie przez następny adres URL, nagłówek Link, przesunięcie i numer strony jest obsługiwane, łącznie z początkiem, rozmiarem strony lub nazwą parametru szablonowanymi z pola wiersza. |
| Blend Agent (`blend`) | Pełny | [Złączenie wewnętrzne](/pl/reference/workflow-steps/tables/table-inner-join/), [Złączenie zewnętrzne](/pl/reference/workflow-steps/tables/table-outer-join/), [Złączenie anty](/pl/reference/workflow-steps/tables/table-anti-join/) | Złączenia wewnętrzne, lewostronne, prawostronne, pełne, anty oraz zewnętrzne z wyłączeniem wewnętrznego, warunki połączone przez OR, warunki „zawiera” i „jest częścią”, ze strumieniami dopasowanymi i niedopasowanymi; kolumny, które obrót lub analiza nazywają dopiero w czasie uruchomienia, są przenoszone dalej. |
| Dedupe Agent (`deduplicate`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z unikatowymi wierszami | Zachowuje pierwszy rekord dla klucza, w obrębie grup Grupuj według, a duplikaty kieruje do drugiego strumienia lub oznacza flagą. |
| Destination Agent (`destination`) | Pełny | [Eksport: CSV](/pl/reference/workflow-steps/export/export-to-csv/), [Eksport: Excel](/pl/reference/workflow-steps/export/export-to-excel/), Eksport: Parquet, JSON, Avro lub XML, [Export to PDF](/pl/reference/workflow-steps/export/export-to-pdf/), [Eksport: Tableau Hyper](/pl/reference/workflow-steps/export/export-hyper/) z [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/pl/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/pl/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/pl/reference/workflow-steps/notifications/notify-via-slack/) lub e-mail | Zapisuje przez destination_bindings na koncie dokumentów (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF lub plik Tableau .hyper, w dowolnym zestawie znaków Java, łącznie z aliasami oraz formami CESU-8 i ze znacznikiem kolejności bajtów; znak, którego zestaw znaków nie zawiera, jest zapisywany jako ?), w tabeli połączenia, w arkuszu Google, w źródle danych Tableau, na kanale Slack lub do odbiorców e-mail. Cel bez powiązania zapisuje tabelę projektu lub plik Dokumentu (zobacz „Dokąd trafiają dane” poniżej). Plik, podfolder lub karta na każdą wartość pola dzieli pliki CSV, Excel, Parquet i PDF oraz karty Arkuszy Google; szablon zasila każdy skoroszyt podziału. Opcje Excel są mapowane: puste wartości trafiają do `Sheet1`, kolidujące nazwy arkuszy dostają sufiks, `formatFromTemplate`, `topLeftCell` i tryb `create`. Append, upsert, update i groupReplace scalają według kluczy dopasowania (plik lub tabela jest odczytywany z powrotem i zapisywany ponownie; podział odczytuje plik, do którego zapisywana jest każda wartość uruchomienia, i scala w jego obrębie, pozostawiając pozostałe pliki bez zmian; Tableau aktualizuje swoje wiersze w miejscu). Kolumny nazwane tylko w danych (nagłówek po awansie, wartości obrotu, klucze przeanalizowanego JSON lub XML) są zapisywane obok znanych przez każdy eksport i zapis tabeli, sortowane i dzielone według nich oraz dołączane lub scalane do tabeli albo do pliku odczytanego z powrotem ze wszystkimi jego kolumnami. |
| Explode Agent (`explode`) | Pełny | [Złączenie krzyżowe](/pl/reference/workflow-steps/tables/table-cross-join/) | Łączy krzyżowo małą stronę z głównym strumieniem. |
| Filter Agent (`filter`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem filtru | Dzieli rekordy według kreatora lub wyrażenia na ścieżki prawdy i fałszu. |
| Filter Pushdown (`pdfilter`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniem filtru | Filtr po stronie bazy danych, konwertowany tak samo jak Filter. |
| Format Agent (`format`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) ze zmianą nazw kolumn lub Promote Header | Ukrywa, zmienia typ, zmienia nazwę i wypełnia pola dopasowane według nazwy (zawiera, zaczyna się od, kończy się na) lub według tego, że są puste; wypełnienie zapisuje wartość domyślną w każdej kolumnie, której typ pozwala na rzutowanie tej wartości (tekst, liczba, data). Awans wiersza nagłówka i dopasowanie pustych pól działają w czasie uruchomienia w kroku Promote Header, a awansowany nagłówek odczytuje każdą kolumnę swojego pliku. |
| Fuse Agent (`fuzzy_match`) | Pełny | [Fuzzy Match](/pl/reference/workflow-steps/tables/table-fuzzy-match/), między Union All a dwoma złączeniami | Łączy oba wejścia, dopasowuje rekordy po polach klucza z progiem podobieństwa 80 i łączy obie strony z powrotem z wynikiem pewności (Confidence Score). |
| Group (`group`) | Pełny | Kontener kanwy | Zachowany jako organizacja przepływu pracy. |
| Infer Agent (`gen_ai`) | Pełny | Zadanie z promptem [AI/NLP](/pl/reference/workflow-steps/text-documents/nlp-ai/) | Prompt jest uruchamiany dla każdego wiersza na polach wejściowych, na widocznym połączeniu LLM odpowiadającym dostawcy i modelowi z Savant; odpowiedź trafia do kolumny AI Answer obok każdej kolumny wejściowej. rowLimit ogranicza liczbę wierszy, na które udzielana jest odpowiedź w jednym uruchomieniu, i zachowuje wcześniejsze odpowiedzi: wiersz, na który już odpowiedziano (ten sam prompt, model i wartości wejściowe), zachowuje swoją odpowiedź, a do limitu liczą się tylko wiersze bez odpowiedzi. |
| JSON Agent (`json`) | Pełny | [Parsowanie JSON](/pl/reference/workflow-steps/tables/table-json-parse/) | Spłaszcza pole JSON do kolumn z kluczami oddzielonymi kropkami lub rozwija tablicę do jednego wiersza na element; klucze są odczytywane z danych w czasie uruchomienia. |
| Notes Agent (`notes`) | Pełny | Adnotacja kanwy | Zachowany jako kontekst przepływu pracy. |
| Pivot Agent (`pivot`) | Pełny | [Pivot](/pl/reference/workflow-steps/tables/table-pivot/) | Obraca wiersze w kolumny z agregacją. |
| Recursion Agent (`hierarchy`) | Pełny | Hierarchy Closure, [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) i [Złączenie wielu tabel](/pl/reference/workflow-steps/tables/table-multi-table-join/) | Przechodzi drzewo rodzic/dziecko na dowolną głębokość, agregując każdy węzeł po identyfikatorach na jego ścieżce do korzenia, wraz z nim samym, i zapisując Depth oraz Path; pętla zatrzymuje się na powtórzonym węźle. |
| Sample Agent (`sample`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z limitem wierszy | Zachowuje pierwsze N wierszy, opcjonalnie dla grupy, losowy procent lub N wierszy albo jeden wiersz z każdych N. |
| Search and Replace (`search_replace`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z zagnieżdżonymi wyrażeniami zamiany, podzielony na etapy | Reguły znajdź/zamień (zawiera lub pasuje; zamień lub dołącz), z uwzględnieniem wielkości liter lub bez, całe słowo lub nie, stosowane po kolei do wybranych pól tekstowych albo do każdego pola tekstowego, gdy żadne nie zostało wskazane. |
| Source Agent (`source`) | Pełny | Kroki importu powiązane przez `source_bindings` ([Import: CSV](/pl/reference/workflow-steps/import/import-csv/), [Import: Excel](/pl/reference/workflow-steps/import/import-excel/), [Import: SQL](/pl/reference/workflow-steps/import/import-sql/)) lub istniejąca tabela | Odczytuje powiązaną tabelę lub dokument; źródło bez powiązania tworzy pusty import i ostrzeżenie. Tekst XML odczytuje swój dokument przez Importuj XML (niepowiązany odczytuje savant/<workflow>/<name>.xml). Źródło powiązane z dokumentem XML zapisuje również pozostałe kolumny eksportu: kolumnę nazwy pliku lub ścieżki z dokumentu, resztę pustą. Źródło poniżej Format, który awansuje wiersz nagłówka, odczytuje według pozycji każdą kolumnę swojego pliku CSV, Excel (łącznie z Excel 97 .xls), JSON, Parquet lub Avro. |
| Spatial Match Agent (`spatial_match`) | Pełny | [Spatial Match (executor)](/pl/reference/workflow-steps/spatial/spatial-match-executor/), [Złączenie krzyżowe](/pl/reference/workflow-steps/tables/table-cross-join/) lub [Znajdź najbliższe](/pl/reference/workflow-steps/spatial/spatial-find-nearest/) | Dopasowania intersects, within, contains, touches, crosses, overlaps, equals, disjoint oraz wielu reguł z and/or, odległość geodezyjna within distance między dowolnymi geometriami (punkty, linie, wielokąty: najmniejsza odległość na kuli o promieniu 6371 km), najbliższe N według tej samej odległości z odległością maksymalną (pojedyncza reguła nearest nie zapisuje kolumny Distance, tak jak Savant jej nie zapisuje; w połączeniu z innymi regułami jako nearest-then-filter, złączenia AND i sumy OR, każda reguła nearest dodaje własną kolumnę Distance) oraz Cross, ze strumieniami dopasowanymi i niedopasowanymi. |
| Spatial Summarize Agent (`spatial_summarize`) | Pełny | [Łączenie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid i kroki punkt-linia | Suma, przecięcie, prostokąt ograniczający, jeden lub kilka środków geometrycznych oraz budowa polilinii lub wielokątów, dla każdej grupy z opcjonalnym sortowaniem. |
| Split Agent (`split`) | Pełny | Split Text lub [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z kolumnami split_part | Dzieli pole tekstowe po literalnym separatorze o dowolnej długości na wiersze lub kolumny, z przycinaniem i zachowaniem oryginału; liczba kolumn jest odczytywana z danych w czasie uruchomienia. |
| Split Output (`outlet`) | Pełny | Krawędź przepływu pracy | Kieruje nazwane wyjście do jego odbiorców. |
| Stack Agent (`multi_stack`) | Pełny | [Union All](/pl/reference/workflow-steps/tables/table-union-all/) | Łączy w stos dowolną liczbę wejść według nazwy lub pozycji. |
| Summarize Agent (`summarize`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z agregacją | Grupuje i agreguje, łącznie z pierwszym/ostatnim według deterministycznego sortowania oraz agregatami okna dla każdego wiersza (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z agregacją | Agregacja po stronie bazy danych, konwertowana tak samo jak Summarize. |
| Text (`text`) | Pełny | Adnotacja kanwy | Zachowany jako kontekst przepływu pracy. |
| Time Series Agent (`rollup`) | Pełny | Agregacja [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) po wyrażeniu koszyka okresu, Period Spine, [Anti Join](/pl/reference/workflow-steps/tables/table-anti-join/) i [Union All](/pl/reference/workflow-steps/tables/table-union-all/) | Zwija rekordy do okresów dnia, tygodnia, miesiąca, kwartału, roku lub dekady między opcjonalnymi datami początku i końca, dla każdej grupy, z wyłączeniem dat NULL i z uzupełnieniem pustych okresów zerami. |
| Transform Agent (`edit`) | Pełny | [Table Extract](/pl/reference/workflow-steps/tables/table-extract/) z wyrażeniami kolumn | Kolumny obliczane, zmiany typów i obliczenia okienkowe (lag, lead, suma narastająca, numer wiersza, wypełnianie w przód i w tył), oceniane po kolei. Edycja zawierająca tylko skompilowane kroki jest konwertowana jako te kroki stosowane po kolei, z których każdy zasila następny. |
| Unpivot Agent (`unpivot`) | Pełny | [Melt](/pl/reference/workflow-steps/tables/table-melt/) | Zamienia kolumny w wiersze jako parę nazwa/wartość. |
| Vision Agent (`vision`) | Pełny | [Image OCR](/pl/reference/workflow-steps/text-documents/image-ocr/), a następnie zadanie z promptem [AI/NLP](/pl/reference/workflow-steps/text-documents/nlp-ai/) | Każdy dokument trafia do dostawcy jako obraz lub PDF, gdy ten akceptuje taki typ i rozmiar, w przeciwnym razie wysyłana jest warstwa tekstowa PDF lub tekst z OCR; odpowiedź na prompt trafia do kolumny AI Answer. |
| XML Agent (`xml`) | Pełny | [Analiza XML](/pl/reference/workflow-steps/tables/table-xml-parse/) | Wybiera elementy, wyodrębnia wartości i atrybuty elementów podrzędnych do kolumn lub konwertuje XML na JSON; prosta ścieżka //a/b jest konwertowana jak dotąd, a każda inna ścieżka XPath 1.0 (predykaty, testy atrybutów, symbole wieloznaczne, funkcje takie jak count(), name() i contains()) jest obliczana jako XPath, z uwzględnieniem przestrzeni nazw lub tak, jak zapisano. |

Warianty okablowania, kanwy i pushdown (Split Output, Group, Text, Filter Pushdown, Summarize Pushdown) to typy węzłów Savant bez własnego artykułu o agencie w centrum pomocy; każdy jest konwertowany jak agent, który odzwierciedla.

Poświadczenie w żądaniu API Agent nigdy nie jest kopiowane do kroku przepływu pracy. Przez https trafia do połączenia REST; przez http, bez uprawnienia do zapisu połączeń lub w konwersji wykonanej przez MCP jest wstrzymywane z ostrzeżeniem. Jest to zamierzone i nie obniża poziomu.

Dwa ograniczenia celu nie obniżają poziomu. Kilka rzadkich zestawów znaków (na przykład `x-ISCII91` lub `JIS_X0212`) nie może być zapisanych; plik jest zapisywany jako UTF-8, a konwersja ostrzega. Publikacja Tableau scalająca po kluczach wymaga `replace: true` w powiązaniu celu; bez niego konwersja ostrzega i publikuje nowe źródło danych, co kończy się niepowodzeniem w uruchomieniu, w którym ono już istnieje.

## Nazwane odrzucenia

Osiem konstrukcji jest odrzucanych z nazwy zamiast konwertowanych. Żadna nie obniża poziomu agenta.

| Konstrukcja | Dlaczego jest odrzucana |
| --- | --- |
| Żądanie API Agent, które zawiera poświadczenie i pobiera host z pola wejściowego | Każdy wiersz mógłby wysłać poświadczenie do hosta wybranego przez dane. Żądanie staje się nazwanym symbolem zastępczym. Żądanie bez poświadczenia oraz poświadczenie na stałym hoście są konwertowane. |
| Edycja Transform bez wyrażenia i bez skompilowanych kroków, taka jak edycja Copilot, która ma tylko swój prompt | Nie ma czego konwertować: prompt nie jest formułą. Edycja ze skompilowanymi krokami jest konwertowana. |
| Konstrukcja wyrażenia regularnego w wyrażeniu Transform lub Filter, której PlaidCloud nie potrafi odczytać: klasa w klasie, przecięcie klas (`&&`) lub nieznana właściwość `\p{}` | Krok staje się nazwanym symbolem zastępczym, który odmawia wykonania w czasie uruchomienia. |
| Funkcja agregująca lub okienkowa w wyrażeniu Transform lub Filter | Sam Savant kończy się na niej niepowodzeniem w czasie uruchomienia. Jako obliczenie Transform lub w Summarize jest konwertowana. |
| `HASH` w wyrażeniu Transform lub Filter z literalnym algorytmem innym niż `md5` lub `sha1` | Sam Savant kończy się na nim niepowodzeniem (algorytm to `md5` lub `sha1`). Algorytm odczytany z kolumny jest konwertowany i daje NULL dla każdej innej wartości. |
| Sortowanie celu po kolumnie, której jego wejście nie zawiera | Sam Savant kończy się na nim niepowodzeniem w czasie uruchomienia. |
| Plik, podfolder, karta lub arkusz celu na każdą wartość kolumny, której jego wejście nie zawiera | Sam Savant kończy się na nim niepowodzeniem w czasie uruchomienia. |
| Ścieżka XML Agent, która nie jest XPath 1.0 | Savant również nie potrafi jej uruchomić. |

Względny adres URL API jest konwertowany, gdy powiążesz bazowy adres URL lub połączenie REST przez `api_bindings`; zobacz [Powiązania czasu konwersji](/pl/guides/workflows/migrate-savant-analyses/#powiązania-w-czasie-konwersji).

## Język wyrażeń

Funkcje i operatory wyrażeń Savant są konwertowane na wyrażenia PlaidCloud. Poziom: **Pełny**. Każda funkcja i każdy format są konwertowane, w tym `TO_TEXT` ze wzorcem liczbowym, format znany dopiero dla każdego wiersza, tokeny dat z ułamkami sekund, tygodniowe, kwartalne i strefowe, dwucyfrowe lata oraz konstrukcje wyrażeń regularnych Java. Funkcje GEO_* w dowolnym miejscu wyrażenia działają w towarzyszących krokach Spatial. Wyjątkiem są [nazwane odrzucenia](#nazwane-odrzucenia).

Znane przypadki szczególne: `TO_DATE` lub `TO_DATETIME` z formatem zawierającym literał `[`, `]`, cudzysłów, ukośnik odwrotny lub `^`, dla tekstu, który odczytuje się jako 9999-12-30 lub 9999-12-31, czyli po ostatnim znaczniku czasu obsługiwanym przez magazyn danych; konwersja ostrzega.

## Formaty eksportu

Moduł ładujący akceptuje każdy kształt eksportu Savant (płaski, opakowany w model, rekord serwera, koperta przepisu, opakowany w tablicę, z prefiksem BOM oraz starsze aliasy typów) i normalizuje je do jednego modelu. Poziom: **Pełny**.

## Parametry analizy

Parametry analizy Savant są konwertowane na zmienne przepływu pracy, a odwołania do nich w konfiguracjach węzłów są przepisywane na składnię zmiennych PlaidCloud. Ładowane są kształty parametrów w postaci listy, słownika i z aliasami. Poziom: **Pełny**.

Znane przypadki szczególne: parametr, którego nazwa zawiera słowo wskazujące na sekret lub którego wartość wygląda jak poświadczenie, staje się zmienną z pustą wartością, z ostrzeżeniem. Parametr używany przez węzeł, którego eksport nie deklaruje, staje się zmienną z pustą wartością, z ostrzeżeniem.

## Łączenie z systemami zewnętrznymi

Konektory Savant to cele źródłowe i docelowe, a nie kroki, a eksport nie zawiera zbiorów danych ani poświadczeń. PlaidCloud łączy się z tymi systemami przez połączenie, a nie przez węzeł na kanwie.

| Savant | Dokąd trafia w PlaidCloud |
| --- | --- |
| Konektor źródła | `source_bindings` mapuje węzeł lub zbiór danych Savant na tabelę PlaidCloud lub plik Dokumentu, odczytywany przez odpowiedni krok importu; źródło bez powiązania ostrzega i niczego nie przetwarza |
| Cel: CSV, Excel i inne formaty plików | Krok eksportu ([Eksport: CSV](/pl/reference/workflow-steps/export/export-to-csv/), [Eksport: Excel](/pl/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/pl/reference/workflow-steps/export/export-to-pdf/)) |
| Cel: Arkusze Google, Tableau, Slack | [Export to Google Spreadsheet](/pl/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/) lub [Notify via Slack](/pl/reference/workflow-steps/notifications/notify-via-slack/), przez połączenie powiązane za pomocą `destination_bindings` |
| Cel: niepowiązana baza danych, magazyn danych lub cel SaaS (Oracle, ogólna baza danych, Looker Studio, NetSuite, SAP oraz Arkusze Google, Tableau lub Slack bez powiązanego połączenia) | Tabela projektu nazwana według węzła celu, z ostrzeżeniem wskazującym pierwotny cel |
| Cel: niepowiązany cel systemu plików (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | Plik, w typie pliku celu, w folderze Dokumentów odzwierciedlającym folder docelowy, z ostrzeżeniem. Poświadczenia i tokeny udostępniania są usuwane ze ścieżki folderu |
| Cel: niepowiązany e-mail | Plik CSV z ostrzeżeniem |
| Cel: powiązanie, którego nie można użyć | Plik CSV z ostrzeżeniem wskazującym pierwotny cel |

Konwersja nigdy nie łączy się z systemem źródłowym ani docelowym.
