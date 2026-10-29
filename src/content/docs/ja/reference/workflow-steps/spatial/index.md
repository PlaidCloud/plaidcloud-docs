---
title: 地理空間ステップ
description: PlaidCloudの地理空間ワークフローステップ一覧です。空間ファイルのインポート、バッファー、照合、計測、ジオメトリの構築を行え、Alteryxの空間ツールを網羅しています。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

ジオメトリの読み取り、構築、変換、照合を行うワークフローステップです。[ジオメトリ式](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/)と組み合わせることで、Alteryxの空間ツール全体をカバーします。ツールごとの対応については、[Alteryx変換マトリックス](/ja/reference/alteryx-conversion-matrix/)を参照してください。

## ジオメトリはWKT

すべての空間ステップは、ジオメトリを通常のテキスト列内の**WKT**（Well-Known Text）として読み書きします。宣言が必要な特別なジオメトリ型はなく、ステップ間での変換も不要です。たとえば、[空間ファイルのインポート](/ja/reference/workflow-steps/spatial/spatial-file-import/)ステップが生成したジオメトリ列は、[Spatial Buffer](/ja/reference/workflow-steps/spatial/spatial-buffer/)ステップ、[空間照合](/ja/reference/workflow-steps/spatial/spatial-match/)ステップ、またはSQL式で、順序を問わずそのまま使用できます。

## 2つの実行ルート

各ステップは、正しい結果が得られる最も単純なルートで実行されます。

| ルート | 実行されるもの | 理由 |
|---|---|---|
| **SQL** — データベース内 | 最近傍検索、照合、および[ジオメトリ式](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/) | 述語結合と列の式はテーブルの規模に合わせてスケールし、行がウェアハウスの外に出ることはありません |
| **ワークフローエンジン** — ShapelyとGDAL | ジオメトリの形状を変更するすべての処理 | バッファー、平滑化、ディゾルブはデータベースのSQLでは表現できません |

ルートを選択する必要はありません。ステップの種類ごとに1つのルートが決まっています。ジョブの規模を見積もる際には、この違いが重要になります。SQLルートのステップはウェアハウスに合わせてスケールし、エンジンルートのステップはワークフローのポッドに合わせてスケールします。

## ジオメトリの読み込みと書き出し

- [空間ファイルのインポート](/ja/reference/workflow-steps/spatial/spatial-file-import/) — MapInfoの`.TAB`、ESRIの`.shp`、`.kml`、`.geojson`ファイルとそのサイドカーファイルを読み取ります
- [空間ファイルのエクスポート](/ja/reference/workflow-steps/spatial/spatial-file-export/) — WKTジオメトリとその属性を、シェープファイル、GeoJSON、GeoPackage、KML、GML、MapInfoファイルに書き込みます
- [Geometry in SQL](/ja/reference/workflow-steps/spatial/spatial-sql-recipes/) — 経度・緯度の列からポイントを作成します

## 照合と計測

- [Spatial Find Nearestステップ](/ja/reference/workflow-steps/spatial/spatial-find-nearest/) — あるテーブルの各行に対して、別のテーブルから距離の近いN行を取得します
- [空間照合](/ja/reference/workflow-steps/spatial/spatial-match/) — ジオメトリが交差する、内包される、または含む行をペアにします
- [Spatial Match (Intersect / Unmatched)](/ja/reference/workflow-steps/spatial/spatial-match-executor/) — 同じ照合を行い、重なり部分のジオメトリまたは一致しなかった行を出力します
- [Spatial Infoステップ](/ja/reference/workflow-steps/spatial/spatial-info/) — 面積、長さ、重心、外接矩形を測地線で計測します
- [空間の再投影](/ja/reference/workflow-steps/spatial/spatial-reproject/) — ジオメトリをある座標参照系から別の座標参照系に変換します

## ジオメトリの形状変更

- [Spatial Bufferステップ](/ja/reference/workflow-steps/spatial/spatial-buffer/) — 各ジオメトリを一定の距離だけ拡張します
- [Spatial Trade Areaステップ](/ja/reference/workflow-steps/spatial/spatial-trade-area/) — 実世界の単位で大きさを指定した同心円状のバッファーを作成します
- [Spatial Generalizeステップ](/ja/reference/workflow-steps/spatial/spatial-generalize/) — 許容値に基づいて簡略化します
- [Spatial Smoothステップ](/ja/reference/workflow-steps/spatial/spatial-smooth/) — 指定した回数だけ平滑化します
- [空間処理](/ja/reference/workflow-steps/spatial/spatial-process/) — 2つのジオメトリ列の交差、結合、切り取りを行います

## 構築と分解

- [Spatial Poly-Buildステップ](/ja/reference/workflow-steps/spatial/spatial-poly-build/) — ポイントのグループごとに、ポリゴンまたは凸包を構築します
- [Spatial Poly-Splitステップ](/ja/reference/workflow-steps/spatial/spatial-poly-split/) — 頂点、構成ポリゴン、または穴ごとに1行を出力します
- [空間結合](/ja/reference/workflow-steps/spatial/spatial-combine/) — 各グループのジオメトリを1つにディゾルブします
- [Spatial Centroidステップ](/ja/reference/workflow-steps/spatial/spatial-centroid/) — 各ジオメトリの中心点を追加します
- [Spatial Point to Lineステップ](/ja/reference/workflow-steps/spatial/spatial-point-to-line/) — 各グループのポイントを結んで線にします
- [Spatial Line to Polygonステップ](/ja/reference/workflow-steps/spatial/spatial-line-to-polygon/) — 各線を閉じてポリゴンにします
- [Spatial Make Gridステップ](/ja/reference/workflow-steps/spatial/spatial-make-grid/) — 範囲を正方形のセルで敷き詰めます

## 式のリファレンス

- [ジオメトリ関数（Lakehouse v1）](/ja/reference/expressions/lakehouse-v1/09-geometry-functions/) — `ST_*`ファミリー
- [ジオグラフィ関数（Lakehouse v1）](/ja/reference/expressions/lakehouse-v1/09-geo-functions/) — H3六角形インデックスとジオハッシュ
- [空間関数（Lakehouse v2）](/ja/reference/expressions/lakehouse-v2/17-spatial-functions/)

## 関連情報

- [地理空間分析](/ja/guides/workflows/geospatial-analytics/) — ソースファイルから公開マップまでの実践的な手順
- [空間Alteryxワークフローの移行](/ja/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Mapステップ](/ja/reference/workflow-steps/reports/report-map/) — ジオメトリをレポートにレンダリングします
- [パッケージ化マクロのステップ](/ja/reference/workflow-steps/macros/) — Heat MapとPie Wedge Trade Area
