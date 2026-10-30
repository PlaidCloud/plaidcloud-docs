---
title: L'API de données pour les applications Panel
description: "Lisez des tables PlaidCloud depuis une application Panel avec panel_data : filtrez, paginez, comptez et agrégez sur le serveur, en tant que lecteur connecté, avec la sécurité au niveau des lignes appliquée."
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` est le moyen pour une application Panel serveur de lire une table sans charger toute la table dans l'application. Vous décrivez ce que vous voulez (les lignes correspondant à certains filtres, une page de ces lignes, un nombre de lignes, un total groupé) et la base de données de PlaidCloud fait le travail. Seul le résultat revient à l'application.

Chaque requête s'exécute en tant que personne qui consulte l'application : ses autorisations sur le projet et la [sécurité au niveau des lignes](/fr/guides/panel-apps/accessing-data/) s'appliquent donc à tout ce qui est renvoyé.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` ouvre une table du projet de l'application, c'est-à-dire le projet auquel l'application a été [affectée](/fr/guides/panel-apps/branding/#affecter-une-application-à-un-projet) lors de sa publication. Pour lire une table d'un autre projet, indiquez-le : `table("sales", project="Finance")`. Le projet peut être un identifiant, un nom ou un chemin.

Un handle de table ne change jamais. `filter` renvoie un nouveau handle : vous pouvez donc conserver celui qui n'est pas filtré et en dériver plusieurs vues.

## Filter

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Chaque argument nommé est un nom de colonne. Une valeur unique correspond aux lignes qui lui sont égales. Une liste, un tuple ou un ensemble correspond aux lignes égales à l'un de ses membres. Plusieurs arguments se combinent avec AND, et un nouvel appel à `filter` sur le résultat ajoute des conditions.

Une valeur `None`, une chaîne vide ou une liste vide laisse la colonne non filtrée. C'est ce qui permet à un widget de filtre vide de laisser les données intactes : `sales.filter(**widget_values)` fonctionne sans vérifier d'abord les valeurs vides.

Nommer une colonne qui n'existe pas lève une erreur qui indique la table et la colonne.

## Page

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` renvoie la page `n` (en comptant à partir de 1) de `size` lignes sous la forme d'un dataframe pandas.

- `sort` est une liste de noms de colonnes. Préfixez un nom par `-` pour un ordre décroissant : `["region", "-amount"]`.
- `key` est la colonne unique, ou la liste de colonnes uniques, de la table. Transmettez-la toujours.

### Pagination stable

La pagination prend une tranche d'une liste ordonnée de lignes. Chaque requête est une requête distincte. Si deux lignes sont à égalité sur les colonnes de tri, la base de données peut les renvoyer dans un ordre différent à la requête suivante : une ligne peut alors apparaître dans deux tranches ou dans aucune. `key` comble cette lacune : PlaidCloud l'ajoute après vos colonnes de tri, de sorte que l'ordre est toujours complet et que chaque ligne se retrouve dans exactement une tranche.

Sans `key`, la pagination se rabat sur un tri par toutes les colonnes. C'est lent sur une table large, et toujours instable si deux lignes sont identiques. Transmettez une clé unique chaque fois que vous paginez, et, pour la même raison, transmettez-la à [`DataGrid`](/fr/guides/panel-apps/app-kit/#datagrid).

## Count

```python
total_rows = emea.count()
```

Renvoie le nombre de lignes qui correspondent aux filtres, sous la forme d'un nombre entier.

## Aggregate

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` renvoie un dataframe avec une ligne par groupe, ordonné par les colonnes `by`. Chaque mesure est de la forme `name=(column, function)`, où la fonction est `sum`, `count`, `avg`, `min` ou `max`. Au moins une mesure est requise.

Sans `by`, vous obtenez une seule ligne de totaux sur les lignes filtrées. `limit` plafonne le nombre de groupes renvoyés.

Les colonnes décimales peuvent arriver sous forme de chaînes. Convertissez-les avec `float(...)` ou `astype(float)` avant de les représenter dans un graphique ou de les mettre en forme.

## Assembler le tout

```python
import panel as pn
import plaidcloud_panel as pcp
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

orders = table("orders")
bar = pcp.FilterBar(orders, "status")

pcp.App(
    "Orders",
    sidebar=[bar],
    main=[
        pcp.KpiCard("Open value", bar.table, "amount"),
        pn.bind(lambda t: pcp.DataGrid(t, key="order_id"), bar.table),
    ],
).servable()
```

`FilterBar`, `KpiCard` et `DataGrid` acceptent tous ces handles de table : la plupart des applications n'appellent donc jamais `page`, `count` ou `aggregate` directement. Utilisez-les lorsque vous construisez vos propres vues. Consultez [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/).

## Voir aussi

- [Lecture des données et utilisateur connecté](/fr/guides/panel-apps/accessing-data/) : se connecter en tant que lecteur, et quand utiliser `PlaidConnection` directement.
