---
title: Rozwiązywanie problemów z PlaidXL
description: Rozwiązania typowych problemów z PlaidXL — dodatek nie pojawia się na wstążce, okno logowania się nie otwiera, brakujące obszary robocze lub projekty, tabele wyświetlane na czerwono, wolne pobieranie i błędy w formułach PlaidXL.
sidebar:
  label: Rozwiązywanie problemów
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Karty PlaidCloud nie ma na wstążce

- Zamknij wszystkie okna Excela i uruchom go ponownie. Nowo zainstalowany dodatek często pojawia się dopiero po ponownym uruchomieniu.
- Otwórz **Insert → My Add-ins** i wybierz **PlaidCloud**.
- Sprawdź, czy używasz Excela na komputery dla Microsoft 365 albo Excela 2021 lub nowszego. Zobacz [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/).
- Jeśli Twoja organizacja zarządza dodatkami, zapytaj administratora Microsoft 365, czy dodatek **PlaidCloud** został dla Ciebie wdrożony.

## Okno logowania się nie otwiera

Po kliknięciu **Sign In** Excel pyta, czy wyświetlić okno podręczne. Zezwól na nie. Jeśli odrzucono monit, kliknij **Sign In** ponownie.

Jeśli okno się otwiera, ale nie można dokończyć logowania, spróbuj zalogować się do PlaidCloud w przeglądarce przy użyciu tego samego adresu e-mail. Problem występujący tam — wygasłe hasło lub urządzenie dwuskładnikowe, którego już nie ma — trzeba najpierw rozwiązać w PlaidCloud. Zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Obszar roboczy nie jest wymieniony

Lista **Select a workspace** zawiera obszary robocze, do których należy Twój adres e-mail. Jeśli któregoś brakuje, sprawdź, czy wpisano ten sam adres e-mail, którego używasz w tym obszarze roboczym, a następnie poproś administratora obszaru roboczego o potwierdzenie, że jesteś jego członkiem. Zobacz [Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/).

Aby przejść do innego obszaru roboczego, do którego należysz, otwórz menu konta i wybierz **Switch workspace**.

## Brakuje projektu, tabeli lub wymiaru

PlaidXL pokazuje to, co Twoje konto widzi w PlaidCloud. Jeśli brakuje projektu, poproś jego właściciela o przyznanie dostępu. Jeśli brakuje tabeli, sprawdź, czy istnieje w wybranym projekcie i czy załadowano do niej dane — tabela, do której nigdy nic nie zapisano, po wybraniu pokazuje komunikat **Unable to get table metadata**.

Foldery na listach projektów, tabel i wymiarów są początkowo zwinięte. Wpisz część nazwy w polu filtru na górze listy, aby znaleźć element wewnątrz folderu.

## Tabela jest wyświetlana na czerwono

Tabela ma więcej wierszy lub kolumn, niż mieści arkusz Excela. Wybierz **Zaawansowane**, aby przefiltrować wiersze, i wyczyść niepotrzebne kolumny, aż tabela się zmieści. Zobacz [Tabele wyświetlane na czerwono](/pl/reference/cli/plaidxl/retrieve/#tabele-wyświetlane-na-czerwono).

## Pobieranie jest wolne

Excel działa najwolniej z szerokimi tabelami. Wyczyść pola wyboru niepotrzebnych kolumn i przefiltruj wiersze za pomocą **Zaawansowane**. Pobieranie tylko danych, z którymi pracujesz, jest szybsze i daje mniejszy skoroszyt.

## Formuła pokazuje błąd

| Co widzisz | Co sprawdzić |
|---|---|
| `#SPILL!` | Coś znajduje się w komórkach, których potrzebuje wynik. Wyczyść komórki pod formułą lub obok niej. |
| `#NAME?` | Excel nie rozpoznaje funkcji. Sprawdź, czy PlaidXL jest zainstalowany — karta **PlaidCloud** jest na wstążce — i sprawdź pisownię względem [listy funkcji](/pl/reference/cli/plaidxl/functions/). |
| Błąd z funkcji `PLAIDXL` | Sprawdź, czy jesteś zalogowany i wybrano właściwy projekt, a następnie sprawdź każdą nazwę tabeli, kolumny, wymiaru i węzła względem PlaidCloud — nazwy muszą być dokładnie takie same. |
| `CELL` zgłasza, że nie znaleziono kolumny filtra | Pierwszy argument `DIMENSION_REPR` to kolumna tabeli, a nie wymiar. Użyj dokładnie nazwy kolumny tabeli. Zobacz [Wartości](/pl/reference/cli/plaidxl/functions/#wartości). |
| `#VALUE!` z `CELL` lub `CELLS` | Najedź kursorem na komórkę, aby przeczytać przyczynę podaną przez PlaidCloud, np. nieznana kolumna, węzeł, który nie istnieje lub nie ma elementów, albo problem z obliczeniem wartości. Sprawdź nazwy względem PlaidCloud. |
| `CELL` zwraca nieoczekiwaną sumę | Węzeł jest agregowany tylko w kolumnie powiązanej z jego wymiarem; w każdej innej kolumnie musi dokładnie pasować do wartości. Sprawdź kolumnę i węzeł każdego filtra. |
| Wartości nie zmieniają się po zmianie danych lub projektu | Wymuś pełne przeliczenie — w systemie Windows **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` zwraca błąd | Użyj jednej z wartości `sum`, `mean`, `median`, `min`, `max`, `std` lub `var`, małymi literami. |

## Formuły zwracają dane z innego projektu

Funkcje PlaidXL odczytują dane z projektu powiązanego ze skoroszytem. Otwórz okienko zadań w tym skoroszycie, wybierz projekt, dla którego zbudowano raport, a następnie wymuś pełne przeliczenie. Każdy skoroszyt ma własny projekt, więc wybranie projektu w innym skoroszycie nie zmienia tego. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Tabele z innego obszaru roboczego są pomijane

Po zmianie obszaru roboczego okienko zadań informuje, ile śledzonych tabel należy do innego obszaru roboczego i jest pomijanych przez **Refresh All Tables**. Pobierz każdą tabelę ponownie w bieżącym obszarze roboczym, aby ją powiązać.

## Zapis jest odrzucony lub wstrzymany

| Co widzisz | Co zrobić |
|---|---|
| W tabeli są puste wiersze | Dwa lub więcej pustych wierszy z rzędu, pod którymi są dane, wstrzymują zapis. Usuń puste wiersze lub wypełnij je, a następnie zapisz ponownie. |
| Tabela zmieniła się od czasu pobrania | Ktoś inny zapisał tabelę w PlaidCloud. Pobierz ją ponownie i zastosuj swoje zmiany jeszcze raz. |
| Nie można przekonwertować wartości | Nic nie jest zapisywane, a wiersze są wymienione. Popraw wartości tak, aby pasowały do typu danych kolumny. |
| Arkusz nie jest powiązany z tabelą | Najpierw pobierz tabelę do arkusza. **Save to PlaidCloud…** pojawia się tylko dla tabel pobranych do aktywnego arkusza. |

Aby cofnąć zapis, kliknij **Restore previous version** w komunikacie potwierdzenia albo otwórz tabelę w PlaidCloud i wybierz wersję sprzed zapisu w menu **As of**. Punkt przywracania jest przechowywany przez 7 dni. Zobacz [Zapisz tabelę w PlaidCloud](/pl/reference/cli/plaidxl/retrieve/#zapisz-tabelę-w-plaidcloud).

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/)
- [Logowanie do PlaidXL](/pl/reference/cli/plaidxl/connect/)
- [Uzyskiwanie pomocy](/pl/guides/support/getting-help/) — otwórz zgłoszenie do pomocy technicznej
