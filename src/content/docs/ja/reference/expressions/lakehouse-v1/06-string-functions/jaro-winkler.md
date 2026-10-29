---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER — 2つの文字列間の Jaro-Winkler 距離を計算します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

2つの文字列間の [Jaro-Winkler 距離](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)を計算します。文字列間の類似度の測定によく使われ、値は 0.0（まったく異なる）から 1.0（同一の文字列）の範囲になります。 

## Analyze の構文

```python
func.jaro_winkler(<string1>, <string2>)
```

## Analyze の例

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## SQL構文

```sql
JARO_WINKLER(<string1>, <string2>)
```

## SQLの例

JARO_WINKLER 関数は、2つの入力文字列の類似度を表す FLOAT64 値を返します。戻り値は次のルールに従います。

- 類似度の範囲: 結果は 0.0（まったく異なる）から 1.0（同一）の範囲になります。

    ```sql
    SELECT JARO_WINKLER('databend', 'Databend') AS similarity;

    ┌────────────────────┐
    │     similarity     │
    ├────────────────────┤
    │ 0.9166666666666666 │
    └────────────────────┘

    SELECT JARO_WINKLER('databend', 'database') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │        0.9 │
    └────────────┘
    ```
- NULL の扱い: string1 または string2 のいずれかが NULL の場合、結果は NULL になります。

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- 空文字列:
    - 2つの空文字列を比較すると 1.0 を返します。

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - 空文字列と空でない文字列を比較すると 0.0 を返します。

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
