---
title: Rozwiązywanie problemów z PlaidXL
description: Rozwiązania typowych problemów z PlaidXL — dodatek nieobecny na wstążce, okno logowania, które się nie otwiera, brakujące obszary robocze lub projekty, tabele wyświetlane na czerwono, wolne pobieranie i błędy w formułach PlaidXL.
sidebar:
  label: Rozwiązywanie problemów
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## Karty PlaidCloud nie ma na wstążce

- Zamknij wszystkie okna Excela i uruchom Excela ponownie. Nowo zainstalowany dodatek często pojawia się dopiero po ponownym uruchomieniu.
- Otwórz **Insert → My Add-ins** i wybierz **PlaidCloud**.
- Sprawdź, czy używasz Excela na komputery stacjonarne w wersji dla Microsoft 365 albo Excela 2021 lub nowszego. Zobacz [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/).
- Jeśli Twoja organizacja zarządza dodatkami, zapytaj administratora Microsoft 365, czy dodatek **PlaidCloud** został dla Ciebie wdrożony.

## Okno logowania się nie otwiera

Po kliknięciu **Sign In** Excel pyta, czy wyświetlić okno podręczne. Zezwól na to. Jeśli odrzucono monit, kliknij **Sign In** ponownie.

Jeśli okno podręczne się otwiera, ale nie możesz dokończyć logowania, spróbuj zalogować się do PlaidCloud w przeglądarce, używając tego samego adresu e-mail. Problem występujący tam — wygasłe hasło lub urządzenie dwuskładnikowe, którego już nie masz — trzeba najpierw naprawić w PlaidCloud. Zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Obszaru roboczego nie ma na liście

Pole **Select a tenant** wyświetla obszary robocze, do których należy Twój adres e-mail. Jeśli któregoś brakuje, sprawdź, czy wpisano ten sam adres e-mail, którego używasz w tym obszarze roboczym, a następnie poproś administratora obszaru roboczego o potwierdzenie, że jesteś członkiem. Zobacz [Zarządzanie członkami obszaru roboczego](/pl/administration/access/overview/managing-workspace-members/).

Aby przejść do innego obszaru roboczego, do którego należysz, kliknij **Logout** i zaloguj się ponownie.

## Brakuje projektu, tabeli lub wymiaru

PlaidXL pokazuje to, co Twoje konto widzi w PlaidCloud. Jeśli brakuje projektu, poproś jego właściciela o przyznanie dostępu. Jeśli brakuje tabeli, sprawdź, czy istnieje w wybranym projekcie i czy załadowano do niej dane — tabela, do której nigdy nic nie zapisano, po wybraniu pokazuje komunikat **Unable to get table metadata**.

Foldery na listach projektów, tabel i wymiarów są początkowo zwinięte. Wpisz fragment nazwy w polu filtru u góry listy, aby znaleźć element wewnątrz folderu.

## Tabela jest wyświetlana na czerwono

Tabela ma więcej wierszy lub kolumn, niż mieści arkusz Excela. Wybierz **Zaawansowane**, aby przefiltrować wiersze, i wyczyść niepotrzebne kolumny, aż tabela się zmieści. Zobacz [Tabele wyświetlane na czerwono](/pl/reference/cli/plaidxl/retrieve/#tabele-wyświetlane-na-czerwono).

## Pobieranie jest wolne

Excel działa najwolniej przy szerokich tabelach. Wyczyść pola wyboru niepotrzebnych kolumn i przefiltruj wiersze za pomocą **Zaawansowane**. Pobieranie tylko danych, z którymi pracujesz, jest szybsze i daje mniejszy skoroszyt.

## Formuła pokazuje błąd

| Co widzisz | Co sprawdzić |
|---|---|
| `#SPILL!` | Coś znajduje się w komórkach potrzebnych na wynik. Wyczyść komórki poniżej formuły lub obok niej. |
| `#NAME?` | Excel nie rozpoznaje funkcji. Sprawdź, czy PlaidXL jest zainstalowany — karta **PlaidCloud** jest na wstążce — i sprawdź pisownię z [listą funkcji](/pl/reference/cli/plaidxl/functions/). |
| Błąd z funkcji `PLAIDXL` | Sprawdź, czy jesteś zalogowany i wybrano właściwy projekt, a następnie porównaj z PlaidCloud każdą nazwę tabeli, kolumny, wymiaru i węzła — nazwy muszą dokładnie się zgadzać. |
| `CELL` zgłasza, że nie znaleziono kolumny filtru | Pierwszy argument `DIMENSION_REPR` to kolumna tabeli, a nie wymiar. Użyj dokładnie nazwy kolumny tabeli. Zobacz [Wartości](/pl/reference/cli/plaidxl/functions/#wartości). |
| `CELL` zwraca 0 lub nieoczekiwaną sumę | Sprawdź nazwę węzła względem wymiaru — węzeł, który nie istnieje, nie agreguje niczego i zwraca 0. Węzeł agreguje się tylko w kolumnie powiązanej ze swoim wymiarem; w każdej innej kolumnie musi dokładnie odpowiadać wartości. |
| Wartości nie zmieniają się po zmianie danych lub projektu | Wymuś pełne przeliczenie — w systemie Windows naciśnij **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` zwraca błąd | Użyj jednej z wartości `sum`, `mean`, `median`, `min`, `max`, `std` lub `var`, małymi literami. |

## Formuły zwracają dane z innego projektu

Funkcje PlaidXL odczytują dane z projektu wybranego w okienku zadań, a ten wybór jest wspólny dla wszystkich otwartych skoroszytów. Wybierz projekt, dla którego zbudowano raport, a następnie wymuś pełne przeliczenie. **Ustaw jako domyślną** zapisuje projekt w skoroszycie, dzięki czemu jest wybrany po otwarciu tam okienka zadań. Zobacz [Ustawianie projektu domyślnego](/pl/reference/cli/plaidxl/retrieve/#ustawianie-projektu-domyślnego).

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/)
- [Logowanie do PlaidXL](/pl/reference/cli/plaidxl/connect/)
- [Uzyskiwanie pomocy](/pl/guides/support/getting-help/) — otwórz zgłoszenie do pomocy technicznej
