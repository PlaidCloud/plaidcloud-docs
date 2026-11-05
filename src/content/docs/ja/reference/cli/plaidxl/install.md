---
title: PlaidXLのインストール
description: WindowsまたはMacのExcelにPlaidXLアドインを追加し、PlaidCloudリボンタブを見つけて、PlaidXLタスクペインを開きます。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

PlaidXLのインストールは、ブックごとではなくコンピューターごとに1回だけ行います。その後は、開くすべてのブックのExcelリボンに **PlaidCloud** タブが表示されます。

## 始める前に

- WindowsまたはMac上の、Microsoft 365版のExcel、またはExcel 2021以降を使用してください。
- 組織でOfficeアドインを一元管理している場合は、Microsoft 365の管理者によるPlaidXLの配布が必要なことがあります。自分でアドインをインストールできない場合は、管理者に **PlaidCloud** アドインの追加を依頼してください。

## Windowsにインストールする

1. Excelで **挿入 → アドイン** を開きます（バージョンによっては **ホーム → アドイン**）。
2. アドインの検索ボックスに `PlaidCloud` と入力します。
3. **PlaidCloud** アドインを選択し、**追加** をクリックします。

## Macにインストールする

1. Mac版のExcelで **挿入 → アドイン** を開きます。古いバージョンでは、メニューは **挿入 → ストア** です。
2. アドインの検索ボックスに `PlaidCloud` と入力します。
3. **PlaidCloud** アドインを選択し、**追加** をクリックします。

## タスクペインを開く

1. リボンの **PlaidCloud** タブをクリックします。
2. **接続** グループで、**Open PlaidXL** をクリックします。

PlaidXLタスクペインがウィンドウの右側に開き、サインインを求められます。続いて[サインイン](/ja/reference/cli/plaidxl/connect/)に進みます。

タスクペインはセッションをまたいでサインインしたままなので、通常はサインインは1回だけで、必要なときにタスクペインを開くだけで済みます。

## PlaidXLが表示されない場合

- すべてのExcelウィンドウを閉じて、Excelを開き直します。アドインは、Excelを再起動するまでリボンに表示されないことがよくあります。
- **挿入 → マイ アドイン**（Windows）または **挿入 → アドイン → マイ アドイン**（Mac）を確認し、そこから **PlaidCloud** を選択します。
- 組織がストアからのアドインをブロックしている場合は、Microsoft 365の管理者に配布を依頼してください。

その他の解決方法は、[トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/)のページを参照してください。

## 関連情報

- [サインイン](/ja/reference/cli/plaidxl/connect/) — アドインをワークスペースに接続します
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — **PlaidCloud** タブのすべてのコマンド
