---
title: Gérer les tables et les vues
description: Gérez les tables et les vues des projets PlaidCloud, y compris leur création, leur configuration, leurs autorisations et l'organisation des objets de données.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud permet d'organiser et de gérer les tables, y compris leurs libellés. Les tables sont disponibles pour tous les workflows d'un projet et offrent de nombreux outils et options.


Outre les tables, PlaidCloud propose aussi des vues fondées sur les données des tables. Les vues se mettent à jour instantanément lorsque les tables sous-jacentes changent, et économisent de l'espace de stockage.



Les options comprennent :


* Une même table peut exister sur plusieurs chemins de la hiérarchie (hiérarchies alternatives)
* Les tables peuvent recevoir des étiquettes pour faciliter la recherche et l'inclusion dans les processus PlaidCloud
* Les tables peuvent être versionnées
* Les tables peuvent être publiées pour être disponibles dans les visualisations de tableaux de bord

PlaidCloud utilise un système fondé sur des chemins pour organiser les tables, comme vous le feriez pour naviguer dans une série de dossiers, ce qui permet une organisation plus souple et plus logique des tables. Avec ce système, les tables peuvent être déplacées dans une hiérarchie, et vous pouvez créer plusieurs références vers une même table à partir d'emplacements différents de la hiérarchie (hiérarchies alternatives). La possibilité de gérer les tables de cette manière permet à la structure de refléter les besoins opérationnels, le reporting et le contrôle.



## Rechercher des tables


Utilisez la zone de filtre en bas à gauche de la hiérarchie pour rechercher dans les noms et les libellés des tables. Les résultats s'affichent dans la hiérarchie au-dessus.


### Par workflow

Le dossier **Par workflow** à la fin de l'onglet **Tables** regroupe les tables sous chaque workflow qui les lit ou les écrit. Ouvrez un workflow pour voir ses tables. Ce dossier est une vue des mêmes tables ; vous ne pouvez donc rien en déplacer ni en copier.


### Par colonne

Saisissez un nom de colonne dans la zone de recherche de colonnes de l'onglet **Tables** et appuyez sur Entrée, ou sélectionnez la loupe à côté, pour n'afficher que les tables qui possèdent une colonne portant ce nom. La recherche porte sur les noms de colonnes et non sur les données ; elle est donc rapide. Sélectionnez **Contient** pour faire correspondre une partie d'un nom de colonne plutôt que le nom entier. Videz la zone pour afficher de nouveau toutes les tables. Une longue recherche peut renvoyer ses résultats par pages, et la ligne d'état indique lorsqu'elle est encore en cours ou peut être incomplète.

Sélectionnez **Arborescence des colonnes** pour rechercher depuis une fenêtre dédiée. Chaque table qui possède la colonne s'ouvre sur deux listes :

* **Alimentée par** — les tables qui fournissent la colonne
* **Alimente** — les tables que la colonne va ensuite alimenter

Un assistant IA connecté via MCP trouve les mêmes tables avec `table_find(column=...)`, en faisant correspondre le nom entier ou une partie de celui-ci.


### Rechercher des valeurs

Pour trouver quelles tables contiennent une valeur, choisissez **Rechercher des valeurs dans les données… (lent)** dans le menu **Actions** de l'onglet **Tables**, ou faites un clic droit sur une table et choisissez cette commande pour chercher dans cette table uniquement. Saisissez la valeur, choisissez **Contient** pour faire correspondre une partie d'une valeur, puis sélectionnez **Rechercher**. Chaque table qui contient la valeur est listée avec les colonnes où elle apparaît et quelques valeurs correspondantes. Double-cliquez sur une table, ou appuyez sur Entrée dessus, pour l'ouvrir dans l'Explorateur de tables. Une colonne ouvre la table filtrée sur les lignes correspondantes. Si la zone de recherche de colonnes contient du texte, il remplit la valeur à rechercher.

Avant de lancer la recherche, sachez que :

* La recherche lit chaque ligne de chaque table recherchée ; elle peut donc être très lente et consommer beaucoup de ressources de l'entrepôt de données. La fenêtre vous en avertit, et les boutons de recherche restent désactivés jusqu'à la fin d'une recherche.
* Vous ne voyez que les lignes que vous pouviez déjà ouvrir. La sécurité au niveau des lignes s'applique à chaque recherche.
* L'historique des requêtes de votre entrepôt de données enregistre les valeurs que vous recherchez.
* La recherche couvre les colonnes de texte des tables. Les tables qui n'ont pas été construites sont ignorées et nommées dans un avertissement.
* Les résultats arrivent par pages. Lorsque la ligne d'état indique que la recherche s'est arrêtée prématurément, choisissez **Rechercher plus** pour continuer avec les tables pas encore recherchées.

Un assistant IA connecté via MCP utilise `table_value_search`. Il renvoie les tables et les colonnes qui contiennent la valeur, jamais les valeurs elles-mêmes. Lorsque vous demandez à l'assistant IA d'un projet de trouver une valeur, Weave envoie au fournisseur du modèle de langage les noms des tables et des colonnes correspondantes.



## Importer un fichier CSV

**Pour transformer un fichier CSV en nouvelle table dans ce projet :**

1. Faites glisser le fichier depuis votre ordinateur vers la liste **Tables** du projet, ou choisissez **Nouveau** > **Table à partir d'un fichier CSV** dans la barre d'outils, puis déposez le fichier dans la zone ou cliquez sur **Choisir un fichier CSV**.
2. PlaidCloud téléverse le fichier dans votre **Personal Temp Drive**, ou dans le **Temp Drive** de l'espace de travail si vous n'en avez pas, et l'importe dans une nouvelle table au premier niveau de la liste, nommée d'après le fichier : `Sales Data.csv` devient `sales_data`. Si le projet possède déjà une table portant ce nom, la nouvelle reçoit un numéro, par exemple `sales_data_2`.
3. La liste s'actualise avec la nouvelle table sélectionnée, et **Vos données en un coup d'œil** s'ouvre dessus. Consultez [Démarrer avec votre propre CSV](/fr/get-started/quickstart/#commencer-avec-votre-propre-csv) pour voir ce qu'affiche le panneau.

Seuls les fichiers se terminant par `.csv` sont acceptés. Vous avez besoin de l'autorisation de créer des tables et d'écrire dans le stockage de documents, et un projet verrouillé n'accepte pas de CSV tant qu'il n'est pas déverrouillé. Si l'importation échoue, la fenêtre en indique la raison et votre projet reste tel qu'il était. PlaidCloud supprime le fichier téléversé du lecteur temporaire une fois l'importation terminée, qu'elle ait réussi ou non ; à défaut, le lecteur temporaire le supprime au bout d'un jour.

## Déplacer


**Pour déplacer une table :**


1. Faites-la glisser dans le dossier où vous souhaitez la placer

## Renommer


**Pour renommer une table :**


1. Faites un clic droit sur la table
2. Sélectionnez l'option de renommage
3. Saisissez le nouveau nom et enregistrez-le
4. La table est maintenant renommée, mais elle conserve son identifiant unique d'origine.

## Vider


**Pour vider une table :**


1. Sélectionnez les tables dans la hiérarchie ‘
2. Cliquez sur le bouton de vidage dans la barre d'outils supérieure.

*Remarque : vous pouvez vider une seule table ou plusieurs tables*



## Supprimer


**Pour supprimer une table :**


1. Sélectionnez les tables dans la hiérarchie
2. Cliquez sur le bouton de suppression dans la barre d'outils supérieure
3. L'opération de suppression vérifie si la table est utilisée par des étapes de workflow ou des vues. Si c'est le cas, il vous sera demandé de supprimer ces associations avant que la suppression puisse avoir lieu.

*Remarque : vous pouvez aussi forcer la suppression des tables. Forcer la suppression laisse des références rompues ; à utiliser avec parcimonie.*


### Dernière lecture

La fenêtre de suppression indique quand la table a été lue pour la dernière fois, par exemple **Last read 3 days ago by** suivi d'une personne ou d'une étape, afin que vous puissiez distinguer une table que personne n'utilise d'une table encore en service. PlaidCloud tire cette information de l'historique des requêtes de votre entrepôt de données et exclut les lectures effectuées par ses propres tâches de maintenance.

| Entrepôt de données | Prérequis |
| --- | --- |
| Snowflake | Les lectures proviennent d'Access History, que Snowflake enregistre avec un retard pouvant atteindre environ 3 heures. Le rôle de la connexion a besoin du rôle de base de données `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` sur la base de données `SNOWFLAKE` fonctionne aussi). L'édition Snowflake Standard n'a pas d'Access History. |
| Databricks | Les lectures proviennent de la table de lignage, que Databricks enregistre aussi avec un délai ; une lecture récente peut donc ne pas encore apparaître. L'identité de la connexion a besoin de `USE CATALOG` sur `system`, de `USE SCHEMA` sur `system.access` et de `SELECT` sur `system.access.table_lineage`. |
| PlaidCloud Lakehouse | L'historique de lecture n'est pas encore disponible. La fenêtre affiche **Read history incomplete**. |

Lorsque vous connectez votre entrepôt de données, [le contrôle de la connexion](/fr/guides/connections/external-lakehouse/#3-vérifier-puis-lutiliser) recommande celles de ces autorisations qui manquent, chacune avec l'instruction à exécuter. Elles sont recommandées, non obligatoires : sans elles, l'entrepôt de données se connecte et la fenêtre affiche **Read history incomplete**.

Lorsque PlaidCloud ne peut pas lire l'historique complet, la ligne indique **Read history incomplete** et ne signale jamais « aucune lecture » à la place. Toute personne disposant d'un accès SQL direct à votre entrepôt de données peut définir une balise de session qui modifie la façon dont ses propres lectures sont étiquetées.

Un assistant IA connecté via MCP obtient la même réponse avec `table_describe(include=['last_read'])`.



## Afficher les colonnes d'une table


Sélectionner une table ouvre son panneau de détails. Sa section **Colonnes** liste chaque colonne avec son **Type** et sa **Description**, la description provenant de **Propriétés de la colonne**. Pointez une ligne pour lire une longue description en entier.

Une table qui n'est pas dans l'entrepôt de données pour le moment, parce que ses données ont expiré ou qu'aucune étape ne l'a construite, n'a aucune colonne à lister. La section l'indique et affiche le nombre de colonnes de la table. Exécutez une étape qui écrit la table pour les lister.


## Voir où une table est utilisée


Sélectionner une table ouvre son panneau de détails, qui liste les étapes de workflow qui la touchent :


* **Table créée par** — les étapes qui écrivent dans la table
* **La table contribue à** — les étapes qui la lisent
* **Peut référencer cette table** — les étapes qui atteignent une table via une variable qui ne peut pas être résolue. Cette section n'apparaît que s'il existe de telles étapes.


Une étape peut nommer une table directement, ou l'atteindre par un chemin contenant une variable, tel que `/Periods/{period}/Sales`. Lorsque cette variable a une valeur actuelle, l'étape apparaît dans les deux premières listes avec une icône d'information à côté. Survolez la ligne pour voir le chemin tel que l'étape l'enregistre.


Considérez ces lignes comme la réponse plus faible qu'elles sont. Elles décrivent ce qu'une exécution lancée maintenant toucherait — et non tout ce qui a jamais touché la table. Changez la variable et une autre table est lue.


Certaines variables ne peuvent pas être résolues. Soit rien n'a défini la variable, soit la valeur qu'utilise une exécution ne provient pas de ce qui est stocké — un Worklow Loop prend ses variables dans les données au fil de l'itération, une étape Set Variable les affecte pendant l'exécution, une macro reçoit ses variables de l'étape qui l'appelle, et une exécution démarrée par un capteur porte les détails propres à ce capteur. Dans chaque cas, ce qui est stocké entre les exécutions est un reliquat de la dernière exécution et non une valeur fiable. Plutôt que de les résoudre vers une table qui peut être la mauvaise, PlaidCloud liste les étapes par nom sous **Peut référencer cette table**, avec la variable qu'il n'a pas pu résoudre, afin que vous puissiez les ouvrir et vérifier.


Une étape que votre rôle ne peut pas voir est tout de même listée, afin que vous sachiez que la table est utilisée, mais sans son nom ni son workflow, et vous ne pouvez pas l'ouvrir. Elle compte toujours lorsque vous supprimez la table. Une étape que vous pouvez voir est listée sans les workflows que votre rôle masque. Rien n'est masqué à un Architecte.


*Remarque : lorsque vous supprimez des tables depuis la liste **Tables**, une étape qui atteint une table par un chemin, avec ou sans variable, compte comme l'utilisant, même lorsque sa variable ne peut pas être résolue. La fenêtre de suppression liste l'étape, et la suppression n'a lieu que si vous la forcez.*



## Créer une nouvelle structure de dossiers


**Pour ajouter un nouveau dossier :**


1. Cliquez sur le bouton Nouveau dossier dans la barre d'outils

**Pour ajouter un dossier à un dossier existant :**


1. Faites un clic droit sur le dossier
2. Sélectionnez Nouveau dossier


## Afficher les données (Explorateur de tables)


Les données d'une table s'affichent avec l'Explorateur de tables. L'Explorateur de tables propose une vue en grille des données ainsi qu'un récapitulatif colonne par colonne des valeurs et des statistiques. Le filtrage par pointer-cliquer et l'exportation vers des formats de fichier courants sont tous deux disponibles. Les sélections de filtre peuvent aussi être enregistrées sous forme d'étape Extract utilisable dans un workflow.



## Publier une table pour le reporting


Les visualisations de tableaux de bord sont volontairement limitées aux tables qui ont été publiées. Lorsque vous publiez une table, vous pouvez fournir un nom unique qui permet de distinguer les données. Cela peut être utile lorsque la table porte un nom plus obscur dans la partie du workflow qui l'a générée, mais qu'elle a besoin d'un nom plus clair pour ceux qui construisent des tableaux de bord.


Les tables publiées n'ont pas de chemins associés. Elles apparaîtront sous forme de liste de tables à utiliser dans la zone des tableaux de bord.



## Marquer une table pour les rôles de consultation


L'affichage des tables par les différents rôles peut être contrôlé en cochant les cases Explorateur ou Gestionnaire. Si plusieurs tables doivent être mises à jour, sélectionnez les tables dans la hiérarchie et choisissez le rôle de consultation souhaité dans le menu Actions de la barre d'outils supérieure.



## Mémos pour décrire le contenu d'une table


Ajoutez un mémo à une table pour mieux comprendre les données.



## Afficher la forme, la taille et l'heure de dernière mise à jour d'une table


Le nombre de lignes, de colonnes et la taille des données de chaque table sont affichés dans la hiérarchie des tables. Pour les très grandes tables (plusieurs millions de lignes), le nombre de lignes peut être estimé, et un indicateur de nombre de lignes approximatif est alors affiché.



## Afficher d'autres attributs d'une table


**Pour afficher et modifier d'autres attributs d'une table :**


1. Sélectionnez une table
2. Cliquez pour afficher le formulaire de contexte de la table à droite.


## Dupliquer une table


**Pour dupliquer une table :**


1. Sélectionnez la table
2. Cliquez sur le bouton de duplication dans la barre d'outils supérieure.


## Créer une application Panel à partir d'une table


Sélectionnez une table ou une vue et choisissez **Créer une application Panel** dans le menu **Nouveau** ou dans le menu contextuel. La boîte de dialogue **Nouvelle application Studio** s'ouvre avec le projet et la table déjà choisis. L'application prend le nom de la table ; modifiez-le si vous le souhaitez, puis choisissez **Créer**, et Panel Studio l'ouvre avec Weave prêt à construire sa première page. La commande est disponible lorsque vous sélectionnez une seule table ou vue, que vous avez un accès en modification au projet et que le projet n'est pas en lecture seule. Consultez [Créer une application Panel](/fr/guides/panel-apps/creating/#partir-dune-table).


## Voir ce que stockent les tables


La liste **Tables** affiche les colonnes **Données actuelles**, **Historique**, **Jours de Time Travel** et **Remarque** à côté de la taille de chaque table. **Jours de Time Travel** est le paramètre propre à la table ; **1** signifie qu'elle utilise la valeur par défaut du projet. La barre d'état sous la liste donne le total du projet : le volume qu'il stocke, dont la part de données actuelles et la part d'historique. Les tailles marquées **Estimation** proviennent de la forme de la table jusqu'à ce que PlaidCloud la mesure.

Choisissez **Stockage** dans la barre d'outils pour ouvrir la fenêtre **Stockage** du projet, avec des suggestions pour libérer de l'espace et les paramètres de time travel. Consultez [Gérer le stockage](/fr/guides/projects/managing-storage/#la-fenêtre-stockage-dun-projet).


## Créer un éditeur de données à partir d'une table


Vous pouvez transformer une table en éditeur de données configuré en une seule étape — sélectionnez la table et choisissez **Créer un éditeur de données à partir de la table** dans le menu **Nouveau** ou dans le menu contextuel. PlaidCloud examine les colonnes de la table et préconstruit les contrôles de saisie de l'éditeur. Consultez [Créer un éditeur de données à partir d'une table](/fr/guides/projects/managing-data-editors/#créer-un-éditeur-de-données-à-partir-dune-table) pour plus de détails.
