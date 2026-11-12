---
title: Rozwiązywanie problemów z PlaidXL
description: Rozwiązania typowych problemów z PlaidXL — dodatek nie pojawia się na wstążce, okno logowania się nie otwiera, brakujące obszary robocze lub projekty, tabele wyświetlane na czerwono, wolne pobieranie, błędy w formułach i metrykach PlaidXL, wpisane wartości, które nie są zapisywane, oraz zapisy, które się zatrzymują.
sidebar:
  label: Rozwiązywanie problemów
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Karty PlaidCloud nie ma na wstążce

- Zamknij wszystkie okna programu Excel i uruchom go ponownie. Nowo zainstalowany dodatek często pojawia się dopiero po ponownym uruchomieniu.
- Otwórz **Wstawianie → Moje dodatki** i wybierz **PlaidCloud**.
- Sprawdź, czy używasz programu Excel na komputer dla Microsoft 365 albo Excel 2021 lub nowszego. Zobacz [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/).
- Jeśli Twoja organizacja zarządza dodatkami, zapytaj administratora Microsoft 365, czy dodatek **PlaidCloud** został Ci wdrożony.

## Okno podręczne logowania się nie otwiera

Po kliknięciu **Sign In** program Excel pyta, czy wyświetlić okno podręczne. Zezwól na to. Jeśli odrzucono monit, kliknij **Sign In** ponownie.

Jeśli okno się otwiera, ale nie możesz dokończyć logowania, spróbuj zalogować się do PlaidCloud w przeglądarce z tym samym adresem e-mail. Problem tam — wygasłe hasło lub urządzenie uwierzytelniania dwuskładnikowego, którego już nie masz — trzeba najpierw rozwiązać w PlaidCloud. Zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Obszar roboczy nie jest wyświetlony

**Select a workspace** wyświetla obszary robocze, do których należy Twój adres e-mail. Jeśli którego brakuje, sprawdź, czy wpisano ten sam adres e-mail, którego używasz w danym obszarze roboczym, a następnie poproś administratora obszaru roboczego o potwierdzenie, że jesteś jego członkiem. Zobacz [Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/).

Aby przejść do innego obszaru roboczego, do którego należysz, otwórz menu konta i wybierz **Switch workspace**.

## Brakuje projektu, tabeli lub wymiaru

PlaidXL pokazuje to, co Twoje konto widzi w PlaidCloud. Jeśli brakuje projektu, poproś jego właściciela o udzielenie dostępu. Jeśli brakuje tabeli, sprawdź, czy istnieje w wybranym projekcie i czy załadowano do niej dane — tabela, do której nigdy nic nie zapisano, po wybraniu pokazuje **Unable to get table metadata**.

Foldery na listach projektów, tabel i wymiarów są początkowo zwinięte. Wpisz fragment nazwy w polu filtra na górze listy, aby znaleźć element wewnątrz folderu.

## Tabela jest pokazana na czerwono

Tabela ma więcej wierszy lub kolumn, niż mieści arkusz programu Excel, albo PlaidCloud nie może podać jej rozmiaru. Możesz ją pobrać, a wiersze, które się nie mieszczą, są kontynuowane w kolejnych arkuszach, ale tabeli podzielonej na kilka arkuszy nie można zapisać. Wybierz **Zaawansowane**, aby przefiltrować wiersze, i wyczyść niepotrzebne kolumny, aż tabela się zmieści. Zobacz [Tabele wyświetlane na czerwono](/pl/reference/cli/plaidxl/retrieve/#tabele-pokazane-na-czerwono).

## Pobieranie jest wolne

Excel najwolniej radzi sobie z szerokimi tabelami. Wyczyść pola wyboru niepotrzebnych kolumn i przefiltruj wiersze opcją **Zaawansowane**. Pobieranie tylko danych, z którymi pracujesz, jest szybsze i daje mniejszy skoroszyt.

Duże tabele są pobierane i odświeżane znacznie szybciej w programie Excel w przeglądarce i w aktualnym programie Excel na komputery. Starsze wersje programu Excel nadal działają, tylko bez przyspieszenia.

Jeśli panel wyświetla **PlaidXL was updated — reload the pane**, zamknij panel zadań, otwórz go ponownie i pobierz dane jeszcze raz. Po aktualizacji PlaidXL panel pobiera nową wersję przy następnym załadowaniu.

Jeśli pobieranie kończy się komunikatem **This PlaidCloud workspace needs an update for PlaidXL**, poproś administratora o zaktualizowanie obszaru roboczego do aktualnego wydania PlaidCloud.

## Formuła pokazuje błąd

| Co widzisz | Co sprawdzić |
|---|---|
| `#SPILL!` | Coś znajduje się w komórkach, których potrzebuje wynik. Wyczyść komórki poniżej formuły lub obok niej. |
| `#NAME?` | Excel nie rozpoznaje funkcji. Sprawdź, czy PlaidXL jest zainstalowany — karta **PlaidCloud** jest na wstążce — i sprawdź pisownię z [listą funkcji](/pl/reference/cli/plaidxl/functions/). |
| Błąd z funkcji `PLAIDXL` | Sprawdź, czy jesteś zalogowany i wybrano właściwy projekt, a następnie porównaj z PlaidCloud nazwy każdej tabeli, kolumny, wymiaru i węzła — nazwy muszą być dokładnie takie same. |
| `CELL` zgłasza, że nie znaleziono kolumny filtra | Pierwszym argumentem `DIMENSION_REPR` jest kolumna tabeli, a nie wymiar. Użyj dokładnej nazwy kolumny tabeli. Zobacz [Wartości](/pl/reference/cli/plaidxl/functions/#wartości). |
| `#VALUE!` z `METRIC` lub `METRIC_BREAKDOWN` | Najedź kursorem na komórkę, aby przeczytać przyczynę. Zobacz [Błędy metryk](/pl/reference/cli/plaidxl/functions/#błędy-metryk). |
| `#VALUE!` z metryki: **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | Obszar roboczy wymaga aktualizacji, zanim metryka będzie mogła łączyć element hierarchii alternatywnej z innymi elementami. Zapytaj administratora. Pozostałe komórki w tym samym przeliczeniu nadal zwracają odpowiedzi. |
| `#VALUE!` z `CELL` lub `CELLS` | Najedź kursorem na komórkę, aby przeczytać przyczynę podaną przez PlaidCloud, taką jak nieznana kolumna, węzeł, który nie istnieje lub nie ma elementów, albo problem z obliczeniem wartości. Porównaj nazwy z PlaidCloud. |
| `CELL` zwraca nieoczekiwaną sumę | Węzeł jest agregowany tylko w kolumnie powiązanej z jego wymiarem; w każdej innej kolumnie musi dokładnie pasować do wartości. Sprawdź kolumnę i węzeł każdego filtra. |
| Wartości nie zmieniają się po zmianie danych lub projektu | Kliknij **Recalculate PlaidXL formulas** w menu **Odśwież** na wstążce. |
| `MEASURE_TYPE` zwraca błąd | Użyj jednej z wartości `sum`, `mean`, `median`, `min`, `max`, `std` lub `var`, małymi literami. |

## Formuły zwracają dane z innego projektu

Funkcje PlaidXL odczytują dane z projektu powiązanego ze skoroszytem. Otwórz panel zadań w tym skoroszycie, wybierz projekt, dla którego zbudowano raport, a następnie kliknij **Recalculate PlaidXL formulas** w menu **Odśwież** na wstążce. Każdy skoroszyt ma własny projekt, więc wybór projektu w innym skoroszycie nie zmienia tego. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Tabele z innego obszaru roboczego są pomijane

Po zmianie obszaru roboczego **Refresh All Tables** informuje, że tabele lub wymiary z innego obszaru roboczego w tym skoroszycie nie zostały odświeżone, i nie są one wyświetlane w sekcji **On this sheet**. Pobierz każdą tabelę ponownie w bieżącym obszarze roboczym, aby ją powiązać.

## Wpisana wartość nie jest zapisywana

Gdy wpisujesz wartość nad `CELL`, panel zadań informuje, co zapisał, i wymienia wszystko, czego nie zapisał, wraz z przyczyną. Zobacz [Wpisywanie wartości do PlaidCloud](/pl/reference/cli/plaidxl/write-values/).

| Co widzisz | Co zrobić |
|---|---|
| Wpisaną wartość przyjmuje tylko komórka zawierająca jedno `PLAIDXL.CELL` | Wpisz wartość nad komórką, której formuła jest pojedynczym `CELL`, ewentualnie mnożonym, dzielonym lub z odwróconym znakiem. |
| Argumentu nie można tu odczytać | Argumenty `CELL` muszą być komórkami lub tekstem, a nie innymi obliczeniami. |
| Metoda rozkładu, kształt lub blokada dotyczą wyłącznie sum | Kody takie jak `E1200`, `1200 like FY2025` i `H` działają tylko w komórkach typu **sum**. W pozostałych wpisz zwykłą liczbę. |
| Wszystkie elementy są zablokowane | Zwolnij blokadę kodem `H`, a następnie wpisz wartość ponownie. |
| Obszar roboczy nie przyjmuje jeszcze wartości wpisywanych w programie Excel | Poproś administratora o zaktualizowanie obszaru roboczego. |

## Zapis jest odrzucony lub zatrzymany

Zapis następuje od razu i rzadko się zatrzymuje. Zatrzymuje się, gdy:

| Co widzisz | Co zrobić |
|---|---|
| Wiersz nagłówka nie odpowiada już pobranym kolumnom | Przywróć nagłówek do stanu z pobrania albo pobierz tabelę ponownie. |
| Wartości nie można skonwertować | Nic nie jest zapisywane, a wiersze są wymienione. Popraw wartości, aby odpowiadały typowi danych kolumny. |
| Tabela jest kontynuowana w innych arkuszach | Tabeli podzielonej na kilka arkuszy nie można zapisać. Pobierz ją z filtrem, aby mieściła się w jednym arkuszu. |
| Tabelę pobrano z filtrem, którego zapis nie może uwzględnić | Pobierz ją ponownie z filtrem złożonym z reguł **równa się** i **in** połączonych operatorem **AND** albo bez filtra. |
| Wiersze są poza Twoim dostępem do wierszy | Nic nie jest zapisywane. Usuń te wiersze, a następnie zapisz ponownie. |
| Kolumny zawierają tekst dłuższy niż 32 767 znaków komórki programu Excel | Excel wyświetla tekst w postaci obciętej, a zapis obciąłby go także w PlaidCloud, więc zapis jest dla tej tabeli wyłączony. Pobierz tabelę bez tych kolumn, aby ją zapisać. |
| Tabela została zapisana tylko częściowo | Excel odrzucił część ostatniego odświeżenia. Odśwież tabelę, a następnie ją zapisz. |
| Arkusz nie jest powiązany z tabelą | Najpierw pobierz tabelę do arkusza. Tylko tabele pobrane do aktywnego arkusza są wyświetlane w sekcji **On this sheet**. |

Aby cofnąć zapis, kliknij **Cofnij** w komunikacie albo **Undo last write** na wstążce. Każdy zapis zachowuje własny punkt przywracania przez 7 dni, więc możesz cofnąć dowolny zapis przez maksymalnie 7 dni od jego wykonania. Zobacz [Zapisywanie tabeli w PlaidCloud](/pl/reference/cli/plaidxl/retrieve/#zapisywanie-tabeli-w-plaidcloud).

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/)
- [Logowanie do PlaidXL](/pl/reference/cli/plaidxl/connect/)
- [Uzyskiwanie pomocy](/pl/guides/support/getting-help/) — otwórz zgłoszenie do pomocy technicznej
