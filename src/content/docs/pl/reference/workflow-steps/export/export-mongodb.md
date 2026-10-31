---
title: Eksportuj MongoDB
description: Zapisz tabelę PlaidCloud w kolekcji MongoDB jako wstawiane, zastępowane, aktualizowane lub upsertowane dokumenty.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-mongodb.md
---

## Opis

Zapisuje każdy wiersz tabeli projektu w kolekcji MongoDB jako dokument. Kolekcja jest tworzona, jeśli nie istnieje. Krok łączy się z MongoDB przez [połączenie MongoDB](/pl/reference/connectors/databases/mongodb/).

## Źródło i cel

| Ustawienie | Wymagane | Co robi |
| --- | --- | --- |
| Tabela źródłowa | Tak | Tabela do zapisania. |
| Połączenie MongoDB | Tak | Połączenie, przez które odbywa się zapis. |
| Baza danych | Nie | Baza danych do zapisu. Pozostaw puste, aby użyć **Domyślnej bazy danych** połączenia. |
| Kolekcja | Tak | Kolekcja do zapisu. |

## Opcje zapisu

| Ustawienie | Co robi |
| --- | --- |
| Tryb zapisu | **Wstaw jeden dokument na wiersz** (domyślnie), **Zastąp pasujący dokument**, **Zaktualizuj pola pasującego dokumentu**, **Zastąp pasujący dokument lub wstaw** albo **Zaktualizuj pola pasującego dokumentu lub wstaw**. |
| Kolumny dopasowania | Kolumny oddzielone przecinkami, które identyfikują dokument. Wymagane w każdym trybie poza wstawianiem. |
| Usuń wszystkie dokumenty z kolekcji przed zapisem | Najpierw opróżnia kolekcję, tak aby zawierała tylko wiersze z tego uruchomienia. |
| Zatrzymaj po pierwszym nieudanym zapisie | Zatrzymuje się na pierwszym dokumencie odrzuconym przez MongoDB. Wyczyść, aby kontynuować z resztą. |
| Czekaj, aż zapis trafi do dziennika | Czeka, aż MongoDB zapisze każdą partię w swoim dzienniku. |
| Write Concern | Puste dla wartości połączenia, liczba serwerów lub `majority`. |
| Dokumenty na żądanie | Ile dokumentów jest wysyłanych w każdym żądaniu. |

Wstawianie dodaje dokumenty ponownie przy każdym uruchomieniu kroku. Tryby zastępujące lub aktualizujące zostawiają kolekcję taką samą bez względu na to, ile razy krok zostanie uruchomiony, więc użyj jednego z nich, gdy przepływ pracy może zostać uruchomiony dwa razy na tych samych wierszach.

## Powiązane

- [Importuj MongoDB](/pl/reference/workflow-steps/import/import-mongodb/)
- [Połączenie MongoDB](/pl/reference/connectors/databases/mongodb/)
