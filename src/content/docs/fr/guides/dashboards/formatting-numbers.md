---
title: Mise en forme des nombres et des autres types de données
description: "Mettez en forme les nombres dans les tableaux de bord PlaidCloud : devises, pourcentages, décimales et motifs d'affichage personnalisés."
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/formatting-numbers.md
---

## Mise en forme des nombres et des autres types de données

Il existe deux façons de mettre en forme les nombres dans PlaidCloud. La première consiste à transformer directement les valeurs dans les tables ; la seconde (plus courante) consiste à les mettre en forme à l'affichage, afin que les valeurs ne perdent pas en précision dans la table et que l'utilisateur les voie sous une forme plus claire et plus adaptée.

Lorsque j'affiche une valeur dans un tableau de bord, comment la mettre en forme comme je le souhaite ?
La principale façon d'afficher une valeur passe par un objet graphique dans un tableau de bord. Les graphiques peuvent être des tableaux, des grands nombres, des diagrammes à barres, etc. Chaque objet graphique peut offrir un emplacement ou un moyen légèrement différent pour afficher les valeurs. Par exemple, dans les tableaux, vous pouvez modifier le format de chaque colonne, et pour un grand nombre, vous pouvez modifier le format du nombre.

Pour modifier le format, modifiez le graphique et repérez le champ `D3 FORMAT` ou `NUMBER FORMAT`. Pour un graphique de type grand nombre, cliquez sur l'onglet `CUSTOMIZE` : vous y verrez `NUMBER FORMAT`. Pour un tableau, cliquez sur l'onglet `CUSTOMIZE`, sélectionnez une colonne numérique (affichée avec un #) dans `CUSTOMIZE COLUMN` : vous verrez le champ `D3 FORMAT`.

La valeur par défaut est `Adaptive formatting`. Elle ajuste le format en fonction des valeurs. Mais si vous souhaitez imposer un format (par exemple $12.23 ou 12,345,678), sélectionnez le format voulu dans la liste déroulante ou saisissez manuellement une autre valeur (si le champ le permet).

## Mise en forme D3 : de quoi s'agit-il ?

La mise en forme D3 est un moyen structuré et formalisé d'afficher des résultats de données dans un format donné. Par exemple, dans certaines situations, vous pouvez vouloir afficher une grande valeur sous la forme 3B (3 milliards), formatée `.3s` en format D3, ou sous la forme 3,001,238,383, formatée `,d`. Autre exemple courant : choisir de représenter les montants en dollars avec 2 décimales, ou de les arrondir au dollar le plus proche avec $,d, ou encore $,.2f pour afficher le signe dollar, les virgules, 2 décimales et une notation à virgule fixe.
Pour approfondir D3, consultez le site suivant : [GitHub D3](https://github.com/d3/d3-format)


## Format D3 général

La structure générale de D3 est la suivante :

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

Le caractère de remplissage (fill) peut être n'importe quel caractère (un point, un x ou tout autre). Si vous utilisez un caractère de remplissage, il est suivi d'un caractère `align`, qui doit être l'un des suivants :

`>` - Aligné à droite dans l'espace disponible (comportement par défaut).
`<` - Aligné à gauche dans l'espace disponible.
`^` - Centré dans l'espace disponible.
`=` - Comme >, mais avec le signe et le symbole éventuels à gauche du remplissage.

Le `sign` peut être :
`-` - vide pour zéro ou positif, et un signe moins pour négatif (comportement par défaut).
`+` - un signe plus pour zéro ou positif, et un signe moins pour négatif.
`(` - rien pour zéro ou positif, et des parenthèses pour négatif.
(espace) - une espace pour zéro ou positif, et un signe moins pour négatif.

Le `symbol` peut être :
`$` - applique le symbole monétaire.

L'option `zero` (0) active le remplissage par des zéros ; elle fixe implicitement le remplissage (fill) à 0 et l'alignement (align) à =.

Le `width` définit la largeur minimale du champ ; s'il n'est pas spécifié, la largeur est déterminée par le contenu. Par exemple, avec 8, la largeur du champ sera de 8 caractères.

L'option `comma` (,) active l'utilisation des virgules comme séparateurs (par exemple pour les milliers).

Selon le type, la `precision` peut indiquer soit le nombre de chiffres après la virgule décimale (types f et %), soit le nombre de chiffres significatifs (types ​, g, r, s et p). Si la précision n'est pas spécifiée, elle vaut 6 par défaut pour tous les types sauf (aucun), pour lequel elle vaut 12.

L'option `tilde` ~ supprime les zéros de fin non significatifs pour tous les types de format. Elle s'utilise le plus souvent avec les types r, s et %.

`types`
|Type |   Description                                                                               |
|-----|---------------------------------------------------------------------------------------------|
|f    |notation à virgule fixe. **(courant)**
|d    |notation décimale, arrondie à l'entier. **(courant)**
|%    |multiplie par 100, puis notation décimale avec un signe pourcentage. **(courant)**
|g    |notation décimale ou exponentielle, arrondie aux chiffres significatifs.
|r    |notation décimale, arrondie aux chiffres significatifs.
|s    |notation décimale avec un préfixe SI, arrondie aux chiffres significatifs.
|p    |multiplie par 100, arrondit aux chiffres significatifs, puis notation décimale avec un signe pourcentage.

## Exemples
|Expression|Entrée|Sortie|Remarques|
|----------|-----|------|-----|
|,d|12345.67|12,346|arrondit la valeur à l'entier le plus proche, ajoute des virgules
|,.2f|12345.678|12,345.68|ajoute des virgules, 2 décimales, arrondit à la décimale la plus proche
|$,.2f|12345.67|$12,345.67|ajoute un symbole $, des virgules, 2 chiffres après la virgule décimale
|$,d|12345.67|$12,346|
|.&lt;10,|151925|151,925...|des points à gauche de la valeur, 10 caractères de large, avec des virgules
|0>10|12345|0000012345|complète la valeur avec des zéros à gauche, 10 caractères de large. Pratique pour fixer la largeur d'un code
|,.2%|13.215|1,321.50%|des virgules, 2 chiffres à droite de la virgule décimale, conversion en pourcentage, et affichage d'un symbole %
|x^+$16,.2f|123456|xx+$123,456.00xx| remplissage avec « x », centré, avec un symbole +/-, un symbole $, 16 caractères de large, des virgules, 2 décimales
