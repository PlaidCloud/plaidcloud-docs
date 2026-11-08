---
title: Rozwiązywanie problemów z PlaidXL
description: Rozwiązania typowych problemów z PlaidXL — dodatek brakujący na wstążce, okno podręczne logowania, które się nie otwiera, brakujące obszary robocze lub projekty, tabele pokazane na czerwono, wolne pobieranie, błędy w formułach PlaidXL i metrykach, wpisane wartości, które nie są zapisywane, oraz zapisy, które się zatrzymują.
sidebar:
  label: Rozwiązywanie problemów
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Karty PlaidCloud nie ma na wstążce

- Zamknij wszystkie okna programu Excel i uruchom go ponownie. Nowo zainstalowany dodatek często pojawia się dopiero po ponownym uruchomieniu.
- Otwórz **Insert → My Add-ins** i wybierz **PlaidCloud**.
- Sprawdź, czy używasz programu Excel na komputerze w wersji dla Microsoft 365 albo Excel 2021 lub nowszego. Zobacz [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/).
- Jeśli Twoja organizacja zarządza dodatkami, zapytaj administratora Microsoft 365, czy dodatek **PlaidCloud** został Ci wdrożony.

## Okno podręczne logowania się nie otwiera

Po kliknięciu **Sign In** Excel pyta, czy wyświetlić okno podręczne. Zezwól na nie. Jeśli odrzucono monit, kliknij **Sign In** ponownie.

Jeśli okno podręczne się otwiera, ale nie możesz dokończyć logowania, spróbuj zalogować się do PlaidCloud w przeglądarce tym samym adresem e-mail. Problem tam — wygasłe hasło lub urządzenie dwuskładnikowe, którego już nie masz — trzeba najpierw rozwiązać w PlaidCloud. Zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Obszar roboczy nie jest wyświetlony

**Select a workspace** wyświetla obszary robocze, do których należy Twój adres e-mail. Jeśli jednego brakuje, sprawdź, czy wpisano ten sam adres e-mail, którego używasz w tym obszarze roboczym, a następnie poproś administratora obszaru roboczego o potwierdzenie, że jesteś jego członkiem. Zobacz [Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/).

Aby przejść do innego obszaru roboczego, do którego należysz, otwórz menu konta i wybierz **Switch workspace**.

## Brakuje projektu, tabeli lub wymiaru

PlaidXL pokazuje to, co Twoje konto widzi w PlaidCloud. Jeśli brakuje projektu, poproś jego właściciela o udzielenie dostępu. Jeśli brakuje tabeli, sprawdź, czy istnieje w wybranym projekcie i czy załadowano do niej dane — tabela, do której nigdy nic nie zapisano, po zaznaczeniu pokazuje **Unable to get table metadata**.

Foldery na listach projektów, tabel i wymiarów są początkowo zwinięte. Wpisz część nazwy w polu filtra na górze listy, aby znaleźć element wewnątrz folderu.

## Tabela jest pokazana na czerwono

Tabela ma więcej wierszy lub kolumn, niż mieści arkusz programu Excel, albo PlaidCloud nie potrafi podać jej rozmiaru. Możesz ją pobrać, a wiersze, które się nie mieszczą, są kontynuowane na kolejnych arkuszach, ale tabeli rozłożonej na kilka arkuszy nie można zapisać. Zaznacz **Zaawansowane**, aby przefiltrować wiersze, i wyczyść niepotrzebne kolumny, aż tabela się zmieści. Zobacz [Tabele pokazane na czerwono](/pl/reference/cli/plaidxl/retrieve/#tabele-pokazane-na-czerwono).

## Pobieranie jest wolne

Excel jest najwolniejszy przy szerokich tabelach. Wyczyść pola wyboru kolumn, których nie potrzebujesz, i przefiltruj wiersze za pomocą **Zaawansowane**. Pobieranie tylko danych, z którymi pracujesz, jest szybsze i daje mniejszy skoroszyt.

## Formuła pokazuje błąd

| Co widzisz | Co sprawdzić |
|---|---|
| `#SPILL!` | Coś znajduje się w komórkach potrzebnych na wynik. Wyczyść komórki poniżej formuły lub obok niej. |
| `#NAME?` | Excel nie rozpoznaje funkcji. Sprawdź, czy PlaidXL jest zainstalowany — karta **PlaidCloud** jest na wstążce — i sprawdź pisownię z [listą funkcji](/pl/reference/cli/plaidxl/functions/). |
| Błąd z funkcji `PLAIDXL` | Sprawdź, czy jesteś zalogowany i wybrano właściwy projekt, a następnie sprawdź w PlaidCloud każdą nazwę tabeli, kolumny, wymiaru i węzła — nazwy muszą dokładnie się zgadzać. |
| `CELL` zgłasza, że nie znaleziono kolumny filtra | Pierwszym argumentem `DIMENSION_REPR` jest kolumna tabeli, a nie wymiar. Użyj dokładnej nazwy kolumny tabeli. Zobacz [Wartości](/pl/reference/cli/plaidxl/functions/#wartości). |
| `#VALUE!` z `METRIC` lub `METRIC_BREAKDOWN` | Najedź wskaźnikiem na komórkę, aby przeczytać przyczynę. Zobacz [Błędy metryk](/pl/reference/cli/plaidxl/functions/#błędy-metryk). |
| `#VALUE!` z metryki: **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | Obszar roboczy wymaga aktualizacji, zanim metryka będzie mogła łączyć członka hierarchii alternatywnej z innymi członkami. Skontaktuj się z administratorem. Pozostałe komórki w tym samym przeliczeniu nadal zwracają odpowiedź. |
| `#VALUE!` z `CELL` lub `CELLS` | Najedź wskaźnikiem na komórkę, aby przeczytać przyczynę podaną przez PlaidCloud, taką jak nieznana kolumna, węzeł, który nie istnieje lub nie ma członków, albo problem z obliczeniem wartości. Sprawdź nazwy w PlaidCloud. |
| `CELL` zwraca nieoczekiwaną sumę | Węzeł jest agregowany tylko w kolumnie powiązanej z jego wymiarem; w każdej innej kolumnie musi dokładnie pasować do wartości. Sprawdź kolumnę i węzeł każdego filtra. |
| Wartości nie zmieniają się po zmianie danych lub projektu | Kliknij **Recalculate PlaidXL formulas** w menu **Odśwież** na wstążce. |
| `MEASURE_TYPE` zwraca błąd | Użyj jednej z wartości `sum`, `mean`, `median`, `min`, `max`, `std` lub `var`, małymi literami. |

## Formuły zwracają dane z innego projektu

Funkcje PlaidXL czytają dane z projektu powiązanego ze skoroszytem. Otwórz okienko zadań w tym skoroszycie, wybierz projekt, dla którego zbudowano raport, a następnie kliknij **Recalculate PlaidXL formulas** w menu **Odśwież** na wstążce. Każdy skoroszyt ma własny projekt, więc wybranie projektu w innym skoroszycie nie zmienia tego. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Tabele z innego obszaru roboczego są pomijane

Po przełączeniu obszaru roboczego **Refresh All Tables** informuje, że tabele lub wymiary z innego obszaru roboczego w tym skoroszycie nie zostały odświeżone, a w obszarze **On this sheet** nie są wyświetlane. Pobierz każdą tabelę ponownie w bieżącym obszarze roboczym, aby ją powiązać.

## Wpisana wartość nie jest zapisywana

Gdy wpisujesz wartość nad formułą `CELL`, okienko zadań podaje, co zapisało, i wymienia wszystko, czego nie zapisało, wraz z przyczyną. Zobacz [Wpisywanie wartości do PlaidCloud](/pl/reference/cli/plaidxl/write-values/).

| Co widzisz | Co zrobić |
|---|---|
| Wpisaną wartość przyjmuje tylko komórka zawierająca wyłącznie jedną formułę `PLAIDXL.CELL` | Wpisz wartość nad komórką, której formuła jest pojedynczym `CELL`, ewentualnie pomnożonym, podzielonym lub z odwróconym znakiem. |
| Nie można tu odczytać argumentu | Argumentami `CELL` muszą być komórki lub tekst, a nie inne obliczenia. |
| Metoda rozłożenia, kształt lub blokada dotyczą wyłącznie sum | Kody takie jak `E1200`, `1200 like FY2025` i `H` działają tylko w komórkach **Suma**. W pozostałych wpisz zwykłą liczbę. |
| Wszyscy członkowie są zablokowani | Zwolnij blokadę za pomocą `H`, a następnie wpisz wartość ponownie. |
| Obszar roboczy nie przyjmuje jeszcze wartości wpisanych w programie Excel | Poproś administratora o aktualizację obszaru roboczego. |

## Zapis jest odrzucony lub zatrzymany

Zapis następuje od razu i rzadko się zatrzymuje. Zatrzymuje się, gdy:

| Co widzisz | Co zrobić |
|---|---|
| Wiersz nagłówka nie odpowiada już pobranym kolumnom | Przywróć nagłówek do postaci z pobrania lub pobierz tabelę ponownie. |
| Wartości nie można przekonwertować | Nic nie jest zapisywane, a wiersze są wymienione. Popraw wartości, aby odpowiadały typowi danych kolumny. |
| Tabela jest kontynuowana na innych arkuszach | Tabeli rozłożonej na kilka arkuszy nie można zapisać. Pobierz ją z filtrem, aby mieściła się na jednym arkuszu. |
| Tabelę pobrano z filtrem, którego zapis nie może zachować | Pobierz ją ponownie z filtrem złożonym z reguł **równa się** i **in** połączonych przez **AND** lub bez filtra. |
| Wiersze są poza Twoim dostępem do wierszy | Nic nie jest zapisywane. Usuń te wiersze, a następnie zapisz ponownie. |
| Arkusz nie jest powiązany z tabelą | Najpierw pobierz tabelę do arkusza. W obszarze **On this sheet** wyświetlane są tylko tabele pobrane do aktywnego arkusza. |

Aby cofnąć zapis, kliknij **Cofnij** w komunikacie lub **Undo last write** na wstążce. Każdy zapis przechowuje własny punkt przywracania przez 7 dni, więc możesz cofnąć dowolny zapis do 7 dni po jego wykonaniu. Zobacz [Zapisywanie tabeli w PlaidCloud](/pl/reference/cli/plaidxl/retrieve/#zapisywanie-tabeli-w-plaidcloud).

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/)
- [Logowanie do PlaidXL](/pl/reference/cli/plaidxl/connect/)
- [Uzyskiwanie pomocy](/pl/guides/support/getting-help/) — otwórz zgłoszenie do pomocy technicznej
