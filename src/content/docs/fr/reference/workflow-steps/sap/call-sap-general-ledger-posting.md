---
title: Étape Call SAP General Ledger Posting
description: Appelle un Remote Function Call (RFC) SAP ECC / S/4HANA conçu pour comptabiliser une écriture de journal, y compris la TVA et les retenues à la source applicables.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## Description


Appelle un Remote Function Call (RFC) SAP ECC / S/4HANA conçu pour comptabiliser une écriture de journal, y compris la TVA et les retenues à la source applicables. Il peut aussi s'exécuter en mode test : le processus de comptabilisation est alors effectué sans être finalisé. Cela permet de recueillir les erreurs détectables, par exemple un compte clôturé ou un client inexistant dans la société indiquée. Le contrôle d'erreurs est complet et peut renvoyer plusieurs erreurs détectées en un seul test.


## Exemples


### Paramètres RFC


Sélectionnez l'agent dans Agent à utiliser. Sélectionnez le Répertoire cible dans la liste déroulante, puis parcourez l'arborescence ci-dessous pour trouver le sous-dossier de destination du fichier. Nommez ensuite correctement le « Target File Name ». Sous « Function Call Information », saisissez la fonction et le Paramètre de valeur de retour, puis sélectionnez les paramètres. 



Vous pouvez choisir Insérer une ligne ou Ajouter une ligne dans la section Paramètres, nommer les paramètres et leur attribuer des valeurs. Choisissez le Nombre max. de requêtes simultanées, puis sélectionnez Wait for RFC to Complete. Enregistrez et exécutez l'étape (Enregistrer et exécuter).
