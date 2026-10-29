---
title: Connecteur REST SAP S/4HANA Cloud
description: Configurez une connexion SAP S/4HANA Cloud Public Edition dans PlaidCloud pour importer la balance générale et les postes d'écritures de journal via OData, et comptabiliser des écritures de journal via SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## Documentation de l'API

L'[API Trial Balance (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) et l'[API Journal Entry Item - Basic (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) de SAP S/4HANA Cloud sur SAP API Business Hub documentent les points de terminaison OData qu'utilise ce connecteur, ainsi que le service SOAP de création en masse d'écritures de journal exposé via un Communication Arrangement.

## Fonctionnement de l'authentification

La connexion s'authentifie en tant qu'application via les **informations d'identification client OAuth2** : l'ID client et le secret d'un Communication Arrangement sont échangés contre un jeton d'accès auprès du point de terminaison de jeton OAuth2 du locataire. Il n'y a aucune connexion interactive.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| Hôte | Texte | L'hôte de votre locataire S/4HANA Cloud, par exemple `https://yourorg.s4hana.ondemand.com`. |
| URL du jeton | Texte | Le point de terminaison de jeton OAuth2 du Communication Arrangement. |
| ID client | Texte | L'ID client OAuth2 du Communication Arrangement. |
| Secret client | Texte | Le secret client OAuth2 du Communication Arrangement. Stocké chiffré. |

## Entités disponibles à l'import

L'étape **Import S/4HANA Entity** couvre deux entités : `trial_balance` (soldes agrégés des comptes du grand livre en fin de période, via `API_OPLACCTGDOCITEMCUBE_SRV`) et `journal_entry_items` (postes d'écritures de journal comptabilisées, via `API_JOURNALENTRYITEMBASIC_SRV`). Les deux prennent en charge des filtres côté serveur sur `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod` et `Ledger`, avec des bornes de plage `ge`/`le` acceptées pour `PostingDate`, `FiscalYear` et `FiscalPeriod`. Consultez [Import S/4HANA Entity](/fr/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) pour la référence complète des champs.

## Comptabilisation des écritures de journal

L'étape **S/4HANA: Post Journal Entry** comptabilise des écritures de journal du grand livre via le pipeline d'écriture ERP partagé de PlaidCloud : soumission via le service SOAP `JournalEntryBulkCreateRequest_In` de S/4HANA Cloud, interrogation jusqu'à la confirmation `JournalEntryBulkCreateConfirmation_Out`, puis confirmation avant de signaler une écriture comme comptabilisée. Une correction comptabilise une nouvelle écriture d'extourne, avec débit et crédit inversés, au lieu de modifier l'écriture d'origine. Consultez [S/4HANA: Post Journal Entry](/fr/reference/workflow-steps/s4hana-cloud/s4hana-post/) pour la référence des champs, et [Se connecter à SAP S/4HANA Cloud](/fr/guides/connections/s4hana-cloud/) pour la procédure complète de comptabilisation.

## Limitations connues

| Limitation | Ce que cela signifie |
|---|---|
| Latence de confirmation | Le service SOAP de création en masse traite les requêtes de façon asynchrone, ce qui est nettement plus lent qu'une écriture OData synchrone de même taille. |
| Les champs filtrables dépendent de votre Communication Scenario | Un objet de coût ou une dimension non exposé par votre Communication Scenario ne peut pas être filtré côté serveur : limitez-le dans votre workflow après l'extraction. |

## Voir aussi

- [Se connecter à SAP S/4HANA Cloud (guide)](/fr/guides/connections/s4hana-cloud/) — pas à pas : créer la connexion, la tester, importer une entité et comptabiliser un journal.
- [Import S/4HANA Entity](/fr/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/fr/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [Consulter l'historique de comptabilisation ERP](/fr/guides/connections/erp-post-history/)
- [Connecteur SAP ECC / S/4HANA](/fr/reference/connectors/erp/sap-s4/) — le connecteur distinct, basé sur RFC et agent, pour S/4HANA sur site ou en cloud privé.
