---
title: Report Singleステップ
description: テンプレート、データソース、設定可能なレイアウトオプションを使用して、PlaidCloud のワークフローステップから単一の PDF レポートを生成します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## 説明



RML（Report Markup Language）テンプレートに、1 つ以上の PlaidCloud テーブルのデータを差し込んで PDF レポートを生成します。請求書、財務諸表、規制当局への提出書類、ブランド仕様のサマリーなど、書式の整った正式なレポートに使用します。

RML テンプレートがレイアウト（ページサイズ、フォント、固定テキスト、テーブルの配置）を定義し、入力テーブルが可変データを提供します。1 つのテンプレートから多数のレポート（顧客ごとに 1 つなど）を生成する場合は、[Reports Batchステップ](/ja/reference/workflow-steps/reports/reports-batch/)と比較してください。


## テンプレートが読み取る名前

テンプレートは、**レポートデータ**タブの各ソースと、**レポート定数（固定値）** の各定数を、それぞれの名前で読み取ります。新しいソースには `new_source`、`new_source_2` のような名前が付き、テンプレートはそのまま読み取れます。内容がわかる名前に変更してください。


## 保存時にチェックされる内容

すべてのソース名と定数名は、次の条件を満たす必要があります。

- **指定されている** — 空白の名前は拒否されます。
- **重複していない** — 2 つのソース、2 つの定数、またはソースと定数が同じ名前を共有することはできません。テンプレートからはそのうちの 1 つしか見えないためです。*Source name 'sales' is also a constant name; rename one of them.*
- **テンプレートが読み取れる** — 英字、数字、アンダースコアのみで、英字またはアンダースコアで始まる必要があります。*Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **テンプレートの予約語ではない** — `True`、`False`、`None`、`true`、`false`、`none`、`not`、`self` は、データとは別の意味に解釈されます。*Source name 'self' is a word the template reserves, so it can't be read as a name.*


## 例

例はまだありません...
