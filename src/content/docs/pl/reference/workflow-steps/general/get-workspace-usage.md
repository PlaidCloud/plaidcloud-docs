---
title: Get Workspace Usage
description: Zapisz sumy użycia obszaru roboczego z raportów użycia do tabeli projektu, dziennie lub miesięcznie, aby móc tworzyć wykresy adopcji lub zasilać kolejny krok.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Opis

Zapisuje do tabeli projektu informacje o tym, jak jest używany Twój obszar roboczy. Użyj go, aby śledzić adopcję w czasie, raportować użycie według działu lub zespołu, tworzyć własne pulpity albo wykrywać spadek aktywności w zaplanowanym przepływie pracy. Wartości są takie same jak w [Raportach użycia](/pl/administration/access/usage-reports/).

Trzy zbiory danych zawierają wyłącznie sumy: żaden wiersz nie wskazuje członka, a ścieżki notebooków są zastąpione znakiem `*`. Pozostałe cztery (**Członkowie**, **Dziennie na członka**, **Treść** i **Zawartość na członka**) są przeznaczone do raportowania. Zbiory **Członkowie**, **Dziennie na członka** i **Zawartość na członka** zawierają tożsamość członka (identyfikator użytkownika, nazwę użytkownika, adres e-mail, imię, nazwisko i grupy zabezpieczeń), dlatego traktuj tabelę docelową tak samo jak każdą listę członków. Każde uruchomienie kroku jest rejestrowane w Dziennik zabezpieczeń.

## Konfiguracja

### Dane użycia

**Zbiór danych** określa, co zawiera każdy wiersz:

| Zbiór danych | Wartość | Jeden wiersz dla każdego | Zawiera tożsamość |
|---|---|---|---|
| **Dziennie według elementu** | `daily_item` | dnia, obszaru, zdarzenia i tematu | Nie |
| **Miesięcznie według elementu** | `monthly_item` | miesiąca, obszaru, zdarzenia i tematu | Nie |
| **Sumy miesięczne** (domyślnie) | `monthly_tenant` | miesiąca i obszaru | Nie |
| **Członkowie** | `members` | osoby w obszarze roboczym | Tak |
| **Dziennie na członka** | `daily_user` | osoby, dnia i obszaru | Tak |
| **Treść** | `content` | pulpitu, aplikacji lub notebooka | Nie |
| **Zawartość na członka** | `content_user` | osoby i elementu | Tak |

**Obszar** ogranicza wiersze do jednego obszaru. Pozostaw wartość **Wszystkie obszary**, aby uwzględnić wszystkie.

| Obszar | Wartość |
|---|---|
| **Wszystkie obszary** (domyślnie) | `""` |
| **Aplikacja PlaidCloud** | `plaidclient` |
| **Pulpity** | `superset` |
| **Aplikacje** | `panel` |
| **Wizyty w aplikacjach** | `panel_visit` |
| **Serwery notebooków** | `jupyterhub` |
| **Notebooki** | `jupyter` |

Wartości to to, co krok przechowuje po utworzeniu lub edycji za pośrednictwem API albo asystenta AI.

### Kolumny

#### Dziennie według elementu

`day`, `source`, `event`, `subject`, `events`.

#### Miesięcznie według elementu

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Sumy miesięczne

`month`, `source`, `active_users`, `coverage_start`, `partial`.

Wartość `partial` jest prawdziwa dla miesiąca, którego historia nie obejmuje w całości, a `coverage_start` to data rozpoczęcia zbierania danych. Miesiąc jest uwzględniany po 3 dniach od jego zakończenia, gdy jego wartości się ustabilizują.

#### Kolumny członków

Zbiory **Członkowie**, **Dziennie na członka** i **Zawartość na członka** zaczynają się od tych samych siedmiu kolumn:

| Kolumna | Zawiera |
|---|---|
| `user_id` | Identyfikator członka. |
| `user_name` | Nazwa użytkownika członka. |
| `email` | Adres e-mail członka, małymi literami. |
| `first_name` | Imię. |
| `last_name` | Nazwisko. |
| `is_active` | Prawda, gdy członek jest aktywny, fałsz, gdy został dezaktywowany. |
| `groups` | Grupy zabezpieczeń członka, oddzielone znakami `; `. |

Kolumna `groups` zawiera tylko grupy najwyższego poziomu. Podgrupy nie są rozwijane.

#### Członkowie

Kolumny członków, a następnie:

| Kolumna | Zawiera |
|---|---|
| `first_seen` | Pierwszy dzień, w którym członek użył PlaidCloud, niezależnie od zakresu dat. Po ustawieniu wartości **Obszar** jest to pierwszy dzień w tym obszarze. |
| `last_seen` | Ostatni dzień aktywności członka w zakresie. |
| `active_days` | Dni z aktywnością w zakresie. |
| `events` | Zdarzenia aktywności w zakresie. |
| `active_minutes` | Minuty aktywności. Nakładające się minuty w różnych obszarach są liczone raz. |
| `session_minutes` | Minuty w sesjach. |
| `app_open_minutes` | Minuty, w których członek miał otwarte aplikacje Panel. |

Każdy członek ma wiersz, z wyjątkiem członków, których dane użycia zostały wymazane. Konta usług i agenci nie są wymieniani. Członek bez aktywności w zakresie ma puste wartości po kolumnie `groups`. Sumy zgadzają się z [Raportami użycia](/pl/administration/access/usage-reports/), z wyjątkiem członków usuniętych od tego czasu.

#### Dziennie na członka

Kolumny członków, a następnie `day`, `source` (obszar), `events`, `active_minutes`, `session_minutes`, `first_at` i `last_at` (czas pierwszej i ostatniej aktywności tego dnia).

#### Treść

| Kolumna | Zawiera |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` lub `notebook`. |
| `subject` | Identyfikator elementu. Wszystkie notebooki współdzielą jeden wiersz, z wartością `*` w tej kolumnie. |
| `name` | Nazwa elementu lub `*` dla notebooków. |
| `deleted` | Prawda, gdy element został od tego czasu usunięty. |
| `users` | Członkowie, którzy go otworzyli. |
| `opens` | Liczba otwarć. |
| `last_used` | Kiedy był ostatnio używany. |
| `app_open_minutes` | Minuty, w których aplikacje Panel były otwarte. |

#### Zawartość według członka

Kolumny członków, a następnie `type`, `subject`, `name` (jak w zbiorze **Treść**), `opens` (liczba otwarć elementu przez tego członka) i `last_day` (ostatni dzień użycia przez członka).

### Uwagi o zbiorach danych członków

- Aktywność agentów, kont usług i członków usuniętych od tego czasu ma puste kolumny tożsamości. Usunięty członek zachowuje tylko `user_id`.
- Liczba otwarć w zbiorze **Treść** może przekraczać sumę otwarć w zbiorze **Zawartość na członka**. Różnicą są otwarcia, których nie można przypisać do członka, takie jak osadzone widoki pulpitu lub widoki gości. Zbiór **Treść** je liczy, a **Zawartość na członka** nie może.

### Przykład: aktywne minuty według działu

Zbiory **Członkowie** i **Zawartość na członka** zawierają adres `email` członka, małymi literami, dzięki czemu można je złączyć z własną tabelą, taką jak tabela kadrowa lub struktury organizacyjnej, i raportować według działu.

1. Dodaj krok **Get Workspace Usage** z wartością **Zbiór danych** ustawioną na **Członkowie** i tabelą docelową, na przykład `usage_members`.
2. Dodaj krok **Tabela: złączenie wewnętrzne**, który łączy `usage_members` z tabelą organizacji tam, gdzie kolumny `email` pisane małymi literami są zgodne. Zachowaj dział z własnej tabeli oraz kolumny `active_minutes` i `events` z `usage_members`.
3. W tym samym kroku zagreguj według działu i zsumuj `active_minutes`.

Wynikiem są aktywne minuty według działu. Członkowie, których nie ma w tabeli organizacji, są pomijani w złączeniu wewnętrznym, więc użyj złączenia lewostronnego, jeśli chcesz ich zobaczyć. Powtórz z drugim krokiem dla zbioru **Zawartość na członka** i zsumuj `opens` według działu, aby zobaczyć, kto korzysta z których pulpitów i aplikacji.

### Zakres dat

**Zakres** określa dni do odczytu:

| Zakres | Wartość | Odczytuje |
|---|---|---|
| **Ostatnia liczba dni** (domyślnie 30) | `last_days` | Ostatnie dni, łącznie z dzisiejszym. |
| **Poprzedni miesiąc** | `previous_month` | Ostatni pełny miesiąc kalendarzowy. |
| **Od początku miesiąca** | `month_to_date` | Od pierwszego dnia bieżącego miesiąca do dziś. |
| **Między datami** | `dates` | Od daty **Data początkowa** do daty **Data końcowa**. Pozostaw pole **Data końcowa** puste, aby czytać do dziś. |

Dni i daty są w UTC. Pola **Dni**, **Data początkowa** i **Data końcowa** akceptują [zmienną](/pl/guides/workflows/manage-workflow-variables/), taką jak `{report_start}`, a także liczbę lub datę w formacie `YYYY-MM-DD`. Początek nie może być późniejszy niż koniec.

### Cel użycia

**Tabela docelowa** otrzymuje wynik. Krok zastępuje wszystko, co tabela zawierała, i zawsze zapisuje kolumny zbioru danych, nawet gdy nie ma wierszy.

## Ostrzeżenia

Nie powodują one niepowodzenia kroku. Krok kończy się ostrzeżeniem, które opisuje, co się stało, i nadal zapisuje tabelę:

- Zbieranie danych użycia nie zostało jeszcze skonfigurowane dla obszaru roboczego.
- W zakresie nie było żadnego użycia.
- Zakres zaczyna się przed okresem przechowywania danych, więc został skrócony tak, aby zaczynał się tam, gdzie zaczyna się historia. Dane dzienne są przechowywane przez 180 dni, a dane miesięczne przez 25 miesięcy.

## Dziennik zabezpieczeń

Każde uruchomienie zapisuje wpis w Dziennik zabezpieczeń, rejestrujący zbiór danych, zakres, tabelę docelową, przepływ pracy, krok i uruchomienie oraz liczbę zapisanych wierszy.

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Raporty użycia](/pl/administration/access/usage-reports/)
- [Get Workspace Members](/pl/reference/workflow-steps/general/get-workspace-members/)
