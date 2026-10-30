---
title: UNNEST (Lakehouse v1)
description: UNNEST：展开数组并返回元素集合。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

展开数组并返回元素集合。

## Analyze 语法

```python
func.unnest( <array> )
```

## Analyze 示例

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## SQL 语法

```sql
UNNEST( <array> )
```

## SQL 示例

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

## 实用示例
在下面的示例中，将使用名为 contacts 的表，其 phones 列定义为文本数组。

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

phones 列是一个一维数组，保存联系人可能拥有的各种电话号码。

要定义多维数组，请添加方括号。

例如，可以按如下方式定义二维数组：

```python
column_name data_type [][]
```

向该表插入数据的示例
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
或
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

unnest() 函数会将数组展开为多行。例如，下面的查询会展开 phones 数组中的所有电话号码。

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

输出：
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
