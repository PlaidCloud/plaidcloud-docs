---
title: MATCH（Lakehouse v1）
description: MATCH — 搜索包含指定关键词的文档。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

搜索包含指定关键词的文档。请注意，MATCH 函数只能用于 WHERE 子句。

:::info
PlaidCloud Lakehouse 的 MATCH 函数受 Elasticsearch 的 [MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match) 启发。
:::

## SQL 语法

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| 参数         | 说明 |
|--------------|------|
| `<columns>`  | 以逗号分隔的列名列表，指定在表中搜索关键词的列；可使用 (^) 语法为每列设置权重，从而影响各列在搜索中的重要性。 |
| `<keywords>` | 要与表中指定列进行匹配的关键词。此参数也可用于后缀匹配：搜索词后加星号 (*) 可匹配任意数量的字符或单词。 |
| `<options>` | 一组以分号 `;` 分隔的配置选项，用于自定义搜索行为。详见下表。 |

| 选项      | 说明 | 示例 | 解释 |
|-----------|------|------|------|
| fuzziness | 允许匹配在指定莱文斯坦距离内的词项。`fuzziness` 可设为 1 或 2。 | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1'); | 匹配查询词 "box" 时，`fuzziness=1` 允许匹配 "fox" 等词项，因为 "box" 与 "fox" 的莱文斯坦距离为 1。 |
| operator  | 指定多个查询词的组合方式。可设为 OR（默认）或 AND。OR 返回包含任一查询词的结果，AND 返回包含所有查询词的结果。 | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | 使用 `operator=AND` 时，查询要求结果中同时包含 "action" 和 "works"。由于设置了 `fuzziness=1`，它可匹配 "Actions" 和 "words" 等词项，因此会返回 "Actions speak louder than words"。 |
| lenient   | 控制查询文本无效时是否报错。默认为 `false`。设为 `true` 时，查询文本无效也不会报错，而是返回空结果集。 | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true'); | 如果查询文本 `()` 无效，设置 `lenient=true` 可避免抛出错误，并改为返回空结果集。 |

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
