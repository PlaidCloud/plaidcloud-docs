---
title: Run SAP PCM Console Job
description: Exécutez une tâche de console SAP PCM depuis une étape de workflow PlaidCloud pour lancer à distance des traitements par lots et des opérations d'administration.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-console-job.md
---

## Description



Lance une tâche dans la console SAP PCM sur le serveur PCM distant. Elle sert généralement aux tâches d'administration ou de traitement par lots que PCM expose via son interface de console plutôt que via l'API de calcul des modèles.

Parmi les cas d'usage figurent les opérations d'archivage, les exécutions de hyperloader ou les routines de maintenance propres à l'éditeur. La tâche exacte et ses paramètres dépendent de votre déploiement PCM.


## Nos références


PlaidCloud est un partenaire officiel de SAP et un fournisseur privilégié de services liés à la conception et à la mise en œuvre de modèles SAP PCM.








## Exemples


Sélectionnez Agent à utiliser dans la liste déroulante, saisissez le chemin du fichier de console dans le champ « Console File Path », cochez la case « Wait for Console Job to Complete » (si vous le souhaitez), puis cliquez sur « Save and Run Step ».
