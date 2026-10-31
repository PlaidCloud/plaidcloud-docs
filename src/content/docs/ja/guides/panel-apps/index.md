---
title: Panelアプリ
description: インタラクティブなHoloViz PanelデータアプリケーションをPlaidCloudで作成してデプロイします。静的なブラウザー内アプリとしても、gitリポジトリからビルドするサーバーサイドのアプリとしても利用できます。
sidebar:
  label: Panelアプリ
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Panelアプリを使うと、パラメーター化された入力、ライブチャート、埋め込みデータテーブルを備えたインタラクティブな[HoloViz Panel](https://panel.holoviz.org/)アプリケーションを、PlaidCloudから直接公開できます。アプリは**マイPanelアプリ**画面で管理します。この画面には、すべてのアプリが、ランタイム、ビルドステータス、URLとともに一覧表示されます。

まず[Panel Studio](/ja/guides/panel-apps/studio/)から始めてください。**新しい Studio アプリ**を選択すると、リポジトリをセットアップすることなく、空のアプリ、テーブル、ビュー、ギャラリーのいずれかを元に、PlaidCloud上でアプリを作成できます。独自の要件がある場合は、**ランタイム**列に表示される次のランタイムのいずれかで公開します。

- **WASM** — ブラウザー（Pyodide）内だけで実行される静的なアプリです。ドキュメントアカウントにあるビルド済みのHTMLファイルを公開します。サーバープロセスはなく、スケールさせるものもありません。すぐに配信されます。
- **サーバー** — gitリポジトリからビルドされ、サーバーサイドで実行されるアプリです。公開すると、PlaidCloudはリポジトリをコンテナーにビルドします。コンテナーはレプリカ0でアイドル状態になり、URLへの最初のリクエストで起動して（ライブ更新を含めて）配信し、アイドルになると再びゼロにスケールダウンします。Pythonランタイム、サーバーサイドの計算、ブラウザーで実行できないライブラリが必要なアプリに適しています。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Panelアプリの2つのランタイム。WASMアプリは、ビルド済みのHTMLファイルがサーバーなしでブラウザーに直接配信されます。サーバーアプリは、gitリポジトリからコンテナーにビルドされ、レプリカ0でアイドル状態になり、最初のリクエストで約15秒で起動して配信し、アイドルになるとゼロにスケールダウンします。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ビルド済みHTMLファイル</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ブラウザー · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">すぐに配信</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">サーバー</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">gitリポジトリ</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">コンテナーをビルド</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">アイドル · レプリカ0</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">実行なし</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">最初のリクエスト</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">配信中</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">起動に約15秒</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">アイドルになると0にスケールダウン</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">2つのランタイム: <strong>WASM</strong>アプリはビルド済みのHTMLファイルがブラウザーに直接配信されます。<strong>サーバー</strong>アプリはgitからビルドされ、ゼロでアイドル状態になり、最初のリクエストで起動し（約15秒）、配信し、再びゼロにスケールダウンします。</figcaption>
</figure>

## ランタイムの選択

| | WASM | サーバー |
|---|---|---|
| ソース | 公開されたHTMLファイル | gitリポジトリ（接続、ブランチ、エントリポイント） |
| 実行場所 | ブラウザー内 | サーバーサイド、ゼロへのスケールダウン |
| 適した用途 | 軽量で自己完結したダッシュボード | サーバーでの計算や完全なPythonライブラリが必要なアプリ |
| コールドスタート | なし | 最初のリクエストでアプリが起動（約15秒） |

## 次のステップ

- [Panel Studio](/ja/guides/panel-apps/studio/) — リポジトリをセットアップせずに、PlaidCloudでアプリを作成、編集、プレビュー、公開します。
- [PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/) — 認証情報不要の管理対象接続を使って、リポジトリから配信されるアプリまでを一通り説明します。
- [WeaveでPanelアプリを作成する](/ja/guides/panel-apps/build-with-weave/) — アプリの内容を説明し、Weaveが提案する具体的な変更を承認します。
- [Panelアプリの作成](/ja/guides/panel-apps/creating/) — 空のアプリ、テーブル、ギャラリーからStudioアプリを開始するか、gitからサーバーアプリを、ファイルからWASMアプリを公開します。
- [Panelアプリキット](/ja/guides/panel-apps/app-kit/) — ライトとダークの両方で、フィルター、見出しの数値、サーバーページング対応のデータグリッド、チャート、フォーム、実行ボタン、保存済み設定、印刷を備えた、PlaidCloudの外観のアプリを作成します。
- [Panelアプリ向けData API](/ja/guides/panel-apps/data-api/) — サーバー上でテーブルをフィルター、ページング、カウント、集計します。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — 数値が上限を超えたときにプッシュ通知、メール、SlackまたはTeamsのメッセージを受け取ったり、定期サマリーを受け取ったりします。
- [アプリギャラリー](/ja/guides/panel-apps/gallery/) — アプリをテンプレートとして掲載し、掲載されたアプリから新しいアプリを作成します。
- [プロジェクトのブランディングとアプリプロジェクト](/ja/guides/panel-apps/branding/) — プロジェクトのアプリに色とロゴを設定し、アプリをプロジェクトに割り当てます。
- [Panelアプリの使用](/ja/guides/panel-apps/using/) — ビルドステータス、アプリを開く、編集、削除について説明します。
- [Panelアプリ内にAIエージェントを構築する](/ja/get-started/tutorials/panel-ai-agent/) — チュートリアル: AIエージェントにREST APIをツールとして与え、閲覧者自身の権限の範囲に限定します。
