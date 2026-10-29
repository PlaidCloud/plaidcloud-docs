---
title: PlaidXL
description: PlaidXLのExcelアドインを使って、PlaidCloudのワークスペースにサインインし、プロジェクトのテーブルやディメンション階層をワークシートに取り込み、必要に応じて更新し、PlaidXLカスタム関数でライブのレポートを作成します。
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXLは、Microsoft Excel用のPlaidCloudアドインです。ブックをPlaidCloudのワークスペースに接続し、ワークフローが次に実行されたときに古くなってしまうコピーではなく、信頼できるプロジェクトのテーブルとディメンションからモデルやレポートがデータを読み取るようにします。

PlaidXLの使い方は2つあり、ほとんどのブックでは両方を使用します。

- **タスクペイン** — プロジェクトを参照し、テーブルまたはディメンションを選択し、列とフィルターを選んで、データをワークシートに取得します。**Refresh All Tables**は、取得したすべてのテーブルの最新データを取り込みます。
- **カスタム関数** — `=PLAIDXL.TABLE.GET_TABLE("Sales")`や`=PLAIDXL.CELL(...)`のような数式で、PlaidCloudのデータをセルに直接読み込みます。テーブルやディメンションの一覧表示、階層のレイアウト、レポート用の集計値の計算に使用します。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="ExcelにはPlaidXLタスクペインとPlaidXLカスタム関数があります。どちらも、ユーザー本人としてサインインした状態で、PlaidCloudワークスペース内のプロジェクトにリクエストを送信します。プロジェクトは、テーブルの行、ディメンション階層、集計値をワークシートのセルに返します。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excelブック</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXLタスクペイン</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">参照、フィルター、取得、更新</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PLAIDXL.*関数</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">セル内のテーブル、階層、値</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">PlaidCloudワークスペース</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">プロジェクト</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">テーブル</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">ディメンションと階層</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">本人としてサインイン</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">行、ノード、値</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">タスクペインとカスタム関数はどちらも、ユーザー自身のPlaidCloud権限で、選択したプロジェクトから読み取ります。</figcaption>
</figure>

PlaidXLはデータを読み取るだけです。PlaidCloudには何も書き戻さないため、取得したシートを編集しても、プロジェクトのテーブルが変更されることはありません。

## 要件

- WindowsまたはMac用の、Microsoft 365版Excel、またはExcel 2021以降。PlaidCloudリボンタブとタスクペインは、デスクトップ版Excelで動作します。
- 少なくとも1つのワークスペースに属するPlaidCloudアカウントと、読み取りたいプロジェクトへのアクセス権。PlaidXLには、アカウントがPlaidCloudですでに表示できるプロジェクト、テーブル、ディメンションのみが表示されます。

## トピック

- [インストール](/ja/reference/cli/plaidxl/install/) — PlaidXLをExcelに追加してタスクペインを開く
- [サインイン](/ja/reference/cli/plaidxl/connect/) — ワークスペースに接続し、サインアウトして、ワークスペースを切り替える
- [テーブルとディメンションを操作する](/ja/reference/cli/plaidxl/retrieve/) — プロジェクトを選択し、テーブルをフィルターし、シートに取得して更新する
- [カスタム関数](/ja/reference/cli/plaidxl/functions/) — すべての`PLAIDXL`関数、その引数、返される値
- [カスタム関数でレポートを作成する](/ja/reference/cli/plaidxl/build-a-report/) — 階層をレイアウトし、集計値で埋める
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — 更新、ドリル、サニタイズのコマンド
- [トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/) — よくある問題の解決方法

PlaidXLは初めてですか。[PlaidXLでExcelを操作する](/ja/get-started/tutorials/excel-with-plaidxl/)チュートリアルでは、アドインのインストールから最初のレポートの作成まで、約20分で説明します。

## 関連項目

- [プロジェクト](/ja/guides/projects/) — プロジェクトに含まれるものと、探し方
- [テーブルとビュー](/ja/guides/data/tables-views/) — PlaidXLが取得するテーブル
- [ディメンションの使用](/ja/guides/dimensions/dimensions/) — PlaidXLがレイアウトして集計する階層
