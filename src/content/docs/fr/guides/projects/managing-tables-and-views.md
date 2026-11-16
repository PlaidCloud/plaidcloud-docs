---
title: Gérer les tables et les vues
description: Gérez les tables et les vues dans les projets PlaidCloud, notamment la création, la configuration, les autorisations et l’organisation des objets de données.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

PlaidCloud permet d’organiser et de gérer les tables, y compris leurs libellés. Les tables sont disponibles pour tous les workflows d’un projet et offrent de nombreux outils et options.


En plus des tables, PlaidCloud propose aussi des vues basées sur les données des tables. Les vues permettent des mises à jour instantanées lorsque les tables sous-jacentes changent, et économisent de l’espace de stockage.



Les options comprennent :


* Une même table peut exister sur plusieurs chemins de la hiérarchie (hiérarchies alternatives)
* Les tables peuvent recevoir des étiquettes pour faciliter la recherche et l’inclusion dans les processus PlaidCloud
* Les tables peuvent être versionnées
* Les tables peuvent être publiées afin d’être disponibles pour les visualisations de tableaux de bord

PlaidCloud utilise un système basé sur des chemins pour organiser les tables, comme celui que vous utiliseriez pour naviguer dans une série de dossiers, ce qui permet une organisation plus souple et plus logique des tables. Avec ce système, les tables peuvent être déplacées dans une hiérarchie, ou il est possible de créer plusieurs références vers une même table à partir d’emplacements différents de la hiérarchie (hiérarchies alternatives). La gestion des tables selon cette méthode permet à la structure de refléter les besoins opérationnels, le reporting et le contrôle.



## Rechercher des tables


Utilisez **Filtre** en bas de la liste, à côté du nombre de lignes, pour rechercher dans les noms et les libellés des tables. Appuyez sur **/** ou sur Ctrl/Cmd+F pour y accéder directement. Le même filtre s’applique à l’arborescence et à la liste à plat. Le commutateur **Tous | Published** à côté du filtre limite la liste aux tables publiées ; il est défini sur **Tous** par défaut et s’applique à la fois à l’arborescence et à la liste à plat.


### Par workflow

Le dossier **Par workflow**, à la fin de l’onglet **Tables**, regroupe les tables sous chaque workflow qui les lit ou les écrit. Ouvrez un workflow pour voir ses tables. Le dossier est une vue des mêmes tables ; vous ne pouvez donc rien en déplacer ni en copier.


### Par colonne

Sélectionnez **Rechercher une colonne** dans la barre d’outils de l’onglet **Tables** pour trouver les tables qui possèdent une colonne portant un nom donné. La recherche porte sur les noms de colonnes, pas sur les données ; elle est donc rapide. Elle ne trouve que les tables déjà générées. La fenêtre s’ouvre sur la dernière recherche que vous avez lancée dans ce projet depuis l’ouverture du projet, si vous en avez lancé une.

Saisissez au moins deux caractères et les résultats se mettent à jour pendant la saisie, ou appuyez sur Entrée pour rechercher ce que vous avez saisi. Choisissez comment le nom est comparé :

* **Exact** : le nom complet de la colonne, sans tenir compte de la casse
* **Contient** : une partie du nom de la colonne, sans tenir compte de la casse. C’est le choix par défaut.
* **Approximatif** : les noms proches, sans tenir compte de la casse, des espaces, des traits de soulignement et des autres séparateurs, et tolérant les petites fautes de frappe. Les correspondances les plus proches viennent en premier.

La fenêtre mémorise dans ce navigateur le type de correspondance que vous avez choisi en dernier. Tant que la zone de recherche est vide, elle liste vos cinq dernières recherches dans le projet ; sélectionnez-en une pour la relancer. Une recherche est considérée comme lancée et rejoint la liste lorsque vous appuyez sur Entrée, la sélectionnez dans la liste ou agissez sur ses résultats.

Chaque table correspondante occupe une ligne, avec son nom, son chemin et les trois premières colonnes correspondantes. La ligne au-dessus des résultats compte les tables trouvées jusqu’ici pendant que la recherche se poursuit. Lorsque rien ne correspond avec **Exact** ou **Contient**, sélectionnez **Essayer Approximatif ?** pour relancer la recherche avec **Approximatif**. Si la recherche échoue ou s’arrête prématurément, sélectionnez **Réessayer**. Lorsque les colonnes de certaines tables n’ont pas pu être lues, les résultats indiquent qu’ils peuvent être incomplets.

Lorsque les résultats comportent plus d’un nom de colonne, des pastilles au-dessus de la liste nomment jusqu’à 12 d’entre eux, les plus fréquents en premier, chacun avec le nombre de tables qui le possèdent. Sélectionnez une pastille pour ne lister que les tables ayant cette colonne, et sélectionnez-la de nouveau pour les lister toutes.

Développez une ligne pour voir :

* **Colonnes correspondantes** : chaque colonne correspondante, avec son type lorsqu’il s’agit de texte, d’entier, de nombre, de date, d’horodatage ou de booléen. Une colonne affichée dans la couleur d’avertissement a un type différent dans d’autres tables des résultats ; survolez-la pour voir les types.
* **Alimentée par** : les tables lues par les étapes qui écrivent cette table, chacune avec le nom de l’étape
* **Alimente** : les tables écrites par les étapes qui lisent cette table, chacune avec le nom de l’étape

Seules les étapes du même projet sont listées.

Pour agir sur les résultats :

* Double-cliquez sur une ligne, ou appuyez sur Entrée dessus, pour fermer la fenêtre et sélectionner cette table dans l’onglet **Tables**. Si une recherche de colonne affichée dans l’arborescence ou le commutateur **Tous | Published** masque la table, elle est effacée et un message vous l’indique. Appuyez sur Ctrl+Entrée, ou Cmd+Entrée sur un Mac, pour ouvrir plutôt la table dans l’Explorateur de tables. Les flèches Haut et Bas dans la zone de recherche permettent de passer d’une ligne à l’autre.
* Sélectionnez **Afficher dans l'arborescence** pour restreindre l’arborescence et la liste aplatie aux tables des résultats, ou à celles de la pastille sélectionnée, et ouvrir les dossiers de l’arborescence qui les contiennent. Une pastille au-dessus de la liste nomme la recherche et compte ses tables. Sélectionnez la pastille pour rouvrir la recherche, ou le × qu’elle contient pour afficher toutes les tables. Actualiser l’onglet **Tables** relance la recherche.
* Sélectionnez **Copier** pour copier les tables listées, une par ligne, avec le nom, le chemin, les colonnes correspondantes et leurs types de chaque table séparés par des tabulations.

**Afficher dans l'arborescence** et **Copier** sont disponibles une fois la recherche terminée avec au moins une table.

Un assistant IA connecté via MCP trouve les mêmes tables avec `table_find(column=...)`. Il fait correspondre le nom entier, une partie de celui-ci, son début ou sa fin, ou des noms proches avec `column_match='fuzzy'`, et renvoie les types des colonnes correspondantes et, pour une correspondance approximative, le degré de proximité de la meilleure colonne.


### Rechercher des valeurs

Pour trouver quelles tables contiennent une valeur, choisissez **Rechercher des valeurs dans les données… (lent)** dans le menu **Actions** de l’onglet **Tables**, ou faites un clic droit sur une table et choisissez cette option pour ne chercher que dans cette table. Saisissez la valeur, choisissez **Contient** pour faire correspondre une partie d’une valeur, puis sélectionnez **Rechercher**. Chaque table qui contient la valeur est listée avec les colonnes dans lesquelles elle apparaît et quelques-unes des valeurs correspondantes. Double-cliquez sur une table, ou appuyez sur Entrée dessus, pour l’ouvrir dans l’Explorateur de tables. Une colonne ouvre la table filtrée sur les lignes correspondantes.

Avant de lancer une recherche, sachez que :

* La recherche lit chaque ligne de chaque table recherchée ; elle peut donc être très lente et consommer beaucoup de ressources de l’entrepôt. La fenêtre vous en avertit, et les boutons de recherche restent désactivés jusqu’à la fin d’une recherche.
* Vous ne voyez que les lignes que vous pouviez déjà ouvrir. La sécurité au niveau des lignes s’applique à chaque recherche.
* L’historique des requêtes de votre entrepôt enregistre les valeurs que vous recherchez.
* La recherche porte sur les colonnes de texte des tables. Les tables qui n’ont pas été générées sont ignorées et nommées dans un avertissement.
* Les résultats arrivent par pages. Lorsque la ligne d’état indique que la recherche s’est arrêtée prématurément, choisissez **Rechercher plus** pour continuer avec les tables pas encore recherchées.

Un assistant IA connecté via MCP utilise `table_value_search`. Il renvoie les tables et les colonnes qui contiennent la valeur, jamais les valeurs elles-mêmes. Lorsque vous demandez à l’assistant IA d’un projet de trouver une valeur, Weave envoie les noms des tables et des colonnes correspondantes au fournisseur du modèle de langage.



## Importer un fichier CSV

**Pour transformer un fichier CSV en nouvelle table dans ce projet :**

1. Faites glisser le fichier depuis votre ordinateur vers la liste **Tables** du projet, ou choisissez **Nouveau** > **Table à partir d'un fichier CSV** dans la barre d’outils et déposez le fichier dans la zone ou cliquez sur **Choisir un fichier CSV**.
2. PlaidCloud téléverse le fichier dans votre **Personal Temp Drive**, ou dans le **Temp Drive** de l’espace de travail si vous n’en avez pas, et l’importe dans une nouvelle table au niveau supérieur de la liste, nommée d’après le fichier : `Sales Data.csv` devient `sales_data`. Si le projet possède déjà une table portant ce nom, la nouvelle reçoit un numéro, comme `sales_data_2`.
3. La liste s’actualise avec la nouvelle table sélectionnée, et **Vos données en un coup d'œil** s’ouvre dessus. Consultez [Commencer avec votre propre CSV](/fr/get-started/quickstart/#commencer-avec-votre-propre-csv) pour ce que le panneau affiche.

Seuls les fichiers se terminant par `.csv` sont acceptés. Vous devez avoir l’autorisation de créer des tables et d’écrire dans le stockage de documents, et un projet verrouillé n’accepte pas de CSV tant qu’il n’est pas déverrouillé. Si l’importation échoue, la fenêtre en indique la raison et votre projet reste tel qu’il était. PlaidCloud supprime le fichier téléversé du lecteur temporaire une fois l’importation terminée, qu’elle ait réussi ou non ; à défaut, le lecteur temporaire le supprime au bout d’un jour.

## Déplacer


**Pour déplacer une table :**


1. Faites-la glisser dans le dossier où vous souhaitez la placer

Pour déplacer une table au niveau supérieur du projet, faites-la glisser sur l’espace vide sous la dernière ligne. Dans les sélecteurs de dossier, `/` correspond au niveau supérieur du projet.

## Renommer


**Pour renommer une table :**


1. Faites un clic droit sur la table
2. Sélectionnez l’option de renommage
3. Saisissez le nouveau nom et enregistrez-le
4. La table est alors renommée, mais elle conserve son identifiant unique d’origine.

## Effacer


**Pour effacer une table :**


1. Sélectionnez les tables dans la hiérarchie ‘
2. Cliquez sur le bouton d’effacement de la barre d’outils supérieure.

*Remarque : vous pouvez effacer une seule table ou plusieurs tables*



## Supprimer


**Pour supprimer une table :**


1. Sélectionnez les tables dans la hiérarchie
2. Cliquez sur le bouton de suppression de la barre d’outils supérieure
3. L’opération de suppression vérifie si la table est utilisée par des étapes de workflow ou des vues. Si c’est le cas, vous êtes invité à supprimer ces associations avant que la suppression puisse avoir lieu.

*Remarque : vous pouvez aussi forcer la suppression de la ou des tables. La suppression forcée laisse des références rompues ; elle doit donc être utilisée avec parcimonie.*


### Dernière lecture

La fenêtre de suppression indique quand la table a été lue pour la dernière fois, par exemple **Last read 3 days ago by** une personne ou une étape, afin que vous puissiez distinguer une table que personne n’utilise d’une table encore utilisée. PlaidCloud tire cette information de l’historique des requêtes propre à votre entrepôt et exclut les lectures effectuées par ses propres tâches de maintenance.

| Entrepôt | Prérequis |
| --- | --- |
| Snowflake | Les lectures proviennent d’Access History, que Snowflake enregistre avec un retard pouvant atteindre environ 3 heures. Le rôle de la connexion a besoin du rôle de base de données `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` sur la base de données `SNOWFLAKE` fonctionne aussi). L’édition Snowflake Standard n’a pas d’Access History. |
| Databricks | Les lectures proviennent de la table de lignage, que Databricks enregistre aussi avec un délai ; une lecture récente peut donc ne pas apparaître encore. L’identité de la connexion a besoin de `USE CATALOG` sur `system`, de `USE SCHEMA` sur `system.access` et de `SELECT` sur `system.access.table_lineage`. |
| PlaidCloud Lakehouse | L’historique de lecture n’est pas encore disponible. La fenêtre affiche **Read history incomplete**. |

Lorsque vous connectez votre entrepôt, [le contrôle de la connexion](/fr/guides/connections/external-lakehouse/#3-vérifier-puis-lutiliser) recommande chacune de ces autorisations qui manque, avec l’instruction à exécuter. Elles sont recommandées, non obligatoires : sans elles, l’entrepôt se connecte et la fenêtre affiche **Read history incomplete**.

Lorsque PlaidCloud ne peut pas lire l’historique complet, la ligne indique **Read history incomplete** et ne signale jamais « aucune lecture » à la place. Toute personne disposant d’un accès SQL direct à votre entrepôt peut définir une balise de session qui modifie la façon dont ses propres lectures sont étiquetées.

Un assistant IA connecté via MCP obtient la même réponse avec `table_describe(include=['last_read'])`.



## Voir les colonnes d’une table


La sélection d’une table ouvre son panneau de détails. Sa section **Colonnes** liste chaque colonne avec son **Type** et sa **Description**, la description provenant de **Propriétés de la colonne**. Pointez une ligne pour lire une longue description en entier.

Une table qui n’est pas actuellement dans l’entrepôt, parce que ses données ont expiré ou qu’aucune étape ne l’a générée, n’a pas de colonnes à lister. La section l’indique et affiche le nombre de colonnes de la table. Exécutez une étape qui écrit la table pour les lister.


## Voir où une table est utilisée


La sélection d’une table ouvre son panneau de détails, qui liste les étapes de workflow qui la touchent :


* **Table créée par** : les étapes qui écrivent dans la table
* **La table contribue à** : les étapes qui la lisent
* **Peut référencer cette table** : les étapes qui atteignent une table via une variable qui ne peut pas être résolue. Cette section n’apparaît que lorsque de telles étapes existent.


La sélection d’une autre table efface immédiatement ces listes. Une étape d’un autre projet qui partage les données de ce projet, comme une étape **Importation : table de projet externe** qui lit cette table, est également listée, sans son nom ni son workflow, car vous n’avez peut-être pas accès à ce projet. Ces étapes peuvent apparaître un instant après les autres.


Une étape peut nommer une table explicitement, ou l’atteindre via un chemin contenant une variable, comme `/Periods/{period}/Sales`. Lorsque cette variable a une valeur actuelle, l’étape apparaît dans les deux premières listes avec une icône d’information à côté. Survolez la ligne pour voir le chemin tel que l’étape le stocke.


Considérez ces lignes pour la réponse plus faible qu’elles sont. Elles décrivent ce qu’une exécution démarrant maintenant toucherait, et non tout ce qui a jamais touché la table. Changez la variable et une autre table est lue.


Certaines variables ne peuvent pas être résolues. Soit rien n’a défini la variable, soit la valeur utilisée par une exécution ne provient pas de ce qui est stocké : un Workflow Loop prend ses variables dans les données au fil de l’itération, une étape Set Variable les affecte pendant l’exécution, une macro reçoit ses variables de l’étape qui l’appelle, et une exécution démarrée par un capteur porte les propres détails de ce capteur. Dans chaque cas, ce qui est stocké entre les exécutions est un reliquat de la précédente et non une valeur fiable. Plutôt que de les résoudre vers une table qui peut être la mauvaise, PlaidCloud liste les étapes par nom sous **Peut référencer cette table**, avec la variable qu’il n’a pas pu résoudre, afin que vous puissiez les ouvrir et vérifier.


Une étape que votre rôle ne peut pas voir est tout de même listée, pour que vous sachiez que la table est utilisée, mais sans son nom ni son workflow, et vous ne pouvez pas l’ouvrir. Elle compte toujours lorsque vous supprimez la table. Une étape que vous pouvez voir est listée sans les workflows que votre rôle masque. Rien n’est masqué pour un Architecte.


*Remarque : lorsque vous supprimez des tables depuis la liste **Tables**, une étape qui atteint une table via un chemin, avec ou sans variable, compte comme l’utilisant, même lorsque sa variable ne peut pas être résolue. La fenêtre de suppression liste l’étape, et la suppression n’a lieu que si vous la forcez.*



## Créer une nouvelle structure de répertoires


**Pour ajouter un nouveau dossier :**


1. Cliquez sur le bouton Nouveau dossier de la barre d’outils

**Pour ajouter un dossier à un dossier existant :**


1. Faites un clic droit sur le dossier
2. Sélectionnez Nouveau dossier

Lorsque la sélection se trouve dans un dossier, l’invite pour le nom du nouveau dossier propose aussi **Créer au niveau supérieur**. Cochez-la pour placer le nouveau dossier au niveau supérieur du projet.


## Afficher les données (Explorateur de tables)


Les données des tables s’affichent avec l’Explorateur de données. L’Explorateur de données propose une vue en grille des données ainsi qu’un résumé colonne par colonne des valeurs et des statistiques. Le filtrage par pointer-cliquer et l’exportation vers des formats de fichier courants sont tous deux disponibles. Les sélections de filtre peuvent aussi être enregistrées sous forme d’étape Extract utilisable dans un workflow.



## Publier une table pour le reporting


Les visualisations de tableaux de bord sont volontairement limitées aux tables qui ont été publiées. Lors de la publication d’une table, vous pouvez fournir un nom unique qui permet de distinguer les données. Cela peut être utile lorsque la table porte un nom plus obscur dans la partie du workflow qui l’a générée, mais qu’elle a besoin d’un nom plus clair pour les personnes qui créent des tableaux de bord.


Les tables publiées n’ont pas de chemins associés. Elles apparaissent sous forme de liste de tables à utiliser dans la zone des tableaux de bord.



## Marquer une table pour les rôles de consultation


La consultation des tables par les différents rôles peut être contrôlée en cliquant sur les cases à cocher Explorateur ou Gestionnaire. Si plusieurs tables doivent être mises à jour, sélectionnez les tables dans la hiérarchie et choisissez le rôle de consultation souhaité dans le menu Actions de la barre d’outils supérieure.



## Mémos décrivant le contenu des tables


Ajoutez un mémo à une table pour mieux comprendre les données.



## Voir la forme, la taille et l’heure de dernière mise à jour d’une table


Le nombre de lignes, le nombre de colonnes et la taille des données de chaque table sont affichés dans la hiérarchie des tables. Pour les très grandes tables (plusieurs millions de lignes), le nombre de lignes peut être estimé et un indicateur de nombre de lignes approximatif est alors affiché.



## Afficher les attributs supplémentaires d’une table


**Pour afficher et modifier les autres attributs d’une table :**


1. Sélectionnez une table
2. Cliquez pour afficher le formulaire de contexte de la table à droite.


## Dupliquer une table


**Pour dupliquer une table :**


1. Sélectionnez la table
2. Cliquez sur le bouton de duplication de la barre d’outils supérieure.


## Créer une application Panel à partir d’une table


Sélectionnez une table ou une vue et choisissez **Créer une application Panel** dans le menu **Nouveau** ou dans le menu du clic droit. La boîte de dialogue **Nouvelle application Studio** s’ouvre avec le projet et la table déjà choisis. L’application prend le nom de la table ; modifiez-le si vous le souhaitez, puis choisissez **Créer**, et Panel Studio l’ouvre avec Weave prêt à générer sa première page. La commande est disponible lorsque vous sélectionnez une seule table ou vue, que vous avez un accès en modification au projet et que le projet n’est pas en lecture seule. Consultez [Créer une application Panel](/fr/guides/panel-apps/creating/#partir-dune-table).


## Voir ce que les tables stockent


La liste **Tables** affiche les colonnes **Données actuelles**, **Historique**, **Jours de Time Travel** et **Remarque** à côté de la taille de chaque table. **Jours de Time Travel** est le paramètre propre à la table ; **1** signifie qu’elle utilise la valeur par défaut du projet. La barre d’état sous la liste donne le total du projet : ce qu’il stocke, dont la part de données actuelles et la part d’historique. Les tailles marquées **Estimation** proviennent de la forme de la table jusqu’à ce que PlaidCloud la mesure.

Choisissez **Stockage** dans le menu **Actions** pour ouvrir la fenêtre **Stockage** du projet, avec des suggestions pour libérer de l’espace et les paramètres de Time Travel. Consultez [Gérer le stockage](/fr/guides/projects/managing-storage/#la-fenêtre-stockage-dun-projet).


## Créer un éditeur de données à partir d’une table


Vous pouvez transformer une table en éditeur de données configuré en une seule étape : sélectionnez la table et choisissez **Créer un éditeur de données à partir de la table** dans le menu **Nouveau** ou dans le menu du clic droit. PlaidCloud examine les colonnes de la table et préconstruit les contrôles de saisie de l’éditeur. Consultez [Créer un éditeur de données à partir d’une table](/fr/guides/projects/managing-data-editors/#créer-un-éditeur-de-données-à-partir-dune-table) pour plus de détails.
