---
title: Étape Call SAP Master Data Table RFC
description: Appelle un Remote Function Call (RFC) SAP ECC / S/4HANA conçu pour accéder aux tables de données de référence et en récupère les données sous forme de tableau.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## Description


Appelle un Remote Function Call (RFC) SAP ECC / S/4HANA conçu pour accéder aux tables de données de référence et en récupère les données sous forme de tableau. Ces données sont ensuite disponibles pour les processus de transformation dans PlaidCloud. L'étape permet aussi d'exporter la structure de la table de données de référence vers un fichier distinct, qui contient les noms des colonnes, leurs types de données et leur ordre.


## Exemples


### Paramètres RFC


Sélectionnez l'agent dans Agent à utiliser. Sélectionnez le Répertoire cible dans la liste déroulante, puis parcourez l'arborescence ci-dessous pour trouver le sous-dossier de destination du fichier. Nommez ensuite correctement le « Target File Name ». Sous « Function Call Information », saisissez la fonction et le Paramètre de valeur de retour, puis sélectionnez les paramètres.



Vous pouvez choisir Insérer une ligne ou Ajouter une ligne dans la section Paramètres, nommer les paramètres et leur attribuer des valeurs. Choisissez le Nombre max. de requêtes simultanées, puis sélectionnez Wait for RFC to Complete. Enregistrez et exécutez l'étape (Enregistrer et exécuter).
