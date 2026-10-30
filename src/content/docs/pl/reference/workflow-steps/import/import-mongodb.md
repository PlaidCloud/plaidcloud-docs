---
title: Importuj MongoDB
description: Odczytaj kolekcję MongoDB lub wynik potoku agregacji do tabeli PlaidCloud jako krok przepływu pracy.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-mongodb.md
---

## Opis

Odczytuje dokumenty kolekcji MongoDB do tabeli projektu, po jednym wierszu na dokument. Użyj filtra, aby odczytać tylko potrzebne dokumenty, lub potoku agregacji, aby przekształcić je w MongoDB przed zapisaniem. Krok łączy się z MongoDB przez [połączenie MongoDB](/pl/reference/connectors/databases/mongodb/).

## Źródło i cel

| Ustawienie | Wymagane | Działanie |
| --- | --- | --- |
| Połączenie MongoDB | Tak | Połączenie, przez które odbywa się odczyt. |
| Baza danych | Nie | Baza danych do odczytu. Pozostaw puste, aby użyć **Domyślnej bazy danych** połączenia. |
| Kolekcja | Tak | Kolekcja do odczytu. |
| Tabela docelowa | Tak | Tabela, do której trafiają dokumenty. Musi to być tabela, a nie widok. |

## Zapytanie

| Ustawienie | Działanie |
| --- | --- |
| Filtr (JSON) | Filtr zapytania MongoDB jako obiekt JSON, na przykład `{"status": "open"}`. Odczytywane są tylko pasujące dokumenty. |
| Potok agregacji (JSON) | Potok agregacji jako tablica JSON, na przykład `[{"$match": {"status": "open"}}]`. Gdy jest ustawiony, kolekcja jest agregowana zamiast filtrowana. Potok z etapem `$out` lub `$merge` jest odrzucany, ponieważ zapisywałby dane w MongoDB. |
| Limit wierszy (0 = wszystkie) | Maksymalna liczba dokumentów do odczytu. `0` odczytuje wszystkie. |
| Limit czasu (sekundy) | Jak długo MongoDB może wykonywać odczyt, zanim go przerwie. |
| Dokumenty próbkowane dla kolumn | Gdy krok nie deklaruje kolumn, określa, ile dokumentów, licząc od pierwszego, decyduje o kolumnach i ich typach: każde pole najwyższego poziomu, które zawierają, staje się kolumną. Domyślnie 1000. |

Filtr i potok przyjmują zmienne przepływu pracy zapisane jako `{name}`, na przykład `{"region": "{region}"}`. Wartość każdej zmiennej jest wstawiana jako pojedynczy ciąg znaków lub liczba JSON, więc zmienna nie może dodać do zapytania kluczy ani operatorów. Niezdefiniowana zmienna zatrzymuje krok z błędem wskazującym jej nazwę.

## Mapowanie kolumn

Zmapuj każde pole dokumentu na kolumnę tabeli docelowej na karcie mapowania. Kolumna odczytuje pole dokumentu o tej samej nazwie. Kolekcja, która nie istnieje, kończy się z ostrzeżeniem i pozostawia tabelę docelową pustą.

## Powiązane

- [Eksportuj MongoDB](/pl/reference/workflow-steps/export/export-mongodb/)
- [Połączenie MongoDB](/pl/reference/connectors/databases/mongodb/)
