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
| Simulate | Każdy krok księgowania ERP buduje i sprawdza dokładnie to, co zaksięguje, po czym niczego nie zatwierdza i nigdy nie łączy się z ERP. Wpisy, które zostałyby zaksięgowane, są zapisywane w [historii księgowań ERP](/pl/guides/connections/erp-post-history/) i oznaczane jako symulowane, dzięki czemu można je przejrzeć przed uruchomieniem na żywo. |
| Off | Kroki księgowania są całkowicie pomijane. |

Projekt ma również własny limit trybu księgowania, ustawiany za pomocą interfejsu API projektu lub asystenta przez dowolnego członka z uprawnieniami do zapisu w odblokowanym projekcie. Limit może jedynie zwiększać bezpieczeństwo uruchomienia, nigdy je zmniejszać: efektywny tryb uruchomienia to bardziej restrykcyjny z wybranego trybu i limitu projektu, więc projekt z limitem Simulate pozostaje symulowany, nawet jeśli uruchomienie rozpoczęto jako Live.

[Zdarzenie harmonogramu](/pl/administration/scheduled-events/event-scheduler/#tryb-księgowania-erp) zachowuje własny tryb księgowania, więc harmonogram ustawiony na Simulate działa w trybie symulacji przy każdym wyzwoleniu.

Tryb obejmuje wszystko, czego dotyka uruchomienie. Podprzepływ pracy, makro oraz kroki **Run Model**, **Conditional Run Model** i **Loop Model** dziedziczą tryb uruchomienia nadrzędnego, podobnie jak uruchomienie [wznowione](#wstrzymywanie-zatrzymywanie-i-wznawianie) po zatrzymaniu — uruchomienie symulowane nie może nigdzie w swoim obrębie zaksięgować naprawdę.

:::caution
Kroki księgowania SAP, załączników SAP i ogólne kroki SAP RFC nie wykonują próbnego uruchomienia. W trybie Simulate lub Off są po prostu pomijane, ponieważ własne flagi testowe SAP nadal otwierają rzeczywiste połączenie z SAP — pominięcie kroku to jedyny sposób, aby uruchomienie symulowane nigdy nie dotarło do SAP.
:::

:::note
Pojedynczy krok księgowania ERP ma także własne ustawienie Validate Only (w niektórych krokach oznaczone jako Preview lub Test Only Mode), niezależne od trybu księgowania uruchomienia opisanego powyżej. Edytor kroku zawsze zapisuje je jawnie. Konfiguracja kroku zapisana w inny sposób — przez REST API, MCP lub import pakietu przepływu pracy — która całkowicie pomija to ustawienie, teraz również domyślnie wykonuje podgląd zamiast księgowania na żywo.
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

Krok, którego nie można bezpiecznie powtórzyć, nie jest uruchamiany ponownie. Kończy się raz błędem z komunikatem **interrupted**, ponieważ drugie uruchomienie mogłoby zduplikować to, co zapisała już pierwsza próba. Kroki zapisujące dane wyjściowe z `{date}` w nazwie lub ścieżce są traktowane jako niebezpieczne do powtórzenia, ponieważ ponowne uruchomienie mogłoby przypaść na inną datę. Aby wyjść z sytuacji, sprawdź w celu kroku, co zapisała pierwsza próba, w razie potrzeby to wyczyść, a następnie [uruchom krok ponownie](/pl/guides/workflows/running-one-step-in-a-workflow/) lub **Wznów** uruchomienie.

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

## Wstrzymywanie, zatrzymywanie i wznawianie

Gdy przepływ pracy jest uruchomiony, można użyć **Wstrzymaj**, aby kroki w toku się zakończyły, a nowe kroki czekały, lub **Zatrzymaj**, co anuluje kroki w kolejce oraz wszystkie nadal działające zadania importu lub eksportu, a także zapytanie w hurtowni danych, z którego odczytywał eksport. Kroki importu i wymiarów, które nadal były w kolejce, są anulowane w czysty sposób, więc nie blokują późniejszych importów i ładowań wymiarów w obszarze roboczym. Zatrzymanie zatrzymuje także oczekujące lub działające synchronizacje konektora (Singer) przepływu pracy, aby synchronizacja nie działała dalej po zatrzymaniu przepływu pracy.

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
