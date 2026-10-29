---
title: UNNEST (Lakehouse v1)
description: UNNEST — 배열을 펼쳐 요소 집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/unnest.md
---

배열을 펼쳐 요소 집합을 반환합니다.

## Analyze 구문

```python
func.unnest( <array> )
```

## Analyze 예제

```python
func.unnest([1, 2])

┌──────────────────────┐
│  func.unnest([1, 2]) │
├──────────────────────┤
│                    1 │
│                    2 │
└──────────────────────┘
```

## SQL 구문

```sql
UNNEST( <array> )
```

## SQL 예제

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

## 실용적인 예제
아래 예제에서는 텍스트 배열로 정의된 phones 열이 있는 contacts 테이블을 사용합니다.

```python
CREATE TABLE contacts (
  id SERIAL PRIMARY KEY, 
  name VARCHAR (100), 
  phones TEXT []
);
```

phones 열은 연락처가 가질 수 있는 여러 전화번호를 담는 1차원 배열입니다.

다차원 배열을 정의하려면 대괄호를 추가합니다.

예를 들어 2차원 배열은 다음과 같이 정의할 수 있습니다.

```python
column_name data_type [][]
```

해당 테이블에 데이터를 삽입하는 예제입니다.
```python
INSERT INTO contacts (name, phones)
VALUES('John Doe',ARRAY [ '(408)-589-5846','(408)-589-5555' ]);
```
또는
```python
INSERT INTO contacts (name, phones)
VALUES('Lily Bush','{"(408)-589-5841"}'),
      ('William Gate','{"(408)-589-5842","(408)-589-5843"}');
```

unnest() 함수는 배열을 행 목록으로 펼칩니다. 예를 들어 다음 쿼리는 phones 배열의 모든 전화번호를 펼칩니다.

```python
SELECT 
  name, 
  unnest(phones) 
FROM 
  contacts;
```

출력:
|     name     |     unnest     |
|--------------|----------------|
| John Doe     | (408)-589-5846 |
| John Doe     | (408)-589-5555 |
| Lily Bush    | (408)-589-5841 |
| William Gate | (408)-589-5843 |
