---
title: QUERY (Lakehouse v1)
description: QUERY – Sucht nach Dokumenten, die einen angegebenen Abfrageausdruck erfüllen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

Sucht nach Dokumenten, die einen angegebenen Abfrageausdruck erfüllen. Bitte beachten Sie, dass die Funktion QUERY nur in einer WHERE-Klausel verwendet werden kann.

:::info
Die Funktion QUERY von PlaidCloud Lakehouse ist von der Funktion [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) in Elasticsearch inspiriert.
:::

## SQL Syntax

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

Der Abfrageausdruck unterstützt die folgenden Syntaxformen. Bitte beachten Sie, dass `<keyword>` auch für den Suffix-Abgleich verwendet werden kann: Ein Suchbegriff, auf den ein Sternchen (*) folgt, entspricht beliebig vielen Zeichen oder Wörtern.

| Syntax                                                  | Beschreibung | Beispiele                               |
|---------------------------------------------------------|--------------|-----------------------------------------|
| `<column>:<keyword>`                                    | Findet Dokumente, bei denen die angegebene Spalte das angegebene Schlüsselwort enthält. | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | Findet Dokumente, bei denen die angegebene Spalte mindestens eines der in eckigen Klammern aufgeführten Schlüsselwörter enthält. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | Findet Dokumente, bei denen die angegebene Spalte beide oder eines der angegebenen Schlüsselwörter enthält. In Abfragen mit AND und OR hat AND Vorrang vor OR, das heißt, „a AND b OR c“ wird als „(a AND b) OR c“ gelesen. | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | Findet Dokumente, bei denen das angegebene positive Schlüsselwort in der angegebenen Spalte vorkommt, und schließt Dokumente aus, in denen das angegebene negative Schlüsselwort vorkommt. | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | Findet Dokumente, bei denen die angegebene Spalte genau die angegebene Phrase enthält. | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | Findet Dokumente, bei denen das angegebene Schlüsselwort in den angegebenen Spalten vorkommt, wobei die angegebenen Boosts ihre Relevanz in der Suche erhöhen. Mit dieser Syntax können Sie mehreren Spalten unterschiedliche Gewichte zuweisen, um die Suchrelevanz zu beeinflussen. | `QUERY('title:art^5 body:reading^1.2')` |


| Option    | Beschreibung | Beispiel | Erklärung |
|-----------|--------------|----------|-----------|
| fuzziness | Ermöglicht den Abgleich von Begriffen innerhalb einer bestimmten Levenshtein-Distanz. `fuzziness` kann auf 1 oder 2 gesetzt werden. | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1'); | Beim Abgleich des Suchbegriffs „box“ erlaubt `fuzziness=1` Treffer wie „fox“, da „box“ und „fox“ eine Levenshtein-Distanz von 1 haben. |
| operator  | Legt fest, wie mehrere Suchbegriffe verknüpft werden. Kann auf OR (Standard) oder AND gesetzt werden. OR liefert Ergebnisse, die mindestens einen der Suchbegriffe enthalten, AND liefert Ergebnisse, die alle Suchbegriffe enthalten. | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND'); | Mit `operator=AND` müssen in den Ergebnissen sowohl „action“ als auch „works“ vorkommen. Wegen `fuzziness=1` werden auch Begriffe wie „Actions“ und „words“ gefunden, sodass „Actions speak louder than words“ zurückgegeben wird. |
| lenient   | Steuert, ob Fehler gemeldet werden, wenn der Suchtext ungültig ist. Standardmäßig `false`. Bei `true` wird kein Fehler gemeldet, und bei ungültigem Suchtext wird eine leere Ergebnismenge zurückgegeben. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true'); | Ist der Suchtext `()` ungültig, verhindert `lenient=true`, dass ein Fehler ausgelöst wird, und liefert stattdessen eine leere Ergebnismenge. |

## SQL Examples

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
