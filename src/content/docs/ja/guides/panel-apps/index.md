---
title: Panelアプリ
description: インタラクティブなHoloViz Panelデータアプリケーションを、PlaidCloudで構築してデプロイします。静的なブラウザー内アプリとしても、gitリポジトリから構築されるサーバーサイドのアプリとしても利用できます。
sidebar:
  label: Panelアプリ
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Panelアプリを使用すると、パラメーター化された入力、ライブチャート、埋め込みのデータテーブルを備えた、インタラクティブな[HoloViz Panel](https://panel.holoviz.org/)アプリケーションを、PlaidCloudから直接公開できます。**アプリ**画面で管理します。この画面には、すべてのアプリが、そのランタイム、ビルドのステータス、URLとともに一覧表示されます。

[Panel Studio](/ja/guides/panel-apps/studio/)から始めてください。**新規アプリ** > **Studio**を選択すると、リポジトリを設定することなく、PlaidCloudで、空のアプリ、テーブル、ビュー、ギャラリーからアプリを構築できます。独自の要件がある場合は、**ランタイム**列に表示される、次のランタイムのいずれかで公開します。

- **WASM** — ブラウザー内で完全に実行される静的アプリです。ドキュメントアカウントから、事前にビルドされたHTMLファイルを公開します。サーバープロセスはなく、スケールするものもありません。すぐに提供されます。
- **サーバー** — gitリポジトリから構築され、サーバーサイドで実行されるアプリです。公開すると、PlaidCloudがリポジトリをコンテナーにビルドします。コンテナーはレプリカ数ゼロでアイドル状態になり、そのURLへの最初のリクエストで起動し、（ライブ更新を含めて）提供を行い、アイドル状態になるとゼロにスケールバックします。Pythonランタイム、サーバーサイドの計算、ブラウザーでは実行できないライブラリが必要なアプリに適しています。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Panelアプリの2つのランタイム。WASMアプリは、事前にビルドされたHTMLファイルで、サーバーなしでブラウザーに直接提供されます。サーバーアプリは、gitリポジトリからコンテナーにビルドされ、レプリカ数ゼロでアイドル状態になり、最初のリクエストで約15秒で起動し、提供を行い、アイドル状態になるとゼロにスケールバックします。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ビルド済みHTMLファイル</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">ブラウザー · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">すぐに提供</text>
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
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">何も実行されていない</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">最初のリクエスト</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">提供中</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">起動に約15秒</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">アイドル時は0にスケールバック</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">2つのランタイム。<strong>WASM</strong>アプリは、事前にビルドされたHTMLファイルをブラウザーに直接提供します。<strong>サーバー</strong>アプリは、gitからビルドされ、ゼロでアイドル状態になり、最初のリクエスト（約15秒）で起動し、提供を行い、ゼロにスケールバックします。</figcaption>
</figure>

## ランタイムの選択

| | WASM | サーバー |
|---|---|---|
| ソース | 公開されたHTMLファイル | gitリポジトリ（接続、ブランチ、エントリポイント） |
| 実行場所 | ブラウザー内 | サーバーサイド、ゼロへのスケール |
| 適した用途 | 軽量で自己完結型のダッシュボード | サーバーでの計算や、完全なPythonライブラリが必要なアプリ |
| コールドスタート | なし | 最初のリクエストでアプリが起動（約15秒） |

## 次のステップ

- [Panel Studio](/ja/guides/panel-apps/studio/) — リポジトリを設定することなく、PlaidCloudでアプリを作成、編集、プレビュー、公開します。
- [PlaidCloud GitからのPanelアプリのデプロイ](/ja/guides/panel-apps/deploy-from-git/) — 認証情報不要の管理対象接続を使用して、リポジトリから提供されるアプリまでの一連の流れを説明します。
- [WeaveによるPanelアプリの構築](/ja/guides/panel-apps/build-with-weave/) — アプリを説明し、Weaveが提案する変更を正確に承認します。
- [Panelアプリの作成](/ja/guides/panel-apps/creating/) — 空のアプリ、テーブル、ギャラリーからStudioアプリを開始するか、gitからサーバーアプリ、ファイルからWASMアプリを公開します。
- [Panelアプリキット](/ja/guides/panel-apps/app-kit/) — フィルター、主要な数値、サーバーでページ分割されるデータグリッド、チャート、フォーム、実行ボタン、保存された設定、印刷を備えた、ライトとダークのPlaidCloudのような見た目のアプリを構築します。
- [Panelアプリ向けのData API](/ja/guides/panel-apps/data-api/) — サーバー上で、テーブルのフィルター、ページ送り、カウント、集計を行います。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — 数値が上限を超えたときに、プッシュ通知、メール、Slack、Teamsのメッセージを受け取るか、定期サマリーを受け取ります。
- [アプリギャラリー](/ja/guides/panel-apps/gallery/) — アプリをテンプレートとして掲載し、掲載されたアプリから新しいアプリを作成します。
- [プロジェクトのブランディングとアプリプロジェクト](/ja/guides/panel-apps/branding/) — プロジェクトのアプリに色とロゴを設定し、アプリをプロジェクトに割り当てます。
- [Panelアプリの使い方](/ja/guides/panel-apps/using/) — ビルドのステータス、アプリを開く、編集、削除。
- [Panelアプリ内でAIエージェントを構築する](/ja/get-started/tutorials/panel-ai-agent/) — チュートリアル：閲覧者自身の権限の範囲で、REST APIをツールとしてAIエージェントに与えます。
