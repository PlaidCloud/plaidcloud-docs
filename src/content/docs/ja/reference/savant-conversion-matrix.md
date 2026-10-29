---
title: Savant 変換マトリックス
description: PlaidCloud が Savant Labs の分析をネイティブの高度なワークフローに変換する方法を、各エージェントの対応ティアと、名前を挙げて示す少数のエッジケースとともに説明します。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud は、Savant Labs の分析をネイティブの高度なワークフローに変換します。
インポーターは、Savant の各エージェントをワークフローステップ、プロジェクト変数、またはキャンバスオブジェクトにマッピングするため、変換されたワークフローはクラウドネイティブで実行されます。

変換を実行するには、[Savant 分析の移行](/ja/guides/workflows/migrate-savant-analyses/)を参照してください。

各エージェントには対応ティアがあります。**完全**とは、エージェントのすべてのオプションが PlaidCloud ステップへの有効なマッピングを持つことを意味します。
名前を挙げて拒否される構成要素は、「名前付きの拒否」にまとめています。

外部システムのコネクターは**接続されるものであり、変換されません**。詳細は[外部システムへの接続](#外部システムへの接続)を参照してください。

## エージェントのサポート

33 個のエージェントすべてが完全で変換されます。

| エージェント | ティア | PlaidCloud での対応 | 変換内容 |
| --- | --- | --- | --- |
| Adapter Agent (`adapter`) | 完全 | 選択およびスキーマ射影ステップ | フィールドの名前変更、型変更、並べ替えを行います。 |
| API / Infer Agent (legacy service) (`service`) | 完全 | serviceType に応じて API Agent または Infer Agent と同じ | LLMService は Infer Agent として、APIService は API Agent として変換されます。serviceType がない、またはスペルが誤っている場合は、ノードのキーから読み取られ、警告が出ます。 |
| API Agent (`apiService`) | 完全 | Table Extract、[RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/)、および左結合による戻し | 入力行ごとに GET、POST、PUT、PATCH、DELETE のいずれかのリクエストを 1 つ送信します。生のレスポンス本文はテキスト列に格納され、HTTP エラーは行として残り、すべての入力行が保持されます。期間あたりのクォータは、小数のリクエスト毎秒になります。相対 URL は、api_bindings のベース URL または REST 接続のホストと結合されます。行のフィールドに由来するホスト、ポート、パスは行ごとに置換されます。次 URL、Link ヘッダー、オフセット、ページによるページングに対応し、行のフィールドからテンプレート化された開始位置、ページサイズ、パラメーター名も含まれます。 |
| Blend Agent (`blend`) | 完全 | [内部結合](/ja/reference/workflow-steps/tables/table-inner-join/)、[外部結合](/ja/reference/workflow-steps/tables/table-outer-join/)、[アンチ結合](/ja/reference/workflow-steps/tables/table-anti-join/) | 内部、左、右、完全、アンチ、内部を除く外部のブレンド、OR 結合、含む条件と一部である条件に対応し、一致するストリームと一致しないストリームを出力します。ピボットや解析が実行時にのみ名前を決める列は、そのまま引き継がれます。 |
| Dedupe Agent (`deduplicate`) | 完全 | 個別行を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | キーごとに最初のレコードを保持します（グループ化のグループ内）。重複は 2 つ目のストリームに振り分けるか、フラグを付けます。 |
| Destination Agent (`destination`) | 完全 | [エクスポート: CSV](/ja/reference/workflow-steps/export/export-to-csv/)、[エクスポート: Excel](/ja/reference/workflow-steps/export/export-to-excel/)、Export: Parquet、JSON、Avro、XML、[Export to PDF](/ja/reference/workflow-steps/export/export-to-pdf/)、[エクスポート: Tableau Hyper](/ja/reference/workflow-steps/export/export-hyper/) と [Publish to Tableau](/ja/reference/workflow-steps/export/export-to-tableau/)、[Export: External Database Tables](/ja/reference/workflow-steps/export/export-external-tables/)、[Export to Google Spreadsheet](/ja/reference/workflow-steps/export/export-to-google-spreadsheet/)、[Notify via Slack](/ja/reference/workflow-steps/notifications/notify-via-slack/)、またはメール | destination_bindings を通じて、ドキュメントアカウント（CSV、TSV、TXT、Excel、Parquet、JSON、Avro、XML、PDF、Tableau の .hyper。別名、CESU-8、バイトオーダーマーク形式を含む任意の Java 文字セットに対応し、文字セットにない文字は ? として書き込まれます）、接続テーブル、Google スプレッドシート、Tableau データソース、Slack チャンネル、またはメールの宛先に書き込みます。バインドされていない出力先は、代わりにプロジェクトテーブルまたはドキュメントファイルに書き込みます（下の「PlaidCloud での対応先」を参照）。フィールドの値ごとのファイル、サブフォルダー、タブにより、CSV、Excel、Parquet、PDF ファイルと Google スプレッドシートのタブが分割されます。テンプレートは、分割後のすべてのワークブックの元になります。Excel のオプションは次のように対応します。空白の値は `Sheet1` に入り、シート名が重複する場合は接尾辞が付き、`formatFromTemplate`、`topLeftCell`、モード `create` に対応します。追加、アップサート、更新、groupReplace は、一致キーでマージします（ファイルまたはテーブルは読み戻して書き直されます。分割では、実行中の各値の書き込み先ファイルを読み戻してその中でマージし、他のファイルはそのままにします。Tableau では行が適切な位置で更新されます）。データだけが名前を決める列（昇格されたヘッダーの列、ピボットの値、解析された JSON や XML のキー）は、すべてのエクスポートとテーブル書き込みで既知の列と並べて書き込まれ、並べ替えと分割の対象になり、テーブルに追加またはマージされます。ファイルの場合は、そのファイルがすべての列を持った状態で読み戻されます。 |
| Explode Agent (`explode`) | 完全 | [クロス結合](/ja/reference/workflow-steps/tables/table-cross-join/) | 小さい側をメインストリームとクロス結合します。 |
| Filter Agent (`filter`) | 完全 | フィルター式を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | ウィザードまたは式によってレコードを真と偽のパスに分割します。 |
| Filter Pushdown (`pdfilter`) | 完全 | フィルター式を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | データベース側のフィルターで、Filter と同じように変換されます。 |
| Format Agent (`format`) | 完全 | 列の名前変更を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/)、または Promote Header | 名前（含む、次で始まる、次で終わる）または空であることで一致したフィールドを、非表示、型変更、名前変更、入力します。入力では、デフォルト値をキャストできる型（テキスト、数値、日付）の任意の列にデフォルト値を書き込みます。ヘッダー行の昇格と空であることの一致は、Promote Header ステップで実行時に行われ、昇格されたヘッダーはファイルのすべての列を読み取ります。 |
| Fuse Agent (`fuzzy_match`) | 完全 | Union All と 2 つの結合の間にある[Fuzzy Match](/ja/reference/workflow-steps/tables/table-fuzzy-match/) | 両方の入力を積み重ね、類似度しきい値 80 でキーフィールドのレコードを照合し、信頼度スコアを付けて両側を結合し直します。 |
| Group (`group`) | 完全 | キャンバスコンテナー | ワークフローの整理用として保持されます。 |
| Infer Agent (`gen_ai`) | 完全 | [AI/NLP](/ja/reference/workflow-steps/text-documents/nlp-ai/) プロンプトタスク | プロンプトは、Savant のプロバイダーとモデルに一致する表示可能な LLM 接続で、入力フィールドに対して行ごとに実行されます。回答は、すべての入力列の横にある AI Answer 列に格納されます。rowLimit は、1 回の実行で回答する行数の上限を設定し、以前の回答を保持します。以前に回答済みの行（同じプロンプト、モデル、入力値）は回答が保持され、未回答の行のみが上限にカウントされます。 |
| JSON Agent (`json`) | 完全 | [JSON 解析](/ja/reference/workflow-steps/tables/table-json-parse/) | JSONフィールドをドット区切りキーの列にフラット化するか、配列を要素ごとに 1 行へ展開します。キーは実行時にデータから読み取られます。 |
| Notes Agent (`notes`) | 完全 | キャンバス注釈 | ワークフローのコンテキストとして保持されます。 |
| Pivot Agent (`pivot`) | 完全 | [Pivot](/ja/reference/workflow-steps/tables/table-pivot/) | 集計しながら行を列にピボットします。 |
| Recursion Agent (`hierarchy`) | 完全 | Hierarchy Closure、[Table Extract](/ja/reference/workflow-steps/tables/table-extract/)、[複数テーブル結合](/ja/reference/workflow-steps/tables/table-multi-table-join/) | 親子ツリーを任意の深さまでたどり、ルートまでのパス上の ID（自身を含む）ごとに各ノードを集計して、Depth と Path を書き込みます。ループは、繰り返されたノードで停止します。 |
| Sample Agent (`sample`) | 完全 | 行数の上限を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | 先頭の N 行を保持します。グループごと、ランダムなパーセンテージまたは N 行、あるいは N 行ごとに 1 行を保持することもできます。 |
| Search and Replace (`search_replace`) | 完全 | ステージに分けて入れ子の置換式を使用する[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | 検索/置換ルール（含む、または一致する。置換または追加）を、大文字と小文字の区別、単語全体かどうかを指定して、選択したテキストフィールド（指定がない場合はすべてのテキストフィールド）に順番に適用します。 |
| Source Agent (`source`) | 完全 | `source_bindings` でバインドされたインポートステップ（[インポート: CSV](/ja/reference/workflow-steps/import/import-csv/)、[インポート: Excel](/ja/reference/workflow-steps/import/import-excel/)、[インポート: SQL](/ja/reference/workflow-steps/import/import-sql/)）、または既存のテーブル | バインドされたテーブルまたはドキュメントを読み取ります。バインドされていないソースは、空のインポートを作成し、警告を出します。XML テキストは、XMLのインポートを通じてドキュメントを読み取ります（バインドされていない場合は savant/<workflow>/<name>.xml を読み取ります）。XML ドキュメントにバインドされたソースは、エクスポートのその他の列も書き込みます。ドキュメントからのファイル名またはパスの列を書き込み、残りは空白になります。ヘッダー行を昇格する Format の下にあるソースは、CSV、Excel（Excel 97 の .xls を含む）、JSON、Parquet、Avro ファイルのすべての列を位置で読み取ります。 |
| Spatial Match Agent (`spatial_match`) | 完全 | [空間照合 (executor)](/ja/reference/workflow-steps/spatial/spatial-match-executor/)、[クロス結合](/ja/reference/workflow-steps/tables/table-cross-join/)、または[最近傍検索](/ja/reference/workflow-steps/spatial/spatial-find-nearest/) | 交差、内包される、含む、接する、横切る、重なる、等しい、離れている、および and/or の複数ルールによる照合に対応します。任意のジオメトリ間（点、線、ポリゴン：半径 6371 km の球面上の最短距離）の測地線距離による範囲内の判定、最大距離を指定した同じ距離による上位 N 件の最近傍（最近傍ルールが 1 つだけの場合は、Savant と同様に Distance 列を書き込みません。他のルールと組み合わせる場合は、最近傍の後にフィルターを適用し、AND 結合と OR 和集合では、最近傍ルールごとに独自の Distance 列を追加します）、および Cross に対応し、一致するストリームと一致しないストリームを出力します。 |
| Spatial Summarize Agent (`spatial_summarize`) | 完全 | [空間結合](/ja/reference/workflow-steps/spatial/spatial-combine/)、Spatial Centroid、および点から線へのステップ | 和集合、交差、バウンディングボックス、1 つまたは複数のジオメトリ中心、ポリラインまたはポリゴンの構築に対応し、グループごとに処理され、並べ替えも任意で指定できます。 |
| Split Agent (`split`) | 完全 | Split Text、または split_part 列を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | 任意の長さのリテラル区切り文字でテキストフィールドを行または列に分割し、トリムと元の値の保持に対応します。列数は実行時にデータから読み取られます。 |
| 出力を分割 (`outlet`) | 完全 | ワークフローのエッジ | 名前付きの出力を、その利用先にルーティングします。 |
| Stack Agent (`multi_stack`) | 完全 | [Union All](/ja/reference/workflow-steps/tables/table-union-all/) | 任意の数の入力を、名前または位置で積み重ねます。 |
| Summarize Agent (`summarize`) | 完全 | 集計を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | グループ化と集計を行います。決定的な並べ替えによる先頭/末尾の値や、行ごとのウィンドウ集計（useWindow）も含まれます。 |
| Summarize Pushdown (`pdsummarize`) | 完全 | 集計を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | データベース側の集計で、Summarize と同じように変換されます。 |
| Text (`text`) | 完全 | キャンバス注釈 | ワークフローのコンテキストとして保持されます。 |
| Time Series Agent (`rollup`) | 完全 | 期間バケット式に対する集計を行う[Table Extract](/ja/reference/workflow-steps/tables/table-extract/)、Period Spine、[アンチ結合](/ja/reference/workflow-steps/tables/table-anti-join/)、[Union All](/ja/reference/workflow-steps/tables/table-union-all/) | 任意の開始日と終了日の間で、グループごとに、レコードを日、週、月、四半期、年、10 年の期間に集約します。NULL の日付は除外し、空の期間はゼロで埋めます。 |
| Transform Agent (`edit`) | 完全 | 列の式を指定した[Table Extract](/ja/reference/workflow-steps/tables/table-extract/) | 計算列、型変更、ウィンドウ計算（lag、lead、累積合計、行番号、前方および後方の補完）を順番に評価します。コンパイル済みのステップのみを持つ編集は、それらのステップを順番に適用し、それぞれが次に渡すものとして変換されます。 |
| Unpivot Agent (`unpivot`) | 完全 | [Melt](/ja/reference/workflow-steps/tables/table-melt/) | 列を名前と値のペアとして行に変換します。 |
| Vision Agent (`vision`) | 完全 | [Image OCR](/ja/reference/workflow-steps/text-documents/image-ocr/)、続いて [AI/NLP](/ja/reference/workflow-steps/text-documents/nlp-ai/) プロンプトタスク | 各ドキュメントは、プロバイダーがその種類とサイズを受け付ける場合は画像または PDF として送信され、受け付けない場合は PDF のテキストレイヤーまたは OCR テキストが送信されます。プロンプトの回答は AI Answer 列に格納されます。 |
| XML Agent (`xml`) | 完全 | [XML解析](/ja/reference/workflow-steps/tables/table-xml-parse/) | 要素を選択し、子の値と属性を列に抽出するか、XML を JSON に変換します。単純な //a/b パスは従来どおり変換され、それ以外の XPath 1.0 パス（述語、属性テスト、ワイルドカード、count()、name()、contains() などの関数）は、名前空間を考慮して、または記述されたとおりに XPath として評価されます。 |

配線、キャンバス、プッシュダウンの各バリアント（出力を分割、Group、Text、Filter Pushdown、Summarize Pushdown）は、ヘルプセンターに独自のエージェント記事がない Savant のノードタイプです。それぞれ、対応するエージェントとして変換されます。

API Agent のリクエスト内の認証情報は、ワークフローステップにコピーされません。https の場合は REST 接続に移され、http の場合、接続を書き込む権限がない場合、または MCP 経由で行った変換の場合は、警告とともに保留されます。これは仕様であり、ティアは下がりません。

出力先に関する 2 つの制限は、ティアを下げません。まれな文字セット（たとえば `x-ISCII91` や `JIS_X0212`）は書き込めないため、ファイルは UTF-8 で書き込まれ、変換時に警告が出ます。キーでマージする Tableau の公開には、その出力先バインディングで `replace: true` が必要です。指定しない場合、変換は警告を出して新しいデータソースを公開しますが、すでに存在する場合の実行では失敗します。

## 名前付きの拒否

8 つの構成要素は、変換されずに名前を挙げて拒否されます。エージェントのティアが下がるものはありません。

| 構成要素 | 拒否される理由 |
| --- | --- |
| 認証情報を持ち、ホストを入力フィールドから取得する API Agent のリクエスト | 各行が、データによって決まるホストに認証情報を送信する可能性があります。リクエストは名前付きのプレースホルダーになります。認証情報のないリクエストや、固定ホストへの認証情報は変換されます。 |
| 式もコンパイル済みのステップもない Transform の編集（プロンプトのみを持つ Copilot の編集など） | 変換するものがありません。プロンプトは数式ではありません。コンパイル済みのステップを持つ編集は変換されます。 |
| Transform または Filter の式内にある、PlaidCloud が読み取れない正規表現の構成要素。クラス内のクラス、クラスの積集合 (`&&`)、不明な `\p{}` プロパティ | ステップは名前付きのプレースホルダーになり、実行時に拒否します。 |
| Transform または Filter の式内の集計関数またはウィンドウ関数 | Savant 自体が実行時に失敗します。Transform の計算または Summarize 内では変換されます。 |
| `md5` または `sha1` 以外のリテラルアルゴリズムを指定した Transform または Filter の式内の `HASH` | Savant 自体が失敗します（アルゴリズムは `md5` または `sha1` です）。列から読み取ったアルゴリズムは変換され、それ以外の値には NULL が返されます。 |
| 入力にない列での出力先の並べ替え | Savant 自体が実行時に失敗します。 |
| 入力にない列の値ごとの出力先のファイル、サブフォルダー、タブ、ワークシート | Savant 自体が実行時に失敗します。 |
| XPath 1.0 ではない XML Agent のパス | Savant でも実行できません。 |

相対 API URL は、`api_bindings` でベース URL または REST 接続をバインドすると変換されます。[変換時のバインディング](/ja/guides/workflows/migrate-savant-analyses/#変換時のバインド)を参照してください。

## 式言語

Savant の式の関数と演算子は、PlaidCloud の式に変換されます。ティア: **完全**。すべての関数と形式が変換されます。これには、数値パターンを指定した `TO_TEXT`、行ごとにのみ判明する形式、小数秒、週ベース、四半期、タイムゾーンの日付トークン、2 桁の年、Java 正規表現の構成要素が含まれます。式内の任意の場所にある GEO_* 関数は、付随する Spatial ステップで実行されます。例外は[名前付きの拒否](#名前付きの拒否)です。

既知のエッジケース: `[`、`]`、引用符、バックスラッシュ、`^` のリテラルを含む形式の `TO_DATE` または `TO_DATETIME` で、9999-12-30 または 9999-12-31 に読み込まれるテキストの場合。これはウェアハウスが保持する最後のタイムスタンプを超えており、変換時に警告が出ます。

## エクスポート形式

ローダーは、Savant のあらゆるエクスポート形式（フラット、モデルでラップされたもの、サーバーレコード、レシピエンベロープ、配列でラップされたもの、BOM 付き、従来の型エイリアス）を受け付け、1 つのモデルに正規化します。ティア: **完全**。

## 分析パラメーター

Savant の分析パラメーターはワークフロー変数に変換され、ノード設定内のそれらへの参照は PlaidCloud の変数構文に書き換えられます。リスト、辞書、エイリアス付きのパラメーター形式がすべて読み込まれます。ティア: **完全**。

既知のエッジケース: 名前に秘密を示す語を含む、または値が認証情報のように見えるパラメーターは、空白の値を持つ変数になり、警告が出ます。ノードが使用していてもエクスポートで宣言されていないパラメーターは、空の値を持つ変数になり、警告が出ます。

## 外部システムへの接続

Savant のコネクターはステップではなく、ソースと出力先のターゲットであり、エクスポートにはデータセットも認証情報も含まれません。PlaidCloud は、キャンバス上のノードではなく、接続を通じてこれらのシステムに接続します。

| Savant | PlaidCloud での対応先 |
| --- | --- |
| ソースコネクター | `source_bindings` が、Savant のノードまたはデータセットを PlaidCloud のテーブルまたはドキュメントファイルにマッピングし、対応するインポートステップで読み取ります。バインドされていないソースは警告を出し、何も処理しません |
| 出力先: CSV、Excel、その他のファイル形式 | エクスポートステップ（[エクスポート: CSV](/ja/reference/workflow-steps/export/export-to-csv/)、[エクスポート: Excel](/ja/reference/workflow-steps/export/export-to-excel/)、[Export to PDF](/ja/reference/workflow-steps/export/export-to-pdf/)） |
| 出力先: Google スプレッドシート、Tableau、Slack | `destination_bindings` でバインドした接続を通じて、[Export to Google Spreadsheet](/ja/reference/workflow-steps/export/export-to-google-spreadsheet/)、[Publish to Tableau](/ja/reference/workflow-steps/export/export-to-tableau/)、または [Notify via Slack](/ja/reference/workflow-steps/notifications/notify-via-slack/) |
| 出力先: バインドされていないデータベース、ウェアハウス、SaaS ターゲット（Oracle、汎用データベース、Looker Studio、NetSuite、SAP、および接続がバインドされていない Google スプレッドシート、Tableau、Slack） | 出力先ノードにちなんだ名前のプロジェクトテーブル。元のターゲットを示す警告が出ます |
| 出力先: バインドされていないファイルシステムのターゲット（S3、GCS、Box、SFTP、SharePoint、Google ドライブ、OneDrive） | 出力先のファイルタイプのファイルを、ターゲットフォルダーを反映したドキュメントフォルダーに保存し、警告が出ます。認証情報と共有トークンは、フォルダーパスから除外されます |
| 出力先: バインドされていないメール | CSV と警告 |
| 出力先: 使用できないバインディング | CSV と、元のターゲットを示す警告 |

変換時に、ソースシステムまたは出力先システムに接続することはありません。
