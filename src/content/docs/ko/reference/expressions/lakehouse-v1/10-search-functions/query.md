---
title: QUERY (Lakehouse v1)
description: QUERY — 지정한 쿼리 식을 만족하는 문서를 검색합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-search-functions/query.md
---

지정한 쿼리 식을 만족하는 문서를 검색합니다. 참고: QUERY 함수는 WHERE 절에서만 사용할 수 있습니다.

:::info
PlaidCloud Lakehouse의 QUERY 함수는 Elasticsearch의 [QUERY](https://www.elastic.co/guide/en/elasticsearch/reference/current/sql-functions-search.html#sql-functions-search-query)에서 착안했습니다.
:::

## SQL Syntax

```sql
QUERY( '<query_expr>'[, '<options>'] )
```

쿼리 식은 다음 구문을 지원합니다. 참고: `<keyword>`는 접미사 일치에도 사용할 수 있으며, 검색어 뒤에 별표(*)를 붙이면 임의 개수의 문자나 단어와 일치합니다.

| 구문                                                  | 설명                                                                                                                                                                                                                                             | 예시                                |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `<column>:<keyword>`                                    | 지정한 열에 지정한 키워드가 포함된 문서와 일치합니다.                                                                                                                                                                            | `QUERY('title:power')`                  |
| `<column>:IN [<keyword1>, <keyword2>...]` | 지정한 열에 대괄호 안에 나열된 키워드 중 하나라도 포함된 문서와 일치합니다. | `QUERY('title:IN [power, art]')`|
| `<column>:<keyword> AND / OR <keyword>`                 | 지정한 열에 지정한 키워드가 모두 또는 하나라도 포함된 문서와 일치합니다. AND와 OR가 함께 있는 쿼리에서는 AND 연산이 OR보다 먼저 계산되므로 'a AND b OR c'는 '(a AND b) OR c'로 해석됩니다.                       | `QUERY('title:power AND art')`          |
| `<column>:+<keyword> -<keyword>`                        | 지정한 열에 지정한 포함 키워드가 있는 문서와 일치하고, 지정한 제외 키워드가 있는 문서는 제외합니다.                                                                                               | `QUERY('title:+the -reading')`          |
| `<column>:"<phrase>"`                                   | 지정한 열에 지정한 구문이 정확히 포함된 문서와 일치합니다.                                                                                                                                                                       | `QUERY('title:"Benefits of Exercise"')` |
| `<column>:<keyword>^<boost> <column>:<keyword>^<boost>` | 지정한 열에 지정한 키워드가 있는 문서와 일치하며, 지정한 부스트로 검색 관련도를 높입니다. 이 구문으로 여러 열에 서로 다른 가중치를 설정해 검색 관련도에 영향을 줄 수 있습니다. | `QUERY('title:art^5 body:reading^1.2')` |


| 옵션    | 설명                                                                                                                                                                                         | 예시                                                                                              | 설명                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fuzziness | 지정한 레벤슈타인 거리 이내의 용어와 일치하도록 허용합니다. `fuzziness`는 1 또는 2로 설정할 수 있습니다.                                                                                                    | SELECT id, score(), content FROM t WHERE query('content:box', 'fuzziness=1');                        | 검색어 "box"와 일치시킬 때 `fuzziness=1`이면 "fox" 같은 용어도 일치합니다. "box"와 "fox"의 레벤슈타인 거리가 1이기 때문입니다.                                                                          |
| operator  | 여러 검색어를 결합하는 방식을 지정합니다. OR(기본값) 또는 AND로 설정할 수 있습니다. OR은 검색어 중 하나라도 포함된 결과를 반환하고, AND는 모든 검색어가 포함된 결과를 반환합니다.     | SELECT id, score(), content FROM t WHERE query('content:action works', 'fuzziness=1;operator=AND');  | `operator=AND`이면 결과에 "action"과 "works"가 모두 있어야 합니다. `fuzziness=1` 덕분에 "Actions", "words" 같은 용어와도 일치하므로 "Actions speak louder than words"가 반환됩니다. |
| lenient   | 검색 텍스트가 올바르지 않을 때 오류를 보고할지 여부를 제어합니다. 기본값은 `false`입니다. `true`로 설정하면 오류를 보고하지 않으며, 검색 텍스트가 올바르지 않을 경우 빈 결과 집합을 반환합니다. | SELECT id, score(), content FROM t WHERE query('content:()', 'lenient=true');                        | 검색 텍스트 `()`가 올바르지 않더라도 `lenient=true`로 설정하면 오류가 발생하지 않고 대신 빈 결과 집합을 반환합니다.                                                                               |

## SQL Examples

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
