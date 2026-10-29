---
title: 集計関数 (Lakehouse v1)
description: "Lakehouse v1 の SQL 集計関数: 行を集約します — SUM、AVG、MIN、MAX、COUNT、および統計集計。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/07-aggregate-functions/index.md
---

集計関数は SQL に欠かせないツールで、値の集合に対して計算を行い、単一の結果を返します。

これらの関数を使用すると、データベースからデータを抽出して要約し、価値のあるインサイトを得ることができます。

| 関数名                                                    | 機能                                                                 | 
|------------------------------------------------------------------|------------------------------------------------------------------------------|
| [ANY](aggregate-any)                                             | 指定した条件を満たす行があるかどうかを確認します                              | 
| [APPROX_COUNT_DISTINCT](aggregate-approx-count-distinct)         | HyperLogLog を使用して一意な値の数を推定します                     | 
| [ARG_MAX](aggregate-arg-max)                                     | val の最大値に対応する arg の値を求めます                                | 
| [ARG_MIN](aggregate-arg-min)                                     | val の最小値に対応する arg の値を求めます                                | 
| [AVG_IF](aggregate-avg-if)                                       | 条件を満たす行の平均を計算します                          | 
| [ARRAY_AGG](aggregate-array-agg)                                 | 列のすべての値を配列に変換します                              |
| [AVG](aggregate-avg)                                             | 特定の列の平均値を計算します                            | 
| [COUNT_DISTINCT](aggregate-count-distinct)                       | 列内の一意な値の数をカウントします                             | 
| [COUNT_IF](aggregate-count-if)                                   | 指定した条件を満たす行をカウントします                                    | 
| [COUNT](aggregate-count)                                         | 特定の基準を満たす行数をカウントします                         | 
| [COVAR_POP](aggregate-covar-pop)                                 | 数値ペアの集合の母共分散を返します                   | 
| [COVAR_SAMP](aggregate-covar-samp)                               | 数値ペアの集合の標本共分散を返します                       | 
| [GROUP_ARRAY_MOVING_AVG](aggregate-group-array-moving-avg)       | 入力値の移動平均を計算した要素を持つ配列を返します |
| [GROUP_ARRAY_MOVING_SUM](aggregate-group-array-moving-sum)       | 入力値の移動合計を計算した要素を持つ配列を返します     |
| [HISTOGRAM](aggregate-histogram)                                | 等高バケット方式でデータ分布のヒストグラムを生成します        | 
| [JSON_ARRAY_AGG](aggregate-json-array-agg)                      | NULL をスキップして値を JSON 配列に変換します                           | 
| [JSON_OBJECT_AGG](aggregate-json-object-agg)                    | キーと値のペアを JSON オブジェクトに変換します                                 | 
| [KURTOSIS](aggregate-kurtosis)                                   | 値の集合の超過尖度を計算します                            | 
| [MAX_IF](aggregate-max-if)                                       | 条件を満たす行の最大値を求めます                         | 
| [MAX](aggregate-max)                                             | 特定の列の最大値を求めます                                 | 
| [MEDIAN](aggregate-median)                                       | 特定の列の中央値を計算します                             | 
| [MEDIAN_TDIGEST](aggregate-median-tdigest)                       | t-digest アルゴリズムを使用して特定の列の中央値を計算します    | 
| [MIN_IF](aggregate-min-if)                                       | 条件を満たす行の最小値を求めます                         | 
| [MIN](aggregate-min)                                             | 特定の列の最小値を求めます                                | 
| [QUANTILE_CONT](aggregate-quantile-cont)                         | 特定の列の補間分位数を計算します                   |
| [QUANTILE_DISC](aggregate-quantile-disc)                         | 特定の列の分位数を計算します                                | 
| [QUANTILE_TDIGEST](aggregate-quantile-tdigest)                   | t-digest アルゴリズムを使用して分位数を計算します                             |
| [QUANTILE_TDIGEST_WEIGHTED](aggregate-quantile-tdigest-weighted) | t-digest アルゴリズムを使用して重み付き分位数を計算します               |
| [RETENTION](aggregate-retention)                                 | イベントの集合のリテンションを計算します                                     | 
| [SKEWNESS](aggregate-skewness)                                   | 値の集合の歪度を計算します                                   | 
| [STDDEV_POP](aggregate-stddev-pop)                               | 列の母標準偏差を計算します                     | 
| [STDDEV_SAMP](aggregate-stddev-samp)                             | 列の標本標準偏差を計算します                         | 
| [STRING_AGG](aggregate-string-agg)                               | NULL ではないすべての値を String に変換し、区切り文字で区切って連結します       |
| [SUM_IF](aggregate-sum-if)                                       | 特定の列で条件を満たす値を合計します                  | 
| [SUM](aggregate-sum)                                             | 特定の列の値を合計します                                      | 
| [WINDOW_FUNNEL](aggregate-windowfunnel)                          | 時系列順のイベントシーケンスでユーザーの行動を分析します                  |
