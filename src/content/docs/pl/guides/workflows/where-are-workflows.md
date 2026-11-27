---
title: Gdzie są przepływy pracy
description: Przechodź do przepływów pracy PlaidCloud w swoich projektach i zarządzaj nimi za pomocą interfejsu przepływów pracy i narzędzi nawigacji po projektach.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Przepływy pracy znajdują się w projektach. Aby je znaleźć:

1. W górnym menu otwórz **Projekty**.
2. Kliknij projekt zawierający przepływy pracy, których szukasz.
3. Przejdź na kartę **Przepływy pracy**.

Zobaczysz każdy przepływ pracy w projekcie, uporządkowany w hierarchii przypominającej foldery.

## Co zobaczysz dla każdego przepływu pracy

- **Stan** — uruchomiony, ukończony normalnie lub zakończony z ostrzeżeniem albo błędem
- Znaczniki czasu **Utworzono** i **ostatnia aktualizacja** oraz nazwy osób odpowiedzialnych
- **Organizacja w foldery** — przepływy pracy można grupować w zagnieżdżone foldery, aby łatwiej zarządzać nimi w dużych projektach

Kliknij przepływ pracy dwukrotnie, aby otworzyć **Eksplorator przepływów pracy**, w którym możesz wyświetlać kroki, uruchamiać cały przepływ pracy, uruchamiać pojedynczy krok lub wybrać zakres.

## Dlaczego przepływ pracy może nie być widoczny

Przepływy pracy, które widzisz, zależą od dwóch rzeczy:

- **Dostęp do projektu** — administrator obszaru roboczego przyznaje Ci dostęp do określonych projektów. Jeśli oczekujesz, że zobaczysz projekt, ale go nie widzisz, poproś właściciela projektu o dodanie Cię.
- **Rola wyświetlania** — w projekcie masz przypisaną jedną z trzech ról:
  - **Architekt** — może widzieć i edytować wszystko
  - **Menedżer** — może widzieć i uruchamiać przepływy pracy, ale nie może ich modyfikować
  - **Eksplorator** — ograniczona widoczność; niektóre przepływy pracy mogą być ukryte

Jeśli oczekujesz, że zobaczysz konkretne przepływy pracy, a ich nie widzisz, Twoja rola może je odfiltrowywać. Architekt projektu może potwierdzić, co powinieneś widzieć.

Twoja rola decyduje także o tym, czy możesz zmienić krok. Jeśli możesz otworzyć przepływ pracy, ale nie możesz go modyfikować, formularz kroku otwiera się tylko do odczytu — jego pola są wyłączone, a przycisk **Zapisz** jest ukryty — dzięki czemu możesz odczytać konfigurację kroku bez możliwości jej zmiany. Dotyczy to każdego miejsca, w którym formularz się otwiera: ikony koła zębatego i menu prawego przycisku myszy w tabeli przepływu pracy, kanwy wizualnej, siatki **Kroki** projektu oraz menu **Nowy krok**.

## Niezapisane zmiany w oknie kroku

Okno kroku oznacza niezapisane zmiany znakiem **•** w tytule. Zamknięcie okna klawiszem **Esc**, przyciskiem **X**, **Anuluj** lub przyciskiem jego karty wyświetla pytanie **Odrzucić niezapisane zmiany?**, aby edycja nie została utracona przypadkiem. Wybierz **Odrzuć**, aby zamknąć bez zapisywania, albo wróć, aby kontynuować edycję.

## Krok zmienił się od czasu jego otwarcia

**Zapisz** w formularzu kroku nigdy nie nadpisuje zmiany zapisanej po otwarciu formularza, niezależnie od tego, czy wprowadził ją Weave, czy ktoś inny. Nic nie zostaje zapisane: formularz pozostaje otwarty z Twoimi zmianami, a ostrzeżenie zatytułowane **Aktualizacja nie powiodła się** informuje: *Ten krok zmienił się od czasu jego otwarcia. Załaduj go ponownie, aby zobaczyć najnowszą wersję; niezapisane zmiany zostaną utracone.* Wybierz **Odśwież**, aby pokazać krok w obecnym stanie, a następnie wprowadź zmiany ponownie. Dodanie lub usunięcie jednej z etykiet kroku nie jest uznawane za zmianę. Jeśli podczas zapisu kroku trafiają na niego kolejne zapisy, komunikat **Aktualizacja nie powiodła się** informuje: *Ten krok zmieniał się podczas zapisywania. Spróbuj ponownie.* i nic nie zostaje zapisane; zapisz ponownie, gdy ustaną.

Przez REST API `GET /rest/v1/analyze/projects/{project_id}/transform/{step_id}` zwraca krok wraz z `_etag`. Odeślij go jako `if_match` w `PUT` pod tę samą ścieżkę, a zapis nadpisujący nowszą zmianę zostanie odrzucony z kodem `412` i nic nie zostanie zapisane. Bez niego wygrywa ostatni zapis. `PUT`, który wyprzedzają kolejne zapisy, jest odrzucany z kodem `503` i tym samym komunikatem *Ten krok zmieniał się podczas zapisywania. Spróbuj ponownie.*, a nic nie zostaje zapisane. Gdy `PUT` zawiera `labels` i nie udało się zapisać tylko ich, odpowiada kodem `503` i komunikatem *Krok został zapisany, ale jego etykiety nie: zmieniały się podczas zapisywania. Ustaw etykiety ponownie.* Asystenci AI połączeni przez MCP otrzymują to samo sprawdzenie, przekazując `_etag` z `step_describe` jako `if_match` do `step_upsert`.

## Następne kroki

- [Eksplorator przepływów pracy](/pl/guides/workflows/workflow-explorer/) — co robić w otwartym przepływie pracy
- [Utwórz przepływ pracy](/pl/guides/workflows/create-workflow/) — rozpocznij nowy
- [Uruchom przepływ pracy](/pl/guides/workflows/run-a-workflow/) — wykonaj od początku do końca
