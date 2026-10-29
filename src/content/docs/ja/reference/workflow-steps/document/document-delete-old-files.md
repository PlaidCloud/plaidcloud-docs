---
title: Delete Old Filesステップ
description: ドキュメントアカウント内のファイルを、指定した期間より古いもの、または新しいものを対象に削除します。削除前にドライランの一覧で確認できます。
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## 説明

ドキュメントアカウント内のファイルを、経過期間に基づいて削除します。エクスポート用や受け取り用のフォルダーが際限なく大きくなるのを防ぐために使用します。たとえば、前日の抽出ファイルを削除したり、1年以上前のアーカイブを整理したりします。

## 設定

### 削除するファイル

- **ファイルパス** — 作業対象のドキュメントアカウントとフォルダーです。
- **期間** — 数値と単位（分、時間、日、月、年）です。
- **以前または以降** — 基準日時より**前**に最終更新されたファイル（通常の整理の向き）、または**後**に最終更新されたファイルを削除します。
- **再帰** — デフォルトではオフです。オンにするとサブフォルダーも対象になります。
- **テスト結果テーブル** — ステップエディターの**テスト**ボタンが、一致するファイルのプレビューを書き込むテーブルです。

<Aside type="caution" title="注意：プレビューにはテストを使用します。ステップの実行では確認できません">
  プレビューは、ステップの編集中に**テスト**ボタンから取得します。
  ワークフローでステップを実行すると、常に削除が行われます。ドライランモードはなく、
  テスト結果テーブルがあっても削除は回避されません。削除は元に戻せません。また、**再帰**がオンの状態でパスを間違えると、想定より広い範囲に影響します。
  スケジュールする前に、プレビューを確認してください。
</Aside>

## 関連項目

- [ドキュメントステップ](/ja/reference/workflow-steps/document/)
- [Delete Document Fileステップ](/ja/reference/workflow-steps/document/delete-document-file/)
- [ディレクトリ一覧](/ja/reference/workflow-steps/document/directory-listing/)
