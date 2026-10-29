---
title: 式と集計のためのディメンション関数
description: PlaidCloud のディメンションで関数式を使い、計算値、条件ロジック、動的なメンバープロパティを定義します。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## ディメンション階層の式で使用する関数

ディメンション階層画面では、「集計」と「式」を追加できます。それぞれの説明を以下に示します。

## 集計
集計は、テーブルから集計した値を表示するために使用します（「Sum」、「Count」、「Min」、「Max」のいずれかを指定できます）。
次の画像は、階層内の各「Period」の値を表示できるように、「Line Item Values」テーブルから値を取得するよう構成した集計を示しています。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_1_agg.png)

集計にはフィルターを設定して、条件に一致する項目だけを表示できます。次の画像では、「Account」ディメンションで選択した項目の値を表示するように集計を設定しています。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_2_agg.png)

これらのフィルターを空のままにした場合は、次の画像のように、画面上部のディメンションフィルターバーでデータを絞り込めます。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## 式

式を使うと、ディメンションに表示されている集計の値に基づいて計算した値を表示できます。
式は数式で作成します。数式には、さまざまな種類の演算子と、いくつかの特別な関数を含められます。[演算子の一覧](https://mathjs.org/docs/expressions/syntax.html)をご覧ください。使用できる関数は以下のとおりです。


## 関数
### Column(`<column_name>`)
現在の行/ノードについて、指定した名前の列から値を取得します。

以下は、Line Item Value に 2 を掛けた結果を表示する式を定義した例です。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

現在の行/ノードの子の数を返します。現在の行/ノードがリーフ項目の場合は 0 を返します。

次の例では、親ノードの子ノードの平均値を返すために使用しています。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
現在の行/ノードについて、ツリー内で見つかったリーフ項目の数を返します。現在の行/ノードがリーフ項目の場合は 1 を返します。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
現在の行/ノードについて、ツリー内で見つかった項目の総数を返します。現在の行/ノードがリーフ項目の場合は 0 を返します。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
現在の行/ノードの兄弟項目の数を返します。返される値には現在のノードも含まれます。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
指定した名前のノードについて、指定した名前の列から値を返します。
次は、各行/ノードについて「LIV」合計に対する割合を表示するために使用している例です。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
現在のノードの親について、指定した列から値を返します。
この例は、親ノードの値のうち、子ノードが使用している割合を示しています。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

指定した名前の列のテキストが、指定した値より大きいか、小さいか、等しいかを表す数値を返します。

列のテキストが指定したテキストと等しい場合、この関数は 0 を返します。

列のテキストが指定したテキストより小さい場合、この関数は -1 を返します。

列のテキストが指定したテキストより大きい場合、この関数は 0 を返します。


次の例では、Period の名前を「Jun」と比較しています。


![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## 条件式
上記の例はかなり単純です。式の中で条件を使うと、より複雑な式を作成できます。
式の中の条件は、次の形式です。
`<condition>` ? `<value_if_true>` : `<value_if_false>`
例: '12 > 6 ? 1000: 0'

条件と関数の両方を含む式を組み合わせると、さらに複雑な式を作成できます。次の例では、月が「Jun」の場合に Line Item Value に 100,000 を加算しています。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## 別の例: 単純な配賦

この例は、リーフノードのリソースドライバー値を使って消費される、親の明細項目値の金額を示しています。

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![ディメンションの読み込み](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## 制限事項:
現在、他の式の値に基づく式は作成できません。式は、集計の値のみを使って作成できます。
