---
title: WeaveでPanelアプリを構築する
description: 作りたいアプリを説明すると、WeaveがPanel Studioでそれを作成します。何かが保存される前に、変更の内容を正確に確認して承認できます。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weaveは、Panelアプリの作成や変更を代行できます。[Panel Studio](/ja/guides/panel-apps/studio/)で、開いているアプリに対して作業し、Weaveが提案した内容は、承認するまでアプリを変更しません。

## Weaveに依頼する

1. Panel Studioでアプリを開きます。
2. **Ask Weave**を選択し、希望する内容を説明します。たとえば「地域フィルターと、月別の売上のチャートを追加してください」のように入力します。

Weaveは、作業中のアプリについてすでに把握しています。アプリのファイル、ビルドの状況とビルドエラー、元になっているテーブルまたはビューです。コードやエラーを会話に貼り付ける必要はありません。ビルドが失敗した場合は、Weaveに修正を依頼してください。

## 変更を承認する

Weaveがアプリのコードを変更しようとすると、承認カードに完全な差分が表示されます。追加される行と削除される行が、ファイルごとにすべて示されます。

1. 差分を読みます。
2. **承認**を選択すると変更がアプリのドラフトに保存されます。**却下**を選択すると破棄されます。

承認するとドラフトが保存されます。公開はされません。結果をプレビューし、問題なければ[公開](/ja/guides/panel-apps/studio/#公開)します。

### 承認はWebのみ

コードの変更を承認できるのは、Web版のPlaidCloudだけです。PlaidCloudモバイルアプリでは、提案されたコードの変更を却下できますが、承認はできません。Weaveのその他の変更は、引き続きスマートフォンで承認できます。[モバイルでのWeave](/ja/guides/mobile-app/weave-on-mobile/)を参照してください。

## 次のステップ

- [Panel Studio](/ja/guides/panel-apps/studio/) — 保存、プレビュー、公開を行います。
- [Panelアプリキット](/ja/guides/panel-apps/app-kit/) — Weaveが構築に使うコンポーネントです。
