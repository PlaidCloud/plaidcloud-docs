---
title: Call SAP Financial Document Attachmentステップ
description: ワークフローステップからSAPの財務伝票の添付ファイルを取得し、伝票の抽出と処理を自動化します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## 説明



RFC（Remote Function Call）を使用して、SAP ECC / S/4HANAの特定のFI（財務会計）伝票にファイルを添付します。スキャンした請求書、承認ワークフロー、契約書の写しなど、裏付けとなる書類を、それに対応する財務仕訳とあわせて登録する場合に便利です。

SAPコネクターで設定されたSAP RFCの認証情報と、対象のFI伝票番号（会社コード、伝票番号、会計年度）が必要です。


## 保存時に確認される内容

このステップは、**テーブルデータの選択**タブの出力列にある`relative_file_path`列から各ファイルのパスを読み取ります。この列はテキスト型である必要があります。この列がない場合、保存は拒否されます — *The output columns must include relative_file_path, the path of each file to attach.* 別のデータ型の場合も同様です — *The relative_file_path column must be text, not integer.*

ソーステーブルを選択しているものの、ソース列またはターゲット列が指定されていない状態で保存すると、**両方のマッピングテーブルを入力**を実行した場合と同様に、空の側がソースから補完されます。


## 例


### RFCパラメーター


**使用するエージェント**を選択します。ドロップダウンバーから**ターゲットディレクトリ**を選択し、その下でファイルの保存先となる子フォルダーを参照して選択します。次に、「Target File Name」に適切な名前を付けます。「Function Call Information」で、Function、**戻り値パラメーター**を入力し、パラメーターを選択します。



「Parameters」セクションで**行を挿入**または**行を追加**を選択できるほか、パラメーターに名前を付けて値を設定できます。**最大同時リクエスト数**を選択し、「Wait for RFC to Complete」を選択します。ステップを保存して実行します。
