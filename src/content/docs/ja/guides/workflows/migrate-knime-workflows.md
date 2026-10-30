---
title: KNIMEワークフローを移行する
description: KNIMEワークフロー（.knwf）またはワークフローグループ（.knar）を、Analyzeアプリ、REST API、またはMCP接続のAIエージェントからPlaidCloudの高度なワークフローに変換し、入力と接続をバインドして、変換レポートを読み取ります。
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloudはKNIMEのドロップインの代替です。KNIMEノード設定の98.5%が完全に変換され、207種類のコアノードのうち205種類がFullです。各ノードは、そのノードの処理を行う標準のPlaidCloudワークフローステップになります。コンバーターは、KNIMEのワークフローアーカイブを実行可能な高度なワークフローに変換し、元のグラフを保持して、設定が必要な項目を示す変換レポートを返します。すべてのノードは[KNIME変換マトリックス](/ja/reference/knime-conversion-matrix/)で確認できます。

変換で読み取るのは、指定したアーカイブだけです。KNIMEノードが読み取りや書き込みを行う先のシステムには接続しません。

変換は1回限りの操作です。同じアーカイブをもう一度変換すると新しいワークフローが作成され、PlaidCloudで加えた編集が後からのエクスポートとマージされることはありません。

## PlaidCloudが作成するもの

- KNIMEワークフローごとに1つの高度なワークフロー。`.knwf`からは1つのワークフローが、`.knar`からはグループ内のワークフローごとに1つずつ作成されます。
- 各KNIMEノードは、対応するワークフローステップ、プロジェクト変数、またはキャンバスオブジェクトになり、上流と下流の関係は維持されます。メタノードとコンポーネントはワークフローに展開されるため、それらのノードは通常のステップとして実行されます。
- フロー変数と、ConfigurationノードおよびWidgetノードは、デフォルト値を保持するプロジェクト変数になります。変換時に値が確定しているスイッチとループは、削除され、実行されるステップに展開されます。
- KNIMEの式言語（Expression、String Manipulation、Math Formula、Column Expressions、Rule Engine）は、PlaidCloudの式に変換されます。
- アーカイブに含まれるデータファイルは、プロジェクトのデフォルトのドキュメントアカウントの`knime/`フォルダーに、ワークフローごとに1つのフォルダーとしてアップロードされ、変換後のリーダーはそこからインポートします。
- ビュー、チャート、カラーマネージャーはデータに影響しません。これらは削除され、変換レポートに一覧表示されます。

## 始める前に

1. KNIME Analytics Platformからワークフローを`.knwf`ファイルとしてエクスポートします。複数のワークフローを一度に変換するには、ワークフローグループを`.knar`ファイルとしてエクスポートします。リーダーが使用するファイルは、アーカイブに含まれるようにワークフローの`data`フォルダーに置いてください。
2. 読み取り可能な[ドキュメントアカウント](/ja/guides/documents/adding-accounts/)にアーカイブをアップロードします。Analyzeアプリでは、インポートウィンドウの**参照**でお使いのコンピューターからアップロードできます。
3. ワークフローを受け取るPlaidCloudプロジェクトを選択します。そのプロジェクトのアーキテクトまたはマネージャーであり、プロジェクトにデフォルトのドキュメントアカウントがある必要があります。
4. ワークフローのリーダーとコネクターノードに使用させるPlaidCloudのテーブル、ファイル、接続を控えておきます。[ソースをバインドする](#ソースをバインドする)を参照してください。

## ワークフローを変換する

Analyzeアプリ、REST API、またはMCP接続のAIエージェントから変換します。REST APIとMCPツールは同じフィールドを受け取ります。ウィンドウでは、表示されているフィールドを使用します。

### Analyzeアプリ

1. **Analyze**を開き、**Tools → Import KNIME Workflow**を選択します。
2. **Import Source and Target**で、**Target Project**と、ドキュメントアカウント内の**KNIME Archive (.knwf or .knar)** を選択します。お使いのコンピューターからアーカイブをアップロードするには、**Browse**を選択します。
3. **Object Prefixes**で、必要に応じて**Workflow Prefix**、**Step Prefix**、**Table Prefix**を設定します。テーブルプレフィックスのデフォルトはワークフローの名前です。
4. **Source Bindings (optional)** で、必要に応じてリーダーをターゲットプロジェクト内の既存のテーブルにバインドします。**Add**を選択し、**KNIME Reader**（`12:3`のようなノードID、ノード名、またはファイル名）と**Table ID**を入力します。接続、ドキュメント、他のプロジェクトのテーブルをバインドするには、REST APIまたはMCPツールを使用します。[ソースをバインドする](#ソースをバインドする)を参照してください。
5. **Import**を選択します。

ウィンドウにはアーカイブの変換中は進行状況が表示され、その後に変換レポートが表示されます。レポートには、ステップ数（**Steps**、**High confidence**、**Medium**、**Low**、**Not converted**）、変換できなかったノードとその下流のステップ、部分的な変換、警告、アップロードするソースファイル、ステップのないノードが含まれます。確認が必要な項目がない場合はその旨が表示され、ウィンドウは自動的に閉じます。

### フィールド

| フィールド | 必須 | 内容 |
| --- | --- | --- |
| `source_account_id` | はい | KNIMEアーカイブを保持するドキュメントアカウント。 |
| `source_file_path` | はい | そのアカウント内にある`.knwf`または`.knar`ファイルのパス。 |
| `project_id` | はい | ワークフローを作成するプロジェクト。 |
| `workflow_prefix` | いいえ | ワークフロー名に付けるプレフィックス。 |
| `step_prefix` | いいえ | ステップ名に付けるプレフィックス。 |
| `table_prefix` | いいえ | テーブル名に付けるプレフィックス。デフォルトはワークフロー自身の名前です。既存のテーブル名と重複することになるプレフィックスは、何も作成される前に拒否されます。`.knar`の場合、各ワークフローのプレフィックスの後ろにそのワークフローの名前が付きます。 |
| `source_bindings` | いいえ | リーダーとコネクターノードを、すでにあるデータや接続にバインドします（最大500件）。[ソースをバインドする](#ソースをバインドする)を参照してください。 |

### REST

フィールドをJSON本文として次の宛先に送信します。

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

MCP接続のAIエージェントが、同じフィールドを指定して`knime_convert`ツールを呼び出します。エージェントの接続方法は[AIエージェント（MCP）](/ja/integrations/ai-coding-agents/)を参照してください。このツールはプロジェクトを変更するため、承認する前に呼び出し内容を確認してください。

## ソースをバインドする

`source_bindings`を使用すると、KNIMEリーダーをアーカイブ内のコピーではなく、PlaidCloudにすでにあるデータに向けることができます。キーには、ノードID（`12:3`など）、ノード名、同梱ファイルのパス（`data/sales.csv`など）、ファイル名のいずれかを指定でき、この順序で最初に一致したものが使用されます。値は次のいずれかです。

- ターゲットプロジェクト内のテーブルの`analyzetable_`ID。そのテーブルがリーダーに置き換わります。
- 読み取り可能な別のプロジェクトのテーブルには、`{"project": "<project id>", "table": "<table id>"}`。リーダーは、そのテーブルをコピーする[Import Project Table](/ja/reference/workflow-steps/import/import-project-table/)ステップになります。ソースプロジェクトは、ターゲットプロジェクトに対して読み取りを共有している必要があります。共有していない場合、ステップは警告を出します。行アクセスで管理されているテーブルは拒否されます。
- 読み取り可能なドキュメントには、`{"account": "<document account id>", "path": "/finance/budget.xlsx"}`。リーダーがそのドキュメントをインポートします。
- データベースまたはREST接続のコネクターノードには、`{"connection": "<connection id>"}`。変換後のステップはその接続で実行されます。

Analyzeアプリのウィンドウでは、テーブルIDを使ってリーダーをターゲットプロジェクト内のテーブルにバインドします。接続、ドキュメント、他のプロジェクトのテーブルは、REST APIまたはMCPツールでバインドしてください。

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

存在しないテーブルへのバインドや、どのリーダーにも一致しないキーは警告になります。適用されたバインドは、プロジェクト名とテーブル名とともに、変換レポートの`bindings`に一覧表示されます。

### バインドされていない入力

アーカイブにファイルがないリーダーは、デフォルトのドキュメントアカウントにあるワークフローのフォルダー内の`inputs/<file name>`から読み取ります。変換レポートの`missing_inputs`にそのパスが警告とともに一覧表示されます。そのパスにファイルをアップロードして、ワークフローを実行してください。ファイルが置かれるまで、インポートは警告付きで完了して空のテーブルを作成し、ワークフローは続行されます。

## 認証情報と接続

KNIMEの認証情報は移行されません。他のシステムにサインインする各ステップは、認証情報をPlaidCloudの接続または設定したプロジェクト変数から読み取ります。どちらを使用するかは、変換レポートのそのステップの警告に記載されます。

| KNIME | 設定する内容 |
| --- | --- |
| データベースコネクター | データベース接続。`{"connection": "<id>"}`でバインドするか、ステップで選択します。 |
| サインインを行うRESTおよびWebサービスノード | [REST接続](/ja/reference/connectors/rest/generic-rest/)。`{"connection": "<id>"}`でバインドするか、ステップで選択します。 |
| Speech Recognizer (IBM Watson) | ベースURLが警告に示されたWatsonサービスURLで、ユーザーが`apikey`、基本認証のパスワードがお客様のAPIキーであるREST接続。ノードにバインドします。 |
| Email Connector（Email ReaderまたはEmail Mover併用） | 警告に示された名前を持つ、メールサーバーのパスワードを保持するプロジェクト変数。ホストとユーザーはEmail Connectorから取得されます。 |
| パスワード付きブックを使用するExcel ReaderまたはExcel Writer | 警告に示された名前を持つ、パスワードを保持するプロジェクト変数。 |
| LLMコネクターと認証ノード | AIステップのLLM接続。 |

プロジェクト変数の設定方法は、[ワークフロー変数を管理する](/ja/guides/workflows/manage-workflow-variables/)を参照してください。

## 変換レポートを読む

インポートが完了すると、Analyzeアプリのウィンドウに変換レポートが表示されます。RESTとMCPのレスポンスにも同じレポートが含まれます。ワークフローを実行する前に確認してください。

- `summary`は、作成されたステップ数と、信頼度が高、中、低でマッピングされたステップ数を示します。
- `warnings`は、各警告をノード、ステップ、および取るべき対応とともに一覧表示します。設定が必要なすべての認証情報と接続も含まれます。
- `missing_inputs`は、バインドされていない入力のファイルをアップロードするドキュメントのパスを一覧表示します。
- `bindings`は、適用されたバインドを一覧表示します。
- `table_prefix`は、使用されたプレフィックスです。`.knar`の場合、`workflows`に各ワークフローとそれぞれのプレフィックスが一覧表示されます。
- レポートと並んで表示される`uploaded_files`は、デフォルトのドキュメントアカウントにアップロードされた同梱ファイルを一覧表示します。
- `dropped_tools`は、削除されたビューとチャートを一覧表示します。

## プレースホルダー

変換パスのないノードは、名前付きのプレースホルダーとしてキャンバスに残ります。プレースホルダーはデータをそのまま通過させ、KNIMEノードの名前とともに警告を出します。その下流のステップはすべてレポートでフラグが付けられるため、結果の欠落が見過ごされることはありません。結果が重要な場合は、標準のステップでその機能を再構築してください。

## 変換したワークフローを実行する

1. プロジェクトで新しいワークフローを開きます。
2. 警告に示されたプロジェクト変数と接続を設定します。
3. バインドされていない入力のファイルを、ウィンドウの**Source files to upload**に示されたパス、または`missing_inputs`のパスにアップロードします。
4. [ワークフローを実行](/ja/guides/workflows/run-a-workflow/)し、各ステップの出力テーブルを確認します。

## エッジケース

KNIMEとの既知の違いは、以下のみです。

- **Crosstab。** [Table: Pivot ステップ](/ja/reference/workflow-steps/tables/table-pivot/)に変換されます。一部の設定の組み合わせでは、KNIMEと結果が異なります。
- **Loop End (Column Append)。** [テーブル: 内部結合 ステップ](/ja/reference/workflow-steps/tables/table-inner-join/)に変換されます。一部の設定の組み合わせでは、KNIMEと結果が異なります。
- **ランダム抽出。** Row Sampler、Table Partitioner、Equal Size Samplingは、[Table KNIME Random Sample ステップ](/ja/reference/workflow-steps/tables/table-knime-random-sample/)でKNIME独自のランダム抽出を行うため、シードを指定したノードはKNIMEと同じ行を選択します。抽出できるテーブルは最大10,000,000行までで、それより大きいテーブルではステップが失敗します。

## 関連ガイド

- [KNIME変換マトリックス](/ja/reference/knime-conversion-matrix/)
- [REST接続](/ja/reference/connectors/rest/generic-rest/)
- [ドキュメントアカウントを追加する](/ja/guides/documents/adding-accounts/)
- [ワークフロー変数を管理する](/ja/guides/workflows/manage-workflow-variables/)
- [ワークフローを実行する](/ja/guides/workflows/run-a-workflow/)
