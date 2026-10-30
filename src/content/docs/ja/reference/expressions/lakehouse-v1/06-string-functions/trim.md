---
title: TRIM (Lakehouse v1)
description: TRIM — 指定した削除文字列を先頭と末尾から取り除いた文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

指定した削除文字列を先頭と末尾から取り除いた文字列を返します。削除文字列を省略した場合は、スペースが取り除かれます。

Analyzeの関数は、先頭と末尾の両方のスペースを自動的にトリムします。

## Analyzeの構文

```python
func.trim(str)
```

## Analyzeの例

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## SQLの構文

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## SQLの例

ご注意: このセクションのすべての例は、文字列 'databend' を返します。

次の例は、文字列 'xxxdatabendxxx' から先頭と末尾の文字列 'xxx' を削除します。

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

次の例は、文字列 'xxxdatabend' から先頭の文字列 'xxx' を削除します。

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
次の例は、文字列 'databendxxx' から末尾の文字列 'xxx' を削除します。

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

削除文字列を指定しない場合、関数は先頭と末尾のスペースをすべて削除します。次の例は、先頭と末尾のどちらか、または両方のスペースを削除します。

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
