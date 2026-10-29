---
title: Alteryx変換マトリックス
description: PlaidCloudがAlteryxのツールを、ネイティブの高度なワークフローのステップ、マクロ、変数、マネージドエグゼキューターにどのように変換するかを、ツールごとの対応状況とともに説明します。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloudは、Alteryxのワークフロー、アプリ、マクロをネイティブの高度なワークフローに変換します。
インポーターは、各Alteryxツールを、ワークフローのステップ、マクロの構成要素、制御された変数、
ドキュメントを使ったファイル操作、またはマネージドジョブエグゼキューターにマッピングします。
そのため、変換後のワークフローはエミュレーションではなく、クラウドネイティブに実行されます。

**標準的なAlteryxツールのほぼすべてが完全に変換されます。** 以下の対応状況はツールごとのものです。

- **完全**：ネイティブのPlaidCloudのステップ、マクロ、変数、アーティファクト、または
  マネージドエグゼキューターに変換され、ツールの機能を実行します。ほとんどのツールがこれに該当します。
- **部分対応**：一般的な用途では変換して実行できますが、ツールの特定の
  *機能モード* が、まだ再現されていません。まれなケースです。
- **未対応**：変換されません。その機能は、代わりにネイティブに構築し直します。

外部システムのコネクター（Salesforce、HTTP、Google Analytics、Cassandra、
メール、Hadoop、Sparkなど）は、**変換ではなく接続**されます。
[外部システムへの接続](#外部システムへの接続)をご覧ください。

## ツールの対応状況

| Alteryxツール | ステータス | PlaidCloudでの対応 | 変換内容 |
| --- | --- | --- | --- |
| Action | 完全 | 変数バインディングと条件付きステップ設定 | 変換されたアプリの入力から、下流のステップの設定を更新します。 |
| Analytic App interface (`.yxwz`) | 部分対応 | 公開されたPanelの「App Runner」フロントエンド | アプリの `<Questions>` レイアウトが、ユーザーの入力を収集して変換後のワークフローを動かす、動作するPanelアプリとして具体化され、変換の一環として自動的に公開されます（入力ウィジェットのないアプリはスキップされます）。一般的な質問タイプ（テキスト、数値（Numeric Up Down）、日付、チェックボックス、ラジオボタン、ドロップダウン、リストボックス、ツリー、ファイル参照、フォルダー参照）は、App Runnerのウィジェットになります。値がどのワークフロー変数にもバインドされない質問は、使われない値を黙って収集するのではなく、目に見える注記付きで表示されます。あまり一般的でない質問タイプは、具体化されずにレビュー対象としてフラグが付けられます。[変換されたAlteryxアプリを使用する](/ja/guides/workflows/use-converted-alteryx-apps/#app-runnerフロントエンド)をご覧ください。 |
| Append Fields | 完全 | フィールド追加変換 | あるストリームのフィールドを別のストリームに追加します。 |
| Auto Field | 完全 | フィールドサイズ自動設定変換 | 推定されたフィールドサイズを保持します。 |
| AutoML | 完全 | [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/) | モデル方式、ターゲット、候補アルゴリズムの選択を、ClassificationやRegressionと同様に、ML Trainステップに統合します。AutoMLは、Alteryxの実行時にどの候補アルゴリズムが選ばれたかを記録しないため、変換ではML Trainがサポートする最初のチェック済みアルゴリズムを選び、その選択を注記します。変換後のAutoMLステップは、ご自身のAlteryxの結果と比較してください。 |
| Barcode | 完全 | バーコードエグゼキューター | 設定されたシンボル体系でバーコードを読み取りまたは書き込みます。 |
| Batch Macro | 部分対応 | コントロールアンカーテーブルに沿って展開されるマクロ | 呼び出し元は、コントロール入力のレコードごとにマクロ全体を1回ずつ実行し、パスごとに内部のコントロールパラメーターをバインドします。これには、1つだけが使われている場合に呼び出し元が表示ラベルに名前を変更したコントロールパラメーターや、変数からSelectのフィールドリストを書き換える `UpdateRawXml` Actionも含まれます。パスごとの値を安全に再現できない形は、誤って変換されるのではなく、名前を示して安全側に失敗します。具体的には、Selectのフィールドリスト以外を書き換える `UpdateRawXml` と、Filterの式全体を変数で置き換えるAction（その未加工のパスごとの構文は誤って評価されます）です。 |
| Browse | 完全 | Browse / パススルー | 実行時のコストなしで、確認用に保持されます。 |
| Buffer | 完全 | [Spatial Buffer](/ja/reference/workflow-steps/spatial/spatial-buffer/)ステップ | 各ジオメトリを一定の距離だけ拡大します。 |
| Build Features | 部分対応 | [Build Features](/ja/reference/workflow-steps/tables/table-build-features/)ステップ | 算術と交互作用のプリミティブ、日付部分の抽出、明示的なしきい値によるビニング、zスコアとmin-maxのスケーリング、ワンホットエンコーディングを変換します。テーブル間の集計（Manage Relationshipsタブをまたぐ Deep Feature Synthesis）、PCA、ターゲットエンコーディング、データ駆動の自動ビニングには同等の機能がなく、黙って削除されるのではなく、いずれも変換レポートに名前を示してフラグが付けられます。 |
| Calgary Cross Count | 完全 | [Calgaryデータベース](/ja/guides/workflows/migrate-alteryx-workflows/#calgaryデータベース)の集計 | インデックス付きフィールドをグループ化し、各カスタムフィールドの名前付きの値の数を数えます。 |
| Calgary Cross Count Append | 完全 | [Calgary Cross Count Append](/ja/guides/workflows/migrate-alteryx-workflows/#calgary-joinとcross-count-append) | 各入力レコードを値インデックスと照合し、一致したデータベースレコードの数を数えます。 |
| Calgary Input | 完全 | [Calgaryデータベース](/ja/guides/workflows/migrate-alteryx-workflows/#calgaryデータベース)の入力 | 保存されたクエリをフィルターとして適用して、データベースを読み取ります。 |
| Calgary Join | 完全 | [Calgary Join](/ja/guides/workflows/migrate-alteryx-workflows/#calgary-joinとcross-count-append) | 各レコードをデータベース上の値インデックスと照合し、一致したレコードを保持します。 |
| Calgary Loader | 完全 | [Calgaryデータベース](/ja/guides/workflows/migrate-alteryx-workflows/#calgaryデータベース)のライター | すべてのCalgaryリーダーがバインドする代替テーブルを書き込みます。 |
| Centroid | 完全 | Centroidエグゼキューター操作 | 各ジオメトリを中心点に縮約し、`Centroid` 列として追加します。 |
| Check Box | 完全 | 制御されたワークフロー変数 | アプリのチェックボックスの選択を、制御された入力に変換します。 |
| Classification | 完全 | [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/) | Assisted Modelingのチェーンを、アルゴリズム、ターゲット、特徴量、ハイパーパラメーターを持つ1つのML Trainステップに統合します。 |
| Comment / Annotation / Link | 完全 | キャンバスの注釈 | ワークフローのコンテキストとして保持されます。 |
| Condition | 完全 | ステップ条件 | 式から、警告、エラー、分岐を発生させます。 |
| Control Parameter | 完全 | マクロのコントロールパラメーター | PlaidCloudのマクロパラメーターにマッピングされます。 |
| Convex Hull | 完全 | Convex Hullエグゼキューター操作 | 各ジオメトリを囲む最小の凸多角形を作成し、`ConvexHull` 列として追加します。 |
| Create Points | 完全 | `geom_point` を使用する[Table Extract](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/)ステップ | 経度/緯度の列から、SQLでポイントジオメトリを作成します。 |
| Create Samples | 完全 | 出力ごとに1つのTable Extractステップ | 入力を、設定された割合でEstimation、Validation、Holdoutに分割します。 |
| Cross Tab | 完全 | ピボット / クロス集計変換 | すべての集計方法と派生した合計にわたって、行を列にピボットします。 |
| Data Cleansing | 完全 | データクレンジング変換 | 空白、null、句読点、大文字小文字を整えます。 |
| Date | 完全 | ワークフロー変数（日付） | ステップと条件向けに、ISO形式の日付値を出力します。 |
| DateTime | 完全 | 日付/時刻変換 | 日付と時刻の解析と書式設定を変換します。 |
| Detour | 完全 | 条件付き分岐ルーティング | ルート選択をDAGの条件に変換します。 |
| Detour End | 完全 | 条件付き分岐のマージ | 条件によって選択された分岐を再結合します。 |
| Directory | 完全 | ドキュメントのディレクトリ一覧 | ドキュメントのパスからファイルを一覧表示します。 |
| Distance | 完全 | `ST_DISTANCE_SPHERE` を使用する[Table Extract](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/)ステップ | 点から点までの測地線距離と方位を、SQLで求めます。 |
| Download | 完全 | RESTの接続に対する[RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) | 外部のデータまたはアーティファクトをダウンロードします。実行前に、変換されたステップにREST接続を割り当ててください。 |
| Drop Down | 完全 | 制御されたワークフロー変数 | アプリのドロップダウンの選択を、制御された入力に変換します。 |
| Dynamic Input | 部分対応 | 動的なドキュメント入力 | ファイルパターンと変数駆動の入力を、実行時に解決します。Excelの *ReadList*（Directoryツールが一覧表示するすべてのブックから1つのワークシートを読み取り、結合するもの）は、上流のFilterが完全一致でシートを1つの名前に固定している場合に、フォルダーglobによるシート読み取りに変換されます。Contains、不等号、OR条件のFilterで選ばれるシートや、複数のシートにまたがる読み取りは、誤ったシートを読み取るのではなく、変換を拒否します。 |
| Dynamic Rename | 完全 | 動的な名前変更変換 | メタデータまたはルールに基づいてフィールド名を変更します。 |
| Dynamic Replace | 完全 | 動的な置換変換 | 2つ目のストリームの置換ルールを適用します。 |
| Dynamic Select | 完全 | 動的なフィールド選択変換 | 型、名前、またはルールでフィールドを選択します。 |
| Error | 完全 | ステップ条件（エラー） | 設定されたエラー動作を、ステップ条件に変換します。 |
| Feature Types | 完全 | [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/)の特徴量設定 | 各フィールドに割り当てられたモデル上の役割を、統合されたML Trainステップに引き継ぎます。 |
| File Browse | 完全 | 制御されたドキュメントファイル変数 | 変換されたアプリの実行で、ユーザーがファイルを選択できるようにします。 |
| Filter | 完全 | フィルター変換 | 式に基づいて、レコードを真と偽のパスに分割します。 |
| Fit | 完全 | [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/) | 統合されたML Trainステップにまとめられます。 |
| Folder Browse | 完全 | 制御されたドキュメントフォルダー変数 | 変換されたアプリの実行で、ユーザーがフォルダーを選択できるようにします。 |
| Formatted Excel output into a styled template | 部分対応 | テンプレート対応のExcelライター（複数シートの場合は[Export to Excel Sheets](/ja/reference/workflow-steps/export/export-to-excel-sheets/)ステップ） | スタイル付きテンプレートに書き込むと、テンプレートの書式が保持されます。値、数値書式、フォント、塗りつぶし、罫線、結合セル、列幅が、指定したシートと範囲に引き継がれます。これは、単一のシートにも、1つのブックの異なるシートに組み立てられる複数の出力にも該当し、後者は1回のパスで入力されるため、シート同士が上書きされることはなくなりました。1つのケースだけは部分対応のままです。ピボットテーブルやグラフを含むテンプレートでは、シートの書き込み時にそれらのオブジェクトが削除されます。スタイルなしの通常のExcel出力は完全に対応しています。Output Dataをご覧ください。 |
| Formula | 完全 | 計算式変換 | フィールドの式を、PlaidCloudの式またはSQLに変換します。 |
| Fuzzy Match | 完全 | あいまい一致エグゼキューター | キー、しきい値、候補のレビューに基づいて照合します。 |
| Generalize | 完全 | [Spatial Generalize](/ja/reference/workflow-steps/spatial/spatial-generalize/)ステップ | トポロジーを保持しながら、許容誤差に合わせてジオメトリを単純化します。 |
| HTML | 完全 | レポートテキスト / HTMLアーティファクト | コンテンツを、レポートまたはアーティファクトの出力として保持します。 |
| Image Processing | 完全 | 画像変換エグゼキューター | グレースケール、拡大縮小、切り抜き、回転を、キャンバスの順序で適用します。 |
| Image Profile | 完全 | 画像プロファイルエグゼキューター | 寸法、モード、形式、チャンネル、輝度の統計を報告します。 |
| Image to Text | 完全 | OCRエグゼキューター | マネージドOCRを通じて、画像からテキストを抽出します。 |
| Input Data | 完全 | ドキュメントを使ったファイル入力 | `.yxdb`、`.dbf`、Excel、固定幅の `.flat` ソースファイルを、ワークフローのデータに読み込みます。 |
| Insights | 完全 | ダッシュボード / アーティファクトの出力 | クラウドネイティブなレビュー用アーティファクトを作成します。 |
| Interactive Chart | 完全 | グラフアーティファクト | 変換されたデータからグラフのアーティファクトを作成します。 |
| Join | 完全 | 結合変換 | 単一または複数フィールドのキー、または位置による結合で、結合結果、左のみ、右のみのストリームを生成します。 |
| Join Multiple | 完全 | 複数結合変換 | 複数の入力ストリームを結合します。 |
| Key/Value Pairs | 完全 | [Text: NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ（keyvalueタスク） | LLMを使ったNLP AIステップを通じて、テキスト列からキーと値のペアを抽出します。候補キーの指定と、あいまい一致または完全一致の選択もできます。 |
| Line To Polygon | 完全 | Line To Polygonエグゼキューター操作 | 各ラインを閉じてポリゴンのリングにし、`Polygon` 列として追加します。 |
| List Box | 完全 | 制御されたワークフロー変数 | アプリのリストの選択を、制御された入力に変換します。 |
| Location Optimizer | 部分対応 | [ロケーションオプティマイザー](/ja/reference/workflow-steps/optimization/location-optimizer/) | 線形の距離最小化のケース（K個の拠点を選んで、需要までの合計距離または加重距離を最小化する）を、ネイティブのp-median MIPステップに変換します。重力カーネルのスコア、独自のスコアリングマクロ、その他の候補探索の目的関数は、引き続き変換を拒否します。[Alteryxワークフローの移行](/ja/guides/workflows/migrate-alteryx-workflows/#変換後のワークフローのマクロ)をご覧ください。 |
| Macro calls | 完全 | マクロの呼び出し | 既知のマクロソースをインポートし、マクロの呼び出しをPlaidCloudのマクロステップにマッピングします。 |
| Macro Input / Macro Output | 完全 | マクロの入力 / 出力ポート | PlaidCloudのマクロポートに直接マッピングされます。 |
| Make Grid | 完全 | [Spatial Make Grid](/ja/reference/workflow-steps/spatial/spatial-make-grid/)ステップ | 範囲を正方形のセルに分割し、セルごとに1行を生成します。 |
| Map | 完全 | マップアーティファクト | PlaidCloudのマップアーティファクトを作成します。 |
| Map Input | 完全 | [空間ファイルのインポート](/ja/reference/workflow-steps/spatial/spatial-file-import/) | MapInfo、ESRI、KML、GeoJSONのファイルを、付随ファイルとともに読み取ります。 |
| Master Selector | 部分対応 | 制御されたワークフロー変数と条件付きステップ表示 | インターフェイス要素に対するツールの表示/非表示の条件を、条件付きステップ表示に変換します。選択によって実行されるサブワークフローは、ベストエフォートで変換されます。実際のテナント上のアプリでの検証はまだ行われていないため、本番で使用する前に、選択された実行対象を確認してください。 |
| Message | 完全 | ステップ条件（メッセージ） | 条件から、ワークフローの警告、メッセージ、エラーを出力します。 |
| Modeling | 完全 | [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/) | パイプラインのモデル選択とともに、ML Trainステップに統合されます。 |
| Multi-Field Formula | 完全 | 複数フィールド計算式変換 | 選択したフィールド全体に計算式を適用します。 |
| Multi-Row Formula | 完全 | ウィンドウ / 行認識の計算式変換 | 行相対のロジックを、グループ化で分割されたウィンドウの動作に変換します。 |
| Named Entity Recognition (NER) | 完全 | [Text: NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ（nerタスク） | LLMを使ったNLP AIステップを通じて、テキスト列からエンティティ（人物、組織、場所、日付、数量、またはカスタムの種類のリスト）を抽出します。 |
| Numeric Up Down | 完全 | 制御された数値変数 | アプリの数値入力を、型付きの変数に変換します。 |
| Output Data | 完全 | ドキュメント / テーブルの出力 | ParquetやAvroのファイルを含め、ドキュメントまたはPlaidCloudのテーブルに出力を書き込みます。`.yxdb`、`.hyper`、`.dbf` の出力はParquetとして書き込まれます。 |
| Overlay | 完全 | [空間処理](/ja/reference/workflow-steps/spatial/spatial-process/) | 2つのジオメトリ列の交差、結合、切り取りを行います。 |
| PDF Input | 完全 | PDF抽出エグゼキューター | PDFからテキストまたはテーブルを抽出します。 |
| Point To Line | 完全 | Point To Lineエグゼキューター操作 | 各グループのポイントを、シーケンスフィールドの順に並べて、グループごとに1つの `SequenceLine` にまとめます。 |
| Poly-Build | 完全 | [Spatial Poly-Build](/ja/reference/workflow-steps/spatial/spatial-poly-build/)ステップ | ポイントのグループごとに、ポリゴンまたは凸包を作成します。 |
| Poly-Split | 完全 | [Spatial Poly-Split](/ja/reference/workflow-steps/spatial/spatial-poly-split/)ステップ | 頂点、構成ポリゴン、または穴ごとに1行を生成します。 |
| Portfolio Composer (Text / Table / Image / Layout / Render) | 完全 | レポートアーティファクト | レポートのコンテンツ、レイアウト、レンダリングを、PlaidCloudのレポート出力に変換します。 |
| POS Tagger | 完全 | [Text: NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ（posタスク） | LLMを使ったNLP AIステップを通じて、テキスト列の各トークンに品詞のタグを付けます。 |
| Predict | 完全 | [ML: スコアリング](/ja/reference/workflow-steps/machine-learning/ml-score/) | 学習済みモデルのテーブルでデータをスコアリングし、予測列を追加します。 |
| Radio Button | 完全 | 制御されたワークフロー変数 | アプリのラジオボタンの選択を、制御された入力に変換します。 |
| Random % Sample | 完全 | Table Extractステップ（ランダム） | 要求された正確な件数または割合のレコードを返します。 |
| Record ID | 完全 | 行識別子変換 | 設定された型と開始値で、決定的なレコード識別子を追加し、グループごとにやり直します。 |
| Redistribute | 完全 | Redistributeエグゼキューター操作 | 重なる面積に応じて、ある地域の集合の指標値を別の集合に再配分し、`Redistributed` 列として追加します。 |
| RegEx | 完全 | 正規表現変換 | テキストの解析、照合、置換を行います。 |
| Regression | 完全 | [ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/) | Assisted Modelingのチェーンを、1つのML Trainステップに統合します。 |
| Report Map | 完全 | マップレポートアーティファクト | クラウドネイティブなマップ/レポートのアーティファクトを生成します。 |
| Run Command | 部分対応 | RESTの接続に対する[RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/)（`curl`/`wget` のみ） | `curl` または `wget` のコマンドラインを、RESTリクエストステップに変換します。インタープリターやスクリプトのコマンド（`cscript`、PowerShell、Pythonなど）、Excel-COMによる自動化、ファイルシステム操作、および内容が不明なコマンドやワークフローを起動するコマンドは、自動変換されず、手動レビュー用に名前を示してフラグが付けられます。 |
| Sample | 完全 | サンプル変換 | 件数、割合、またはグループ化に基づいてレコードを保持します。 |
| Select | 完全 | 選択とスキーマ射影のステップ | フィールドの選択、名前変更、並べ替え、型の変更を行います。 |
| Smooth | 完全 | [Spatial Smooth](/ja/reference/workflow-steps/spatial/spatial-smooth/)ステップ | 指定した回数のパスで、各ジオメトリを平滑化します。 |
| Sort | 完全 | 並べ替え変換 | 設定されたフィールドと方向でレコードを並べ替えます。 |
| Spatial Info | 完全 | [Spatial Info](/ja/reference/workflow-steps/spatial/spatial-info/)ステップ | 面積、長さ、重心、外接矩形を測地線による測定値として求めます。 |
| Spatial Match | 完全 | [空間照合](/ja/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/ja/reference/workflow-steps/spatial/spatial-match-executor/)ステップ | すべての関係（Within、Contains、Intersects、Touches、Crosses、Overlaps、Centroid-In）を変換し、データベースまたはワークフローエンジンで照合します。 |
| Spatial Process | 完全 | [空間処理](/ja/reference/workflow-steps/spatial/spatial-process/) | ジオメトリ列の交差、結合、切り取りを行います。 |
| Summarize | 完全 | 集計変換 | グループ化と集計を行います。合計、件数、平均、最小、最大、中央値、最頻値、標準偏差、分散、重複排除件数に対応します。 |
| Tab | 完全 | アプリのタブのグループ化 | 変換されたアプリの構造として保持されます。 |
| Test | 完全 | ステップ条件 | テストのアサーションを、ステップ条件に変換します。 |
| Text Box | 完全 | 制御されたテキスト変数 | アプリのテキスト入力を、型付きの変数に変換します。 |
| Text Input | 完全 | インラインテーブル入力 | ワークフロー用のインラインデータを作成します。 |
| Text Pre-processing | 完全 | NLP前処理エグゼキューター | テキストを正規化し、前処理します。 |
| Text Summary | 完全 | [Text: NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ（summaryタスク） | LLMを使ったNLP AIステップを通じて、テキスト列を、設定された最大文数に要約します。 |
| Text To Columns | 完全 | 列分割変換 | テキストをフィールドまたは行に分割します。 |
| Tile | 完全 | タイル / グループ化変換 | 設定されたルールで、タイルグループを割り当てます。 |
| Tool Container | 完全 | キャンバスのコンテナー / 実行グループ | ワークフローの整理として保持されます。 |
| Topic Modeling | 完全 | トピックモデリングエグゼキューター | マネージドNLPを通じて、トピックモデリングを実行します。 |
| Transformation | 完全 | 変換ステップ | 変換ロジックを、PlaidCloudの式またはSQLに変換します。 |
| Transpose | 完全 | アンピボット変換 | 列を行に変換し、名前と値のペアにします。 |
| Tree | 完全 | 制御されたワークフロー変数 | アプリのツリーの選択を、制御された入力に変換します。 |
| Union | 完全 | ユニオン変換 | 名前、位置、または設定されたルールで、ストリームを結合します。 |
| Unique | 完全 | 一意 / 重複分割変換 | 最初の一意のレコードと重複を分離します。 |
| Visual Layout | 完全 | キャンバスのレイアウトメタデータ | デザインのコンテキストとして保持されます。 |
| Word Cloud | 完全 | テキスト可視化アーティファクト | テキスト分析から、可視化のアーティファクトを作成します。 |
| XML Parse | 完全 | XML解析変換 | XMLのフィールドを、ワークフローのデータに抽出します。 |
| Zero-shot Text Classification | 完全 | [Text: NLP AI](/ja/reference/workflow-steps/text-documents/nlp-ai/)ステップ（zeroshotタスク） | LLMを使ったNLP AIステップを通じて、行ごとの候補ラベルのリストに対して、シングルラベルまたはマルチラベルでテキスト列を分類します。 |
| Find Nearest | 完全 | [Spatial Find Nearest](/ja/reference/workflow-steps/spatial/spatial-find-nearest/)ステップ | 距離順の最近傍結合です。直線距離に加え、PlaidCloudのセルフホスト型ルーティングエンジンによる、ドライブタイム（道路ネットワーク上の所要分数で順位付け）での最近傍にも対応します。ドライブタイムはワークスペースごとに有効化します。 |
| Trade Area | 完全 | [Spatial Trade Area](/ja/reference/workflow-steps/spatial/spatial-trade-area/)ステップ | 実世界の単位で大きさを指定した同心円状のバッファーです。固定半径に加え、セルフホスト型ルーティングエンジンによる、ドライブタイム（道路ネットワーク上の所要分数）の商圏にも対応します。ドライブタイムはワークスペースごとに有効化します。 |
| Image Template | 完全 | Image Templateエグゼキューター操作 | 手動モードでは、テンプレート上に描画した各領域に画像を切り抜きます。自動モードでは、オープンスタンダードのレイアウトモデルでページの領域を検出し、領域ごとに1行を出力します。各行には、レビュー用に検出された境界と信頼度が含まれます。モデルが確信を持って読み取れないページは、切り抜かれずに名前を示してフラグが付けられます。オープンスタンダードによる検出はAlteryx独自のものと異なる場合があるため、検出された領域を確認するか、正確に制御したい場合は手動モードを使用してください。 |
| Image Recognition | 完全 | 画像認識エグゼキューター | ワークフロー内で画像分類器を学習させ、その場で新しい画像をスコアリングします。外部アカウントは不要で、データがPlaidCloudの外に出ることはありません。分類器はAlteryxからコピーするのではなく再学習されるため、結果はビット単位で一致するものではなく、忠実な近似になります。学習はCPUで実行されます。ワークスペースごとに有効化します。 |
| Geocoder | 完全 | セルフホスト型ジオコーダー | PlaidCloud独自のジオコーダーを使って、住所を座標にジオコーディングし、座標を住所に逆ジオコーディングします。外部アカウントは不要で、データがPlaidCloudの外に出ることはありません。ワークスペースごとに有効化します。 |

インターフェイスのウィジェット（ドロップダウン、リストボックス、チェックボックス、
テキスト/数値/日付の入力、ファイルとフォルダーのピッカー）、キャンバスのオブジェクト（コメント、リンク、
コンテナー）、およびマクロポートは、いずれもネイティブの制御された変数またはキャンバスオブジェクトとして変換されます。
Alteryxアプリのインターフェイスレイアウト全体（`.yxwz` ファイルの
`<Questions>` 定義）も、公開されたPanelの「App
Runner」フロントエンドとして具体化されます。そのため、アプリを変換すると、個々の制御された変数だけでなく、
同じ値を収集して変換後のワークフローを動かす、動作する入力フォームが生成されます。
上の「Analytic App interface」の行と、
[変換されたAlteryxアプリを使用する](/ja/guides/workflows/use-converted-alteryx-apps/#app-runnerフロントエンド)をご覧ください。

**Excel出力に関する注記：** 既定の書式でデータを書き込む、新規の通常のブックは、
完全に変換されます。名前付きのシートと範囲に書式を保持したまま入力する、*スタイル付きテンプレート* への書き込みは、
単一のシートに対しても、1つのブックの異なるシートに組み立てられる複数の出力に対しても変換されます
（[Export to Excel Sheets](/ja/reference/workflow-steps/export/export-to-excel-sheets/)
ステップが、すべてのシートを1回のパスで入力します）。ピボットテーブルやグラフを含むテンプレートでは、
シートの書き込み時にそれらのオブジェクトが削除されます。Run Command（Excel COM/VBS）から
行うシート単位のファイル操作は、自動変換されず、手動レビュー用に名前を示してフラグが付けられます。

## 空間ツールの対応範囲

Alteryxの **Spatial** パレットにあるすべてのツールには、PlaidCloudでの対応ルートがあり、
そのすべてのルートは手作業でも構築できるステップです。変換は
便利な手段であって、唯一の方法ではありません。完全なリファレンスは[地理空間ステップ](/ja/reference/workflow-steps/spatial/)を、
それらがどう組み合わさるかは[地理空間分析](/ja/guides/workflows/geospatial-analytics/)をご覧ください。

| Alteryx空間ツール | PlaidCloudでのルート | 実行場所 |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/ja/reference/workflow-steps/spatial/spatial-buffer/)ステップ | ワークフローエンジン |
| Centroid | Centroidエグゼキューター操作 | ワークフローエンジン |
| Convex Hull | Convex Hullエグゼキューター操作 | ワークフローエンジン |
| Create Points | [Table Extractの式](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/) | データベース |
| Distance | [Table Extractの式](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/) | データベース |
| Find Nearest | [Spatial Find Nearest](/ja/reference/workflow-steps/spatial/spatial-find-nearest/)ステップ | データベース。ドライブタイムの場合はルーティングサービス |
| Generalize | [Spatial Generalize](/ja/reference/workflow-steps/spatial/spatial-generalize/)ステップ | ワークフローエンジン |
| Heat Map | [Heat Map (macro)](/ja/reference/workflow-steps/macros/macro-heat-map/) | ワークフローエンジン |
| Line To Polygon | Line To Polygonエグゼキューター操作 | ワークフローエンジン |
| Make Grid | [Spatial Make Grid](/ja/reference/workflow-steps/spatial/spatial-make-grid/)ステップ | ワークフローエンジン |
| Point To Line | Point To Lineエグゼキューター操作 | ワークフローエンジン |
| Poly-Build | [Spatial Poly-Build](/ja/reference/workflow-steps/spatial/spatial-poly-build/)ステップ | ワークフローエンジン |
| Poly-Split | [Spatial Poly-Split](/ja/reference/workflow-steps/spatial/spatial-poly-split/)ステップ | ワークフローエンジン |
| Redistribute | Redistributeエグゼキューター操作 | ワークフローエンジン |
| Smooth | [Spatial Smooth](/ja/reference/workflow-steps/spatial/spatial-smooth/)ステップ | ワークフローエンジン |
| Spatial Info | [Spatial Info](/ja/reference/workflow-steps/spatial/spatial-info/)ステップ | ワークフローエンジン |
| Spatial Match | [空間照合](/ja/reference/workflow-steps/spatial/spatial-match/) | データベース |
| Spatial Match（交差オブジェクト、Unmatched） | [Spatial Match (Intersect / Unmatched)](/ja/reference/workflow-steps/spatial/spatial-match-executor/)ステップ | ワークフローエンジン |
| Spatial Process | [空間処理](/ja/reference/workflow-steps/spatial/spatial-process/) | ワークフローエンジン |
| Trade Area（固定半径とドライブタイム） | [Spatial Trade Area](/ja/reference/workflow-steps/spatial/spatial-trade-area/)ステップ | ワークフローエンジン。ドライブタイムの場合はルーティングサービス |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/ja/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | ワークフローエンジン |
| 空間ファイル入力 | [空間ファイルのインポート](/ja/reference/workflow-steps/spatial/spatial-file-import/) | ワークフローエンジン |
| Summarize（SpatialObjCombine、SpatialObjConvexHull） | [空間結合](/ja/reference/workflow-steps/spatial/spatial-combine/) | ワークフローエンジン |
| Report Map | [Report Map](/ja/reference/workflow-steps/reports/report-map/)ステップ | ワークフローエンジン |

**ドライブタイムの商圏と最近傍：** Trade Areaのドライブタイムリングと、Find
Nearestのドライブタイムによる順位付けは、ホスト型のサードパーティ
APIではなく、PlaidCloudのセルフホスト型ルーティングエンジン
（道路ネットワークの等時間圏と移動時間マトリックス）で実行されるため、起点の座標がプラットフォームの外に出ることはありません。ドライブタイムは
ワークスペースごとに有効化します。ルーティングとドライブタイムのエリアには、OpenStreetMapのデータを使用しています。
© OpenStreetMap contributors。[Open Database License
(ODbL)](https://www.openstreetmap.org/copyright)の下で利用できます。

### 空間に関する既知の前提条件

空間ツール自体は変換されます。以下は、入力側の前提条件です。

- **`.geo` GeoFile形式。** Alteryx独自のバイナリ形式のGeoFileには、公開されたリーダーがないため、
  そのインポートは、実行時にクラッシュするのではなく、安全側に失敗します。
  Alteryxでレイヤーを標準的な空間形式（シェープファイルまたはGeoJSON）に
  再エクスポートし、それをインポートしてください。他の空間形式には影響しません。
  [空間を扱うAlteryxワークフローの移行](/ja/guides/workflows/migrate-spatial-alteryx-workflows/#空間入力のパッケージ化)をご覧ください。
- **Spatial InfoのPeanoキーの測定値。** Peanoキーは、公開された仕様のない、Alteryx独自の
  空間インデックスです。そのため、それを要求するSpatial Infoは、
  その1列をスキップし、注記でそれを明示します。Spatial Infoのそれ以外の測定値
  （面積、長さ、重心、外接矩形、オブジェクトタイプ、パーツ数とポイント数、
  端点）は、すべて変換されます。
- **投影座標系のCreate Pointsの座標。** Create Pointsは、
  浮動小数点と整数（×1,000,000）の経度/緯度の座標を直接変換します。
  すでに投影座標系になっている座標は、ワークフローがどの投影法を使っているかを記録していないため、
  先に上流でWGS84の経度/緯度に再投影する必要があります。

## Calgaryツールの対応範囲

AlteryxのCalgaryデータベース（`.cydb`）は、PlaidCloudでは開けない、独自のインデックス付きストアです。変換では、それぞれを、`calgary_<database name>` という名前の、通常のPlaidCloudテーブル1つに対応するものとして扱います。そのため、それを中心に作られたツールは、変換を完全に拒否されるのではなく、通常のテーブル操作として変換されます。代替テーブルの仕組みは[Calgaryデータベース](/ja/guides/workflows/migrate-alteryx-workflows/#calgaryデータベース)を、インデックス照合ツールについては[Calgary JoinとCross Count Append](/ja/guides/workflows/migrate-alteryx-workflows/#calgary-joinとcross-count-append)をご覧ください。

| Alteryx Calgaryツール | PlaidCloudでのルート | 変換可否 |
| --- | --- | --- |
| Calgary Loader | `calgary_<database>` に書き込むTable Extractステップ | はい。データベースに名前が付いていて、少なくとも1つのデータフィールドを保存している場合。 |
| Calgary Input | 保存されたクエリをフィルターとして、`calgary_<database>` を読み取る動的なドキュメント入力 | はい。OrまたはNotで包んで構築されたクエリ、およびcontainsやstarts-withのフィルター（SQLのLIKEとして再構築）も含みます。空間検索のクエリと、Skip Records/Max Recordsの制限では変換を拒否します。 |
| Calgary Input (Count Only) / Calgary Cross Count | `calgary_<database>` に対する集計変換 | はい。OrまたはNotで包んで構築されたバケットも含みます。複数のカスタムフィールドにまたがるクロスと、数える対象の列を指定していないcount-only読み取りでは、変換を拒否します。 |
| Calgary Join | 入力の各レコードを `calgary_<database>` と照合する動的なドキュメント入力 | 受け取ったフィールドが、値インデックスと照合される通常の値である場合。Count Onlyモードも含みます。このモードでは、入力レコードごとに一致したデータベースレコードの数を数え、何にも一致しないレコードは0になります。フィールドが空間である場合（Spatial Matchとして再構築してください）、またはその型が未解決の場合、さらに、範囲インデックスまたはUnmatched出力が接続されたJoin、一致フィールドを指定していないJoin、入力に何も接続されていないJoinでは、変換を拒否します。 |
| Calgary Cross Count Append | 各レコードを照合する動的なドキュメント入力と、それに続く `calgary_<database>` に対するカウント付き結合 | 受け取ったフィールドが、値インデックスと照合される通常の値である場合。入力レコードごとに、一致したデータベースレコードの数を数え、何にも一致しないレコードは0になります。空間または未解決のインデックス（Spatial Matchとして再構築してください）、カスタム値のクロスカウントグリッド、範囲インデックス、フィールドを指定していない照合では、変換を拒否します。 |

### Calgaryに関する既知の前提条件

これらの大半は、変換の制限ではなく、入力側の前提条件です。

- **空間インデックスの照合は、Spatial Matchとして再構築する必要があります。** 空間インデックスと照合されるCalgary JoinまたはCross Count Appendは、代替テーブルの名前を示して変換を拒否します。ワークフローはインデックスの名前を記録しますが、それが通常の値を保持しているのか空間ジオメトリを保持しているのかは記録しません。また、値の照合（等価結合）と空間の照合（点とポリゴンの包含）は、異なる操作だからです。データベースをテーブルにエクスポートし、照合をJoin（値インデックス）またはSpatial Match（空間インデックス）として再構築してください。
- **Skip RecordsまたはMax Recordsで制限された読み取りには、明示的な順序が必要です。** エクスポートされた代替テーブルにはレコードの順序がないため、位置で先頭または末尾のN件を取得したい場合は、エクスポート時に順序列を追加してください。
- **人口統計や参照用のデータベースは、先に読み込んでおく必要があります。** データベースが読み込まれる前にCalgaryの読み取りを行うと、構築すべきテーブルの名前を示して停止します。`.cydb` ファイル自体には公開されたリーダーがないため、Alteryxで再エクスポートし（Calgary InputをOutput Dataツールに接続して、CSVまたはParquetを書き込みます）、それを名前付きテーブルとしてインポートしてください。[読み取れない .cydb（Calgary）データベース](/ja/guides/workflows/troubleshoot-alteryx-imports/#読み取れないcydbcalgaryデータベース)をご覧ください。これは、Alteryxが同梱する、ライセンスされた人口統計や参照用の `.cydb` ファイル（Experian、Censusなど）で一般的なケースです。サードパーティのそのデータを再現できるコンバーターはないため、ライセンスされた参照データをご自身で用意して名前付きテーブルに読み込んでください。これはGeocoderの参照データと同様です。
- **データフィールドを保存しないCalgary Loaderは変換されません。** 書き込まれるテーブルに列がなくなるためです。
- **カスタム値のクロスカウントグリッドは、まだ変換されません。** 単一の通常のクロスカウントフィールドは変換され、入力レコードごとに、一致するデータベースレコードの数を数えます。しかし、*名前付きの* カスタム値のグリッドは、値ごとに1つのカウント列を追加することになり、Alteryxはその列数も列名も文書化していません。今後のリリースで対応を予定しており、列の仕様をリバースエンジニアリングするための参照用エクスポートを待っています。

値、範囲、contains、starts-withのクエリは、すべてフィルターに変換されます。変換されないのは、列レベルの同等機能がないインデックス操作である、空間検索のクエリだけです。

## 外部システムへの接続

Alteryxのコネクターのエンドポイント（Salesforce、HTTP、Google Analytics、Cassandra、
メール、Hadoop、Spark。入力と出力の両方向）は、変換されません。
PlaidCloudは、これらのシステムに、キャンバス上のツールではなく接続を通じてアクセスするためです。それぞれ、
名前を示して変換を拒否し、その作業をどこで行うかを案内します。

| Alteryxツール | PlaidCloudでの移行先 |
| --- | --- |
| Salesforce Input / Output | **Salesforce**接続 |
| Anaplan | **Anaplan**接続 |
| HTTP Input | **REST**接続に対する**RESTリクエスト**ステップ |
| Google Analytics Input | Google Analytics tapを使った**インポート: Singerソース** |
| Cassandra Input | Cassandra tapを使った**インポート: Singerソース** |
| Email Input | GMail tapを使った**インポート: Singerソース** |
| Hadoop Input / Output | Hive、Impala、Presto接続を通じた**インポート: SQL** / **エクスポート: SQL** |
| Spark Input / Output | Databricks接続を通じた**インポート: SQL** / **エクスポート: SQL** |

これらのうち4つには、書き込みパスがまったくありません。PlaidCloudは、Google Analyticsと
Cassandraを読み取りますが、書き込みは行いません。そのため、Google Analytics OutputまたはCassandra
Outputツールは、サポートされている宛先への**エクスポート: SQL**になります。
メールもデータの宛先ではありません。**通知: メール**は、ユーザーに
通知を送信するものなので、Email Outputツールは、Exportステップと、
別個の通知に置き換えられます。**Anaplan**接続も、同様に読み取り専用です。
保存されたビューを読み取り、既存のエクスポートアクションを実行し、リストをPlaidCloudのディメンションに読み込みますが、
Anaplanに書き戻すPlaidCloudのステップはありません。

## 変換されたワークフローの検証

本番のワークフローでは、変換された出力を、信頼できるAlteryxの出力と照合して検証してください。
PlaidCloudの検証は、スキーマ、行数、行の値に重点を置き、
ワークフローが順序に依存しない限り、行の順序は無視します。専門的な
操作（空間、あいまい一致、OCR、NLP、レポート）は、ワークフローをクラウドネイティブに保つ
マネージドジョブエグゼキューターを通じて実行されます。機械学習のパイプラインは、
ネイティブの[ML: モデルの学習](/ja/reference/workflow-steps/machine-learning/ml-train/)と
[ML: スコアリング](/ja/reference/workflow-steps/machine-learning/ml-score/)のステップに変換されます。
インポートから検証までの一連のガイドは、[Alteryxワークフローの移行](/ja/guides/workflows/migrate-alteryx-workflows/)
をご覧ください。
