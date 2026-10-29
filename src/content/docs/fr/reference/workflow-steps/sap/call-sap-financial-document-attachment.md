---
title: Étape Call SAP Financial Document Attachment
description: Récupérez les pièces jointes de documents financiers SAP depuis une étape de workflow PlaidCloud pour automatiser l'extraction et le traitement des documents.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Description



Joint un fichier à un document FI (Financial Accounting) précis dans SAP ECC / S/4HANA via un RFC (Remote Function Call). Utile pour enregistrer des justificatifs — factures numérisées, circuits d'approbation, copies de contrats — avec les écritures financières qu'ils appuient.

Nécessite les identifiants RFC SAP configurés sur le connecteur SAP et le numéro du document FI cible (société, numéro de document, exercice).


## Contrôles effectués à l'enregistrement

L'étape lit le chemin de chaque fichier dans une colonne `relative_file_path` parmi les colonnes de sortie de son onglet **Sélection des données de la table**, et cette colonne doit être de type texte. L'enregistrement est refusé si elle est absente — *The output columns must include relative_file_path, the path of each file to attach.* — ou si elle a un autre type — *The relative_file_path column must be text, not integer.*

Si vous enregistrez avec une table source choisie mais sans colonnes source ou cible, le côté vide est rempli à partir de la source, comme le ferait **Renseigner les deux tables de mappage**.


## Exemples


### Paramètres RFC


Sélectionnez l'agent dans Agent à utiliser. Sélectionnez le Répertoire cible dans la liste déroulante, puis parcourez l'arborescence ci-dessous pour trouver le sous-dossier de destination du fichier. Nommez ensuite correctement le « Target File Name ». Sous « Function Call Information », saisissez la fonction et le Paramètre de valeur de retour, puis sélectionnez les paramètres.



Vous pouvez choisir Insérer une ligne ou Ajouter une ligne dans la section Paramètres, nommer les paramètres et leur attribuer des valeurs. Choisissez le Nombre max. de requêtes simultanées, puis sélectionnez Wait for RFC to Complete. Enregistrez et exécutez l'étape (Enregistrer et exécuter).
