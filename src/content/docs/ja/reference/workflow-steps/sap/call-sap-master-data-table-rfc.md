---
title: Call SAP Master Data Table RFCステップ
description: マスターデータテーブルにアクセスするSAP ECC / S/4HANAのRemote Function Call（RFC）を呼び出し、データを表形式で取得します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## 説明


マスターデータテーブルにアクセスするよう設計されたSAP ECC / S/4HANAのRemote Function Call（RFC）を呼び出し、データを表形式で取得します。取得したデータは、PlaidCloudの変換処理で利用できます。また、列名、データ型、列の順序の情報を含むマスターデータテーブルの構造を、別のファイルにエクスポートすることもできます。


## 例


### RFCパラメーター


**使用するエージェント**を選択します。ドロップダウンバーから**ターゲットディレクトリ**を選択し、その下でファイルの保存先となる子フォルダーを参照して選択します。次に、「Target File Name」に適切な名前を付けます。「Function Call Information」で、Function、**戻り値パラメーター**を入力し、パラメーターを選択します。



「Parameters」セクションで**行を挿入**または**行を追加**を選択できるほか、パラメーターに名前を付けて値を設定できます。**最大同時リクエスト数**を選択し、「Wait for RFC to Complete」を選択します。ステップを保存して実行します。
