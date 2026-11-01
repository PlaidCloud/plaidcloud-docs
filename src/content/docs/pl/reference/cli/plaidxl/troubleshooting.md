---
title: Rozwiązywanie problemów z PlaidXL
description: Rozwiązania typowych problemów z PlaidXL — brak dodatku na wstążce, nieotwierające się okno logowania, brakujące obszary robocze lub projekty, tabele wyświetlane na czerwono, wolne pobieranie i błędy w formułach PlaidXL.
sidebar:
  label: Rozwiązywanie problemów
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Karty PlaidCloud nie ma na wstążce

- Zamknij wszystkie okna Excela i uruchom Excela ponownie. Nowo zainstalowany dodatek często pojawia się dopiero po ponownym uruchomieniu.
- Otwórz **Wstawianie → Moje dodatki** i wybierz **PlaidCloud**.
- Sprawdź, czy używasz programu Excel na komputer dla Microsoft 365 albo Excela 2021 lub nowszego. Zobacz [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/).
- Jeśli Twoja organizacja zarządza dodatkami, zapytaj administratora Microsoft 365, czy dodatek **PlaidCloud** jest dla Ciebie wdrożony.

## Okno logowania się nie otwiera

Po kliknięciu **Sign In** Excel pyta, czy wyświetlić okno podręczne. Zezwól na to. Jeśli odrzucono monit, kliknij **Sign In** ponownie.

Jeśli okno się otwiera, ale nie możesz dokończyć logowania, spróbuj zalogować się do PlaidCloud w przeglądarce, używając tego samego adresu e-mail. Problem w tym miejscu — wygasłe hasło lub urządzenie do uwierzytelniania dwuskładnikowego, którego już nie masz — trzeba najpierw naprawić w PlaidCloud. Zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Obszar roboczy nie jest wyświetlany

**Select a workspace** wyświetla obszary robocze, do których należy Twój adres e-mail. Jeśli którego brakuje, sprawdź, czy wpisano ten sam adres e-mail, którego używasz w tym obszarze roboczym, a następnie poproś administratora obszaru roboczego o potwierdzenie, że jesteś jego członkiem. Zobacz [Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/).

Aby przejść do innego obszaru roboczego, do którego należysz, otwórz menu konta i wybierz **Switch workspace**.

## Brakuje projektu, tabeli lub wymiaru

PlaidXL pokazuje to, co Twoje konto widzi w PlaidCloud. Jeśli brakuje projektu, poproś jego właściciela o przyznanie dostępu. Jeśli brakuje tabeli, sprawdź, czy istnieje w wybranym projekcie i została załadowana danymi — tabela, do której nigdy nic nie zapisano, po wybraniu pokazuje **Unable to get table metadata**.

Foldery na listach projektów, tabel i wymiarów są początkowo zwinięte. Wpisz część nazwy w polu filtru na górze listy, aby znaleźć element wewnątrz folderu.

## Tabela jest wyświetlana na czerwono

Tabela ma więcej wierszy lub kolumn, niż mieści arkusz Excela. Wybierz **Advanced**, aby przefiltrować wiersze, i wyczyść niepotrzebne kolumny, aż tabela się zmieści. Zobacz [Tabele wyświetlane na czerwono](/pl/reference/cli/plaidxl/retrieve/#tabele-wyświetlane-na-czerwono).

## Pobieranie jest wolne

Excel działa najwolniej z szerokimi tabelami. Wyczyść pola wyboru kolumn, których nie potrzebujesz, i przefiltruj wiersze za pomocą **Advanced**. Pobieranie tylko danych, z którymi pracujesz, jest szybsze i daje mniejszy skoroszyt.

## Formuła wyświetla błąd

| Co widzisz | Co sprawdzić |
|---|---|
| `#SPILL!` | Coś znajduje się w komórkach potrzebnych na wynik. Wyczyść komórki poniżej lub obok formuły. |
| `#NAME?` | Excel nie rozpoznaje funkcji. Sprawdź, czy PlaidXL jest zainstalowany — karta **PlaidCloud** jest na wstążce — i sprawdź pisownię w [liście funkcji](/pl/reference/cli/plaidxl/functions/). |
| Błąd z funkcji `PLAIDXL` | Sprawdź, czy jesteś zalogowany i wybrano właściwy projekt, a następnie porównaj z PlaidCloud każdą nazwę tabeli, kolumny, wymiaru i węzła — nazwy muszą dokładnie się zgadzać. |
| `CELL` zgłasza, że nie znaleziono kolumny filtru | Pierwszy argument `DIMENSION_REPR` to kolumna tabeli, a nie wymiar. Użyj dokładnej nazwy kolumny tabeli. Zobacz [Wartości](/pl/reference/cli/plaidxl/functions/#wartości). |
| `#VALUE!` z `CELL` lub `CELLS` | Najedź na komórkę, aby przeczytać przyczynę podaną przez PlaidCloud, taką jak nieznana kolumna, węzeł, który nie istnieje lub nie ma członków, albo problem z obliczeniem wartości. Porównaj nazwy z PlaidCloud. |
| `CELL` zwraca nieoczekiwaną sumę | Węzeł agreguje się tylko w kolumnie powiązanej z jego wymiarem; w każdej innej kolumnie musi dokładnie odpowiadać wartości. Sprawdź kolumnę i węzeł każdego filtru. |
| Wartości nie zmieniają się po zmianie danych lub projektu | Wymuś pełne przeliczenie — w systemie Windows **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` zwraca błąd | Użyj jednej z wartości `sum`, `mean`, `median`, `min`, `max`, `std` lub `var`, małymi literami. |

## Formuły zwracają dane z innego projektu

Funkcje PlaidXL czytają z projektu powiązanego ze skoroszytem. Otwórz okienko zadań w tym skoroszycie, wybierz projekt, dla którego zbudowano raport, a następnie wymuś pełne przeliczenie. Każdy skoroszyt ma własny projekt, więc wybranie projektu w innym skoroszycie nie zmienia tego. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Tabele z innego obszaru roboczego są pomijane

Po zmianie obszaru roboczego okienko zadań informuje, ile śledzonych tabel należy do innego obszaru roboczego i jest pomijanych przez **Refresh All Tables**. Pobierz każdą tabelę ponownie w bieżącym obszarze roboczym, aby ją powiązać.

## Zapis jest odrzucony lub zatrzymany

| Co widzisz | Co zrobić |
|---|---|
| Wiersze wewnątrz tabeli są puste | Pojedynczy pusty wiersz jest pomijany. Dwa lub więcej pustych wierszy pod rząd, z danymi poniżej, wstrzymują zapis. Usuń puste wiersze lub je wypełnij, a następnie zapisz ponownie. |
| Tabela zmieniła się od czasu jej pobrania | Ktoś inny zapisał tabelę w PlaidCloud. Pobierz ją ponownie i zastosuj swoje zmiany jeszcze raz. (PlaidCloud może to sprawdzić tylko dla niektórych typów tabel; tam, gdzie nie może, potwierdzenie ostrzega, że zmiany innych osób zostaną nadpisane.) |
| Wartości nie można przekonwertować | Nic nie jest zapisywane, a wiersze są wyświetlane na liście. Popraw wartości, aby odpowiadały typowi danych kolumny. |
| Arkusz nie jest powiązany z tabelą | Najpierw pobierz tabelę do arkusza. **Save to PlaidCloud…** pojawia się tylko dla tabel pobranych do aktywnego arkusza. |

Aby cofnąć zapis, kliknij **Restore previous version** w komunikacie potwierdzenia albo otwórz tabelę w PlaidCloud i wybierz wersję sprzed zapisu w menu **As of**. Punkt przywracania jest przechowywany przez 7 dni. Zobacz [Zapisywanie tabeli w PlaidCloud](/pl/reference/cli/plaidxl/retrieve/#zapisywanie-tabeli-w-plaidcloud).

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/)
- [Logowanie do PlaidXL](/pl/reference/cli/plaidxl/connect/)
- [Uzyskiwanie pomocy](/pl/guides/support/getting-help/) — zgłoś zgłoszenie do pomocy technicznej
