---
title: Rozwiązywanie problemów z PlaidXL
description: Rozwiązania typowych problemów z PlaidXL — dodatek nieobecny na wstążce, okno logowania, które się nie otwiera, brakujące obszary robocze lub projekty, tabele wyświetlane na czerwono, wolne pobieranie, błędy w formułach i metrykach PlaidXL, wpisane wartości, które nie są zapisywane, oraz zapisy, które się zatrzymują.
sidebar:
  label: Rozwiązywanie problemów
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Karty PlaidCloud nie ma na wstążce

- Zamknij wszystkie okna Excela i uruchom go ponownie. Nowo zainstalowany dodatek często pojawia się dopiero po ponownym uruchomieniu.
- Otwórz **Insert → My Add-ins** i wybierz **PlaidCloud**.
- Sprawdź, czy używasz Excela na komputerze w wersji dla Microsoft 365 albo Excela 2021 lub nowszego. Zobacz [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/).
- Jeśli Twoja organizacja zarządza dodatkami, zapytaj administratora Microsoft 365, czy dodatek **PlaidCloud** został dla Ciebie wdrożony.

## Okno logowania się nie otwiera

Gdy klikniesz **Sign In**, Excel pyta, czy wyświetlić okno podręczne. Zezwól na to. Jeśli odrzuciłeś ten monit, kliknij **Sign In** ponownie.

Jeśli okno się otwiera, ale nie możesz dokończyć logowania, spróbuj zalogować się do PlaidCloud w przeglądarce, używając tego samego adresu e-mail. Problem w tamtym miejscu — wygasłe hasło albo urządzenie dwuskładnikowe, którego już nie masz — trzeba najpierw naprawić w PlaidCloud. Zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Obszar roboczy nie jest wymieniony

Lista **Select a workspace** zawiera obszary robocze, do których należy Twój adres e-mail. Jeśli któregoś brakuje, sprawdź, czy wpisano ten sam adres e-mail, którego używasz w tym obszarze roboczym, a następnie poproś administratora obszaru roboczego o potwierdzenie, że jesteś jego członkiem. Zobacz [Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/).

Aby przejść do innego obszaru roboczego, do którego należysz, otwórz menu konta i wybierz **Switch workspace**.

## Brakuje projektu, tabeli lub wymiaru

PlaidXL pokazuje to, co Twoje konto widzi w PlaidCloud. Jeśli brakuje projektu, poproś jego właściciela o dostęp. Jeśli brakuje tabeli, sprawdź, czy istnieje w wybranym projekcie i czy zawiera wczytane dane — tabela, do której nigdy nie zapisano danych, po wybraniu pokazuje **Unable to get table metadata**.

Foldery na listach projektów, tabel i wymiarów są domyślnie zwinięte. Wpisz fragment nazwy w polu filtra u góry listy, aby znaleźć element w folderze.

## Tabela jest wyświetlana na czerwono

Tabela ma więcej wierszy lub kolumn, niż mieści arkusz Excela, albo PlaidCloud nie może podać jej rozmiaru. Możesz ją pobrać, a wiersze, które się nie mieszczą, są kontynuowane na kolejnych arkuszach, ale tabeli podzielonej na arkusze nie można zapisać. Wybierz **Zaawansowane**, aby przefiltrować wiersze, i wyczyść zaznaczenie niepotrzebnych kolumn, aż tabela się zmieści. Zobacz [Tabele wyświetlane na czerwono](/pl/reference/cli/plaidxl/retrieve/#tabele-wyświetlane-na-czerwono).

## Pobieranie jest wolne

Excel działa najwolniej z szerokimi tabelami. Wyczyść pola wyboru kolumn, których nie potrzebujesz, i przefiltruj wiersze za pomocą **Zaawansowane**. Pobieranie tylko danych, z którymi pracujesz, jest szybsze i daje mniejszy skoroszyt.

## Formuła pokazuje błąd

| Co widzisz | Co sprawdzić |
|---|---|
| `#SPILL!` | Coś znajduje się w komórkach potrzebnych na wynik. Wyczyść komórki poniżej lub obok formuły. |
| `#NAME?` | Excel nie rozpoznaje funkcji. Sprawdź, czy PlaidXL jest zainstalowany — karta **PlaidCloud** jest na wstążce — oraz pisownię na [liście funkcji](/pl/reference/cli/plaidxl/functions/). |
| Błąd z funkcji `PLAIDXL` | Sprawdź, czy jesteś zalogowany i wybrano właściwy projekt, a następnie porównaj z PlaidCloud nazwy wszystkich tabel, kolumn, wymiarów i węzłów — nazwy muszą być zgodne dokładnie. |
| `CELL` zgłasza, że nie znaleziono kolumny filtra | Pierwszym argumentem `DIMENSION_REPR` jest kolumna tabeli, a nie wymiar. Użyj dokładnej nazwy kolumny tabeli. Zobacz [Wartości](/pl/reference/cli/plaidxl/functions/#wartości). |
| `#VALUE!` z `METRIC` lub `METRIC_BREAKDOWN` | Najedź kursorem na komórkę, aby przeczytać przyczynę. Zobacz [Błędy metryk](/pl/reference/cli/plaidxl/functions/#błędy-metryk). |
| `#VALUE!` z `CELL` lub `CELLS` | Najedź kursorem na komórkę, aby przeczytać przyczynę podaną przez PlaidCloud, taką jak nieznana kolumna, węzeł, który nie istnieje lub nie ma elementów, albo problem z obliczeniem wartości. Porównaj nazwy z PlaidCloud. |
| `CELL` zwraca nieoczekiwaną sumę | Węzeł agreguje się tylko w kolumnie powiązanej z jego wymiarem; w każdej innej kolumnie musi dokładnie odpowiadać wartości. Sprawdź kolumnę i węzeł każdego filtra. |
| Wartości nie zmieniają się po zmianie danych lub projektu | Kliknij **Recalculate PlaidXL formulas** w menu **Odśwież** na wstążce. |
| `MEASURE_TYPE` zwraca błąd | Użyj jednej z wartości `sum`, `mean`, `median`, `min`, `max`, `std` lub `var`, małymi literami. |

## Formuły zwracają dane z innego projektu

Funkcje PlaidXL odczytują dane z projektu powiązanego ze skoroszytem. Otwórz okienko zadań w tym skoroszycie, wybierz projekt, dla którego zbudowano raport, a następnie kliknij **Recalculate PlaidXL formulas** w menu **Odśwież** na wstążce. Każdy skoroszyt ma własny projekt, więc wybór projektu w innym skoroszycie nie zmienia tego. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Tabele z innego obszaru roboczego są pomijane

Po przełączeniu obszaru roboczego **Refresh All Tables** informuje, że tabele lub wymiary z innego obszaru roboczego w tym skoroszycie nie zostały odświeżone, i nie są wymienione w sekcji **On this sheet**. Pobierz każdą tabelę ponownie w bieżącym obszarze roboczym, aby ją powiązać.

## Wpisana wartość nie jest zapisywana

Gdy wpisujesz nad `CELL`, okienko zadań podaje, co zapisało, i wymienia to, czego nie zapisało, wraz z przyczyną. Zobacz [Wpisywanie wartości do PlaidCloud](/pl/reference/cli/plaidxl/write-values/).

| Co widzisz | Co zrobić |
|---|---|
| Wpisaną wartość przyjmuje tylko komórka zawierająca wyłącznie jedną formułę `PLAIDXL.CELL` | Wpisz nad komórką, której formuła jest pojedynczą `CELL`, ewentualnie pomnożoną, podzieloną lub zanegowaną. |
| Argumentu nie można tu odczytać | Argumenty `CELL` muszą być komórkami lub tekstem, a nie innymi obliczeniami. |
| Metoda rozdzielania, kształt lub blokada dotyczy tylko sum | Kody takie jak `E1200`, `1200 like FY2025` i `H` działają tylko w komórkach **suma**. W pozostałych wpisz zwykłą liczbę. |
| Wszystkie elementy zablokowane | Zwolnij blokadę za pomocą `H`, a następnie wpisz wartość ponownie. |
| Obszar roboczy nie przyjmuje jeszcze wartości wpisanych w Excelu | Poproś administratora o aktualizację obszaru roboczego. |

## Zapis jest odrzucony lub zatrzymany

Zapis następuje natychmiast i rzadko się zatrzymuje. Zatrzymuje się, gdy:

| Co widzisz | Co zrobić |
|---|---|
| Wiersz nagłówka nie odpowiada już pobranym kolumnom | Przywróć nagłówek do postaci z pobrania albo pobierz tabelę ponownie. |
| Wartości nie można przekonwertować | Nic nie jest zapisywane, a wiersze są wymienione. Popraw wartości, aby odpowiadały typowi danych kolumny. |
| Tabela jest kontynuowana na innych arkuszach | Tabeli podzielonej na arkusze nie można zapisać. Pobierz ją z filtrem, aby mieściła się na jednym arkuszu. |
| Tabelę pobrano z filtrem, którego zapis nie może zachować | Pobierz ją ponownie z filtrem złożonym z reguł **równa się** i **należy do** połączonych operatorem **AND** albo bez filtra. |
| Wiersze są poza Twoim dostępem do wierszy | Nic nie jest zapisywane. Usuń te wiersze albo poproś Architekta projektu o ich zapisanie. |
| Arkusz nie jest powiązany z tabelą | Najpierw pobierz tabelę na arkusz. Na liście **On this sheet** są wymienione tylko tabele pobrane na aktywny arkusz. |

Aby cofnąć zapis, kliknij **Cofnij** w komunikacie albo **Undo last write** na wstążce. Punkt przywracania jest przechowywany przez 7 dni. Zobacz [Zapisywanie tabeli do PlaidCloud](/pl/reference/cli/plaidxl/retrieve/#zapisz-tabelę-do-plaidcloud).

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/)
- [Logowanie do PlaidXL](/pl/reference/cli/plaidxl/connect/)
- [Uzyskiwanie pomocy](/pl/guides/support/getting-help/) — zgłoś zgłoszenie do pomocy technicznej
