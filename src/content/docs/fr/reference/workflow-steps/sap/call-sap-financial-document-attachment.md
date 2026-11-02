---
title: Étape Call SAP Financial Document Attachment
description: Récupérez les pièces jointes des documents financiers SAP depuis une étape de workflow PlaidCloud pour automatiser l'extraction et le traitement des documents.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Description



Joint un fichier à un document FI (comptabilité financière) précis dans SAP ECC / S/4HANA via un RFC (appel de fonction distant). Utile pour comptabiliser des pièces justificatives (factures numérisées, workflows d'approbation, copies de contrats) à côté des écritures financières qu'elles étayent.

Nécessite les identifiants RFC SAP configurés sur le connecteur SAP et le numéro du document FI cible (société, numéro de document, exercice).


## Ce qui est contrôlé à l'enregistrement

L'étape lit le chemin de chaque fichier dans une colonne `relative_file_path` parmi les colonnes de sortie de son onglet **Colonnes**, et cette colonne doit être de type texte. L'enregistrement est refusé en son absence (*The output columns must include relative_file_path, the path of each file to attach.*) ou lorsqu'elle a un autre type (*The relative_file_path column must be text, not integer.*).

Enregistrer avec une table source choisie mais sans colonnes source ou sans colonnes cibles remplit le côté vide à partir de la source, comme le ferait **Renseigner les deux tables de mappage**.


## Exemples


### Paramètres RFC


Sélectionnez l'**Agent à utiliser**. Sélectionnez le **Répertoire cible** dans la liste déroulante, puis parcourez ci-dessous pour trouver le sous-dossier de destination correct du fichier. Ensuite, nommez correctement le « Target File Name ». Sous « Function Call Information », saisissez la fonction, le **Paramètre de valeur de retour**, puis sélectionnez les paramètres.



Vous pouvez choisir **Insérer une ligne** ou **Ajouter une ligne** dans la section Paramètres, ainsi que nommer les paramètres et leur donner des valeurs. Choisissez le nombre pour **Nombre max. de requêtes simultanées**, puis sélectionnez « Wait for RFC to Complete ». Enregistrez et exécutez l'étape (**Enregistrer et exécuter**).
