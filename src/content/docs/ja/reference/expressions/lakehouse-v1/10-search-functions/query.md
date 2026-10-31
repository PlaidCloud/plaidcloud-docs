---
title: QUERY (Lakehouse v1)
description: QUERY — 指定したクエリ式を満たすドキュメントを検索します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

指定したクエリ式を満たすドキュメントを検索します。ご注意：QUERY関数はWHERE句でのみ使用できます。

:::info
PlaidCloud LakehouseのQUERY関数は、Elasticsearchの[QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query)を参考にしています。
:::

## SQL構文

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

クエリ式では次の構文を使用できます。`<keyword>` は後方一致にも使用でき、検索語の後にアスタリスク（*）を付けると、任意の数の文字または単語に一致します。

| 構文                                                  | 説明                                                                                                                                                                                                                                             | 例                                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | 指定した列に指定したキーワードを含むドキュメントに一致します。                                                                                                                                                                            | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | 指定した列に、角かっこ内に列挙したキーワードのいずれかを含むドキュメントに一致します。 | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | 指定した列に、指定した両方のキーワード、またはいずれかのキーワードを含むドキュメントに一致します。ANDとORの両方を含むクエリでは、ANDがORより優先されるため、'a AND b OR c' は '(a AND b) OR c' として解釈されます。                       | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | 指定した列に肯定キーワードが存在し、否定キーワードが存在しないドキュメントに一致します。                                                                                               | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | 指定した列に、指定したフレーズと完全に一致する語句を含むドキュメントに一致します。                                                                                                                                                                       | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | 指定した列に指定したキーワードが存在するドキュメントに一致し、指定したブーストで検索における関連度を高めます。この構文では、複数の列に異なる重みを設定して、検索の関連度を調整できます。 | `QUERY('title:art^5 body:reading^1.2')` |


| オプション    | 説明                                                                                                                                                                                         | 例                                                                                              | 解説                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | 指定したレーベンシュタイン距離以内の語に一致させます。`fuzziness` には1または2を設定できます。                                                                                                    | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | 検索語「box」に一致させる場合、「box」と「fox」のレーベンシュタイン距離は1であるため、`fuzziness=1` では「fox」のような語にも一致します。                                                                          |
| operator  | 複数の検索語の組み合わせ方を指定します。OR（デフォルト）またはANDを設定できます。ORはいずれかの検索語を含む結果を返し、ANDはすべての検索語を含む結果を返します。     | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | `operator=AND` では、結果に「action」と「works」の両方が含まれている必要があります。`fuzziness=1` により「Actions」や「words」のような語にも一致するため、「Actions speak louder than words」が返されます。 |
| lenient   | 検索テキストが無効な場合にエラーを報告するかどうかを制御します。デフォルトは `false` です。`true` に設定すると、検索テキストが無効でもエラーは報告されず、空の結果セットが返されます。 | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | 検索テキスト `()` が無効な場合、`lenient=true` を設定するとエラーが発生せず、代わりに空の結果セットが返されます。                                                                               |

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
