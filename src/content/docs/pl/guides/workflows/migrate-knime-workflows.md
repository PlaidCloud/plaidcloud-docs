---
title: Migracja przepływów pracy KNIME
description: Przekonwertuj przepływ pracy KNIME (.knwf) lub grupę przepływów pracy (.knar) na zaawansowane przepływy pracy PlaidCloud z aplikacji Analyze, interfejsu REST API lub agenta AI połączonego przez MCP, powiąż jego wejścia i połączenia oraz przeczytaj raport z konwersji.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloud jest pełnoprawnym zamiennikiem KNIME. 98,5% konfiguracji węzłów KNIME konwertuje się w pełni, a 205 z 207 podstawowych typów węzłów ma status Full: każdy z nich staje się standardowymi krokami przepływu pracy PlaidCloud, które wykonują pracę węzła. Konwerter zamienia archiwum przepływu pracy KNIME na uruchamialne zaawansowane przepływy pracy, zachowuje oryginalny graf i zwraca raport z konwersji wskazujący wszystko, co trzeba ustawić. [Macierz konwersji KNIME](/pl/reference/knime-conversion-matrix/) zawiera listę wszystkich węzłów.

Konwersja odczytuje wyłącznie archiwum, na które wskazujesz. Nigdy nie łączy się z systemem, z którego węzeł KNIME odczytuje dane lub do którego je zapisuje.

Konwersja to czynność jednorazowa. Ponowna konwersja tego samego archiwum tworzy nowe przepływy pracy, a zmiany wprowadzone w PlaidCloud nigdy nie są scalane z późniejszym eksportem.

## Co tworzy PlaidCloud

- Jeden zaawansowany przepływ pracy dla każdego przepływu pracy KNIME. Plik `.knwf` daje jeden przepływ pracy, a plik `.knar` daje po jednym dla każdego przepływu pracy w grupie.
- Każdy węzeł KNIME staje się odpowiednim krokiem przepływu pracy, zmienną projektu lub obiektem na kanwie, z zachowaniem zależności między elementami poprzedzającymi i następującymi. Metawęzły i komponenty są spłaszczane do przepływu pracy, więc ich węzły działają jako zwykłe kroki.
- Zmienne przepływu oraz węzły Configuration i Widget stają się zmiennymi projektu z wartościami domyślnymi. Przełączniki i pętle, których wartości są znane w chwili konwersji, są przycinane i rozwijane do kroków, które uruchamiają.
- Języki wyrażeń KNIME — Expression, String Manipulation, Math Formula, Column Expressions i Rule Engine — konwertują się na wyrażenia PlaidCloud.
- Pliki danych dostarczone w archiwum są przesyłane do folderu `knime/` w domyślnym koncie dokumentów projektu, po jednym folderze na przepływ pracy, a skonwertowane czytniki importują je stamtąd.
- Widoki, wykresy i menedżery kolorów nie wpływają na dane. Są pomijane i wymienione w raporcie z konwersji.

## Zanim zaczniesz

1. Wyeksportuj przepływ pracy z KNIME Analytics Platform jako plik `.knwf`. Aby skonwertować kilka przepływów pracy naraz, wyeksportuj ich grupę jako plik `.knar`. Pliki używane przez czytniki trzymaj w folderze `data` przepływu pracy, aby były dostarczone w archiwum.
2. Prześlij archiwum na [konto dokumentów](/pl/guides/documents/adding-accounts/), które możesz odczytać. W aplikacji Analyze przycisk **Przeglądaj** w oknie importu przesyła je z Twojego komputera.
3. Wybierz projekt PlaidCloud, który ma otrzymać przepływy pracy. Musisz być Architektem lub Menedżerem projektu, a projekt musi mieć domyślne konto dokumentów.
4. Zanotuj tabele, pliki i połączenia PlaidCloud, których mają używać czytniki i węzły łączników przepływu pracy. Zobacz [Powiązywanie źródeł](#powiązywanie-źródeł).

## Konwersja przepływu pracy

Konwertuj z aplikacji Analyze, interfejsu REST API lub agenta AI połączonego przez MCP. Interfejs REST API i narzędzie MCP przyjmują te same pola; okno przyjmuje te, które wyświetla.

### Aplikacja Analyze

1. Otwórz **Analyze** i wybierz **Tools → Importuj przepływ pracy KNIME**.
2. W sekcji **Importuj źródło i cel** wybierz **Projekt docelowy** oraz **Archiwum KNIME (.knwf lub .knar)** na koncie dokumentów. Wybierz **Przeglądaj**, aby przesłać archiwum ze swojego komputera.
3. W sekcji **Prefiksy obiektów** opcjonalnie ustaw **Prefiks przepływu pracy**, **Prefiks kroku** i **Prefiks tabeli**. Prefiks tabeli domyślnie przyjmuje nazwę przepływu pracy.
4. W sekcji **Powiązania źródeł (opcjonalne)** opcjonalnie powiąż czytnik z istniejącą tabelą w projekcie docelowym: wybierz **Dodaj**, a następnie wprowadź **Czytnik KNIME** (jego identyfikator węzła, taki jak `12:3`, nazwę węzła lub nazwę pliku) i **ID tabeli**. Aby powiązać połączenia, dokumenty lub tabele w innych projektach, użyj interfejsu REST API lub narzędzia MCP. Zobacz [Powiązywanie źródeł](#powiązywanie-źródeł).
5. Wybierz **Importuj**.

Okno pokazuje postęp konwersji archiwum, a następnie raport z konwersji: liczby kroków (**Kroki**, **Wysoka pewność**, **Średnia**, **Niska** i **Nieprzekonwertowane**), węzły, których nie udało się skonwertować, oraz kroki znajdujące się za nimi, konwersje częściowe, ostrzeżenia, pliki źródłowe do przesłania i węzły bez kroku. Jeśli konwersja nie ma niczego do przejrzenia, okno informuje o tym i zamyka się samo.

### Pola

| Pole | Wymagane | Działanie |
| --- | --- | --- |
| `source_account_id` | Tak | Konto dokumentów zawierające archiwum KNIME. |
| `source_file_path` | Tak | Ścieżka pliku `.knwf` lub `.knar` na tym koncie. |
| `project_id` | Tak | Projekt, w którym tworzone są przepływy pracy. |
| `workflow_prefix` | Nie | Prefiks dodawany do nazw przepływów pracy. |
| `step_prefix` | Nie | Prefiks dodawany do nazw kroków. |
| `table_prefix` | Nie | Prefiks dodawany do nazw tabel. Domyślnie nazwa samego przepływu pracy. Prefiks, który użyłby ponownie istniejącej nazwy tabeli, jest odrzucany, zanim cokolwiek zostanie utworzone. W przypadku pliku `.knar` po prefiksie każdego przepływu pracy następuje nazwa tego przepływu pracy. |
| `source_bindings` | Nie | Wiąże czytniki i węzły łączników z danymi i połączeniami, które już masz; do 500 wpisów. Zobacz [Powiązywanie źródeł](#powiązywanie-źródeł). |

### REST

Wyślij pola jako treść JSON na adres:

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

Agent AI połączony przez MCP wywołuje narzędzie `knime_convert` z tymi samymi polami. Aby połączyć agenta, zobacz [Agenci AI (MCP)](/pl/integrations/ai-coding-agents/). Narzędzie zmienia Twój projekt, więc przejrzyj wywołanie, zanim je zatwierdzisz.

## Powiązywanie źródeł

Użyj `source_bindings`, aby wskazać czytnikowi KNIME dane, które już istnieją w PlaidCloud, zamiast kopii z archiwum. Kluczem jest identyfikator węzła (na przykład `12:3`), nazwa węzła, ścieżka dołączonego pliku (na przykład `data/sales.csv`) lub nazwa pliku; wygrywa pierwsze dopasowanie w tej kolejności. Wartością jest jedno z poniższych:

- Identyfikator `analyzetable_` tabeli w projekcie docelowym. Tabela zastępuje czytnik.
- `{"project": "<project id>", "table": "<table id>"}` dla tabeli w innym projekcie, który możesz odczytać. Czytnik staje się krokiem [Import Project Table](/pl/reference/workflow-steps/import/import-project-table/) (krok), który ją kopiuje. Projekt źródłowy musi udostępniać projektowi docelowemu uprawnienie Read, w przeciwnym razie krok wyświetla ostrzeżenie. Tabela objęta dostępem do wierszy jest odrzucana.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` dla dokumentu, który możesz odczytać. Czytnik go importuje.
- `{"connection": "<connection id>"}` dla węzła łącznika bazy danych lub REST. Skonwertowane kroki działają na tym połączeniu.

Okno aplikacji Analyze wiąże czytniki z tabelami w projekcie docelowym według identyfikatora tabeli. Połączenia, dokumenty i tabele w innych projektach wiąż za pomocą interfejsu REST API lub narzędzia MCP.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

Powiązana tabela, która nie istnieje, lub klucz, który nie pasuje do żadnego czytnika, to ostrzeżenie. Zastosowane powiązania wraz z nazwami ich projektów i tabel są wymienione w raporcie z konwersji w sekcji `bindings`.

### Niepowiązane wejścia

Czytnik, którego pliku nie ma w archiwum, odczytuje z `inputs/<file name>` w folderze przepływu pracy domyślnego konta dokumentów, a raport z konwersji wymienia tę ścieżkę w `missing_inputs` wraz z ostrzeżeniem. Prześlij plik w to miejsce i uruchom przepływ pracy. Dopóki pliku tam nie ma, import kończy się ostrzeżeniem i tworzy pustą tabelę, a przepływ pracy działa dalej.

## Poświadczenia i połączenia

Poświadczenia KNIME nigdy nie są migrowane. Każdy krok, który loguje się do innego systemu, odczytuje swoje poświadczenia z połączenia PlaidCloud lub ze zmiennej projektu, którą ustawisz, a ostrzeżenie kroku w raporcie z konwersji wskazuje, z której.

| KNIME | Co ustawiasz |
| --- | --- |
| Łączniki baz danych | Połączenie z bazą danych: powiąż je za pomocą `{"connection": "<id>"}` lub wybierz je w kroku. |
| Węzły REST i usług sieciowych, które się logują | [Połączenie REST](/pl/reference/connectors/rest/generic-rest/): powiąż je za pomocą `{"connection": "<id>"}` lub wybierz je w kroku. |
| Speech Recognizer (IBM Watson) | Połączenie REST, którego bazowy adres URL to adres URL usługi Watson wskazany w ostrzeżeniu, z użytkownikiem `apikey` i Twoim kluczem API jako logowaniem Basic. Powiąż je z węzłem. |
| Email Connector, z Email Reader lub Email Mover | Zmienna projektu zawierająca hasło serwera poczty, o nazwie podanej w ostrzeżeniu. Host i użytkownik pochodzą z Email Connector. |
| Excel Reader lub Excel Writer z hasłem skoroszytu | Zmienna projektu zawierająca hasło, o nazwie podanej w ostrzeżeniu. |
| Łączniki i uwierzytelniacze LLM | Połączenie LLM w kroku AI. |

Aby ustawić zmienne projektu, zobacz [Zarządzanie zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/).

## Czytanie raportu z konwersji

Okno aplikacji Analyze pokazuje raport z konwersji po zakończeniu importu, a odpowiedzi REST i MCP go zawierają. Przeczytaj go, zanim uruchomisz przepływy pracy.

- `summary` podaje liczbę utworzonych kroków oraz to, ile z nich zmapowano z wysoką, średnią lub niską pewnością.
- `warnings` wymienia każde ostrzeżenie wraz z jego węzłem, krokiem i działaniem do wykonania, w tym każde poświadczenie lub połączenie do ustawienia.
- `missing_inputs` wymienia ścieżki w dokumentach, do których należy przesłać pliki dla niepowiązanych wejść.
- `bindings` wymienia zastosowane powiązania.
- `table_prefix` to użyty prefiks. W przypadku pliku `.knar` pole `workflows` wymienia każdy przepływ pracy z jego własnym prefiksem.
- `uploaded_files`, obok raportu, wymienia dołączone pliki przesłane do domyślnego konta dokumentów.
- `dropped_tools` wymienia widoki i wykresy, które zostały pominięte.

## Symbole zastępcze

Węzeł bez ścieżki konwersji pozostaje na kanwie jako nazwany symbol zastępczy. Symbol zastępczy przekazuje dane dalej i ostrzega nazwą węzła KNIME, a każdy krok za nim jest oznaczony w raporcie, więc brakujący wynik nigdy nie pozostaje niezauważony. Gdy wynik ma znaczenie, odbuduj tę funkcję za pomocą standardowego kroku.

## Uruchamianie skonwertowanego przepływu pracy

1. Otwórz nowy przepływ pracy w projekcie.
2. Ustaw zmienne projektu i połączenia wskazane w ostrzeżeniach.
3. Prześlij pliki dla niepowiązanych wejść do ścieżek podanych w sekcji **Pliki źródłowe do przesłania** w oknie lub w `missing_inputs`.
4. [Uruchom przepływ pracy](/pl/guides/workflows/run-a-workflow/) i przejrzyj tabelę wyjściową każdego kroku.

## Przypadki brzegowe

To jedyne znane różnice w stosunku do KNIME.

- **Crosstab.** Konwertuje się na [Table: Pivot](/pl/reference/workflow-steps/tables/table-pivot/) (krok). Kilka kombinacji ustawień daje wyniki różniące się od KNIME.
- **Loop End (Column Append).** Konwertuje się na [Tabela: złączenie wewnętrzne](/pl/reference/workflow-steps/tables/table-inner-join/). Kilka kombinacji ustawień daje wyniki różniące się od KNIME.
- **Losowania.** Row Sampler, Table Partitioner i Equal Size Sampling wykonują własne losowanie KNIME za pomocą [Table: KNIME Random Sample](/pl/reference/workflow-steps/tables/table-knime-random-sample/) (krok), więc węzeł z ziarnem wybiera te same wiersze co w KNIME. Losowanie przyjmuje tabelę liczącą co najwyżej 10 000 000 wierszy; większa tabela powoduje niepowodzenie kroku.

## Powiązane przewodniki

- [Macierz konwersji KNIME](/pl/reference/knime-conversion-matrix/)
- [Połączenie REST](/pl/reference/connectors/rest/generic-rest/)
- [Dodawanie kont dokumentów](/pl/guides/documents/adding-accounts/)
- [Zarządzanie zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/)
- [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/)
