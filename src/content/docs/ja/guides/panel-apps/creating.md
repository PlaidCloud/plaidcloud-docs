---
title: Panelアプリの作成
description: Panel Studioで、空のアプリ、テーブル、ビュー、ギャラリーからPanelアプリを作成します。独自の要件には、gitからサーバーアプリを公開するか、静的なWASMアプリを公開します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

まずPanel Studioから始めてください。リポジトリもセットアップも不要で、PlaidCloudでアプリを構築し、プレビューして、準備ができたら公開できます。独自のランタイムを選択するのは、Studioが適さない場合のみにしてください。

## Studioアプリの作成

**アプリ**を開き、**新規アプリ**メニューを開きます。**Panel アプリ**の見出しの下にある**Studio**は、標準レイアウトでPlaidCloudのエディターにアプリを書き込んで公開し、コードを保持します。プロジェクトの**ホーム**タブの**アプリとブランディング**カードの**Studio アプリ**行で**新規 Studio アプリ**を選択するか、[テーブルから開始](#テーブルから開始する)することもできます。

1. **新規アプリ** > **Studio**を選択します。
2. **名前**を入力します。**URLスラッグ**は、そこから自動的に入力されます。
3. アプリを所有する**プロジェクト**を選択します。プロジェクトの編集アクセス権が必要です。
4. **開始元**で、アプリの開始元を選択します。

   | 開始元 | 作成されるもの |
   |---|---|
   | **空のアプリ** | `app.py`と`requirements.txt`を持つ最小限のアプリ。 |
   | **テーブルから** | 選択したテーブルに基づいて構築されたアプリ。 |
   | **ビューから** | 同様に、プロジェクトのビューに基づいて構築されたもの。 |
   | **別の Studio アプリから** | 自分のStudioアプリのコピー。 |
   | **ギャラリーから** | ワークスペースが[ギャラリーに掲載した](#ギャラリーから開始する)アプリのコピー。 |

5. **作成**を選択します。Studioが新しいアプリを開きます。テーブルまたはビューの場合は、最初のページを構築するためのWeaveのプロンプトが送信できる状態になっています。

アプリの編集、プレビュー、公開については、[Panel Studio](/ja/guides/panel-apps/studio/)を参照してください。

### テーブルから開始する

プロジェクトの**テーブル**タブから開始することもできます。1つのテーブルまたはビューを選択し、**新規**メニューまたは右クリックメニューから**Panel アプリを作成**を選択します。プロジェクトとテーブルがすでに選択された状態で、**新しい Studio アプリ**ダイアログが開きます。このコマンドは、プロジェクトの編集アクセス権があり、プロジェクトが読み取り専用でない場合に使用できます。

### ギャラリーから開始する

**新規アプリ** > **ギャラリーから…** メニュー項目を選択して、ワークスペースが掲載したアプリを閲覧し、**これからアプリを作成…** ボタンを選択して、自分用のコピーを作成します。または、**新しい Studio アプリ**ダイアログで**ギャラリーから**を選択します。自分のアプリを掲載する方法を含め、[アプリギャラリー](/ja/guides/panel-apps/gallery/)を参照してください。

## その他のランタイム

Studioアプリは、ほとんどのダッシュボードとツールに対応します。独自の要件がある場合は、**新規アプリ**メニューから、他の[ランタイム](/ja/guides/panel-apps/)のいずれかで公開します。

- **ブラウザのみ** — 自分のリポジトリです。アプリは、閲覧者のブラウザーで実行されます。
- **サーバーベース** — 自分のリポジトリです。アプリはPlaidCloudのサーバーで実行されます。たとえば、既存のコードや独自のビルドプロセスを再利用する場合です。
- **Dash アプリ** — Plotly Dashアプリを公開します。[Dashアプリ](/ja/guides/dash-apps/)を参照してください。

## サーバーアプリの作成

サーバーアプリは、gitリポジトリから構築され、`https://<your-tenant-host>/serve/<slug>/`で提供されます。リポジトリのブランチをPlaidCloudに指定すると、コードがコンテナーにビルドされ、そこで`panel serve`が実行され、そのブランチにプッシュするたびに自動的に再ビルドされます。

### アプリのリポジトリを準備する

リポジトリには、2つのものが必要です。**エントリポイント**（Panelアプリを構築し、`.servable()`でマークするPythonファイル）と、必要に応じて、追加のパッケージを一覧にした **`requirements.txt`** です。このファイルは、リポジトリのルート、またはエントリポイントの隣に配置します。

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

これで完全なアプリです。PlaidCloudが提供するのは`.servable()`の呼び出しです。表示したいものはすべて、（直接、またはservableなレイアウトの内側で）servableとしてマークする必要があります。

#### もう少し充実した例

Panelアプリはインタラクティブです。この例では、テーブルをリアルタイムで更新するスライダーを追加します。

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

#### 依存関係の追加

この2つ目の例では、ベースイメージに含まれていない`pandas`をインポートしているため、`requirements.txt`（リポジトリのルート、またはエントリポイントの隣）を追加します。

```text
pandas
```

PlaidCloudは、イメージのビルド時に、これらを`pip`でインストールします。`plotly`、`holoviews`、`hvplot`などの一般的な可視化ライブラリも、ベースイメージには含まれていないため、アプリがインポートするものはここに記載してください。

> **プラットフォームが提供するもの、そして想定しているもの**。アプリを作成するときは、次の前提を念頭に置いてください。
>
> - **`panel`と`bokeh`は、プラットフォームのベースイメージにプリインストールされています**。`requirements.txt`に記載せず、古いPanelバージョンのピン留めも避けてください。ライブ更新の再接続は、新しいバージョンに依存しています。
> - **PlaidCloudのクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされています**。`plaidcloud.rpc`または`plaidcloud.utilities`を直接インポートし、`requirements.txt`には記載しないでください。
> - **`requirements.txt`は、リポジトリのルート、またはエントリポイントの隣に配置できます**。共有（モノレポ）リポジトリでは、各アプリの依存関係をそれぞれのフォルダーに置いてください。ルートレベルのファイルがある場合は、それもインストールされます。共有の依存関係はそこに、アプリ固有のものはアプリの隣に置きます。
> - **アプリは、読み取り専用のファイルシステム上で、非rootユーザーとして実行されます**。書き込めるのは`/tmp`のみのため、一時ファイルはそこに書き込んでください（ほとんどのライブラリは、すでに`$TMPDIR`に従います）。
> - **ポート、URLプレフィックス、ホストをハードコードしないでください**。PlaidCloudがこれらを割り当て、デプロイ時に注入します。`.servable()`を呼び出すだけです。

PlaidCloudの外観と、すぐに使えるフィルター、グリッド、チャートを利用するには、[Panelアプリキット](/ja/guides/panel-apps/app-kit/)でアプリを構築してください。

### テーマの設定：ライト、ダーク、または切り替え

サーバーアプリは、デフォルトで、PlaidCloudのモダンな**Fast**デザインで表示されます。これは、プラットフォーム全体に適用される、Fluent風のすっきりした外観です。公開ダイアログでは、**デザイン**がこのプラットフォーム層を制御します。

- **FAST** — PlaidCloudのデフォルトです。新しいアプリと、Fastテンプレートで構築されたアプリに使用します。
- **デフォルト** — Panelのデフォルトのスタイルです。既存アプリのCSSや外観がFASTで崩れる場合に使用します。

アプリのコードで制御するのは、**テーマ**（ライト、ダーク、または閲覧者が切り替えられるスイッチ）です。

テーマは、提供する**テンプレート**のプロパティです。Fastテンプレート（`FastListTemplate`（単一の列）と`FastGridTemplate`（レスポンシブなグリッド））には、そのための2つの設定があります。

- **`theme`** — ライトの場合は`"default"`、ダークの場合は`"dark"`です。設定すると、閲覧者がURLに`?theme=dark`を追加しても、アプリがそのテーマに固定されます。
- **`theme_toggle`** — `True`はヘッダーにライト/ダークの切り替えスイッチを表示し、`False`は非表示にします。デフォルトは`True`です。スイッチを非表示にしても、テーマが固定されるわけではありません。上記の`theme`で固定してください。固定した後は、何も変更できないスイッチが閲覧者に表示されないよう、`theme_toggle=False`を設定します。

アプリに合ったパターンを選択してください。

**ライトのみ** — 通常、ライトの背景向けに手作業でスタイルが設定される、密度の高いレポートや財務テーブルに最適です。

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

**ダークのみ：**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**閲覧者に選択させる** — デフォルトはライトで、ヘッダーにスイッチがあります。`theme`を省略して、切り替えに従うようにします。

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **ダークを許可する場合は、テーブルもダークに対応させてください**。ライトのテーブルテーマ（`theme="bootstrap"`）に固定された`Tabulator`や、`background: #fff`のようにライトの色をハードコードしたカスタムCSSは、ダークのページでは読み取れない白いブロックとして表示されます。アプリに追従するテーブルテーマ（`pn.widgets.Tabulator(..., theme="fast")`）を使用し、ライトの色のハードコードは避けてください。レポートがライト向けに大幅に手作業でスタイル設定されている場合は、代わりにライトに固定してください（上記の最初のパターン）。

テンプレートのないシンプルなアプリ（`pn.Column(...).servable()`）は、Panelのデフォルトに従い、これらの設定の影響を受けません。明示的に制御したい場合は、テンプレートを使用してください。

リポジトリには、PlaidCloudの**git接続**を通じてアクセスできる必要があります。コードが[PlaidCloud Git](/ja/guides/git/)にある場合は、**Tools > Connections**で、管理対象の**PlaidCloud Git**接続を作成します。サーバーのURLも認証情報も不要です。空のリポジトリから、提供されるアプリまでの一連の流れについては、[PlaidCloud GitからのPanelアプリのデプロイ](/ja/guides/panel-apps/deploy-from-git/)を参照してください。

### アプリを公開する

1. **新規アプリ** > **サーバーベース**を選択して、**サーバーPanelアプリを公開**ダイアログを開きます。設定はセクションごとにグループ化されています。
2. **ディレクトリ設定**で：
   - **アプリ名** — リストに表示される表示名です。
   - **URLスラッグ** — アプリのURLと内部名の両方になるため、有効なDNSラベルである必要があります。小文字、数字、ハイフンのみで、文字で始まり、40文字以内にします（たとえば、`sales-dashboard`）。ダイアログは、公開前にこれを確認します。
   - **メモ** — 任意の説明です。
   - **プロジェクト** — アプリを所有するプロジェクトです。アプリの[ブランディング](/ja/guides/panel-apps/branding/)を提供し、そのテーブルのデフォルトのプロジェクトになります。公開後にここで変更することはできません。[Assign](/ja/guides/panel-apps/branding/#既存のアプリの場合)を使用してください。
3. **Git接続と公開ウォッチャー**で：
   - **Git接続** — アプリのリポジトリを保持する接続です。
   - **ブランチ** — ビルド元のブランチです。このブランチにプッシュすると、アプリが自動的に再ビルドされ、再デプロイされます。
   - **エントリポイント** — Panelが提供する`.py`ファイル（`app.py`）です。
4. **ランタイム**で：
   - アプリのコンテナーが要求する**CPU**と**メモリ**。

     > リソース（CPU/メモリ）を少なくすると、アプリのスケジュールとコールドスタートが速くなります。

   - **デザイン** — PlaidCloudのモダンなデザインには**FAST**を、アプリのCSSがPanelのデフォルトのスタイルを前提としている場合は**デフォルト**を選択します。
   - **アイドル (分)** — トラフィックがない状態で、アプリがウォームのまま維持され、その後ゼロにスケールバックするまでの時間です。デフォルトは5分です。
   - **パブリックアクセスを許可** — チェックすると、認証なしのアクセスが許可されます。チェックしない場合、閲覧者はテナントにサインインする必要があります。
5. **詳細 (埋め込み配信)**（任意）。デフォルトでは、アプリはPlaidCloudのテナントからのみ提供されます。別のサイトに埋め込むには、**ドメインを追加**をクリックし、読み込みを許可する各ドメインを、1行に1つ入力します。ホストのみで、スキームやパスは含めません（たとえば、`example.com`や`app.example.com:8443`）。アプリを他の場所に埋め込む場合を除き、リストは空のままにしてください。
6. **公開**をクリックします。

公開すると、アプリは**ビルド**されます。**ステータス**はリストに表示され、自動的に更新されます。ステータスの意味、準備ができたアプリの開き方、公開を取り消さずに再ビルドを実行する方法については、[Panelアプリの使い方](/ja/guides/panel-apps/using/)を参照してください。

> アプリのURLは、ビルドのステータスが**準備完了**になって初めて機能します。アイドル状態の後の最初のリクエストでは、起動に（約15秒）かかります。

### 詳細：PlaidCloudをローカルで再現する

技術に詳しいユーザーは、PlaidCloudが使用するのと同じ入力で、アプリをビルドしてテストできます。これは、公開前、または**再ビルド**をクリックする前にできる、最も近いローカルでの確認です。

PlaidCloudは、選択したgitブランチから、この生成されたDockerfileでビルドします。ローカルでも、同じ内容を`Dockerfile.plaidcloud-panel`として使用してください。

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

サーバーのビルドと一致させるには：

1. **ブランチ**で選択したものと同じブランチをチェックアウトします。
2. `COPY . /app`がPlaidCloudと一致するように、リポジトリのルートからビルドを実行します。
3. 任意の依存関係は、リポジトリのルート、またはエントリポイントの隣にある`requirements.txt`に記述します。どちらもインストールされ、アプリのフォルダーのものが最後にインストールされます（アプリごとのピン留めが優先されます）。
4. **エントリポイント**で選択したものと同じエントリポイントのパスを使用します。

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

デプロイされるイメージは、ベースイメージのエントリポイントを上書きしません。PlaidCloudが注入する環境変数から`panel serve`を実行します。ビルドしたイメージを、同じランタイムの契約でテストします。

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

テスト時には、公開ダイアログの設定と一致させます。

- **エントリポイント**は、`APP_PATH=/app/<entry-point>`に対応します。
- **CPU**と**メモリ**は、Dockerの`--cpus`と`--memory`の制限に対応します。
- **デザイン：FAST**は、`PLAID_PANEL_DESIGN=fast`に対応します。
- **デザイン：デフォルト**は、`PLAID_PANEL_DESIGN`を省略することを意味します。
- **アイドル (分)** は、デプロイ時のスケールダウンの猶予時間に対応します。ローカルのDockerでは適用されませんが、アプリは、同じPanelのWebSocketキープアライブとセッションクリーンアップの設定を使用します。
- **埋め込み配信**のドメインは、`PANEL_ORIGIN`に対応します。複数のホストをテストする必要がある場合は、スペース区切りのリストを使用します。

コンテナーが不要な場合でも、ローカルのPython環境から、配信レイヤーをテストできます。同じ`requirements.txt`をインストールし、プラットフォームの環境変数を設定してから、デプロイされるイメージと同じフラグで`panel serve`を実行します。

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

デプロイされた外観のデフォルトに合わせるには、`PLAID_PANEL_DESIGN=fast`を使用します。公開ダイアログの**デフォルト**デザインのオプションをテストするには、`PLAID_PANEL_DESIGN`を設定せずに、同じコマンドを実行します。`PANEL_PREFIX`、`PANEL_ORIGIN`、`--keep-alive`、`--unused-session-lifetime`はそのままにしてください。これらは、デプロイされるランタイムの契約の一部です。

## WASMアプリの作成

WASMアプリは、事前にビルドされたHTMLファイルから、ブラウザーで実行されます。

1. **新規アプリ** > **ブラウザのみ**を選択して、**サーバーレスPanelアプリを公開**ダイアログを開きます。
2. **アプリ名**と**バージョン**を入力します。
3. **アプリHTMLの場所**（ドキュメントアカウント内のHTMLファイル）を選択します。
4. **アプリURLスラッグ**と、任意の**メモ**を入力します。
5. **公開**をクリックします。WASMアプリにはビルドのステップがなく、すぐに提供されます。
