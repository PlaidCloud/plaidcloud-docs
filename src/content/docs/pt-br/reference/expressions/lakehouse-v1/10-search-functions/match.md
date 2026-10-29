---
title: MATCH (Lakehouse v1)
description: MATCH — Pesquisa documentos que contêm as palavras-chave especificadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

Pesquisa documentos que contêm as palavras-chave especificadas. Observação: a função MATCH só pode ser usada em uma cláusula WHERE.

:::info
A função MATCH do PlaidCloud Lakehouse é inspirada na função [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) do Elasticsearch.
:::

## Sintaxe SQL

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| Parâmetro    | Descrição                                                                                                                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<columns>`  | Uma lista, separada por vírgulas, de nomes de colunas da tabela nas quais pesquisar as palavras-chave especificadas, com ponderação opcional usando a sintaxe (^), que permite atribuir pesos diferentes a cada coluna e influenciar a importância de cada uma delas na pesquisa. |
| `<keywords>` | As palavras-chave a serem comparadas com as colunas especificadas da tabela. Este parâmetro também pode ser usado para correspondência de sufixo, em que o termo de pesquisa seguido de um asterisco (*) pode corresponder a qualquer quantidade de caracteres ou palavras.                                                                                                                                                                                       |
| `<options>` | Um conjunto de opções de configuração, separadas por ponto e vírgula `;`, que personalizam o comportamento da pesquisa. Consulte a tabela abaixo para obter detalhes. |

| Opção     | Descrição                                                                                                                                                                                           | Exemplo                                                                                               | Explicação                                                                                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | Permite correspondência com termos dentro de uma distância de Levenshtein especificada. `fuzziness` pode ser definido como 1 ou 2.                                                                  | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1');                       | Ao buscar o termo "box", `fuzziness=1` permite corresponder a termos como "fox", pois "box" e "fox" têm distância de Levenshtein igual a 1.                                                                          |
| operator  | Especifica como vários termos da consulta são combinados. Pode ser definido como OR (padrão) ou AND. OR retorna resultados que contêm qualquer um dos termos da consulta, enquanto AND retorna resultados que contêm todos os termos. | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | Com `operator=AND`, a consulta exige que "action" e "works" estejam presentes nos resultados. Por causa de `fuzziness=1`, ela corresponde a termos como "Actions" e "words", portanto "Actions speak louder than words" é retornado. |
| lenient   | Controla se erros são informados quando o texto da consulta é inválido. O padrão é `false`. Se definido como `true`, nenhum erro é informado e um conjunto de resultados vazio é retornado quando o texto da consulta é inválido. | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true');                       | Se o texto da consulta `()` for inválido, definir `lenient=true` evita que um erro seja gerado e retorna um conjunto de resultados vazio.                                                                            |

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
