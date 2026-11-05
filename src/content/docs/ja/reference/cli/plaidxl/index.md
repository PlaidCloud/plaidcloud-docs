---
title: PlaidXL
description: PlaidXL Excelアドインを使って、PlaidCloudワークスペースにサインインし、プロジェクトのテーブルとディメンション階層をワークシートに取り込み、ライブのレポートを作成し、ドリルして数値を説明し、管理されたメトリックを読み取り、値をPlaidCloudに入力して計画を立て、Weaveに質問します。
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXLは、Microsoft Excel用のPlaidCloudアドインです。ブックをPlaidCloudワークスペースに接続するため、モデルやレポートは、ワークフローが次に実行された途端に古くなるコピーではなく、信頼できるプロジェクトのテーブルとディメンションから読み取ります。

PlaidXLは3つの方法で使用でき、ほとんどのブックではそのすべてを使用します。

- **タスクペイン** — プロジェクトを参照し、テーブルまたはディメンションを選択し、列とフィルターを選択して、データをワークシートに取得します。更新によりデータは最新に保たれ、**Save to PlaidCloud** は編集したテーブルを書き戻します。他のタブでは、数式やレポート全体の作成、数値の出どころの説明を行い、普通の言葉でWeaveに質問できます。
- **カスタム関数** — `=PLAIDXL.TABLE.GET_TABLE("Sales")`、`=PLAIDXL.CELL(...)`、`=PLAIDXL.METRIC("Net Revenue")` などの数式で、PlaidCloudのデータを直接セルに読み込みます。テーブルとディメンションの一覧表示、階層のレイアウト、レポート用の集計値の計算、管理されたメトリックの読み取りに使用します。
- **リボンと右クリックメニュー** — 任意のセルからのディメンションのドリル、メンバーの選択、更新、数値の説明、その裏付けとなる行の表示を行います。それぞれにキーボードショートカットがあります。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="ExcelにはPlaidXLタスクペインとPlaidXLカスタム関数があります。どちらも、あなたとしてサインインした状態で、PlaidCloudワークスペース内のプロジェクトにリクエストを送信します。プロジェクトは、テーブルの行、ディメンション階層、集計値をワークシートのセルに返します。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excelブック</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXLタスクペイン</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">参照、フィルター、取得、更新</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PLAIDXL.* 関数</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">セル内のテーブル、階層、値</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">PlaidCloudワークスペース</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">プロジェクト</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">テーブル</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">ディメンションと階層</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">あなたとしてサインイン</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">行、ノード、値</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">タスクペインとカスタム関数は、どちらも、選択したプロジェクトから、あなた自身のPlaidCloud権限で読み取ります。</figcaption>
</figure>

PlaidXLはPlaidCloudから読み取り、プロジェクトのテーブルを変更するのは、あなた自身が書き込んだときだけです。`CELL` の値の上に数値を入力するか、取得したシートを **Save to PlaidCloud** で保存します。どちらもすぐに書き込まれ、**Undo last write** で元に戻せます。[PlaidCloudに値を入力する](/ja/reference/cli/plaidxl/write-values/)を参照してください。

## 要件

- WindowsまたはMac上の、Microsoft 365版のExcel、またはExcel 2021以降。PlaidCloudリボンタブ、右クリックメニュー、タスクペインは、デスクトップ版のExcelで動作します。
- 少なくとも1つのワークスペースにあるPlaidCloudアカウントと、読み取りたいプロジェクトへのアクセス権。PlaidXLに表示されるのは、アカウントがPlaidCloudですでに見ることができるプロジェクト、テーブル、ディメンションだけです。

## トピック

- [インストール](/ja/reference/cli/plaidxl/install/) — PlaidXLをExcelに追加し、タスクペインを開きます
- [サインイン](/ja/reference/cli/plaidxl/connect/) — ワークスペースに接続し、サインアウトして、ワークスペースを切り替えます
- [テーブルとディメンションを操作する](/ja/reference/cli/plaidxl/retrieve/) — プロジェクトを選択し、テーブルをフィルターし、シートに取得して、更新し、書き戻します
- [カスタム関数](/ja/reference/cli/plaidxl/functions/) — すべての `PLAIDXL` 関数、その引数、返される内容
- [レポートを作成する](/ja/reference/cli/plaidxl/build-a-report/) — タスクペインまたは数式で、ライブのレポートをレイアウトします
- [ドリル、メンバーの選択、数値の説明](/ja/reference/cli/plaidxl/drill/) — セルからドリルし、メンバーを選択し、数値とその明細行を説明します
- [PlaidCloudに値を入力する](/ja/reference/cli/plaidxl/write-values/) — レポートの値を上書き入力して計画を立て、書き込みを元に戻します
- [ExcelでWeaveに質問](/ja/reference/cli/plaidxl/weave/) — 普通の言葉の依頼から、作成、ドリル、修正を行います
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — すべてのコマンド、右クリックメニュー、キーボードショートカット
- [トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/) — よくある問題の解決方法

PlaidXLは初めてですか？[PlaidXLでExcelを使う](/ja/get-started/tutorials/excel-with-plaidxl/)チュートリアルでは、アドインのインストールから最初のレポートまでを、約20分で説明します。

## 関連情報

- [プロジェクト](/ja/guides/projects/) — プロジェクトに含まれるものと、見つけ方
- [テーブルとビュー](/ja/guides/data/tables-views/) — PlaidXLが取得するテーブル
- [ディメンションを使用する](/ja/guides/dimensions/dimensions/) — PlaidXLがレイアウトして集計する階層
