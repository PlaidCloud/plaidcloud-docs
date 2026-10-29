---
title: MATCH (Lakehouse v1)
description: MATCH – Sucht nach Dokumenten, die bestimmte Schlüsselwörter enthalten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

Sucht nach Dokumenten, die bestimmte Schlüsselwörter enthalten. Bitte beachten Sie, dass die Funktion MATCH nur in einer WHERE-Klausel verwendet werden kann.

:::info
Die Funktion MATCH von PlaidCloud Lakehouse ist von der Funktion [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) in Elasticsearch inspiriert.
:::

## SQL Syntax

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| Parameter    | Beschreibung |
|--------------|--------------|
| `<columns>`  | Eine durch Kommas getrennte Liste von Spaltennamen der Tabelle, in denen nach den angegebenen Schlüsselwörtern gesucht wird. Optional ist mit der Syntax (^) eine Gewichtung möglich, mit der Sie jeder Spalte ein anderes Gewicht zuweisen und so ihre Bedeutung für die Suche beeinflussen. |
| `<keywords>` | Die Schlüsselwörter, die mit den angegebenen Spalten der Tabelle abgeglichen werden. Dieser Parameter kann auch für den Suffix-Abgleich verwendet werden: Ein Suchbegriff, auf den ein Sternchen (*) folgt, entspricht beliebig vielen Zeichen oder Wörtern. |
| `<options>` | Eine Reihe von Konfigurationsoptionen, durch Semikolons `;` getrennt, die das Suchverhalten anpassen. Details finden Sie in der folgenden Tabelle. |

| Option    | Beschreibung | Beispiel | Erklärung |
|-----------|--------------|----------|-----------|
| fuzziness | Ermöglicht den Abgleich von Begriffen innerhalb einer bestimmten Levenshtein-Distanz. `fuzziness` kann auf 1 oder 2 gesetzt werden. | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1'); | Beim Abgleich des Suchbegriffs „box“ erlaubt `fuzziness=1` Treffer wie „fox“, da „box“ und „fox“ eine Levenshtein-Distanz von 1 haben. |
| operator  | Legt fest, wie mehrere Suchbegriffe verknüpft werden. Kann auf OR (Standard) oder AND gesetzt werden. OR liefert Ergebnisse, die mindestens einen der Suchbegriffe enthalten, AND liefert Ergebnisse, die alle Suchbegriffe enthalten. | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | Mit `operator=AND` müssen in den Ergebnissen sowohl „action“ als auch „works“ vorkommen. Wegen `fuzziness=1` werden auch Begriffe wie „Actions“ und „words“ gefunden, sodass „Actions speak louder than words“ zurückgegeben wird. |
| lenient   | Steuert, ob Fehler gemeldet werden, wenn der Suchtext ungültig ist. Standardmäßig `false`. Bei `true` wird kein Fehler gemeldet, und bei ungültigem Suchtext wird eine leere Ergebnismenge zurückgegeben. | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true'); | Ist der Suchtext `()` ungültig, verhindert `lenient=true`, dass ein Fehler ausgelöst wird, und liefert stattdessen eine leere Ergebnismenge. |

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
