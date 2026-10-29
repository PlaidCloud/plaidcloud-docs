---
title: Notify Via SMS
description: Wyślij wiadomość SMS z kroku przepływu pracy do członków obszaru roboczego, którzy wyrazili zgodę na alerty tekstowe, z potwierdzeniem dostarczenia, awaryjnym e-mailem, scalaniem powtórzeń i godzinami ciszy.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-sms.md
---

## Opis

Wysyłaj SMS-y do członków obszaru roboczego, gdy przepływ pracy wymaga ich uwagi. SMS trafia tylko do członka, który sam wyraził zgodę w oknie **Alerty tekstowe** w menu użytkownika, podając potwierdzony numer telefonu komórkowego w USA. Wybierasz członków lub listę dystrybucyjną; numeru telefonu nigdy nie wpisujesz w kroku. Aby wyrazić zgodę, zobacz [Alerty tekstowe](/pl/guides/workflows/text-alerts/).

SMS-y są obsługiwane wyłącznie dla numerów w USA. Nie umieszczaj w wiadomości SMS danych osobowych dotyczących zdrowia ani finansów.

SMS-y są wysyłane z jednego numeru alertów PlaidCloud i mają postać `PlaidCloud [your workspace name]: ` po którym następuje Twoja wiadomość. Zobacz [Warunki SMS](https://plaidcloud.com/sms-terms/) i [Politykę prywatności SMS](https://plaidcloud.com/sms-privacy/).

## Odbiorcy

Wybierz **Członkowie** lub **Lista dystrybucyjna**.

- **Członkowie** to lista członków Twojego obszaru roboczego. Przy każdym widoczny jest status **Zgoda udzielona**, **Brak zgody** lub **Zrezygnowano - wyślij SMS-em START na numer alertów**.
- **Lista dystrybucyjna** wysyła SMS do każdego członka listy, który wyraził zgodę.

Członek, który nie wyraził zgody, nie otrzymuje SMS-a. Jest to problem dla kroku (zobacz **Jeśli nie można dostarczyć wiadomości SMS**), a domyślnie taka osoba otrzymuje wiadomość e-mailem.

## Komunikat

Napisz **Komunikat**. Zmienne projektu i zmienne przepływu pracy działają, a **Wstaw zmienną** dodaje dowolną z poniższych:

| Zmienna | Wartość |
|---|---|
| `{workflow_name}` | Nazwa uruchomionego przepływu pracy |
| `{project_name}` | Nazwa projektu |
| `{run_url}` | Link do uruchomienia w PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | Istniejące zmienne |

Licznik pod komunikatem pokazuje w przybliżeniu, ile znaków i segmentów zajmuje SMS, wliczając prefiks `PlaidCloud [workspace]:` i link do uruchomienia. SMS dłuższy niż 3 segmenty jest przycinany. Linki z publicznych skracaczy są odrzucane.

## Dostarczanie

| Ustawienie | Działanie |
|---|---|
| **Jeśli nie można dostarczyć wiadomości SMS** | **Zakończ krok niepowodzeniem** (domyślnie) lub **Ostrzeż i kontynuuj**. Niedostarczony SMS nigdy nie jest cichy: zawsze jest zgłaszany w kroku. |
| **Wyślij e-mail do odbiorców, którym nie można dostarczyć wiadomości SMS** | Domyślnie włączone. Członek, któremu SMS się nie powiódł, który nie wyraził zgody lub z niej zrezygnował, otrzymuje wiadomość e-mailem. |
| **Scalaj powtórzenia przez (minuty)** | Domyślnie 60. Powtórzenie tej samej wiadomości do tego samego członka w tym czasie nie jest wysyłane, a następny wysłany SMS kończy się tekstem `(+N similar since HH:MM)`. |
| **Wstrzymaj wiadomości SMS w godzinach ciszy** | Wybierz godziny **Od** i **do** oraz strefę czasową. SMS, który miałby zostać wysłany w tym oknie, jest wstrzymywany do jego końca. |

Każdy członek otrzymuje najwyżej 20 SMS-ów dziennie, obszar roboczy wysyła najwyżej 500 SMS-ów i awaryjnych e-maili dziennie, a jeden krok wysyła SMS-y do najwyżej 50 członków naraz.

## Wyślij test do mnie

**Wyślij test do mnie** wysyła testowy SMS na Twój numer i pokazuje wynik obok przycisku. Jeśli nie wyraziłeś zgody, otwiera się okno **Alerty tekstowe**, w którym możesz to zrobić.

## Co widzą odbiorcy

Każdy SMS pochodzi z numeru alertów. Odpowiedź **STOP** zatrzymuje wszystkie SMS-y z PlaidCloud na ten numer, a **HELP** zwraca dane kontaktowe. Po STOP członek wysyła SMS-em **START** na numer alertów, aby wznowić, a następnie ponownie włącza alerty tekstowe w oknie **Alerty tekstowe**. Formularz kroku pokazuje **Zrezygnowano - wyślij SMS-em START na numer alertów** obok tego członka, dopóki tego nie zrobi.

Administratorzy obszaru roboczego widzą status alertów tekstowych każdego członka, z zamaskowanym numerem, na karcie **Informacje o członku** w oknie członka. Członkowie wyrażają zgodę i rezygnują samodzielnie; administrator nie może tego zrobić za nich.

## Kroki z wpisanym numerem

Wcześniejsza wersja tego kroku przyjmowała operatora komórkowego i wpisany numer telefonu. Krok nadal zapisany w ten sposób nie powoduje niepowodzenia przepływu pracy i nie wysyła SMS-a na wpisany numer.

- **Nie wybrano odbiorców:** krok kończy się z ostrzeżeniem, *No text was sent: this step still uses the retired mobile provider and number. Open the step, choose members who've opted in to text alerts, and save it.* Nic nie jest wysyłane.
- **Wybrano członków lub listę dystrybucyjną:** krok wysyła SMS-y do tych odbiorców i ignoruje pozostały po poprzedniej wersji numer i operatora.

Aby naprawić krok, otwórz go, wybierz członków lub listę dystrybucyjną i zapisz.

## Przykłady

Brak przykładów...
