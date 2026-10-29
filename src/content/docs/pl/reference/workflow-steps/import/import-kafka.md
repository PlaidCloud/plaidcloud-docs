---
title: Importuj Kafka
description: Odczytaj komunikaty tematów Apache Kafka między dwoma offsetami do tabeli PlaidCloud, po jednym wierszu na komunikat.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/import-kafka.md
---

## Opis

Odczytuje komunikaty z jednego lub kilku tematów Apache Kafka do tabeli projektu, po jednym wierszu na komunikat. Krok odczytuje stały zakres: od offsetów początkowych do offsetów końcowych, gdzie `latest` oznacza koniec każdej partycji w chwili uruchomienia kroku. Komunikaty, które napływają w trakcie działania kroku, nie są odczytywane. Krok łączy się z Kafka przez [połączenie Apache Kafka](/pl/reference/connectors/databases/apache-kafka/).

## Źródło i cel

| Ustawienie | Wymagane | Działanie |
| --- | --- | --- |
| Połączenie Kafka | Tak | Połączenie, przez które odbywa się odczyt. |
| Tematy | Jedno z dwóch | Tematy do odczytu, po jednym w wierszu. |
| Wzorzec tematów | Jedno z dwóch | Wyrażenie regularne wybierające tematy do odczytu, używane zamiast pola **Tematy**. |
| Tabela docelowa | Tak | Tabela, do której trafiają komunikaty. |

## Zakres komunikatów

| Ustawienie | Domyślnie | Działanie |
| --- | --- | --- |
| Offsety początkowe | `earliest` | `earliest`, `latest` lub JSON wskazujący offset dla każdej partycji, na przykład `{"orders": {"0": 1200, "1": 980}}`. W JSON `-2` oznacza earliest, a `-1` latest. |
| Offsety końcowe | `latest` | `latest` lub JSON w tej samej postaci co offsety początkowe. |
| Limit komunikatów (0 = wszystkie) | `0` | Maksymalna liczba komunikatów do odczytu. `0` odczytuje każdy komunikat z zakresu. |
| Limit bezczynności (sekundy) | `10` | Odczyt kończy się po tylu sekundach bez nowego komunikatu. |
| Limit czasu (sekundy) | `10800` | Najdłuższy dozwolony czas odczytu. |

Offsety przyjmują zmienne przepływu pracy zapisane jako `{name}`.

## Wartość komunikatu

| Ustawienie | Działanie |
| --- | --- |
| Format wartości | **JSON**, **Tekst** lub **Avro**. |
| Schemat Avro (JSON) | Schemat Avro wartości komunikatu. Wymagany, gdy formatem jest **Avro**. |
| Dodatkowe ustawienia konsumenta (JSON) | Dodatkowe ustawienia konsumenta Kafka jako obiekt JSON, na przykład `{"fetch.min.bytes": 1}`. Akceptowane są tylko ustawienia dozwolone przez PlaidCloud. |

## Mapowanie kolumn

Zmapuj co najmniej jedną kolumnę na karcie mapowania. Kolumna odczytuje jedną z części komunikatu: `key`, `value`, `topic`, `partition`, `offset`, `timestamp`, `timestamp_type` lub `headers`, albo pole przeanalizowanej wartości według jego ścieżki. Ten krok nie ma przycisku **Sprawdź źródło**, więc wpisz kolumny ręcznie.

## Powiązane

- [Eksportuj Kafka](/pl/reference/workflow-steps/export/export-kafka/)
- [Połączenie Apache Kafka](/pl/reference/connectors/databases/apache-kafka/)
