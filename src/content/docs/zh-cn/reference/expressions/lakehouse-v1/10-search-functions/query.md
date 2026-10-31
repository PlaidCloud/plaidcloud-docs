---
title: QUERY（Lakehouse v1）
description: QUERY — 搜索满足指定查询表达式的文档。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

搜索满足指定查询表达式的文档。请注意，QUERY 函数只能用于 WHERE 子句。

:::info
PlaidCloud Lakehouse 的 QUERY 函数受 Elasticsearch 的 [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query) 启发。
:::

## SQL 语法

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

查询表达式支持以下语法。请注意，`<keyword>` 也可用于后缀匹配：搜索词后加星号 (*) 可匹配任意数量的字符或单词。

| 语法 | 说明 | 示例 |
|------|------|------|
| `<column>:<keyword>` | 匹配指定列包含指定关键词的文档。 | `QUERY('title:power')` |
| `<column>:IN [<keyword1>, <keyword2>...]` | 匹配指定列包含方括号内任一关键词的文档。 | `QUERY('title:IN [power, art]')` |
| `<column>:<keyword> AND / OR <keyword>` | 匹配指定列同时包含或任一包含指定关键词的文档。在同时包含 AND 和 OR 的查询中，AND 运算优先于 OR，即 'a AND b OR c' 按 '(a AND b) OR c' 解读。 | `QUERY('title:power AND art')` |
| `<column>:+<keyword> -<keyword>` | 匹配指定列中存在指定正向关键词的文档，并排除存在指定负向关键词的文档。 | `QUERY('title:+the -reading')` |
| `<column>:"<phrase>"` | 匹配指定列包含完全相同的指定短语的文档。 | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | 匹配指定列中存在指定关键词的文档，并使用指定的提升值提高其在搜索中的相关度。此语法允许为多个列设置不同的权重，以影响搜索相关度。 | `QUERY('title:art^5 body:reading^1.2')` |

| 选项      | 说明 | 示例 | 解释 |
|-----------|------|------|------|
| fuzziness | 允许匹配在指定莱文斯坦距离内的词项。`fuzziness` 可设为 1 或 2。 | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1'); | 匹配查询词 "box" 时，`fuzziness=1` 允许匹配 "fox" 等词项，因为 "box" 与 "fox" 的莱文斯坦距离为 1。 |
| operator  | 指定多个查询词的组合方式。可设为 OR（默认）或 AND。OR 返回包含任一查询词的结果，AND 返回包含所有查询词的结果。 | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND'); | 使用 `operator=AND` 时，查询要求结果中同时包含 "action" 和 "works"。由于设置了 `fuzziness=1`，它可匹配 "Actions" 和 "words" 等词项，因此会返回 "Actions speak louder than words"。 |
| lenient   | 控制查询文本无效时是否报错。默认为 `false`。设为 `true` 时，查询文本无效也不会报错，而是返回空结果集。 | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true'); | 如果查询文本 `()` 无效，设置 `lenient=true` 可避免抛出错误，并改为返回空结果集。 |

## SQL 示例

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
