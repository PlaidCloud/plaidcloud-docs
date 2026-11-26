---
title: Uruchamianie przepływu pracy
description: Uruchom przepływ pracy PlaidCloud ręcznie lub na żądanie, śledź stan każdego kroku oraz wstrzymuj, zatrzymuj i wznawiaj uruchomienie od miejsca, w którym zostało przerwane.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pełne uruchomienie przepływu pracy można wywołać, klikając ikonę uruchamiania w hierarchii **Przepływy pracy** albo wybierając **Run All** z menu **Akcje** w danym przepływie pracy.



Można też kliknąć przycisk **Toggle Start/Stop** u góry tabeli przepływów pracy. Ten przycisk przełącznika zatrzymuje uruchomiony przepływ pracy lub uruchamia przepływ pracy.

Jeśli klikniesz **Uruchom** dla przepływu pracy, który już jest uruchomiony, PlaidCloud poinformuje o tym zamiast rozpoczynać drugie uruchomienie.

## Wybór trybu księgowania

Każde uruchomienie ma tryb księgowania ERP. Aby wybrać tryb w PlaidCloud, użyj opcji **Uruchom z trybem księgowania** w menu kontekstowym przepływu pracy (prawy przycisk myszy) lub przycisku trybu uruchomienia na kanwie przepływu pracy; zwykłe **Uruchom przepływ pracy** lub **Uruchom przepływ pracy** wymaga trybu Live, nadal z zastrzeżeniem limitu projektu opisanego poniżej. Tryb można też wybrać, rozpoczynając uruchomienie za pomocą interfejsu API uruchamiania lub asystenta.

| Tryb | Co się dzieje |
|---|---|
| Live | Kroki księgowania księgują dokładnie tak jak zawsze. Jest to ustawienie domyślne. |
| Simulate | Każdy krok księgowania ERP buduje i sprawdza dokładnie to, co zaksięguje, po czym niczego nie zatwierdza i nigdy nie łączy się z ERP. Wpisy, które zostałyby zaksięgowane, są zapisywane, dzięki czemu można je przejrzeć przed uruchomieniem na żywo: wpisy kroku **Księgowanie dokumentów** w [Rejestrze księgowań](/pl/guides/connections/posting-register/) jako **Zostałby zaksięgowany** (zobacz [Księgowanie dokumentów w systemach ERP](/pl/guides/connections/post-documents/)), a wpisy własnego kroku księgowania danego systemu w [historii księgowań ERP](/pl/guides/connections/erp-post-history/), oznaczone jako symulowane. |
| Off | Kroki księgowania są całkowicie pomijane. |

Projekt ma również własny limit trybu księgowania, ustawiany za pomocą interfejsu API projektu lub asystenta przez dowolnego członka z uprawnieniami do zapisu w odblokowanym projekcie. Limit może jedynie zwiększać bezpieczeństwo uruchomienia, nigdy je zmniejszać: efektywny tryb uruchomienia to bardziej restrykcyjny z wybranego trybu i limitu projektu, więc projekt z limitem Simulate pozostaje symulowany, nawet jeśli uruchomienie rozpoczęto jako Live.

[Zdarzenie harmonogramu](/pl/administration/scheduled-events/event-scheduler/#tryb-księgowania-erp) zachowuje własny tryb księgowania, więc harmonogram ustawiony na Simulate działa w trybie symulacji przy każdym wyzwoleniu.

Tryb obejmuje wszystko, czego dotyka uruchomienie. Podprzepływ pracy, makro oraz kroki **Run Model**, **Conditional Run Model** i **Loop Model** dziedziczą tryb uruchomienia nadrzędnego, podobnie jak uruchomienie [wznowione](#wstrzymywanie-zatrzymywanie-i-wznawianie) po zatrzymaniu — uruchomienie symulowane nie może nigdzie w swoim obrębie zaksięgować naprawdę.

:::caution
Kroki księgowania SAP, załączników SAP i ogólne kroki SAP RFC nie wykonują próbnego uruchomienia. W trybie Simulate lub Off są po prostu pomijane, ponieważ własne flagi testowe SAP nadal otwierają rzeczywiste połączenie z SAP — pominięcie kroku to jedyny sposób, aby uruchomienie symulowane nigdy nie dotarło do SAP.
:::

:::note
Pojedynczy krok księgowania ERP ma także własne ustawienie Validate Only (w niektórych krokach oznaczone jako Preview lub Test Only Mode), niezależne od trybu księgowania uruchomienia opisanego powyżej. Edytor kroku zawsze zapisuje je jawnie. Konfiguracja kroku zapisana w inny sposób — przez REST API, MCP lub import pakietu przepływu pracy — która całkowicie pomija to ustawienie, teraz również domyślnie wykonuje podgląd zamiast księgowania na żywo. Krok **Księgowanie dokumentów** nie ma takiego ustawienia: o tym, czy księguje, decydują tryb uruchomienia i tryb jego systemu — zobacz [Księgowanie dokumentów w systemach ERP](/pl/guides/connections/post-documents/).
:::

## Autoryzowanie projektu do księgowania

Uruchomienie przepływu pracy księguje w ERP jako projekt, a nie jako osoba, która je rozpoczęła. Aby uruchomienie mogło księgować, projekt potrzebuje autoryzacji dla każdego połączenia ERP i środowiska używanego przez jego kroki księgowania. Bez niej krok kończy się błędem „This project isn't authorized to post to connection …” z nazwą połączenia i środowiska. Kroki **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** i **Call SAP RFC** nie wymagają autoryzacji.

Aby autoryzować projekt, otwórz jego stronę główną i wybierz **Autoryzacje zapisu ERP** w sekcji **Księgowanie ERP**. Każdy wiersz to jedno połączenie w jednym środowisku. Zaznacz **Autoryzowano**, aby umożliwić projektowi księgowanie w tym miejscu, lub wyczyść zaznaczenie, aby to zatrzymać. Kolumny **Autoryzowane przez** i **Autoryzowano o** pokazują, kto ostatnio udzielił autoryzacji i kiedy.

- Przycisk jest widoczny dla Architektów projektu i administratorów obszaru roboczego, ale tylko Architekt może zmienić autoryzację i to tylko wtedy, gdy projekt jest odblokowany. Administrator obszaru roboczego, który nie jest Architektem, może najpierw dodać siebie jako Architekta.
- Wybranie wiersza w celu autoryzowania lub wyczyszczenia autoryzacji nie przeładowuje listy: pozycja przewijania i wybrane sortowanie kolumn pozostają bez zmian. Rozmiar okna można zmieniać, a uwaga o projektach publicznych jest wyświetlana w całości.
- Aby autoryzować połączenie, potrzebujesz również uprawnień do zapisu w nim: jesteś jego właścicielem albo zostało ci udostępnione imiennie lub przez jedną z twoich grup zabezpieczeń. Połączenie ustawione na **Wszyscy członkowie obszaru roboczego** się nie liczy.
- Projekt ustawiony na **Wszyscy członkowie obszaru roboczego** jest autoryzowany jak każdy inny. Każdy członek jest jego Architektem, więc każdy członek z uprawnieniami do zapisu w połączeniu może autoryzować dla niego projekt. Po autoryzacji każdy członek może księgować w tym połączeniu z przepływów pracy projektu, a okno informuje o tym nad siatką.
- Nowa kopia prywatna dla Ciebie, utworzona z danymi tabel lub członkami wymiarów, zachowuje autoryzacje źródła, których mógłbyś udzielić samodzielnie, i trafia w tryb Simulate, jeśli źródło było w trybie Live — zobacz [Autoryzacje zapisu ERP w kopii](/pl/guides/projects/managing-projects/#autoryzacje-zapisu-erp-w-kopii). Każda inna kopia lub projekt utworzony z archiwum projektu zaczyna bez autoryzacji. Autoryzuj go, zanim zacznie księgować.

## Śledzenie stanu kroku

Gdy przepływ pracy jest uruchomiony, każdy krok ma ikonę stanu pokazującą, na jakim jest etapie, obok czasu jego trwania. Najedź kursorem na ikonę, aby zobaczyć stojący za nią komunikat.

| Stan | Co oznacza |
|---|---|
| Oczekuje | Krok jest w kolejce i jeszcze się nie rozpoczął. |
| Uruchomiony | Krok działa, a jego czas trwania rośnie w miarę postępu. |
| Ukończony | Krok zakończył się pomyślnie. |
| Ostrzeżenie | Krok zakończył się, ale zgłosił coś wartego przeczytania w [dzienniku przepływu pracy](/pl/guides/workflows/viewing-workflow-log/). |
| Błąd | Krok zakończył się niepowodzeniem. Zobacz [Zarządzanie błędami kroków](/pl/guides/workflows/managing-step-errors/). |
| Pominięty | Krok został pominięty — jest wyłączony lub nie spełniono jego warunków uruchomienia. Zobacz [Pomijanie kroków w przepływie pracy](/pl/guides/workflows/skip-steps-in-a-workflow/). |
| Kontynuowany | Krok zakończył się niepowodzeniem, ale jest ustawiony na kontynuację po błędzie, więc przepływ pracy działał dalej. Zobacz [Kontynuuj po błędzie](/pl/guides/workflows/continue-on-error/). |
| Zatrzymany | Uruchomienie zostało zatrzymane, zanim krok mógł się zakończyć. |
| Porzucony | Wykonywanie kroku zostało przerwane, więc nigdy się nie zakończy. Wznów uruchomienie lub uruchom przepływ pracy ponownie. |

Otwarty widok przepływu pracy odświeża się samoczynnie w miarę postępu uruchomienia, więc wyświetlane stany pozostają aktualne bez przeładowywania strony.

### Porzucone kroki

Krok jest oznaczany jako **porzucony**, gdy to, co go wykonywało, zniknęło w trakcie uruchomienia — najczęściej dlatego, że ktoś nacisnął **Zatrzymaj**, albo dlatego, że uruchomienie przerwały prace konserwacyjne platformy. Czas trwania kroku przestaje rosnąć, a podpowiedź stanu wyjaśnia, co się stało.

Porzucony krok nie został ukończony i nie wytworzył żadnych danych wyjściowych. Nie jest to wolny krok ani problem z danymi lub konfiguracją.

Aby wrócić do pracy, [**Wznów**](#wstrzymywanie-zatrzymywanie-i-wznawianie) uruchomienie — porzucony krok zostanie uruchomiony ponownie — lub uruchom ponownie cały przepływ pracy. Oba sposoby są bezpieczne.

### Przerwane kroki

Jeśli serwer wykonujący krok zostanie utracony w trakcie uruchomienia, PlaidCloud automatycznie uruchamia krok ponownie, gdy bezpiecznie jest go powtórzyć: krok, który zastępuje swoje dane wyjściowe, kończy z takim samym wynikiem jak pojedyncze czyste uruchomienie, więc nie ma nic do sprawdzenia. Dziennik kroku pokazuje ostrzeżenie w miejscu, w którym zaczyna się druga próba: „Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start.”

Krok, którego nie można bezpiecznie powtórzyć, nie jest uruchamiany ponownie. Kończy się raz błędem z komunikatem **interrupted**, ponieważ drugie uruchomienie mogłoby zduplikować to, co zapisała już pierwsza próba. Kroki zapisujące dane wyjściowe z `{date}` lub `{date_iso}` w nazwie lub ścieżce są traktowane jako niebezpieczne do powtórzenia, ponieważ ponowne uruchomienie mogłoby przypaść na inną datę. Aby wyjść z sytuacji, sprawdź w miejscu docelowym kroku, co zapisała pierwsza próba, w razie potrzeby to wyczyść, a następnie [uruchom krok ponownie](/pl/guides/workflows/running-one-step-in-a-workflow/) lub **Wznów** uruchomienie.

### Kroki, które nigdy się nie rozpoczynają

Gdy krok czeka na proces roboczy, jego komunikat stanu brzmi „Waiting for a worker… N min. No import worker has picked this step up yet.” (rodzaj procesu roboczego odpowiada krokowi, na przykład import lub eksport). Komunikat znika, gdy praca się rozpocznie.

Jeśli zadanie kroku nigdy nie może się rozpocząć, krok kończy się niepowodzeniem z podaniem przyczyny, zamiast czekać w nieskończoność:

| Przyczyna | Niepowodzenie po około |
|---|---|
| Żaden proces roboczy nie podejmuje zadania kroku importu lub wymiaru | 40 minutach |
| Pod kroku utknął w stanie Pending | 20 minutach |
| Nie można pobrać obrazu kroku | 5 minutach |
| Dla kroku nie utworzono poda | 20 minutach |
| Żaden runner nie podejmuje synchronizacji konektora (Singer) | 30 minutach |

Komunikat o synchronizacji konektora wskazuje nazwę synchronizacji. Jeśli proces roboczy rozpoczął zadanie, a następnie zniknął, krok również kończy się niepowodzeniem z komunikatem, że proces roboczy został zatrzymany. Komunikaty dotyczące importu i wymiaru zawierają „Use Run from here to retry.”

### Uruchomienia, które przestają odpowiadać

Uruchomienie nigdy nie pozostaje w stanie **Uruchomiony** po zniknięciu pracy, która za nim stoi. Jeśli serwer wykonujący przepływ pracy zostanie utracony, uruchomienie kończy się niepowodzeniem. Uruchomienie może trwać najwyżej 12 godzin: takie, które w tym momencie nadal trwa, kończy się niepowodzeniem z komunikatem „Run failed: still running at the 12-hour limit. Re-run the workflow.”

## Run Insight

Run Insight pokazuje, na co jedno uruchomienie przepływu pracy zużyło czas i które kroki trwały dłużej lub krócej niż zwykle. Ocenia każdy krok względem jego własnych ostatnich uruchomień, więc krok, który jest zawsze wolny, nie jest wyróżniany.

### Otwieranie Run Insight

- Na kanwie kliknij **Historia** na pasku narzędzi. Zobacz [Wizualny projektant przepływów pracy](/pl/guides/workflows/advanced-workflows/).
- Na karcie **Przepływy pracy** zaznacz jeden przepływ pracy i wybierz **Run Insight** z menu **Akcje** lub z menu kontekstowego.
- Na stronie głównej wybierz **Otwórz ostatnie uruchomienie** na karcie przepływu pracy.
- W oknie dialogowym historii uruchomień wybierz uruchomienie w tabeli **Uruchomienia** za pomocą **Otwórz w Insight** albo otwórz jego wiersz.
- W komunikacie Weave w aplikacji o wolnym uruchomieniu kliknij **Otwórz uruchomienie**. Zobacz [Powiadamianie o zakończeniu uruchomienia](/pl/guides/ai-assistant/weave-findings/#powiadamianie-po-zakończeniu-uruchomienia).

Okno dialogowe ma tytuł **Historia uruchomień** — nazwa przepływu pracy. Przełącznik **Insight** | **Uruchomienia** zmienia ten widok a tabelą poprzednich uruchomień. Historia uruchomień pojedynczego kroku, otwarta z Inspektora, pokazuje tylko tabelę.

### Odczytywanie nagłówka i listy uwag

Nagłówek podaje wynik uruchomienia w jednym wierszu: **Czas:** *czas*, **Trwa od** *czas*, gdy uruchomienie trwa, **Zatrzymano po** *czas* dla ostatniego uruchomienia, które zatrzymano, albo **Niepowodzenie w** przepływie pracy, w którym wystąpiło niepowodzenie. Zdanie pod nim mówi, co się wyróżnia, na przykład kroki, które działały wolniej niż zwykle, czas spędzony na oczekiwaniu albo to, że każdy krok z historią mieścił się w swoim zwykłym zakresie. Poniżej znajdują się czas rozpoczęcia i liczba przepływów pracy i kroków oraz, gdy niektóre kroki mają zbyt małą historię, by je ocenić, ich liczba. Gdy coś wymaga spojrzenia, obok nagłówka pojawia się licznik oznaczony **Do sprawdzenia:**.

Obok nagłówka znajduje się pasek ostatnich uruchomień z podpisem nad nim. Każdy słupek to uruchomienie, a jego wysokość odpowiada czasowi, jaki zajęło; dzień jest opisany tylko tam, gdzie się zmienia. Kliknij uruchomienie na pasku, aby je otworzyć. Czerwona nasadka i ✕ oznaczają uruchomienie, które zakończyło się niepowodzeniem, a przerywany kontur oznacza uruchomienie, które wykonało mniej kroków niż większość ostatnich uruchomień, ponieważ nie można go porównać z pełnym uruchomieniem.

**Wymaga uwagi** wymienia w tej kolejności najpierw niepowodzenia, potem czas ponad normę, a na końcu oczekiwanie. Każda pozycja jest kartą z nazwą, utraconym czasem lub oznaczeniem **Niepowodzenie**, miejscem, w którym się znajduje, oraz paskiem jej czasu, na którym szary kolor oznacza czas w normie, a bursztynowy czas ponad normę, a pasek niepowodzenia jest czerwony. Krok zapisany po ostatnim uruchomieniu ma znacznik **Zapisano** *data*. Kliknij kartę, aby zaznaczyć ją w widoku; zaznaczona karta jest wyróżniona.

### Przepływ, oś czasu i tabela

Nagłówek nad widokiem zawiera nazwę przepływu pracy, następnie **Porównaj z**, potem **Widok**, którego przyciski **Przepływ**, **Oś czasu** i **Tabela** wybierają widok, a po prawej przycisk Odśwież.

| Widok | Co pokazuje |
|---|---|
| **Przepływ** | Bloki, których wysokość odpowiada czasowi. Bursztynowy kolor oznacza czas ponad normę kroku. Blok, który nie jest otwarty, ale zawiera niepowodzenie, pokazuje ✕ i czerwony kontur. Zakończony niepowodzeniem lub zaznaczony blok zbyt krótki, by pomieścić nazwę, jest rysowany wyższy, a legenda mówi, że nie jest wtedy w skali. Gdy krok wywołał inne przepływy pracy, wycinek **Narzut wywołania** to czas samego kroku poza tymi przepływami pracy. Gdy żaden krok nie był uruchomiony, wycinek **Oczekiwanie** pokazuje przerwę; przepływ pracy wykonany równolegle jej nie rysuje. |
| **Oś czasu** | Czas zegarowy od początku uruchomienia. Przerywany kontur pokazuje, jak długo blok trwał w porównywanym uruchomieniu. |
| **Tabela** | Wszystko w kolejności wywołań, z kolumnami **Nazwa**, **To uruchomienie**, **Zwykle**, **Dodatkowe**, **Porównywane uruchomienie** i **Stan**. |

Przepływ pracy, który wywołał inne przepływy pracy, pokazuje je w swoim wnętrzu. Kliknij dwukrotnie blok przepływu pracy lub wybierz **Powiększ**, aby pracować w jego wnętrzu, a aby wrócić, użyj ścieżki nad widokiem. Gdy kilka bloków zgodnych z normą stoi obok siebie, **Przepływ** zwija je w jeden blok **N zgodnie z normą**; kliknij jeden z nich lub kliknij **Pokaż wszystkie bloki (***liczba***)** po prawej stronie ścieżki, aby je otworzyć; liczba oznacza wszystkie bloki w widoku. **Zwiń bloki zgodne z normą** zwija je ponownie, a przycisk pojawia się tylko wtedy, gdy coś można zwinąć.

Zaznacz blok, aby zobaczyć jego panel szczegółów. Pokazuje on nazwę i miejsce bloku, znacznik stanu z jednym z poniższych oznaczeń oraz wiersze z tymi spośród **To uruchomienie**, **Zwykle**, **Historia**, **Ponad normę** i **Porównywane uruchomienie**, które mają zastosowanie. Następnie widać linię trendu: dla przepływu pracy tego uruchomienia są to jego ostatnie pełne uruchomienia, z tym uruchomieniem jako kropką, gdy zostało ukończone; dla kroku ze zwykłym zakresem jest to ten zakres jako pasmo z tym uruchomieniem jako kropką. Uwagi wyjaśniają oznaczenie, a przyciski to **Pokaż w jego przepływie pracy**, **Pokaż jego kroki** lub **Powiększ**, **Otwórz przepływ pracy** i **Wyświetl dziennik uruchomienia**. **Otwórz przepływ pracy** otwiera przepływ pracy na kanwie, a **Wyświetl dziennik uruchomienia** otwiera jego [dziennik](/pl/guides/workflows/viewing-workflow-log/).

### Co oznaczają znaczniki

| Znacznik | Znaczenie |
|---|---|
| **Niepowodzenie** | Krok zakończył się błędem. Panel pokazuje jego komunikat, chyba że Twoja rola nie może zobaczyć nazwy kroku. |
| **Wolniej niż zwykle** | Krok trwał dłużej niż jego zwykły zakres. |
| **Wolniej w całości** | Każdy krok w przepływie pracy działał wolniej mniej więcej o tyle samo, co wskazuje na coś wspólnego dla całego przepływu pracy, a nie na pojedynczy krok. Jego kroki pokazują **Część wspólnego spowolnienia**. |
| **Ma wolne kroki** | Przepływ pracy z **Wolne kroki wewnątrz**. |
| **Zgodnie z normą** | Krok mieścił się w swoim zwykłym zakresie. |
| **Szybciej** | Krok działał szybciej niż jego zwykły zakres. |
| **Za mało historii** | Krok nie był uruchamiany wystarczająco często, by mieć zwykły zakres, więc nie jest oceniany. |
| **Błąd, kontynuowano** | Krok zakończył się niepowodzeniem, ale jest skonfigurowany tak, aby [kontynuować po błędzie](/pl/guides/workflows/continue-on-error/). |
| **Pominięto** | Krok został pominięty. |
| **Uruchomiony** | Krok jeszcze się nie zakończył. |

Krok, którego ostatnie uruchomienia były już wolne lub bardzo się różniły, może nie zostać oznaczony. Uruchomienie na koniec okresu, porównane ze zwykłymi dniami, może wyglądać na wolniejsze w całości. Starsze zatrzymane uruchomienie pojawia się jako krótkie uruchomienie, a nie jako zatrzymane.

Panel może też wyjaśnić znacznik. **Oczekiwanie** to czas, gdy żaden krok nie był uruchomiony, więc nie ma kroku, który za to odpowiada. W kroku, który działał wolniej niż zwykle, **Zapisane wiersze** porównuje wynik kroku z jego zwykłą liczbą i jest pomijane, gdy zabezpieczenia na poziomie wierszy filtrują to, co możesz odczytać, a **Zapisano od ostatniego uruchomienia** oznacza, że krok został zapisany po jego poprzednim uruchomieniu i przed rozpoczęciem tego; rekord pokazuje zapis, a nie to, co się zmieniło. **Inna praca** zlicza kroki, które się nie uruchomiły, oraz kroki, które się uruchomiły bez historii, mierzone względem historii każdego kroku albo, gdy porównujesz z innym uruchomieniem, względem tego uruchomienia. **Wykonano równolegle** oznacza, że części przepływu pracy działały jednocześnie, więc ich czasy sumują się do więcej niż czas zegarowy. **Wywołujący niepewny** oznacza, że historia nie pozwala pokazać, który krok wywołał przepływ pracy. **Nazwa ukryta** oznacza krok lub przepływ pracy, którego nazwy Twoja rola nie może zobaczyć; są pokazane jako **Ukryty krok** lub **Ukryty przepływ pracy**.

### Porównaj z

**Porównaj z** ustala, względem czego mierzone jest uruchomienie. Przycisk jego menu pokazuje wybór: **Norma**, **Norma + poprzednie uruchomienie** lub **Norma + uruchomienie z** czasem rozpoczęcia wybranego uruchomienia. **Norma** używa ostatnich uruchomień każdego kroku. **Norma + poprzednie uruchomienie** i **Norma + wybrane uruchomienie** dodają też czas tego uruchomienia dla każdego kroku, który **Oś czasu** obrysowuje, a **Tabela** pokazuje w kolumnie **Porównywane uruchomienie**. **Norma + wybrane uruchomienie** otwiera listę ostatnich uruchomień do wyboru.

### Jeden przepływ pracy wewnątrz większego uruchomienia

Gdy otworzysz przepływ pracy wywołany przez inny przepływ pracy, Insight pokazuje tylko jego część uruchomienia. **Otwórz całe uruchomienie** przełącza to samo okno dialogowe na przepływ pracy, który rozpoczął uruchomienie.

### Uruchomienia na żywo

Uruchomienie, które nadal trwa, jest odczytywane ponownie co 30 sekund, dopóki okno dialogowe jest widoczne. Powiększenie, zaznaczenie i widok pozostają bez zmian. Przejście z Insight do **Uruchomienia** zatrzymuje aktualizacje, a powrót do Insight ponownie odczytuje uruchomienie i wznawia je. Przycisk Odśwież, okrągłe strzałki po prawej stronie nagłówka, ładuje uruchomienie od nowa, resetuje powiększenie i zaznaczenie oraz ponownie zwija bloki zgodne z normą.

### Dla asystentów AI i interfejsu REST API

Ten sam profil jest dostępny poza oknem dialogowym:

- REST: `GET /rest/v1/analyze/workflow/run-insight` z `project_id` i `workflow_id`. `run_id` wskazuje uruchomienie (najnowsze, gdy pominięto), a `baseline` to `typical`, `previous` lub `run:<id>`.
- MCP: `workflow_describe` z `include=['run_insight']` oraz opcjonalnymi `run_id` i `baseline`.

Każdy przepływ pracy i każdy krok wraca z czasem, miejscem w uruchomieniu, werdyktem względem własnej historii i powodami. Uruchomienie, które nie istnieje lub nie ma wierszy kroków, zwraca zamiast błędu brak profilu i ostrzeżenie.

## Wstrzymywanie, zatrzymywanie i wznawianie

Gdy przepływ pracy jest uruchomiony, można użyć **Wstrzymaj**, aby kroki w toku się zakończyły, a nowe kroki czekały, lub **Zatrzymaj**, co anuluje kroki w kolejce oraz, w ciągu kilku sekund, wszystkie nadal działające zadania importu lub eksportu, a także zapytanie w hurtowni danych, z którego odczytywał eksport. Kroki importu i wymiarów, które nadal były w kolejce, są anulowane w czysty sposób, więc nie blokują późniejszych importów i ładowań wymiarów w obszarze roboczym. Zatrzymanie zatrzymuje także oczekujące lub działające synchronizacje konektora (Singer) przepływu pracy, aby synchronizacja nie działała dalej po zatrzymaniu przepływu pracy.

Po naciśnięciu **Zatrzymaj** działające zadanie importu lub eksportu nie rozpoczyna żadnego nowego zapisu: eksport nie przesyła pliku, a import nie ładuje tabeli. Zapis już w toku zostaje najpierw dokończony, więc żaden plik, żadna tabela ani żaden wymiar nie zostają zapisane tylko w połowie. Eksport wielu plików lub eksport kilku tabel zachowuje pliki, które zdążył już zapisać. Eksport CSV wielu plików zatrzymany w trakcie zdążył już opróżnić swój folder, więc folder zawiera tylko te pliki i żadnych z wcześniejszego uruchomienia. Ładowanie wymiaru oraz eksport do MongoDB lub Kafka zapisują dane na bieżąco, więc taki, który już się rozpoczął, działa do końca. Krok **Importuj SQL** lub **Importuj zewnętrzne tabele bazy danych** zatrzymuje się, gdy źródłowa baza danych zwróci to, co odczytywała, ponieważ PlaidCloud nie anuluje zapytania do źródła. W Databend eksport, który sam Databend zapisuje na koncie dokumentów, jest jednym zapisem, więc działa do końca i zapisuje swój plik.

Makro może działać w kilku miejscach jednocześnie, wywoływane przez inne przepływy pracy lub przez krok **Makro: uruchomienie współbieżne**. Zatrzymanie makra zatrzymuje wszystkie jego działające kopie. Zatrzymanie jednej kopii zatrzymuje tylko tę kopię i to, co uruchomiła, a przepływ pracy, który ją wywołał, działa dalej — tak samo jak wtedy, gdy krok **Macro Concurrent** rezygnuje z kopii, która przestała odpowiadać. Makro działające tylko wewnątrz innych przepływów pracy jest wyświetlane na liście przepływów pracy jako **Uruchomiony**, z dostępną opcją **Zatrzymaj**, a po jego otwarciu widać stan każdego kroku oraz czas rozpoczęcia i zakończenia z jego ostatniego uruchomienia.

**Wznów** podejmuje wstrzymane, zatrzymane lub zakończone błędem uruchomienie od miejsca, w którym zostało przerwane, zamiast zaczynać od nowa. Jest dostępne zawsze, gdy ostatnie uruchomienie przepływu pracy zakończyło się w stanie wstrzymanym, zatrzymanym lub błędu.

Znaczenie „miejsca, w którym przerwano” zależy od sposobu wykonywania przepływu pracy:

| Wykonywanie | Przy wznowieniu |
|---|---|
| Szeregowe | Rozpoczyna od kroku, który był wykonywany, gdy uruchomienie się zakończyło, i kontynuuje od niego. Jeśli ten krok znajduje się w grupie, Wznów podejmuje całą grupę najwyższego poziomu, która go zawiera: kroki w grupie, które już zakończyły się pomyślnie, są pomijane, pozostałe są uruchamiane, a uruchomienie kontynuuje po grupie. |
| Równoległe | Uruchamia ponownie każdy krok, który jeszcze nie zakończył się pomyślnie, i pomija ukończone kroki. |
| Zaawansowane (graf) | Uruchamia ponownie węzeł, który zakończył się błędem, i wszystko, co na niego nadal czeka, a ukończone węzły pomija. |

Kroki wywołujące inny przepływ pracy — **Run Model**, **Conditional Run Model** i **Loop Model** — wznawiają wywoływany przepływ pracy zamiast go restartować, przez dowolną liczbę poziomów zagnieżdżenia. Krok pętli wznawia przerwaną iterację i pomija iteracje, które już się zakończyły.

Gdy wznawiasz przepływ pracy uruchomiony jako **zagnieżdżony element podrzędny** innego — wywołany przez krok **Run Model** w elemencie nadrzędnym — PlaidCloud oferuje **Wznów od początku łańcucha**. Wznowienie samego elementu podrzędnego nie może kontynuować orkiestracji elementu nadrzędnego, więc ta opcja wznawia element nadrzędny najwyższego poziomu — korzeń łańcucha — i kontynuuje cały łańcuch od miejsca, w którym się zatrzymał. Wznawianie przepływu pracy najwyższego poziomu pozostaje bez zmian. Początek łańcucha jest ustalany w obrębie tego samego projektu: łańcuch przekraczający granicę innego projektu jest wznawiany od początku części znajdującej się w projekcie.

Wznawianie zawsze kontynuuje **oryginalne** uruchomienie. Uruchamia ponownie każdy krok z tego uruchomienia, który nie zakończył się pomyślnie — krok, który zakończył się błędem lub został porzucony, jest uruchamiany ponownie, a nie traktowany jako ukończony — a ponowne uruchomienie pojedynczego kroku w międzyczasie nie zmienia tego, co Wznów podejmie następnie. Dotyczy to również podrzędnego przepływu pracy: jeśli jeden z jego kroków uruchomiono ponownie osobno, wznowienie nadrzędnego przepływu pracy nadal uruchamia wszystko, co pozostało do wykonania w przepływie podrzędnym, a nie tylko ten krok.

Wznowione uruchomienie jest zapisywane jako **nowe uruchomienie** w historii uruchomień przepływu pracy i zawiera tylko kroki, które ponownie uruchomiło. Oryginalne uruchomienie zachowuje własny wpis w historii. Gdy jedno uruchomienie wywołuje ten sam podrzędny przepływ pracy więcej niż raz, każde wywołanie ma własny wpis w historii uruchomień przepływu podrzędnego. Iteracje kroku pętli liczą się jako jedno wywołanie.

:::note
Krok pętli dopasowuje ukończone iteracje według wartości ich zmiennych. Jeśli dane, po których iteruje pętla, zmieniły się między oryginalnym uruchomieniem a wznowieniem, iteracje, których nie można już dopasować, są uruchamiane ponownie zamiast pomijane.
:::
