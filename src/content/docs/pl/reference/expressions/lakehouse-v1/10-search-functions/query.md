---
title: QUERY (Lakehouse v1)
description: QUERY — wyszukuje dokumenty spełniające określone wyrażenie zapytania.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

Wyszukuje dokumenty spełniające określone wyrażenie zapytania. Uwaga: funkcji QUERY można używać wyłącznie w klauzuli WHERE.

:::info
Funkcja QUERY w PlaidCloud Lakehouse jest wzorowana na funkcji [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) z Elasticsearch.
:::

## Składnia SQL

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

Wyrażenie zapytania obsługuje następujące składnie. Uwaga: `<keyword>` może być też używane do dopasowania przyrostkowego, w którym szukany termin zakończony gwiazdką (*) może pasować do dowolnej liczby znaków lub słów.

| Składnia                                                | Opis                                                                                                                                                                                                                                                    | Przykłady                               |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | Dopasowuje dokumenty, w których podana kolumna zawiera podane słowo kluczowe.                                                                                                                                                                           | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | Dopasowuje dokumenty, w których podana kolumna zawiera dowolne ze słów kluczowych wymienionych w nawiasach kwadratowych. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | Dopasowuje dokumenty, w których podana kolumna zawiera oba podane słowa kluczowe lub jedno z nich. W zapytaniach zawierających jednocześnie AND i OR operacje AND mają pierwszeństwo przed OR, co oznacza, że „a AND b OR c” jest odczytywane jako „(a AND b) OR c”. | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | Dopasowuje dokumenty, w których podane słowo kluczowe z plusem występuje w podanej kolumnie, i wyklucza dokumenty, w których występuje podane słowo kluczowe z minusem.                                                                                  | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | Dopasowuje dokumenty, w których podana kolumna zawiera dokładnie podaną frazę.                                                                                                                                                                          | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | Dopasowuje dokumenty, w których podane słowo kluczowe występuje w podanych kolumnach, ze wskazanymi wzmocnieniami zwiększającymi ich trafność w wyszukiwaniu. Ta składnia pozwala ustawić różne wagi dla wielu kolumn, aby wpływać na trafność wyszukiwania. | `QUERY('title:art^5 body:reading^1.2')` |


| Opcja     | Opis                                                                                                                                                                                                | Przykład                                                                                             | Wyjaśnienie                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Umożliwia dopasowanie terminów w granicach określonej odległości Levenshteina. Opcję `fuzziness` można ustawić na 1 lub 2.                                                                          | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | Przy dopasowywaniu terminu „box” ustawienie `fuzziness=1` pozwala dopasować terminy takie jak „fox”, ponieważ „box” i „fox” dzieli odległość Levenshteina równa 1.                                                   |
| operator  | Określa sposób łączenia wielu terminów zapytania. Można ustawić OR (domyślnie) lub AND. OR zwraca wyniki zawierające dowolny z terminów zapytania, a AND zwraca wyniki zawierające wszystkie terminy zapytania. | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | Przy `operator=AND` zapytanie wymaga, aby w wynikach występowały zarówno „action”, jak i „works”. Dzięki `fuzziness=1` dopasowywane są terminy takie jak „Actions” i „words”, więc zwracane jest „Actions speak louder than words”. |
| lenient   | Określa, czy zgłaszane są błędy, gdy tekst zapytania jest nieprawidłowy. Domyślnie `false`. Po ustawieniu `true` błąd nie jest zgłaszany, a w przypadku nieprawidłowego tekstu zapytania zwracany jest pusty zbiór wyników. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | Jeśli tekst zapytania `()` jest nieprawidłowy, ustawienie `lenient=true` zapobiega zgłoszeniu błędu i zamiast tego zwraca pusty zbiór wyników.                                                                       |

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

-- Retrieve documents where the 'title' column contains the keyword 'power'
SELECT * FROM test WHERE QUERY('title:power');

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains values that start with 'The' followed by any characters
SELECT * FROM test WHERE QUERY('title:The*');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                      body                                      │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────────────┤
│ The Importance of Reading           │ Reading is a crucial skill that opens up a world of knowledge and imagination. │
│ The Benefits of Exercise            │ Exercise is essential for maintaining a healthy lifestyle.                     │
│ The Power of Perseverance           │ Perseverance is the key to overcoming obstacles and achieving success.         │
│ The Art of Communication            │ Effective communication is crucial in everyday life.                           │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.                   │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains either the keyword 'power' or 'art'
SELECT * FROM test WHERE QUERY('title:power OR art');

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT * FROM test WHERE QUERY('title:IN [power, art]')

┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                  body                                  │
│      Nullable(String)     │                            Nullable(String)                            │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Power of Perseverance │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the positive keyword 'the' but not 'reading'
SELECT * FROM test WHERE QUERY('title:+the -reading');

┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                title                │                                  body                                  │
├─────────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ The Benefits of Exercise            │ Exercise is essential for maintaining a healthy lifestyle.             │
│ The Power of Perseverance           │ Perseverance is the key to overcoming obstacles and achieving success. │
│ The Art of Communication            │ Effective communication is crucial in everyday life.                   │
│ The Impact of Technology on Society │ Technology has revolutionized our society in countless ways.           │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the exact phrase 'Benefits of Exercise'
SELECT * FROM test WHERE QUERY('title:"Benefits of Exercise"');

┌───────────────────────────────────────────────────────────────────────────────────────┐
│           title          │                            body                            │
├──────────────────────────┼────────────────────────────────────────────────────────────┤
│ The Benefits of Exercise │ Exercise is essential for maintaining a healthy lifestyle. │
└───────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'title' column contains the keyword 'art' with a boost of 5 and the 'body' column contains the keyword 'reading' with a boost of 1.2
SELECT *, score() FROM test WHERE QUERY('title:art^5 body:reading^1.2');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           title           │                                      body                                      │  score()  │
├───────────────────────────┼────────────────────────────────────────────────────────────────────────────────┼───────────┤
│ The Importance of Reading │ Reading is a crucial skill that opens up a world of knowledge and imagination. │ 1.3860708 │
│ The Art of Communication  │ Effective communication is crucial in everyday life.                           │ 7.1992116 │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

-- Retrieve documents where the 'body' column contains both "knowledge" and "imagination" (allowing for minor typos).
SELECT * FROM test WHERE QUERY('body:knowledg OR imaginatio', 'fuzziness = 1; operator = AND');

-[ RECORD 1 ]-----------------------------------
title: The Importance of Reading
 body: Reading is a crucial skill that opens up a world of knowledge and imagination.
```
