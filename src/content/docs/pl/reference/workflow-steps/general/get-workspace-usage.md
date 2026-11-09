---
title: Get Workspace Usage
description: Zapisz sumy użycia obszaru roboczego z Raportów użycia do tabeli projektu, dziennie lub miesięcznie, aby wykresować wykorzystanie lub zasilić kolejny krok.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Opis

Zapisuje do tabeli projektu informacje o tym, jak używany jest Twój obszar roboczy. Użyj go do śledzenia wykorzystania w czasie, raportowania użycia według działu lub zespołu, tworzenia własnych pulpitów albo wykrywania spadku aktywności w zaplanowanym przepływie pracy. Wartości są te same, które pokazują [Raporty użycia](/pl/administration/access/usage-reports/).

Trzy zbiory danych zawierają wyłącznie sumy: żaden wiersz nie wskazuje członka, a ścieżki notatników są zastąpione znakiem `*`. Pozostałe cztery (**Członkowie**, **Dzienne według członka**, **Treść** i **Treść według członka**) są przeznaczone do raportowania. **Członkowie**, **Dzienne według członka** i **Treść według członka** zawierają tożsamość członka (identyfikator użytkownika, nazwę użytkownika, adres e-mail, imię i nazwisko oraz grupy zabezpieczeń), dlatego traktuj tabelę docelową tak jak każdą listę członków. Każde uruchomienie kroku jest zapisywane w Dzienniku zabezpieczeń.

## Konfiguracja

### Dane użycia

**Zbiór danych** określa, co zawiera każdy wiersz:

| Zbiór danych | Jeden wiersz dla każdego | Zawiera tożsamość |
|---|---|---|
| **Dzienne według elementu** | Dnia, obszaru, zdarzenia i przedmiotu | Nie |
| **Miesięczne według elementu** | Miesiąca, obszaru, zdarzenia i przedmiotu | Nie |
| **Sumy miesięczne** (domyślny) | Miesiąca i obszaru | Nie |
| **Członkowie** | Osoby w obszarze roboczym | Tak |
| **Dzienne według członka** | Osoby, dnia i obszaru | Tak |
| **Treść** | Pulpitu, aplikacji lub notatnika | Nie |
| **Treść według członka** | Osoby i elementu | Tak |

**Obszar** ogranicza wiersze do jednego obszaru: **Aplikacja PlaidCloud**, **Pulpity**, **Aplikacje**, **Wizyty w aplikacjach** lub **Notatniki**. Pozostaw **Wszystkie obszary**, aby uwzględnić wszystkie.

### Kolumny

#### Dzienne według elementu

`day`, `source`, `event`, `subject`, `events`.

#### Miesięczne według elementu

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Sumy miesięczne

`month`, `source`, `active_users`, `coverage_start`, `partial`.

Wartość `partial` jest prawdziwa dla miesiąca, którego historia nie obejmuje w całości, a `coverage_start` to data rozpoczęcia zbierania danych. Miesiąc jest uwzględniany po jego zamknięciu i ustabilizowaniu się danych, co trwa 3 dni.

#### Kolumny członka

**Członkowie**, **Dzienne według członka** i **Treść według członka** zaczynają się od tych samych siedmiu kolumn:

| Kolumna | Zawiera |
|---|---|
| `user_id` | Identyfikator członka. |
| `user_name` | Nazwa użytkownika członka. |
| `email` | Adres e-mail członka, małymi literami. |
| `first_name` | Imię. |
| `last_name` | Nazwisko. |
| `is_active` | Prawda, gdy członek jest aktywny; fałsz, gdy został dezaktywowany. |
| `groups` | Grupy zabezpieczeń członka, oddzielone znakami `; `. |

Kolumna `groups` zawiera wyłącznie grupy najwyższego poziomu. Podgrupy nie są rozwijane.

#### Członkowie

Kolumny członka, a następnie:

| Kolumna | Zawiera |
|---|---|
| `first_seen` | Pierwszy dzień, w którym członek użył PlaidCloud, niezależnie od zakresu dat. |
| `last_seen` | Ostatni dzień aktywności członka w zakresie. |
| `active_days` | Dni z aktywnością w zakresie. |
| `events` | Zdarzenia aktywności w zakresie. |
| `active_minutes` | Minuty aktywności. Nakładające się minuty w różnych obszarach są liczone raz. |
| `session_minutes` | Minuty w sesjach. |
| `app_open_minutes` | Minuty, przez które członek miał otwarte aplikacje Panel. |

Każda osoba w obszarze roboczym ma wiersz. Członek bez aktywności w zakresie ma puste wartości po kolumnie `groups`. Sumy zgadzają się z [Raportami użycia](/pl/administration/access/usage-reports/), z wyjątkiem członków usuniętych od tego czasu.

#### Dzienne według członka

Kolumny członka, a następnie `day`, `source` (obszar), `events`, `active_minutes`, `session_minutes`, `first_at` i `last_at` (pierwsza i ostatnia godzina aktywności danego dnia).

#### Treść

| Kolumna | Zawiera |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` lub `notebook`. |
| `subject` | Identyfikator elementu. Wszystkie notatniki współdzielą jeden wiersz, z wartością `*` w tej kolumnie. |
| `name` | Nazwa elementu lub `*` dla notatników. |
| `deleted` | Prawda, gdy element został od tego czasu usunięty. |
| `users` | Członkowie, którzy go otworzyli. |
| `opens` | Liczba otwarć. |
| `last_used` | Kiedy był ostatnio używany. |
| `app_open_minutes` | Minuty, przez które aplikacje Panel były otwarte. |

#### Treść według członka

Kolumny członka, a następnie `type`, `subject`, `name` (jak w zbiorze **Treść**), `opens` (liczba otwarć elementu przez tego członka) i `last_day` (ostatni dzień użycia przez członka).

### Uwagi o zbiorach danych członków

- Aktywność agentów, kont usług i członków usuniętych od tego czasu ma puste kolumny tożsamości. Usunięty członek zachowuje tylko `user_id`.
- Liczba otwarć w zbiorze **Treść** może przekraczać sumę otwarć w zbiorze **Treść według członka**. Różnica to otwarcia, których nie można przypisać do członka, takie jak osadzone lub gościnne wyświetlenia pulpitu. **Treść** je liczy, a **Treść według członka** nie może.

### Przykład: aktywne minuty według działu

**Członkowie** i **Treść według członka** zawierają adres `email` członka, małymi literami, dzięki czemu można je złączyć z własną tabelą, taką jak tabela główna HR lub struktury organizacyjnej, i raportować według działu.

1. Dodaj krok **Get Workspace Usage** z ustawieniem **Zbiór danych** na **Członkowie** i tabelą docelową, np. `usage_members`.
2. Dodaj krok **Tabela: złączenie wewnętrzne**, który łączy `usage_members` z Twoją tabelą organizacyjną tam, gdzie zgadzają się kolumny `email` zapisane małymi literami. Zachowaj dział z Twojej tabeli oraz kolumny `active_minutes` i `events` z `usage_members`.
3. W tym samym kroku zagreguj według działu i zsumuj `active_minutes`.

Wynikiem są aktywne minuty według działu. Członkowie, których nie ma w Twojej tabeli organizacyjnej, odpadają przy złączeniu wewnętrznym, więc użyj złączenia lewostronnego, jeśli chcesz ich zobaczyć. Powtórz z drugim krokiem na zbiorze **Treść według członka** i zsumuj `opens` według działu, aby zraportować, kto używa których pulpitów i aplikacji.

### Zakres dat

**Zakres** określa dni do odczytu:

- **Ostatnia liczba dni** (domyślnie 30) odczytuje ostatnie dni, włącznie z dzisiejszym.
- **Poprzedni miesiąc** odczytuje ostatni pełny miesiąc kalendarzowy.
- **Od początku miesiąca** odczytuje od pierwszego dnia bieżącego miesiąca do dziś.
- **Między datami** odczytuje od **Data początkowa** do **Data końcowa**. Pozostaw **Data końcowa** puste, aby czytać do dziś.

Dni i daty są w UTC. Pola **Dni**, **Data początkowa** i **Data końcowa** akceptują [zmienną](/pl/guides/workflows/manage-workflow-variables/), taką jak `{report_start}`, a także liczbę lub datę w formacie `YYYY-MM-DD`. Początek nie może być późniejszy niż koniec.

### Cel użycia

**Tabela docelowa** otrzymuje wynik. Krok zastępuje całą dotychczasową zawartość tabeli i zawsze zapisuje kolumny zbioru danych, nawet gdy nie ma wierszy.

## Ostrzeżenia

Nie powodują one niepowodzenia kroku. Krok kończy się ostrzeżeniem, które mówi, co się stało, i nadal zapisuje tabelę:

- Zbieranie danych o użyciu nie zostało jeszcze skonfigurowane dla obszaru roboczego.
- W zakresie nie było żadnego użycia.
- Zakres zaczyna się przed okresem przechowywania danych, więc został przycięty do początku historii. Dane dzienne są przechowywane przez 180 dni, a miesięczne przez 25 miesięcy.

## Dziennik zabezpieczeń

Każde uruchomienie zapisuje wpis w Dzienniku zabezpieczeń z informacją o zbiorze danych, zakresie, tabeli docelowej, przepływie pracy, kroku i uruchomieniu oraz liczbie zapisanych wierszy.

## Zobacz też

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [Raporty użycia](/pl/administration/access/usage-reports/)
- [Get Workspace Members](/pl/reference/workflow-steps/general/get-workspace-members/)
