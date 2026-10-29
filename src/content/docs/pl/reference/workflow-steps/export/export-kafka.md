---
title: Eksportuj Kafka
description: Wyślij każdy wiersz tabeli PlaidCloud do tematu Apache Kafka jako komunikat.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-kafka.md
---

## Opis

Wysyła każdy wiersz tabeli projektu do tematu Apache Kafka jako jeden komunikat. Wysłanego komunikatu nie można cofnąć, więc ponowne uruchomienie kroku wysyła wiersze ponownie. Krok łączy się z Kafką przez [połączenie Apache Kafka](/pl/reference/connectors/databases/apache-kafka/).

## Źródło i cel

| Ustawienie | Wymagane | Co robi |
| --- | --- | --- |
| Tabela źródłowa | Tak | Tabela do wysłania. |
| Połączenie Kafka | Tak | Połączenie, przez które odbywa się wysyłka. |
| Temat | Tak | Temat, do którego wysyłany jest każdy wiersz. |

## Komunikat

| Ustawienie | Co robi |
| --- | --- |
| Kolumna klucza | Kolumna, której wartość jest kluczem komunikatu. Pozostaw puste, aby wysyłać komunikaty bez klucza. |
| Kolumny wartości | Kolumny oddzielone przecinkami, które tworzą wartość komunikatu. Pozostaw puste, aby wysłać każdą kolumnę. |
| Kolumna partycji | Kolumna całkowita wskazująca partycję dla każdego komunikatu. Pozostaw puste, aby wybór pozostawić Kafce. |
| Format wartości | **JSON**, **Tekst** lub **Avro**. |
| Schemat Avro (JSON) | Schemat Avro wartości komunikatu. Wymagany, gdy format to **Avro**. |

## Dostarczanie

| Ustawienie | Domyślnie | Co robi |
| --- | --- | --- |
| Oczekiwanie na dostarczenie (sekundy) | `60` | Jak długo krok czeka na końcu, aż Kafka potwierdzi każdy komunikat. |
| Limit czasu (sekundy) | `10800` | Najdłuższy czas, przez jaki może trwać wysyłka. |
| Dodatkowe ustawienia producenta (JSON) | — | Dodatkowe ustawienia producenta Kafka jako obiekt JSON, na przykład `{"compression.type": "gzip"}`. Przyjmowane są tylko ustawienia dozwolone przez PlaidCloud. |

## Powiązane

- [Importuj Kafka](/pl/reference/workflow-steps/import/import-kafka/)
- [Połączenie Apache Kafka](/pl/reference/connectors/databases/apache-kafka/)
