---
title: Convert Document Encoding
description: PlaidCloudワークフローステップで文字セット間のドキュメントファイルのエンコードを変換し、エンコードの互換性の問題を解消します。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## 説明



テキストファイルを、ある文字エンコードから別の文字エンコードに再エンコードします。ソースファイルがレガシーエンコード（Windows-1252、ISO-8859-1）で届くものの、下流のツールがUTF-8を必要とする場合（またはその逆）に便利です。

ソースファイルがUTF-8でない場合、そのエンコードはファイルの内容から割り出されます。非常に短いファイルや繰り返しの多いファイルは、手がかりが少なすぎて誤って読み取られることがあるため、そのようなファイルの変換後の出力は確認してください。

ターゲットエンコードで表現できない文字があると、デフォルトではステップが失敗します。**ターゲットエンコードで表現できない文字を ? に置き換える**を選択すると、Javaのライターと同様に、その文字の代わりに`?`が書き込まれ、ステップは完了します。

ステップの設定でターゲットエンコードを選択します。特定のエンコード用のショートカットについては、[UTF-8](/ja/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)、[UTF-16](/ja/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)、[ASCII](/ja/reference/workflow-steps/document/convert-document-encoding-to-ascii/)の各バリエーションを参照してください。


## 例


ソース入力を作成し、入力ファイルを選択して、その場所にあるファイルを参照します。出力先を選択し、ファイルの保存先を参照して選択します。保存して実行します。
