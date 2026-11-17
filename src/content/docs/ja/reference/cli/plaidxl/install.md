---
title: PlaidXLのインストール
description: WindowsまたはMacのExcelにPlaidXLアドインを追加し、PlaidCloudリボンタブを見つけて、PlaidXLのタスクペインを開きます。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

PlaidXLのインストールは、ブックごとではなく、コンピューターごとに1回だけ行います。インストール後は、開くすべてのブックでExcelのリボンに **PlaidCloud** タブが表示されます。

## 始める前に

- WindowsまたはMac上で、Microsoft 365版のExcel、またはExcel 2021以降を使用してください。
- PlaidCloudワークスペースが最新のリリースである必要があります。古いワークスペースでは、プル時に **This PlaidCloud workspace needs an update for PlaidXL** と表示されます。その場合は、管理者にワークスペースの更新を依頼してください。
- 組織でOfficeアドインを一元管理している場合は、Microsoft 365の管理者がPlaidXLを配布する必要があることがあります。自分でアドインをインストールできない場合は、管理者に **PlaidCloud** アドインの追加を依頼してください。

## Windowsにインストールする

1. Excelで **挿入 → アドイン** を開きます（バージョンによっては **ホーム → アドイン**）。
2. アドインの検索ボックスに `PlaidCloud` と入力します。
3. **PlaidCloud** アドインを選択し、**追加** をクリックします。

## Macにインストールする

1. Excel for Macで **挿入 → アドイン** を開きます。古いバージョンでは、メニューは **挿入 → ストア** です。
2. アドインの検索ボックスに `PlaidCloud` と入力します。
3. **PlaidCloud** アドインを選択し、**追加** をクリックします。

## タスクペインを開く

1. リボンの **PlaidCloud** タブをクリックします。
2. **接続** グループで **Open PlaidXL** をクリックします。

PlaidXLのタスクペインがウィンドウの右側に開き、サインインを求められます。[サインイン](/ja/reference/cli/plaidxl/connect/)に進んでください。

タスクペインはセッションをまたいでサインインしたままになるため、通常はサインインを1回行えば、あとは必要なときにタスクペインを開くだけです。

## PlaidXLが表示されない場合

- すべてのExcelウィンドウを閉じて、Excelを開き直します。アドインは、Excelを再起動するまでリボンに表示されないことがよくあります。
- **挿入 → 個人用アドイン**（Windows）または **挿入 → アドイン → 個人用アドイン**（Mac）を確認し、そこから **PlaidCloud** を選択します。
- 組織がストアからのアドインをブロックしている場合は、Microsoft 365の管理者にアドインの配布を依頼してください。

その他の対処方法は、[トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/)ページにあります。

## 関連情報

- [サインイン](/ja/reference/cli/plaidxl/connect/) — アドインをワークスペースに接続します
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — **PlaidCloud** タブのすべてのコマンド
