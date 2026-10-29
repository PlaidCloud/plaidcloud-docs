---
title: Panel Studio
description: PlaidCloudを離れずに、Panelアプリの作成、編集、プレビュー、公開を行います。さらに、以前のバージョンの復元、アプリの利用状況と速度の確認、アラートとダイジェストの設定、ギャラリーへの掲載、ホームへのピン留めも可能です。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studioは、PlaidCloud内でPanelアプリを編集するためのエディターです。アプリのファイルをエディターの横に表示し、開ける非公開のプレビューをビルドして、準備ができたらアプリを公開します。始めるのにgitリポジトリは必要ありません。

## Panel Studioを開く

- プロジェクトの**ホーム**ボードで、Panelアプリの**Open in Studio**を選択します。
- **マイPanelアプリ**で、アプリの行にある**Open in Studio**を選択します。

新しいアプリを始めるには、どちらの場所でも**Create app**を選択します。

## アプリを作成する

**Create app**ダイアログでは、次の5つの出発点から選べます。

| 開始元 | 作成されるもの |
|---|---|
| **Blank** | `app.py`と`requirements.txt`を持つ最小限のアプリ。 |
| **テーブル** | 選択したテーブルをもとに構築されたアプリ。 |
| **ビュー** | プロジェクトのビューをもとに構築された、同様のアプリ。 |
| **テンプレート** | [Panelアプリキット](/ja/guides/panel-apps/app-kit/#テンプレートから始める)のすぐに使えるアプリ。 |
| **From the gallery** | ワークスペースが[アプリギャラリー](/ja/guides/panel-apps/gallery/)に掲載したアプリのコピー。 |

アプリに名前を付け、**プロジェクト**を選んで、**作成**を選択します。Studioが新しいアプリを開き、左側にそのファイルが一覧表示されます。

## 編集

リストからファイルを選ぶと、エディターで編集できます。Pythonの依存関係は、1行に1パッケージずつ`requirements.txt`に記載します。依存関係は、アプリのビルド時にインストールされます。

**Ask Weave**を選択すると、Weaveにアプリの作成や変更を任せられます。[WeaveでPanelアプリを構築する](/ja/guides/panel-apps/build-with-weave/)を参照してください。

## 保存、プレビュー、公開

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="保存すると、自分だけが見られるドラフトが保持されます。プレビューは、エディター用にドラフトの非公開コピーをビルドします。公開は、確認の後でライブのアプリを置き換えます。" style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">保存</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">ドラフトのみ</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">プレビュー</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">エディターのみ</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">公開</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">ライブのアプリ</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">編集内容が閲覧者に届くのは、公開したときだけです。</figcaption>
</figure>

### 保存

**保存**すると、変更内容がドラフトとして保存されます。ライブのアプリは変更されず、他のユーザーにドラフトが見えることもありません。

### プレビュー

**プレビュー**は、保存したドラフトを非公開のコピーとしてビルドし、開きます。プレビューを開けるのは、アプリの編集者だけです。

- プレビューは、保存しないまま24時間が経過すると削除されます。
- ワークスペースで同時に持てるプレビューは、最大10個です。
- 最新の編集内容を確認するには、もう一度保存して**プレビュー**を選択します。

### 公開

**公開**すると、ライブのアプリが保存したドラフトに置き換えられます。アプリのプロジェクトに対する編集権限が必要で、Studioはまず確認を求めます。

アプリを開いた後に他のユーザーが変更を公開した場合、Studioはその作業を上書きせずに、競合を報告します。アプリを再読み込みし、自分の編集内容を取り込んで、もう一度公開してください。

## ビルドステータスとエラー

**ビルド**タブには、最新のビルドのステータスが表示され、実行中は更新されます。ビルドが失敗すると、タブに各エラーがファイル名と行番号とともに一覧表示されるため、その行に直接移動できます。`requirements.txt`の依存関係の問題には、修正方法のヒントが付きます。

エラーと警告は、エディター内の該当する行にもマークされるため、問題をその場所で確認できます。

アプリの公開後の各ステータスの意味については、[Panelアプリの使用](/ja/guides/panel-apps/using/#ビルドステータスサーバーアプリ)を参照してください。

## 履歴と復元

**履歴**タブには、アプリの公開済みのバージョンがすべて、新しいものから順に、ビルドステータスとともに一覧表示されます。古いものを表示するには、**さらに読み込む**を選択します。

以前のバージョンに戻すには、そのバージョンで**復元**を選択して確認します。復元したバージョンがライブのアプリになり、再ビルドされます。未保存のドラフトは失われません。ドラフトとして残り、次に公開するときに、復元したバージョンの上に重ねて反映されます。アプリがすでにそのバージョンと一致している場合、Studioはその旨を表示し、何も変更しません。復元中に他のユーザーが公開した場合、Studioは何も復元せず、もう一度試すよう求めます。

## インサイト

**インサイト**タブには、ユーザーがアプリをどのように使っているか、アプリの応答がどのくらい速いかが表示されます。過去7日、14日、30日から選択します。

| セクション | 表示内容 |
|---|---|
| **Views per day** | 毎日アプリが開かれた回数。 |
| **Page load** | 対象期間のページ読み込みから算出した、読み込み時間の中央値と、読み込みの95パーセントがそれより速く完了する時間。 |
| **Slowest queries** | 最も時間がかかったクエリ。実行された頻度と、その中央値、遅い側の値、最も遅い値が付きます。 |
| **エラー** | 対象期間に発生した問題。エラーの種類と、アプリ内での発生場所別。 |

対象期間の活動量がインサイトで読み取れる量を超えている場合は、数値が部分的であることが示されます。ページ読み込みがアプリの[パフォーマンスの上限](/ja/guides/panel-apps/app-kit/#パフォーマンスバジェット)を超えると、インサイトは、その件数と、遅かったクエリを警告します。インサイトに、クエリが返したデータや、アプリを開いたユーザーの名前が表示されることはありません。

2つのタブはどちらも、アプリがプロジェクトに割り当てられている必要があります。未割り当てのアプリには、割り当てを促すメッセージが表示されます。

## アラートとダイジェスト

**Alerts & Digests**を選択すると、アプリのデータの数値を監視して上限を超えたときに通知する設定や、スケジュールに沿って要約を送信する設定ができます。[アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/)を参照してください。

## アプリをギャラリーに掲載する

**Gallery…** を選択すると、プロジェクトを閲覧できるユーザーなら誰でもそこから自分のアプリを作成できるテンプレートとしてアプリを掲載したり、ギャラリーから削除したりできます。[アプリギャラリー](/ja/guides/panel-apps/gallery/)を参照してください。

## ホームにピン留めする

**Pin to Home**を選択すると、アプリがプロジェクトの**ホーム**ボードに追加されます。**Unpin from Home**を選択すると削除されます。

## アプリを削除する

Panelアプリを削除する前には、確認が求められます。**マイPanelアプリ**で、アプリの行にある**マイナス**アイコンを使用します。公開の取り消しでも確認が求められます。

## 次のステップ

- [WeaveでPanelアプリを構築する](/ja/guides/panel-apps/build-with-weave/) — アプリを説明し、変更の内容を正確に承認します。
- [Panelアプリキット](/ja/guides/panel-apps/app-kit/) — Studioのテーブル、ビュー、テンプレートからの開始で使われるコンポーネントです。
- [アラートとダイジェスト](/ja/guides/panel-apps/alerts-and-digests/) — 数値が上限を超えたとき、またはスケジュールに沿って、ユーザーに通知します。
- [アプリギャラリー](/ja/guides/panel-apps/gallery/) — アプリを他のユーザーの出発点として共有します。
- [Panelアプリの使用](/ja/guides/panel-apps/using/) — 公開後のログ、利用状況、再ビルドを説明します。
