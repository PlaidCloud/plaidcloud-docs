---
title: Panelアプリ
description: PlaidCloudで、インタラクティブなHoloViz Panelデータアプリケーションを構築してデプロイします。ブラウザー内で動作する静的なアプリも、gitリポジトリからビルドするサーバー側のアプリも利用できます。
sidebar:
  label: Panelアプリ
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Panelアプリを使うと、パラメーター化された入力、リアルタイムのチャート、埋め込みデータテーブルなどを備えたインタラクティブな[HoloViz Panel](https://panel.holoviz.org/)アプリケーションを、PlaidCloudから直接公開できます。アプリは**マイPanelアプリ**画面で管理します。この画面には、すべてのアプリが、ランタイム、ビルドステータス、URLとともに一覧表示されます。

ランタイムは2種類あり、**ランタイム**列に表示されます。

- **WASM** — ブラウザー内（Pyodide）だけで動作する静的なアプリです。ドキュメントアカウントから、ビルド済みのHTMLファイルを公開します。サーバープロセスはなく、スケールさせるものもありません。すぐに配信されます。
- **サーバー** — gitリポジトリからビルドされ、サーバー側で実行されるアプリです。公開すると、PlaidCloudがリポジトリをコンテナーにビルドします。コンテナーはレプリカ数ゼロで待機し、そのURLへの最初のリクエストで起動して、（ライブ更新を含めて）配信し、アイドル状態になるとゼロにスケールダウンします。Pythonランタイム、サーバー側の計算、ブラウザー内で実行できないライブラリが必要なアプリに適しています。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Panelアプリの2つのランタイム。WASMアプリは、サーバーなしでブラウザーに直接配信されるビルド済みのHTMLファイルです。サーバーアプリは、gitリポジトリからコンテナーにビルドされ、レプリカ数ゼロで待機し、最初のリクエストで約15秒かけて起動して配信し、アイドル状態になるとゼロにスケールダウンします。" style="width:100%;max-width:680px;height:auto;">
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
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">待機 · レプリカ0</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">何も実行されていない</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">最初のリクエスト</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">配信中</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">起動に約15秒</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">アイドル状態になると0にスケールダウン</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">2つのランタイム：<strong>WASM</strong>アプリはビルド済みのHTMLファイルをブラウザーに直接配信します。<strong>サーバー</strong>アプリはgitからビルドされ、ゼロで待機し、最初のリクエスト（約15秒）で起動して配信し、ゼロにスケールダウンします。</figcaption>
</figure>

## ランタイムを選ぶ

| | WASM | サーバー |
|---|---|---|
| ソース | 公開済みのHTMLファイル | gitリポジトリ（接続、ブランチ、エントリポイント） |
| 実行場所 | ブラウザー内 | サーバー側、ゼロへのスケールダウン |
| 適した用途 | 軽量で自己完結したダッシュボード | サーバーの計算能力や完全なPythonライブラリを必要とするアプリ |
| コールドスタート | なし | 最初のリクエストでアプリが起動（約15秒） |

## 次のステップ

- [PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/) — リポジトリから配信されるアプリまでの全体の流れを、認証情報が不要なマネージド接続で説明します。
- [Panel Studio](/ja/guides/panel-apps/studio/) — リポジトリを用意せずに、PlaidCloudでアプリの作成、編集、プレビュー、公開を行います。
- [WeaveでPanelアプリを構築する](/ja/guides/panel-apps/build-with-weave/) — アプリを説明し、Weaveが提案する変更の内容を正確に確認して承認します。
- [Panelアプリの作成](/ja/guides/panel-apps/creating/) — gitからサーバーアプリを、またはファイルからWASMアプリを公開します。
- [Panelアプリキット](/ja/guides/panel-apps/app-kit/) — PlaidCloudらしい外観で、ライトとダークの両方に対応し、フィルター、主要な数値、サーバー側でページ分割されるデータグリッド、チャート、フォーム、実行ボタン、保存済み設定、印刷を備えたアプリを構築します。
- [Panelアプリ向けData API](/ja/guides/panel-apps/data-api/) — サーバー側でテーブルのフィルター、ページ分割、カウント、集計を行います。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — 数値が上限を超えたときにプッシュ通知、メール、SlackまたはTeamsのメッセージを受け取ったり、スケジュール済みの要約を受け取ったりします。
- [アプリギャラリー](/ja/guides/panel-apps/gallery/) — アプリをテンプレートとして掲載し、掲載されたアプリから新しいアプリを作成します。
- [プロジェクトのブランディングとアプリのプロジェクト](/ja/guides/panel-apps/branding/) — プロジェクトのアプリに色とロゴを設定し、アプリをプロジェクトに割り当てます。
- [Panelアプリの使用](/ja/guides/panel-apps/using/) — ビルドステータス、アプリの開き方、編集、削除を説明します。
- [Panelアプリ内にAIエージェントを構築する](/ja/get-started/tutorials/panel-ai-agent/) — チュートリアル：閲覧者自身の権限の範囲で、REST APIをツールとしてAIエージェントに提供します。
