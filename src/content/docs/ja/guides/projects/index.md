---
title: プロジェクト
description: PlaidCloudのプロジェクトを設定・管理して、ワークフロー、テーブル、データのインポート、その他の分析オブジェクトを目的別に整理します。
sidebar:
  label: プロジェクト
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

**プロジェクト**は、PlaidCloudにおける作業の単位です。各プロジェクトは、独自のデータ、ワークフロー、ディメンション、監査履歴を保持します。プロジェクト同士は状態を共有せず、互いに分離されているため、個別の分析、業務プロセス、データプロダクトを分けるための自然な境界になります。

ほとんどのチームは、分析領域ごとに1つのプロジェクトから始めます。人員コストの配賦用、収益分析用、月次決算用など、チームの作業の捉え方に合わせたプロジェクトです。

## このセクションの内容

- [プロジェクトの管理](/ja/guides/projects/managing-projects/) — ワークスペースでプロジェクトを作成、構成、整理します
- [Data Foundation: Common Finance Model](/ja/guides/projects/data-foundation/) — 複数のERPシステムとインスタンスのERPデータを、それぞれの直接接続を通じて、レポート、メトリック、AIアシスタントのすべてが参照する1つのCommon Finance Modelに取り込みます
- [プロジェクトの表示](/ja/guides/projects/viewing-projects/) — 既存のプロジェクトを検索して開きます
- [階層の管理](/ja/guides/projects/managing-hierarchies/) — 多数のプロジェクトを整理するためのフォルダー構造
- [テーブルとビューの管理](/ja/guides/projects/managing-tables-and-views/) — プロジェクト内のデータレイヤー
- [データエディターの管理](/ja/guides/projects/managing-data-editors/) — プロジェクトデータを変更できるユーザー
- [プロジェクトログの表示](/ja/guides/projects/viewing-the-project-log/) — 変更の監査証跡
- [プロジェクトのアーカイブ](/ja/guides/projects/archive-a-project/) — 完了した作業を削除せずに保存します
- [パンくずリストとリンク](/ja/guides/projects/breadcrumbs-and-shareable-links/) — どのウィンドウからでも上の階層に移動し、表示中の内容へのリンクを共有します
- [プロジェクトの比較とマージ](/ja/guides/projects/compare-and-merge-projects/) — 2つのプロジェクトの差分を確認し、変更を選択的にコピーします
- [ポータブル形式へのエクスポート](/ja/guides/projects/export-to-portable-format/) — プロジェクトを、プラットフォーム外で実行できるスタンドアロンのPython + DuckDBプログラムとしてパッケージ化します
- [ストレージの管理](/ja/guides/projects/managing-storage/) — ワークスペースに保存されている内容を確認し、テーブルが履歴を保持する期間を設定します
- [ラベルによる作業の整理](/ja/guides/projects/organizing-with-labels/) — ワークフロー、ステップ、テーブルなどのオブジェクトにタグを付けて、グループ化とフィルターを行います
- [リンクの共有](/ja/guides/projects/sharing-links/) — アドレスバーからリンクをコピーして、プロジェクト、ワークフロー、テーブル、ディメンションを直接開きます

## 関連情報

- [コンセプト](/ja/get-started/concepts/) — プロジェクトとワークスペース、メンバー、より広範なデータモデルとの関係
- [ワークフロー](/ja/guides/workflows/) — プロジェクト内に存在する自動化の基本要素
- [アクセス管理](/ja/administration/access/) — プロジェクトを表示・編集できるユーザーを制御するワークスペースレベルの設定
