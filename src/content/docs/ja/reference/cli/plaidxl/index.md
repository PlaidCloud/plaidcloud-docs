---
title: PlaidXL
description: PlaidXL Excelアドインを使用して、PlaidCloudワークスペースにサインインし、プロジェクトのテーブルとディメンション階層をワークシートに取り込み、必要に応じて更新し、PlaidXLカスタム関数でライブレポートを作成します。
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXLは、Microsoft Excel用のPlaidCloudアドインです。ブックをPlaidCloudワークスペースに接続し、次にワークフローが実行されたときに古くなってしまうコピーではなく、信頼できるプロジェクトのテーブルとディメンションから、モデルやレポートがデータを読み取れるようにします。

PlaidXLの使い方は2通りあり、ほとんどのブックでは両方を使用します。

- **作業ウィンドウ** — プロジェクトを参照し、テーブルまたはディメンションを選択し、列とフィルターを指定して、データをワークシートに取得します。**Refresh All Tables**は、取得したすべてのテーブルの最新データを取得し、**Save to PlaidCloud…** ボタンは編集したテーブルを書き戻します。**Formulas**タブでは、PlaidXLの数式を作成できます。
- **カスタム関数** — `=PLAIDXL.TABLE.GET_TABLE("Sales")`や`=PLAIDXL.CELL(...)`などの数式で、PlaidCloudのデータをセルに直接読み込みます。テーブルやディメンションの一覧表示、階層のレイアウト、レポート用の集計値の計算に使用します。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="ExcelにはPlaidXL作業ウィンドウとPlaidXLカスタム関数があります。どちらも、ユーザー本人としてサインインした状態で、PlaidCloudワークスペース内のプロジェクトにリクエストを送信します。プロジェクトは、テーブルの行、ディメンション階層、集計値をワークシートのセルに返します。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excelブック</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXL作業ウィンドウ</text>
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
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">作業ウィンドウとカスタム関数は、どちらも選択したプロジェクトから、ユーザー自身のPlaidCloud権限で読み取ります。</figcaption>
</figure>

PlaidXLはPlaidCloudから読み取り、プロジェクトのテーブルを変更するのは、ユーザー自身が書き戻したときだけです。取得したシートを編集し、**Save to PlaidCloud…** ボタンをクリックして確定します。それまでは何も書き込まれず、復元ポイントは7日間保持されます。

## 要件

- WindowsまたはMac上の、Microsoft 365版Excel、またはExcel 2021以降。PlaidCloudリボンタブと作業ウィンドウは、デスクトップ版Excelで動作します。
- 少なくとも1つのワークスペースにあるPlaidCloudアカウントと、読み取りたいプロジェクトへのアクセス権。PlaidXLには、PlaidCloudですでに表示できるプロジェクト、テーブル、ディメンションだけが表示されます。

## トピック

- [インストール](/ja/reference/cli/plaidxl/install/) — PlaidXLをExcelに追加して作業ウィンドウを開く
- [サインイン](/ja/reference/cli/plaidxl/connect/) — ワークスペースへの接続、サインアウト、ワークスペースの切り替え
- [テーブルとディメンションを扱う](/ja/reference/cli/plaidxl/retrieve/) — プロジェクトの選択、テーブルのフィルター、シートへの取得、更新、書き戻し
- [カスタム関数](/ja/reference/cli/plaidxl/functions/) — すべての`PLAIDXL`関数、その引数、返される値
- [カスタム関数でレポートを作成する](/ja/reference/cli/plaidxl/build-a-report/) — 階層をレイアウトし、集計値で埋める
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — 更新、階層の展開、値への変換
- [トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/) — よくある問題の対処方法

PlaidXLを初めて使う場合は、[PlaidXLでExcelを使って作業する](/ja/get-started/tutorials/excel-with-plaidxl/)チュートリアルで、アドインのインストールから最初のレポートの作成まで、約20分で学べます。

## 関連項目

- [プロジェクト](/ja/guides/projects/) — プロジェクトに含まれるものと、その見つけ方
- [テーブルとビュー](/ja/guides/data/tables-views/) — PlaidXLが取得するテーブル
- [ディメンションの使用](/ja/guides/dimensions/dimensions/) — PlaidXLがレイアウトして集計する階層
