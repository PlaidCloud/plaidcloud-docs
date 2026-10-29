---
title: MATCH (Lakehouse v1)
description: MATCH — wyszukuje dokumenty zawierające określone słowa kluczowe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

Wyszukuje dokumenty zawierające określone słowa kluczowe. Uwaga: funkcji MATCH można używać wyłącznie w klauzuli WHERE.

:::info
Funkcja MATCH w PlaidCloud Lakehouse jest wzorowana na funkcji [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) z Elasticsearch.
:::

## Składnia SQL

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| Parametr     | Opis                                                                                                                                                                                                                                                      |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<columns>`  | Rozdzielana przecinkami lista nazw kolumn tabeli, w których wyszukiwane są podane słowa kluczowe, z opcjonalnym ważeniem przy użyciu składni (^), które pozwala przypisać różne wagi poszczególnym kolumnom i wpływać na ich znaczenie w wyszukiwaniu. |
| `<keywords>` | Słowa kluczowe dopasowywane do podanych kolumn tabeli. Parametr ten może być też używany do dopasowania przyrostkowego, w którym szukany termin zakończony gwiazdką (*) może pasować do dowolnej liczby znaków lub słów.                                                                                                                                                                                       |
| `<options>` | Zestaw opcji konfiguracji, rozdzielonych średnikami `;`, które dostosowują zachowanie wyszukiwania. Szczegóły znajdziesz w poniższej tabeli. |

| Opcja     | Opis                                                                                                                                                                                                | Przykład                                                                                              | Wyjaśnienie                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Umożliwia dopasowanie terminów w granicach określonej odległości Levenshteina. Opcję `fuzziness` można ustawić na 1 lub 2.                                                           | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1');                       | Przy dopasowywaniu terminu „box” ustawienie `fuzziness=1` pozwala dopasować terminy takie jak „fox”, ponieważ „box” i „fox” dzieli odległość Levenshteina równa 1.                                                   |
| operator  | Określa sposób łączenia wielu terminów zapytania. Można ustawić OR (domyślnie) lub AND. OR zwraca wyniki zawierające dowolny z terminów zapytania, a AND zwraca wyniki zawierające wszystkie terminy zapytania. | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | Przy `operator=AND` zapytanie wymaga, aby w wynikach występowały zarówno „action”, jak i „works”. Dzięki `fuzziness=1` dopasowywane są terminy takie jak „Actions” i „words”, więc zwracane jest „Actions speak louder than words”. |
| lenient   | Określa, czy zgłaszane są błędy, gdy tekst zapytania jest nieprawidłowy. Domyślnie `false`. Po ustawieniu `true` błąd nie jest zgłaszany, a w przypadku nieprawidłowego tekstu zapytania zwracany jest pusty zbiór wyników. | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true');                       | Jeśli tekst zapytania `()` jest nieprawidłowy, ustawienie `lenient=true` zapobiega zgłoszeniu błędu i zamiast tego zwraca pusty zbiór wyników.                                                                       |

## Przykłady SQL

```sql
CREATE TABLE test(title STRING, body STRING);

CREATE INVERTED INDEX idx ON test(title, body);

INSERT INTO test VALUES
('The Importance of Reading', 'Reading is a crucial skill that opens up a world of knowledge and imagination.'),
('The Benefits of Exercise', 'Exercise is essential for maintaining a healthy lifestyle.'),
('The Power of Perseverance', 'Perseverance is the key to overcoming obstacles and achieving success.'),
('The Art of Communication', 'Effective communication is crucial in everyday life.'),
('The Impact of Technology on Society', 'Technology has revolutionized our society in countless ways.');

-- Retrieve documents where the 'title' column matches 'art power'
SELECT * FROM test WHERE MATCH('title', 'art power');

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains values that start with 'The' followed by any characters
SELECT * FROM test WHERE MATCH('title', 'The*')

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │
│           Nullable(String)          │                                Nullable(String)                                │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │
│ The Benefits of Exercise            │ Exercise is essential for maintaining a healthy lifestyle.                     │
│ The Power of Perseverance           │ Perseverance is the key to overcoming obstacles and achieving success.         │
│ The Art of Communication            │ Effective communication is crucial in everyday life.                           │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where either the 'title' or 'body' column matches 'knowledge technology'
SELECT *, score() FROM test WHERE MATCH('title, body', 'knowledge technology');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │  score()  │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.1550591 │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │ 2.6830134 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where either the 'title' or 'body' column matches 'knowledge technology', with weighted importance on both columns
SELECT *, score() FROM test WHERE MATCH('title^5, body^1.2', 'knowledge technology');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │  score()  │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.3860708 │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │ 7.8053584 │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'body' column contains both "knowledge" and "imagination" (allowing for minor typos).
SELECT * FROM test WHERE MATCH('body', 'knowledg imaginatio', 'fuzziness = 1; operator = AND');

-[ RECORD 1 ]-----------------------------------
title: The Importance of Reading
 body: Reading is a crucial skill that opens up a world of knowledge and imagination.
```
