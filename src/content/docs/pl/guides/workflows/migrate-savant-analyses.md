---
title: Migracja analiz Savant
description: Skonwertuj eksport analizy Savant Labs na zaawansowany przepływ pracy PlaidCloud z poziomu aplikacji Analyze, REST API lub agenta AI połączonego przez MCP, powiąż jego źródła i przeczytaj raport z konwersji.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

PlaidCloud jest bezpośrednim zamiennikiem Savant. Każdy agent, wyrażenie i ustawienie Savant jest konwertowane na PlaidCloud i działa. Konwerter przekształca eksport analizy Savant Labs w działający zaawansowany przepływ pracy: mapuje każdego agenta Savant na krok przepływu pracy, zmienną projektu lub obiekt na kanwie, zachowuje oryginalny graf i zwraca raport z konwersji, który wskazuje wszystko, czego nie udało się skonwertować.

Konwersja odczytuje wyłącznie plik eksportu, który wskażesz, oraz nagłówki plików powiązanych z jego źródłami. Nigdy nie łączy się z systemem, z którym łączy się źródło lub miejsce docelowe Savant.

## Co tworzy PlaidCloud

- Każdy agent Savant staje się odpowiednim krokiem przepływu pracy, z zachowaniem relacji nadrzędnych i podrzędnych. [Macierz konwersji Savant](/pl/reference/savant-conversion-matrix/) wymienia każdego agenta i jego poziom mapowania.
- Parametry analizy Savant stają się zmiennymi projektu, a odwołania do nich w ustawieniach agentów są przepisywane na składnię zmiennych PlaidCloud.
- Notatki i grupy trafiają na kanwę jako notatki i grupy.
- Każde źródło staje się krokiem importu lub odczytuje istniejącą tabelę, zależnie od sposobu powiązania.
- Każdy typ agenta Savant jest konwertowany w pełni: każda opcja ma swoje mapowanie. Konfiguracja, przy której zawodzi sam Savant lub która nie jest udokumentowana, trafia jako nazwany krok zastępczy. Zobacz [Kroki zastępcze dla niekonwertowanych konfiguracji](#kroki-zastępcze-dla-niekonwertowanych-konfiguracji).

## Zanim zaczniesz

1. Wyeksportuj analizę z Savant za pomocą **Export JSON**.
2. Prześlij plik `.json` na [konto dokumentów](/pl/guides/documents/adding-accounts/), które możesz odczytać.
3. Wybierz projekt PlaidCloud, który ma otrzymać przepływ pracy. Potrzebujesz do niego uprawnień do zapisu.
4. Wybierz konto dokumentów i folder bazowy, z których będą odczytywane pliki źródłowe analizy.

## Konwersja analizy

Konwertuj z aplikacji Analyze, przez REST API lub z katalogu narzędzi MCP. Wszystkie trzy przyjmują te same pola.

### Aplikacja Analyze

1. Otwórz **Analyze** i wybierz **Tools → Importuj analizę Savant**.
2. Wybierz **Projekt docelowy** oraz **Plik eksportu Savant (.json)** przesłany na konto dokumentów.
3. Wybierz **Załaduj źródła**. Okno wyświetli listę węzłów źródłowych z eksportu.
4. Aby powiązać źródło z danymi, które już masz, zaznacz je i wybierz **Powiąż…**. Wybierz **Tabela projektu**, aby odczytać tabelę w projekcie docelowym, lub **Dokument**, aby odczytać plik z konta dokumentów (z opcjonalną nazwą arkusza dla Excela). Wybierz **Usuń powiązanie**, aby usunąć powiązanie.
5. W polu **Katalog niepowiązanych źródeł** wybierz konto dokumentów i folder bazowy, z których odczytywane są pliki niepowiązanych źródeł.
6. W sekcji **Opcje konwersji** wybierz **Typ przepływu pracy** oraz czy **Zezwalaj na niekonwertowane symbole zastępcze**. W sekcji **Prefiksy obiektów** możesz opcjonalnie ustawić prefiksy przepływu pracy, kroków i tabel.
7. Wybierz **Konwertuj**.

Po zakończeniu konwersji okno wyświetla raport z konwersji: nazwę przepływu pracy i prefiks tabel, ostrzeżenia, tabelę ścieżek dokumentów, do których należy przesłać pliki dla niepowiązanych źródeł, oraz kroki wymagające przeglądu. Jeśli nie można załadować listy źródeł, dodaj wiersz dla każdego źródła z jego identyfikatorem węzła i identyfikatorem `analyzetable_` tabeli, którą chcesz powiązać.

### Pola

REST API i narzędzie MCP przyjmują te pola.

| Pole | Wymagane | Co robi |
| --- | --- | --- |
| `source_account_id` | Tak | Konto dokumentów zawierające eksport Savant. |
| `source_file_path` | Tak | Ścieżka eksportu na tym koncie. |
| `project_id` | Tak | Projekt, w którym tworzony jest przepływ pracy. |
| `document_account_id` | Tak | Konto dokumentów, z którego odczytywane są niepowiązane źródła. |
| `document_account_path` | Tak | Folder bazowy na tym koncie dla niepowiązanych źródeł. Pusta wartość lub `/` oznacza katalog główny konta, a początkowy `/` jest ignorowany. Ścieżki z `..` lub segmentami zaczynającymi się od kropki, nawiasami klamrowymi, literą dysku lub schematem URL albo znakami sterującymi są odrzucane. |
| `workflow_prefix` | Nie | Prefiks dodawany do nazw przepływów pracy. |
| `step_prefix` | Nie | Prefiks dodawany do nazw kroków. |
| `table_prefix` | Nie | Prefiks dodawany do nazw tabel. Domyślnie jest to nazwa samego przepływu pracy. Prefiks, który użyłby ponownie istniejącej nazwy tabeli, jest odrzucany, zanim cokolwiek zostanie utworzone. Użyty prefiks jest zwracany w raporcie z konwersji. |
| `workflow_type` | Nie | `advanced` (domyślnie) układa graf na kanwie DAG. `standard` tworzy szeregową listę kroków. |
| `source_bindings` | Nie | Wiąże źródła z istniejącymi danymi. Zobacz [Wiązanie źródeł](#wiązanie-źródeł). |
| `destination_bindings` | Nie | Kieruje miejsca docelowe do konta dokumentów, tabeli połączenia, Arkusza Google, źródła danych Tableau, kanału Slack lub adresatów e-mail. Tylko REST i MCP. Zobacz [Miejsca docelowe](#miejsca-docelowe). |
| `api_bindings` | Nie | Określa, dokąd trafia względny adres URL agenta API: bazowy adres URL lub połączenie REST. Tylko REST i MCP. Zobacz [Wiązanie żądań API](#wiązanie-żądań-api). |
| `allow_unconverted_placeholders` | Nie | Określa, co robi krok zastępczy w czasie wykonania. Zobacz [Kroki zastępcze dla niekonwertowanych konfiguracji](#kroki-zastępcze-dla-niekonwertowanych-konfiguracji). |

### REST

Wyślij pola jako treść JSON pod adres:

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

Aby wyświetlić węzły źródłowe eksportu przed zbudowaniem `source_bindings`, wyślij `source_account_id` i `source_file_path` pod adres:

```text
POST /rest/v1/analyze/savant/sources
```

Każdy wpis w odpowiedzi zawiera `node_id`, `name` i `connector` źródła.

### MCP

Agent AI połączony przez MCP wywołuje narzędzie `savant_convert` z tymi samymi polami. Informacje o łączeniu agenta znajdziesz w [agentach AI (MCP)](/pl/integrations/ai-coding-agents/). Narzędzie zmienia Twój projekt, więc przejrzyj wywołanie, zanim je zatwierdzisz.

## Powiązania w czasie konwersji

Eksport Savant nie zawiera danych, poświadczeń ani połączeń, dlatego trzy parametry czasu konwersji łączą go z Twoimi zasobami. Każdy z nich jest mapą z identyfikatora lub nazwy węzła Savant na cel, a powiązanie, którego nie możesz użyć, powoduje odrzucenie całej konwersji, zanim cokolwiek zostanie utworzone.

| Parametr | Co wiąże | Sekcja |
| --- | --- | --- |
| `source_bindings` | Agenci źródłowi z tabelami lub plikami | [Wiązanie źródeł](#wiązanie-źródeł) |
| `destination_bindings` | Agenci docelowi z plikiem, tabelą, arkuszem, źródłem danych Tableau, kanałem Slack lub e-mailem | [Miejsca docelowe](#miejsca-docelowe) |
| `api_bindings` | Agenci API ze względnym adresem URL z bazowym adresem URL lub połączeniem REST | [Wiązanie żądań API](#wiązanie-żądań-api) |

## Wiązanie źródeł

Eksport Savant opisuje, skąd pochodzą jego dane, ale nie zawiera danych ani poświadczeń. Użyj `source_bindings`, aby połączyć każde źródło z danymi, które już masz w PlaidCloud. Kluczem jest identyfikator węzła źródła, identyfikator zbioru danych lub nazwa. Wartością jest:

- Identyfikator `analyzetable_` tabeli w projekcie docelowym. Skonwertowany przepływ pracy odczytuje tę tabelę bezpośrednio.
- Obiekt z polami `account`, `path` i opcjonalnie `sheet`, aby odczytać plik z konta dokumentów.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Powiązanie, którego nie możesz odczytać, jest odrzucane. Klucz, który nie pasuje do żadnego źródła, jest zgłaszany jako ostrzeżenie.

Ścieżka pliku źródłowego w eksporcie może zaczynać się od `/` lub przebiegać przez foldery z kropką, takie jak `.archive`, i jest konwertowana. Źródło odczytujące XML konwertuje tekst XML, a źródło dokumentu XML zawiera też kolumny kontekstu pliku Savant.

### Niepowiązane źródła

Źródło bez powiązania staje się krokiem importu bez danych, a raport z konwersji zawiera dla niego ostrzeżenie. Krok odczytuje dane z:

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Prześlij plik pod tę ścieżkę i uruchom przepływ pracy. Dopóki pliku nie ma, krok importu kończy się z ostrzeżeniem i tworzy pustą tabelę, a przepływ pracy jest kontynuowany.

## Jak konwertowani są agenci

Większość agentów jest konwertowana na krok, który zbudowałbyś ręcznie; [macierz konwersji Savant](/pl/reference/savant-conversion-matrix/) wymienia każdego agenta. Ci agenci wymagają dodatkowej uwagi.

| Agent Savant | Na co się przekształca | Zastrzeżenia |
| --- | --- | --- |
| Infer Agent (`gen_ai` oraz starszy `service` z usługą LLM) | Krok [AI/NLP](/pl/reference/workflow-steps/text-documents/nlp-ai/) z zadaniem **Prompt**. Prompt jest uruchamiany raz dla każdego wiersza na polach wejściowych, a odpowiedź trafia do kolumny **AI Answer** obok każdej kolumny wejściowej. Limit wierszy staje się **Maks. liczba wierszy**, a puste źródło ostrzega i zapisuje pustą tabelę. **Max New Rows** odpowiada tylko na wiersze, które są nowe, i zachowuje odpowiedzi z wcześniejszych uruchomień. | Odpowiada model LLM, więc wynik nigdy nie jest identyczny bajt w bajt z wynikiem Savant i może się różnić między uruchomieniami. Każde wywołanie ma swój koszt. Zobacz [Dostawcy AI](#dostawcy-ai). Partia, która się nie powiedzie, zachowuje swoje wiersze z pustą odpowiedzią i ostrzega. |
| Vision Agent (`vision`) | Krok [Document Read Blob](/pl/reference/workflow-steps/text-documents/document-blob-extract/), [Image OCR](/pl/reference/workflow-steps/text-documents/image-ocr/), a następnie zadanie **Prompt** AI/NLP. Każdy dokument trafia do dostawcy jako obraz lub plik PDF, gdy dostawca akceptuje ten typ i rozmiar. W przeciwnym razie krok wysyła warstwę tekstową pliku PDF lub tekst z OCR. | Takie same zastrzeżenia dotyczące LLM jak w przypadku Infer Agent. Całe dokumenty opuszczają PlaidCloud i trafiają do dostawcy, a konwersja ostrzega o tym. Pliki TIFF i BMP są wysyłane jako tekst z OCR, a ustawienia maksymalnego rozmiaru dokumentu nie ma. Dokument, którego nie znaleziono, jest pomijany, a krok ostrzega, podając jego ścieżkę. |
| API Agent (`apiService` oraz starszy `service` z usługą API) | Krok [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/), który wysyła jedno żądanie na wiersz wejściowy, a następnie złączenie zwrotne zachowujące każdy wiersz wejściowy. Surowa treść odpowiedzi trafia do kolumny tekstowej, obok której znajduje się kolumna statusu. Limit na okres staje się ułamkową wartością **Maks. liczba żądań/s**. Względny adres URL jest łączony z bazowym adresem URL lub połączeniem REST powiązanym przez `api_bindings`. Host, port lub ścieżka pochodzące z pola wiersza są uzupełniane dla każdego wiersza. Stronicowanie przez następny adres URL, nagłówek Link, przesunięcie i numer strony jest obsługiwane, a wartość stronicowania (początek, rozmiar strony lub nazwa parametru) może pochodzić z pola wejściowego lub parametru. | Metoda inna niż GET działa na systemie produkcyjnym raz dla każdego wiersza wejściowego przy każdym uruchomieniu przepływu pracy, więc przed pierwszym uruchomieniem potwierdź cel. Żądania inne niż GET nie są automatycznie ponawiane. Nieudane żądanie pozostaje jako wiersz z jego statusem. Żądanie zawierające poświadczenie nie może pobierać hosta z pola wiersza. Poświadczenia są obsługiwane w sposób opisany w sekcji [Kroki API z poświadczeniami](#kroki-api-z-poświadczeniami). |
| Recursion Agent (`hierarchy`) | Krok [Hierarchy Closure](/pl/reference/workflow-steps/tables/table-hierarchy-closure/), który przechodzi każdy wiersz w górę łańcucha elementów nadrzędnych na dowolną głębokość, a następnie agreguje każdy węzeł po identyfikatorach na jego ścieżce do korzenia, włącznie z nim samym. Zapisuje Depth i Path. Wiersz z pustym elementem nadrzędnym lub wskazujący siebie jako element nadrzędny jest korzeniem. | Pętla w identyfikatorach elementów nadrzędnych zatrzymuje się na powtórzonym węźle i zachowuje wszystkich przodków przed nim. Wiersze z kilkoma elementami nadrzędnymi zachowują własne wartości. |
| Search and Replace (`search_replace`) | Krok [Table Extract](/pl/reference/workflow-steps/tables/table-extract/), który stosuje każdą regułę po kolei do wybranych kolumn tekstowych, z uwzględnieniem wielkości liter lub bez, jako całe słowo lub nie. Każda reguła działa w swoim trybie: zastąp dopasowany tekst, zastąp całą komórkę, gdy zawiera tekst, zastąp całą komórkę, gdy dokładnie pasuje, lub dołącz do komórki. | Reguły to tekst dosłowny, a nie wzorce. |
| Split (`split`) | Krok [Split Text](/pl/reference/workflow-steps/tables/table-split-text/). Dzieli na kolumny lub wiersze według dosłownego separatora o dowolnej długości i ustala liczbę kolumn na podstawie danych w czasie uruchomienia przepływu pracy. | Brak. |
| Time Series (`rollup`) | Krok Table Extract grupujący według wyrażenia okresu, wraz z [Period Spine](/pl/reference/workflow-steps/tables/table-period-spine/), anty-złączeniem i sumą, które uzupełniają zerami okresy bez rekordów. | Rekordy z wartością NULL w dacie są wykluczane. Oś okresów kończy się na 100 000 okresów. |
| Format (`format`) | Krok Table Extract ze zmianami nazw, zmianami typów, ukrywaniem i uzupełnianiem lub krok [Promote Header](/pl/reference/workflow-steps/tables/table-promote-header/) dla opcji zastąpienia nazw wierszem. | Uzupełnienie w kolumnie, która nie jest tekstowa, rzutuje wartość domyślną na typ kolumny. Awansowanie nagłówka nad źródłem, które nie deklaruje kolumn, odczytuje każdą kolumnę z plików CSV, Excel, XLS, JSON, Parquet i Avro. Zobacz [Pliki bez zadeklarowanych kolumn](#pliki-bez-zadeklarowanych-kolumn). |
| Spatial Match Agent (`spatial_match`) | Krok [Dopasowanie przestrzenne (wykonawca)](/pl/reference/workflow-steps/spatial/spatial-match-executor/) dla relacji intersects, within, contains, touches, crosses, overlaps, equals i disjoint, z kilkoma połączonymi regułami; Złączenie krzyżowe dla dopasowania krzyżowego; [Znajdź najbliższe](/pl/reference/workflow-steps/spatial/spatial-find-nearest/) dla dopasowania najbliższego. | Dopasowanie najbliższego szereguje i filtruje według odległości po okręgu wielkim, tak jak robi to Savant. Reguła najbliższego połączona z innymi regułami najpierw znajduje najbliższe rekordy, a następnie stosuje pozostałe reguły: z AND wynik zachowuje rekordy spełniające każdą regułę, a z OR łączy najbliższe rekordy z rekordami pasującymi do pozostałych reguł. Reguła najbliższego bez liczby i bez maksymalnej odległości zachowuje jeden najbliższy rekord. Dopasowanie w obrębie odległości również jest konwertowane, w kilometrach, gdy reguła nie podaje jednostki, i mierzy odległość geodezyjną między dowolnymi geometriami, a nie tylko punktami. Geometria, której nie można przeanalizować, daje NULL lub brak dopasowania, z ostrzeżeniem. |
| Spatial Summarize Agent (`spatial_summarize`) | [Łączenie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-combine/) dla sumy, części wspólnej i prostokąta ograniczającego, a także [Spatial Centroid](/pl/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/pl/reference/workflow-steps/spatial/spatial-point-to-line/) i [Spatial Line to Polygon](/pl/reference/workflow-steps/spatial/spatial-line-to-polygon/) dla środka geometrycznego oraz budowania linii lub wielokątów. | Wielokąt zbudowany z mniej niż 3 punktów jest wielokątem pustym. |
| Destination Agent (`destination`) | Krok eksportu do powiązanego celu albo tabela projektu lub plik, gdy cel nie jest powiązany. Zobacz [Miejsca docelowe](#miejsca-docelowe). | Zobacz [Przypadki brzegowe](#przypadki-brzegowe). |

`GEO_POINT`, `GEO_TYPE` i `GEO_SPATIAL_DISTANCE` są konwertowane na wyrażenia. Edycja, której całe wyrażenie jest inną funkcją `GEO_*`, taką jak `GEO_AREA` lub `GEO_UNION`, jest konwertowana na odpowiedni krok przestrzenny, w tym [Spatial Info](/pl/reference/workflow-steps/spatial/spatial-info/). Geometria jest przekazywana jako tekst WKT. `GEO_AREA`, `GEO_PERIMETER` i `GEO_SPATIAL_DISTANCE` w milach używają mili lądowej.

Źródło odczytujące pliki binarne, takie jak dokumenty odczytywane przez agenta Vision, jest konwertowane na wyodrębnienie dokumentu z powiązanego dokumentu lub z pliku oczekiwanego pod ścieżką niepowiązanych źródeł.

## Dostawcy AI

Agent Infer lub Vision jest konwertowany na krok AI/NLP, który korzysta z połączenia LLM. Konwerter obsługuje Anthropic, OpenAI, Gemini, Azure OpenAI, Grok i GitHub Models.

- Konwerter wybiera połączenie dla dostawcy i modelu wskazanego przez agenta spośród połączeń LLM widocznych dla importującego użytkownika. Nigdy nie wskazuje połączenia, którego użytkownik nie widzi. W przypadku asystenta AI (MCP) oznacza to połączenia widoczne dla użytkownika asystenta.
- Gdy dla dostawcy nie ma widocznego połączenia albo dostawca Savant nie ma odpowiednika w PlaidCloud (hostowane w chmurze API modeli lub dostawca z własnym kluczem w obszarze roboczym Savant), krok używa domyślnego połączenia obszaru roboczego, jeśli użytkownik może je zobaczyć. W przeciwnym razie pozostawia połączenie puste, a krok używa domyślnego połączenia obszaru roboczego podczas uruchomienia. Raport z konwersji w obu przypadkach ostrzega, więc jeśli ma odpowiadać inne połączenie, wybierz je w kroku.

## Miejsca docelowe

Miejsce docelowe Savant zapisuje otrzymaną tabelę do powiązanego celu. Powiąż miejsca docelowe za pomocą `destination_bindings` w treści REST lub wywołaniu MCP. Kluczem jest identyfikator węzła lub nazwa miejsca docelowego. Okno aplikacji Analyze nie wiąże miejsc docelowych, więc miejsce docelowe skonwertowane tam zapisuje wynik niepowiązany, opisany w sekcji [Niepowiązane miejsca docelowe](#niepowiązane-miejsca-docelowe).

| Cel | Powiązanie | Wynik |
| --- | --- | --- |
| Konto dokumentów | `{account, path[, file_name]}` | Plik CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF lub Tableau Hyper, zależnie od rodzaju miejsca docelowego. Potrzebujesz uprawnienia do zapisu w magazynie dokumentów na tym koncie. |
| Tabela w połączeniu | `{connection, table[, schema, replace]}` | Krok [Export: External Database Tables](/pl/reference/workflow-steps/export/export-external-tables/). Potrzebujesz uprawnienia do zapisu w połączeniu. Zastąpienie tabeli wymaga `replace: true`. |
| Arkusze Google | `{connection, spreadsheet_name[, sheet_name, replace]}` lub `{connection, spreadsheet_id[, sheet_name, replace]}` | Krok [Export to Google Spreadsheet](/pl/reference/workflow-steps/export/export-to-google-spreadsheet/) na połączeniu Arkuszy Google. Karta domyślnie ma nazwę wskazaną przez miejsce docelowe, a w przeciwnym razie `Sheet1`. Miejsce docelowe, które zastępuje wiersze arkusza, czyści kartę, więc wymaga `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | Ekstrakt Tableau Hyper zapisany w folderze konta, a następnie krok [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/) na [połączeniu Tableau](/pl/reference/connectors/collaboration/tableau/). Zastąpienie źródła danych lub zmiana jego wierszy według kluczy dopasowania wymaga `replace: true`. |
| Slack | `{connection[, channel]}` | Plik CSV jest zapisywany na koncie dokumentów, a następnie krok [Notify via Slack](/pl/reference/workflow-steps/notifications/notify-via-slack/) przesyła go na kanał. Połączenie wymaga tokenu bota, a kanał musi być identyfikatorem kanału, pobranym z powiązania lub, w jego braku, z eksportu. |
| E-mail | `{email_to: [...]}` oraz `email_export_recipients: true`, aby użyć także adresatów wymienionych w eksporcie | Plik CSV jest wysyłany e-mailem jako załącznik. Potrzebujesz uprawnienia do zapisu e-maili. |

Połączenie z Arkuszami, Tableau lub Slack jest sprawdzane tak samo jak połączenie z tabelą: musisz je widzieć i mieć uprawnienie do zapisu w połączeniu, inaczej konwersja zostanie odrzucona.

### Tryby zapisu

- Miejsce docelowe pliku lub tabeli, które dołącza dane, odczytuje wcześniejszy plik z powrotem i zapisuje go ponownie wraz z nowymi wierszami. Nigdy go nie nadpisuje.
- Miejsce docelowe upsert, update lub groupReplace scala dane według kluczy dopasowania miejsca docelowego. Plik lub tabela są odczytywane z powrotem i zapisywane ponownie, a w źródle danych Tableau pasujące wiersze są zmieniane w miejscu.
- Dołączanie i scalanie działają także na istniejących plikach podzielonych według wartości, bez nagłówka (wiersze są dopasowywane według pozycji), plikach Excel zakotwiczonych w komórce w lewym górnym rogu oraz plikach w zestawie znaków innym niż UTF-8. Podział odczytuje z powrotem plik, do którego zapisywana jest każda wartość, i scala dane w jego obrębie, pozostawiając pozostałe pliki bez zmian.
- Miejsce docelowe Tableau mapuje tryby Savant na sześć trybów [Publish to Tableau](/pl/reference/workflow-steps/export/export-to-tableau/#tryby): append i insert dodają wiersze, replace nadpisuje, a upsert, update i groupReplace dopasowują według kluczy. Tryb zmieniający istniejące dane publikuje tylko wtedy, gdy powiązanie zawiera `replace: true`; w przeciwnym razie miejsce docelowe publikuje nowe źródło danych, a raport o tym informuje.
- Miejsce docelowe z kodowaniem wyjściowym zapisuje plik w tym zestawie znaków Javy. Znak, którego zestaw nie zawiera, jest zapisywany jako `?`, tak jak w Savant. Akceptowane są aliasy Javy, CESU-8 i formy ze znacznikiem kolejności bajtów. Kilku rzadkich zestawów znaków (na przykład `x-ISCII91` lub `JIS_X0212`) nie można zapisać; plik jest zapisywany jako UTF-8, a raport ostrzega. Podział w zestawie znaków innym niż UTF-8 konwertuje folder.
- Nazwy plików eksportu muszą pozostawać wewnątrz powiązanego folderu.

### Co mogą wiązać wywołujący AI

Konwersja przez asystenta AI (MCP) wiąże te same kształty, ale z zatrzymaniem niektórych części, każde z ostrzeżeniem wskazującym daną część:

| Zatrzymana część | Co dzieje się zamiast tego |
| --- | --- |
| `replace` w tabeli, arkuszu lub źródle danych Tableau | Miejsce docelowe, które dołącza dane, nadal dołącza je do powiązanej tabeli lub arkusza. Miejsce docelowe, które zastępuje dane, zapisuje plik CSV. Miejsce docelowe Tableau publikuje nowe źródło danych. |
| Adresaci e-mail | Zamiast e-maila zapisywany jest plik CSV. |
| Slack | Zamiast wpisu na Slacku zapisywany jest plik CSV. |

Aby powiązać te części, konwertuj z aplikacji Analyze lub przez REST API albo zaloguj się samodzielnie, zamiast korzystać z asystenta.

### Niepowiązane miejsca docelowe

Miejsce docelowe bez powiązania zapisuje swój odpowiednik w PlaidCloud i ostrzega **Destination target unbound**, podając nazwę oryginalnego celu. Konwersja nigdy nie łączy się z systemem docelowym.

| Miejsce docelowe | Wynik |
| --- | --- |
| Cel typu baza danych, hurtownia lub SaaS (Oracle, ogólna baza danych, Looker Studio, NetSuite, SAP oraz Arkusze Google, Tableau lub Slack bez powiązanego połączenia) | Tabela w projekcie, nazwana od węzła miejsca docelowego. |
| Magazyn plików (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | Plik, w typie pliku miejsca docelowego, w folderze dokumentów na koncie podanym dla niepowiązanych źródeł. Folder odzwierciedla folder docelowy. Poświadczenia i tokeny udostępniania są usuwane ze ścieżki. |
| E-mail | Plik CSV na koncie dokumentów podanym dla niepowiązanych źródeł. |

Ostrzeżenie informuje, co powiązać, aby dotrzeć do rzeczywistego celu. Miejsce docelowe, którego powiązania nie można użyć, zapisuje plik CSV i ostrzega **Fallback, target not written**, podając w komunikacie oryginalny cel; sprawdź ten plik CSV, zanim na nim polegasz. Zwykłe miejsce docelowe CSV zapisuje własny plik.

### Podzielone miejsca docelowe

Miejsce docelowe zapisujące plik, podfolder lub kartę dla każdej wartości pola dzieli pliki CSV, Excel, Parquet i PDF oraz karty Arkuszy Google.

- **Parquet i PDF.** Jeden plik na wartość.
- **Arkusze Google.** Jedna karta na wartość.
- **Szablon.** Szablonowy skoroszyt jest podstawą skoroszytu dla każdej wartości. Brakujący szablon powoduje ostrzeżenie, a skoroszyt jest zapisywany bez niego.
- **Wartości NULL.** Wartość podziału NULL jest zapisywana do osobnego pliku lub karty i nie jest pomijana.
- **Pole, którego brakuje w danych wejściowych.** Podział lub sortowanie według pola, którego dane wejściowe nie zawierają, jest odrzucane z podaniem nazwy, ponieważ Savant na tym zawodzi.
- **Znak `/` lub `\` w wartości.** Wartość podziału zawierająca ukośnik lub odwrotny ukośnik nie może być nazwą pliku ani karty, więc jest oczyszczana. Zmieniona wartość otrzymuje stały sześcioznakowy sufiks, `-` a po nim pierwsze sześć znaków skrótu MD5 wartości, umieszczony przed rozszerzeniem pliku. Wartości, które nie wymagają zmiany, zachowują swoją nazwę.

### Eksportowane wartości i kolejność wierszy

- **Zwykłe liczby i wartości logiczne.** Eksporty CSV, TSV i TXT zapisują liczby jako zwykłe liczby, a wartości logiczne jako `true` i `false`, bez `+00:00` przy znacznikach czasu.
- **Stabilna kolejność wierszy.** Miejsce docelowe, które sortuje, zapisuje jedną kolejność wierszy przy każdym uruchomieniu: remisy są rozstrzygane za każdym razem tak samo, a trasy podziału i części również sortują. Cele Parquet, Arkuszy Google, Tableau i tabel nie zachowują kolejności wierszy.

### Opcje Excela

Miejsce docelowe Excel mapuje te opcje:

- **Karta na wartość pola.** Każda wartość pola staje się arkuszem. Puste wartości trafiają do `Sheet1`, a arkusze o kolidujących nazwach otrzymują sufiks liczbowy.
- **Format z szablonu.** Każde uruchomienie najpierw kopiuje `<name>_template.xlsx` z tego samego folderu na skoroszyt, a następnie zapisuje w nim dane, więc skoroszyt jest zawsze zastępowany. Jeśli szablonu nie ma, kopiowanie ostrzega, a skoroszyt jest zapisywany bez niego.
- **Komórka w lewym górnym rogu.** Wiersze są zapisywane w skoroszycie, zaczynając od tej komórki.
- **Tryb `create`.** Każde uruchomienie zapisuje plik zgodnie z trybem zapisu miejsca docelowego.

## Wiązanie żądań API

Agent API, którego adres URL jest względny, na przykład `/v2/customers`, nie ma hosta, do którego mógłby wysyłać żądania. Powiąż go za pomocą `api_bindings`. Kluczem jest identyfikator lub nazwa węzła API albo `*` dla każdego węzła API bez własnego powiązania. Wartością jest jedno z:

- Bazowy adres URL, jako ciąg lub `{"base_url": "https://host/path"}`. Względny adres URL jest z nim łączony. Adres URL musi mieć schemat `http` lub `https` z publicznym hostem i nie może zawierać użytkownika, zapytania ani fragmentu.
- `{"connection": "<REST connection id>"}`. Żądanie trafia do hosta tego [połączenia REST](/pl/reference/connectors/rest/generic-rest/) i zawiera jego poświadczenia. Potrzebujesz uprawnienia do zapisu w połączeniu, a połączenie musi być połączeniem REST, które widzisz.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

Niedopasowany klucz jest ostrzeżeniem, a powiązanie, którego nie możesz użyć, jest odrzucane. Względny adres URL bez powiązania pozostaje nazwanym krokiem zastępczym.

Jeśli asystent AI (MCP) nie ma uprawnienia do zapisu w połączeniu, powiązanie z połączeniem jest ignorowane z ostrzeżeniem, a względny adres URL, który zostałby połączony, pozostaje krokiem zastępczym. Powiąż bazowy adres URL albo konwertuj z aplikacji Analyze lub przez REST API.

Host, port lub ścieżka pochodzące z pola wejściowego nie wymagają powiązania. Są uzupełniane dla każdego wiersza, a każda wartość jest sprawdzana w momencie użycia, a raport wymienia hosty, które wiersz może wskazać. Żądanie zawierające poświadczenie nie może pobierać hosta z pola wiersza: wysłanie poświadczenia do hosta wybranego przez dane jest odrzucane.

Stronicowanie również jest konwertowane. Adres URL następnej strony w odpowiedzi, nagłówek `Link`, przesunięcie i numer strony stają się trybem stronicowania w kroku [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/), który odczytuje każdą stronę. Wartość stronicowania może pochodzić z pola wejściowego (`{{Field}}`) lub parametru (`{{Param}}`), a wartość zapisana jako tekst liczbowy, taki jak `10.0`, jest odczytywana jako liczba.

## Kroki API z poświadczeniami

Poświadczenie w nagłówkach, ścieżce adresu URL, zapytaniu lub treści agenta API trafia do połączenia REST PlaidCloud, które tworzy import. Krok Żądanie REST odwołuje się do tego połączenia, więc poświadczenie nigdy nie znajduje się w kroku.

- Odpowiedź wymienia połączenia, które import utworzył lub ponownie wykorzystał, w polu `connections`, a raport z importu je nazywa. Ponowny import tej samej analizy wykorzystuje to samo połączenie zamiast tworzyć kolejne.
- Poświadczenia w informacjach o użytkowniku w adresie URL oraz w nagłówkach trafiają do własnych pól uwierzytelniania połączenia lub jego domyślnych nagłówków. Sekrety w ścieżce, zapytaniu i treści są przechowywane w połączeniu w postaci zaszyfrowanej i uzupełniane w czasie wykonania, tylko dla żądań do własnego hosta `https` tego połączenia.
- Niezaszyfrowany punkt końcowy `http://` nie jest konwertowany z poświadczeniami. Poświadczenie jest pomijane, a raport z konwersji ostrzega, że nie zostało skopiowane.
- Import przez asystenta AI (MCP) nie tworzy połączeń. Poświadczenia są pomijane, a ostrzeżenie o tym informuje. Zamiast tego zaimportuj z aplikacji Analyze lub przez REST API albo dodaj poświadczenie do połączenia REST ręcznie i wybierz je w kroku.
- Użytkownik bez uprawnienia do zapisu w połączeniu otrzymuje ten sam wynik: poświadczenia są pomijane i pojawia się ostrzeżenie.
- Tylko miejsce na poświadczenie API przenosi parametr do połączenia. Parametr potoku użyty w nagłówku, zapytaniu, ścieżce lub treści w miejscu, gdzie trafia poświadczenie API, trafia do zaszyfrowanych `secret_values` połączenia, a krok odwołuje się do niego przez połączenie. Nigdy nie jest tworzony jako zmienna przepływu pracy, niezależnie od nazwy parametru.
- Każdy inny parametr, którego nazwa zawiera słowo wskazujące na sekret (takie jak `password`, `token`, `secret` lub `key`, przy czym `key` jest pomijane po słowie danych, takim jak `sort` lub `partition`), staje się zmienną przepływu pracy z pustą wartością i ostrzeżeniem. Nazwa taka jak `api_key_2` również jest czyszczona. Ustaw wartość w zmiennej projektu po imporcie.
- Parametr nazwany od liczby lub limitu, taki jak `max_tokens`, zachowuje swoją wartość.
- Sekret wpisany w formule, filtrze lub wartości zamiany jest pomijany w kroku, a raport z konwersji ostrzega. Ścieżka, adres URL oraz 40- lub 64-znakowy skrót szesnastkowy są zachowywane, chyba że ich część lub nazwa sekretu wskazuje inaczej. Linki do udostępniania folderów i adresy e-mail adresatów nigdy nie pojawiają się w ostrzeżeniach ani uwagach.
- Odpowiedź, która odsyła poświadczenie z powrotem, jest przechowywana tak, jak została odebrana. Traktuj tabelę wyjściową takiego żądania jako wrażliwą.

## JWT_ENCODE

`JWT_ENCODE` jest konwertowane na krok [JWT Encode](/pl/reference/workflow-steps/tables/table-jwt-encode/). Dosłowny klucz podpisu trafia do dedykowanego połączenia powiązanego z krokiem, a token jest podpisywany w czasie wykonania, więc klucz nigdy nie pojawia się w konfiguracji kroku. Przez asystenta AI lub bez uprawnienia do zapisu w połączeniu klucz jest pomijany, token ma wartość NULL, a ostrzeżenie informuje, że należy zaimportować ponownie z uprawnieniem do tworzenia połączeń.

## Awansowanie wiersza danych na nagłówki kolumn

Agent Format ustawiony na **replace names with row** jest konwertowany na krok [Promote Header](/pl/reference/workflow-steps/tables/table-promote-header/). W czasie wykonania wybrany wiersz, liczony od 1, staje się nazwami kolumn i jest usuwany. Źródło, które nie niesie kolejności rekordów, otrzymuje uwagę, ponieważ to, który wiersz nazywa kolumny, może zmieniać się między uruchomieniami. Kolumna, którą ten wiersz nazywa, ale której nie wymienia żaden późniejszy krok, nie jest przenoszona dalej za krok, który wymienia kolumny, jakie odczytuje.

## Pliki bez zadeklarowanych kolumn

Źródło bez zadeklarowanych kolumn zachowuje te kolumny:

- Źródło CSV, TSV lub TXT powiązane podczas importu zachowuje każdą kolumnę z nagłówka pliku.
- Każdy inny typ pliku i każde niepowiązane źródło zachowuje tylko kolumny wymienione w późniejszych krokach, a raport z konwersji ostrzega.
- Awansowany nagłówek nad takim źródłem odczytuje każdą kolumnę z plików CSV, Excel, XLS, JSON, Parquet i Avro.

Gdy takie źródło zasila wyłącznie awansowany nagłówek, import jest krokiem [Import Delimited](/pl/reference/workflow-steps/import/import-delimited/), który odczytuje każdą kolumnę według pozycji. Krok, który eksportuje lub łączy dane po awansowanym nagłówku, przenosi każdą kolumnę, jaką tabela ma w czasie wykonania (zobacz **Also carry columns named at run time** w [Table Extract](/pl/reference/workflow-steps/tables/table-extract/)).

## Zachowania warte znajomości

Te konwersje zachowują się w następujący sposób.

| Agent | Zachowanie |
| --- | --- |
| Blend (`blend`) | Łączy według predykatów połączonych OR, contains i is-part-of. Blendy typu outer-excluding-inner oraz niedopasowane wyjścia są konwertowane na odpowiednie strumienie złączeń. Dla każdego operatora zduplikowany klucz po prawej stronie jest usuwany z wyniku. |
| Dedupe (`deduplicate`) | Zachowuje pierwszy rekord dla każdego klucza w obrębie każdej grupy **Grupuj według**. Flaga duplikatów oznacza każdego członka grupy duplikatów, a duplikaty mogą też trafiać do drugiego strumienia. Przy podłączonym jednym wyjściu zachowuje się tak jak w Savant. |
| Summarize (`summarize`) | Agregaty okienkowe dodają agregat do każdego wiersza zamiast zwijać grupy. |
| Sample (`sample`) | Pierwszych N wierszy, dla grupy lub ogółem, losowy procent lub liczba wierszy albo jeden wiersz na każdy N-ty. |
| Time Series (`rollup`) | Okresy dzień, tydzień, miesiąc, kwartał, rok i dekada między opcjonalnymi datami początkowymi i końcowymi, dla każdej grupy. Okresy miesięczne są oznaczane `YYYY-MM`, a okresy bez rekordów pojawiają się z zerami. Rekordy z wartością NULL w dacie są wykluczane. |
| Pivot (`pivot`) | COUNT zlicza wiersze. |
| XML (`xml`) | SELECT wyodrębnia elementy, ścieżki mogą zawierać przestrzenie nazw, a TO_JSON konwertuje XML na JSON. Każda ścieżka XPath 1.0 jest konwertowana, w tym predykaty, testy atrybutów, symbole wieloznaczne i funkcje takie jak `count()`, `name()` i `contains()`, a krok [Analiza XML](/pl/reference/workflow-steps/tables/table-xml-parse/) odczytuje ją jako XPath. Przy wyłączonym `processNs` nazwy są dopasowywane dosłownie, łącznie z prefiksem. Plik XML, którego brakuje podczas konwersji, ma element główny ustalany w czasie uruchomienia przepływu pracy. |
| JSON (`json`) | Spłaszcza do szerokich kolumn. Tekst, który nie jest poprawnym JSON, daje NULL, a tablice są zwracane jako tekst. |
| Split (`split`) | Dzieli na kolumny lub wiersze, z liczbą kolumn odczytywaną z danych przy każdym uruchomieniu przepływu pracy. |

Te funkcje wyrażeń dają takie same wyniki jak w Savant:

| Funkcja | Zachowanie |
| --- | --- |
| `DATE_DIFF` | Tygodnie i kwartały są liczone tak jak w Savant. |
| `PAD` | Nie obcina wartości dłuższej niż docelowa szerokość. |
| `+` na tekście | Łączy tekst. Kolumna ze źródła bez zadeklarowanych typów jest odczytywana jako liczba, więc `+` dodaje, a uwaga o tym informuje. |
| Podział na wiersze | Zachowuje puste fragmenty jako wiersze. |
| `LAST` bez sortowania | Zwraca ostatni wiersz w kolejności nadejścia wierszy, z uwagą, że hurtownia danych nie gwarantuje tej kolejności. |
| `JOIN_STR` | Łączy liczbę ułamkową tak, jak zapisuje ją Savant, bez dopełnienia końcowymi zerami. |
| `JSON_FORMAT` | Formatuje JSON z wcięciami; w Snowflake zapisuje JSON w zwartej postaci w jednym wierszu. |
| `JSON_SET` | Zachowuje kolejność kluczy Savant. |
| `GREATEST` i `LEAST` | Pomijają argumenty NULL. Wynik jest NULL tylko wtedy, gdy każdy argument jest NULL. |
| `ROUNDUP` | Zaokrągla w górę do następnego pełnego kroku, więc liczba ujemna zaokrągla się w stronę zera: -1,5 daje -1. `ROUNDDOWN` pozostaje bez zmian. |
| `DURING_DAYLIGHT_SAVING` i `DURING_STANDARD` | NULL na wejściu daje NULL na wyjściu. |
| `TO_TEXT` z formatem daty | Odczytuje tokeny formatu tak jak Savant. `YYYY`, `w` i `u` to rok tygodniowy ISO, tydzień i dzień tygodnia, a litera strefy lub ery jest zapisywana tak jak dla czasu UTC. |
| `TO_TEXT` i wynik liczba-na-tekst | Zapisuje zwykłe liczby, takie jak `12`, a nie `12.0000000000`. |
| `TO_TEXT` z wzorcem liczbowym | Formatuje tak jak `DecimalFormat` w Javie, zaokrąglając do parzystej, w tym wzorce naukowe, takie jak `##0.##E0`. |
| `TO_TEXT` i parsowanie dat z formatem dla każdego wiersza | Odczytuje format z każdego wiersza. |
| Tokeny ułamków sekund, wąskich miesięcy i dat opartych na tygodniach | Są konwertowane. Tokeny tygodni są odczytywane jako tygodnie ISO. |
| Lata dwucyfrowe (`yy`, `y`) | Odczytywane w oknie 80 lat wstecz i 20 lat w przód od bieżącego roku. |
| `REGEX_MATCH` | Dopasowanie częściowe: wzorzec pasuje w dowolnym miejscu tekstu, a nie do całego tekstu. |

`TO_TEXT` i formaty dat są konwertowane w kroku [Text Function](/pl/reference/workflow-steps/tables/table-text-function/). Edycja, która zawiera tylko skompilowane kroki, bez wyrażenia, jest konwertowana jako te kroki zastosowane po kolei, każdy zasilający następny, a raport z konwersji odnotowuje przyjętą kolejność. Konwerter odrzuca z podaniem nazwy to, na czym zawodzi sam Savant lub co nie ma czego konwertować, a krok staje się krokiem zastępczym: zwykła funkcja agregująca lub okienkowa wewnątrz wyrażenia Transform lub Filter (wewnątrz obliczenia lub Summarize jest konwertowana), `HASH` z dosłownym algorytmem innym niż `md5` lub `sha1`, konstrukcja wyrażenia regularnego, której PlaidCloud nie potrafi odczytać (klasa wewnątrz klasy, część wspólna klas lub nieznana właściwość `\p{}`), edycja Transform bez wyrażenia i bez skompilowanych kroków (na przykład edycja Copilot, która ma tylko swój prompt), ścieżka XML, która nie jest XPath 1.0, oraz żądanie API zawierające poświadczenie i pobierające host z pola wiersza. [Macierz konwersji Savant](/pl/reference/savant-conversion-matrix/#nazwane-odrzucenia) wymienia każdy z tych przypadków wraz z powodem.

Funkcje wyrażeń są też konwertowane dla `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, funkcji czasu letniego (`DST`) oraz funkcji wyrażeń regularnych przyjmujących n-te dopasowanie. `DAY_OF_WEEK` numeruje niedzielę jako 7, a `DAY_NAME` zwraca nazwę dnia.

## Czytanie raportu z konwersji

Odpowiedź zawiera raport z konwersji: podsumowanie, ile kroków zostało skonwertowanych z wysoką, średnią lub niską pewnością i ile nie zostało skonwertowanych, a także ostrzeżenia i węzły wchłonięte przez inne. Przeczytaj go przed uruchomieniem przepływu pracy. Wskazuje każdy krok zastępczy, każde niepowiązane źródło i niedopasowane powiązanie oraz użyty prefiks tabel.

## Kroki zastępcze dla niekonwertowanych konfiguracji

Konfiguracja, której konwerter nie potrafi odtworzyć, jest tworzona jako krok zastępczy noszący nazwę agenta, a raport z konwersji go wskazuje. Krok zastępczy pojawia się dla konstrukcji, którą konwerter odrzuca z podaniem nazwy (zobacz [macierz konwersji Savant](/pl/reference/savant-conversion-matrix/#nazwane-odrzucenia)), lub takiej, której eksport nie opisuje w pełni, na przykład brakującej konfiguracji API. Domyślnie krok zastępczy kończy się niepowodzeniem, gdy przepływ pracy do niego dotrze, więc uruchomienie nie może zgłosić sukcesu dla pracy, która nigdy nie została wykonana.

Ustaw `allow_unconverted_placeholders` na `true`, aby zaimportować każdy krok zastępczy jako krok przekazujący dane bez zmian. Uruchomienie jest wtedy kontynuowane za nim, a wynik kroku zastępczego jest jego wejściem. Odbuduj tę funkcjonalność za pomocą natywnego kroku, gdy jej wynik ma znaczenie.

## Uruchamianie skonwertowanego przepływu pracy

1. Otwórz nowy przepływ pracy w projekcie.
2. Ustaw wszystkie zmienne projektu pochodzące z parametrów Savant.
3. Prześlij pliki dla niepowiązanych źródeł pod ścieżki podane w raporcie.
4. Uruchom przepływ pracy i przejrzyj tabelę wyjściową każdego kroku.

## Przypadki brzegowe

To jedyne znane różnice względem Savant. Raport z konwersji wskazuje każdą, która ma zastosowanie.

- **Formaty dat.** `TO_DATE` lub `TO_DATETIME` z formatem zawierającym literał `[`, `]`, `'`, `\` lub `^`, na tekście, który odczytuje do 9999-12-30 lub 9999-12-31, wychodzi poza ostatni znacznik czasu obsługiwany przez hurtownię danych, a raport ostrzega.
- **Parametry z sekretami.** Parametr, którego nazwa zawiera słowo wskazujące na sekret lub którego wartość wygląda jak poświadczenie, staje się zmienną projektu z pustą wartością, z założenia. Ustaw wartość w zmiennej.
- **Niezadeklarowane parametry.** Parametr używany przez węzeł, którego eksport nie deklaruje, trafia jako zmienna projektu z pustą wartością.
- **`JSON_FORMAT` w Snowflake.** Zapisuje zwarty JSON w jednym wierszu.
- **Kolejność wierszy.** Posortowane cele Parquet, Arkuszy Google, Tableau i tabel nie zachowują kolejności wierszy.
- **Arkusze Google i Tableau.** Publikowanie w jednym z nich wymaga powiązania jego konta przez `destination_bindings`.

## Powiązane przewodniki

- [Macierz konwersji Savant](/pl/reference/savant-conversion-matrix/)
- [Połączenie REST](/pl/reference/connectors/rest/generic-rest/)
- [Dodawanie kont dokumentów](/pl/guides/documents/adding-accounts/)
- [Zarządzanie zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/)
- [Krok AI/NLP](/pl/reference/workflow-steps/text-documents/nlp-ai/)
- [Krok Żądanie REST](/pl/guides/workflows/rest-request-step/)
- [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/)
