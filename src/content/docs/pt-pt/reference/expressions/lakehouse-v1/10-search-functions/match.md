---
title: MATCH (Lakehouse v1)
description: MATCH — Pesquisa documentos que contêm as palavras-chave especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

Pesquisa documentos que contêm as palavras-chave especificadas. Tenha em atenção que a função MATCH só pode ser utilizada numa cláusula WHERE.

:::info
A função MATCH do PlaidCloud Lakehouse é inspirada na função [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) do Elasticsearch.
:::

## Sintaxe SQL

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| Parâmetro    | Descrição                                                                                                                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<columns>`  | Uma lista, separada por vírgulas, de nomes de colunas da tabela onde pesquisar as palavras-chave especificadas, com ponderação opcional através da sintaxe (^), que permite atribuir pesos diferentes a cada coluna e, assim, influenciar a importância de cada coluna na pesquisa. |
| `<keywords>` | As palavras-chave a fazer corresponder às colunas especificadas na tabela. Este parâmetro também pode ser utilizado para correspondência de sufixos, em que o termo de pesquisa seguido de um asterisco (*) pode corresponder a qualquer número de carateres ou palavras.                                                                                                                                                                                       |
| `<options>` | Um conjunto de opções de configuração, separadas por ponto e vírgula `;`, que personalizam o comportamento da pesquisa. Consulte a tabela abaixo para obter detalhes. |

| Opção     | Descrição                                                                                                                                                                                           | Exemplo                                                                                               | Explicação                                                                                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Permite corresponder termos dentro de uma Distância de Levenshtein especificada. `fuzziness` pode ser definido como 1 ou 2.                                                                         | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1');                       | Ao fazer corresponder o termo de consulta "box", `fuzziness=1` permite corresponder termos como "fox", uma vez que "box" e "fox" têm uma Distância de Levenshtein de 1.                                              |
| operator  | Especifica como são combinados vários termos de consulta. Pode ser definido como OR (predefinido) ou AND. OR devolve resultados que contêm qualquer um dos termos de consulta, enquanto AND devolve resultados que contêm todos os termos de consulta. | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | Com `operator=AND`, a consulta exige que "action" e "works" estejam ambos presentes nos resultados. Devido a `fuzziness=1`, corresponde a termos como "Actions" e "words", pelo que "Actions speak louder than words" é devolvido. |
| lenient   | Controla se são comunicados erros quando o texto da consulta é inválido. O valor predefinido é `false`. Se definido como `true`, não é comunicado nenhum erro e, se o texto da consulta for inválido, é devolvido um conjunto de resultados vazio. | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true');                       | Se o texto da consulta `()` for inválido, definir `lenient=true` evita que seja gerado um erro e devolve, em vez disso, um conjunto de resultados vazio.                                                              |

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
