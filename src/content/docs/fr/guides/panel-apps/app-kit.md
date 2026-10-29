---
title: Le kit d'applications Panel
description: "Créez des applications Panel aux couleurs de PlaidCloud avec le kit plaidcloud_panel : shell App, palette de commandes, FilterBar, KpiCard, DataGrid, Chart, Form, boutons d'exécution, paramètres enregistrés, impression et traductions, en mode clair et sombre."
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Le kit `plaidcloud_panel` est installé dans chaque application Panel serveur. Il donne à votre application l'apparence PlaidCloud (les mêmes couleurs, la même typographie et les mêmes espacements que le reste de la plateforme, en mode clair et sombre) ainsi qu'un ensemble de composants prêts à l'emploi pour les écrans dont la plupart des applications ont besoin : filtres, chiffres clés, grande grille de données, graphiques et formulaires. Votre application reprend automatiquement l'[image de marque de son projet](/fr/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

L'importation du kit applique aussi l'apparence PlaidCloud aux graphiques Plotly et Matplotlib.

## Partir d'un modèle

Le kit inclut une commande qui écrit une application de démarrage fonctionnelle. Exécutez-la depuis n'importe quel dossier, puis modifiez les noms de table et de colonnes :

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Option | Ce qu'elle fait |
|---|---|
| `--layout dashboard` | Filtres dans la barre latérale, deux chiffres clés et un graphique. |
| `--layout explorer` | Filtres dans la barre latérale, un nombre de lignes et une table de lignes. |
| `--table` | La table PlaidCloud que l'application lit. |
| `--filters` | Colonnes de filtrage, séparées par des virgules. La première alimente le graphique. |
| `--measure` | La colonne numérique à totaliser. |
| `--dir` | L'emplacement où écrire `app.py` et `requirements.txt`. Par défaut, le dossier courant. |

La commande s'arrête sans rien écrire si `app.py` existe déjà. Validez les deux fichiers dans votre dépôt et [publiez l'application](/fr/guides/panel-apps/creating/).

## Exemple d'application

Cette application filtre une table de ventes par région et par année, affiche deux chiffres clés, un graphique et une grille paginée des lignes correspondantes. La grille affiche les montants avec des séparateurs de milliers et les marges en pourcentages. Chaque élément suit les filtres.

```python
import panel as pn
import plaidcloud_panel as pcp
from bokeh.plotting import figure
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

sales = table("sales")
bar = pcp.FilterBar(sales, "region", "year")


def by_region(t):
    df = t.aggregate(by=["region"], total=("amount", "sum"))
    regions = df["region"].astype(str).tolist()
    fig = figure(x_range=regions, height=320, toolbar_location=None)
    fig.vbar(x=regions, top=df["total"].astype(float).tolist(), width=0.8, color=pcp.series()[0])
    return fig


def grid(t):
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"}, formats={"amount": "0,0", "margin": "0.0%"})


pcp.App(
    "Sales",
    sidebar=[bar],
    main=[
        pn.Row(
            pcp.KpiCard("Total amount", bar.table, "amount"),
            pcp.KpiCard("Orders", bar.table),
        ),
        pcp.Chart(pn.bind(by_region, bar.table), title="Amount by region"),
        pcp.Section("Orders", pn.bind(grid, bar.table)),
    ],
).servable()
```

Le schéma est le même dans toutes les applications du kit : construisez une `FilterBar` sur une table, puis liez chaque vue à `bar.table`. Une vue qui n'est pas liée à `bar.table` (ou à un widget) ne s'actualise jamais lorsque les filtres changent.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` construit le shell de l'application : un en-tête avec le titre, le logo du projet et l'utilisateur connecté, une barre latérale et une zone principale. Appelez `.servable()` sur le résultat.

- **Navigation** : transmettez `nav=[("Overview", overview_page), ("Detail", detail_page)]` pour obtenir un menu de pages en haut de la barre latérale. Chaque page est un objet Panel ou une fonction qui en renvoie un. Les fonctions s'exécutent lorsque la page est sélectionnée.
- **Thème** : l'application s'ouvre dans le thème clair. Transmettez `theme="dark"` pour l'ouvrir dans le thème sombre, ou ajoutez `?theme=dark` à l'URL. Avec `theme_toggle=True` (valeur par défaut), l'en-tête comporte un commutateur clair/sombre.
- **Image de marque** : l'application lit les couleurs de marque et le logo de son projet au démarrage d'une session. Un projet sans image de marque reçoit les valeurs PlaidCloud par défaut.
- **Palette de commandes** : appuyez sur Ctrl-K (Cmd-K sur Mac) pour rechercher et exécuter des commandes. Chaque page de `nav` est listée sous la forme **Aller à** suivi du nom de la page, et `commands={"Refresh data": refresh}` ajoute vos propres entrées, chacune composée d'un libellé et d'une fonction sans argument. Choisissez une entrée et l'application l'exécute.
- **Visite guidée de la première exécution** : `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` affiche une courte introduction pas à pas, chaque étape étant un titre et une ligne de texte. Elle apparaît en haut de la page jusqu'à ce que vous la terminiez ou l'ignoriez, puis ne vous est plus montrée.
- **Tout le reste** : les autres arguments nommés sont transmis au `FastListTemplate` de Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` crée une zone de sélection multiple avec recherche pour chaque colonne que vous nommez, listant les valeurs distinctes de cette colonne (jusqu'à 1 000, avec un avis lorsque la liste est tronquée). Une zone affiche **Tous** lorsque rien n'est sélectionné. Transmettez vos propres widgets par nom de colonne pour tout le reste.

- `bar.table` est la table restreinte par les sélections en cours. Un widget vide ne restreint pas les données.
- Les sélections sont enregistrées dans l'URL de la page (`?region=EU`), ce qui permet de partager une vue filtrée sous forme de lien.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` affiche un chiffre clé. `fn` vaut `sum`, `count`, `avg`, `min` ou `max`, calculé par le serveur sur l'ensemble de la table. Sans `column`, il affiche le nombre de lignes. Transmettez `bar.table` comme source pour que le chiffre suive les filtres.

Transmettez `drill_to=grid`, une `DataGrid`, pour ajouter un bouton **View rows** sous le chiffre. Le choisir oriente la grille vers la propre table de la carte, de sorte que la grille liste les lignes à l'origine du chiffre.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` est une vue tabulaire pour des données de toute taille. Seule la page courante est envoyée au navigateur ; la pagination, le tri, les totaux et l'export s'exécutent tous sur le serveur.

- **Pagination** : 200, 500 ou 1 000 lignes par page, avec des boutons Précédent et Suivant et un compteur de lignes.
- **Tri** : cliquez sur un en-tête de colonne. Le tri s'applique à toute la table, pas seulement à la page visible.
- **Totaux** : `totals` associe une colonne à `sum`, `count`, `avg`, `min` ou `max`. Le serveur calcule chacun sur toutes les lignes correspondantes et épingle le résultat comme dernière ligne de la grille.
- **Export** : les boutons **CSV** et **XLSX** téléchargent toutes les lignes correspondantes dans le tri courant, jusqu'à `export_cap` lignes (100 000 par défaut). Lorsque la table est plus grande, un avis vous invite à restreindre les filtres. Les cellules de texte qui commencent par `=`, `+`, `-` ou `@` sont préfixées d'une apostrophe afin qu'un tableur les lise comme du texte.
- **Formats numériques** : `formats={"margin": "0.0%", "amount": "0,0"}` définit un format d'affichage par colonne, à l'aide de chaînes de format [numbro](https://numbrojs.com/format.html). Un format `%` multiplie par 100. La ligne Total utilise le même format. Les colonnes à virgule flottante sans format affichent jusqu'à deux décimales avec des séparateurs de milliers. **Copier**, **CSV** et **XLSX** conservent les valeurs brutes.
- **Clé** : `key` est la colonne, ou la liste de colonnes, qui identifie une ligne de façon unique. Transmettez-la toujours. Consultez [Pagination stable](/fr/guides/panel-apps/data-api/#pagination-stable).

- **Regrouper par** : `group_by=["region"]` affiche une ligne par groupe, avec les mesures de `totals` et un nombre de lignes `rows`, le tout calculé par le serveur, ainsi qu'une ligne **Total** sur toutes les lignes correspondantes. Transmettez `groupable=["region", "year"]` pour ajouter un sélecteur **Regrouper par** permettant aux lecteurs de choisir les colonnes. Une grille affiche jusqu'à 1 000 groupes et vous indique lorsqu'elle a tronqué la liste. Les lignes de groupe n'ont pas de liens **Ouvrir**.
- **Mise en forme conditionnelle** : `rules` colore les cellules selon leur valeur. Chaque règle nomme une `column`, un `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` ou `between`), une `value` (`[low, high]` pour `between`) et un `token` (`success`, `warning`, `error` ou `info`), par exemple `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. La ligne Total n'est jamais colorée.
- **Copier** : le bouton **Copier** place la page courante, avec les colonnes visibles et la ligne Total, dans le presse-papiers sous forme de texte séparé par des tabulations, qui se colle dans Excel.
- **Open in PlaidCloud** : lorsque la source est une table PlaidCloud, un lien **Open in PlaidCloud** ouvre cette table.
- **Disposition de colonnes enregistrée** : `layout_key="orders"` ajoute les sélecteurs **Colonnes** et **Pinned** pour choisir et ordonner les colonnes et en épingler certaines. Le choix de chaque lecteur est enregistré sous ce nom et rétabli à sa prochaine ouverture de l'application.
- **Liens de ligne** : `row_link` est une fonction qui prend une ligne, sous forme de dictionnaire, et renvoie une adresse web, ou `None` pour aucun lien. La grille ajoute une colonne **Ouvrir** avec un lien sur chaque ligne qui en a un. Seules les adresses `http` et `https` et les chemins du même site sont transformés en liens.
- **Actualisation** : `grid.refresh()` interroge de nouveau la même source et conserve la page, le tri et le regroupement. Appelez-la après qu'une [exécution](#boutons-dexécution-et-fraîcheur) a fini d'écrire la table.

`source` est un nom de table ou une table issue de l'[API de données](/fr/guides/panel-apps/data-api/). Pour refiltrer une grille, affectez à `grid.source` une table filtrée, ou construisez une nouvelle grille à partir de `bar.table` comme le fait l'exemple.

La grille est soumise à la sécurité au niveau des lignes du lecteur : elle lit via la propre connexion de celui-ci.

## Chart

`pcp.Chart(obj, title=None, height=320)` place un graphique dans une carte titrée. `obj` peut être une figure Bokeh, un graphique hvPlot ou HoloViews, une figure Plotly, une figure Matplotlib, ou un `pn.bind(...)` qui renvoie l'un d'eux. Les axes numériques des figures Bokeh affichent des séparateurs de milliers : 800000 s'affiche donc 800,000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` dispose des widgets de saisie dans un formulaire unique doté d'un bouton d'envoi. `form.values()` renvoie `{widget.name: widget.value}` pour chaque widget nommé, et `on_submit` reçoit ce dictionnaire lorsque l'on clique sur le bouton.

## Section, Card, Tabs et Loading

| Composant | À utiliser pour |
|---|---|
| `pcp.Section(title, *objects)` | Un groupe titré directement sur l'arrière-plan de la page. |
| `pcp.Card(title, *objects)` | Un groupe titré sur une surface en relief. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Des onglets qui chargent le contenu d'un onglet lorsqu'il est sélectionné. L'onglet actif prend la couleur de la marque. |
| `pcp.Loading(height=200)` | Un espace réservé scintillant à afficher pendant le chargement des données. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` affiche un avis en ligne. `kind` vaut `error`, `warning`, `success` ou `info`.

## Boutons d'exécution et fraîcheur

`pcp.run_workflow_button(workflow_id, label=None)` ajoute un bouton qui exécute un workflow PlaidCloud en tant que personne qui a ouvert l'application, et affiche **En cours d'exécution…**, puis **Terminé** ou **Échec**. Un échec nomme les étapes en échec, au nombre de cinq au maximum. Le workflow appartient au projet de l'application, sauf si vous transmettez `project_id`.

`pcp.RunButton(label, start, status)` fait de même pour n'importe quelle tâche. `start` la lance et renvoie un identifiant d'exécution ; `status(run_id)` renvoie `"running"`, `"succeeded"` ou `"failed"`, ou `("failed", reason)` pour afficher un motif. Les deux sont des fonctions ordinaires, comme des appels à une API REST. La valeur `runs` du bouton augmente de un chaque fois qu'une exécution réussit : une vue qui doit s'actualiser ensuite s'y lie donc :

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` indique quand une table a été écrite pour la dernière fois, sous la forme **Updated 5 min ago**. L'âge évolue tant que la page reste ouverte. Transmettez `stale_after=datetime.timedelta(hours=24)` pour signaler par un avertissement les données plus anciennes, et appelez `.refresh()` après une exécution. Une table dont la date est inconnue affiche **Last update unknown** ; ce n'est jamais une erreur. `pcp.Freshness(fetch)` fait de même pour n'importe quelle source, `fetch` renvoyant la date de dernière modification des données.

## Paramètres enregistrés

`pcp.user_state` mémorise les choix de chaque personne d'une visite à l'autre, de sorte qu'une application s'ouvre comme elle a été laissée.

- `pcp.user_state.persist(widget, "region")` rétablit la valeur enregistrée dans le widget et l'enregistre à chaque modification. Une valeur enregistrée que le widget ne propose plus est ignorée.
- La page choisie dans `nav` est enregistrée automatiquement.
- Une clé qui commence par `filters.`, comme `pcp.user_state.persist(widget, "filters.region")`, contient un choix de filtre. PlaidCloud le réduit à l'accès aux lignes actuel de la personne à chaque lecture, de sorte qu'un filtre enregistré ne rétablit jamais des valeurs qu'elle ne peut plus voir.
- `pcp.user_state.get(key, default)` et `pcp.user_state.set(key, value)` enregistrent toute autre petite valeur.

Les paramètres enregistrés appartiennent à une personne dans une application, dans la limite de 8 Ko. Ils ne sont jamais partagés entre les personnes. Si PlaidCloud est inaccessible lors de l'enregistrement d'un paramètre, l'application le conserve jusqu'à la fin de la session.

## Imprimer et enregistrer au format PDF

`pcp.PrintButton()` ouvre la boîte de dialogue d'impression du navigateur, dans laquelle la destination peut être **Enregistrer au format PDF**. La page s'imprime avec la barre latérale et les contrôles masqués et l'image de marque de votre projet appliquée. Chaque `DataGrid` imprime toute sa page courante, jusqu'à 1 000 lignes, avec sa ligne Total en dernier. Une application en mode sombre s'imprime avec la palette claire.

## Langues

Les textes propres au kit, tels que les boutons, les avis, la palette de commandes, la visite guidée, les messages d'exécution et de fraîcheur et le pied de grille, apparaissent en anglais, en allemand ou en français. La langue est définie par `?lang=de` ou `?lang=fr` dans l'adresse de la page, sinon par la langue du navigateur. Les nombres utilisent les séparateurs de la langue. Vos données, noms de colonnes et libellés que vous écrivez ne sont jamais traduits.

## Budgets de performance

Un chargement de page dont le premier affichage prend plus de 3 000 ms, ou qui exécute une requête de plus de 2 000 ms, écrit un avertissement dans le journal de l'application en nommant ce qui a dépassé la limite. Les mêmes chiffres apparaissent dans l'onglet **Analyses** de [Panel Studio](/fr/guides/panel-apps/studio/#analyses). Pour définir d'autres limites pour une application, définissez ces variables d'environnement :

| Variable | Par défaut | Définit |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Les millisecondes avant le premier affichage. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Les millisecondes pour une requête. |

Une valeur qui n'est pas un nombre entier est ignorée, et la valeur par défaut s'applique.

## Couleurs pour vos propres graphiques

`pcp.series()` renvoie la palette de graphiques PlaidCloud sous forme de liste de couleurs, dans l'ordre. Utilisez-la pour que les graphiques que vous dessinez vous-même s'harmonisent avec les composants du kit, comme le fait l'exemple pour le graphique en barres.

## Étapes suivantes

- [L'API de données](/fr/guides/panel-apps/data-api/) : filtrez, paginez, comptez et agrégez des tables PlaidCloud depuis votre application.
- [Alertes et résumés](/fr/guides/panel-apps/alerts-and-digests/) : envoyez des alertes de KPI et des résumés planifiés depuis une application.
- [Image de marque du projet](/fr/guides/panel-apps/branding/) : définissez une fois vos couleurs et votre logo pour toutes les applications d'un projet.
