---
title: PlaidXLのインストール
description: WindowsまたはMacのExcelにPlaidXLアドインを追加し、PlaidCloudリボンタブを見つけて、PlaidXL作業ウィンドウを開きます。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

PlaidXLのインストールは、ブックごとではなく、コンピューターごとに1回だけ行います。その後は、開くすべてのブックで、Excelのリボンに**PlaidCloud**タブが表示されます。

## 始める前に

- WindowsまたはMac上の、Microsoft 365版Excel、またはExcel 2021以降を使用してください。
- 組織でOfficeアドインを一元管理している場合は、Microsoft 365管理者によるPlaidXLの配布が必要なことがあります。自分でアドインをインストールできない場合は、管理者に**PlaidCloud**アドインの追加を依頼してください。

## Windowsにインストールする

1. Excelで**Insert → Add-ins**を開きます（バージョンによっては**Home → Add-ins**）。
2. アドインの検索ボックスに`PlaidCloud`と入力します。
3. **PlaidCloud**アドインを選択し、**追加**をクリックします。

## Macにインストールする

1. Excel for Macで**Insert → Add-ins**を開きます。古いバージョンでは、メニューは**Insert → Store**です。
2. アドインの検索ボックスに`PlaidCloud`と入力します。
3. **PlaidCloud**アドインを選択し、**追加**をクリックします。

## 作業ウィンドウを開く

1. リボンの**PlaidCloud**タブをクリックします。
2. **データ**グループで、**Open PlaidXL**をクリックします。

PlaidXL作業ウィンドウがウィンドウの右側に開き、サインインを求められます。[サインイン](/ja/reference/cli/plaidxl/connect/)に進んでください。

作業ウィンドウはセッションをまたいでサインイン状態を維持するため、通常はサインインを1回行えば、あとは必要なときに作業ウィンドウを開くだけで済みます。

## PlaidXLが表示されない場合

- すべてのExcelウィンドウを閉じて、Excelを開き直します。アドインは、Excelを再起動するまでリボンに表示されないことがよくあります。
- **Insert → My Add-ins**（Windows）または**Insert → Add-ins → My Add-ins**（Mac）を確認し、そこから**PlaidCloud**を選択します。
- 組織がストアからのアドインをブロックしている場合は、Microsoft 365管理者にアドインの配布を依頼してください。

そのほかの対処方法は、[トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/)ページを参照してください。

## 関連項目

- [サインイン](/ja/reference/cli/plaidxl/connect/) — アドインをワークスペースに接続する
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — **PlaidCloud**タブのすべてのコマンド
