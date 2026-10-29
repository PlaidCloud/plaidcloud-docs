---
title: Macierz konwersji Alteryx
description: Jak PlaidCloud konwertuje narzędzia Alteryx na natywne kroki zaawansowanego przepływu pracy, makra, zmienne i zarządzanych wykonawców — ze statusem obsługi dla każdego narzędzia.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloud konwertuje przepływy pracy, aplikacje i makra Alteryx na natywne zaawansowane
przepływy pracy. Importer mapuje każde narzędzie Alteryx na krok przepływu pracy, konstrukcję
makra, kontrolowaną zmienną, operację na plikach opartą na dokumentach lub zarządzanego wykonawcę
zadań — dzięki temu skonwertowany przepływ pracy działa natywnie w chmurze, a nie jako emulacja.

**Niemal każde standardowe narzędzie Alteryx konwertuje się w pełni.** Poniższy status obsługi
dotyczy poszczególnych narzędzi:

- **Pełny** — konwertuje się na natywny krok, makro, zmienną, artefakt lub
  zarządzanego wykonawcę PlaidCloud i realizuje funkcję narzędzia. Większość narzędzi należy do tej grupy.
- **Częściowy** — konwertuje się i działa w typowym zastosowaniu, ale jeden odrębny
  *tryb możliwości* narzędzia nie jest jeszcze odtwarzany. Zdarza się rzadko.
- **Nieobsługiwany** — brak konwersji; możliwość jest odtwarzana natywnie od podstaw.

Złącza systemów zewnętrznych (Salesforce, HTTP, Google Analytics, Cassandra,
e-mail, Hadoop, Spark i podobne) są **podłączane, a nie konwertowane** — zobacz
[Łączenie z systemami zewnętrznymi](#łączenie-z-systemami-zewnętrznymi).

## Obsługa narzędzi

| Narzędzie Alteryx | Status | Odpowiednik w PlaidCloud | Co jest konwertowane |
| --- | --- | --- | --- |
| Action | Pełny | Powiązanie ze zmienną i warunkowa konfiguracja kroku | Aktualizuje ustawienia kroków niższego rzędu na podstawie danych wejściowych skonwertowanej aplikacji. |
| Interfejs aplikacji analitycznej (`.yxwz`) | Częściowy | Opublikowany front-end „App Runner" aplikacji Panel | Układ `<Questions>` aplikacji jest materializowany w działającą aplikację Panel, która zbiera dane wejściowe od użytkownika i steruje skonwertowanym przepływem pracy; jest publikowana automatycznie w ramach konwersji (aplikacja bez widżetów wejściowych jest pomijana). Typowe typy pytań — tekst, liczba (Numeric Up Down), data, pole wyboru, przycisk opcji, lista rozwijana, pole listy, drzewo, wybór pliku i wybór folderu — stają się widżetami App Runner. Pytanie, którego wartość nie jest powiązana z żadną zmienną przepływu pracy, jest renderowane z widoczną uwagą, zamiast po cichu zbierać nieużywaną wartość, a rzadsze typy pytań są oznaczane do przeglądu zamiast być materializowane. Zobacz [Korzystanie ze skonwertowanych aplikacji Alteryx](/pl/guides/workflows/use-converted-alteryx-apps/#interfejs-app-runner). |
| Append Fields | Pełny | Transformacja dołączania pól | Dołącza pola z jednego strumienia do drugiego. |
| Auto Field | Pełny | Transformacja automatycznego dobierania rozmiaru pól | Zachowuje wywnioskowane rozmiary pól. |
| AutoML | Pełny | [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/) | Łączy wybór metody modelu, zmiennej docelowej i kandydujących algorytmów w jeden krok ML: trenuj model, tak samo jak Classification i Regression. AutoML nigdy nie zapisuje, który algorytm kandydujący faktycznie wygrał w czasie uruchomienia w Alteryx, więc konwersja wybiera pierwszy zaznaczony algorytm obsługiwany przez ML: trenuj model i odnotowuje ten wybór. Porównaj skonwertowany krok AutoML z własnymi wynikami z Alteryx. |
| Barcode | Pełny | Wykonawca kodów kreskowych | Odczytuje lub zapisuje kody kreskowe w skonfigurowanej symbolice. |
| Batch Macro | Częściowy | Makro rozgałęzione po tabeli kotwicy sterującej | Wywołujący uruchamia całe makro raz dla każdego rekordu swojego wejścia sterującego, wiążąc parametry sterujące wnętrza w każdym przebiegu — w tym parametr sterujący, który wywołujący przemianował na etykietę wyświetlaną, gdy w grze jest dokładnie jeden, oraz akcję `UpdateRawXml`, która przepisuje listę pól kroku Select na podstawie zmiennej. Konstrukcje, dla których wartości na przebieg nie da się bezpiecznie odtworzyć, kończą się bezpiecznym odrzuceniem z podaniem nazwy, zamiast konwertować się błędnie: `UpdateRawXml`, który przepisuje cokolwiek poza listą pól kroku Select, oraz akcja, która zastępuje całe wyrażenie kroku Filter zmienną (jej surowa składnia na przebieg byłaby błędnie obliczana). |
| Browse | Pełny | Browse / przekazanie | Zachowane do inspekcji bez kosztu w czasie działania. |
| Buffer | Pełny | [Spatial Buffer](/pl/reference/workflow-steps/spatial/spatial-buffer/) | Powiększa każdą geometrię o stałą odległość. |
| Build Features | Częściowy | [Build Features](/pl/reference/workflow-steps/tables/table-build-features/) | Konwertuje prymitywy arytmetyczne i interakcji, wyodrębnianie części daty, podział na przedziały według jawnych progów, skalowanie z-score i min-max oraz kodowanie one-hot. Agregacja między tabelami (Deep Feature Synthesis przez kartę Manage Relationships), PCA, kodowanie docelowe i automatyczny podział na przedziały oparty na danych nie mają odpowiedników — każdy z nich jest oznaczony z nazwy w raporcie konwersji, zamiast być po cichu pomijany. |
| Calgary Cross Count | Pełny | Agregat [bazy danych Calgary](/pl/guides/workflows/migrate-alteryx-workflows/#bazy-danych-calgary) | Grupuje indeksowane pola i zlicza nazwane wartości każdego pola niestandardowego. |
| Calgary Cross Count Append | Pełny | [Calgary Cross Count Append](/pl/guides/workflows/migrate-alteryx-workflows/#calgary-join-i-cross-count-append) | Dopasowuje każdy rekord wejściowy do indeksu wartości, a następnie zlicza, ile rekordów bazy danych zostało dopasowanych. |
| Calgary Input | Pełny | Wejście [bazy danych Calgary](/pl/guides/workflows/migrate-alteryx-workflows/#bazy-danych-calgary) | Odczytuje bazę danych z zapisanym zapytaniem zastosowanym jako filtr. |
| Calgary Join | Pełny | [Calgary Join](/pl/guides/workflows/migrate-alteryx-workflows/#calgary-join-i-cross-count-append) | Dopasowuje każdy rekord do indeksu wartości w bazie danych, zachowując dopasowane rekordy. |
| Calgary Loader | Pełny | Zapis do [bazy danych Calgary](/pl/guides/workflows/migrate-alteryx-workflows/#bazy-danych-calgary) | Zapisuje tabelę zastępczą, z którą wiążą się wszystkie moduły odczytu Calgary. |
| Centroid | Pełny | Operacja wykonawcy Centroid | Redukuje każdą geometrię do jej punktu środkowego, dołączonego jako kolumna `Centroid`. |
| Check Box | Pełny | Kontrolowana zmienna przepływu pracy | Konwertuje wybory w polach wyboru aplikacji na kontrolowane dane wejściowe. |
| Classification | Pełny | [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/) | Łączy łańcuch Assisted Modeling w jeden krok ML: trenuj model z jego algorytmem, zmienną docelową, cechami i hiperparametrami. |
| Comment / Annotation / Link | Pełny | Adnotacja na kanwie | Zachowane jako kontekst przepływu pracy. |
| Condition | Pełny | Warunek kroku | Wyzwala ostrzeżenia, błędy lub gałęzie na podstawie wyrażenia. |
| Control Parameter | Pełny | Parametr sterujący makra | Mapowany na parametry makr PlaidCloud. |
| Convex Hull | Pełny | Operacja wykonawcy Convex Hull | Buduje najmniejszy wypukły wielokąt obejmujący każdą geometrię, dołączony jako kolumna `ConvexHull`. |
| Create Points | Pełny | [Table Extract](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) z `geom_point` | Buduje geometrię punktową z kolumn długości i szerokości geograficznej, w SQL. |
| Create Samples | Pełny | Table Extract, po jednym na każde wyjście | Dzieli dane wejściowe na zbiory Estimation, Validation i Holdout w skonfigurowanych proporcjach procentowych. |
| Cross Tab | Pełny | Transformacja przestawna / tabeli krzyżowej | Przestawia wiersze na kolumny dla każdej metody agregacji i wyprowadzonych sum. |
| Data Cleansing | Pełny | Transformacja czyszczenia danych | Czyści białe znaki, wartości puste, interpunkcję i wielkość liter. |
| Date | Pełny | Zmienna przepływu pracy (data) | Emituje wartości dat ISO dla kroków i warunków. |
| DateTime | Pełny | Transformacja daty/godziny | Konwertuje analizę i formatowanie daty i godziny. |
| Detour | Pełny | Warunkowe kierowanie gałęzi | Konwertuje wybór trasy na warunki DAG. |
| Detour End | Pełny | Warunkowe scalanie gałęzi | Ponownie łączy warunkowo wybrane gałęzie. |
| Directory | Pełny | Lista katalogu dokumentów | Wyświetla pliki ze ścieżki dokumentu. |
| Distance | Pełny | [Table Extract](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) z `ST_DISTANCE_SPHERE` | Odległość geodezyjna i azymut między punktami, w SQL. |
| Download | Pełny | Krok [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) względem połączenia REST | Pobiera dane zewnętrzne lub artefakty; przypisz połączenie REST do skonwertowanego kroku przed jego uruchomieniem. |
| Drop Down | Pełny | Kontrolowana zmienna przepływu pracy | Konwertuje wybory z listy rozwijanej aplikacji na kontrolowane dane wejściowe. |
| Dynamic Input | Częściowy | Dynamiczne wejście dokumentu | Rozwiązuje wzorce plików i wejścia sterowane zmiennymi w czasie uruchomienia. *ReadList* programu Excel — jeden arkusz odczytywany z każdego skoroszytu wymienionego przez narzędzie Directory, a następnie łączony w unię — konwertuje się na odczyt arkusza z użyciem wzorca folderu, gdy poprzedzający Filter przypina arkusz do jednej nazwy przez dokładne dopasowanie. Arkusz wybrany przez Contains, nierówność lub filtr OR albo odczyt obejmujący więcej niż jeden arkusz kończy się odrzuceniem, zamiast odczytać zły arkusz. |
| Dynamic Rename | Pełny | Transformacja dynamicznej zmiany nazw | Zmienia nazwy pól na podstawie metadanych lub reguł. |
| Dynamic Replace | Pełny | Transformacja dynamicznej zamiany | Stosuje reguły zamiany z drugiego strumienia. |
| Dynamic Select | Pełny | Transformacja dynamicznego wyboru pól | Wybiera pola według typu, nazwy lub reguły. |
| Error | Pełny | Warunek kroku (błąd) | Konwertuje skonfigurowane zachowanie błędu na warunki kroku. |
| Feature Types | Pełny | Konfiguracja cech [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/) | Przenosi rolę modelową przypisaną każdemu polu do połączonego kroku ML: trenuj model. |
| File Browse | Pełny | Kontrolowana zmienna pliku dokumentu | Pozwala użytkownikom wybrać plik do uruchomienia skonwertowanej aplikacji. |
| Filter | Pełny | Transformacja filtrująca | Dzieli rekordy według wyrażenia na ścieżki prawdy i fałszu. |
| Fit | Pełny | [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/) | Zwija się w połączony krok ML: trenuj model. |
| Folder Browse | Pełny | Kontrolowana zmienna folderu dokumentu | Pozwala użytkownikom wybrać folder do uruchomienia skonwertowanej aplikacji. |
| Formatted Excel output into a styled template | Częściowy | Moduł zapisu Excel uwzględniający szablon ([Export to Excel Sheets](/pl/reference/workflow-steps/export/export-to-excel-sheets/) dla wielu arkuszy) | Zapis do sformatowanego szablonu zachowuje jego formatowanie — wartości, formaty liczb, czcionki, wypełnienia, obramowania, scalone komórki i szerokości kolumn są przenoszone do nazwanego arkusza i zakresu. Dotyczy to zarówno pojedynczego arkusza, jak i kilku wyjść złożonych w różnych arkuszach jednego skoroszytu, wypełnianych w jednym przebiegu, dzięki czemu arkusze już się nawzajem nie nadpisują. Jeden przypadek pozostaje częściowy: szablon zawierający tabele przestawne lub wykresy traci te obiekty podczas zapisu arkuszy. Zwykłe (niesformatowane) wyjście do Excela jest w pełni obsługiwane — zobacz Output Data. |
| Formula | Pełny | Transformacja formuły | Konwertuje wyrażenia pól na wyrażenia PlaidCloud lub SQL. |
| Fuzzy Match | Pełny | Wykonawca dopasowania rozmytego | Dopasowuje według kluczy, progów i przeglądu kandydatów. |
| Generalize | Pełny | [Spatial Generalize](/pl/reference/workflow-steps/spatial/spatial-generalize/) | Upraszcza geometrię do tolerancji, zachowując topologię. |
| HTML | Pełny | Tekst raportu / artefakt HTML | Zachowuje zawartość jako wyjście raportu lub artefaktu. |
| Image Processing | Pełny | Wykonawca transformacji obrazu | Stosuje skalę szarości, skalowanie, kadrowanie i obrót w kolejności kanwy. |
| Image Profile | Pełny | Wykonawca profilu obrazu | Raportuje wymiary, tryb, format, kanały i statystyki luminancji. |
| Image to Text | Pełny | Wykonawca OCR | Wyodrębnia tekst z obrazów za pomocą zarządzanego OCR. |
| Input Data | Pełny | Wejście plikowe oparte na dokumentach | Wczytuje pliki źródłowe `.yxdb`, `.dbf`, Excel i `.flat` o stałej szerokości do danych przepływu pracy. |
| Insights | Pełny | Wyjście pulpitu / artefaktu | Tworzy natywny w chmurze artefakt przeglądu. |
| Interactive Chart | Pełny | Artefakt wykresu | Tworzy artefakt wykresu ze skonwertowanych danych. |
| Join | Pełny | Transformacja złączenia | Tworzy strumienie złączone, tylko lewe i tylko prawe na kluczu jedno- lub wielopolowym albo według pozycji. |
| Join Multiple | Pełny | Transformacja złączenia wielu strumieni | Łączy wiele strumieni wejściowych. |
| Key/Value Pairs | Pełny | [Text: NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) (zadanie keyvalue) | Wyodrębnia pary klucz/wartość z kolumny tekstowej za pomocą kroku NLP AI opartego na LLM, z opcjonalnymi kluczami kandydującymi i dopasowaniem rozmytym lub dokładnym. |
| Line To Polygon | Pełny | Operacja wykonawcy Line To Polygon | Zamyka każdą linię w pierścień wielokąta, dołączony jako kolumna `Polygon`. |
| List Box | Pełny | Kontrolowana zmienna przepływu pracy | Konwertuje wybory z pola listy aplikacji na kontrolowane dane wejściowe. |
| Optymalizator lokalizacji | Częściowy | [Optymalizator lokalizacji](/pl/reference/workflow-steps/optimization/location-optimizer/) | Konwertuje liniowy przypadek minimalizacji odległości — wybór K lokalizacji tak, aby zminimalizować całkowitą lub ważoną odległość do popytu — na natywny krok MIP p-mediany. Wynik jądra grawitacyjnego, własne makro punktujące lub dowolny inny cel przeszukiwania kandydatów nadal kończy się odrzuceniem; zobacz [Migracja przepływów pracy Alteryx](/pl/guides/workflows/migrate-alteryx-workflows/#makra-w-skonwertowanym-przepływie-pracy). |
| Macro calls | Pełny | Wywołanie makra | Importuje znane źródła makr i mapuje wywołania makr na kroki makr PlaidCloud. |
| Macro Input / Macro Output | Pełny | Port wejściowy / wyjściowy makra | Mapowane bezpośrednio na porty makr PlaidCloud. |
| Utwórz siatkę | Pełny | [Spatial Make Grid](/pl/reference/workflow-steps/spatial/spatial-make-grid/) | Dzieli zakres na kwadratowe komórki, jeden wiersz na komórkę. |
| Map | Pełny | Artefakt mapy | Tworzy artefakt mapy PlaidCloud. |
| Map Input | Pełny | [Import pliku przestrzennego](/pl/reference/workflow-steps/spatial/spatial-file-import/) | Odczytuje pliki MapInfo, ESRI, KML i GeoJSON wraz z plikami towarzyszącymi. |
| Master Selector | Częściowy | Kontrolowana zmienna przepływu pracy i warunkowa widoczność kroku | Konwertuje warunki pokazywania/ukrywania narzędzia dla elementów interfejsu na warunkową widoczność kroku. Konwertuje to, który podprzepływ pracy uruchamia wybór, w trybie najlepszych starań — walidacja na rzeczywistych aplikacjach w dzierżawie jest nadal w toku, więc przejrzyj wybrany cel uruchomienia, zanim zaczniesz na nim polegać w środowisku produkcyjnym. |
| Message | Pełny | Warunek kroku (komunikat) | Emituje ostrzeżenie, komunikat lub błąd przepływu pracy na podstawie warunku. |
| Modeling | Pełny | [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/) | Łączy się z krokiem ML: trenuj model wraz z wyborem modelu w potoku. |
| Multi-Field Formula | Pełny | Transformacja formuły wielopolowej | Stosuje formułę do wybranych pól. |
| Multi-Row Formula | Pełny | Transformacja formuły okienkowej / uwzględniającej wiersze | Konwertuje logikę względną wobec wierszy na zachowanie okienkowe, z podziałem na partycje według ustawienia Grupuj według. |
| Named Entity Recognition (NER) | Pełny | [Text: NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) (zadanie ner) | Wyodrębnia jednostki (osoby, organizacje, lokalizacje, daty, ilości lub własną listę typów) z kolumny tekstowej za pomocą kroku NLP AI opartego na LLM. |
| Numeric Up Down | Pełny | Kontrolowana zmienna liczbowa | Konwertuje liczbowe dane wejściowe aplikacji na zmienną o określonym typie. |
| Output Data | Pełny | Wyjście do dokumentu / tabeli | Zapisuje wyjście do dokumentów lub tabel PlaidCloud, w tym plików Parquet i Avro; wyjścia `.yxdb`, `.hyper` i `.dbf` są zapisywane jako Parquet. |
| Overlay | Pełny | [Przetwarzanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-process/) | Część wspólna, suma lub wycięcie dwóch kolumn geometrii. |
| PDF Input | Pełny | Wykonawca ekstrakcji z PDF | Wyodrębnia tekst lub tabele z plików PDF. |
| Point To Line | Pełny | Operacja wykonawcy Point To Line | Nawleka punkty każdej grupy na jedną linię `SequenceLine` na grupę, uporządkowaną według pola sekwencji. |
| Poly-Build | Pełny | [Spatial Poly-Build](/pl/reference/workflow-steps/spatial/spatial-poly-build/) | Buduje wielokąt lub otoczkę wypukłą dla każdej grupy punktów. |
| Poly-Split | Pełny | [Spatial Poly-Split](/pl/reference/workflow-steps/spatial/spatial-poly-split/) | Jeden wiersz na wierzchołek, wielokąt składowy lub otwór. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Pełny | Artefakty raportów | Konwertują zawartość, układ i renderowanie raportu na wyjście raportu PlaidCloud. |
| POS Tagger | Pełny | [Text: NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) (zadanie pos) | Oznacza część mowy każdego tokenu z kolumny tekstowej za pomocą kroku NLP AI opartego na LLM. |
| Predict | Pełny | [ML: oceniaj](/pl/reference/workflow-steps/machine-learning/ml-score/) | Ocenia dane za pomocą wytrenowanej tabeli modelu i dołącza kolumnę predykcji. |
| Radio Button | Pełny | Kontrolowana zmienna przepływu pracy | Konwertuje wybory przycisków opcji aplikacji na kontrolowane dane wejściowe. |
| Random % Sample | Pełny | Table Extract (losowy) | Zwraca dokładną żądaną liczbę lub procent rekordów. |
| Record ID | Pełny | Transformacja identyfikatora wiersza | Dodaje deterministyczny identyfikator rekordu w skonfigurowanym typie i wartości początkowej, restartowany dla każdej grupy. |
| Redistribute | Pełny | Operacja wykonawcy Redistribute | Realokuje miarę z jednego zbioru obszarów geograficznych na inny według powierzchni nakładania, dołączoną jako kolumna `Redistributed`. |
| RegEx | Pełny | Transformacja wyrażenia regularnego | Analizuje, dopasowuje lub zamienia tekst. |
| Regression | Pełny | [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/) | Łączy łańcuch Assisted Modeling w jeden krok ML: trenuj model. |
| Report Map | Pełny | Artefakt raportu z mapą | Tworzy natywny w chmurze artefakt mapy/raportu. |
| Run Command | Częściowy | Krok [Żądanie REST](/pl/reference/workflow-steps/general/rest-request/) względem połączenia REST (tylko `curl`/`wget`) | Konwertuje wiersz poleceń `curl` lub `wget` na krok Żądanie REST. Polecenia interpretera i skryptów (`cscript`, PowerShell, Python i podobne), automatyzacja Excel-COM, operacje na systemie plików oraz polecenia nieprzejrzyste lub uruchamiające przepływy pracy są oznaczane z nazwy do ręcznego przeglądu, zamiast być konwertowane automatycznie. |
| Sample | Pełny | Transformacja próbkowania | Zachowuje rekordy według liczby, procentu lub grupowania. |
| Select | Pełny | Krok wyboru i projekcji schematu | Wybiera, zmienia nazwy, zmienia kolejność i zmienia typy pól. |
| Smooth | Pełny | [Spatial Smooth](/pl/reference/workflow-steps/spatial/spatial-smooth/) | Wygładza każdą geometrię w kilku przebiegach. |
| Sort | Pełny | Transformacja sortowania | Sortuje rekordy według skonfigurowanych pól i kierunków. |
| Spatial Info | Pełny | [Spatial Info](/pl/reference/workflow-steps/spatial/spatial-info/) | Pole powierzchni, długość, centroid i prostokąt ograniczający jako miary geodezyjne. |
| Dopasowanie przestrzenne | Pełny | [Dopasowanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/pl/reference/workflow-steps/spatial/spatial-match-executor/) | Konwertuje każdą relację — Within, Contains, Intersects, Touches, Crosses, Overlaps i Centroid-In — dopasowywaną w bazie danych lub w silniku przepływu pracy. |
| Przetwarzanie przestrzenne | Pełny | [Przetwarzanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-process/) | Część wspólna, suma lub wycięcie kolumn geometrii. |
| Summarize | Pełny | Transformacja agregująca | Grupuje i agreguje — suma, liczba, średnia, minimum, maksimum, mediana, dominanta, odchylenie standardowe, wariancja i liczba unikatowych. |
| Tab | Pełny | Grupowanie kart aplikacji | Zachowane jako struktura skonwertowanej aplikacji. |
| Test | Pełny | Warunek kroku | Konwertuje asercje testowe na warunki kroku. |
| Text Box | Pełny | Kontrolowana zmienna tekstowa | Konwertuje tekstowe dane wejściowe aplikacji na zmienną o określonym typie. |
| Text Input | Pełny | Wbudowane wejście tabeli | Tworzy wbudowane dane dla przepływu pracy. |
| Text Pre-processing | Pełny | Wykonawca przetwarzania wstępnego NLP | Normalizuje i wstępnie przetwarza tekst. |
| Text Summary | Pełny | [Text: NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) (zadanie summary) | Streszcza kolumnę tekstową do skonfigurowanej maksymalnej liczby zdań za pomocą kroku NLP AI opartego na LLM. |
| Text To Columns | Pełny | Transformacja dzielenia kolumn | Dzieli tekst na pola lub wiersze. |
| Tile | Pełny | Transformacja kafli / grupowania | Przypisuje grupy kafli według skonfigurowanej reguły. |
| Tool Container | Pełny | Kontener kanwy / grupa wykonania | Zachowany jako organizacja przepływu pracy. |
| Topic Modeling | Pełny | Wykonawca modelowania tematów | Uruchamia modelowanie tematów za pomocą zarządzanego NLP. |
| Transformation | Pełny | Krok transformacji | Konwertuje logikę transformacji na wyrażenia PlaidCloud lub SQL. |
| Transpose | Pełny | Transformacja unpivot | Konwertuje kolumny na wiersze w parę Nazwa/Wartość. |
| Tree | Pełny | Kontrolowana zmienna przepływu pracy | Konwertuje wybór z drzewa w aplikacji na kontrolowane dane wejściowe. |
| Union | Pełny | Transformacja unii | Łączy strumienie według nazwy, pozycji lub skonfigurowanych reguł. |
| Unique | Pełny | Transformacja podziału na unikatowe / duplikaty | Oddziela pierwsze unikatowe rekordy od duplikatów. |
| Visual Layout | Pełny | Metadane układu kanwy | Zachowany jako kontekst projektu. |
| Word Cloud | Pełny | Artefakt wizualizacji tekstu | Tworzy artefakt wizualizacji z analizy tekstu. |
| Analiza XML | Pełny | Transformacja analizy XML | Wyodrębnia pola XML do danych przepływu pracy. |
| Zero-shot Text Classification | Pełny | [Text: NLP AI](/pl/reference/workflow-steps/text-documents/nlp-ai/) (zadanie zeroshot) | Klasyfikuje kolumnę tekstową względem listy etykiet kandydujących dla każdego wiersza, jedno- lub wieloetykietowo, za pomocą kroku NLP AI opartego na LLM. |
| Znajdź najbliższe | Pełny | [Spatial Find Nearest](/pl/reference/workflow-steps/spatial/spatial-find-nearest/) | Złączenie najbliższych sąsiadów uszeregowane według odległości — w linii prostej oraz najbliższe według czasu dojazdu (uszeregowane według minut w sieci drogowej) za pośrednictwem własnego silnika routingu PlaidCloud. Czas dojazdu włączany dla każdego obszaru roboczego. |
| Obszar handlowy | Pełny | [Spatial Trade Area](/pl/reference/workflow-steps/spatial/spatial-trade-area/) | Koncentryczne bufory o rozmiarach w jednostkach rzeczywistych — o stałym promieniu oraz obszary handlowe według czasu dojazdu (minuty w sieci drogowej) za pośrednictwem własnego silnika routingu. Czas dojazdu włączany dla każdego obszaru roboczego. |
| Image Template | Pełny | Operacja wykonawcy Image Template | Tryb ręczny kadruje obraz do każdego regionu narysowanego na szablonie. Tryb automatyczny wykrywa regiony strony za Ciebie za pomocą otwartego modelu układu i emituje jeden wiersz na region, każdy z wykrytymi granicami i poziomem pewności do przeglądu; strona, której model nie potrafi pewnie odczytać, jest oznaczana z nazwy, zamiast być kadrowana. Wykrywanie oparte na otwartych standardach może różnić się od własnego wykrywania Alteryx — przejrzyj wykryte regiony lub użyj trybu ręcznego, aby uzyskać dokładną kontrolę. |
| Image Recognition | Pełny | Wykonawca rozpoznawania obrazów | Trenuje klasyfikator obrazów w przepływie pracy i ocenia nim nowe obrazy na miejscu — bez zewnętrznego konta i bez opuszczania PlaidCloud przez dane. Klasyfikator jest trenowany od nowa, a nie kopiowany z Alteryx, więc wyniki są wiernym przybliżeniem, a nie zgodnością co do bitu, a trenowanie działa na CPU. Włączane dla każdego obszaru roboczego. |
| Geocoder | Pełny | Własny geokoder | Geokoduje adresy do współrzędnych i odwrotnie geokoduje współrzędne do adresów za pomocą własnego geokodera PlaidCloud — bez zewnętrznego konta, bez opuszczania PlaidCloud przez dane. Włączane dla każdego obszaru roboczego. |

Widżety interfejsu (listy rozwijane, pola list, pola wyboru, dane wejściowe tekstowe/liczbowe/daty,
selektory plików i folderów), obiekty kanwy (komentarze, łącza,
kontenery) i porty makr — wszystkie konwertują się na natywne kontrolowane zmienne lub
obiekty kanwy. Pełny układ interfejsu aplikacji Alteryx — definicja `<Questions>` z pliku `.yxwz` — jest również materializowany w opublikowanym front-endzie „App
Runner" aplikacji Panel, więc konwersja aplikacji tworzy działający formularz wejściowy, który
zbiera te same wartości i steruje skonwertowanym przepływem pracy, a nie tylko
poszczególne kontrolowane zmienne. Zobacz wiersz Interfejs aplikacji analitycznej powyżej oraz
[Korzystanie ze skonwertowanych aplikacji Alteryx](/pl/guides/workflows/use-converted-alteryx-apps/#interfejs-app-runner).

**Uwaga o wyjściu do Excela.** Zwykły nowy skoroszyt — dane zapisane z domyślnym
formatowaniem — konwertuje się w pełni. Zapis do *sformatowanego szablonu*, z wypełnianiem nazwanych
arkuszy i zakresów przy zachowaniu ich formatowania, konwertuje się dla pojedynczego
arkusza oraz dla kilku wyjść złożonych w różnych arkuszach jednego skoroszytu
(krok [Export to Excel Sheets](/pl/reference/workflow-steps/export/export-to-excel-sheets/)
wypełnia wszystkie arkusze w jednym przebiegu). Szablony zawierające tabele przestawne lub wykresy
tracą te obiekty podczas zapisu arkuszy; ingerencja w pliki na poziomie arkusza, sterowana
z Run Command (Excel COM/VBS), jest oznaczana z nazwy do ręcznego przeglądu, zamiast być
konwertowana automatycznie.

## Obsługa narzędzi przestrzennych

Każde narzędzie z palety **Spatial** Alteryx ma odpowiednią trasę w PlaidCloud, a każda
z tych tras to krok, który można też zbudować ręcznie — konwersja jest
wygodą, a nie jedyną drogą. Zobacz [kroki geoprzestrzenne](/pl/reference/workflow-steps/spatial/)
w celu uzyskania pełnej dokumentacji referencyjnej oraz [Analityka geoprzestrzenna](/pl/guides/workflows/geospatial-analytics/),
aby dowiedzieć się, jak te elementy współpracują.

| Narzędzie przestrzenne Alteryx | Trasa w PlaidCloud | Miejsce uruchomienia |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/pl/reference/workflow-steps/spatial/spatial-buffer/) | Silnik przepływu pracy |
| Centroid | Operacja wykonawcy Centroid | Silnik przepływu pracy |
| Convex Hull | Operacja wykonawcy Convex Hull | Silnik przepływu pracy |
| Create Points | [Wyrażenie Table Extract](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) | Baza danych |
| Distance | [Wyrażenie Table Extract](/pl/reference/workflow-steps/spatial/spatial-sql-recipes/) | Baza danych |
| Znajdź najbliższe | [Spatial Find Nearest](/pl/reference/workflow-steps/spatial/spatial-find-nearest/) | Baza danych; usługa routingu dla czasu dojazdu |
| Generalize | [Spatial Generalize](/pl/reference/workflow-steps/spatial/spatial-generalize/) | Silnik przepływu pracy |
| Heat Map | [Heat Map (macro)](/pl/reference/workflow-steps/macros/macro-heat-map/) | Silnik przepływu pracy |
| Line To Polygon | Operacja wykonawcy Line To Polygon | Silnik przepływu pracy |
| Utwórz siatkę | [Spatial Make Grid](/pl/reference/workflow-steps/spatial/spatial-make-grid/) | Silnik przepływu pracy |
| Point To Line | Operacja wykonawcy Point To Line | Silnik przepływu pracy |
| Poly-Build | [Spatial Poly-Build](/pl/reference/workflow-steps/spatial/spatial-poly-build/) | Silnik przepływu pracy |
| Poly-Split | [Spatial Poly-Split](/pl/reference/workflow-steps/spatial/spatial-poly-split/) | Silnik przepływu pracy |
| Redistribute | Operacja wykonawcy Redistribute | Silnik przepływu pracy |
| Smooth | [Spatial Smooth](/pl/reference/workflow-steps/spatial/spatial-smooth/) | Silnik przepływu pracy |
| Spatial Info | [Spatial Info](/pl/reference/workflow-steps/spatial/spatial-info/) | Silnik przepływu pracy |
| Dopasowanie przestrzenne | [Dopasowanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-match/) | Baza danych |
| Dopasowanie przestrzenne — obiekt przecięcia, Unmatched | [Spatial Match (Intersect / Unmatched)](/pl/reference/workflow-steps/spatial/spatial-match-executor/) | Silnik przepływu pracy |
| Przetwarzanie przestrzenne | [Przetwarzanie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-process/) | Silnik przepływu pracy |
| Obszar handlowy (o stałym promieniu + czas dojazdu) | [Spatial Trade Area](/pl/reference/workflow-steps/spatial/spatial-trade-area/) | Silnik przepływu pracy; usługa routingu dla czasu dojazdu |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/pl/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Silnik przepływu pracy |
| Wejście pliku przestrzennego | [Import pliku przestrzennego](/pl/reference/workflow-steps/spatial/spatial-file-import/) | Silnik przepływu pracy |
| Summarize — SpatialObjCombine, SpatialObjConvexHull | [Łączenie przestrzenne](/pl/reference/workflow-steps/spatial/spatial-combine/) | Silnik przepływu pracy |
| Report Map | [Report Map](/pl/reference/workflow-steps/reports/report-map/) | Silnik przepływu pracy |

**Obszary handlowe i najbliższe według czasu dojazdu** — pierścienie czasu dojazdu w Trade Area i
ranking czasu dojazdu w Find Nearest działają na własnym silniku routingu PlaidCloud
(izochrony sieci drogowej i macierze czasów podróży), a nie na hostowanym interfejsie
API firmy trzeciej, więc współrzędne źródłowe nigdy nie opuszczają platformy. Czas dojazdu jest włączany dla każdego
obszaru roboczego. Routing i obszary czasu dojazdu korzystają z danych OpenStreetMap —
© OpenStreetMap contributors, dostępnych na licencji [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright).

### Znane wymagania wstępne dla danych przestrzennych

Same narzędzia przestrzenne się konwertują; poniższe punkty to wymagania wstępne dotyczące danych wejściowych.

- **Format GeoFile `.geo`.** Własnościowy binarny GeoFile Alteryx nie ma otwartego
  czytnika, więc jego import kończy się bezpiecznym odrzuceniem, zamiast awarii w czasie
  działania. W Alteryx wyeksportuj ponownie warstwę do standardowego formatu przestrzennego —
  shapefile lub GeoJSON — i zaimportuj ją zamiast tego; inne formaty przestrzenne
  nie są dotknięte. Zobacz
  [Migracja przestrzennych przepływów pracy Alteryx](/pl/guides/workflows/migrate-spatial-alteryx-workflows/#pakowanie-danych-wejściowych-przestrzennych).
- **Miara Peano key w Spatial Info.** Peano key to własnościowy indeks przestrzenny Alteryx
  bez publicznej specyfikacji, więc Spatial Info, który o nią prosi,
  pomija tę jedną kolumnę i wymienia ją w uwadze. Każda inna miara Spatial Info
  — pole powierzchni, długość, centroid, prostokąt ograniczający, typ obiektu, liczba części i punktów
  oraz punkty końcowe — jest konwertowana.
- **Współrzędne Create Points w układzie rzutowanym.** Create Points konwertuje
  współrzędne długości/szerokości geograficznej zmiennoprzecinkowe i całkowite (×1 000 000) bezpośrednio.
  Współrzędne już w układzie rzutowanym trzeba najpierw przekształcić do długości/szerokości WGS84
  wcześniej w przepływie, ponieważ przepływ pracy nie zapisuje, jakiego odwzorowania używają.

## Obsługa narzędzi Calgary

Baza danych Alteryx Calgary (`.cydb`) to własnościowy indeksowany magazyn, którego PlaidCloud nie może otworzyć. Konwersja traktuje każdą z nich jako reprezentującą jedną zwykłą tabelę PlaidCloud o nazwie `calgary_<database name>`, więc narzędzia zbudowane wokół niej konwertują się jako zwykłe operacje na tabelach, zamiast od razu się odrzucać. Zobacz [Bazy danych Calgary](/pl/guides/workflows/migrate-alteryx-workflows/#bazy-danych-calgary), aby dowiedzieć się, jak działa tabela zastępcza, oraz [Calgary Join i Cross Count Append](/pl/guides/workflows/migrate-alteryx-workflows/#calgary-join-i-cross-count-append), aby poznać narzędzia dopasowujące indeks.

| Narzędzie Alteryx Calgary | Trasa w PlaidCloud | Co jest konwertowane |
| --- | --- | --- |
| Calgary Loader | Table Extract zapisujący `calgary_<database>` | Tak, gdy baza danych ma nazwę i przechowuje co najmniej jedno pole danych. |
| Calgary Input | Dynamiczne wejście dokumentu odczytujące `calgary_<database>`, z zapisanym zapytaniem jako filtrem | Tak, w tym zapytanie zbudowane z Or lub opakowane w Not oraz filtr contains lub starts-with (odbudowany jako SQL LIKE). Odrzuca zapytanie wyszukiwania przestrzennego oraz limity Skip Records/Max Records. |
| Calgary Input (Count Only) / Calgary Cross Count | Transformacja agregująca nad `calgary_<database>` | Tak, w tym przedział zbudowany z Or lub opakowany w Not. Odrzuca cross dla więcej niż jednego pola niestandardowego oraz odczyt count-only, który nie wskazuje kolumny do zliczania. |
| Calgary Join | Dynamiczne wejście dokumentu dopasowujące każdy rekord swojego wejścia do `calgary_<database>` | Gdy pole przychodzące jest zwykłą wartością dopasowywaną do indeksu wartości — w tym w trybie Count Only, który zlicza rekordy bazy danych dopasowane przez każdy rekord wejściowy, przy czym rekord bez dopasowań daje zero. Odrzuca, gdy pole jest przestrzenne (odbuduj jako Spatial Match) lub jego typ jest nierozwiązany, a także dla Join z indeksem zakresu lub z podłączonym wyjściem unmatched, dla Join bez pola dopasowania oraz dla Join bez niczego podłączonego do wejścia. |
| Calgary Cross Count Append | Dynamiczne wejście dokumentu dopasowujące każdy rekord, a następnie zliczające złączenie nad `calgary_<database>` | Gdy pole przychodzące jest zwykłą wartością dopasowywaną do indeksu wartości: zlicza dla każdego rekordu wejściowego dopasowane rekordy bazy danych, a rekord bez dopasowań daje zero. Odrzuca indeks przestrzenny lub nierozwiązany (odbuduj jako Spatial Match), siatkę zliczania krzyżowego wartości niestandardowych, indeks zakresu oraz dopasowanie bez wskazanego pola. |

### Znane wymagania wstępne dla Calgary

Większość z nich to wymagania wstępne dotyczące danych wejściowych, a nie ograniczenia konwersji.

- **Dopasowanie do indeksu przestrzennego trzeba odbudować jako Spatial Match.** Calgary Join lub Cross Count Append dopasowywany do indeksu przestrzennego jest odrzucany z podaniem tabeli zastępczej — przepływ pracy zapisuje nazwę indeksu, ale nie to, czy zawiera zwykłe wartości, czy geometrię przestrzenną, a dopasowanie wartości (złączenie równościowe) i dopasowanie przestrzenne (punkt w wielokącie) to różne operacje. Wyeksportuj bazę danych do tabeli i odbuduj dopasowanie jako Join (indeks wartości) lub Spatial Match (indeks przestrzenny).
- **Odczyt ograniczony przez Skip Records lub Max Records wymaga jawnej kolejności.** Wyeksportowana tabela zastępcza nie przechowuje kolejności rekordów, więc dodaj kolumnę kolejności podczas eksportu, jeśli chcesz pobrać pierwsze lub ostatnie N rekordów według pozycji.
- **Bazę danych demograficznych lub referencyjnych trzeba najpierw załadować.** Odczyt Calgary przed załadowaniem jego bazy danych zatrzymuje się, podając tabelę do zbudowania. Sam plik `.cydb` nie ma otwartego czytnika, więc wyeksportuj go ponownie w Alteryx (Calgary Input do narzędzia Output Data zapisującego CSV lub Parquet) i zaimportuj jako nazwaną tabelę — zobacz [Nieczytelne bazy danych .cydb (Calgary)](/pl/guides/workflows/troubleshoot-alteryx-imports/#nieczytelne-bazy-danych-cydb-calgary). To częsty przypadek dla licencjonowanych demograficznych i referencyjnych plików `.cydb` dostarczanych z Alteryx (Experian, Census i podobnych): żaden konwerter nie odtworzy tych danych firm trzecich, więc dostarcz własne licencjonowane dane referencyjne i załaduj je do nazwanej tabeli — tak samo jak dane referencyjne Geocodera.
- **Calgary Loader, który nie przechowuje żadnego pola danych, się nie konwertuje**, ponieważ zapisana przez niego tabela nie miałaby kolumn.
- **Siatka zliczania krzyżowego wartości niestandardowych jeszcze się nie konwertuje.** Pojedyncze zwykłe pole zliczania krzyżowego się konwertuje — zlicza dla każdego rekordu wejściowego pasujące rekordy bazy danych — ale siatka *nazwanych* wartości niestandardowych dołączałaby jedną kolumnę zliczeń na wartość, a Alteryx nie dokumentuje ani liczby tych kolumn, ani ich nazw. Planowane w przyszłym wydaniu, po uzyskaniu referencyjnego eksportu do inżynierii wstecznej kontraktu kolumn.

Zapytania wartości, zakresu, contains i starts-with konwertują się na filtr; nie konwertuje się tylko zapytanie wyszukiwania przestrzennego, czyli operacja indeksu bez odpowiednika na poziomie kolumny.

## Łączenie z systemami zewnętrznymi

Punkty końcowe złączy Alteryx — Salesforce, HTTP, Google Analytics, Cassandra,
e-mail, Hadoop i Spark, w obu kierunkach — nie są konwertowane, ponieważ
PlaidCloud łączy się z tymi systemami przez połączenie, a nie przez
narzędzie na kanwie. Każde z nich jest odrzucane z podaniem nazwy i wskazaniem, gdzie
należy zrealizować to zadanie:

| Narzędzie Alteryx | Gdzie to trafia w PlaidCloud |
| --- | --- |
| Salesforce Input / Output | Połączenie **Salesforce** |
| Anaplan | Połączenie **Anaplan** |
| HTTP Input | Krok **Żądanie REST** względem połączenia **REST** |
| Google Analytics Input | **Import: źródło Singer** z tapem Google Analytics |
| Cassandra Input | **Import: źródło Singer** z tapem Cassandra |
| Email Input | **Import: źródło Singer** z tapem GMail |
| Hadoop Input / Output | **Import: SQL** / **Eksport: SQL** przez połączenie Hive, Impala lub Presto |
| Spark Input / Output | **Import: SQL** / **Eksport: SQL** przez połączenie Databricks |

Cztery z nich nie mają w ogóle ścieżki zapisu. PlaidCloud odczytuje Google Analytics
i Cassandrę, ale nigdy do nich nie zapisuje, więc narzędzie Google Analytics Output lub
Cassandra Output zamienia się w **Eksport: SQL** do obsługiwanego miejsca docelowego.
E-mail również nie jest miejscem docelowym danych: **Powiadomienie: e-mail** wysyła
powiadomienie do osób, więc narzędzie Email Output zamienia się w krok eksportu plus
osobne powiadomienie. Połączenie **Anaplan** jest tylko do odczytu w ten sam
sposób — odczytuje zapisany widok, uruchamia istniejącą akcję eksportu lub ładuje
listy do wymiaru PlaidCloud, ale nie istnieje krok PlaidCloud, który
zapisywałby z powrotem do Anaplan.

## Walidacja skonwertowanego przepływu pracy

W przypadku przepływów pracy produkcyjnych zwaliduj skonwertowane wyjścia względem zaufanych wyjść
Alteryx — walidacja PlaidCloud koncentruje się na schemacie, liczbie wierszy i wartościach wierszy
i ignoruje kolejność wierszy, chyba że przepływ pracy od niej zależy. Wyspecjalizowane
operacje (przestrzenne, dopasowanie rozmyte, OCR, NLP, raportowanie) działają przez zarządzanych
wykonawców zadań, którzy zachowują natywność przepływu pracy w chmurze; potoki uczenia maszynowego
konwertują się na natywne kroki [ML: trenuj model](/pl/reference/workflow-steps/machine-learning/ml-train/)
i [ML: oceniaj](/pl/reference/workflow-steps/machine-learning/ml-score/).
Zobacz [Migracja przepływów pracy Alteryx](/pl/guides/workflows/migrate-alteryx-workflows/),
aby zapoznać się z kompletnym przewodnikiem importu i walidacji.
