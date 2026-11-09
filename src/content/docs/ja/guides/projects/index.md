---
title: プロジェクト
description: PlaidCloudのプロジェクトを設定・管理し、ワークフロー、テーブル、データのインポート、その他の分析オブジェクトを目的別に整理します。
sidebar:
  label: プロジェクト
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

**プロジェクト**は、PlaidCloudにおける作業の単位です。各プロジェクトは、独自のデータ、ワークフロー、ディメンション、監査履歴を保持します。プロジェクト同士は状態を共有せず、互いに分離されているため、個別の分析、業務プロセス、データプロダクトを切り分ける自然な境界になります。

多くのチームは、分析領域ごとに1つのプロジェクトから始めます。たとえば、人件費配賦用のプロジェクト、収益分析用のプロジェクト、月次決算用のプロジェクトなど、チームの仕事の捉え方に合わせて分けます。

## このセクションの内容

- [プロジェクトを管理する](/ja/guides/projects/managing-projects/) — ワークスペース内のプロジェクトの作成、設定、整理
- [Data Foundation: Common Finance Model](/ja/guides/projects/data-foundation/) — 複数のERPシステムやインスタンスのERPデータを直接接続経由で1つのCommon Finance Modelに取り込み、レポート、メトリック、AIアシスタントのすべてがそのモデルを参照
- [Data Foundationを始める](/ja/guides/projects/data-foundation-getting-started/) — 新規プロジェクトから、読み込み・チェック・引き渡しが済んだモデルまでのセットアップチェックリスト
- [Cost to Serve](/ja/guides/projects/cost-to-serve/) — 営業費用を活動別に顧客へ配分し、顧客対応コストを差し引いた後のマージンを確認
- [Operational Transfer Pricing](/ja/guides/projects/operational-transfer-pricing/) — 各エンティティの利益水準をポリシーの範囲と照らして検証し、真の調整額を確認
- [プロジェクトホーム](/ja/guides/projects/project-home/) — プロジェクトの概要を一目で確認し、変数、スケジュール、アクセス、データのデフォルト、アプリを管理
- [プロジェクトを表示する](/ja/guides/projects/viewing-projects/) — 既存のプロジェクトの検索と表示
- [階層を管理する](/ja/guides/projects/managing-hierarchies/) — 多数のプロジェクトを整理するためのフォルダー構造
- [テーブルとビューを管理する](/ja/guides/projects/managing-tables-and-views/) — プロジェクト内のデータ層
- [データエディターを管理する](/ja/guides/projects/managing-data-editors/) — プロジェクトデータを変更できるユーザー
- [プロジェクトログを表示する](/ja/guides/projects/viewing-the-project-log/) — 変更の監査証跡
- [プロジェクトをアーカイブする](/ja/guides/projects/archive-a-project/) — 完了した作業を削除せずに保存
- [パンくずリストとリンク](/ja/guides/projects/breadcrumbs-and-shareable-links/) — どのウィンドウからでも上の階層へ移動し、表示中の内容へのリンクを共有
- [プロジェクトの比較とマージ](/ja/guides/projects/compare-and-merge-projects/) — 2つのプロジェクトの差分を確認し、変更を選択してコピー
- [ポータブル形式へのエクスポート](/ja/guides/projects/export-to-portable-format/) — プロジェクトを、プラットフォーム外で動作するスタンドアロンのPython + DuckDBプログラムとしてパッケージ化
- [ストレージを管理する](/ja/guides/projects/managing-storage/) — ワークスペースが保存している内容を確認し、テーブルの履歴を保持する期間を設定
- [ラベルで作業を整理する](/ja/guides/projects/organizing-with-labels/) — ワークフロー、ステップ、テーブル、その他のオブジェクトにタグを付けてグループ化・フィルター
- [リンクを共有する](/ja/guides/projects/sharing-links/) — アドレスバーからリンクをコピーして、プロジェクト、ワークフロー、テーブル、ディメンションを直接開く

## 関連項目

- [コンセプト](/ja/get-started/concepts/) — プロジェクトとワークスペース、メンバー、より広いデータモデルとの関係
- [ワークフロー](/ja/guides/workflows/) — プロジェクト内に存在する自動化の基本要素
- [アクセス管理](/ja/administration/access/) — プロジェクトを表示・編集できるユーザーを制御するワークスペースレベルの設定
