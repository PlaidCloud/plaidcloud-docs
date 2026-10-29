---
title: MATCH (Lakehouse v1)
description: MATCH — 指定したキーワードを含むドキュメントを検索します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/match.md
---

指定したキーワードを含むドキュメントを検索します。ご注意：MATCH関数はWHERE句でのみ使用できます。

:::info
PlaidCloud LakehouseのMATCH関数は、Elasticsearchの[MATCH](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-match)を参考にしています。
:::

## SQL構文

```sql
MATCH( '<columns>', '<keywords>'[, '<options>'] )
```

| パラメーター    | 説明                                                                                                                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<columns>`  | 指定したキーワードを検索するテーブルの列名をカンマ区切りで指定したリストです。構文（^）を使って重み付けを指定でき、列ごとに異なる重みを割り当てて、検索における各列の重要度を調整できます。 |
| `<keywords>` | テーブルの指定した列と照合するキーワードです。このパラメーターは後方一致にも使用でき、検索語の後にアスタリスク（*）を付けると、任意の数の文字または単語に一致します。 |
| `<options>` | 検索の動作をカスタマイズする、セミコロン `;` 区切りの設定オプションです。詳細は下の表を参照してください。 |

| オプション    | 説明                                                                                                                                                                                         | 例                                                                                               | 解説                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | 指定したレーベンシュタイン距離以内の語に一致させます。`fuzziness` には1または2を設定できます。                                                                                                    | SELECT id, score(), content FROM t WHERE match(content, 'box', 'fuzziness=1');                       | 検索語「box」に一致させる場合、「box」と「fox」のレーベンシュタイン距離は1であるため、`fuzziness=1` では「fox」のような語にも一致します。                                                                          |
| operator  | 複数の検索語の組み合わせ方を指定します。OR（デフォルト）またはANDを設定できます。ORはいずれかの検索語を含む結果を返し、ANDはすべての検索語を含む結果を返します。     | SELECT id, score(), content FROM t WHERE match(content, 'action works', 'fuzziness=1;operator=AND'); | `operator=AND` では、結果に「action」と「works」の両方が含まれている必要があります。`fuzziness=1` により「Actions」や「words」のような語にも一致するため、「Actions speak louder than words」が返されます。 |
| lenient   | 検索テキストが無効な場合にエラーを報告するかどうかを制御します。デフォルトは `false` です。`true` に設定すると、検索テキストが無効でもエラーは報告されず、空の結果セットが返されます。 | SELECT id, score(), content FROM t WHERE match(content, '()', 'lenient=true');                       | 検索テキスト `()` が無効な場合、`lenient=true` を設定するとエラーが発生せず、代わりに空の結果セットが返されます。                                                                               |

## SQLの例

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
