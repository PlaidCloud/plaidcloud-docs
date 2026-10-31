---
title: Connecteur REST Sage Intacct
description: Configurez une connexion à l'API REST de Sage Intacct dans PlaidCloud pour intégrer des données financières et comptables à vos workflows.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## Documentation de l'API

La documentation de l'API REST de Sage Intacct est disponible sur le [site Sage Developer](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Exigences de sécurité

PlaidCloud fournit une connexion **Intacct** dédiée dans la famille des connexions REST (affichée sous le nom **REST - Intacct**). Elle s'authentifie avec les informations d'identification client OAuth2 auprès de l'API REST d'Intacct : le couple Sender ID / Sender password des **Web Services** de Sage Intacct est saisi comme **ID client** et **Secret client** de la connexion, avec en plus un nom d'utilisateur du service web et un ID de société. Les identifiants d'expéditeur doivent être activés pour votre société par le support de Sage ; l'utilisateur des Web Services doit disposer des autorisations sur chaque objet Intacct que le connecteur lira.

Traitez l'ID client et le secret client comme des secrets : stockez-les uniquement via la zone **Credentials** de PlaidCloud et référencez-les depuis la connexion.


## Obtenir les identifiants

1. Ouvrez la zone **Company Setup** de Sage Intacct
2. Activez les Web Services pour le Sender ID fourni par Sage
3. Créez ou sélectionnez un utilisateur des Web Services pour PlaidCloud
4. Accordez à l'utilisateur des autorisations sur chaque objet que vous comptez interroger
5. Notez l'ID de société, le nom d'utilisateur du service web, le Sender ID et le Sender password


## Créer le connecteur Sage Intacct

1. Accédez à **Tools > Connections** et cliquez sur `Add Connection`
2. Sous **REST**, sélectionnez **Intacct** (affichée sous le nom **REST - Intacct**)
3. Saisissez :
    * **Nom de la connexion** — nom convivial affiché dans les étapes de workflow
    * **ID client** — votre Sender ID Intacct
    * **Secret client** — votre Sender password Intacct
    * **Nom d'utilisateur du service web** — l'identifiant de connexion de l'utilisateur des Web Services
    * **ID de la société** — la société Intacct à laquelle vous vous connectez
4. Cliquez sur `Test` pour valider les identifiants
5. Cliquez sur `Save`


## Utiliser dans les étapes de workflow

La même connexion sert à la fois à lire et à comptabiliser dans Intacct. Elle est sélectionnable depuis :

* L'étape [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) — en-têtes de factures fournisseur
* L'étape [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) — détail des lignes de factures fournisseur
* L'étape [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) — requête générique sur n'importe quel objet Intacct
* L'étape [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) — détail du grand livre, soldes, écritures et données de base des dimensions, avec pagination automatique
* L'étape [Intacct : comptabiliser une écriture de journal](../../../workflow-steps/sage-intacct/export-to-sage/) — comptabilise des écritures de journal
