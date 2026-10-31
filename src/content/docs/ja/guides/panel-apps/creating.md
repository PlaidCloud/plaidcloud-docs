---
title: Panelアプリの作成
description: Panel Studioで、空のアプリ、テーブル、ビュー、ギャラリーのいずれかからPanelアプリを作成します。独自の要件がある場合は、gitからサーバーアプリを、または静的なWASMアプリを公開します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

まずPanel Studioから始めてください。リポジトリもセットアップも不要で、PlaidCloud上でアプリを作成してプレビューし、準備ができたら公開できます。Studioでは対応できない場合にだけ、独自のランタイムを選択してください。

## Studioアプリを作成する

**マイPanelアプリ**を開きます。**新しい Studio アプリ**はツールバーの最初のボタンです。プロジェクトの**ホーム**タブの**Panelアプリ**ボックスで**新しい Studio アプリ**を選択するか、[テーブルから開始](#テーブルから開始する)することもできます。

1. **新しい Studio アプリ**を選択します。
2. **名前**を入力します。**URLスラッグ**は名前から自動入力されます。
3. アプリを所有する**プロジェクト**を選択します。プロジェクトの編集アクセス権が必要です。
4. **開始元**で、アプリの開始元を選択します。

   | 開始元 | 作成されるもの |
   |---|---|
   | **空のアプリ** | `app.py`と`requirements.txt`だけの最小限のアプリです。 |
   | **テーブルから** | 選択したテーブルを元に作成されるアプリです。 |
   | **ビューから** | 同様に、プロジェクトのビューを元に作成されるアプリです。 |
   | **別の Studio アプリから** | ご自身のStudioアプリのコピーです。 |
   | **ギャラリーから** | ワークスペースが[ギャラリーに掲載した](#ギャラリーから開始する)アプリのコピーです。 |

5. **作成**を選択します。Studioが新しいアプリを開きます。テーブルまたはビューの場合は、最初のページを作成するためのWeaveのプロンプトがすぐに送信できる状態になっています。

アプリの編集、プレビュー、公開については、[Panel Studio](/ja/guides/panel-apps/studio/)を参照してください。

### テーブルから開始する

プロジェクトの**テーブル**タブから始めることもできます。テーブルまたはビューを1つ選択し、**新規**メニューまたは右クリックメニューから**Panel アプリを作成**を選択します。プロジェクトとテーブルがすでに選択された状態で、**新しい Studio アプリ**ダイアログが開きます。このコマンドは、プロジェクトの編集アクセス権があり、プロジェクトが読み取り専用でない場合に使用できます。

### ギャラリーから開始する

**マイPanelアプリ**ツールバーの**ギャラリー**を選択すると、ワークスペースが掲載したアプリを参照できます。続いて **これからアプリを作成…** ボタンを選択して、自分用のコピーを作成します。**新しい Studio アプリ**ダイアログで**ギャラリーから**を選択する方法もあります。ご自身のアプリを掲載する方法を含め、[アプリギャラリー](/ja/guides/panel-apps/gallery/)を参照してください。

## その他のランタイム

Studioアプリは、ほとんどのダッシュボードやツールに対応します。独自の要件がある場合は、**マイPanelアプリ**ツールバーから、他の[ランタイム](/ja/guides/panel-apps/)のいずれかで公開します。

- **WASMアプリを追加** — 静的なブラウザー内アプリをファイルから公開します。
- **新しいサーバーアプリ** — 自分で管理するgitリポジトリからアプリをビルドして実行します。たとえば、既存のコードや独自のビルドプロセスを再利用する場合に使います。
- **新しいDashアプリ** — Plotly Dashアプリを公開します。[Dashアプリ](/ja/guides/dash-apps/)を参照してください。

## サーバーアプリの作成

サーバーアプリはgitリポジトリからビルドされ、`https://<your-tenant-host>/serve/<slug>/`で配信されます。PlaidCloudにリポジトリのブランチを指定すると、コードをコンテナーにビルドして`panel serve`で実行し、そのブランチにプッシュするたびに自動的に再ビルドします。

### アプリのリポジトリを準備する

リポジトリには2つのものが必要です。**エントリポイント**（Panelアプリを構築して`.servable()`を付けるPythonファイル）と、必要に応じて追加パッケージを列記した **`requirements.txt`**（リポジトリのルート、またはエントリポイントの隣）です。

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

`app.py`を作成します。

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

これで完全なアプリです。PlaidCloudが配信するのは`.servable()`を呼び出したものです。表示したいものはすべて、直接、または servable なレイアウトの内側に置くことで、servableにする必要があります。

#### もう少し複雑な例

Panelアプリはインタラクティブです。次の例では、テーブルをリアルタイムに更新するスライダーを追加しています。

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### 依存関係を追加する

この2つ目の例では`pandas`をインポートしています。これはベースイメージに含まれていないため、`requirements.txt`を追加します（リポジトリのルート、またはエントリポイントの隣）。

```text
pandas
```

PlaidCloudは、イメージのビルド時にこれらを`pip`でインストールします。`plotly`、`holoviews`、`hvplot`などの一般的な可視化ライブラリもベースイメージに含まれていないため、アプリがインポートするものはここに記載してください。

> **プラットフォームが提供するもの、および前提とするもの。** アプリを作成するときは、次の前提に留意してください。
>
> - **`panel`と`bokeh`はプリインストールされています**。プラットフォームのベースイメージに含まれています。`requirements.txt`には記載せず、古いPanelバージョンへの固定も避けてください。ライブ更新の再接続は新しいバージョンに依存しています。
> - **PlaidCloudのクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされています。** `plaidcloud.rpc`または`plaidcloud.utilities`を直接インポートしてください。`requirements.txt`には記載しないでください。
> - **`requirements.txt`は、リポジトリのルートまたはエントリポイントの隣に置けます。** 共有（モノレポ）リポジトリでは、各アプリの依存関係をそれぞれのフォルダーに置いてください。ルートにファイルがある場合は、それもインストールされます。共通の依存関係はルートに、アプリ固有のものはアプリの隣に置きます。
> - **アプリは、読み取り専用のファイルシステム上で非rootユーザーとして実行されます。** 書き込めるのは`/tmp`のみのため、一時ファイルはそこに書き込んでください（ほとんどのライブラリはすでに`$TMPDIR`を参照します）。
> - **ポート、URLプレフィックス、ホストをハードコードしないでください。** これらはPlaidCloudが割り当て、デプロイ時に注入します。`.servable()`を呼び出すだけで十分です。

PlaidCloudの外観と、既製のフィルター、グリッド、チャートを利用するには、[Panelアプリキット](/ja/guides/panel-apps/app-kit/)でアプリを作成してください。

### テーマの設定: ライト、ダーク、切り替え

サーバーアプリは、既定でPlaidCloudのモダンな**Fast**デザインで表示されます。これはプラットフォーム全体に適用される、Fluent風のすっきりした外観です。公開ダイアログでは、**デザイン**がこのプラットフォーム層を制御します。

- **FAST** — PlaidCloudのデフォルトです。新しいアプリや、Fastテンプレートで作成したアプリに使用します。
- **デフォルト** — Panelのデフォルトのスタイルです。既存アプリのCSSや表示がFASTで崩れる場合に使用します。

アプリのコードで制御するのは**テーマ**です。ライト、ダーク、または閲覧者が切り替えられるスイッチのいずれかです。

テーマは、配信する**テンプレート**のプロパティです。Fastテンプレートの`FastListTemplate`（1列）と`FastGridTemplate`（レスポンシブなグリッド）には、テーマ用に2つの設定があります。

- **`theme`** — ライトの場合は`"default"`、ダークの場合は`"dark"`です。これを設定すると、閲覧者がURLに`?theme=dark`を追加しても、アプリはそのテーマに固定されます。
- **`theme_toggle`** — `True`にするとヘッダーにライト/ダークのスイッチが表示され、`False`にすると非表示になります。デフォルトは`True`です。スイッチを非表示にしただけではテーマは固定されません。上記の`theme`で固定し、そのうえで`theme_toggle=False`を設定して、何も変更できないスイッチが閲覧者に表示されないようにします。

アプリに合ったパターンを選んでください。

**ライトのみ** — 通常はライトな背景に合わせて手作業でスタイルを設定する、密度の高いレポートや財務テーブルに最適です。

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**ダークのみ:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**閲覧者に選択させる** — デフォルトはライトで、ヘッダーにスイッチが表示されます。`theme`を省略すると、トグルに従います。

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **ダークを許可する場合は、テーブルもダークに対応させてください。** ライトのテーブルテーマに固定された`Tabulator`（`theme="bootstrap"`）や、`background: #fff`のようにライトな色をハードコードしたカスタムCSSは、ダークなページ上で読めない白いブロックとして表示されます。アプリに追従するテーブルテーマ（`pn.widgets.Tabulator(..., theme="fast")`）を使用し、ライトな色のハードコードは避けてください。レポートがライト向けに細かくスタイル設定されている場合は、代わりにライトに固定してください（上記の最初のパターン）。

テンプレートを使わないシンプルなアプリ（`pn.Column(...).servable()`）は、Panelのデフォルトに従い、これらの設定の影響を受けません。明示的に制御したい場合は、テンプレートを使用してください。

リポジトリは、PlaidCloudの**Git接続**を通じて到達できる必要があります。コードが[PlaidCloud Git](/ja/guides/git/)にある場合は、**Tools > Connections**で、管理対象の**PlaidCloud Git**接続を作成します。サーバーURLも認証情報も不要です。空のリポジトリから配信されるアプリまでの全体の流れについては、[PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/)を参照してください。

### アプリを公開する

1. **新しいサーバーアプリ**をクリックして、**サーバーPanelアプリを公開**ダイアログを開きます。設定はセクションごとにまとめられています。
2. **ディレクトリ設定**で次を設定します。
   - **アプリ名** — 一覧に表示される表示名です。
   - **URLスラッグ** — アプリのURLと内部名の両方になるため、有効なDNSラベルである必要があります。小文字、数字、ハイフンで、英字で始まり、40文字以内にしてください（例: `sales-dashboard`）。ダイアログが公開前にこれを確認します。
   - **メモ** — 任意の説明です。
   - **プロジェクト** — アプリを所有するプロジェクトです。アプリの[ブランディング](/ja/guides/panel-apps/branding/)を提供し、アプリのテーブルのデフォルトのプロジェクトになります。公開後にここで変更することはできません。[Assign](/ja/guides/panel-apps/branding/#既存のアプリの場合)を使用してください。
3. **Git接続と公開ウォッチャー**で次を設定します。
   - **Git接続** — アプリのリポジトリを保持する接続です。
   - **ブランチ** — ビルド元のブランチです。このブランチへのプッシュにより、アプリが自動的に再ビルドされ、再デプロイされます。
   - **エントリポイント** — Panelが配信する`.py`ファイル（`app.py`）です。
4. **ランタイム**で次を設定します。
   - アプリのコンテナーが要求する**CPU**と**メモリ**。

     > リソース（CPU/メモリ）を減らすと、アプリのスケジュールとコールドスタートが速くなります。

   - **デザイン** — PlaidCloudのモダンなデザインの場合は**FAST**を、アプリのCSSがPanelのデフォルトのスタイルを前提としている場合は**デフォルト**を選択します。
   - **アイドル (分)** — トラフィックがない状態でアプリがウォーム状態を維持し、その後ゼロにスケールダウンするまでの時間です。デフォルトは5分です。
   - **パブリックアクセスを許可** — 認証なしのアクセスを許可する場合はオンにします。オフの場合、閲覧者はテナントにサインインする必要があります。
5. **詳細 (埋め込み配信)** — 任意です。既定では、アプリはPlaidCloudテナントからのみ配信されます。別のサイトに埋め込むには、**ドメインを追加**をクリックし、読み込みを許可する各ドメインを1行に1つずつ入力します。ホストのみで、スキームやパスは含めません（例: `example.com`、`app.example.com:8443`）。アプリを他の場所に埋め込む場合を除き、一覧は空のままにしてください。
6. **公開**をクリックします。

公開後、アプリは**ビルド**されます。**ステータス**は一覧に表示され、自動的に更新されます。ステータスの意味、準備ができたアプリを開く方法、公開を取り消さずに再ビルドを実行する方法については、[Panelアプリの使用](/ja/guides/panel-apps/using/)を参照してください。

> アプリのURLは、ビルドのステータスが**準備完了**になって初めて機能します。また、アイドル状態の後の最初のリクエストでアプリが起動します（約15秒）。

### 上級: PlaidCloudをローカルで再現する

技術的なユーザーは、PlaidCloudと同じ入力でアプリをビルドしてテストできます。これは、公開前または**再ビルド**をクリックする前に行える、最も近いローカルでの確認方法です。

PlaidCloudは、選択したgitブランチから、次の生成されたDockerfileを使ってビルドします。ローカルでも同じ内容を`Dockerfile.plaidcloud-panel`として使用してください。

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

サーバーでのビルドに合わせるには、次の手順に従います。

1. **ブランチ**で選択したものと同じブランチをチェックアウトします。
2. `COPY . /app`がPlaidCloudと一致するよう、リポジトリのルートからビルドを実行します。
3. 任意の依存関係は`requirements.txt`に記載します。リポジトリのルート、またはエントリポイントの隣に置きます。両方がインストールされ、アプリのフォルダーのものが最後にインストールされます（アプリごとの固定が優先されます）。
4. **エントリポイント**で選択したものと同じエントリポイントのパスを使用します。

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

デプロイされたイメージは、ベースイメージのエントリポイントを上書きしません。PlaidCloudが注入する環境変数から`panel serve`を実行します。同じランタイムの契約で、ビルドしたイメージをテストします。

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

`http://localhost:5006/serve/local/`を開きます。

テストするときは、公開ダイアログの設定に合わせてください。

- **エントリポイント**は`APP_PATH=/app/<entry-point>`に対応します。
- **CPU**と**メモリ**は、Dockerの`--cpus`と`--memory`の制限に対応します。
- **デザイン: FAST**は`PLAID_PANEL_DESIGN=fast`に対応します。
- **デザイン: デフォルト**は、`PLAID_PANEL_DESIGN`を省略することを意味します。
- **アイドル (分)** は、デプロイ環境でのスケールダウンまでの時間に対応します。ローカルのDockerでは適用されませんが、アプリは同じPanelのwebsocketキープアライブとセッションクリーンアップの設定を使用します。
- **埋め込み配信**のドメインは`PANEL_ORIGIN`に対応します。複数のホストをテストする必要がある場合は、スペース区切りのリストを使用してください。

コンテナーが不要な場合でも、ローカルのPython環境から配信レイヤーをテストできます。同じ`requirements.txt`をインストールし、プラットフォームの環境変数を設定してから、デプロイされたイメージと同じフラグで`panel serve`を実行します。

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

`http://localhost:5006/serve/local/`を開きます。

デプロイ時の外観に合わせるには、`PLAID_PANEL_DESIGN=fast`を使用します。公開ダイアログの**デフォルト**デザインオプションをテストするには、`PLAID_PANEL_DESIGN`を未設定のまま同じコマンドを実行します。`PANEL_PREFIX`、`PANEL_ORIGIN`、`--keep-alive`、`--unused-session-lifetime`はそのまま維持してください。これらはデプロイされたランタイムの契約の一部です。

## WASMアプリの作成

WASMアプリは、ビルド済みのHTMLファイルからブラウザー内で実行されます。

1. **WASMアプリを追加**をクリックして、**サーバーレスPanelアプリを公開**ダイアログを開きます。
2. **アプリ名**と**バージョン**を入力します。
3. **アプリHTMLの場所**を選択します。ドキュメントアカウント内のHTMLファイルです。
4. **アプリURLスラッグ**と、任意の**メモ**を入力します。
5. **公開**をクリックします。WASMアプリにはビルドの手順がなく、すぐに配信されます。
