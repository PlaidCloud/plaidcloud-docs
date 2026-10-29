---
title: Calculate PCM Model
description: Déclenchez les calculs d'un modèle SAP PCM depuis une étape de workflow PlaidCloud afin d'exécuter les traitements de rentabilité et d'allocation des coûts.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## Description



Déclenche le moteur de calcul d'un modèle SAP Profitability and Cost Management (PCM). Utilisez-la dans un workflow pour exécuter le calcul des coûts une fois que les chargements de données en amont ont alimenté les entrées du modèle (affectations, inducteurs, données source).

Le calcul est asynchrone côté serveur PCM ; associez-la à [Stop PCM Model Calculation](/fr/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/) (étape) si vous devez interrompre un calcul de longue durée.


## Nos références


PlaidCloud est un partenaire officiel de SAP et un fournisseur privilégié de services liés à la conception et à la mise en œuvre de modèles SAP PCM.







## Exemples


Sélectionnez Agent à utiliser dans la liste déroulante, saisissez le nom du modèle dans le champ « Nom du modèle », cochez la case « Wait for Calculation to Complete » (si vous le souhaitez), puis cliquez sur « Save and Run Step ».
