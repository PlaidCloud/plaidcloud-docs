---
title: Call SAP General Ledger Postingステップ
description: SAP ECC / S/4HANAのRemote Function Call（RFC）を呼び出し、VATおよび源泉徴収税を含む仕訳を転記します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## 説明


SAP ECC / S/4HANAのRemote Function Call（RFC）を呼び出し、該当するVATおよび源泉徴収税を含む仕訳を転記します。テストモードでも実行でき、その場合は転記処理を実行しますが、転記は完了しません。これにより、勘定科目が締められている、指定した会社コードに顧客が存在しないなど、検出可能なエラーを収集できます。エラーチェックは堅牢で、1回のテストで複数のエラーを検出して返すことができます。


## 例


### RFCパラメーター


**使用するエージェント**を選択します。ドロップダウンバーから**ターゲットディレクトリ**を選択し、その下でファイルの保存先となる子フォルダーを参照して選択します。次に、「Target File Name」に適切な名前を付けます。「Function Call Information」で、Function、**戻り値パラメーター**を入力し、パラメーターを選択します。 



「Parameters」セクションで**行を挿入**または**行を追加**を選択できるほか、パラメーターに名前を付けて値を設定できます。**最大同時リクエスト数**を選択し、「Wait for RFC to Complete」を選択します。ステップを保存して実行します。


## 伝票を転記に変換する

保存済みのステップには **ドキュメント転記に変換…** ボタンがあります。最初に、何が変換されるか（ドキュメントのフィールドに対応付けられる列の数と、システムに振り分けられるエンティティの数）が表示され、確定すると、ステップが **伝票を転記** ステップに変更されます（[ERPシステムに伝票を転記する](/ja/guides/connections/post-documents/)を参照）。古い設定は、ステップのバージョンに残ります。
