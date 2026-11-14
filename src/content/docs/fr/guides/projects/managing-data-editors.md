---
title: Gérer les éditeurs de données
description: Gérez les attributions d’éditeurs de données dans les projets PlaidCloud pour contrôler qui peut modifier directement les données d’une table via l’interface de données.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

PlaidCloud permet d’organiser et de gérer les éditeurs de données, y compris leurs libellés. Les éditeurs de données permettent de modifier les données d’une table ou d’en créer par interaction de l’utilisateur.



PlaidCloud utilise un système basé sur des chemins pour organiser les éditeurs de données, comme celui que vous utiliseriez pour naviguer dans une série de dossiers, ce qui permet une organisation plus souple et plus logique (hiérarchie de contrôle) des éditeurs de données. Avec ce système, les éditeurs de données peuvent être déplacés au sein d’une hiérarchie de contrôle. Il est possible de créer plusieurs références vers un même éditeur de données à partir d’emplacements différents de la hiérarchie de contrôle (hiérarchies alternatives). La gestion des éditeurs de données selon cette méthode permet à la structure de refléter les besoins opérationnels, le reporting et le contrôle.




## Créer un éditeur de données à partir d’une table


Vous pouvez créer un éditeur de données prêt à l’emploi directement à partir d’une table existante. PlaidCloud examine les colonnes de la table et préconfigure l’éditeur : il choisit un contrôle de saisie pour chaque colonne et transforme les colonnes qui contiennent un petit ensemble de valeurs répétées en listes de choix déroulantes.


Pour créer un éditeur de données à partir d’une table :


1. Ouvrez la vue **Tables** du projet et sélectionnez une seule table
2. Ouvrez **Créer un éditeur de données à partir de la table**, depuis le menu **Nouveau** de la barre d’outils ou par un clic droit sur la table
3. PlaidCloud profile la table et ouvre la fenêtre **Configuration de l'éditeur de données** entièrement préremplie : elle définit la source et la cible sur la table sélectionnée, de sorte que vos modifications sont enregistrées directement dans celle-ci, et elle attribue à chaque colonne de l’onglet **Colonnes du formulaire** un contrôle adapté à son type de données et à ses valeurs
4. Passez en revue les colonnes et ajustez les contrôles si nécessaire
5. Cliquez sur **Enregistrer** ou **Enregistrer et fermer**

L’enregistrement crée l’éditeur ; un clic sur **Annuler** n’ajoute rien.

Lorsqu’une colonne correspond à une dimension, choisissez une hiérarchie pour elle dans l’onglet Colonnes du formulaire avant d’enregistrer. PlaidCloud bloque l’enregistrement tant qu’une colonne de dimension n’a pas de hiérarchie.


## Comment PlaidCloud configure les colonnes


Lorsque vous créez un éditeur à partir d’une table, ou que vous utilisez **Remplir à partir de la source**, PlaidCloud configure automatiquement chaque colonne :


- Les colonnes **Booléen** deviennent une case à cocher, ou une liste Vrai/Faux lorsque la colonne autorise les valeurs vides
- Les colonnes **Date** deviennent un sélecteur de date
- Les colonnes **Numérique** deviennent un champ numérique
- Les colonnes qui correspondent à une **dimension** deviennent un sélecteur de dimension, dans lequel vous choisissez la hiérarchie ; la modification d’une cellule ouvre la même arborescence de sélection de membres que celle décrite dans [Propriétés de type dimension et sélecteur de membres](/fr/guides/dimensions/dimensions/#propriétés-de-type-dimension-et-sélecteur-de-membres), avec **Tout développer**, **Tout réduire**, **Appliquer**, **Effacer** et **Annuler**
- Les colonnes dont les valeurs se répètent sur un petit ensemble, par exemple un code de statut ou de région, deviennent une **liste déroulante** qui répertorie les valeurs trouvées dans la colonne
- Les autres colonnes de **texte** deviennent un champ de texte, ou une zone de texte pour les valeurs longues
- PlaidCloud inclut les colonnes de type clé, comme les identifiants générés automatiquement, mais les marque en lecture seule

Pour les très grandes tables, PlaidCloud estime la liste des valeurs à partir d’un échantillon de lignes. Vous pouvez ensuite modifier le contrôle de n’importe quelle colonne.

Dans l’onglet **Colonnes du formulaire**, sélectionnez une colonne pour afficher une courte explication du choix de son contrôle par PlaidCloud.


## Ajuster le seuil des listes de choix


PlaidCloud ne transforme une colonne en liste déroulante que si ses valeurs se répètent sur un petit ensemble. Vous pouvez modifier ce seuil et déduire de nouveau les colonnes :


1. Dans l’onglet **Colonnes du formulaire**, définissez **Nombre max. de valeurs de liste de choix** sur le plus grand nombre de valeurs distinctes qu’une colonne peut avoir tout en devenant une liste déroulante
2. Cliquez sur **Reprofiler**

PlaidCloud réexamine la table source avec le nouveau paramètre et reconstruit les colonnes. Si l’éditeur contient déjà des colonnes, le reprofilage les remplace ; PlaidCloud vous demande donc de confirmer.


## Remplir un éditeur existant à partir d’une table


Vous pouvez appliquer la même configuration automatique à un éditeur que vous êtes déjà en train de modifier :


1. Ouvrez la configuration de l’éditeur de données et accédez à l’onglet **Source et cible**
2. Définissez la source sur une table
3. Dans l’onglet **Colonnes du formulaire**, cliquez sur **Remplir à partir de la source**

PlaidCloud ajoute une colonne configurée pour chaque colonne de la table source. Il conserve les colonnes que vous avez déjà personnalisées et vous invite à supprimer les colonnes qui ne figurent plus dans la source.


## Recherche


Pour rechercher des éditeurs de données :


1. Utilisez **Filtre** en bas de la liste, à côté du nombre de lignes (appuyez sur **/** ou sur Ctrl/Cmd+F pour y accéder directement)

Le filtre de recherche recherche des correspondances dans les noms et les libellés des éditeurs de données et affiche les résultats dans la hiérarchie.




## Déplacer


Pour déplacer un éditeur de données dans la hiérarchie de contrôle :


1. Faites-le glisser dans le dossier où vous souhaitez le placer

## Renommer


Pour renommer un éditeur de données :


1. Faites un clic droit sur l’éditeur de données
2. Sélectionnez l’option de renommage
3. Saisissez le nouveau nom et enregistrez-le

L’éditeur de données est alors renommé, mais il conserve son identifiant unique d’origine.




## Supprimer


Vous pouvez supprimer un seul éditeur de données ou plusieurs éditeurs de données.


Pour supprimer un éditeur de données :


1. Sélectionnez les éditeurs de données dans la hiérarchie de contrôle
2. Cliquez sur le bouton de suppression de la barre d’outils supérieure


## Créer une nouvelle structure de répertoires


Pour ajouter un nouveau dossier à la hiérarchie de contrôle :


1. Cliquez sur le bouton Nouveau dossier de la barre d’outils

Pour ajouter un dossier à un dossier existant :


1. Faites un clic droit sur le dossier
2. Sélectionnez Nouveau dossier


## Marquer la hiérarchie pour les rôles de consultation


La consultation des éditeurs de données par les différents rôles :


1. Cliquez sur les cases à cocher Explorateur ou Gestionnaire

Pour mettre à jour plusieurs éditeurs de données :


1. Sélectionnez les éditeurs de données dans la hiérarchie de contrôle
2. Sélectionnez le rôle de consultation souhaité dans le menu Actions de la barre d’outils supérieure


## Mémos décrivant le contenu des tables


Pour ajouter un mémo à un éditeur de données :


1. Sélectionnez l’éditeur de données
2. Mettez à jour le mémo dans le formulaire de contexte de droite


## Afficher les attributs supplémentaires de la hiérarchie


Pour afficher et modifier les attributs supplémentaires d’un éditeur de données :


1. Sélectionnez l’éditeur de données et consultez le formulaire de contexte de l’éditeur de données à droite


## Dupliquer un éditeur de données


Pour dupliquer un éditeur de données :


1. Sélectionnez l’éditeur de données
2. Cliquez sur le bouton Dupliquer de la barre d’outils supérieure


## Écrire via l’assistant IA ou MCP

Au-delà des écrans de configuration, `editor_upsert` peut définir la source, la cible et les contrôles d’un éditeur de données, et y écrire directement des lignes : `data` est une liste d’objets de ligne indexés par l’identifiant de chaque contrôle. Une date non valide est refusée avant toute modification de la table cible, de sorte qu’une écriture erronée n’est jamais appliquée partiellement.
