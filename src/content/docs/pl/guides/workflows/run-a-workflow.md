---
title: Uruchamianie przepływu pracy
description: Uruchom przepływ pracy PlaidCloud ręcznie lub na żądanie, śledź stan każdego kroku oraz wstrzymuj, zatrzymuj i wznawiaj uruchomienie od miejsca, w którym zostało przerwane.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pełne uruchomienie przepływu pracy możesz wywołać, klikając ikonę uruchamiania w hierarchii **Przepływy pracy** albo wybierając **Run All** z menu **Akcje** w danym przepływie pracy.



Możesz też kliknąć przycisk **Toggle Start/Stop** u góry tabeli przepływów pracy. Ten przełącznik zatrzymuje uruchomiony przepływ pracy albo go uruchamia.

Jeśli klikniesz **Uruchom** dla przepływu pracy, który już działa, PlaidCloud poinformuje o tym zamiast rozpoczynać drugie uruchomienie.

## Wybór trybu księgowania

Każde uruchomienie ma tryb księgowania ERP. Aby wybrać tryb w PlaidCloud, użyj **Uruchom z trybem księgowania** w menu kontekstowym przepływu pracy (prawy przycisk myszy) albo przycisku trybu uruchomienia na kanwie przepływu pracy; zwykłe **Uruchom przepływ pracy** lub **Uruchom przepływ pracy** żąda trybu Na żywo, z zastrzeżeniem limitu projektu opisanego poniżej. Tryb możesz też wybrać, uruchamiając przepływ pracy przez API uruchamiania lub asystenta.

| Tryb | Co się dzieje |
|---|---|
| Na żywo | Kroki księgowania księgują dokładnie tak, jak dotychczas. Jest to tryb domyślny. |
| Symulacja | Każdy krok księgowania ERP buduje i waliduje dokładnie to, co by zaksięgował, po czym niczego nie zatwierdza i nigdy nie łączy się z ERP. Zapisy, które zostałyby zaksięgowane, są rejestrowane w [historii księgowań ERP](/pl/guides/connections/erp-post-history/) i oznaczone jako symulowane, dzięki czemu możesz je przejrzeć przed uruchomieniem na żywo. |
| Wyłączone | Kroki księgowania są całkowicie pomijane. |

Projekt ma również własny limit trybu księgowania, ustawiany przez API projektu lub asystenta przez dowolnego członka z uprawnieniami do zapisu w odblokowanym projekcie. Limit może jedynie zwiększać bezpieczeństwo uruchomienia, nigdy go nie rozluźnia: efektywny tryb uruchomienia to bardziej restrykcyjny z wybranego przez Ciebie trybu i limitu projektu, więc projekt z limitem Symulacja pozostaje symulowany, nawet jeśli uruchomisz go jako Na żywo.

[Zdarzenie harmonogramu](/pl/administration/scheduled-events/event-scheduler/#tryb-księgowania-erp) zachowuje własny tryb księgowania, więc harmonogram ustawiony na Symulację uruchamia się w trybie symulacji za każdym razem.

Tryb obowiązuje we wszystkim, czego dotyczy uruchomienie. Podprzepływ pracy, makro oraz kroki **Run Model**, **Conditional Run Model** i **Loop Model** dziedziczą tryb uruchomienia nadrzędnego, podobnie jak uruchomienie [wznowione](#wstrzymywanie-zatrzymywanie-i-wznawianie) po zatrzymaniu — uruchomienie symulowane nie może nigdzie wewnątrz siebie księgować naprawdę.

:::caution
Kroki księgowania SAP, załączników SAP i ogólne kroki SAP RFC nie wykonują próbnego przebiegu. W trybie Symulacja lub Wyłączone są po prostu pomijane, ponieważ własne flagi testowe SAP nadal otwierają rzeczywiste połączenie z SAP — pominięcie kroku to jedyny sposób, aby uruchomienie symulowane nigdy nie dotarło do SAP.
:::

:::note
Pojedynczy krok księgowania ERP ma także własne ustawienie Validate Only (w niektórych krokach nazywane Preview lub Test Only Mode), niezależne od opisanego wyżej trybu księgowania uruchomienia. Edytor kroku zawsze zapisuje je jawnie. Konfiguracja kroku zapisana w inny sposób — przez REST API, MCP lub import pakietu przepływu pracy — która w ogóle pomija to ustawienie, również domyślnie wykonuje teraz podgląd zamiast księgowania na żywo.
:::

## Autoryzacja projektu do księgowania

Uruchomienie przepływu pracy księguje w ERP jako projekt, a nie jako osoba, która je rozpoczęła. Aby uruchomienie mogło księgować, projekt potrzebuje autoryzacji dla każdego połączenia ERP i środowiska używanego przez jego kroki księgowania. Bez niej krok kończy się błędem „This project isn't authorized to post to connection …”, w którym podane są połączenie i środowisko. Kroki **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** i **Call SAP RFC** jej nie wymagają.

Aby autoryzować projekt, otwórz jego stronę główną i wybierz **Autoryzacje zapisu ERP** w sekcji **Księgowanie ERP**. Każdy wiersz to jedno połączenie w jednym środowisku. Zaznacz **Autoryzowano**, aby zezwolić projektowi na księgowanie tam, albo wyczyść pole, aby to cofnąć. **Autoryzowane przez** i **Autoryzowano o** pokazują, kto ostatnio udzielił autoryzacji i kiedy.

- Przycisk jest widoczny dla Architektów projektu i administratorów obszaru roboczego, ale autoryzację może zmienić tylko Architekt i tylko wtedy, gdy projekt jest odblokowany. Administrator obszaru roboczego, który nie jest Architektem, może wcześniej dodać siebie jako Architekta.
- Wybranie wiersza w celu autoryzowania lub cofnięcia autoryzacji nie przeładowuje listy: pozycja przewijania i wybrane sortowanie kolumn pozostają bez zmian. Rozmiar okna można zmieniać, a uwaga o projektach publicznych jest zawijana w całości.
- Aby autoryzować połączenie, potrzebujesz także uprawnień do zapisu w nim: jesteś jego właścicielem albo zostało Ci udostępnione imiennie lub przez jedną z Twoich grup zabezpieczeń. Połączenie ustawione na **Wszyscy członkowie obszaru roboczego** się nie liczy.
- Projekt ustawiony na **Wszyscy członkowie obszaru roboczego** jest autoryzowany tak jak każdy inny. Każdy członek jest jego Architektem, więc każdy członek z uprawnieniami do zapisu w połączeniu może autoryzować projekt dla tego połączenia. Po autoryzacji każdy członek może księgować do tego połączenia z przepływów pracy projektu, a okno informuje o tym nad siatką.
- Nowa kopia prywatna dla Ciebie, wykonana z danymi tabel lub elementami wymiarów, zachowuje te autoryzacje źródła, które możesz przyznać samodzielnie, a jeśli źródło działało w trybie Na żywo, kopia trafia w trybie Symulacja — zobacz [Autoryzacje zapisu ERP w kopii](/pl/guides/projects/managing-projects/#autoryzacje-zapisu-erp-w-kopii). Każda inna kopia oraz projekt utworzony z archiwum projektu zaczynają bez żadnych autoryzacji. Autoryzuj taki projekt, zanim zacznie księgować.

## Śledzenie stanu kroku

Podczas działania przepływu pracy każdy krok ma ikonę stanu pokazującą, na jakim etapie się znajduje, obok czasu jego trwania. Najedź kursorem na ikonę, aby zobaczyć stojący za nią komunikat.

| Stan | Co oznacza |
|---|---|
| Oczekuje | Krok jest w kolejce i jeszcze się nie rozpoczął. |
| Uruchomiony | Krok działa, a jego czas trwania rośnie na bieżąco. |
| Zakończony | Krok zakończył się pomyślnie. |
| Ostrzeżenie | Krok się zakończył, ale zgłosił coś, co warto przeczytać w [dzienniku przepływu pracy](/pl/guides/workflows/viewing-workflow-log/). |
| Błąd | Krok zakończył się niepowodzeniem. Zobacz [Zarządzanie błędami kroków](/pl/guides/workflows/managing-step-errors/). |
| Pominięty | Krok został pominięty — jest wyłączony albo nie spełniono jego warunków uruchomienia. Zobacz [Pomijanie kroków w przepływie pracy](/pl/guides/workflows/skip-steps-in-a-workflow/). |
| Kontynuowany | Krok zakończył się niepowodzeniem, ale jest ustawiony na kontynuowanie po błędzie, więc przepływ pracy działał dalej. Zobacz [Kontynuowanie po błędzie](/pl/guides/workflows/continue-on-error/). |
| Zatrzymany | Uruchomienie zostało zatrzymane, zanim krok zdążył się zakończyć. |
| Porzucony | Wykonywanie kroku zostało przerwane, więc nigdy się nie zakończy. Wznów uruchomienie albo uruchom przepływ pracy ponownie. |

Otwarty widok przepływu pracy odświeża się samoczynnie w miarę postępu uruchomienia, więc wyświetlane stany pozostają aktualne bez przeładowywania strony.

### Porzucone kroki

Krok jest oznaczany jako **porzucony**, gdy to, co go wykonywało, zniknęło w trakcie uruchomienia — najczęściej dlatego, że ktoś nacisnął **Zatrzymaj**, albo dlatego, że uruchomienie przerwały prace konserwacyjne platformy. Czas trwania kroku przestaje rosnąć, a etykieta narzędzia dla stanu wyjaśnia, co się stało.

Porzucony krok nie został ukończony i nie wygenerował żadnych danych wyjściowych. Nie jest to wolny krok ani problem z Twoimi danymi czy konfiguracją.

Aby wznowić pracę, [**Wznów**](#wstrzymywanie-zatrzymywanie-i-wznawianie) uruchomienie — porzucony krok zostanie uruchomiony ponownie — albo uruchom ponownie cały przepływ pracy. Obie metody są bezpieczne.

### Przerwane kroki

Jeśli serwer wykonujący krok zostanie utracony w trakcie uruchomienia, PlaidCloud automatycznie uruchamia krok ponownie, gdy bezpiecznie można go powtórzyć: krok, który zastępuje swoje dane wyjściowe, daje taki sam wynik jak pojedyncze czyste uruchomienie, więc nie musisz niczego sprawdzać.

Krok, którego nie można bezpiecznie powtórzyć, nie jest uruchamiany ponownie. Kończy się jednorazowym błędem z komunikatem **Przerwano**, ponieważ drugie uruchomienie mogłoby zduplikować to, co zapisała pierwsza próba. Kroki zapisujące dane wyjściowe z `{date}` w nazwie lub ścieżce są traktowane jako niebezpieczne do powtórzenia, ponieważ ponowne uruchomienie mogłoby trafić na inną datę. Aby odzyskać stan, sprawdź w miejscu docelowym kroku, co zapisała pierwsza próba, w razie potrzeby to wyczyść, a następnie [uruchom krok ponownie](/pl/guides/workflows/running-one-step-in-a-workflow/) albo **Wznów** uruchomienie.

### Kroki, które nigdy się nie rozpoczynają

Jeśli żaden proces roboczy nie podejmie zadania kroku importu lub wymiaru w ciągu około 40 minut, krok kończy się niepowodzeniem, zamiast pokazywać **Uruchomiony** aż do upłynięcia 24-godzinnego limitu czasu. Jeśli proces roboczy rozpoczął zadanie, a potem zniknął, krok również kończy się niepowodzeniem, z komunikatem informującym, że proces roboczy się zatrzymał. Oba komunikaty zawierają tekst „Use Run from here to retry.”

## Wstrzymywanie, zatrzymywanie i wznawianie

Gdy przepływ pracy działa, możesz kliknąć **Wstrzymaj**, aby kroki w toku się zakończyły, a nowe kroki czekały, albo **Zatrzymaj**, co anuluje kroki oczekujące w kolejce oraz wszystkie nadal działające zadania importu lub eksportu. Kroki importu i wymiarów, które nadal były w kolejce, są anulowane w czysty sposób, więc nie blokują późniejszych importów i ładowań wymiarów w obszarze roboczym.

**Wznów** podejmuje wstrzymane, zatrzymane lub zakończone błędem uruchomienie od miejsca, w którym zostało przerwane, zamiast zaczynać od nowa. Jest dostępne zawsze, gdy ostatnie uruchomienie przepływu pracy zakończyło się stanem wstrzymania, zatrzymania lub błędu.

To, co oznacza „od miejsca, w którym zostało przerwane”, zależy od sposobu wykonywania przepływu pracy:

| Wykonywanie | Przy wznowieniu |
|---|---|
| Szeregowe | Zaczyna od kroku, który działał, gdy uruchomienie się zakończyło, i kontynuuje od niego. Jeśli ten krok znajduje się w grupie, Wznów podejmuje całą grupę najwyższego poziomu, która go zawiera: kroki w grupie, które już zakończyły się pomyślnie, są pomijane, pozostałe są uruchamiane, a uruchomienie jest kontynuowane po grupie. |
| Równoległe | Ponownie uruchamia każdy krok, który nie zakończył się jeszcze pomyślnie, i pomija zakończone kroki. |
| Zaawansowane (graf) | Ponownie uruchamia węzeł, który zakończył się błędem, oraz wszystko, co na niego nadal czeka, i pomija zakończone węzły. |

Kroki wywołujące inny przepływ pracy — **Run Model**, **Conditional Run Model** i **Loop Model** — wznawiają wywoływany przepływ pracy zamiast uruchamiać go od początku, przez dowolną liczbę poziomów zagnieżdżenia. Krok pętli wznawia przerwaną iterację i pomija iteracje, które już się zakończyły.

Gdy wznawiasz przepływ pracy uruchomiony jako **zagnieżdżony element podrzędny** innego — wywołany przez krok **Run Model** w przepływie nadrzędnym — PlaidCloud oferuje **Wznów od początku łańcucha**. Samodzielne wznowienie elementu podrzędnego nie może kontynuować orkiestracji elementu nadrzędnego, więc ta opcja wznawia przepływ nadrzędny najwyższego poziomu — korzeń łańcucha — i kontynuuje cały łańcuch od miejsca, w którym został zatrzymany. Wznowienie przepływu pracy najwyższego poziomu przebiega bez zmian. Początek łańcucha jest ustalany w obrębie tego samego projektu: łańcuch przekraczający granicę innego projektu jest wznawiany od początku części znajdującej się w projekcie.

Wznowienie zawsze kontynuuje **oryginalne** uruchomienie. Ponownie uruchamia każdy krok z tego uruchomienia, który nie zakończył się pomyślnie — krok, który zakończył się błędem lub został porzucony, jest uruchamiany ponownie, a nie traktowany jako ukończony — a samodzielne ponowne uruchomienie pojedynczego kroku w międzyczasie nie zmienia tego, co Wznów podejmie następnie.

Wznowione uruchomienie jest rejestrowane jako **nowe uruchomienie** w historii uruchomień przepływu pracy i zawiera tylko kroki, które ponownie uruchomiło. Oryginalne uruchomienie zachowuje własny wpis w historii.

:::note
Krok pętli dopasowuje ukończone iteracje na podstawie wartości ich zmiennych. Jeśli dane, po których iteruje pętla, zmieniły się między oryginalnym uruchomieniem a wznowieniem, iteracje, których nie można już dopasować, są uruchamiane ponownie zamiast pomijane.
:::
