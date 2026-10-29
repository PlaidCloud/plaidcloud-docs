---
title: UNNEST (Lakehouse v1)
description: UNNEST — 配列を展開し、要素の集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

配列を展開し、要素の集合を返します。

## Analyzeの構文

```python
func.unnest( <array> )
```

## Analyzeの例

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## SQLの構文

```sql
UNNEST( <array> )
```

## SQLの例

```sql
SELECT UNNEST([1, 2]);

┌─────────────────┐
│  unnest([1, 2]) │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘

-- UNNEST(array) can be used as a table function.
SELECT * FROM UNNEST([1, 2]);

┌─────────────────┐
│      value      │
├─────────────────┤
│               1 │
│               2 │
└─────────────────┘
```

## 実践的な例
以下の例では、テキストの配列として定義したphones列を持つ、contactsというテーブルを使用します。

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

phones列は1次元の配列で、連絡先が持つ複数の電話番号を保持します。

多次元配列を定義するには、角括弧を追加します。

たとえば、2次元配列は次のように定義できます。

```python
column_name data_type [][]
```

そのテーブルにデータを挿入する例です。
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
または
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

unnest()関数は、配列を行のリストに展開します。たとえば、次のクエリは、phones配列のすべての電話番号を展開します。

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

出力：
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
