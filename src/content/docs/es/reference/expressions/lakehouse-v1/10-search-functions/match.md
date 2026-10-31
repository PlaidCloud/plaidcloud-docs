---
title: MATCH (Lakehouse v1)
description: MATCH — Busca documentos que contienen las palabras clave especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

Busca documentos que contienen las palabras clave especificadas. Tenga en cuenta que la función MATCH solo puede utilizarse en una cláusula WHERE.

:::info
La función MATCH de PlaidCloud Lakehouse está inspirada en [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) de Elasticsearch.
:::

## Sintaxis SQL

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| Parámetro    | Descripción                                                                                                                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<columns>`  | Una lista separada por comas de nombres de columnas de la tabla en las que se buscan las palabras clave especificadas, con ponderación opcional mediante la sintaxis (^), que permite asignar un peso distinto a cada columna e influir en la importancia de cada una en la búsqueda. |
| `<keywords>` | Las palabras clave que se comparan con las columnas especificadas de la tabla. Este parámetro también puede usarse para la coincidencia de sufijos: el término de búsqueda seguido de un asterisco (*) puede coincidir con cualquier número de caracteres o palabras.                                                                                                                                                                                       |
| `<options>` | Un conjunto de opciones de configuración, separadas por punto y coma `;`, que personalizan el comportamiento de la búsqueda. Consulte la tabla siguiente para más detalles. |

| Opción    | Descripción                                                                                                                                                                                         | Ejemplo                                                                                               | Explicación                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Permite coincidencias con términos dentro de una distancia de Levenshtein especificada. `fuzziness` puede ser 1 o 2.                                                                                                    | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1');                       | Al buscar el término "box", `fuzziness=1` permite coincidir con términos como "fox", ya que "box" y "fox" tienen una distancia de Levenshtein de 1.                                                                          |
| operator  | Especifica cómo se combinan varios términos de la consulta. Puede ser OR (predeterminado) o AND. OR devuelve los resultados que contienen cualquiera de los términos; AND devuelve los que contienen todos los términos.     | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | Con `operator=AND`, la consulta exige que tanto "action" como "works" estén presentes en los resultados. Debido a `fuzziness=1`, coincide con términos como "Actions" y "words", por lo que se devuelve "Actions speak louder than words". |
| lenient   | Controla si se notifican errores cuando el texto de la consulta no es válido. El valor predeterminado es `false`. Si se establece en `true`, no se notifica ningún error y se devuelve un conjunto de resultados vacío cuando el texto de la consulta no es válido. | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true');                       | Si el texto de la consulta `()` no es válido, establecer `lenient=true` evita que se genere un error y devuelve en su lugar un conjunto de resultados vacío.                                                                               |

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
