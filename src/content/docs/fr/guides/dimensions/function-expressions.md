---
title: Fonctions pour les expressions et les agrégations de dimension
description: Utilisez des expressions de fonction dans les dimensions PlaidCloud pour définir des valeurs calculées, une logique conditionnelle et des propriétés de membre dynamiques.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## Fonctions utilisables dans les expressions de hiérarchie de dimension

Dans l'écran Hiérarchie de la dimension, il est possible d'ajouter des « agrégations » et des « expressions ». Leur description figure ci-dessous.

## Agrégations
Une agrégation sert à afficher une valeur agrégée issue d'une table (« Sum », « Count », « Min » ou « Max »).
L'image suivante montre une agrégation configurée pour récupérer des valeurs dans une table « Valeurs de poste » afin d'afficher des valeurs pour chaque « Période » de la hiérarchie.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_1_agg.png)

Les agrégations peuvent être filtrées pour n'afficher que les éléments qui correspondent au filtre. Dans l'image suivante, nous avons configuré l'agrégation pour afficher les valeurs d'un élément sélectionné de la dimension « Compte ».

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_2_agg.png)

Si ces filtres sont laissés vides, les données peuvent être filtrées à l'aide de la barre de filtre de dimension située en haut de l'écran, comme le montre l'image suivante :

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Expressions

Les expressions permettent d'afficher des valeurs calculées à partir des valeurs des agrégations affichées pour la dimension.
Les expressions s'écrivent à l'aide de formules mathématiques, qui peuvent contenir de nombreux types d'opérateurs et quelques fonctions spéciales. Consultez la [liste des opérateurs](https://mathjs.org/docs/expressions/syntax.html). Les fonctions disponibles sont décrites ci-dessous.


## Fonctions
### Column(`<column_name>`)
Récupère une valeur dans une colonne nommée pour la ligne ou le nœud actuel.

Ci-dessous, un exemple d'expression définie pour afficher le résultat de la multiplication de la valeur de poste par 2.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

Renvoie le nombre d'enfants de la ligne ou du nœud actuel. Si la ligne ou le nœud actuel est une feuille, la fonction renvoie 0.

Dans l'exemple suivant, elle sert à renvoyer la valeur moyenne des nœuds enfants d'un nœud parent.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
Renvoie le nombre de feuilles présentes dans l'arbre pour la ligne ou le nœud actuel. Si la ligne ou le nœud actuel est une feuille, la fonction renvoie 1.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
Renvoie le nombre total d'éléments présents dans l'arbre pour la ligne ou le nœud actuel. Si la ligne ou le nœud actuel est une feuille, la fonction renvoie 0.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
Renvoie le nombre d'éléments de même niveau pour la ligne ou le nœud actuel. La valeur renvoyée inclut le nœud actuel.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
Renvoie la valeur d'une colonne nommée pour un nœud nommé.
Voici un exemple qui sert à afficher le pourcentage du total « LIV » pour chaque ligne ou nœud.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
Renvoie la valeur d'une colonne donnée pour le parent du nœud actuel.
Cet exemple montre le pourcentage de la valeur d'un nœud parent utilisé par un nœud enfant.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

Renvoie un résultat numérique indiquant si le texte d'une colonne nommée est supérieur, inférieur ou égal à une valeur fournie.

Si le texte de la colonne est égal au texte fourni, cette fonction renvoie 0.

Si le texte de la colonne est inférieur au texte fourni, cette fonction renvoie -1.

Si le texte de la colonne est supérieur au texte fourni, cette fonction renvoie 0.


L'exemple suivant compare le nom de la Période à « Jun ».


![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Expressions conditionnelles
Les exemples ci-dessus sont assez simples. L'utilisation de conditions dans les expressions permet de créer des expressions plus complexes.
Dans les expressions, les conditions prennent la forme suivante :
`<condition>` ? `<value_if_true>` : `<value_if_false>`
p. ex. '12 > 6 ? 1000: 0'

En combinant des expressions qui contiennent à la fois des conditions et des fonctions, nous pouvons construire des expressions plus complexes, comme dans cet exemple où 100 000 sont ajoutés à une valeur de poste si le mois est « Jun ».

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Autre exemple : allocation simple

Cet exemple montre la part de la valeur de poste d'un parent consommée en utilisant la valeur d'inducteur de ressource d'un nœud feuille.

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Chargement de dimension](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Limites
Il n'est actuellement pas possible de construire des expressions fondées sur les valeurs d'autres expressions. Les expressions ne peuvent être construites qu'à partir de valeurs d'agrégations.
