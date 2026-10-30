---
title: QUERY (Lakehouse v1)
description: QUERY — Busca documentos que cumplen una expresión de consulta especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

Busca documentos que cumplen una expresión de consulta especificada. Tenga en cuenta que la función QUERY solo puede utilizarse en una cláusula WHERE.

:::info
La función QUERY de PlaidCloud Lakehouse está inspirada en [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) de Elasticsearch.
:::

## Sintaxis SQL

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

La expresión de consulta admite las sintaxis siguientes. Tenga en cuenta que `<keyword>` también puede usarse para la coincidencia de sufijos: el término de búsqueda seguido de un asterisco (*) puede coincidir con cualquier número de caracteres o palabras.                                                                         

| Sintaxis                                                | Descripción                                                                                                                                                                                                                                             | Ejemplos                                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | Coincide con los documentos en los que la columna especificada contiene la palabra clave especificada.                                                                                                                                                  | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | Coincide con los documentos en los que la columna especificada contiene alguna de las palabras clave indicadas entre corchetes. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | Coincide con los documentos en los que la columna especificada contiene ambas palabras clave o cualquiera de ellas. En las consultas que combinan AND y OR, las operaciones AND tienen prioridad sobre OR, de modo que 'a AND b OR c' se interpreta como '(a AND b) OR c'. | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | Coincide con los documentos en los que existe la palabra clave positiva especificada en la columna especificada y excluye los documentos en los que existe la palabra clave negativa especificada.                                                       | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | Coincide con los documentos en los que la columna especificada contiene la frase exacta especificada.                                                                                                                                                   | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | Coincide con los documentos en los que la palabra clave especificada existe en las columnas especificadas, con los factores de refuerzo indicados para aumentar su relevancia en la búsqueda. Esta sintaxis permite asignar pesos distintos a varias columnas para influir en la relevancia de la búsqueda. | `QUERY('title:art^5 body:reading^1.2')` |


| Opción    | Descripción                                                                                                                                                                                         | Ejemplo                                                                                              | Explicación                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Permite coincidencias con términos dentro de una distancia de Levenshtein especificada. `fuzziness` puede ser 1 o 2.                                                                                | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | Al buscar el término "box", `fuzziness=1` permite coincidir con términos como "fox", ya que "box" y "fox" tienen una distancia de Levenshtein de 1.                                                                  |
| operator  | Especifica cómo se combinan varios términos de la consulta. Puede ser OR (predeterminado) o AND. OR devuelve los resultados que contienen cualquiera de los términos; AND devuelve los que contienen todos los términos. | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | Con `operator=AND`, la consulta exige que tanto "action" como "works" estén presentes en los resultados. Debido a `fuzziness=1`, coincide con términos como "Actions" y "words", por lo que se devuelve "Actions speak louder than words". |
| lenient   | Controla si se notifican errores cuando el texto de la consulta no es válido. El valor predeterminado es `false`. Si se establece en `true`, no se notifica ningún error y se devuelve un conjunto de resultados vacío cuando el texto de la consulta no es válido. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | Si el texto de la consulta `()` no es válido, establecer `lenient=true` evita que se genere un error y devuelve en su lugar un conjunto de resultados vacío.                                                         |

## Ejemplos de SQL

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
