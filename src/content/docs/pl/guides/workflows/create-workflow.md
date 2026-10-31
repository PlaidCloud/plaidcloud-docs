---
title: Tworzenie przepływu pracy (przewodnik)
description: Utwórz przepływ pracy w PlaidCloud i wybierz jego typ — standardowy szeregowy, standardowy równoległy lub zaawansowany (obszar DAG) — aby ładować, przekształcać i eksportować dane.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/create-workflow.md
---

Aby utworzyć nowy przepływ pracy, potrzebujesz istniejącego projektu. Jeśli jeszcze go nie masz, zobacz [Zarządzanie projektami](/pl/guides/projects/managing-projects/).

## Kroki

1. Otwórz projekt, który ma zawierać przepływ pracy.
2. Przejdź na kartę **Przepływy pracy**.
3. Kliknij **Nowy przepływ pracy** na pasku narzędzi.
4. Wypełnij formularz:
   - **Nazwa** — krótka, opisowa (np. „Zamknięcie miesiąca — załaduj dane rzeczywiste")
   - **Notatka** — opcjonalny dłuższy opis kontekstu
   - **Typ przepływu pracy** — standardowy szeregowy (domyślny), standardowy równoległy lub zaawansowany (obszar DAG). Zobacz [Wybór typu przepływu pracy](#wybór-typu-przepływu-pracy) poniżej.
   - **Uruchom przepływ pracy naprawczy w razie błędu** — opcjonalne; włącz, aby wybrać przepływ pracy naprawczy (zobacz [Przepływy pracy naprawcze](#przepływy-pracy-naprawcze) poniżej).
5. Kliknij **Utwórz**.

Przepływ pracy pojawi się na karcie Przepływy pracy i będzie gotowy do dodawania kroków. Kliknij go dwukrotnie, aby otworzyć [Eksplorator przepływów pracy](/pl/guides/workflows/workflow-explorer/) i zacząć budowanie.

## Sprawdzanie, kiedy tabela źródłowa ostatnio się zmieniła

W formularzu kroku selektor tabeli pokazuje pod wybraną tabelą przygaszony wiersz **Ostatnia aktualizacja** z datą i godziną w Twojej strefie czasowej, dzięki czemu od razu widać, czy dane są aktualne. Najedź na wiersz, aby zobaczyć pełny tekst. Wiersz jest ukryty, gdy wybór jest dynamiczny lub gdy tabela nigdy nie była aktualizowana.

## Wybór typu przepływu pracy

**Typ przepływu pracy** wybrany podczas tworzenia przepływu pracy określa, jak jego kroki są rozmieszczone i uruchamiane. Domyślnie jest to **Standardowy szeregowy**, a ustawiasz go w selektorze typu w formularzu Nowy przepływ pracy.

| Typ | Jak kroki są rozmieszczone i uruchamiane |
|------|--------------------------------|
| **Standardowy szeregowy** | Kroki są uruchamiane z **listy kroków**, pojedynczo, po kolei. |
| **Standardowy równoległy** | Kroki są uruchamiane z **listy kroków**, równolegle tam, gdzie pozwalają na to zależności. |
| **Zaawansowany (obszar DAG)** | Kroki są rozmieszczone na **wizualnej kanwie** i uruchamiane w kolejności zależności, a niezależne gałęzie działają równolegle. Typ zaawansowany odblokowuje też punkty przerwania, kontenery, uruchamianie od tego miejsca, symulację i współpracę w czasie rzeczywistym. |

Czwarty typ, **Makro** — wielokrotnego użytku, wywoływalny przepływ pracy z zadeklarowanymi wejściami i wyjściami — jest wkrótce dostępny i w selektorze jest wyłączony.

:::note
Krok może występować w przepływie pracy tylko raz. Wstawienie, skopiowanie, sklonowanie lub zaimportowanie kroku w pozycji, która umieściłaby go w przepływie pracy po raz drugi, zostaje odrzucone z podaniem nazwy kroku — dlatego nie można już doprowadzić do takiego stanu. Jeśli przepływ pracy sprzed tej poprawki nadal zawiera krok w dwóch miejscach, uruchomienie **standardowego szeregowego** kończy się natychmiast błędem wskazującym zduplikowany krok — podobnie jak uruchomienie **standardowego równoległego** zatrzymane na wybranym kroku końcowym (zobacz [Uruchamianie zakresu kroków w przepływie pracy](/pl/guides/workflows/running-a-range-of-steps-in-a-workflow/)), ponieważ uruchomienie do punktu końcowego również przebiega sekwencyjnie. Uruchomienie **standardowego równoległego** do końca toleruje duplikat i po prostu uruchamia go raz. W obu przypadkach usuń zduplikowany krok, aby naprawić przepływ pracy — usuwanie kroków nigdy nie jest ograniczane.
:::

Wybierz tutaj **Zaawansowany (obszar DAG)**, jeśli od początku chcesz korzystać z [Wizualnego projektanta przepływów pracy](/pl/guides/workflows/advanced-workflows/). Wybór nie jest ostateczny: standardowy przepływ pracy możesz później awansować poleceniem **Konwertuj na zaawansowany…** z listy Przepływy pracy.

## Przepływy pracy naprawcze

Jeśli nowy przepływ pracy zakończy się błędem, PlaidCloud może automatycznie uruchomić w odpowiedzi **przepływ pracy naprawczy**. Jest to przydatne do:

- Wysłania powiadomienia do kanału Slack, listy dystrybucyjnej e-mail lub webhooka, aby ktoś zbadał problem
- Uruchomienia przepływu pracy wycofującego zmiany lub czyszczącego, który przywraca znany dobry stan
- Zapisania błędu w tabeli audytu

Przepływ pracy naprawczy jest opcjonalny. Możesz teraz pozostawić to pole puste i w razie potrzeby skonfigurować go później. Przepływ pracy naprawczy uruchamia się tylko przy błędach kończących, a nie przy ostrzeżeniach pojedynczych kroków.

## Następne kroki

- [Eksplorator przepływów pracy](/pl/guides/workflows/workflow-explorer/) — dodaj kroki do nowego przepływu pracy
- [Zaawansowane przepływy pracy](/pl/guides/workflows/advanced-workflows/) — wybierz typ przepływu pracy i buduj na wizualnej kanwie
- [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/) — uruchom przepływ pracy, gdy będzie miał kroki
- [Zarządzanie błędami kroków](/pl/guides/workflows/managing-step-errors/) — debugowanie niepowodzeń
