---
title: "Essbase: キューブのクエリ"
description: Oracle EssbaseキューブにライブのMDXクエリを実行し、結果のグリッドをワークフローのテーブルに書き込みます。列はグリッドから導出され、結果には行アクセスが適用されます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## 説明

**Essbase: キューブのクエリ**ステップは、Oracle EssbaseキューブにMDXの `SELECT` を実行し、返されたグリッドをターゲットテーブルに書き込みます。これは**真のライブクエリ**です。ステップがMDXを送信し、結果のグリッドを同期的に読み取るため、実行のたびにキューブの最新の数値が反映されます。抽出やポーリングではありません。待機するステージングジョブはなく、実行の間に古くなるスナップショットもありません。

キューブの特定のスライスを取得するために使用します。たとえば、期間ごとの勘定科目のセット、シナリオの比較、配賦のドライバーセットなどです。取得した内容はPlaidCloudのテーブルに格納され、ほかのデータとあわせて変換、結合、レポート作成ができます。

## 前提条件

- Essbase 21c以降またはOracle Analytics Cloud（OAC）を指す[Oracle Essbase接続](/ja/reference/connectors/erp/oracle-essbase/)と、クエリ対象のアプリケーションとキューブを読み取れるサービスアカウント。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Essbase接続から、選択したアプリケーションとキューブ、MDXクエリ、返されたグリッドを経て、ターゲットテーブルに至るフロー。" style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">接続</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">アプリケーション</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ キューブ</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">グリッド</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">テーブル</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">MDXはキューブに対してライブで実行され、返されたグリッドが、グリッド自体から導出された列とともにターゲットテーブルに書き込まれます。</figcaption>
</figure>

## 設定

- **接続** — Oracle Essbase接続です。ピッカーの横にある編集ショートカットから、接続エディターを開いて内容の確認や編集ができます。
- **アプリケーション** — クエリ対象のEssbaseアプリケーションです。ピッカーには、接続のサービスアカウントが参照できるアプリケーションが一覧表示されます。接続にデフォルトのアプリケーションが設定されている場合は、あらかじめ選択されています。
- **Cube (Database)** — 選択したアプリケーション内で、クエリ対象となるキューブです。
- **MDX** — 実行するMDXの `SELECT` 文です。ガイド付きのメンバー選択で作成するか、直接記述します（以下を参照）。
- **ターゲットテーブル** — 返されたグリッドの書き込み先のテーブルです。

## クエリの作成

MDXは2通りの方法で作成できます。

- **ガイド付きメンバー選択。** キューブのディメンションとメンバーを参照して、列と行に配置する内容を選びます。ステップがMDXを組み立てます。メンバーは展開するたびに1レベルずつ読み込まれるため、大きなアウトラインでも動作が軽快です。
- **生のMDX。** MDXの `SELECT` を直接記述または貼り付けます。計算メンバー、関数、セット演算子など、ガイド付きピッカーで対応できないものに使用する逃げ道です。

どちらの方法でも、ステップが実行する同じ `MDX` の値が生成されます。ガイド付きピッカーは出発点であり、いつでも手作業で編集できます。

## オプション

| フィールド | デフォルト | 備考 |
|---|---|---|
| #Missingセルを抑制 | オフ | サーバー側の処理で、`#Missing` やその他の構造上無関係なセルを、ネットワークに流れる前に除外します。安全で、転記済みのゼロが除外されることはありません。 |
| ゼロのセルも抑制する（非可逆） | オフ | 取得後に、値がすでに正確に `0` であるセルも破棄する、別個のオプトインフィルターです。**非可逆**です。プランニングキューブでは、転記済みのゼロは実際の事実であり、データがないことを意味しません。結果からゼロを除外したい場合にのみ有効にしてください。 |
| 行数の上限 | 250,000 | 返される行数の上限です。空欄のままにすると、デフォルトの上限である250,000が使用されます。明示的に増減できます。上限を超えるクエリは、黙って切り捨てられるのではなく、拒否されます。クエリを絞り込む（スライサー、`NON EMPTY`、より絞ったメンバーセットを追加する）か、行数の上限を引き上げてから、もう一度実行してください。 |

## プレビュー

保存する前に、**プレビュー**で現在のMDXをキューブに対して実行し、返された列と最初の数行を表示します。ステップ自体に設定された行数の上限とは関係なく、クエリが想定どおりの形になっているかをすばやく確認できます。

## 結果とスキーマオンリード

Essbaseが返すグリッドは、**返されたグリッドから導出された列**とともにターゲットテーブルに書き込まれます。これがスキーマオンリードです。列の一覧をあらかじめ宣言する必要はありません。

- 列名は、グリッドのヘッダー行から決まります。何にもまたがらないヘッダーセル（行ラベルの上の隅）は、`column_1`、`column_2` のようになります。重複する名前には、数値の接尾辞が付いて一意になります。
- データセルがすべて数値の列は数値型に、それ以外はテキスト型になります。Essbaseの空のセルは、NULLとして格納されます。
- グリッド内のメンバーとエイリアスのラベルは、接続に設定されたエイリアステーブルから取得され、実行のたびに一貫して適用されます。クエリの実行時に誰がログインしていたかによってラベルのテキストが変わる可能性がある、Essbase自身のセッションごとのデフォルトは使用されません。

形がクエリに従うため、MDXで列に配置する内容を変更すると、次の実行でテーブルの列も変わります。特定の列名を参照する下流のステップでは、この点に注意してください。

## 行アクセス

[行レベルセキュリティ](/ja/administration/access/managing-security-groups-and-assignments/#行アクセスの管理)は、ほかのPlaidCloudテーブルとまったく同じように、書き込まれたテーブルに適用されます。ガバナンスはステップが書き込む結果に対して適用されるため、行の制限を受けているユーザーには、セキュリティグループが許可する行だけが表示されます。クエリは接続のサービスアカウントで実行されますが、生成されるテーブルは、ほかのデータと同様に管理されます。

## 例

このMDXは、2つのメジャーを列に、2つの製品を行に配置します。

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

これらの4つの数値を返すキューブに対して実行すると、次のようなテーブルが格納されます。

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

行ラベルの列はグリッドにヘッダーがないため `column_1`（テキスト）になります。`Sales` と `COGS` はすべて数値であるため、数値の列として格納されます。

## 関連項目

- [Oracle Essbaseに接続する（ガイド）](/ja/guides/connections/essbase/) — 接続を作成し、クエリを作成します。
- [Oracle Essbaseコネクタ](/ja/reference/connectors/erp/oracle-essbase/) — 接続フィールドのリファレンスです。
- [Essbase: ディメンションの読み取り](/ja/reference/workflow-steps/essbase/essbase-dimension-read/) — Essbaseのディメンションアウトラインを、PlaidCloudディメンションにクラウド直結で読み込みます。
- [Oracle Essbaseステップ](/ja/reference/workflow-steps/essbase/)
- [RESTリクエスト](/ja/reference/workflow-steps/general/rest-request/) — その他のライブHTTPリクエストに使用する汎用ステップです。
