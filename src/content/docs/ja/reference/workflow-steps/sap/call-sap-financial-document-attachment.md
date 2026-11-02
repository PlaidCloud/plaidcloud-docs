---
title: Call SAP Financial Document Attachment ステップ
description: PlaidCloudのワークフローステップからSAPの財務伝票の添付ファイルを取得し、ドキュメントの抽出と処理を自動化します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## 説明



RFC（Remote Function Call）を介して、SAP ECC / S/4HANAの特定のFI（財務会計）伝票にファイルを添付します。スキャンした請求書、承認ワークフロー、契約書のコピーなどの裏付け資料を、それらが裏付ける財務仕訳とあわせて転記する場合に便利です。

SAPコネクターに設定されたSAP RFCの認証情報と、対象のFI伝票番号（会社コード、伝票番号、会計年度）が必要です。


## 保存時にチェックされる内容

ステップは、**列**タブの出力列の中にある`relative_file_path`列から各ファイルのパスを読み取り、その列はテキストである必要があります。この列がない場合は保存が拒否されます（*The output columns must include relative_file_path, the path of each file to attach.*）。別の型の場合も同様です（*The relative_file_path column must be text, not integer.*）。

ソーステーブルを選択した状態で、ソース列またはターゲット列がない状態で保存すると、**両方のマッピングテーブルを入力**と同様に、空の側がソースから入力されます。


## 例


### RFCパラメーター


**使用するエージェント**を選択します。ドロップダウンバーから**ターゲットディレクトリ**を選択し、下で、ファイルの宛先となる正しい子フォルダーを参照します。次に、「Target File Name」に適切な名前を付けます。「Function Call Information」で、Function、**戻り値パラメーター**を入力し、パラメーターを選択します。



パラメーターセクションで、**行を挿入**または**行を追加**を選択できます。また、パラメーターに名前を付けて値を設定します。**最大同時リクエスト数**の値を選択し、「Wait for RFC to Complete」を選択します。保存して実行します。
