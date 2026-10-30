---
title: Le kit d'applications Panel
description: "Créez des applications Panel qui ont l'apparence de PlaidCloud avec le kit plaidcloud_panel : l'enveloppe App, la palette de commandes, FilterBar, KpiCard, DataGrid, Chart, Form, les boutons d'exécution, les paramètres enregistrés, l'impression et les traductions, en thème clair et sombre."
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Toute application Panel de serveur dispose du kit `plaidcloud_panel`. Il donne à votre application l'apparence de PlaidCloud — les mêmes couleurs, la même typographie et les mêmes espacements que le reste de la plateforme, en thème clair et sombre — ainsi qu'un ensemble de composants prêts à l'emploi pour les écrans dont la plupart des applications ont besoin : filtres, chiffres clés, grande grille de données, graphiques et formulaires. Votre application reprend automatiquement l'[identité visuelle de son projet](/fr/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

L'importation du kit applique aussi l'apparence PlaidCloud aux graphiques Plotly et Matplotlib.

## Partir d'un modèle

Dans [Panel Studio](/fr/guides/panel-apps/studio/), **Nouvelle application Studio** démarre à partir d'une application vierge, d'une table ou d'une vue, d'une autre application Studio ou d'une application de la [galerie](/fr/guides/panel-apps/gallery/), sans commande à exécuter.

Pour une application que vous conservez dans un dépôt git, le kit inclut une commande qui écrit une application de démarrage fonctionnelle. Exécutez-la depuis n'importe quel dossier, puis modifiez les noms de table et de colonne :

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Option | Rôle |
|---|---|
| `--layout dashboard` | Filtres dans la barre latérale, deux chiffres clés et un graphique. |
| `--layout explorer` | Filtres dans la barre latérale, un nombre de lignes et une table de lignes. |
| `--table` | La table PlaidCloud que l'application lit. |
| `--filters` | Colonnes de filtrage, séparées par des virgules. La première alimente le graphique. |
| `--measure` | La colonne numérique à totaliser. |
| `--dir` | L'emplacement où écrire `app.py` et `requirements.txt`. Par défaut, le dossier courant. |

La commande s'arrête sans rien écrire si `app.py` existe déjà. Validez les deux fichiers dans votre dépôt et [publiez-le comme application serveur](/fr/guides/panel-apps/creating/#créer-une-application-serveur).

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

Le schéma est le même dans toute application du kit : construisez un `FilterBar` sur une table, puis liez chaque vue à `bar.table`. Une vue qui n'est pas liée à `bar.table` (ou à un widget) ne s'actualise jamais lorsque les filtres changent.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` construit l'enveloppe de l'application : un en-tête avec le titre, le logo du projet et l'utilisateur connecté, une barre latérale et une zone principale. Appelez `.servable()` sur le résultat.

- **Navigation** — transmettez `nav=[("Overview", overview_page), ("Detail", detail_page)]` pour obtenir un menu de pages en haut de la barre latérale. Chaque page est un objet Panel ou une fonction qui en renvoie un. Les fonctions s'exécutent lorsque la page est sélectionnée.
- **Thème** — l'application s'ouvre en thème clair. Transmettez `theme="dark"` pour l'ouvrir en thème sombre, ou ajoutez `?theme=dark` à l'URL. Avec `theme_toggle=True` (la valeur par défaut), l'en-tête comporte un commutateur clair/sombre.
- **Identité visuelle** — l'application lit les couleurs et le logo de la marque de son projet au démarrage d'une session. Un projet sans identité visuelle reçoit les valeurs par défaut de PlaidCloud.
- **Palette de commandes** — appuyez sur Ctrl-K (Cmd-K sur un Mac) pour rechercher et exécuter des commandes. Chaque page de `nav` est listée sous la forme **Aller à** suivi du nom de la page, et `commands={"Refresh data": refresh}` ajoute vos propres entrées, chacune composée d'un libellé et d'une fonction sans argument. Choisissez une entrée et l'application l'exécute.
- **Visite guidée de première exécution** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` affiche une courte introduction pas à pas, chaque étape étant un titre et une ligne de texte. Elle apparaît en haut de la page jusqu'à ce que vous la terminiez ou l'ignoriez, puis ne vous est plus présentée.
- **Tout le reste** — les autres arguments nommés sont transmis au `FastListTemplate` de Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` crée une zone de choix multiple avec recherche pour chaque colonne nommée, qui liste les valeurs distinctes de cette colonne (jusqu'à 1 000, avec un avertissement lorsque la liste est tronquée). Une zone affiche **Tous** lorsque rien n'est sélectionné. Transmettez vos propres widgets, par nom de colonne, pour tout autre besoin.

- `bar.table` est la table restreinte par les sélections en cours. Un widget vide ne restreint pas les données.
- Les sélections sont enregistrées dans l'URL de la page (`?region=EU`) : une vue filtrée peut donc être partagée sous forme de lien.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` affiche un chiffre clé. `fn` vaut `sum`, `count`, `avg`, `min` ou `max`, calculé par le serveur sur l'ensemble de la table. Sans `column`, elle affiche le nombre de lignes. Transmettez `bar.table` comme source pour que le chiffre suive les filtres.

Transmettez `drill_to=grid`, une `DataGrid`, pour ajouter un bouton **View rows** sous le chiffre. Le choisir oriente la grille vers la table propre à la carte, de sorte que la grille liste les lignes à l'origine du chiffre.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` est une vue tabulaire pour des données de toute taille. Seule la page en cours est envoyée au navigateur ; la pagination, le tri, les totaux et l'export s'exécutent tous sur le serveur.

- **Pagination** — 200, 500 ou 1 000 lignes par page, avec des boutons Précédent et Suivant et un compteur de lignes.
- **Tri** — cliquez sur un en-tête de colonne. Le tri s'applique à toute la table, pas seulement à la page visible.
- **Totaux** — `totals` associe une colonne à `sum`, `count`, `avg`, `min` ou `max`. Le serveur calcule chacun sur toutes les lignes correspondantes et épingle le résultat comme dernière ligne de la grille.
- **Export** — les boutons **CSV** et **XLSX** téléchargent toutes les lignes correspondantes dans le tri en cours, dans la limite de `export_cap` lignes (100 000 par défaut). Lorsque la table est plus grande, un avertissement vous invite à restreindre les filtres. Les cellules de texte qui commencent par `=`, `+`, `-` ou `@` sont précédées d'une apostrophe afin qu'un tableur les lise comme du texte.
- **Formats numériques** — `formats={"margin": "0.0%", "amount": "0,0"}` définit un format d'affichage par colonne, à l'aide des chaînes de format [numbro](https://numbrojs.com/format.html). Un format `%` multiplie par 100. La ligne Total utilise le même format. Les colonnes à virgule flottante sans format affichent jusqu'à deux décimales avec des séparateurs de milliers. **Copier**, **CSV** et **XLSX** conservent les valeurs brutes.
- **Clé** — `key` est la colonne, ou la liste de colonnes, qui identifie une ligne de façon unique. Transmettez-la toujours. Consultez [Pagination stable](/fr/guides/panel-apps/data-api/#pagination-stable).

- **Regrouper par** — `group_by=["region"]` affiche une ligne par groupe, avec les mesures de `totals` et un décompte `rows`, le tout calculé par le serveur, et une ligne **Total** sur toutes les lignes correspondantes. Transmettez `groupable=["region", "year"]` pour ajouter un sélecteur **Regrouper par** et laisser les lecteurs choisir les colonnes. Une grille affiche jusqu'à 1 000 groupes et vous indique lorsqu'elle a tronqué la liste. Les lignes de groupe n'ont pas de liens **Ouvrir**.
- **Mise en forme conditionnelle** — `rules` colore les cellules selon leur valeur. Chaque règle nomme une `column`, un `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` ou `between`), une `value` (`[low, high]` pour `between`) et un `token` (`success`, `warning`, `error` ou `info`), par exemple `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. La ligne Total n'est jamais colorée.
- **Copier** — le bouton **Copier** place sur le presse-papiers la page en cours, avec les colonnes visibles et la ligne Total, sous forme de texte séparé par des tabulations qui se colle dans Excel.
- **Open in PlaidCloud** — lorsque la source est une table PlaidCloud, un lien **Open in PlaidCloud** ouvre cette table.
- **Disposition des colonnes enregistrée** — `layout_key="orders"` ajoute les sélecteurs **Colonnes** et **Pinned** pour choisir et ordonner les colonnes et en épingler certaines. Le choix de chaque lecteur est enregistré sous ce nom et restauré à la prochaine ouverture de l'application.
- **Liens de ligne** — `row_link` est une fonction qui prend une ligne, sous forme de dictionnaire, et renvoie une adresse web, ou `None` pour aucun lien. La grille ajoute une colonne **Ouvrir** avec un lien sur chaque ligne qui en a un. Seules les adresses `http` et `https` et les chemins du même site sont liés.
- **Actualiser** — `grid.refresh()` interroge de nouveau la même source et conserve la page, le tri et le regroupement. Appelez-la une fois qu'une [exécution](#boutons-dexécution-et-fraîcheur) a fini d'écrire la table.

`source` est un nom de table ou une table de l'[API de données](/fr/guides/panel-apps/data-api/). Pour refiltrer une grille, définissez `grid.source` sur une table filtrée, ou construisez une nouvelle grille à partir de `bar.table` comme le fait l'exemple.

La grille est soumise à la sécurité au niveau des lignes du lecteur : elle lit au moyen de la connexion propre au lecteur.

## Chart

`pcp.Chart(obj, title=None, height=320)` place un graphique dans une carte titrée. `obj` peut être une figure Bokeh, un graphique hvPlot ou HoloViews, une figure Plotly, une figure Matplotlib, ou un `pn.bind(...)` qui renvoie l'un d'eux. Les axes numériques des figures Bokeh affichent des séparateurs de milliers : 800000 s'affiche donc 800 000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` dispose des widgets de saisie dans un seul formulaire avec un bouton d'envoi. `form.values()` renvoie `{widget.name: widget.value}` pour chaque widget nommé, et `on_submit` reçoit ce dictionnaire lorsque l'on clique sur le bouton.

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

`pcp.run_workflow_button(workflow_id, label=None)` ajoute un bouton qui exécute un workflow PlaidCloud en tant que personne ayant ouvert l'application, et affiche **En cours d'exécution…**, puis **Terminé** ou **Échec**. Un échec nomme les étapes en échec, jusqu'à cinq. Le workflow appartient au projet de l'application, sauf si vous transmettez `project_id`.

`pcp.RunButton(label, start, status)` fait de même pour n'importe quelle tâche. `start` la lance et renvoie un identifiant d'exécution ; `status(run_id)` renvoie `"running"`, `"succeeded"` ou `"failed"`, ou `("failed", reason)` pour afficher un motif. Les deux sont des fonctions ordinaires, comme des appels à une API REST. La valeur `runs` du bouton augmente de un chaque fois qu'une exécution réussit : une vue qui doit s'actualiser ensuite s'y lie :

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` indique quand une table a été écrite pour la dernière fois, sous la forme **Updated 5 min ago**. L'ancienneté continue d'évoluer tant que la page reste ouverte. Transmettez `stale_after=datetime.timedelta(hours=24)` pour signaler par un avertissement les données plus anciennes, et appelez `.refresh()` après une exécution. Une table dont la date est inconnue affiche **Last update unknown** ; ce n'est jamais une erreur. `pcp.Freshness(fetch)` fait de même pour n'importe quelle source, où `fetch` renvoie la date du dernier changement des données.

## Paramètres enregistrés

`pcp.user_state` mémorise les choix de chaque personne d'une visite à l'autre, de sorte qu'une application s'ouvre comme elle l'a laissée.

- `pcp.user_state.persist(widget, "region")` restaure la valeur enregistrée dans le widget et l'enregistre à chaque modification. Une valeur enregistrée que le widget ne propose plus est ignorée.
- La page choisie dans `nav` est enregistrée automatiquement.
- Une clé qui commence par `filters.`, par exemple `pcp.user_state.persist(widget, "filters.region")`, conserve un choix de filtre. PlaidCloud la restreint à l'accès aux lignes actuel de la personne à chaque lecture : un filtre enregistré ne ramène donc jamais des valeurs qu'elle ne peut plus voir.
- `pcp.user_state.get(key, default)` et `pcp.user_state.set(key, value)` enregistrent toute autre petite valeur.

Les paramètres enregistrés appartiennent à une personne dans une application, jusqu'à 8 Ko. Les paramètres ne sont jamais partagés entre personnes. Si PlaidCloud est injoignable lors de l'enregistrement d'un paramètre, l'application le conserve jusqu'à la fin de la session.

## Imprimer et enregistrer au format PDF

`pcp.PrintButton()` ouvre la boîte de dialogue d'impression du navigateur, où la destination peut être **Enregistrer au format PDF**. La page s'imprime sans la barre latérale ni les contrôles, avec l'identité visuelle de votre projet appliquée. Chaque `DataGrid` imprime toute sa page en cours, jusqu'à 1 000 lignes, avec sa ligne Total en dernier. Une application sombre s'imprime avec la palette claire.

## Langues

Les textes propres au kit, tels que les boutons, les avis, la palette de commandes, la visite guidée, les messages d'exécution et d'actualisation et le pied de grille, apparaissent en anglais, en allemand ou en français. La langue est `?lang=de` ou `?lang=fr` dans l'adresse de la page, sinon la langue du navigateur. Les nombres utilisent les séparateurs de la langue. Vos données, les noms de colonne et les libellés que vous écrivez ne sont jamais traduits.

## Budgets de performance

Un chargement de page dont le premier affichage prend plus de 3 000 ms, ou qui exécute une requête plus lente que 2 000 ms, écrit un avertissement dans le journal de l'application en nommant ce qui a dépassé. Les mêmes chiffres apparaissent dans l'onglet **Analyses** de [Panel Studio](/fr/guides/panel-apps/studio/#analyses). Pour définir d'autres limites pour une application, définissez ces variables d'environnement :

| Variable | Par défaut | Définit |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Millisecondes jusqu'au premier affichage. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Millisecondes pour une requête. |

Une valeur qui n'est pas un nombre entier est ignorée et la valeur par défaut s'applique.

## Couleurs de vos propres graphiques

`pcp.series()` renvoie la palette de graphiques PlaidCloud sous forme de liste de couleurs, dans l'ordre. Utilisez-la pour que les graphiques que vous dessinez vous-même correspondent aux composants du kit, comme le fait l'exemple pour le graphique à barres.

## Étapes suivantes

- [L'API de données](/fr/guides/panel-apps/data-api/) — filtrez, paginez, comptez et agrégez des tables PlaidCloud depuis votre application.
- [Alertes et synthèses](/fr/guides/panel-apps/alerts-and-digests/) — envoyez des alertes d'indicateurs clés et des synthèses planifiées depuis une application.
- [Identité visuelle du projet](/fr/guides/panel-apps/branding/) — définissez une fois vos couleurs et votre logo pour toutes les applications d'un projet.
