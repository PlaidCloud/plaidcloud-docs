---
title: Étape Stop PCM Model Calculation
description: Arrêtez un calcul de modèle SAP PCM en cours depuis une étape de workflow PlaidCloud pour interrompre le traitement en cas d'erreur ou de problème.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation.md
---

## Description



Interrompt un calcul de modèle SAP PCM en cours. Utile lorsqu'un calcul prend trop de temps, a été lancé avec des données d'entrée erronées, ou doit être arrêté pour libérer des ressources serveur au profit d'un travail plus prioritaire.

Si aucun calcul n'est en cours, l'étape écrit un avertissement dans le journal du workflow et continue.


## Nos références


PlaidCloud est un partenaire SAP officiel et un prestataire privilégié pour les services liés à la conception et à la mise en œuvre de modèles SAP PCM.




## Exemples


Sélectionnez l'agent dans la liste déroulante Agent à utiliser, saisissez le « Model Name », cochez la case « Wait for Copy to Complete », puis cliquez sur « Enregistrer et exécuter ».
