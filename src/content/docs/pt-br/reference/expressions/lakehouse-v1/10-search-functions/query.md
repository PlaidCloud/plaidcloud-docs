---
title: QUERY (Lakehouse v1)
description: QUERY — Pesquisa documentos que satisfazem uma expressão de consulta especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

Pesquisa documentos que satisfazem uma expressão de consulta especificada. Observação: a função QUERY só pode ser usada em uma cláusula WHERE.

:::info
A função QUERY do PlaidCloud Lakehouse é inspirada na função [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) do Elasticsearch.
:::

## Sintaxe SQL

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

A expressão de consulta oferece suporte às sintaxes a seguir. Observação: `<keyword>` também pode ser usado para correspondência de sufixo, em que o termo de pesquisa seguido de um asterisco (*) pode corresponder a qualquer quantidade de caracteres ou palavras.

| Sintaxe                                                 | Descrição                                                                                                                                                                                                                                               | Exemplos                                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | Corresponde a documentos em que a coluna especificada contém a palavra-chave especificada.                                                                                                                                                              | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | Corresponde a documentos em que a coluna especificada contém qualquer uma das palavras-chave listadas entre colchetes. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | Corresponde a documentos em que a coluna especificada contém ambas as palavras-chave ou qualquer uma delas. Em consultas com AND e OR, as operações AND têm prioridade sobre as OR, ou seja, 'a AND b OR c' é lido como '(a AND b) OR c'.                | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | Corresponde a documentos em que a palavra-chave positiva especificada existe na coluna especificada e exclui documentos em que a palavra-chave negativa especificada existe.                                                                            | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | Corresponde a documentos em que a coluna especificada contém exatamente a frase especificada.                                                                                                                                                           | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | Corresponde a documentos em que a palavra-chave especificada existe nas colunas especificadas, com os reforços (boosts) especificados para aumentar a relevância na pesquisa. Esta sintaxe permite definir pesos diferentes para várias colunas e influenciar a relevância da pesquisa. | `QUERY('title:art^5 body:reading^1.2')` |


| Opção     | Descrição                                                                                                                                                                                           | Exemplo                                                                                              | Explicação                                                                                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Permite correspondência com termos dentro de uma distância de Levenshtein especificada. `fuzziness` pode ser definido como 1 ou 2.                                                                  | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | Ao buscar o termo "box", `fuzziness=1` permite corresponder a termos como "fox", pois "box" e "fox" têm distância de Levenshtein igual a 1.                                                                          |
| operator  | Especifica como vários termos da consulta são combinados. Pode ser definido como OR (padrão) ou AND. OR retorna resultados que contêm qualquer um dos termos da consulta, enquanto AND retorna resultados que contêm todos os termos. | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | Com `operator=AND`, a consulta exige que "action" e "works" estejam presentes nos resultados. Por causa de `fuzziness=1`, ela corresponde a termos como "Actions" e "words", portanto "Actions speak louder than words" é retornado. |
| lenient   | Controla se erros são informados quando o texto da consulta é inválido. O padrão é `false`. Se definido como `true`, nenhum erro é informado e um conjunto de resultados vazio é retornado quando o texto da consulta é inválido. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | Se o texto da consulta `()` for inválido, definir `lenient=true` evita que um erro seja gerado e retorna um conjunto de resultados vazio.                                                                            |

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
