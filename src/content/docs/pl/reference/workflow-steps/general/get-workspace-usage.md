---
title: Get Workspace Usage
description: Zapisz użycie obszaru roboczego do tabeli projektu jako aktywność, członków, treść lub trendy, aby móc raportować adopcję lub zasilać kolejny krok.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Opis

Zapisuje do tabeli projektu informacje o tym, jak jest używany Twój obszar roboczy. Użyj go, aby śledzić adopcję w czasie, raportować użycie według działu lub zespołu, tworzyć własne pulpity albo wykrywać spadek aktywności w zaplanowanym przepływie pracy. Wartości pochodzą z tych samych danych o użyciu co [Raporty użycia](/pl/administration/access/usage-reports/), a każdy zbiór danych obejmuje wszystkie obszary.

Zbiory **Aktywność** i **Członkowie** zawierają tożsamość członka (identyfikator użytkownika, nazwę użytkownika, adres e-mail, imię, nazwisko i grupy zabezpieczeń). Tabela docelowa jest zwykłą tabelą projektu, więc może ją odczytać każdy, kto ma dostęp do projektu: traktuj ją tak samo jak każdą listę członków. Każde uruchomienie, które zapisuje tabelę, jest rejestrowane w Dziennik zabezpieczeń.

## Konfiguracja

### Dane użycia

**Zbiór danych** określa, co zawiera każdy wiersz. Tekst pod nim opisuje wiersze i wymienia główne kolumny wybranego zbioru.

| Zbiór danych | Wartość | Jeden wiersz dla każdego | Zawiera tożsamość |
|---|---|---|---|
| **Aktywność** (domyślnie) | `activity` | dnia, członka, działania i elementu | Tak |
| **Członkowie** | `members` | członka, także członków bez aktywności | Tak |
| **Treść** | `content` | pulpitu, aplikacji i notebooka, także pulpitów i aplikacji, z których nikt nie korzystał | Nie |
| **Trendy** | `trends` | dnia, tygodnia i miesiąca zakresu | Nie |

Wartości to to, co krok przechowuje po utworzeniu lub edycji za pośrednictwem API albo asystenta AI. Krok zapisany ze zbiorem danych, którego nie ma na tej liście, kończy się niepowodzeniem po uruchomieniu i wymienia cztery zbiory: otwórz go, wybierz **Zbiór danych** i zapisz. Krok **Członkowie** lub **Treść** zapisany wcześniej nadal działa i zapisuje poniższe kolumny, a krok ograniczony wcześniej do jednego obszaru obejmuje teraz wszystkie obszary. W zbiorze **Treść** `subject` to teraz `item_id`, a `type` zawiera `Dashboard`, `App` lub `Notebook`.

### Kolumny

Daty i dni trafiają do tabeli jako znaczniki czasu o północy UTC.

#### Kolumny członków

Zbiory **Aktywność** i **Członkowie** zawierają te kolumny:

| Kolumna | Zawiera |
|---|---|
| `user_id` | Identyfikator członka. |
| `user_name` | Nazwa użytkownika członka. |
| `email` | Adres e-mail członka, małymi literami. |
| `first_name` | Imię. |
| `last_name` | Nazwisko. |
| `is_active` | Prawda, gdy członek jest aktywny, fałsz, gdy został dezaktywowany. |
| `groups` | Grupy zabezpieczeń członka, oddzielone znakami `; `. |

Kolumna `groups` zawiera grupy najwyższego poziomu, do których członek należy bezpośrednio.

#### Aktywność

| Kolumna | Zawiera |
|---|---|
| `day` | Dzień. |
| Kolumny członków | Jak wyżej. |
| `member` | Imię i nazwisko członka lub jego nazwa użytkownika, gdy żadne z nich nie jest ustawione. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` lub `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` lub `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` lub `Notebook`. |
| `item_id` | Identyfikator elementu. W przypadku notebooka jego ścieżka. |
| `item_name` | Nazwa elementu: ekran lub obszar aplikacji słownie, na przykład `Members List`; typ kroku; nazwa pulpitu, wykresu lub aplikacji albo ścieżka notebooka. Gdy nazwy nie można znaleźć, identyfikator elementu. |
| `events` | Ile razy członek wykonał to danego dnia. |
| `source` | Klucz obszaru, tak jak nazywają go eksporty [Raportów użycia](/pl/administration/access/usage-reports/). |
| `event` | Klucz działania, tak jak nazywają go eksporty. |

Kolumna `member` i kolumny członków zależą od tego, kto to zrobił:

- Aktywność, której nie można powiązać z żadnym członkiem, ma w `member` wartość `Unattributed` i puste kolumny członków.
- Członek usunięty od tego czasu zachowuje tylko `user_id`, a `member` ma wartość `Deleted user`.
- Każde inne konto, takie jak konto usługi lub agent, zachowuje tylko `user_id`, a `member` zawiera jego nazwę użytkownika.

Wartość `Used chart` liczy się raz na członka i wykres w każdym 5-minutowym oknie, więc mierzy użycie, a nie zapytania.

#### Członkowie

| Kolumna | Zawiera |
|---|---|
| Kolumny członków | Jak wyżej. |
| `member` | Imię i nazwisko członka lub jego nazwa użytkownika, gdy żadne z nich nie jest ustawione. |
| `created` | Dzień dodania członka do obszaru roboczego, jeśli jest znany. |
| `status` | `Active`, gdy członek był aktywny w zakresie, `Dormant`, gdy używał PlaidCloud wcześniej, ale nie w zakresie, `Never active`, gdy do końca zakresu nie ma żadnego zapisanego użycia. |
| `first_seen` | Pierwszy dzień w zapisach, w którym członek użył PlaidCloud, niezależnie od zakresu. |
| `last_seen` | Ostatni dzień aktywności członka w zakresie. |
| `active_days` | Dni z aktywnością w zakresie. |
| `events` | Zdarzenia aktywności w zakresie. |
| `active_minutes` | Minuty aktywności w zakresie. |
| `session_minutes` | Minuty w sesjach w zakresie. |
| `app_open_minutes` | Minuty, w których członek miał otwarte aplikacje Panel w zakresie. Podglądy w Studio nie są liczone. |

Każdy członek ma wiersz, także dezaktywowani, z wyjątkiem członków, których dane użycia zostały wymazane. Konta usług i agenci nie są wymieniani. Członek bez aktywności w zakresie nie ma `last_seen`, a jego pozostałe kolumny aktywności są puste.

#### Treść

| Kolumna | Zawiera |
|---|---|
| `type` | `Dashboard`, `App` lub `Notebook`. |
| `item_id` | Identyfikator pulpitu lub aplikacji albo ścieżka notebooka. |
| `name` | Nazwa pulpitu lub aplikacji albo ścieżka notebooka. Puste, gdy element został usunięty lub nie można odczytać nazw. |
| `deleted` | Prawda, gdy pulpit lub aplikacja została od tego czasu usunięta. |
| `unused` | Prawda dla pulpitu lub aplikacji, z których nikt nie korzystał w zakresie. |
| `users` | Członkowie, którzy z niego korzystali w zakresie. |
| `opens` | Liczba otwarć w zakresie, wraz z otwarciami, których nie można przypisać do żadnego członka. |
| `last_used` | Ostatni dzień użycia w zakresie. Dla nieużywanego elementu ostatni dzień otwarcia przed końcem zakresu lub puste. |
| `app_open_minutes` | Minuty, w których aplikacja Panel była otwarta w zakresie. Puste dla pulpitów, notebooków oraz aplikacji Dash i WASM. |

Każda ścieżka notebooka ma własny wiersz. Wiersze wymieniają najpierw elementy używane, od największej liczby użytkowników, a potem pulpity i aplikacje, z których nikt nie korzystał. Są to opublikowane pulpity i aplikacje, które istniały już na początku zakresu. Są wymieniane tylko wtedy, gdy zakres zaczyna się w przechowywanych danych dziennych, użycie tego rodzaju elementów było już wtedy zbierane, a nazwy można odczytać. Podglądy aplikacji w Studio są pomijane.

#### Trendy

| Kolumna | Zawiera |
|---|---|
| `period` | `Day`, `Week` lub `Month`. |
| `period_start` | Pierwszy dzień okresu. Tygodnie zaczynają się w poniedziałek. |
| `active_members` | Członkowie aktywni w okresie, w zakresie. |
| `events` | Zdarzenia aktywności w okresie. |
| `active_minutes` | Minuty aktywności w okresie. |
| `session_minutes` | Minuty w sesjach w okresie. |
| `active_members_7d` | W wierszu `Day` członkowie aktywni w ciągu 7 dni kończących się tego dnia. |
| `active_members_28d` | W wierszu `Day` członkowie aktywni w ciągu 28 dni kończących się tego dnia. |
| `stickiness` | W wierszu `Day` wartość `active_members` podzielona przez `active_members_28d`. |
| `complete` | Fałsz dla dzisiejszego dnia, dla tygodnia lub miesiąca, który zawiera dzisiejszy dzień, oraz dla tygodnia lub miesiąca ściętego przez zakres. |

Każdy dzień zakresu, od miejsca, w którym zaczynają się przechowywane dane dzienne, ma wiersz, nawet bez użycia, tak samo jak każdy tydzień i miesiąc, na które te dni przypadają. Kolumny `active_members_7d`, `active_members_28d` i `stickiness` są puste w wierszach `Week` i `Month` oraz w wierszu `Day`, którego 7 lub 28 dni sięga przed przechowywane dane dzienne. Kolumna `stickiness` jest też pusta, gdy `active_members_28d` wynosi 0. Miesiąc, który zaczyna się przed przechowywanymi danymi dziennymi i w całości leży w zakresie, pochodzi z podsumowań miesięcznych: ma `active_members`, ale puste zdarzenia i minuty, a `complete` informuje, czy podsumowanie obejmowało cały miesiąc.

### Przykład: aktywne minuty według działu

Zbiory **Aktywność** i **Członkowie** zawierają adres `email` członka, małymi literami, dzięki czemu można je złączyć z własną tabelą, taką jak tabela kadrowa lub struktury organizacyjnej, i raportować według działu.

1. Dodaj krok **Get Workspace Usage** z wartością **Zbiór danych** ustawioną na **Członkowie** i tabelą docelową, na przykład `usage_members`.
2. Dodaj krok **Tabela: złączenie wewnętrzne**, który łączy `usage_members` z tabelą organizacji tam, gdzie kolumny `email` pisane małymi literami są zgodne. Zachowaj dział z własnej tabeli oraz kolumny `active_minutes` i `events` z `usage_members`.
3. W tym samym kroku zagreguj według działu i zsumuj `active_minutes`.

Wynikiem są aktywne minuty według działu. Członkowie, których nie ma w tabeli organizacji, są pomijani w złączeniu wewnętrznym, więc użyj złączenia lewostronnego, jeśli chcesz ich zobaczyć. Powtórz z drugim krokiem dla zbioru **Aktywność** i zsumuj `events` według działu i `item_name`, aby zobaczyć, kto korzysta z których pulpitów i aplikacji.

### Zakres dat

**Zakres** określa dni do odczytu:

| Zakres | Wartość | Odczytuje |
|---|---|---|
| **Ostatnia liczba dni** (domyślnie 30) | `last_days` | Ostatnie dni, łącznie z dzisiejszym. |
| **Poprzedni miesiąc** | `previous_month` | Ostatni pełny miesiąc kalendarzowy. |
| **Od początku miesiąca** | `month_to_date` | Od pierwszego dnia bieżącego miesiąca do dziś. |
| **Między datami** | `dates` | Od daty **Data początkowa** do daty **Data końcowa**. Pozostaw pole **Data końcowa** puste, aby czytać do dziś. |

Dni i daty są w UTC. Pole **Dni** przyjmuje liczbę całkowitą. Pola **Data początkowa** i **Data końcowa** przyjmują datę w formacie `YYYY-MM-DD` lub [zmienną](/pl/guides/workflows/manage-workflow-variables/), taką jak `{report_start}`. Początek nie może być późniejszy niż koniec.

Dane dzienne są przechowywane przez 180 dni, a podsumowania miesięczne przez 25 miesięcy.

### Cel użycia

**Tabela docelowa** otrzymuje wynik. Krok zastępuje wszystko, co tabela zawierała, i zawsze zapisuje kolumny zbioru danych, nawet gdy nie ma wierszy.

## Ostrzeżenia

Nie powodują one niepowodzenia kroku. Krok kończy się ostrzeżeniem i nadal zastępuje tabelę, z kolumnami zbioru danych:

| Ostrzeżenie | Znaczenie |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | Zbieranie danych użycia nie zostało jeszcze skonfigurowane dla obszaru roboczego. |
| "Usage data is not available right now: the usage database could not be reached." | Nie można było odczytać danych użycia. Uruchom krok ponownie później. |
| "No usage from *start* to *end*." | W zakresie nie było żadnego użycia. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | Zakres zaczyna się przed przechowywanymi danymi dziennymi, więc aktywność jest liczona od *date*. Zbiór **Trendy** nadal zawiera całe miesiące przed tą datą z podsumowań miesięcznych. |
| "This took too long to compute: narrow the date range." | Odczyt przekroczył limit czasu, więc tabela nie ma wierszy. Wybierz krótszy zakres. |
| "Some names are unavailable right now, so those items are named by their id." | Tylko **Aktywność**. Nie można było odczytać niektórych nazw pulpitów, wykresów lub aplikacji, więc `item_name` zawiera identyfikator. |
| "Members could not be read right now, so they are named by their id." | Tylko **Aktywność**. Nie można było odczytać listy członków, więc `member` zawiera identyfikator członka, a z kolumn członków wypełnione jest tylko `user_id`. |
| "Names are unavailable right now, so items nobody used are not listed." | Tylko **Treść**. Nie można było odczytać nazw pulpitów lub aplikacji, więc wymienione są tylko używane elementy. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | Tylko **Treść**. Zakres zaczyna się przed przechowywanymi danymi dziennymi, więc wymienione są tylko używane elementy. |

Gdy nie można odczytać listy członków, zbiór **Członkowie** kończy się niepowodzeniem i pozostawia tabelę docelową bez zmian.

## Dziennik zabezpieczeń

Każde uruchomienie, które zapisuje tabelę, dodaje wpis w Dziennik zabezpieczeń, rejestrujący zbiór danych, zakres, tabelę docelową wraz z jej projektem, przepływ pracy, krok i uruchomienie, liczbę zapisanych wierszy oraz, dla zbiorów **Aktywność** i **Członkowie**, informację, że wiersze zawierają tożsamość członka.

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Raporty użycia](/pl/administration/access/usage-reports/)
- [Get Workspace Members](/pl/reference/workflow-steps/general/get-workspace-members/)
