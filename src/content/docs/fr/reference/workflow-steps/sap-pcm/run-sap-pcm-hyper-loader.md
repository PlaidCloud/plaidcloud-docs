---
title: Étape Run SAP PCM Hyper Loader
description: Exécutez le Hyper Loader SAP PCM depuis une étape de workflow PlaidCloud pour charger en masse et à grande vitesse des données dans des modèles PCM.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## Description


Charge un modèle SAP Profitability and Cost Management (PCM) à l'aide de chargements directs de tables. Ce processus est nettement plus rapide que Databridge. Le Hyper Loader prend en charge la quasi-totalité des tables de données, d'affectations et de structure actuelles de PCM.


Voici la liste actuelle des cibles de chargement disponibles :


* Alias d'activité
* Hiérarchie dimensionnelle des activités
* Alias d'inducteur d'activité
* Hiérarchie dimensionnelle des inducteurs d'activité
* Valeur d'inducteur d'activité
* Composition par défaut de la nomenclature
* Taux unitaire externe de la nomenclature
* Composition de la nomenclature
* Volume de production de la nomenclature
* Unités vendues de la nomenclature
* Alias d'objet de coût 1
* Hiérarchie dimensionnelle de l'objet de coût 1
* Alias d'objet de coût 2
* Hiérarchie dimensionnelle de l'objet de coût 2
* Alias d'objet de coût 3
* Hiérarchie dimensionnelle de l'objet de coût 3
* Alias d'objet de coût 4
* Hiérarchie dimensionnelle de l'objet de coût 4
* Alias d'objet de coût 5
* Hiérarchie dimensionnelle de l'objet de coût 5
* Affectation d'objet de coût
* Inducteur d'objet de coût
* Alias de poste
* Alias de détail de poste
* Hiérarchie dimensionnelle des détails de poste
* Valeur de détail de poste
* Hiérarchie dimensionnelle des postes
* Affectation directe d'activité par poste
* Affectation d'inducteur de ressource par poste
* Valeur de poste
* Alias de période
* Hiérarchie dimensionnelle des périodes
* Alias d'inducteur de ressource
* Hiérarchie dimensionnelle des inducteurs de ressource
* Répartition d'inducteur de ressource
* Valeur d'inducteur de ressource
* Alias de centre de responsabilité
* Hiérarchie dimensionnelle des centres de responsabilité
* Chiffre d'affaires
* Alias de chiffre d'affaires
* Hiérarchie dimensionnelle du chiffre d'affaires
* Alias de service
* Hiérarchie dimensionnelle des services
* Alias de répartition
* Hiérarchie dimensionnelle des répartitions
* Valeur de répartition
* Alias de version
* Hiérarchie dimensionnelle des versions
* Alias de feuille de calcul 1
* Hiérarchie dimensionnelle de la feuille de calcul 1
* Alias de feuille de calcul 2
* Hiérarchie dimensionnelle de la feuille de calcul 2
* Valeur de feuille de calcul

## Nos références


PlaidCloud est un partenaire SAP officiel et un prestataire privilégié pour les services liés à la conception et à la mise en œuvre de modèles SAP PCM.


## Contrôles effectués à l'enregistrement

Chaque source de l'onglet **Étapes de chargement** est transférée vers la table de chargement choisie comme **Table de chargement cible**, avec une correspondance par nom de colonne. L'enregistrement est refusé, avec le nom de la source, dans les cas suivants :

- Une source n'a pas de table de chargement cible, ou celle-ci n'est pas une table de chargement PCM — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- Les colonnes d'une source ne correspondent pas à sa table de chargement : une colonne de la table de chargement est absente, son type diffère de celui de la table de chargement, ou elle n'a ni source, ni expression, ni constante — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* **Réinitialiser les colonnes cibles selon le schéma** remplit à nouveau les colonnes cibles d'une source à partir de sa table de chargement.
- Deux sources portent le même nom. Chaque source est exportée vers un fichier portant son nom, de sorte que l'une écraserait l'autre — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## Exemples


Sélectionnez l'agent dans la liste déroulante Agent à utiliser. Saisissez le nom du modèle et sélectionnez l'emplacement de stockage du package de chargement, puis choisissez le sous-dossier voulu. Utilisez la Sélection des données de la table ci-dessous pour sélectionner le modèle de la table source et la table de chargement cible. Inspecter la source>>propager les deux côtés de la table affichera les données. Cliquez sur « Enregistrer et exécuter » une fois les données saisies et les expressions ajoutées.
