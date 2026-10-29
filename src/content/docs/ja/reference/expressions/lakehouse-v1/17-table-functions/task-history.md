---
title: TASK_HISTORY（Lakehouse v1）
description: TASK_HISTORY — 指定した変数に基づいて、タスクの実行履歴を表示します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

指定した変数に基づいて、タスクの実行履歴を表示します。

## SQLの構文
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## 引数

すべての引数は省略可能です。

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

タスクの実行がスケジュールされていた時間範囲です（TIMESTAMP_LTZ形式）。過去7日以内を指定します。時間範囲が過去7日以内に収まらない場合は、エラーが返されます。

* `SCHEDULED_TIME_RANGE_END` を指定しない場合、この関数は、すでに完了したタスク、現在実行中のタスク、および将来実行がスケジュールされているタスクを返します。
* `SCHEDULED_TIME_RANGE_END` がCURRENT_TIMESTAMPの場合、この関数は、すでに完了したタスクと現在実行中のタスクを返します。現在時刻の直前に実行されたタスクが、スケジュール済みとして識別される場合があることに注意してください。
* すでに完了したタスクと現在実行中のタスクのみを照会するには、フィルターとして `WHERE query_id IS NOT NULL` を含めます。TASK_HISTORYの出力のQUERY_ID列には、タスクの実行が開始された場合にのみ値が入ります。

開始時刻も終了時刻も指定しない場合は、指定したRESULT_LIMITの値を上限として、直近のタスクが返されます。

`RESULT_LIMIT => <integer>`

関数が返す行数の上限を指定する数値です。

一致する行数がこの上限を超える場合は、タイムスタンプが最も新しいタスクの実行が、指定した上限まで返されます。

範囲: `1` ～ `10000`

デフォルト: `100`。

`TASK_NAME => <string>`

タスクを指定する、大文字と小文字を区別しない文字列です。修飾されていないタスク名のみがサポートされます。指定したタスクの実行のみが返されます。同じ名前のタスクが複数ある場合、この関数はそれらすべてのタスクの履歴を返すことに注意してください。

`ERROR_ONLY => { TRUE | FALSE }`

TRUEに設定すると、この関数は失敗またはキャンセルされたタスクの実行のみを返します。

`ROOT_TASK_ID => <string>`

タスクグラフ内のルートタスクの一意の識別子です。このIDは、同じタスクに対するSHOW TASKSの出力のID列の値と一致します。ROOT_TASK_IDを指定すると、ルートタスクと、そのタスクグラフに含まれるすべての子タスクの履歴が表示されます。

## 使用上の注意
* この関数が返す行数は最大10,000行で、RESULT_LIMIT引数の値で設定します。デフォルト値は100です。
* この関数は、ACCOUNTADMINロールに対してのみ結果を返します。


## SQLの例

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
上のSQLクエリは、TASK_HISTORY関数からすべてのタスク履歴レコードを取得し、scheduled_time列で並べ替えます（最大10,000件）。



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

上のSQLクエリは、TASK_HISTORY関数から、スケジュールされた時間範囲が '2022-01-02T01:12:00-07:00' に始まり '2022-01-02T01:12:30-07:00' に終わるすべてのタスク履歴レコードを取得します。つまり、この30秒間に実行がスケジュールされていたタスクが返されます。結果には、この条件に一致するタスクの詳細が含まれます。
