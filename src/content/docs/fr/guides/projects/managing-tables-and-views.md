---
title: Gestion des tables et des vues
description: "Gérez les tables et les vues des projets PlaidCloud : création, configuration, autorisations et organisation des objets de données."
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud permet d'organiser et de gérer les tables, y compris leurs libellés. Les tables sont disponibles pour tous les workflows d'un projet et offrent de nombreux outils et options.


En plus des tables, PlaidCloud propose aussi des vues basées sur les données des tables. Les vues permettent une mise à jour instantanée lorsque les tables sous-jacentes changent, et économisent de l'espace de stockage.



Les options comprennent :


* Une même table peut exister sur plusieurs chemins de la hiérarchie (hiérarchies alternatives)
* Les tables peuvent recevoir des libellés pour faciliter la recherche et l'inclusion dans les processus PlaidCloud
* Les tables peuvent être versionnées
* Les tables peuvent être publiées pour être disponibles dans les visualisations de tableaux de bord

PlaidCloud utilise un système basé sur des chemins pour organiser les tables, comme lorsque vous naviguez dans une série de dossiers, ce qui permet une organisation plus souple et plus logique. Avec ce système, les tables peuvent être déplacées dans une hiérarchie, ou vous pouvez créer plusieurs références vers une même table depuis différents emplacements de la hiérarchie (hiérarchies alternatives). La gestion des tables selon cette méthode permet à la structure de refléter les besoins opérationnels, le reporting et le contrôle.



## Recherche de tables


Utilisez la zone de filtre située en bas à gauche de la hiérarchie pour rechercher dans les noms et les libellés des tables. Les correspondances s'affichent dans la hiérarchie au-dessus.


### Par workflow

Le dossier **By Workflow** à la fin de l'onglet **Tables** regroupe les tables sous chaque workflow qui les lit ou les écrit. Ouvrez un workflow pour voir ses tables. Ce dossier est une vue des mêmes tables ; vous ne pouvez donc rien en déplacer ni en copier.


### Par colonne

Saisissez un nom de colonne dans la zone de recherche de colonne de l'onglet **Tables** pour n'afficher que les tables qui possèdent une colonne portant ce nom. Sélectionnez **Contient** pour rechercher une partie du nom de colonne plutôt que le nom entier. Videz la zone pour afficher à nouveau toutes les tables. Une recherche longue peut renvoyer ses résultats par pages, et la ligne d'état indique si la recherche est encore en cours ou peut être incomplète.

Sélectionnez **Column Tree** pour effectuer la recherche dans une fenêtre dédiée. Chaque table qui possède la colonne s'ouvre sur deux listes :

* **Fed by** : les tables qui alimentent la colonne
* **Feeds** : les tables que la colonne va ensuite alimenter

Un assistant IA connecté via MCP trouve les mêmes tables avec `table_find(column=...)`, en recherchant le nom entier ou une partie de celui-ci.


### Recherche de valeurs

Pour trouver les tables qui contiennent une valeur, sélectionnez **Search Values** dans l'onglet **Tables**, ou effectuez un clic droit sur une table et choisissez **Search Value** pour ne chercher que dans cette table. Saisissez la valeur, choisissez **Contient** pour rechercher une partie d'une valeur, puis sélectionnez **Rechercher**. Chaque table qui contient la valeur est listée avec les colonnes où elle apparaît et quelques valeurs correspondantes.

Avant de lancer la recherche, notez que :

* Vous ne voyez que les lignes que vous pouviez déjà ouvrir. La sécurité au niveau des lignes s'applique à chaque recherche.
* L'historique des requêtes de votre entrepôt enregistre les valeurs que vous recherchez.
* La recherche porte sur les colonnes de texte des tables. Les tables qui n'ont pas été construites sont ignorées et nommées dans un avertissement.
* Les résultats sont paginés. Lorsque la ligne d'état indique que la recherche s'est arrêtée prématurément, choisissez **Search more** pour continuer avec les tables pas encore parcourues.

Un assistant IA connecté via MCP utilise `table_value_search`. Il renvoie les tables et les colonnes qui contiennent la valeur, jamais les valeurs elles-mêmes. Lorsque vous demandez à l'assistant IA d'un projet de trouver une valeur, Weave envoie au fournisseur du modèle de langage les noms des tables et des colonnes correspondantes.



## Importer un fichier CSV

**Pour transformer un fichier CSV en nouvelle table dans ce projet :**

1. Faites glisser le fichier depuis votre ordinateur vers la liste **Tables** du projet, ou choisissez **Nouveau** > **Table à partir d'un fichier CSV** dans la barre d'outils, puis déposez le fichier dans la zone ou cliquez sur **Choisir un fichier CSV**.
2. PlaidCloud téléverse le fichier vers votre **Personal Temp Drive**, ou vers le **Temp Drive** de l'espace de travail si vous n'en avez pas, et l'importe dans une nouvelle table au premier niveau de la liste, nommée d'après le fichier : `Sales Data.csv` devient `sales_data`. Si le projet possède déjà une table portant ce nom, la nouvelle reçoit un numéro, par exemple `sales_data_2`.
3. La liste est actualisée avec la nouvelle table sélectionnée, et **Vos données en un coup d'œil** s'ouvre sur celle-ci. Consultez [Commencer avec votre propre CSV](/fr/get-started/quickstart/#commencer-avec-votre-propre-csv) pour ce que le panneau affiche.

Seuls les fichiers se terminant par `.csv` sont acceptés. Vous devez avoir l'autorisation de créer des tables et d'écrire dans le stockage de documents, et un projet verrouillé n'accepte pas de CSV tant qu'il n'est pas déverrouillé. Si l'importation échoue, la fenêtre en indique la raison et votre projet reste tel qu'il était. PlaidCloud supprime le fichier téléversé du temp drive une fois l'importation terminée, qu'elle ait réussi ou non ; à défaut, le temp drive le supprime au bout d'un jour.

## Déplacer


**Pour déplacer une table :**


1. Faites-la glisser dans le dossier où vous souhaitez la placer

## Renommer


**Pour renommer une table :**


1. Effectuez un clic droit sur la table
2. Sélectionnez l'option de renommage
3. Saisissez le nouveau nom et enregistrez-le
4. La table est maintenant renommée, mais elle conserve son identifiant unique d'origine.

## Vider


**Pour vider une table :**


1. Sélectionnez les tables dans la hiérarchie ‘
2. Cliquez sur le bouton de vidage dans la barre d'outils supérieure.

*Remarque : vous pouvez vider une seule table ou plusieurs tables*



## Supprimer


**Pour supprimer une table :**


1. Sélectionnez les tables dans la hiérarchie
2. Cliquez sur le bouton de suppression dans la barre d'outils supérieure
3. L'opération de suppression vérifie si la table est utilisée par des étapes de workflow ou des vues. Si c'est le cas, il vous sera demandé de supprimer ces associations avant que la suppression puisse avoir lieu.

*Remarque : vous pouvez aussi forcer la suppression des tables. Une suppression forcée laisse des références rompues ; elle doit donc être utilisée avec parcimonie.*


### Dernière lecture

La fenêtre de suppression indique quand la table a été lue pour la dernière fois, par exemple **Last read 3 days ago by** une personne ou une étape, afin que vous puissiez distinguer une table que personne n'utilise d'une table encore en service. PlaidCloud tire cette information de l'historique de requêtes propre à votre entrepôt et exclut les lectures effectuées par ses propres tâches de maintenance.

| Entrepôt | Prérequis |
| --- | --- |
| Snowflake | Les lectures proviennent d'Access History, que Snowflake enregistre avec un retard pouvant atteindre environ 3 heures. Le rôle de la connexion nécessite le rôle de base de données `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` sur la base de données `SNOWFLAKE` fonctionne aussi). L'édition Snowflake Standard n'a pas d'Access History. |
| Databricks | Les lectures proviennent de la table de lignage, que Databricks enregistre aussi avec un délai ; une lecture récente peut donc ne pas encore apparaître. L'identité de la connexion nécessite `USE CATALOG` sur `system`, `USE SCHEMA` sur `system.access` et `SELECT` sur `system.access.table_lineage`. |
| PlaidCloud Lakehouse | L'historique des lectures n'est pas encore disponible. La fenêtre affiche **Read history incomplete**. |

Lorsque vous connectez votre entrepôt, [le contrôle de la connexion](/fr/guides/connections/external-lakehouse/#3-vérifier-puis-lutiliser) recommande les autorisations manquantes parmi celles-ci, chacune avec l'instruction à exécuter. Elles sont recommandées, et non obligatoires : sans elles, l'entrepôt se connecte et la fenêtre affiche **Read history incomplete**.

Lorsque PlaidCloud ne peut pas lire l'historique complet, la ligne indique **Read history incomplete** et ne signale jamais « aucune lecture » à la place. Toute personne disposant d'un accès SQL direct à votre entrepôt peut définir une étiquette de session qui modifie la façon dont ses propres lectures sont libellées.

Un assistant IA connecté via MCP obtient la même réponse avec `table_describe(include=['last_read'])`.



## Voir où une table est utilisée


La sélection d'une table ouvre son panneau de détails, qui liste les étapes de workflow qui la touchent :


* **Table créée par** : les étapes qui écrivent dans la table
* **La table contribue à** : les étapes qui la lisent
* **Peut référencer cette table** : les étapes qui atteignent une table via une variable qui ne peut pas être résolue. Cette section n'apparaît que lorsqu'il existe de telles étapes.


Une étape peut nommer directement une table, ou l'atteindre via un chemin contenant une variable, comme `/Periods/{period}/Sales`. Lorsque cette variable a une valeur actuelle, l'étape apparaît dans les deux premières listes avec une icône d'information à côté. Survolez la ligne pour voir le chemin tel que l'étape le stocke.


Considérez ces lignes comme la réponse plus faible qu'elles sont. Elles décrivent ce qu'une exécution lancée maintenant toucherait, et non tout ce qui a jamais touché la table. Changez la variable et c'est une autre table qui est lue.


Certaines variables ne peuvent pas être résolues. Soit rien n'a défini la variable, soit la valeur utilisée par une exécution ne provient pas de ce qui est stocké : une boucle de workflow (Workflow Loop) prend ses variables dans les données au fil de l'itération, une étape Set Variable affecte pendant l'exécution, une macro reçoit ses variables de l'étape qui l'appelle, et une exécution démarrée par un capteur porte les détails propres à ce capteur. Dans chacun de ces cas, ce qui est stocké entre les exécutions est un reliquat de la dernière exécution et non une valeur fiable. Plutôt que de les résoudre vers une table qui pourrait être la mauvaise, PlaidCloud liste les étapes par nom sous **Peut référencer cette table**, avec la variable qu'il n'a pas pu résoudre, afin que vous puissiez les ouvrir et les vérifier.


Une étape que votre rôle ne peut pas voir est tout de même listée, pour que vous sachiez que la table est utilisée, mais sans son nom ni son workflow, et vous ne pouvez pas l'ouvrir. Elle compte quand même lorsque vous supprimez la table. Une étape que vous pouvez voir est listée sans les workflows que votre rôle ne peut pas voir. Rien n'est masqué pour un Architecte.


*Remarque : lorsque vous supprimez des tables depuis la liste **Tables**, une étape qui atteint une table via un chemin, avec ou sans variable, compte comme l'utilisant, même si sa variable ne peut pas être résolue. La fenêtre de suppression liste l'étape, et la suppression n'a lieu que si vous la forcez.*



## Création d'une arborescence de dossiers


**Pour ajouter un dossier :**


1. Cliquez sur le bouton Nouveau dossier dans la barre d'outils

**Pour ajouter un dossier dans un dossier existant :**


1. Effectuez un clic droit sur le dossier
2. Sélectionnez Nouveau dossier


## Afficher les données (Explorateur de tables)


Les données d'une table sont consultées avec l'Explorateur de données. L'Explorateur de données propose une vue en grille des données ainsi qu'un récapitulatif colonne par colonne des valeurs et des statistiques. Le filtrage par pointer-cliquer et l'exportation vers des formats de fichier courants sont tous deux disponibles. Les sélections de filtre peuvent aussi être enregistrées sous la forme d'une étape Extract utilisable dans un workflow.



## Publier une table pour le reporting


Les visualisations de tableaux de bord sont volontairement limitées aux tables qui ont été publiées. Lors de la publication d'une table, vous pouvez lui donner un nom unique qui permet de distinguer les données. C'est utile lorsque la table porte un nom plus obscur dans la partie du workflow qui l'a générée, mais qu'elle nécessite un nom plus clair pour les personnes qui créent des tableaux de bord.


Les tables publiées n'ont pas de chemin associé. Elles apparaissent sous la forme d'une liste de tables à utiliser dans la zone des tableaux de bord.



## Marquer une table pour les rôles de visualisation


La visualisation des tables par les différents rôles se contrôle en cochant les cases Explorateur ou Gestionnaire. Si plusieurs tables doivent être mises à jour, sélectionnez-les dans la hiérarchie et choisissez le rôle de visualisation souhaité dans le menu Actions de la barre d'outils supérieure.



## Mémos pour décrire le contenu des tables


Ajoutez un mémo à une table pour mieux comprendre les données.



## Afficher la forme, la taille et l'heure de dernière mise à jour d'une table


Le nombre de lignes, de colonnes et la taille des données de chaque table sont affichés dans la hiérarchie des tables. Pour les très grandes tables (plusieurs millions de lignes), le nombre de lignes peut être estimé et un indicateur de nombre de lignes approximatif est alors affiché.



## Afficher des attributs supplémentaires d'une table


**Pour afficher et modifier d'autres attributs d'une table :**


1. Sélectionnez une table
2. Cliquez pour afficher le formulaire de contexte de la table à droite.


## Dupliquer une table


**Pour dupliquer une table :**


1. Sélectionnez la table
2. Cliquez sur le bouton de duplication dans la barre d'outils supérieure.


## Créer un éditeur de données à partir d'une table


Vous pouvez transformer une table en éditeur de données configuré en une seule étape : sélectionnez la table et choisissez **Créer un éditeur de données à partir de la table** dans le menu **Nouveau** ou dans le menu contextuel. PlaidCloud examine les colonnes de la table et prépare à l'avance les contrôles de saisie de l'éditeur. Consultez [Créer un éditeur de données à partir d'une table](/fr/guides/projects/managing-data-editors/#créer-un-éditeur-de-données-à-partir-dune-table) pour plus de détails.
