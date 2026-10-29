---
title: Uruchamianie przepływu pracy
description: Uruchom przepływ pracy PlaidCloud ręcznie lub na żądanie, śledź stan każdego kroku oraz wstrzymuj, zatrzymuj i wznawiaj uruchomienie od miejsca, w którym zostało przerwane.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pełne uruchomienie przepływu pracy możesz wywołać, klikając ikonę uruchamiania w hierarchii **Przepływy pracy** albo wybierając **Run All** z menu **Akcje** w danym przepływie pracy.



Możesz też kliknąć przycisk **Toggle Start/Stop** u góry tabeli przepływów pracy. Ten przycisk przełącznika zatrzymuje uruchomiony przepływ pracy albo go uruchamia.

Jeśli klikniesz **Uruchom** dla przepływu pracy, który już jest uruchomiony, PlaidCloud poinformuje o tym zamiast rozpoczynać drugie uruchomienie.

## Wybór trybu księgowania

Każde uruchomienie ma przypisany tryb księgowania ERP. Aby wybrać tryb w PlaidCloud, użyj **Uruchom z trybem księgowania** w menu kontekstowym przepływu pracy (prawy przycisk myszy) lub przycisku trybu uruchamiania na kanwie przepływu pracy; zwykłe **Uruchom przepływ pracy** żąda trybu Na żywo, nadal z uwzględnieniem limitu projektu opisanego poniżej. Tryb możesz też wybrać, uruchamiając przepływ pracy przez interfejs API uruchamiania lub asystenta.

| Tryb | Co się dzieje |
|---|---|
| Na żywo | Kroki księgowania księgują dokładnie tak, jak dotychczas. To ustawienie domyślne. |
| Symulacja | Każdy krok księgowania ERP buduje i sprawdza dokładnie to, co by zaksięgował, po czym niczego nie zatwierdza i nigdy nie łączy się z ERP. Zapisy, które zostałyby zaksięgowane, są rejestrowane w [historii księgowań ERP](/pl/guides/connections/erp-post-history/) i oznaczone jako symulowane, dzięki czemu możesz je przejrzeć przed uruchomieniem na żywo. |
| Wyłączone | Kroki księgowania są całkowicie pomijane. |

Projekt ma też własny limit trybu księgowania, ustawiany przez interfejs API projektu lub asystenta przez dowolnego członka z uprawnieniami do zapisu w odblokowanym projekcie. Limit może jedynie zwiększać bezpieczeństwo uruchomienia, nigdy je zmniejszać: efektywny tryb uruchomienia to bardziej restrykcyjny z trybu wybranego przez Ciebie i limitu projektu, więc projekt z limitem Symulacja pozostaje symulowany, nawet jeśli uruchomisz go jako Na żywo.

[Zdarzenie harmonogramu](/pl/administration/scheduled-events/event-scheduler/#tryb-księgowania-erp) zachowuje własny tryb księgowania, więc harmonogram ustawiony na Symulację uruchamia się w trybie symulacji za każdym razem.

Tryb jest przenoszony na wszystko, czego dotyka uruchomienie. Podprzepływ pracy, makro oraz kroki **Run Model**, **Conditional Run Model** i **Loop Model** dziedziczą tryb uruchomienia nadrzędnego, podobnie jak uruchomienie [wznowione](#wstrzymywanie-zatrzymywanie-i-wznawianie) po zatrzymaniu — symulowane uruchomienie nie może nigdzie w swoim obrębie księgować naprawdę.

:::caution
Kroki księgowania SAP, załączników SAP i ogólne kroki SAP RFC nie wykonują próbnego uruchomienia. W trybie Symulacja lub Wyłączone są po prostu pomijane, ponieważ własne flagi testowe SAP nadal otwierają rzeczywiste połączenie z SAP — pominięcie kroku to jedyny sposób, by symulowane uruchomienie nigdy nie dotarło do SAP.
:::

:::note
Pojedynczy krok księgowania ERP ma także własne ustawienie Validate Only (w niektórych krokach nazywane Preview lub Test Only Mode), niezależne od trybu księgowania uruchomienia opisanego wyżej. Edytor kroku zawsze zapisuje to ustawienie jawnie. Konfiguracja kroku zapisana w inny sposób — przez interfejs API REST, MCP lub import pakietu przepływu pracy — która całkowicie pomija to ustawienie, domyślnie też wykonuje teraz podgląd zamiast rzeczywistego księgowania.
:::

## Autoryzowanie projektu do księgowania

Uruchomienie przepływu pracy księguje w ERP jako projekt, a nie jako osoba, która je rozpoczęła. Aby uruchomienie mogło księgować, projekt potrzebuje autoryzacji dla każdego połączenia ERP i środowiska, z których korzystają jego kroki księgowania. Bez niej krok kończy się błędem „This project isn't authorized to post to connection …”, z podaniem połączenia i środowiska. Kroki **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** i **Call SAP RFC** jej nie wymagają.

Aby autoryzować projekt, otwórz jego stronę główną i wybierz **Autoryzacje zapisu ERP** w sekcji **Księgowanie ERP**. Każdy wiersz to jedno połączenie w jednym środowisku. Zaznacz **Autoryzowano**, aby pozwolić projektowi księgować w tym miejscu, lub odznacz, aby to cofnąć. **Autoryzowane przez** i **Autoryzowano o** pokazują, kto ostatnio autoryzował i kiedy.

- Przycisk jest widoczny dla Architektów projektu i administratorów obszaru roboczego, ale autoryzację może zmienić tylko Architekt i tylko wtedy, gdy projekt jest odblokowany. Administrator obszaru roboczego, który nie jest Architektem, może najpierw dodać siebie jako Architekta.
- Zaznaczenie wiersza w celu autoryzowania lub cofnięcia autoryzacji nie przeładowuje listy: pozycja przewijania i wybrane sortowanie kolumn pozostają bez zmian. Rozmiar okna można zmieniać, a uwaga o projektach publicznych jest zawijana w całości.
- Aby autoryzować połączenie, musisz też mieć do niego uprawnienia do zapisu: jesteś jego właścicielem albo jest udostępnione Tobie imiennie lub przez jedną z Twoich grup zabezpieczeń. Połączenie ustawione na **Wszyscy członkowie obszaru roboczego** się nie liczy.
- Projekt ustawiony na **Wszyscy członkowie obszaru roboczego** jest autoryzowany jak każdy inny. Każdy członek jest jego Architektem, więc każdy członek z uprawnieniami do zapisu w połączeniu może autoryzować projekt do jego użycia. Po autoryzacji każdy członek może księgować w tym połączeniu z przepływów pracy projektu, a okno informuje o tym nad siatką.
- Skopiowany projekt lub projekt utworzony z archiwum projektu zaczyna bez żadnych autoryzacji. Autoryzuj kopię, zanim zacznie księgować.

## Śledzenie stanu kroku

Gdy przepływ pracy jest uruchomiony, każdy krok ma ikonę stanu pokazującą, na jakim etapie się znajduje, wraz z czasem jego trwania. Najedź kursorem na ikonę, aby zobaczyć komunikat, który za nią stoi.

| Stan | Co oznacza |
|---|---|
| Oczekuje | Krok jest w kolejce i jeszcze się nie rozpoczął. |
| Uruchomiony | Krok pracuje, a jego czas trwania rośnie na bieżąco. |
| Ukończony | Krok zakończył się pomyślnie. |
| Ostrzeżenie | Krok się zakończył, ale zgłosił coś wartego przeczytania w [dzienniku przepływu pracy](/pl/guides/workflows/viewing-workflow-log/). |
| Błąd | Krok zakończył się niepowodzeniem. Zobacz [Zarządzanie błędami kroków](/pl/guides/workflows/managing-step-errors/). |
| Pominięty | Krok został pominięty — jest wyłączony albo nie zostały spełnione jego warunki uruchomienia. Zobacz [Pomijanie kroków w przepływie pracy](/pl/guides/workflows/skip-steps-in-a-workflow/). |
| Kontynuowany | Krok zakończył się niepowodzeniem, ale jest ustawiony na kontynuowanie mimo błędu, więc przepływ pracy działał dalej. Zobacz [Kontynuowanie mimo błędu](/pl/guides/workflows/continue-on-error/). |
| Zatrzymany | Uruchomienie zostało zatrzymane, zanim krok mógł się zakończyć. |
| Porzucony | Wykonywanie kroku zostało przerwane, więc nigdy się nie zakończy. Wznów uruchomienie albo uruchom przepływ pracy ponownie. |

Otwarty widok przepływu pracy odświeża się automatycznie w miarę postępu uruchomienia, więc wyświetlane stany pozostają aktualne bez przeładowywania strony.

### Porzucone kroki

Krok jest oznaczany jako **porzucony**, gdy to, co go wykonywało, zniknęło w trakcie uruchomienia — najczęściej dlatego, że ktoś nacisnął **Zatrzymaj**, albo dlatego, że uruchomienie przerwały prace konserwacyjne platformy. Czas trwania kroku przestaje rosnąć, a podpowiedź stanu wyjaśnia, co się stało.

Porzucony krok nie został ukończony i nie wytworzył żadnych danych wyjściowych. Nie jest to wolny krok ani problem z Twoimi danymi czy konfiguracją.

Aby wrócić do pracy, [**Wznów**](#wstrzymywanie-zatrzymywanie-i-wznawianie) uruchomienie — porzucony krok zostanie uruchomiony ponownie — albo uruchom ponownie cały przepływ pracy. Obie metody są bezpieczne.

### Przerwane kroki

Jeśli serwer wykonujący krok zostanie utracony w trakcie uruchomienia, PlaidCloud automatycznie uruchamia krok ponownie, gdy bezpiecznie jest go powtórzyć: krok, który zastępuje swoje dane wyjściowe, kończy z takim samym wynikiem jak pojedyncze czyste uruchomienie, więc nie masz niczego do sprawdzania.

Krok, którego nie można bezpiecznie powtórzyć, nie jest uruchamiany ponownie. Kończy się jednorazowo komunikatem **Przerwano**, ponieważ drugie uruchomienie mogłoby zduplikować to, co zapisała pierwsza próba. Kroki zapisujące dane wyjściowe z `{date}` w nazwie lub ścieżce są uznawane za niebezpieczne do powtórzenia, ponieważ ponowne uruchomienie mogłoby trafić na inną datę. Aby odzyskać stan, sprawdź w miejscu docelowym kroku, co zapisała pierwsza próba, w razie potrzeby to wyczyść, a następnie [uruchom krok ponownie](/pl/guides/workflows/running-one-step-in-a-workflow/) lub **Wznów** uruchomienie.

## Wstrzymywanie, zatrzymywanie i wznawianie

Gdy przepływ pracy jest uruchomiony, możesz go wstrzymać (**Wstrzymaj**), aby kroki w toku się zakończyły, a nowe kroki czekały, albo zatrzymać (**Zatrzymaj**), co anuluje kroki w kolejce oraz wszystkie zadania importu lub eksportu, które nadal trwają.

**Wznów** podejmuje wstrzymane, zatrzymane lub zakończone błędem uruchomienie od miejsca, w którym zostało przerwane, zamiast zaczynać od nowa. Jest dostępne, gdy ostatnie uruchomienie przepływu pracy zakończyło się stanem wstrzymania, zatrzymania lub błędu.

Co oznacza „od miejsca, w którym zostało przerwane”, zależy od sposobu wykonywania przepływu pracy:

| Wykonywanie | Przy wznowieniu |
|---|---|
| Szeregowe | Rozpoczyna od kroku, który był wykonywany, gdy uruchomienie się zakończyło, i kontynuuje stamtąd. Jeśli ten krok znajduje się w grupie, Wznów podejmuje całą grupę najwyższego poziomu, która go zawiera: kroki w grupie, które już zakończyły się pomyślnie, są pomijane, pozostałe są uruchamiane, a uruchomienie kontynuuje po grupie. |
| Równoległe | Uruchamia ponownie każdy krok, który jeszcze nie zakończył się pomyślnie, i pozostawia ukończone kroki bez zmian. |
| Zaawansowane (graf) | Uruchamia ponownie węzeł, który zakończył się błędem, i wszystko, co na niego nadal czeka, a ukończone węzły pozostawia bez zmian. |

Kroki wywołujące inny przepływ pracy — **Run Model**, **Conditional Run Model** i **Loop Model** — wznawiają wywoływany przepływ pracy zamiast uruchamiać go od początku, przez dowolną liczbę poziomów zagnieżdżenia. Krok pętli wznawia iterację, która została przerwana, i pomija iteracje, które już się zakończyły.

Gdy wznawiasz przepływ pracy, który działał jako **zagnieżdżone dziecko** innego — wywołany przez krok **Run Model** w nadrzędnym — PlaidCloud oferuje **Wznów od początku łańcucha**. Samodzielne wznowienie dziecka nie może kontynuować orkiestracji rodzica, więc ta opcja wznawia rodzica najwyższego poziomu — korzeń łańcucha — i kontynuuje cały łańcuch od miejsca zatrzymania. Wznawianie przepływu pracy najwyższego poziomu pozostaje bez zmian. Początek łańcucha jest ustalany w obrębie tego samego projektu: łańcuch przechodzący do innego projektu jest wznawiany od początku części znajdującej się w projekcie.

Wznowienie zawsze kontynuuje **oryginalne** uruchomienie. Uruchamia ponownie każdy krok z tego uruchomienia, który nie zakończył się pomyślnie — krok, który zakończył się błędem lub został porzucony, jest uruchamiany ponownie, a nie traktowany jako ukończony — a samodzielne ponowne uruchomienie pojedynczego kroku w międzyczasie nie zmienia tego, co Wznów podejmie następnie.

Wznowione uruchomienie jest zapisywane jako **nowe uruchomienie** w historii uruchomień przepływu pracy i zawiera tylko kroki, które ponownie uruchomiło. Oryginalne uruchomienie zachowuje własny wpis w historii.

:::note
Krok pętli dopasowuje swoje ukończone iteracje według wartości zmiennych. Jeśli dane, po których pętla iteruje, zmieniły się między oryginalnym uruchomieniem a wznowieniem, iteracje, których nie można już dopasować, są uruchamiane ponownie zamiast pomijane.
:::
