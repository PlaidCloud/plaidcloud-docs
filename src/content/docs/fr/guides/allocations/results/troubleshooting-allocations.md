---
title: Dépannage des allocations
description: "Résolvez les problèmes d'allocation PlaidCloud : erreurs courantes, problèmes de configuration et techniques de débogage des résultats."
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## Pourquoi une étape d'allocation ne s'enregistre pas

PlaidCloud vérifie le mappage des colonnes d'une étape d'allocation lorsque vous l'enregistrez. Un mappage qui ne peut pas s'exécuter est refusé à ce moment-là, avec une notification **Impossible d'enregistrer** qui liste ce qu'il faut corriger, et le formulaire bascule vers l'onglet qui contient le problème. Auparavant, une telle étape s'enregistrait sans broncher, puis interrompait le workflow en cours d'exécution, souvent plusieurs minutes plus tard, avec un message qui nommait un nombre plutôt qu'un champ.

Rien n'est vérifié tant que vous n'avez pas choisi à la fois la **Table des valeurs à allouer** et la **Table de données de l'inducteur**. Le mappage des colonnes est construit à partir de ces deux tables ; tant qu'elles ne sont pas définies, l'étape ne demande que les tables elles-mêmes.

### Mappage de la source d'allocation

**« No columns specified for allocation. »**
Définissez le **Rôle** d'au moins une colonne sur **Valeur à allouer**. Cette colonne contient les valeurs réparties entre les cibles.

**« Only numeric columns can be allocated, but ... is not numeric. »**
Une colonne marquée **Valeur à allouer** a un **Type** non numérique. Remplacez-le par un type numérique : Numeric, Currency, Integer, Grand entier, Petit entier, Très petit entier, Float, Double, Decimal, Serial ou Grande série.

**« Rename the `alloc_status` target column. »**
Une allocation écrit sa propre colonne `alloc_status` dans la table de résultat ; une colonne cible portant ce nom entre donc en collision avec elle. Renommez la vôtre.

### Mappage des données de l'inducteur

**« No driver split value column found. »**
Définissez le **Rôle** d'une colonne d'inducteur sur **Valeur de fractionnement**. Cette colonne contient les pondérations ou les pourcentages par lesquels l'allocation divise.

**« The driver value column ... must be numeric. »**
Remplacez le **Type** de la colonne **Valeur de fractionnement** par un type numérique.

**« No driver relation columns specified. »**
Définissez le **Rôle** d'au moins une colonne d'inducteur sur **Relation source (dénominateur)**. C'est ce qui relie les lignes de l'inducteur aux lignes de la source.

**« No allocation target columns are indicated. »**
Définissez le **Rôle** d'au moins une colonne d'inducteur sur **Cible d'allocation (numérateur)**. Ces colonnes deviennent les cibles de l'allocation et apparaissent dans la table de résultat.

**« Driver relation columns do not exist in the source data. »**
Une colonne marquée **Relation source (dénominateur)** n'a pas de colonne de même nom dans le **Mappage de la source d'allocation**. Renommez-la pour qu'elle corresponde, ou ajoutez la colonne au mappage de la source.

**« Allocation value column ... is also used as a numerator or denominator column. »**
Le même nom de colonne est à la fois une **Valeur à allouer** dans le mappage de la source et une **Relation source (dénominateur)** ou une **Cible d'allocation (numérateur)** dans le mappage de l'inducteur. Renommez l'une des deux afin que la valeur allouée soit distincte des colonnes qui décrivent sa destination.

### Uniquement pour Split Using Dimension

**« Please select a hierarchy to use for the allocation dimension. »**
Choisissez une **Hiérarchie de la dimension d'affectation** dans l'onglet **Paramètres de la table de données**. Consultez [Configurer une allocation](/fr/guides/allocations/setup/configure-an-allocation/).

## Coût orphelin


Le coût orphelin est....



## Sur-allocation du coût


La sur-allocation du coût se produit lorsque vous obtenez en sortie un coût supérieur...



## Allocation incorrecte du coût


L'allocation incorrecte des coûts se produit lorsque...
