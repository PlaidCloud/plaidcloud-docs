---
title: Panelアプリを作成する
description: サーバーサイドのHoloViz PanelアプリをGitリポジトリから公開する方法（Hello Worldの例付き）と、静的なWASMアプリをファイルから公開する方法を、PlaidCloudで説明します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

**マイPanelアプリ**を開きます。ツールバーには、[ランタイム](/ja/guides/panel-apps/)ごとに1つずつ、公開方法が2つ用意されています。

- **新しいサーバーアプリ** — Gitリポジトリからアプリをビルドして実行します。
- **WASMアプリを追加** — 静的なブラウザー内アプリをファイルから公開します。

リポジトリを用意せずにPlaidCloudの中でアプリを作成するには、[Panel Studio](/ja/guides/panel-apps/studio/)を使用してください。

## サーバーアプリを作成する

サーバーアプリはGitリポジトリからビルドされ、`https://<your-tenant-host>/serve/<slug>/` で提供されます。PlaidCloudにリポジトリのブランチを指定すると、コードがコンテナーにビルドされ、その上で `panel serve` が実行されます。そのブランチにプッシュするたびに、自動的に再ビルドされます。

### アプリのリポジトリを準備する

リポジトリには2つのものが必要です。**エントリポイント**（Panelアプリを構築して `.servable()` を付けるPythonファイル）と、必要に応じて、追加のパッケージを列挙した **`requirements.txt`** です。後者は、リポジトリのルートまたはエントリポイントの隣に置きます。

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

`app.py` を作成します。

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

これで完全なアプリです。PlaidCloudが提供するのは `.servable()` の呼び出しです。表示したいものはすべて、servableとしてマークする必要があります（直接指定するか、servableなレイアウトの内部に置きます）。

#### もう少し充実した例

Panelアプリはインタラクティブです。次の例では、テーブルをリアルタイムで更新するスライダーを追加します。

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

この2番目の例は、ベースイメージに含まれていない `pandas` をインポートしているため、`requirements.txt` を追加します（リポジトリのルート、またはエントリポイントの隣）。

```text
pandas
```

PlaidCloudは、イメージのビルド時に `pip` でこれらをインストールします。`plotly`、`holoviews`、`hvplot` などの一般的な可視化ライブラリもベースイメージには含まれていないため、アプリがインポートするものはここに列挙してください。

> **プラットフォームが提供するもの、そして想定するもの。** アプリを作成するときは、次の前提を念頭に置いてください。
>
> - **`panel` と `bokeh` は、プラットフォームのベースイメージにプリインストールされています。** これらを `requirements.txt` に記載しないでください。また、古いPanelバージョンへの固定は避けてください。ライブ更新の再接続は、比較的新しいバージョンに依存しています。
> - **PlaidCloudクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされています。** `plaidcloud.rpc` または `plaidcloud.utilities` を直接インポートしてください。`requirements.txt` には記載しないでください。
> - **`requirements.txt` は、リポジトリのルートまたはエントリポイントの隣に置けます。** 共有（モノレポ）リポジトリでは、各アプリの依存関係をそのアプリ自身のフォルダーに置いてください。ルートレベルのファイルがある場合は、それもインストールされます。共有の依存関係はそこに、アプリ固有のものはアプリの隣に置きます。
> - **アプリは、読み取り専用のファイルシステム上で、非rootユーザーとして実行されます。** 書き込み可能なのは `/tmp` だけなので、一時ファイルはそこに書き込んでください（ほとんどのライブラリはすでに `$TMPDIR` を尊重します）。
> - **ポート、URLプレフィックス、ホストをハードコードしないでください。** これらはPlaidCloudが割り当て、デプロイ時に注入します。`.servable()` を呼び出すだけで十分です。

PlaidCloudの外観と、すぐに使えるフィルター、グリッド、チャートを利用するには、[Panelアプリキット](/ja/guides/panel-apps/app-kit/)でアプリを構築してください。

### テーマを設定する: ライト、ダーク、または切り替え

サーバーアプリは、デフォルトでPlaidCloudのモダンな **Fast** デザイン（プラットフォーム全体に適用される、すっきりしたFluent風の外観）で表示されます。公開ダイアログでは、**デザイン**がそのプラットフォーム層を制御します。

- **FAST** — PlaidCloudのデフォルトです。新しいアプリや、Fastテンプレートで構築したアプリに使用します。
- **デフォルト** — Panelのデフォルトのスタイルです。既存アプリのCSSや見た目がFASTで崩れる場合に使用します。

アプリのコードで制御するのは、**テーマ**（ライト、ダーク、または閲覧者が切り替えられるスイッチ）です。

テーマは、提供する**テンプレート**のプロパティです。Fastテンプレートの `FastListTemplate`（1列）と `FastGridTemplate`（レスポンシブなグリッド）には、そのための設定が2つあります。

- **`theme`** — ライトの場合は `"default"`、ダークの場合は `"dark"` です。設定すると、閲覧者がURLに `?theme=dark` を追加しても、アプリはそのテーマに固定されます。
- **`theme_toggle`** — `True` にするとヘッダーにライト/ダークのスイッチが表示され、`False` にすると非表示になります。デフォルトは `True` です。スイッチを非表示にしても、それだけではテーマは固定されません。上記の `theme` で固定し、そのうえで `theme_toggle=False` を設定すると、何も変更できないスイッチが閲覧者に表示されずに済みます。

アプリに合ったパターンを選んでください。

**ライトのみ** — 通常は明るい背景向けに手作業でスタイルを設定する、密度の高いレポートや財務テーブルに最適です。

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

**閲覧者に選ばせる** — デフォルトはライトで、ヘッダーにスイッチが表示されます。`theme` を省略すると、切り替えに追従します。

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **ダークを許可する場合は、テーブルもダークに対応させてください。** ライトのテーブルテーマに固定された `Tabulator`（`theme="bootstrap"`）や、`background: #fff` のようにライトの色をハードコードしたカスタムCSSは、ダークのページ上では読めない白いブロックとして表示されます。`pn.widgets.Tabulator(..., theme="fast")` のように、アプリに追従するテーブルテーマを使用し、ライトの色のハードコードは避けてください。ライト向けに手作業でスタイルを設定したレポートの場合は、代わりにライトに固定してください（上の最初のパターン）。

テンプレートのないシンプルなアプリ、つまり `pn.Column(...).servable()` は、Panelのデフォルトに従い、これらの設定の影響を受けません。明示的に制御したい場合は、テンプレートを使用してください。

リポジトリは、PlaidCloudの **Git接続**を通じて到達可能である必要があります。コードが[PlaidCloud Git](/ja/guides/git/)にある場合は、**Tools > Connections** で、マネージドの **PlaidCloud Git** 接続を作成してください。サーバーのURLや認証情報は不要です。空のリポジトリから提供中のアプリまでの全体の手順については、[PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/)を参照してください。

### アプリを公開する

1. **新しいサーバーアプリ**をクリックして、**サーバーPanelアプリを公開**ダイアログを開きます。設定はセクションごとにまとめられています。
2. **ディレクトリ設定**で、次の項目を設定します。
   - **アプリ名** — 一覧に表示される表示名。
   - **URLスラッグ** — アプリのURLと内部名の両方になるため、有効なDNSラベルである必要があります。小文字の英字、数字、ハイフンを使用し、英字で始まり、40文字以内にします（例: `sales-dashboard`）。ダイアログは公開前にこれを確認します。
   - **メモ** — 任意の説明。
   - **プロジェクト** — アプリを所有するプロジェクト。アプリの[ブランディング](/ja/guides/panel-apps/branding/)を提供し、アプリのテーブルのデフォルトのプロジェクトになります。公開後にここで変更することはできません。[割り当て](/ja/guides/panel-apps/branding/#既存のアプリの場合)を使用してください。
3. **Git接続と公開ウォッチャー**で、次の項目を設定します。
   - **Git接続** — アプリのリポジトリを保持している接続。
   - **ブランチ** — ビルド元のブランチ。このブランチへのプッシュにより、アプリが自動的に再ビルドされ、再デプロイされます。
   - **エントリポイント** — Panelが提供する `.py` ファイル（`app.py`）。
4. **ランタイム**で、次の項目を設定します。
   - アプリのコンテナーが要求する **CPU** と **メモリ**。

     > リソース（CPU/メモリ）を少なくすると、アプリのスケジューリングとコールドスタートが速くなります。

   - **デザイン** — PlaidCloudのモダンなデザインには **FAST** を、アプリのCSSがPanelのデフォルトのスタイルを前提としている場合は **デフォルト** を選択します。
   - **アイドル (分)** — トラフィックがない状態で、アプリがウォーム状態を保ち、その後ゼロにスケールダウンするまでの時間。デフォルトは5分です。
   - **パブリックアクセスを許可** — 認証なしのアクセスを許可する場合にチェックします。チェックしない場合、閲覧者はテナントにサインインする必要があります。
5. **詳細 (埋め込み配信)** — 省略可能です。デフォルトでは、アプリはPlaidCloudテナントからのみ提供されます。別のサイトに埋め込むには、**ドメインを追加**をクリックし、読み込みを許可する各ドメインを1行に1つずつ入力します。入力するのはホストだけで、スキームやパスは含めません（例: `example.com` または `app.example.com:8443`）。アプリを別の場所に埋め込む場合を除き、リストは空のままにしてください。
6. **公開**をクリックします。

公開後、アプリは**ビルド**されます。その**ステータス**は一覧に表示され、自動的に更新されます。ステータスの意味、準備ができたアプリの開き方、公開を取り消さずに再ビルドを実行する方法については、[Panelアプリを使用する](/ja/guides/panel-apps/using/)を参照してください。

> アプリのURLは、ビルドのステータスが**準備完了**になって初めて機能します。アイドル状態の後の最初のリクエストでは、アプリが起動します（約15秒）。

### 詳細: PlaidCloudをローカルで再現する

技術に詳しいユーザーは、PlaidCloudが使用するのと同じ入力でアプリをビルドしてテストできます。これは、公開前や**再ビルド**をクリックする前に行える、最も近いローカルでの確認です。

PlaidCloudは、選択したGitブランチから、次の生成されたDockerfileでビルドします。ローカルでも同じ内容を `Dockerfile.plaidcloud-panel` として使用してください。

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

サーバーのビルドに合わせるには、次の手順を実行します。

1. **ブランチ**で選択したのと同じブランチをチェックアウトします。
2. `COPY . /app` がPlaidCloudと一致するように、リポジトリのルートからビルドを実行します。
3. 任意の依存関係を `requirements.txt` に記載します。置き場所は、リポジトリのルートまたはエントリポイントの隣です。両方がインストールされ、アプリのフォルダーのものが最後にインストールされます（アプリごとの固定が優先されます）。
4. **エントリポイント**で選択したのと同じエントリポイントのパスを使用します。

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

デプロイされるイメージは、ベースイメージのエントリポイントを上書きしません。PlaidCloudが注入する環境変数から `panel serve` を実行します。ビルドしたイメージは、同じランタイム契約でテストしてください。

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

`http://localhost:5006/serve/local/` を開きます。

テストするときは、公開ダイアログの設定に合わせます。

- **エントリポイント**は `APP_PATH=/app/<entry-point>` に対応します。
- **CPU**と**メモリ**は、Dockerの `--cpus` と `--memory` の制限に対応します。
- **デザイン: FAST** は `PLAID_PANEL_DESIGN=fast` に対応します。
- **デザイン: デフォルト**は、`PLAID_PANEL_DESIGN` を省略することを意味します。
- **アイドル (分)** は、デプロイ環境でのスケールダウンの時間枠に対応します。ローカルのDockerでは適用されませんが、アプリは引き続き同じPanelのWebSocketキープアライブとセッションクリーンアップの設定を使用します。
- **埋め込み配信**のドメインは `PANEL_ORIGIN` に対応します。複数のホストをテストする必要がある場合は、スペース区切りのリストを使用します。

コンテナーが不要な場合でも、ローカルのPython環境からサーブ層をテストできます。同じ `requirements.txt` をインストールし、プラットフォームの環境変数を設定してから、デプロイされるイメージと同じフラグで `panel serve` を実行します。

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

`http://localhost:5006/serve/local/` を開きます。

デフォルトのデプロイ時の外観に合わせるには、`PLAID_PANEL_DESIGN=fast` を使用します。公開ダイアログの**デフォルト**デザインのオプションをテストするには、`PLAID_PANEL_DESIGN` を未設定のままにして、同じコマンドを実行します。`PANEL_PREFIX`、`PANEL_ORIGIN`、`--keep-alive`、`--unused-session-lifetime` はそのままにしてください。これらはデプロイされるランタイム契約の一部です。

## WASMアプリを作成する

WASMアプリは、ビルド済みのHTMLファイルからブラウザー内で実行されます。

1. **WASMアプリを追加**をクリックして、**サーバーレスPanelアプリを公開**ダイアログを開きます。
2. **アプリ名**と**バージョン**を入力します。
3. **アプリHTMLの場所**（ドキュメントアカウント内のHTMLファイル）を選択します。
4. **アプリURLスラッグ**と、任意で**メモ**を入力します。
5. **公開**をクリックします。WASMアプリにはビルドの手順がなく、すぐに提供されます。
