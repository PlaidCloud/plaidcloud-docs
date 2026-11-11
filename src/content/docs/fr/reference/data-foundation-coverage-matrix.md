---
title: Matrice de couverture de Data Foundation
description: Quel jeu de données du Common Finance Model chaque système connecté à Data Foundation fournit directement, et lequel vous ajoutez sous forme de fichier.
sidebar:
  label: Couverture de Data Foundation
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundation lit directement chaque système ERP et chaque instance que vous connectez, dans un seul Common Finance Model. Les fichiers comblent ce qu'un système ne contient pas ; chacun des jeux de données ci-dessous peut donc aussi être fourni sous forme de fichier.

## Légende

| Mention | Signification |
| --- | --- |
| **Complet** | Data Foundation lit le jeu de données directement depuis le système. |
| **Complet¹** | Lu directement lorsque le système le contient. Un système sans ces données, ou une connexion sans accès à celles-ci, n'interrompt pas le chargement. |
| **Fichier** | Le système ne fournit pas ce jeu de données. Ajoutez-le sous forme de fichier. |

## SAP, Oracle et Dynamics 365

| Jeu de données | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entités | Complet | Complet | Complet | Complet | Complet | Complet |
| Calendrier fiscal | Complet | Complet | Complet | Complet | Complet | Complet |
| Plan comptable | Complet | Complet | Complet | Complet | Complet | Complet |
| Départements | Complet | Complet | Complet | Complet | Complet | Complet |
| Centres de profit | Complet¹ | Complet¹ | Fichier | Fichier | Fichier | Fichier |
| Produits | Complet | Complet | Complet | Complet¹ | Complet¹ | Complet |
| Clients | Complet | Complet | Complet | Complet¹ | Complet¹ | Complet |
| Grand livre | Complet | Complet | Complet | Complet | Complet | Complet |
| Balance de vérification | Complet | Complet | Complet | Complet | Complet | Complet |
| Lignes de vente | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Pipeline | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Soldes de stock | Complet¹ | Complet¹ | Complet¹ | Fichier | Fichier | Complet¹ |
| Budget | Complet¹ | Complet¹ | Complet¹ | Fichier | Fichier | Complet¹ |
| Inducteurs d'allocation | Complet¹ | Complet¹ | Fichier | Fichier | Fichier | Fichier |
| Taux de change | Complet | Complet | Complet | Complet | Complet | Complet |
| Valeurs de segment | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| CO-PA par valorisation | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |

## Systèmes financiers pour le marché intermédiaire et dans le cloud

| Jeu de données | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Entités | Complet | Complet | Complet | Complet | Complet | Complet |
| Calendrier fiscal | Complet | Complet | Complet | Complet | Complet | Complet |
| Plan comptable | Complet | Complet | Complet | Complet | Complet | Complet |
| Départements | Complet | Complet | Complet¹ | Complet | Complet | Complet |
| Centres de profit | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Produits | Complet | Complet | Complet¹ | Complet | Complet¹ | Complet |
| Clients | Complet | Complet | Complet¹ | Complet | Complet¹ | Complet |
| Grand livre | Complet | Complet | Complet | Complet | Complet | Complet |
| Balance de vérification | Complet | Complet | Complet | Complet | Complet | Complet |
| Lignes de vente | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet |
| Pipeline | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Soldes de stock | Fichier | Fichier | Complet¹ | Fichier | Fichier | Complet¹ |
| Budget | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Fichier | Complet¹ |
| Inducteurs d'allocation | Complet¹ | Complet¹ | Fichier | Fichier | Complet¹ | Complet |
| Taux de change | Complet | Complet | Complet¹ | Fichier | Complet | Complet¹ |
| Valeurs de segment | Fichier | Fichier | Fichier | Fichier | Complet¹ | Complet |
| CO-PA par valorisation | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |

## Sources CRM, de consolidation et de planification

| Jeu de données | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entités | Fichier | Fichier | Fichier |
| Calendrier fiscal | Fichier | Fichier | Fichier |
| Plan comptable | Fichier | Fichier | Fichier |
| Départements | Fichier | Fichier | Fichier |
| Centres de profit | Fichier | Fichier | Fichier |
| Produits | Complet¹ | Fichier | Fichier |
| Clients | Complet¹ | Fichier | Fichier |
| Grand livre | Fichier | Fichier | Fichier |
| Balance de vérification | Fichier | Fichier | Fichier |
| Lignes de vente | Fichier | Fichier | Fichier |
| Pipeline | Complet¹ | Fichier | Fichier |
| Soldes de stock | Fichier | Fichier | Fichier |
| Budget | Fichier | Complet | Complet |
| Inducteurs d'allocation | Fichier | Fichier | Fichier |
| Taux de change | Fichier | Fichier | Fichier |
| Valeurs de segment | Fichier | Fichier | Fichier |
| CO-PA par valorisation | Fichier | Fichier | Fichier |

## Remarques par système

- **Salesforce** est une source CRM. Il fournit les clients, les produits et le pipeline des ventes, jamais le grand livre.
- **OneStream** est une source de résultats. Il fournit uniquement le jeu de données de budget, en important vos résultats consolidés afin que Data Foundation puisse rapprocher le compte de résultat du groupe de ces derniers.
- **Anaplan** est une source de plan. Il fournit uniquement le jeu de données de budget, à partir d'un plan de budget, de prévision ou consolidé.
- **SAP S/4HANA et SAP ECC** lisent les mêmes données de base. ECC lit son grand livre à partir des postes de la comptabilité financière et du contrôle de gestion, et ses totaux à partir des tables de totaux du grand livre. Les centres de profit sont lus lorsque le système les contient. Les lignes de vente sont des documents de facturation, et non du CO-PA.
- **CO-PA par valorisation** n'est lu directement depuis aucun système. Ajoutez-le sous forme de fichier.
- **Workday** n'a pas de service direct de journaux ou de soldes. Data Foundation vous fournit les rapports à créer et les lit. Les valeurs de segment (worktags), les clients, les produits, les lignes de vente et les inducteurs d'effectifs proviennent de rapports facultatifs. Les budgets restent des fichiers.
- **Xero** ne fournit pas de taux de change. Ajoutez-les sous forme de fichier si vos entités utilisent plusieurs devises.
- **QuickBooks Online** lit les départements, les clients, les produits, les taux de change, les budgets, les stocks et les lignes de vente lorsque le fichier de la société les contient.
- **NetSuite** lit les segments personnalisés comme des valeurs de segment. Les taux de change et les stocks sont lus lorsque le compte les propose, et les budgets lorsque le compte utilise NetSuite Budgets et que le rôle peut les lire.

## Voir aussi

- [Data Foundation](/fr/guides/projects/data-foundation/)
- [Premiers pas avec Data Foundation](/fr/guides/projects/data-foundation-getting-started/)
- [Ajouter des fichiers pour les données extérieures à votre ERP](/fr/guides/projects/data-foundation/#ajouter-des-fichiers-pour-les-données-hors-de-votre-erp)
- Guides d'accès aux connexions :
  - [NetSuite](/fr/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/fr/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/fr/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/fr/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/fr/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/fr/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/fr/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/fr/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/fr/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/fr/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/fr/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/fr/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/fr/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/fr/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/fr/guides/connections/anaplan/#anaplan-comme-source-pour-data-foundation)
