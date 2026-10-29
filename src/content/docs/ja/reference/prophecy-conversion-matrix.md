---
title: Prophecy 変換マトリックス
description: PlaidCloud が Prophecy のパイプラインと SQL プロジェクトをネイティブの高度なワークフローのステップに変換する方法を、gem ごとの対応状況とともに説明します。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud は、Prophecy の Spark パイプラインと SQL プロジェクトをネイティブの高度なワークフローに変換します。インポーターは各 Prophecy gem をワークフローのステップ、プロジェクト変数、またはキャンバスオブジェクトにマッピングするため、変換後のワークフローはエミュレーションではなく、クラウドネイティブで実行されます。

すべての gem、コネクター、プロジェクト構造が変換されます。**完全**とは、gem がその処理を行うネイティブの PlaidCloud ステップ、変数、またはキャンバスオブジェクトになることを意味します。変換後のワークフローが自動的には再現しないわずかな動作は、[既知のエッジケース](#既知のエッジケース)に、対処方法とともに記載しています。

変換の手順については、[Prophecy プロジェクトの移行](/ja/guides/workflows/migrate-prophecy-projects/)を参照してください。

## Spark パイプラインの gem

### ソース/ターゲット

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Lookup | 完全 | [テーブル: 参照](/ja/reference/workflow-steps/tables/table-lookup/) | 各 lookup の呼び出しは、それを使用するステップ内の参照ステップになります。一致しないキーは NULL として読み取られ、重複したキーはそのうちの1行を返します。 |
| Source | 完全 | データセット形式に応じて選択されるインポートステップ（[コネクター](#コネクター)を参照） | 各 Source は、データセット名にちなんだテーブルへのインポートステップになります。コンバーターが認識しない形式は、ワークフローのドキュメントフォルダーにアップロードされた CSV ファイルとして読み取られ、警告が出ます。 |
| Streaming Source | 完全 | バッチの Source と同じインポート | ストリーミングソースは、警告付きで1回限りのバッチインポートに変換されます。 |
| Streaming Target | 完全 | バッチの追加ロード | ストリーミングターゲットは、警告付きでバッチの追加に変換されます。 |
| Target | 完全 | データセット形式と writeMode に応じて選択されるテーブルのエクスポート/ロードステップ | 各 Target は、gem の書き込みモードのテーブルロードまたはエクスポートステップになります。書き込みモードは、追加、上書き、SET 式付きのマージ、アップサート、SCD2、replaceWhere、insertInto です。 |

### 準備

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Data Cleansing | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内の列式 | null の補完、トリム、大文字小文字のオプションを列式に変換します。クレンジングされた列は最後に移動します。 |
| Sequence | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（行番号式付き） | 開始値と増分から連番列を追加します。 |
| Surrogate Key Generator | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（行番号式付き） | 初期値から連番のキーを追加します。キーは、最後に発行したキーを保持するテーブルから、実行をまたいで継続されます。 |

### 変換

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Aggregate | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（集計付き）。gem がピボットする場合は[Pivot](/ja/reference/workflow-steps/tables/table-pivot/) | グループ化して集計し、HAVING 条件を適用して、ピボット値ごとに1つの列にピボットします。propagate-all は、他のすべての入力列を引き継ぎます。 |
| Bulk Column Expressions | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内で、列ごとに1つの式に展開 | 列挙された列ごとに、テーブル: 抽出ステップ内の1つの式になります。変換時に、gem のレイアウトを前提としているという警告が出ます。 |
| Bulk Column Rename | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内の列名変更 | 列挙された列ごとに、テーブル: 抽出ステップ内の1つの名前変更になります。変換時に、gem のレイアウトを前提としているという警告が出ます。 |
| Deduplicate | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（distinct または行番号フィルター付き） | キーごとに1行を残します。distinct、並べ替え順序による最初または最後、任意の1行、またはちょうど1回だけ現れるキーのみを選べます。 |
| Dynamic Replace | 完全 | 動的置換変換（手動で設定） | 動的置換変換の置換ルールに変換されます。変換時に、gem のレイアウトを前提としているという警告が出ます。 |
| Dynamic Select | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内の、タイプで解決される列の選択 | 変換時に、タイプによって列を解決し、明示的な選択にします。 |
| Filter | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（フィルター式付き） | フィルター式付きのテーブル: 抽出ステップに変換されます。NULL の条件は行を除外します。 |
| Flatten Schema | 完全 | [JSON 解析](/ja/reference/workflow-steps/tables/table-json-parse/)と[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | ネストされたフィールドを、gem の区切り文字で名前を付けた列にフラット化し、配列を要素ごとに1行に展開します。 |
| Fuzzy Match | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)と[User Defined Transform](/ja/reference/workflow-steps/general/user-defined-transform/)ステップ | レコードをペアにし、gem の方式で各一致フィールドをスコア付けし、スコアを平均して、しきい値以上のペアを残します。 |
| Group By Rollup | 完全 | ロールアップレベルごとの[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)集計ステップの和集合 | ロールアップをグルーピングレベルごとに1つの集計に展開し、NULL の小計とともに和集合にします。 |
| Limit | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（行数制限付き） | 行数制限に変換されます。設定の参照はプロジェクト変数になります。 |
| Normalize | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（展開式付き） | 長さの式に従って各レコードを繰り返し、インデックスごとに出力列を計算して、終了条件が成立した最初のインデックスで停止します。 |
| Order By | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ上の並べ替え | 同じキー、方向、null の位置で並べ替えに変換されます。 |
| Reformat | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（列式付き） | 出力列ごとに1つの式を持つテーブル: 抽出ステップに変換されます。列挙されていない列は除外されます。 |
| Sample Rows | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（行数制限またはランダムサンプル付き） | 行のランダムな割合または件数を残します。サンプリングはランダムなため、選ばれる行は Spark の実行時とは異なります。 |
| Schema Transform | 完全 | 順に適用される[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップの連鎖 | 各操作を順に適用します。列の追加または置換、削除、名前変更、デフォルト付きの不足時追加、プロジェクトのビジネスルールの追加です。 |
| Set Operation | 完全 | [テーブル: 和集合（すべて）](/ja/reference/workflow-steps/tables/table-union-all/)。except には[テーブル: アンチ結合](/ja/reference/workflow-steps/tables/table-anti-join/)、intersect には[テーブル: 内部結合](/ja/reference/workflow-steps/tables/table-inner-join/) | union all は入力を積み重ねます。except all と intersect all は、重複行を正しい数だけ残します。 |
| TransposeAgg | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（集計付き） | gem のグルーピング、集計、ピボットを Aggregate として変換し、確認を促す警告が出ます。 |
| Unpivot | 完全 | [Melt](/ja/reference/workflow-steps/tables/table-melt/) | 選択された列を、名前列と値列に積み重ねます。 |
| Watermark | 完全 | ステップは不要 | 削除: バッチの実行は存在するすべてのデータを読み取るため、適用する遅延データのカットオフがありません。 |
| Window Function | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内のウィンドウ式 | gem のパーティション、順序、フレーム（行または範囲）を使い、無制限、現在行、またはオフセットの境界でウィンドウ列を追加します。 |

### 結合/分割

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Compare Columns | 完全 | 完全外部結合と列ごとの集計 | アンピボットしたデータの完全外部結合で列を比較し、一致数と不一致数を出力します。 |
| Join | 完全 | [テーブル: 内部結合](/ja/reference/workflow-steps/tables/table-inner-join/)、[複数テーブル結合](/ja/reference/workflow-steps/tables/table-multi-table-join/)、[テーブル: アンチ結合](/ja/reference/workflow-steps/tables/table-anti-join/)、または[テーブル: クロス結合](/ja/reference/workflow-steps/tables/table-cross-join/) | inner、left、right、full、semi、anti、cross、natural の各タイプの結合を、任意の結合条件で構築し、where 句を適用して、select リストを書き出します。 |
| Repartition | 完全 | ステップは不要 | 削除: パーティショニングは PlaidCloud が管理するため、次のステップは上流のテーブルを直接読み取ります。 |
| Row Distributor | 完全 | 出力ごとに1つの[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)フィルター | 出力ごとに1つのフィルターに変換されます。行は複数の出力に振り分けられることがあります。 |

### 解析

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Column Parser | 完全 | [JSON 解析](/ja/reference/workflow-steps/tables/table-json-parse/) / [XML解析](/ja/reference/workflow-steps/tables/table-xml-parse/) | 指定した列の JSON または XML 解析に変換されます。変換時に、gem のレイアウトを前提としているという警告が出ます。 |

### カスタム

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | 完全 | gem が生成したコードを実行する[User Defined Transform](/ja/reference/workflow-steps/general/user-defined-transform/)ステップ | パイプラインのエクスポートに含まれる、gem が生成した PySpark コードが Python ステップで実行され、確認を促す警告が出ます。 |
| CustomReformatBitbucket | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | gem が持つ式を使った Reformat として変換され、確認を促す警告が出ます。 |
| Data Quality Check | 完全 | チェックごとに1つの結果行を持つ[テーブル: 和集合（すべて）](/ja/reference/workflow-steps/tables/table-union-all/)。失敗時に停止するには[ワークフローエラーの発生](/ja/reference/workflow-steps/workflow-control/raise-workflow-error/) | 入力に対して各チェックを評価し、チェックごとに、ステータスとメッセージを持つ1つの結果行を書き出します。データはそのまま渡され、gem の失敗しきい値に達すると実行が停止します。 |
| Deequ | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)のチェック | データをそのまま渡し、isComplete、isUnique、isNonNegative、isContainedIn の各ルールの制約結果テーブルを構築します。 |
| Delta Table Operations | 完全 | [テーブル: インプレース削除](/ja/reference/workflow-steps/tables/table-in-place-delete/)、[Table Update](/ja/reference/workflow-steps/tables/table-update/)、[Table Drop](/ja/reference/workflow-steps/tables/table-drop/)、[Table Restore to Timestamp](/ja/reference/workflow-steps/tables/table-restore-timestamp/)ステップ | 削除、更新、ドロップ、タイムスタンプへの復元はテーブルステップにマッピングされます。optimize、vacuum、バージョン指定の復元は、警告付きでデータをそのまま渡します。 |
| Directory | 完全 | [ディレクトリ一覧](/ja/reference/workflow-steps/document/directory-listing/) | バインドされたドキュメントフォルダーのファイルを、gem の列で一覧表示します。シート名オプションを使うと、各ブックがシートごとに1行を返します。フォルダーが存在しない場合は0行になります。 |
| Email | 完全 | [通知: メール](/ja/reference/workflow-steps/notifications/notify-via-email/) | バインドされたメール接続を通じて、必要に応じてデータの添付付きでメールを送信します。 |
| Email Data | 完全 | [通知: メール](/ja/reference/workflow-steps/notifications/notify-via-email/) | 入力行をテーブルとしてメール送信し、入力はそのまま渡します。 |
| File Operation | 完全 | [Copy Document File](/ja/reference/workflow-steps/document/copy-document-file/)または[Copy Document Directory](/ja/reference/workflow-steps/document/copy-document-directory/)ステップ | バインドされたドキュメントフォルダーから、変換後のワークフローのドキュメントフォルダーに、ファイルをコピー、移動、または同期します。移動の場合は元のファイルが削除されます。 |
| Log | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | gem のイベント行（時刻、gem 名、イベントタイプ、テキスト）を出力テーブルに書き込みます。 |
| REST API Enrich | 完全 | [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | 行ごとに1回 API を呼び出し、レスポンスの列を追加します。 |
| Script | 完全 | フレームアクセスを書き換えた Python ステップ | スクリプト本体を Python ステップに埋め込み、データフレームへのアクセスを書き換えます。Scala の本体は注記付きで引き継がれます。 |
| Soda Data Quality Check | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)のチェック | Soda のチェックからチェック結果テーブルを構築します。 |
| SQL Statement | 完全 | 出力タブごとの SQL ステップ。テキストはテナントの方言に変換 | 各タブを、入力を一時テーブルとしてバインドした SQL ステップに埋め込みます。テナントの方言に変換されます。 |
| Todo | 完全 | [ワークフローエラーの発生](/ja/reference/workflow-steps/workflow-control/raise-workflow-error/)または[Notify via Log](/ja/reference/workflow-steps/notifications/notify-via-log/)ステップ | まだ書かれていないロジックを示します。何も読み取らない場合はログメッセージ、後続のステップが依存している場合は、gem のメッセージ付きで実行を停止するステップになります。 |

### レポート

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Tableau | 完全 | [Publish to Tableau](/ja/reference/workflow-steps/export/export-to-tableau/)ステップ | Hyper 抽出を書き出し、バインドされた Tableau 接続に公開します。 |

### ML/AI

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Bedrock | 完全 | [Text NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ | ワークスペースの AI 接続を通じて、テキスト列を埋め込みます。 |
| OpenAI | 完全 | [Text NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ | ワークスペースの AI 接続を通じて、質問に回答するか、テキストを埋め込みます。 |
| Pinecone Lookup | 完全 | [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | 行ごとに Pinecone インデックスにクエリを実行し、pinecone_matches と pinecone_error の列を追加します。 |
| SageMaker Endpoint | 完全 | [Text NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ | ワークスペースの AI 接続を通じて質問に回答します。 |
| Text Processing | 完全 | チャンク分割には[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)、Web スクレイピングには[RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | チャンク分割は文字数ベースのチャンク式になります。Web スクレイピングは、各行の URL を取得し、ページの内容を行に結合し直します。 |

### サブグラフ/制御

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Control Flow Input | 完全 | 削除（境界マーカーのみ） | 削除されます。イテレーターのサブワークフローの入力境界を示すだけのものです。 |
| Control Flow Output | 完全 | 削除（境界マーカーのみ） | 削除されます。イテレーターのサブワークフローの出力境界を示すだけのものです。 |
| Subgraph (Basic) | 完全 | インラインプロセスからのキャンバスコンテナ / ネストされたワークフロー | インラインの内部グラフを、入出力テーブルパラメーター付きのネストされたワークフロー（またはインライン化されたステップ）に変換します。 |
| Table Iterator | 完全 | [Workflow Loop](/ja/reference/workflow-steps/workflow-control/workflow-loop/)ステップ | 入力行ごとにループ本体を1回実行し、各設定値をその列から設定します。上限は maxIteration です。 |
| While Iterator | 完全 | [Workflow Loop](/ja/reference/workflow-steps/workflow-control/workflow-loop/)ステップ | 反復番号を渡しながら、本体が行を返さなくなるか gem の最大値に達するまで、パスごとにループ本体を1回実行します。 |

## SQL / アナリスト gem

### ソース/ターゲット

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | 完全 | 対応するデータベース接続を使った外部データのインポート/エクスポートステップ | PlaidCloud の接続を通じて、外部データベースのテーブルを読み取るか書き込みます。 |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | 完全 | ドキュメントアカウント（ADLS/GCS/S3/SFTP/SharePoint/OneDrive）に対するファイルのインポート/エクスポートステップ | クラウド/SFTP ストレージのファイルを読み取るか書き込みます。ワイルドカードによる和集合、トリガー、削除/移動、暗号化のオプションに対応しています。 |
| Model | 完全 | 上流ステップの出力テーブル | 別のモデルを、参照先の上流ステップが生成したテーブルとして読み取ります。 |
| Seed | 完全 | [インポート: CSV](/ja/reference/workflow-steps/import/import-csv/) | シード CSV を PlaidCloud のテーブルにインポートします。 |
| Source | 完全 | データセット形式に応じて選択されるインポートステップ（[コネクター](#コネクター)を参照） | 各 Source は、データセット名にちなんだテーブルへのインポートステップになります。コンバーターが認識しない形式は、ワークフローのドキュメントフォルダーにアップロードされた CSV ファイルとして読み取られ、警告が出ます。 |
| Target Model / Table (Target) | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)、[Upsert](/ja/reference/workflow-steps/tables/table-upsert/)、[テーブルのコピー](/ja/reference/workflow-steps/tables/table-copy/)、[テーブル: 和集合（すべて）](/ja/reference/workflow-steps/tables/table-union-all/) | モデルの最終 select を、置換、追加、アップサート、削除して挿入、SCD2、または述語による置換として PlaidCloud のテーブルに書き込みます。 |
| Upload Files | 完全 | [インポート: CSV](/ja/reference/workflow-steps/import/import-csv/) | アップロードされたローカルファイルが、インポートステップによってテーブルになります。 |

### 準備

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Data Cleansing | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内の列式 | null の補完、トリム、大文字小文字のオプションを列式に変換します。クレンジングされた列は最後に移動します。 |
| Data Masking | 完全 | 文字のマスキングまたはハッシュ化のための列式 | 選択された文字列の列を、その場で、または新しい列としてマスキングまたはハッシュ化します。 |
| Find Duplicates | 完全 | 行番号のウィンドウ式とフィルター | キーごとに、一意の行、重複行、または件数/位置で選択した行を返します。 |
| Generate Rows | 完全 | 入力行ごとに結合してフィルターされるシーケンステーブル | 初期化、条件、ループの式から、入力行ごとに行を生成します。 |
| Imputation | 完全 | 集計と、結合し直した列式 | null またはセンチネル値を、平均、中央値、最頻値、または固定値で置き換えます。 |
| Multi-Column Edit | 完全 | テンプレートから展開される列ごとの式 | 1つの式テンプレートを、選択されたすべての列に適用します。 |
| Multi-Column Rename | 完全 | select ステップ上の列名変更マッピング | 選択された列の名前を、接頭辞、接尾辞、または名前の式で変更します。 |
| Record ID | 完全 | 行番号または uuid の列式 | UUID または連番のレコード ID 列を追加します。 |
| Sample | 完全 | 抽出ステップの行数制限またはサンプルオプション | 全体またはグループごとに、先頭/末尾/ランダム/N 番目/パーセントの行を取得します。 |
| Tile | 完全 | タイル番号とシーケンスのためのウィンドウ式 | 等しい合計、件数、標準偏差の区間、一意の値、または手動のカットオフでタイル番号を割り当てます。 |

### 変換

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Aggregate | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（集計付き）。gem がピボットする場合は[Pivot](/ja/reference/workflow-steps/tables/table-pivot/) | グループ化して集計し、HAVING 条件を適用して、ピボット値ごとに1つの列にピボットします。propagate-all は、他のすべての入力列を引き継ぎます。 |
| Count Records | 完全 | 件数関数を使った集計ステップ | 合計、非 null、または distinct の件数を1行で返します。 |
| Data Encoder/Decoder | 完全 | base64/hex のエンコードとデコードのための列式 | 選択された列をエンコードまたはデコードします。AES は Databricks のみです。 |
| Deduplicate | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（distinct または行番号フィルター付き） | キーごとに1行を残します。distinct、並べ替え順序による最初または最後、任意の1行、またはちょうど1回だけ現れるキーのみを選べます。 |
| Dynamic Select | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内の、タイプで解決される列の選択 | 変換時に、タイプによって列を解決し、明示的な選択にします。 |
| Filter | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（フィルター式付き） | フィルター式付きのテーブル: 抽出ステップに変換されます。NULL の条件は行を除外します。 |
| Finance | 完全 | 財務関数を実装する列式 | 財務関数（FV、PV、NPV、IRR など）の結果を新しい列として追加します。 |
| Flatten Schema | 完全 | [JSON 解析](/ja/reference/workflow-steps/tables/table-json-parse/)と[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | ネストされたフィールドを、gem の区切り文字で名前を付けた列にフラット化し、配列を要素ごとに1行に展開します。 |
| Fuzzy Match | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)と[User Defined Transform](/ja/reference/workflow-steps/general/user-defined-transform/)ステップ | レコードをペアにし、gem の方式で各一致フィールドをスコア付けし、スコアを平均して、しきい値以上のペアを残します。 |
| Limit | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（行数制限付き） | 行数制限に変換されます。設定の参照はプロジェクト変数になります。 |
| Order By | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ上の並べ替え | 同じキー、方向、null の位置で並べ替えに変換されます。 |
| Pivot | 完全 | [Pivot](/ja/reference/workflow-steps/tables/table-pivot/) | 選択されたピボット値を集計の列に変換します。設計時に取得された Simple モードの値リストは、列挙された値として変換されます。 |
| Reformat | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（列式付き） | 出力列ごとに1つの式を持つテーブル: 抽出ステップに変換されます。列挙されていない列は除外されます。 |
| Running Total | 完全 | 累積和のウィンドウ式の列 | 選択された列ごとに累積和を追加します。 |
| Snowflake Unpivot (third-party) | 完全 | [Melt](/ja/reference/workflow-steps/tables/table-melt/) | Snowflake の UNPIVOT で列をアンピボットします。 |
| Transpose | 完全 | [Melt](/ja/reference/workflow-steps/tables/table-melt/) | データ列を、名前列と文字列の値列に積み重ねます。 |
| TransposeAgg | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)（集計付き） | gem のグルーピング、集計、ピボットを Aggregate として変換し、確認を促す警告が出ます。 |
| Unpivot | 完全 | [Melt](/ja/reference/workflow-steps/tables/table-melt/) | データ列を、名前列と値列に積み重ねます。 |
| Weighted Average | 完全 | 加重平均の式を使った集計ステップ | 全体またはグループごとに加重平均を計算します。 |
| Window Function | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)ステップ内のウィンドウ式 | gem のパーティション、順序、フレーム（行または範囲）を使い、無制限、現在行、またはオフセットの境界でウィンドウ列を追加します。 |

### 結合/分割

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Except | 完全 | すべての列に対する[テーブル: アンチ結合](/ja/reference/workflow-steps/tables/table-anti-join/)と、distinct の[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | 最初の入力の行のうち、他のどの入力にも現れないものを残します。 |
| Intersect | 完全 | すべての列に対する[テーブル: 内部結合](/ja/reference/workflow-steps/tables/table-inner-join/)と Distinct | すべての入力に存在する行を残します。 |
| Join | 完全 | [テーブル: 内部結合](/ja/reference/workflow-steps/tables/table-inner-join/)、[複数テーブル結合](/ja/reference/workflow-steps/tables/table-multi-table-join/)、[テーブル: アンチ結合](/ja/reference/workflow-steps/tables/table-anti-join/)、または[テーブル: クロス結合](/ja/reference/workflow-steps/tables/table-cross-join/) | inner、left、right、full、semi、anti、cross、natural の各タイプの結合を、任意の結合条件で構築し、where 句を適用して、select リストを書き出します。 |
| Union | 完全 | [テーブル: 和集合（すべて）](/ja/reference/workflow-steps/tables/table-union-all/) | 入力を位置で積み重ねます。gem が重複を残さない場合は、重複を削除します。 |
| Union By Name | 完全 | [テーブル: 和集合（すべて）](/ja/reference/workflow-steps/tables/table-union-all/) | 列を名前で揃え、不足している列を null で埋める和集合（すべて）になります。 |

### 解析

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| JSON Parse | 完全 | [JSON 解析](/ja/reference/workflow-steps/tables/table-json-parse/) | JSON テキスト列を構造化フィールドに解析します。 |
| Regex | 完全 | テーブル: 抽出 / 変換ステップ内の正規表現の式 | 正規表現でテキスト列を置換、解析、照合、またはトークン化します。 |
| Text To Columns | 完全 | 正規表現の区切り文字を使った列分割 / 展開ステップ | 区切り文字付きの列を、正規表現の区切り文字を使って列または行に分割します。 |
| XML Parse | 完全 | [XML解析](/ja/reference/workflow-steps/tables/table-xml-parse/) | XML テキスト列を構造化フィールドに解析します。 |

### カスタム

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Directory | 完全 | [ディレクトリ一覧](/ja/reference/workflow-steps/document/directory-listing/) | バインドされたドキュメントフォルダーのファイルを、gem の列で一覧表示します。シート名オプションを使うと、各ブックがシートごとに1行を返します。フォルダーが存在しない場合は0行になります。 |
| DynamicInput | 完全 | クエリテンプレートには SQL ステップ、複数ファイルモードにはワークフローループ | クエリテンプレートモードでは、テンプレートを SQL ステップとして埋め込みます。複数ファイルモードは、前提を置いてマッピングされます。 |
| Email | 完全 | [通知: メール](/ja/reference/workflow-steps/notifications/notify-via-email/) | バインドされたメール接続を通じて、必要に応じてデータの添付付きでメールを送信します。 |
| RestAPI | 完全 | [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | 入力行ごとに、URL、ヘッダー、クエリ、本文、再試行を指定して1つのリクエストを送信し、レスポンスを保持して、非同期リクエストは完了するまでポーリングします。認証情報は、バインドした接続から取得されます。 |
| Script | 完全 | フレームアクセスを書き換えた Python ステップ | スクリプト本体を Python ステップに埋め込み、データフレームへのアクセスを書き換えます。Scala の本体は注記付きで引き継がれます。 |
| SQL Statement | 完全 | 出力タブごとの SQL ステップ。テキストはテナントの方言に変換 | 各タブを、入力を一時テーブルとしてバインドした SQL ステップに埋め込みます。テナントの方言に変換されます。 |
| StoredProcedure | 完全 | [Agent Remote Execution of SQL](/ja/reference/workflow-steps/agent/agent-remote-execution-of-sql/)ステップ | 選択した接続を通じて、そのウェアハウス上でプロシージャを呼び出します。各引数を列からバインドして入力行ごとに1回、引数がない場合は1回だけ呼び出します。入力列はそのまま渡されます。 |
| Table Operations | 完全 | [テーブル: インプレース削除](/ja/reference/workflow-steps/tables/table-in-place-delete/)、[Table Update](/ja/reference/workflow-steps/tables/table-update/)、[Table Drop](/ja/reference/workflow-steps/tables/table-drop/)ステップ | 更新、削除、ドロップはテーブルステップにマッピングされます。vacuum と optimize は、テーブルの最適化になるか、警告付きで何も行いません。 |
| ToDo | 完全 | [ワークフローエラーの発生](/ja/reference/workflow-steps/workflow-control/raise-workflow-error/)または[Notify via Log](/ja/reference/workflow-steps/notifications/notify-via-log/)ステップ | まだ書かれていないロジックを示します。何も読み取らない場合はログメッセージ、後続のステップが依存している場合は、gem のメッセージ付きで実行を停止するステップになります。 |

### 空間

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Buffer | 完全 | [Spatial Buffer](/ja/reference/workflow-steps/spatial/spatial-buffer/)ステップ | 各ジオメトリを、設定された距離（マイルまたはキロメートル）だけ拡大します。 |
| CreatePoint | 完全 | `geom_point` を使った[テーブル: 抽出](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/) | 経度と緯度の列からポイントジオメトリを構築します。 |
| Distance | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | 2つの WKT ポイント間の距離、方角、方位角を計算します。 |
| FindNearest | 完全 | クロス結合を使った[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | 各ソースポイントについて、最大距離内にあるターゲットポイントのうち、近い順に N 個を検索します。 |
| HeatMap | 完全 | [Heat Map (macro)](/ja/reference/workflow-steps/macros/macro-heat-map/) | gem の解像度でポイントを H3 六角形にビン分けし、減衰を伴ってグリッド距離にわたって熱を広げ、各六角形の密度と輪郭を出力します。 |
| PolyBuild | 完全 | [テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/)と Python ステップ | グループごとに順序付けられたポイントから、ポリゴンまたはポリラインの WKT を構築します。 |
| Simplify | 完全 | [Spatial Generalize](/ja/reference/workflow-steps/spatial/spatial-generalize/)ステップ | 許容値（マイル/キロメートル）で WKT ジオメトリを単純化します。 |
| SpatialMatch | 完全 | [空間照合](/ja/reference/workflow-steps/spatial/spatial-match/) | intersects/contains/within/touches/envelope で、ソースとターゲットのジオメトリを照合します。 |

### レポート

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| PowerBIWrite | 完全 | [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | Power BI REST API を通じて、Power BI データセットを作成し、行をプッシュします。 |
| TableauWrite | 完全 | [Publish to Tableau](/ja/reference/workflow-steps/export/export-to-tableau/)ステップ | Hyper 抽出を書き出し、バインドされた Tableau 接続に公開します。 |
| Visualize | 完全 | [テーブルのコピー](/ja/reference/workflow-steps/tables/table-copy/) | 行をそのまま渡します。チャートは、同じテーブル上の PlaidCloud ダッシュボードとして構築してください。 |

### サブグラフ/制御

| Gem | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Condition | 完全 | [テーブル: クロス結合](/ja/reference/workflow-steps/tables/table-cross-join/)と[テーブル: 抽出](/ja/reference/workflow-steps/tables/table-extract/) | 入力全体に対して条件を評価し、条件が成立する最初の出力にすべての行を送ります。どれも成立しない場合は最後の出力に送ります。 |
| Macro | 完全 | マクロ本体を展開した SQL ステップ | マクロ本体を、テナントの方言に変換した SQL ステップとして埋め込みます。入力は一時テーブルとしてバインドされます。 |
| Pipeline (trigger) | 完全 | [Workflow Loop](/ja/reference/workflow-steps/workflow-control/workflow-loop/)ステップ | 入力行ごとに、パラメーターとトリガー条件を指定して、指定したパイプラインを1回実行します。実行が失敗しても続行し、実行ごとに1行を返します。 |
| Subgraph (Basic) | 完全 | インラインプロセスからのキャンバスコンテナ / ネストされたワークフロー | インラインの内部グラフを、入出力テーブルパラメーター付きのネストされたワークフロー（またはインライン化されたステップ）に変換します。 |

## コネクター

データセット形式とコネクターは gem ではなく、gem のソースとターゲットの設定です。各形式は、示されたインポートまたはエクスポートステップに変換され、変換がソースシステムやターゲットシステムに接続することはありません。

| 形式 | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Avro | 完全 | インポート: [Avro](/ja/reference/workflow-steps/import/import-avro/)、エクスポート: [Avro](/ja/reference/workflow-steps/export/export-to-avro/) | Avro ファイルを読み取り、書き込みます。 |
| BigQuery | 完全 | テーブルのインポートを伴う外部データベース接続 | 接続を通じて読み取り、書き込みます。 |
| Binary files | 完全 | ファイルの内容を取得する[ディレクトリ一覧](/ja/reference/workflow-steps/document/directory-listing/)。書き込みには[Alteryx実行](/ja/reference/workflow-steps/general/alteryx-executor/) | フォルダー内の各ファイルを、パス、更新時刻、長さ、内容とともに読み取ります。各行の内容を、そのパスが指すファイルに書き込みます。 |
| Catalog table | 完全 | 既存の PlaidCloud テーブルのバインディング | 名前でテーブルにバインドします。読み取りと、すべての書き込みモードが変換されます。 |
| Cosmos DB | 完全 | インポートとエクスポート: [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | Cosmos DB 接続を通じて、コンテナのドキュメントを読み取り、書き込みます。 |
| CSV | 完全 | [インポート: CSV](/ja/reference/workflow-steps/import/import-csv/)、エクスポート: CSV | ヘッダー、区切り文字、引用符、エスケープ、エンコーディングのオプションを指定して、区切りファイルを読み取り、書き込みます。 |
| Data Generator | 完全 | [Table Faker](/ja/reference/workflow-steps/tables/table-faker/)ステップ | 同じ種類のダミーデータで、データセットの列を生成します。 |
| DataHub table | 完全 | [SQLのインポート](/ja/reference/workflow-steps/import/import-sql/) | 接続を通じて、データセットが指定するテーブルを読み取ります。書き込みは PlaidCloud のテーブルに行われます。 |
| Delta | 完全 | 既存の PlaidCloud テーブルのバインディング | すべての書き込みモードでテーブルを読み取り、書き込みます。以前のバージョンの読み取りは、バインドした Databricks 接続を通じて行われます。 |
| Excel (XLSX) | 完全 | インポート: Excel、エクスポート: Excel | ブックのシートと範囲を読み取り、書き込みます。 |
| Fixed format | 完全 | インポート: [固定幅](/ja/reference/workflow-steps/import/import-fixed-width/)、エクスポート: [CSV](/ja/reference/workflow-steps/export/export-to-csv/) | データセットの列幅に基づいてレイアウトされた固定幅ファイルを読み取り、区切りファイルを書き込みます。 |
| Hive | 完全 | インポート: [SQLのインポート](/ja/reference/workflow-steps/import/import-sql/)、エクスポート: [外部テーブル](/ja/reference/workflow-steps/export/export-external-tables/) | Hive 接続を通じて、テーブルを読み取り、書き込みます。 |
| Iceberg | 完全 | 既存の PlaidCloud テーブルのバインディング | テーブルを読み取り、書き込みます。 |
| JDBC | 完全 | テーブルのインポートを伴う外部データベース接続 | 接続を通じて、テーブルまたはクエリを読み取り、置換または追加モードで書き込みます。書き込み後のステートメントは、書き込みの後に実行されます。 |
| JSON | 完全 | [JSON 解析](/ja/reference/workflow-steps/tables/table-json-parse/) | レコードを読み込み、ネストされたフィールドをフラット化します。 |
| Kafka | 完全 | インポート: [Kafkaのインポート](/ja/reference/workflow-steps/import/import-kafka/)、エクスポート: [Kafkaのエクスポート](/ja/reference/workflow-steps/export/export-kafka/) | トピックをメッセージの1バッチとして読み取り、行をメッセージとして書き込みます。 |
| MongoDB | 完全 | インポート: [MongoDB](/ja/reference/workflow-steps/import/import-mongodb/)、エクスポート: [MongoDB](/ja/reference/workflow-steps/export/export-mongodb/) | MongoDB 接続を通じて、コレクションを読み取り、書き込みます。 |
| ORC | 完全 | インポート: [ORC](/ja/reference/workflow-steps/import/import-orc/)、エクスポート: ORC | ORC ファイルを読み取り、書き込みます。 |
| Parquet | 完全 | インポート: Parquet、エクスポート: Parquet | Parquet ファイルを読み取り、書き込みます。 |
| Pinecone | 完全 | インポートとエクスポート: [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | Pinecone REST API を通じて、インデックスのレコードを読み取り、行をベクトルとしてアップサートします。 |
| Redshift | 完全 | テーブルのインポートを伴う外部データベース接続 | 接続を通じて読み取り、書き込みます。 |
| Salesforce | 完全 | インポート: [Salesforce: オブジェクトのクエリ](/ja/reference/workflow-steps/salesforce/query-salesforce-object/)、エクスポート: [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | Salesforce 接続を通じて、オブジェクトまたは SOQL クエリを読み取り、レコードを書き込みます。 |
| Seed (inline) | 完全 | [インポート: CSV](/ja/reference/workflow-steps/import/import-csv/) | インラインの行をテーブルとして読み込みます。 |
| Slack | 完全 | インポート: [Singer](/ja/reference/workflow-steps/import/import-singer/)、エクスポート: [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | Slack 接続を通じて、チャンネルのメッセージを読み取り、各行をメッセージとして投稿します。 |
| Smartsheet | 完全 | インポートとエクスポート: [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | Smartsheet 接続を通じて、シートの行を読み取り、書き込みます。 |
| Snowflake | 完全 | テーブルのインポートを伴う外部データベース接続 | 接続を通じて読み取り、書き込みます。 |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | 完全 | ドキュメントアカウントに対するファイルのインポートとエクスポートのステップ | ファイルタイプを読み取り、書き込みます。PlaidCloud に相当機能のないオプションにはフラグが付きます。 |
| Text | 完全 | 単一列としての[インポート: CSV](/ja/reference/workflow-steps/import/import-csv/) | 各行を1つの列として読み取ります。 |
| Web page | 完全 | [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | データセットの URL にあるページをテーブルに読み取ります。 |
| XML | 完全 | [XML解析](/ja/reference/workflow-steps/tables/table-xml-parse/) | 行タグでレコードを読み込みます。 |

## 式とプロジェクト構造

| 領域 | ステータス | PlaidCloud での相当機能 | 変換内容 |
| --- | --- | --- | --- |
| Expressions | 完全 | 関数ごとに変換される Spark とウェアハウスの SQL 式 | 関数と演算子は PlaidCloud の式に変換されます。相当機能のない関数には、名前付きでフラグが付きます。 |
| Project and graph structure | 完全 | プロジェクトローダー | Prophecy のあらゆるエクスポート形式が、1つのモデルに読み込まれて正規化されます。 |

## 既知のエッジケース

| ケース | 動作 |
| --- | --- |
| エクスポートに含まれないコードやデータ | コードがエクスポートに含まれていない Gem Builder などのカスタム gem や、エクスポートに含まれない dbt パッケージのマクロの呼び出しは、不足しているものを示すステップになります。プロジェクトをパイプラインコードと dbt パッケージとともにエクスポートするか、そのロジックを Python または SQL ステップで再構築してください。Ab Initio の Error Detection と MTime の gem は、適用するルールがエクスポートに含まれないため、入力をそのまま渡します。プロジェクト外のファイルから読み取る Soda チェックや、以前のスキャンまたは別のデータセットと比較する Soda チェック、Soda が指定する形式をテストする Soda チェックは、結果テーブルに行がありません。後続のステップで計算してください。 |
| パイプラインの実行時にのみ判明する結果 | レスポンスをフラット化する REST API gem は、フィールド名がどこにも宣言されていない場合、レスポンス全体を1つの列に格納します。これは実行して初めて判明するため、必要なフィールドは後続のステップで抽出してください。dbt がコンパイルする際にウェアハウスにクエリを実行する dbt マクロは、それを示すステップになります。クエリを、それが返す値に置き換えてください。Spark の StoredProcedure gem は実行されますが、OUT 値は返されません。出力は、そのまま渡される列です。`input_file_name()` は、ファイルを持たないテーブルまたは Delta ソースに対しては空の文字列を返します。集計、ウィンドウ、または複数の入力を持つ gem の内部での `hash()` / `xxhash64()` はウェアハウスが計算するため、Spark の結果と異なる場合があります。 |
| プロジェクトの変換時にステップに書き込まれる値 | 引用符、バックスラッシュ、または波括弧を含むパラメーター値、SQL ステップが読み取るパイプラインの値、設定を通じて Delta テーブル操作が指定するデータベースは、固定値としてステップに書き込まれます。そのため、ワークフロー変数を変更しても反映されません。設定が変わったときは、ステップを編集してください。 |
| Scala コード | Scala のスクリプト、Scala の式、Scala のユーザー定義関数または集計関数は、それを示すステップになります。SQL または Python で書き直してください。 |
| Kafka の Kerberos サインイン | Kerberos（GSSAPI）でサインインする Kafka のソースまたはターゲットは、Kerberos のサービス名とサインイン方式なしで変換されます。それらは PlaidCloud の接続で設定してください。 |
| ストリーミング | ストリーミングのソース、ターゲット、パイプラインは、実行時に存在するデータに対するバッチワークフローとして実行されます。必要な頻度で実行されるように、ワークフローをスケジュールしてください。 |
| ジョブのコンポーネント | Spark ジョブは、その1つのパイプラインとスケジュールが変換されます。その他のコンポーネント、実行条件、設定のオーバーライドは変換されません。 |
| まれな呼び出し | ロールアップまたはウィンドウから呼び出されるユーザー定義の集計関数や、if、for、set、一般的なフィルターを超える Jinja を使う dbt マクロは、その gem を示すステップになります。関数は Aggregate gem から呼び出すか、マクロをインライン化してください。 |

## 変換後のワークフローの検証

変換後のワークフローの出力を、元の Prophecy パイプラインの出力と比較してください。比較するのは、スキーマ、行数、行の値です。ワークフローが行の順序に依存していない限り、順序は無視してかまいません。
