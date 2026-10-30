---
title: QUERY (Lakehouse v1)
description: QUERY — Pesquisa documentos que satisfazem uma expressão de consulta especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

Pesquisa documentos que satisfazem uma expressão de consulta especificada. Tenha em atenção que a função QUERY só pode ser utilizada numa cláusula WHERE.

:::info
A função QUERY do PlaidCloud Lakehouse é inspirada na função [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) do Elasticsearch.
:::

## Sintaxe SQL

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

A expressão de consulta suporta as sintaxes seguintes. Tenha em atenção que `<keyword>` também pode ser utilizado para correspondência de sufixos, em que o termo de pesquisa seguido de um asterisco (*) pode corresponder a qualquer número de carateres ou palavras.                                                                         

| Sintaxe                                                 | Descrição                                                                                                                                                                                                                                               | Exemplos                                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | Corresponde a documentos em que a coluna especificada contém a palavra-chave especificada.                                                                                                                                                              | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | Corresponde a documentos em que a coluna especificada contém qualquer uma das palavras-chave listadas entre parênteses retos. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | Corresponde a documentos em que a coluna especificada contém ambas as palavras-chave especificadas ou qualquer uma delas. Em consultas com AND e OR, as operações AND têm prioridade sobre as OR, ou seja, 'a AND b OR c' é lido como '(a AND b) OR c'. | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | Corresponde a documentos em que a palavra-chave positiva especificada existe na coluna especificada e exclui os documentos em que existe a palavra-chave negativa especificada.                                                                         | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | Corresponde a documentos em que a coluna especificada contém exatamente a frase especificada.                                                                                                                                                           | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | Corresponde a documentos em que a palavra-chave especificada existe nas colunas especificadas, com os reforços (boost) indicados para aumentar a sua relevância na pesquisa. Esta sintaxe permite definir pesos diferentes para várias colunas, de modo a influenciar a relevância da pesquisa. | `QUERY('title:art^5 body:reading^1.2')` |


| Opção     | Descrição                                                                                                                                                                                           | Exemplo                                                                                              | Explicação                                                                                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Permite corresponder termos dentro de uma Distância de Levenshtein especificada. `fuzziness` pode ser definido como 1 ou 2.                                                                         | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | Ao fazer corresponder o termo de consulta "box", `fuzziness=1` permite corresponder termos como "fox", uma vez que "box" e "fox" têm uma Distância de Levenshtein de 1.                                              |
| operator  | Especifica como são combinados vários termos de consulta. Pode ser definido como OR (predefinido) ou AND. OR devolve resultados que contêm qualquer um dos termos de consulta, enquanto AND devolve resultados que contêm todos os termos de consulta. | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | Com `operator=AND`, a consulta exige que "action" e "works" estejam ambos presentes nos resultados. Devido a `fuzziness=1`, corresponde a termos como "Actions" e "words", pelo que "Actions speak louder than words" é devolvido. |
| lenient   | Controla se são comunicados erros quando o texto da consulta é inválido. O valor predefinido é `false`. Se definido como `true`, não é comunicado nenhum erro e, se o texto da consulta for inválido, é devolvido um conjunto de resultados vazio. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | Se o texto da consulta `()` for inválido, definir `lenient=true` evita que seja gerado um erro e devolve, em vez disso, um conjunto de resultados vazio.                                                              |

## Exemplos de SQL

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
