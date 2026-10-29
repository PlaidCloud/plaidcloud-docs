---
title: Archiwizowanie projektu
description: Archiwizuj projekty PlaidCloud, aby zachować ukończoną pracę, zwolnić zasoby obszaru roboczego i utrzymać porządek w środowisku projektów.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/archive-a-project.md
---

## Tworzenie archiwum


Projekty zwykle zawierają krytyczne procesy i logikę, które warto archiwizować. Jeśli kiedykolwiek będzie trzeba przywrócić projekt do określonego stanu, archiwa są niezbędne. 



PlaidCloud pozwala archiwizować projekty w dowolnym momencie. Tworzenie archiwów uzupełnia wbudowane śledzenie zmian w czasie w PlaidCloud, umożliwiając utrwalenie wybranych punktów w czasie. Może to być szczególnie przydatne przed większą zmianą lub aby zachować dokładny stan środowiska produkcyjnego.



**Pełna kopia zapasowa**: obejmuje wszystkie tabele danych należące do projektu. Archiwum może być dość duże, zależnie od ilości danych w projekcie.


**Częściowa kopia zapasowa:** można jej użyć, jeśli wszystkie dane projektu można odtworzyć z innych źródeł. W takim przypadku nie trzeba archiwizować danych projektu, skoro i tak znajdują się gdzie indziej. Częściowe archiwa skracają czas tworzenia archiwum i oszczędzają miejsce.



Aby zarchiwizować projekt:


1. Otwórz Analyze
2. Wybierz kartę „Projekty”
3. Wybierz projekt, a następnie wybierz **Eksportuj archiwum projektu** z menu **Akcje** (lub kliknij projekt prawym przyciskiem myszy i wybierz **Eksportuj archiwum projektu**)

Pasek tytułu okna zawiera nazwę archiwizowanego projektu, więc przed rozpoczęciem możesz potwierdzić, że wybrano właściwy.

### Podczas tworzenia archiwum

Okno eksportu zamyka się, gdy tylko PlaidCloud przyjmie żądanie, a dalej przebieg archiwizacji śledzi okno postępu. Możesz zostawić to okno otwarte, aby obserwować postęp, albo wysłać je w tło i pracować dalej — archiwizacja i tak działa na platformie, a zamknięcie okna postępu jej nie zatrzymuje.

Powiadomienie informuje, jak się zakończyła: że archiwum zostało zapisane, które tabele trafiły do niego bez danych, a w razie niepowodzenia — dlaczego. Nie musisz trzymać okna otwartego, aby je otrzymać.

:::note
Archiwizacja dużego projektu może trwać od kilku sekund do godziny, zależnie od ilości zawartych w nim danych tabel. Długo trwające archiwizowanie jest normalne i nie oznacza, że coś poszło nie tak — poczekaj na powiadomienie zamiast uruchamiać drugi eksport, który archiwizowałby projekt od nowa.
:::

### Tabele, których danych nie można uwzględnić

Czasami tabela wymieniona w projekcie nie ma już żadnych danych — na przykład tabela, która nigdy nie została zbudowana, lub której dane usunięto poza projektem. Archiwum jest mimo to zapisywane: takie tabele są pomijane w danych tabel, a eksport kończy się komunikatem z ich nazwami. Wszystko inne — konfiguracja projektu, przepływy pracy, definicje tabel i dane wszystkich pozostałych tabel — jest archiwizowane normalnie.

Archiwum zapisuje, które tabele trafiły do niego bez danych, a przywracanie ponownie wymienia je na końcu, zamiast przedstawiać je jako kompletne. Tabela, której definicja była nadal czytelna, wraca z kolumnami i bez wierszy; tabela, której definicji również zabrakło, wraca jako wpis bez tabeli. Uruchom ponownie przepływ pracy, który buduje tabelę, aby ją wypełnić.

:::note
Zaplanowane archiwum zapisuje pominięte tabele w dzienniku systemowym zamiast pokazywać komunikat, ponieważ nie ma ekranu, na którym mógłby się pojawić. Gdy ma znaczenie, które tabele uwzględniono, sprawdź komunikat eksportu.
:::

### Jeśli nie możesz odczytać tabel projektu

Odczyt tabel projektu to uprawnienie odrębne od odczytu samego projektu, a archiwum zależy od obu. Jeśli możesz otworzyć projekt, ale nie masz dostępu do odczytu tabel, archiwum jest mimo to zapisywane — po prostu nie zawiera danych tabel ani definicji tabel, ponieważ oba elementy podlegają temu samemu uprawnieniu. Eksport kończy się komunikatem z nazwami pominiętych tabel, podanymi przez ich wewnętrzne identyfikatory, a nie nazwy, ponieważ nazwy pochodzą z definicji, których archiwum nie zawiera.

Archiwum utworzone w ten sposób jest kopią konfiguracji projektu — jego przepływów pracy, zmiennych, wymiarów, widoków i układów, w zakresie, w jakim masz prawo je odczytać — a nie jego danych. **Przywrócenie go nie odtwarza żadnych tabel**, więc nie jest to kopia zapasowa, z której można odbudować dane projektu. Sprawdź komunikat eksportu, zanim zaczniesz polegać na takim archiwum.

W przeciwieństwie do opisanych wyżej tabel nie rozwiąże tego ponowne uruchomienie przepływu pracy — dane nigdy nie zostały odczytane. Poproś administratora obszaru roboczego o przyznanie dostępu do odczytu tabel projektu, a następnie utwórz archiwum ponownie.

:::caution
Dotyczy to również zaplanowanych archiwów, które działają jako określony członek. Jeśli ten członek nie ma dostępu do odczytu tabel, każde archiwum tworzone przez harmonogram zawiera wyłącznie konfigurację, a niedobór jest zapisywany w dzienniku systemowym i nikomu nie pokazywany. Jeśli przechowujesz zaplanowane archiwa jako kopie zapasowe, upewnij się, że członek, jako którego działają, może odczytywać tabele projektu.
:::

### Jeśli projekt korzysta z dostępu do wierszy

Utworzenie archiwum odczytuje tabele projektu, więc [Dostęp do wierszy](/pl/administration/access/managing-security-groups-and-assignments/#zarządzanie-dostępem-do-wierszy) obowiązuje tak samo jak przy każdym innym odczycie. Dla każdej kolumny sterującej archiwum zawiera wiersze przyznane Twoim grupom. Jeśli nie masz uprawnienia do kolumny, wynik zależy od sposobu jej zadeklarowania: kolumna pozostawiona z domyślną odmową nie daje żadnych wierszy, a kolumna zadeklarowana z domyślnym zezwoleniem na wszystko pozostaje niefiltrowana. Tabela niezawierająca żadnej z kolumn sterujących jest archiwizowana w całości, a Architekt projektu archiwizuje wszystkie wiersze niezależnie od uprawnień. Zaplanowane archiwum działa w ramach własnej tożsamości projektu, a nie Twojej, więc archiwizuje wszystkie wiersze.

Archiwum utworzone przez członka mającego tylko część uprawnień jest częściową kopią danych projektu, a kolumna pozostawiona z domyślną odmową oznacza, że tabela może wrócić pusta, a nie tylko zawężona. Przywrócenie takiego archiwum odbudowuje projekt bez tych wierszy i nic w procesie przywracania o tym nie informuje, bo z punktu widzenia archiwum tych wierszy nigdy nie było.

:::caution
Jeśli potrzebujesz archiwum, z którego można odbudować cały projekt, utwórz je jako członek, który odczytuje projekt w całości.
:::

### Jeśli eksport się nie powiedzie

Eksport, który się nie powiedzie, teraz zgłasza błąd. Wcześniej archiwum mogło zgłosić zakończenie, mimo że nie zostało zapisane, i brak pliku wychodził na jaw dopiero później — najczęściej przy próbie przywrócenia. Nieudany eksport teraz to zgłasza, więc traktuj zgłoszony sukces jako prawdziwy i sprawdzaj komunikat przy każdym zgłoszonym błędzie. To samo dotyczy pozostałych typów eksportu, nie tylko archiwów projektów.

## Przywracanie archiwum


Gdy masz archiwum, możesz chcieć je przywrócić. Archiwum można przywrócić do nowego projektu lub do istniejącego projektu.



Aby przywrócić archiwum:


1. Otwórz Analyze
2. Wybierz kartę „Projekty”
3. Wybierz **Importuj archiwum projektu** z menu **Akcje** (lub z paska narzędzi) i wskaż archiwum do przywrócenia
4. Wybierz, czy **Utwórz nowy projekt**, czy **Importuj do istniejącego projektu**, i wskaż w drzewie wyboru, co przenieść
5. Kliknij **Importuj projekt**

Import działa w tle. Okno postępu pokazuje, jak daleko zaszedł, a komunikat informuje o zakończeniu — wraz z wiadomością e-mail, jeśli cokolwiek pominięto. Jeśli importu nie można rozpocząć — na przykład dlatego, że wybrany projekt jest zablokowany — okno pozostaje otwarte i wyjaśnia powód.


Archiwum jest sprawdzane podczas otwierania. Archiwum zawierające treści, których archiwum projektu nigdy nie zawiera — plik, który trafiłby poza własny folder archiwum, łącze wskazujące poza nie lub ustawienia próbujące utworzyć cokolwiek innego niż zwykłe dane — jest odrzucane, zanim cokolwiek z niego zostanie przywrócone.


Nie musisz przenosić całego archiwum. Drzewo wyboru wyświetla zawartość archiwum według typu — przepływy pracy, kroki, tabele, wymiary, edytory danych, funkcje zdefiniowane przez użytkownika — a wszystko, co zaznaczysz, pociąga za sobą swoje zależności.


### Gdy część archiwum nie zostanie zaimportowana


Import jest kontynuowany, gdy część archiwum nie może zostać przywrócona. Dopóki archiwum można odczytać, a sam projekt można skonfigurować, projekt jest importowany, a wszystko, czego nie udało się przywrócić, jest wymienione w wyniku importu. Jeśli archiwum nie można odczytać lub nie można skonfigurować samego projektu, import kończy się niepowodzeniem i podaje powód, a nowy projekt jest usuwany. Import do istniejącego projektu może również zatrzymać się przed ukończeniem. Wszystko, co zostało już przywrócone, pozostaje w projekcie. Komunikat i wiadomość e-mail informują, że import został zatrzymany, a wynik importu podaje kiedy i dlaczego oraz wymienia to, czego do tego momentu nie udało się przywrócić.

Gdy cokolwiek pominięto, komunikat i wiadomość e-mail na końcu importu o tym informują, a komunikat zawiera łącze do okna **Wynik importu**. Okno wymienia każdy element według typu i nazwy, podaje powód i grupuje elementy pod następującymi nagłówkami:

- **Nie zaimportowano** — elementu nie ma w projekcie.
- **Utworzono bez danych** — tabela, widok lub wymiar jest w projekcie, ale nie zawiera danych, ponieważ nie udało się ich odczytać ani załadować.
- **Ostrzeżenia** — element został zaimportowany, ale jest coś do sprawdzenia, na przykład kolumny, które magazyn danych przekonwertował na typy kolumn tabeli.
- **Zmienne, które zachowały wartość tego projektu** — projekt miał już zmienną o tej nazwie, więc zachowała własną wartość.

Najpoważniejsze elementy są wymienione jako pierwsze, a okno informuje, gdy jest ich więcej, niż wyświetla. Aby ponownie otworzyć okno później, wybierz projekt na karcie **Projekty** i wybierz **Wyświetl wynik importu lub kopiowania** z menu **Akcje** albo kliknij projekt prawym przyciskiem myszy.

Wynik pozostaje przy projekcie, dopóki ktoś go nie odrzuci lub dopóki nie zastąpi go późniejszy import do tego samego projektu. Kliknij **Odrzuć wynik**, aby usunąć go dla wszystkich, którzy mogą otworzyć projekt; nic w projekcie się nie zmienia. Odrzucenie wymaga dostępu do edycji projektu, a projekt nie może być zablokowany.


### Importowanie do istniejącego projektu


Import do istniejącego projektu dodaje zawartość, a nie zastępuje go. O tym, co się stanie, gdy archiwum i projekt zawierają ten sam element, decydują dwie rzeczy.


**Musisz mieć możliwość zmiany projektu docelowego.** Import do projektu, w którym nie masz żadnej roli, jest odrzucany, podobnie jak import do projektu zablokowanego przed zmianami — sprawdzenie następuje przed odczytem lub zapisem czegokolwiek, więc odrzucony import nie zmienia projektu.


**Projekt zachowuje własne ustawienia.** Jego nazwa, identyfikator, środowisko połączenia z danymi, domyślne ustawienia magazynu, konto dokumentów, typ dostępu, listy dostępu i uprawnienia dostępu do wierszy pozostają bez zmian. Przenoszona jest tylko zaznaczona zawartość.

Krok ustawiony na **Domyślny projektu** przenosi to ustawienie, a nie konto — po przywróceniu przyjmuje domyślną wartość, jaką ma projekt, a nie tę, jaką miał w chwili archiwizacji.


### Zduplikowane elementy


Gdy przychodzący element jest tym samym elementem, który już jest w projekcie, wybierasz, co się z nim stanie:


- **Nadpisz zduplikowane elementy danymi przychodzącymi** — wersja z archiwum zastępuje tę w projekcie.
- **Utwórz nową kopię zduplikowanych elementów** — projekt zachowuje to, co ma, a przychodzący element jest dodawany obok z dopisanym do nazwy ` copy` (oraz licznikiem, jeśli ta nazwa też jest zajęta). Dotyczy to przepływów pracy, kroków, tabel, wymiarów, edytorów danych, widoków i funkcji zdefiniowanych przez użytkownika.


**Wyjątkiem są zmienne projektu i przepływu pracy.** Zmienna jest identyfikowana po nazwie, więc nie da się dodać jej drugiej kopii bez zmiany nazwy na taką, do której nic się nie odwołuje. Gdy projekt definiuje już zmienną, którą zawiera także archiwum, zachowywana jest wartość projektu, a wynik importu wymienia zmienne pozostawione bez zmian. Jeśli chcesz wartość z archiwum, ustaw ją potem na zmiennej.


Warto wiedzieć: to dopasowanie opiera się na tożsamości, a nie na nazwie. Element pochodzący pierwotnie z tego samego projektu — wszystko, z czego wyeksportowano archiwum, lub jego kopia — jest rozpoznawany jako ten sam element. Dwa elementy, które tylko przypadkiem mają tę samą nazwę, są traktowane jako różne i po imporcie będą obecne oba.

### Jeśli tabela wraca bez danych


Przywrócenie danych tabeli zależy od tego, czy jej kolumny pasują do tabeli, do której trafiają — te same nazwy w tej samej kolejności, ponieważ według tego działa ładowanie. Gdy nie pasują, dane tej tabeli są pomijane, a tabela jest wymieniona w wyniku importu w grupie **Utworzono bez danych**, tak samo jak tabela, której danych nie było w archiwum. Sama różnica w zapisanym typie kolumny nie wstrzymuje danych: dane są ładowane, a tabela jest wymieniona w grupie **Ostrzeżenia** wraz z kolumnami, które magazyn danych przekonwertował.


Import, w którym nie udało się załadować danych żadnej tabeli, nadal zachowuje projekt. Jego końcowy komunikat, podobnie jak wynik importu, informuje, że nie udało się załadować żadnych danych tabel. Jeśli import kończy się z wszystkimi przepływami pracy, tabelami i wymiarami na miejscu, przeczytaj jego końcowy komunikat, zanim założysz, że wiersze również trafiły do projektu.


## Harmonogram archiwizacji


Archiwa mogą również służyć jako okresowa kopia zapasowa projektu. PlaidCloud pozwala zarządzać harmonogramem kopii zapasowych i ustawiać okres przechowywania archiwów kopii zapasowych na dowolną wygodną lub pożądaną wartość.


Ponieważ wszystkie zmiany w projekcie są śledzone automatycznie, archiwizacja nie jest konieczna do celów wycofania zmian. Zapewnia jednak konkretne migawki stanu projektu, które często przydają się do celów kontrolnych lub umożliwiają powrót do znanego punktu.



Aby ustawić harmonogram archiwizacji:


1. Otwórz Analyze
2. Wybierz kartę „Projekty”
3. Kliknij ikonę kopii zapasowej
4. Wybierz katalog docelowy na koncie **Dokument**
5. Wybierz częstotliwość i okres przechowywania kopii zapasowych
6. Wybierz, które elementy objąć kopią zapasową
7. Kliknij „Aktualizuj”
