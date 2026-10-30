---
title: Create SAP PCM Model
description: Créez un modèle SAP PCM depuis une étape de workflow PlaidCloud pour mettre en place des structures de calcul de rentabilité et de gestion des coûts.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/create-sap-pcm-model.md
---

## Description



Crée un nouveau modèle SAP Profitability and Cost Management (PCM) vierge sur le serveur PCM. Utile pour provisionner des modèles par programmation, par exemple lorsqu'une nouvelle unité opérationnelle ou un nouveau scénario a besoin de son propre modèle et que le workflow peut en créer un plutôt que d'attendre une configuration manuelle.

La plupart des utilisateurs copieront un modèle existant servant de modèle type avec [Copy SAP PCM Model](/fr/reference/workflow-steps/sap-pcm/copy-sap-pcm-model/) (étape) plutôt que de partir d'un modèle vierge.


## Nos références


PlaidCloud est un partenaire officiel de SAP et un fournisseur privilégié de services liés à la conception et à la mise en œuvre de modèles SAP PCM.








## Exemples


Sélectionnez Agent à utiliser dans la liste déroulante. Saisissez « Nom du modèle » et sélectionnez « Model type » dans la liste déroulante (les deux se trouvent dans la section « Informations sur le modèle »). Cochez la case « Wait for Copy to Complete », puis cliquez sur « Save and Run Step ».
