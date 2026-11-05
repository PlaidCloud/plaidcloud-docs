---
title: プロジェクト
description: PlaidCloudのプロジェクトを設定・管理し、ワークフロー、テーブル、データのインポート、その他の分析オブジェクトを目的別に整理します。
sidebar:
  label: プロジェクト
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

**プロジェクト**は、PlaidCloudにおける作業の単位です。各プロジェクトは、独自のデータ、ワークフロー、ディメンション、監査履歴を保持します。プロジェクト同士は状態を共有せず、分離されているため、個別の分析、業務プロセス、データプロダクトを分ける自然な境界になります。

多くのチームは、分析領域ごとに1つのプロジェクトから始めます。たとえば、人件費配賦用のプロジェクト、収益分析用のプロジェクト、月次決算用のプロジェクトなど、チームの仕事の捉え方に合わせたものです。

## このセクションの内容

- [プロジェクトの管理](/ja/guides/projects/managing-projects/) — ワークスペース内のプロジェクトを作成、構成、整理します
- [Data Foundation: Common Finance Model](/ja/guides/projects/data-foundation/) — 複数のERPシステムやインスタンスのERPデータを、直接接続を通じて1つのCommon Finance Modelに取り込みます。レポート、メトリック、AIアシスタントはすべてこのモデルを参照します
- [Data Foundationを始める](/ja/guides/projects/data-foundation-getting-started/) — 新しいプロジェクトから、ロード済み、チェック済み、引き渡し済みのモデルまでのセットアップチェックリスト
- [コスト・トゥ・サーブ](/ja/guides/projects/cost-to-serve/) — 営業費用をアクティビティ別に顧客へ配分し、顧客対応コスト控除後のマージンを確認します
- [オペレーショナル移転価格](/ja/guides/projects/operational-transfer-pricing/) — 各エンティティの利益水準をポリシーの範囲に照らしてテストし、true-upを確認します
- [プロジェクトの表示](/ja/guides/projects/viewing-projects/) — 既存のプロジェクトを検索して開きます
- [階層の管理](/ja/guides/projects/managing-hierarchies/) — 多数のプロジェクトを整理するためのフォルダー構造
- [テーブルとビューの管理](/ja/guides/projects/managing-tables-and-views/) — プロジェクト内のデータレイヤー
- [データエディターの管理](/ja/guides/projects/managing-data-editors/) — プロジェクトデータを変更できるユーザー
- [プロジェクトログの表示](/ja/guides/projects/viewing-the-project-log/) — 変更の監査証跡
- [プロジェクトのアーカイブ](/ja/guides/projects/archive-a-project/) — 完了した作業を削除せずに保存します
- [パンくずリストとリンク](/ja/guides/projects/breadcrumbs-and-shareable-links/) — どのウィンドウからでも上の階層に移動し、表示中の内容へのリンクを共有します
- [プロジェクトの比較とマージ](/ja/guides/projects/compare-and-merge-projects/) — 2つのプロジェクトの差分を確認し、変更を選択的にコピーします
- [ポータブル形式へのエクスポート](/ja/guides/projects/export-to-portable-format/) — プロジェクトを、プラットフォーム外で実行できるスタンドアロンのPython + DuckDBプログラムとしてパッケージ化します
- [ストレージの管理](/ja/guides/projects/managing-storage/) — ワークスペースが保存している内容を確認し、テーブルが履歴を保持する期間を設定します
- [ラベルで作業を整理する](/ja/guides/projects/organizing-with-labels/) — ワークフロー、ステップ、テーブル、その他のオブジェクトにタグを付けて、グループ化とフィルターを行います
- [リンクの共有](/ja/guides/projects/sharing-links/) — アドレスバーからリンクをコピーして、プロジェクト、ワークフロー、テーブル、ディメンションを直接開きます

## 関連項目

- [概念](/ja/get-started/concepts/) — プロジェクトがワークスペース、メンバー、より広範なデータモデルとどのように関係するか
- [ワークフロー](/ja/guides/workflows/) — プロジェクト内に存在する自動化の基本要素
- [アクセス管理](/ja/administration/access/) — プロジェクトを閲覧・編集できるユーザーを制御する、ワークスペースレベルの制御
