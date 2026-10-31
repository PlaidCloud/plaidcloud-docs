---
title: PlaidXLのインストール
description: WindowsまたはMacのExcelにPlaidXLアドインを追加し、PlaidCloudリボンタブを見つけて、PlaidXLタスクペインを開きます。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

PlaidXLのインストールは、ブックごとではなく、コンピューターごとに1回行います。その後は、開くすべてのブックのExcelリボンに**PlaidCloud**タブが表示されます。

## 開始する前に

- WindowsまたはMac用の、Microsoft 365版Excel、またはExcel 2021以降を使用します。
- 組織でOfficeアドインを一元管理している場合は、Microsoft 365の管理者がPlaidXLを展開する必要があることがあります。自分でアドインをインストールできない場合は、管理者に**PlaidCloud**アドインの追加を依頼してください。

## Windowsでのインストール

1. Excelで、**Insert → Add-ins**を開きます（バージョンによっては**Home → Add-ins**）。
2. アドインの検索ボックスに`PlaidCloud`と入力します。
3. **PlaidCloud**アドインを選択して、**追加**をクリックします。

## Macでのインストール

1. Mac版Excelで、**Insert → Add-ins**を開きます。古いバージョンでは、メニューは**Insert → Store**です。
2. アドインの検索ボックスに`PlaidCloud`と入力します。
3. **PlaidCloud**アドインを選択して、**追加**をクリックします。

## タスクペインを開く

1. リボンの**PlaidCloud**タブをクリックします。
2. **PlaidXL Controls**グループで、**Show Taskpane**をクリックします。

PlaidXLタスクペインがウィンドウの右側に開き、サインインを求められます。[サインイン](/ja/reference/cli/plaidxl/connect/)に進みます。

タスクペインはセッション間でサインインした状態を維持するため、通常はサインインを1回行えば、必要なときにタスクペインを開くだけで済みます。

## PlaidXLが表示されない場合

- すべてのExcelウィンドウを閉じて、Excelを再起動します。アドインは、Excelを再起動するまでリボンに表示されないことがよくあります。
- Windowsでは**Insert → My Add-ins**、Macでは**Insert → Add-ins → My Add-ins**を確認し、そこから**PlaidCloud**を選択します。
- 組織がストアからのアドインをブロックしている場合は、Microsoft 365の管理者に展開を依頼してください。

その他の解決方法は、[トラブルシューティング](/ja/reference/cli/plaidxl/troubleshooting/)ページにあります。

## 関連項目

- [サインイン](/ja/reference/cli/plaidxl/connect/) — アドインをワークスペースに接続する
- [PlaidCloudリボン](/ja/reference/cli/plaidxl/ribbon/) — **PlaidCloud**タブのすべてのコマンド
