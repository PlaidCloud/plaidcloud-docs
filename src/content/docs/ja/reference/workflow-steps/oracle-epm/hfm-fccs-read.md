---
title: "HFM/FCCS: データの読み取り（アドホック）"
description: ステップフォームでポイントオブビューを組み立てて、Oracle FCCS からデータスライスをセルフサービスで取得します。返されたグリッドは自動的にテーブルとして格納され、同じ取得はキャッシュされ、エンティティ列は行レベルセキュリティに対応しており、オプションのバインドしたターゲットを使うとスケジュールされた定期ロードにできます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## 説明

[HFM/FCCS 接続](/ja/guides/connections/hfm-fccs/)を使用して、クエリを書く代わりに**ポイントオブビュー（POV）**を指定して、Oracle **FCCS**（Financial Consolidation and Close、EPM Cloud）からアドホックなデータスライスを読み取ります。財務ユーザーがアプリケーションを選択し、FCCS のディメンションから POV を組み立てて、ステップを実行すると、返されたグリッドが自動的にプロジェクトテーブルとして格納されます（スキーマオンリード：テーブルはグリッドの列から作成されます）。ライブクエリのように感じられますが、内部的にはステップが FCCS にエクスポートジョブを送信し、完了するまで**ポーリング**してから、結果を取得して格納します。そのため、長時間かかるスライスでもブロックされず、HFM チームへのチケットも不要です。

このステップは、ステップメニューの **Oracle EPM (HFM/FCCS)** の下に表示されます。

:::note[エンティティディメンションの範囲を絞る]
**エンティティ**の選択は範囲を絞ってください。範囲を絞らない抽出は、エクスポートジョブの実行中に FCCS アプリケーションを長時間ロックすることがあります。
:::

## 設定

### ソースとターゲット

| フィールド | 必須 | 備考 |
|---|---|---|
| HFM/FCCS接続 | はい | 読み取りに使用する [HFM/FCCS 接続](/ja/guides/connections/hfm-fccs/)です。 |
| 環境 | はい | 接続の環境です。 |
| アプリケーション | はい | 読み取り元の FCCS アプリケーションです。接続に**デフォルトアプリケーション**が設定されている場合は、それがデフォルトになります。アプリケーションを選択すると、POV のメンバーがライブで検出されます。 |
| ターゲットテーブル | はい | 返されたグリッドを格納するプロジェクトテーブルです。 |

### ポイントオブビュー

FCCS のディメンションからスライスを組み立てます。サポートされているポッドでは、接続とアプリケーションを選択すると、ライブのメタデータ検出によってメンバーリストが自動的に入力されます。古いポッドでは、メンバー名を手動で入力します。

| ディメンション | 必須 | 備考 |
|---|---|---|
| シナリオ | はい | |
| 年 | はい | |
| 期間 | はい | |
| エンティティ | 範囲を限定 | 範囲を限定したスライスを指定する必要があります。空の選択、「all」、500 メンバーを超える選択はフォームで拒否されます。エクスポートでアプリケーションがロックされないよう、範囲を絞ってください。 |
| 勘定科目 | いいえ | |
| Custom1–Custom4 | いいえ | アプリケーションのカスタムディメンションです。 |
| ICP | いいえ | 会社間（Intercompany）です。 |
| ビュー | いいえ | |
| 値 | いいえ | |

設定されていない任意のディメンションは、その軸にフィルターを適用しません（FCCS のデフォルトメンバーが使用されます）。

### バインドしたターゲット

デフォルトではオフです。実行のたびにアドホックなスライスが格納され、ターゲットテーブルが上書きされます。

| フィールド | 備考 |
|---|---|
| バインドしたターゲット（スケジュールされた定期ロード） | オンにすると、ターゲットは**永続的な**テーブルになります。ステップは上書きではなく、キーセットのアップサートでマージし、後続のグリッドで新しい列が追加された場合はスキーマが追加的に拡張されます（新しい列は警告を出しますが、失敗にはなりません）。このステップをスケジュールされたワークフローに配置すると、データを消去せずに蓄積する定期ロードになります。 |
| キー列 | バインドしたターゲットがオンの場合のみ有効です。マージキーを構成する列をカンマ区切りで指定します（例：`Entity, Account`）。**空のまま**にすると、格納されたグリッドに含まれる POV ディメンション列がマージキーとして使用されます。 |

## 仕組み

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="ステップは FCCS にエクスポートジョブを送信し、完了するまでポーリングし、グリッドを取得してテーブルとして格納します。同じポイントオブビューが再度要求された場合は、代わりにキャッシュされたテーブルから提供されます。" style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">ジョブを送信</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">ポーリング</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">グリッドを取得</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">テーブルに格納</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">実行中…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">同じ POV の再取得</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">キャッシュから提供</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">実行すると、エクスポートジョブを送信し、ポーリングし、グリッドを取得して、テーブルとして格納します。同じポイントオブビューが再度要求された場合は、すでに格納されたコピーから提供されます。</figcaption>
</figure>

ジョブの実行中、ステップにはポーリングの状況が表示されます。格納されると、テーブルはグリッドの列から作成されるため、事前にスキーマを定義する必要はありません。

## キャッシュ

同じ POV が再度要求された場合は、FCCS にエクスポートを再送信する代わりに、**すでに格納されたテーブルから**即座に提供されます。実行は、アプリケーション、ターゲットテーブル、ポイントオブビュー、**as-of** タグ（デフォルトは `latest`）で識別されます。すでに格納されたスライスに解決される再取得は、書き直さずにテーブルをそのまま残したことを報告します。同じ POV を強制的に新しく抽出したい場合は、as-of タグを変更してください。

## 行レベルセキュリティ

格納されたグリッドのエンティティ軸は、まさに **`Entity`** という名前の列に正規化されるため、テーブルは**行レベルセキュリティに対応**しています。管理者は[行アクセス](/ja/administration/access/managing-security-groups-and-assignments/)でこれを管理し、セルフサービスのユーザーに、権限のあるエンティティのみを表示させることができます。

これは**管理者の管理下で制御されるもので、自動ではありません**。抽出は接続のサービスアカウントで実行されるため、PlaidCloud はステップ自身にセキュリティを宣言させません。管理者は標準の行アクセスのワークフローに従います。

1. 格納されたテーブルをレポート用に**公開**します。
2. `Entity` 列を管理対象の属性として宣言します（デフォルトは拒否）。
3. 最初の管理対象の書き込みを**承認**します。
4. **照合**して、付与が有効になるようにします。

管理者がこの手順を行うまで、テーブルはフィルターされません。[セキュリティグループと割り当ての管理](/ja/administration/access/managing-security-groups-and-assignments/)を参照してください。

## 機能の制限

| 制限事項 | 意味 |
|---|---|
| 読み取り専用 | FCCS からスライスを抽出します。連結データの書き込み、連結の実行、書き戻しは行いません。 |
| 範囲を限定したエンティティが必須 | 空の選択、「all」、500 メンバーを超えるエンティティの選択はフォームで拒否されます。また、単一の集計メンバーがサーバー側で展開されることがあるため、スライスの範囲を絞ってください。 |
| 古いポッドでは手動でメンバーを入力 | ポッドがメタデータのエンドポイントを公開していない場合、メンバーリストは自動入力されません。メンバー名を手動で入力してください。 |
| 行レベルセキュリティは管理者が制御 | `Entity` 列は RLS に対応していますが、テーブルがフィルターされるには、管理者が公開、宣言、最初の書き込みの承認、照合を行う必要があります。 |

## 関連項目

- [HFM / FCCS からの抽出（ガイド）](/ja/guides/connections/hfm-fccs/) — 手順に沿った完全な解説。
- [HFM / FCCS コネクター](/ja/reference/connectors/rest/hfm-fccs/) — 接続フィールドのリファレンス。
- [Oracle EPM (HFM / FCCS) ステップ](/ja/reference/workflow-steps/oracle-epm/)
- [セキュリティグループと割り当ての管理](/ja/administration/access/managing-security-groups-and-assignments/)
