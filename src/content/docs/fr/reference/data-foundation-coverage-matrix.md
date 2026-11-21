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
| **Complet¹** | Lu directement lorsque le système le contient. Un système sans ces données n'interrompt pas le chargement. Une connexion sans accès à celles-ci laisse ce jeu de données vide ou fait échouer ce seul jeu de données, et le reste se charge. |
| **Fichier** | Le système ne fournit pas ce jeu de données. Ajoutez-le sous forme de fichier. |

## SAP, Oracle et Dynamics 365

| Jeu de données | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entités | Complet | Complet | Complet | Complet | Complet | Complet |
| Calendrier fiscal | Complet | Complet | Complet | Complet | Complet | Complet |
| Plan comptable | Complet | Complet | Complet | Complet | Complet | Complet |
| Départements | Complet | Complet | Complet | Complet | Complet | Complet |
| Centres de profit | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Fichier | Complet¹ |
| Sites | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Projets | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Commerciaux | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Produits | Complet | Complet | Complet | Complet¹ | Complet¹ | Complet |
| Clients | Complet | Complet | Complet | Complet¹ | Complet¹ | Complet |
| Fournisseurs | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Grand livre | Complet | Complet | Complet | Complet | Complet | Complet |
| Balance de vérification | Complet | Complet | Complet | Complet | Complet | Complet |
| Solde de fin de mois | Fichier | Complet¹ | Fichier | Complet¹ | Complet¹ | Fichier |
| Soldes bancaires | Fichier | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ |
| Lignes de vente | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Pipeline | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Lignes de factures fournisseurs | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Bons de commande | Complet¹ | Complet¹ | Fichier | Complet¹ | Complet¹ | Fichier |
| Postes ouverts | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Paiements | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Soldes de stock | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Coûts standard | Complet¹ | Complet¹ | Fichier | Complet¹ | Complet¹ | Fichier |
| Immobilisations | Complet¹ | Complet¹ | Fichier | Complet¹ | Complet¹ | Fichier |
| Mouvements d'immobilisations | Complet¹ | Complet¹ | Fichier | Complet¹ | Complet¹ | Fichier |
| Budget | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Inducteurs d'allocation | Complet¹ | Complet¹ | Fichier | Fichier | Fichier | Fichier |
| Taux de change | Complet | Complet | Complet | Complet | Complet | Complet |
| Valeurs de segment | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| CO-PA par valorisation | Complet¹ | Complet¹ | Fichier | Fichier | Fichier | Fichier |

## Systèmes financiers pour le marché intermédiaire et dans le cloud

| Jeu de données | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entités | Complet | Complet | Complet | Complet | Complet | Complet | Complet |
| Calendrier fiscal | Complet | Complet | Complet | Complet | Complet | Complet | Complet |
| Plan comptable | Complet | Complet | Complet | Complet | Complet | Complet | Complet |
| Départements | Complet | Complet¹ | Complet | Fichier | Complet¹ | Complet | Complet |
| Centres de profit | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Fichier | Complet¹ |
| Sites | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Fichier | Complet¹ |
| Projets | Fichier | Fichier | Complet¹ | Fichier | Fichier | Fichier | Fichier |
| Commerciaux | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Complet¹ |
| Produits | Complet | Fichier | Complet | Complet¹ | Complet¹ | Complet¹ | Complet |
| Clients | Complet | Fichier | Complet | Complet¹ | Complet¹ | Complet¹ | Complet |
| Fournisseurs | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Grand livre | Complet | Complet | Complet | Complet | Complet | Complet | Complet |
| Balance de vérification | Complet | Complet | Complet | Complet | Complet | Complet | Complet |
| Solde de fin de mois | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Fichier |
| Soldes bancaires | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Lignes de vente | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet |
| Pipeline | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Lignes de factures fournisseurs | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Postes ouverts | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Paiements | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Bons de commande | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Soldes de stock | Complet¹ | Fichier | Fichier | Complet¹ | Fichier | Fichier | Complet¹ |
| Coûts standard | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Immobilisations | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Mouvements d'immobilisations | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |
| Budget | Complet¹ | Fichier | Complet¹ | Complet¹ | Complet¹ | Complet¹ | Complet¹ |
| Inducteurs d'allocation | Complet¹ | Fichier | Complet¹ | Fichier | Fichier | Complet¹ | Complet |
| Taux de change | Complet | Fichier | Complet | Complet¹ | Fichier | Complet | Complet¹ |
| Valeurs de segment | Fichier | Fichier | Fichier | Fichier | Fichier | Complet¹ | Complet¹ |
| CO-PA par valorisation | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier | Fichier |

## Sources CRM, de consolidation et de planification

| Jeu de données | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entités | Fichier | Fichier | Fichier |
| Calendrier fiscal | Complet¹ | Fichier | Fichier |
| Plan comptable | Fichier | Fichier | Fichier |
| Départements | Fichier | Fichier | Fichier |
| Centres de profit | Fichier | Fichier | Fichier |
| Projets | Complet¹ | Fichier | Fichier |
| Commerciaux | Complet¹ | Fichier | Fichier |
| Produits | Complet¹ | Fichier | Fichier |
| Clients | Complet¹ | Fichier | Fichier |
| Grand livre | Fichier | Fichier | Fichier |
| Balance de vérification | Fichier | Fichier | Fichier |
| Lignes de vente | Fichier | Fichier | Fichier |
| Pipeline | Complet¹ | Fichier | Fichier |
| Commandes clients | Complet¹ | Fichier | Fichier |
| Soldes de stock | Fichier | Fichier | Fichier |
| Budget | Fichier | Complet | Complet |
| Inducteurs d'allocation | Fichier | Complet¹ | Complet¹ |
| Taux de change | Fichier | Fichier | Fichier |
| Valeurs de segment | Fichier | Fichier | Fichier |
| CO-PA par valorisation | Fichier | Fichier | Fichier |

## Remarques par système

- **Les commandes clients, les contrats, les produits constatés d'avance et les mouvements de stock** ne sont lus depuis aucun système, à l'exception des commandes Salesforce. Ajoutez-les sous forme de fichiers.
- **Salesforce** est une source CRM. Il fournit les clients, les produits, le pipeline des ventes, les commerciaux (utilisateurs), les campagnes en tant que projets, ses mois fiscaux et les commandes, jamais le grand livre. Les commandes nécessitent que Orders soit activé dans Salesforce. Lorsque Salesforce refuse la lecture des commandes, seuls les mois de commandes échouent, et ils conservent ce qu'ils avaient chargé en dernier.
- **OneStream** est une source de résultats. Il fournit le jeu de données de budget, en important vos résultats consolidés afin que Data Foundation puisse rapprocher le compte de résultat du groupe de ces derniers, et un scénario Budget ou Forecast comme plan. Un second adaptateur facultatif fournit les effectifs et les unités planifiés comme inducteurs d'allocation.
- **Anaplan** est une source de plan. Il fournit le jeu de données de budget, à partir d'un plan de budget, de prévision ou consolidé, et des inducteurs d'allocation à partir d'un second export facultatif.
- **SAP S/4HANA et SAP ECC** lisent les mêmes données de base, les fournisseurs, les factures fournisseurs, les bons de commande, les postes ouverts, les paiements, le registre des immobilisations et les coûts standard. ECC lit son grand livre à partir des postes de la comptabilité financière et du contrôle de gestion, et ses totaux et son solde de fin de mois à partir de la table de totaux du grand livre. Les centres de profit et les usines (sites) sont lus lorsque le système les contient. Les lignes de vente sont des documents de facturation. Le CO-PA par valorisation est lu à partir de la table des postes individuels du périmètre d'analyse que vous nommez ; si aucune n'est nommée, ajoutez-le sous forme de fichier.
- **Oracle E-Business Suite** lit les sites et les centres de profit à partir du segment du plan comptable que vous nommez pour chacun.
- **Oracle Fusion** lit chaque jeu de données facultatif à partir de son propre rapport BI Publisher. Un rapport de clients, de produits, de sites ou de fournisseurs que vous ne déployez pas laisse ce jeu de données vide avec un avertissement ; le jeu de données de tout autre rapport échoue et conserve ce qu'il avait chargé en dernier ; tout le reste se charge.
- **Workday** n'a pas de service direct de journaux ou de soldes. Data Foundation vous fournit les rapports à créer et les lit. Les valeurs de segment (worktags), les clients, les produits, les fournisseurs, les lignes de vente, les sous-livres, les soldes bancaires, les budgets et les inducteurs proviennent de rapports facultatifs, et le solde de fin de mois provient du solde de clôture du rapport des soldes d'ouverture.
- **Sage 100** est lu par l'intermédiaire d'un agent PlaidLink, une société par connexion. Il tient ses livres dans une seule devise : il ne fournit donc pas de taux de change, et Data Foundation ne lit ni ses produits, ni ses clients, ni ses lignes de vente. Les départements sont lus à partir du segment de département du compte lorsque le masque de compte en comporte un.
- **Xero** ne fournit pas de taux de change. Ajoutez-les sous forme de fichier si vos entités utilisent plusieurs devises. Les départements, les sites et les centres de profit sont les options des catégories de suivi nommées exactement Department, Site et Profit centre. Xero autorise deux catégories de suivi : une organisation dispose donc d'au plus deux des trois.
- **QuickBooks Online** n'a pas de départements : ses emplacements sont lus comme des sites et ses classes comme des centres de profit. Les clients, les produits, les fournisseurs, les taux de change, les budgets, les stocks, les ventes et les achats sont lus lorsque la société les contient, et les stocks uniquement lorsque la société suit les quantités en stock.
- **NetSuite** lit les segments personnalisés comme des valeurs de segment, les classes comme des centres de profit et les emplacements comme des sites. Les taux de change et les stocks sont lus lorsque le compte les propose, et les budgets lorsque le compte utilise NetSuite Budgets et que le rôle peut les lire.

## Solde de fin de mois

Data Foundation lit le solde de clôture que chaque système publie lui-même à chaque fin de mois (consultez [Peut-on se fier aux chiffres ?](/fr/guides/projects/data-foundation-proof/)) à partir de :

| Système | Solde de fin de mois lu à partir de |
| --- | --- |
| SAP ECC | La table de totaux du grand livre (`FAGLFLEXT`, ou `GLT0` sur le grand livre classique) |
| Oracle E-Business Suite | `GL_BALANCES`, qui doit contenir chaque période |
| Oracle Fusion | Le rapport PlaidCloudBalances, couvrant chaque période |
| Business Central | La balance de vérification à chaque fin de mois |
| Sage Intacct | Les soldes de comptes (le solde de clôture de chaque mois) |
| QuickBooks Online | Le rapport Trial Balance à chaque fin de mois |
| Xero | Le rapport Trial Balance à chaque fin de mois |
| Workday | Le solde de clôture du rapport Beginning Balances |

SAP S/4HANA, SAP S/4HANA Cloud, Dynamics 365 Finance and Operations, NetSuite et Sage 100 ne publient pas de solde distinct que Data Foundation lit. Ils se chargent et fonctionnent normalement. Lorsque Business Central refuse sa balance de vérification à une fin de mois, le solde de ce mois échoue et conserve ce qu'il avait chargé en dernier.

## Détail des journaux

Outre les montants, chaque ligne du grand livre porte le type du journal, sa date de document, qui l'a saisi et quand, qui l'a approuvé, le journal qu'il contrepasse et sa taxe, lorsque le système les contient. Le calendrier fiscal porte le statut de chaque période.

| Système | Type de journal | Date du document | Saisi par et quand | Approbateur | Contrepassation | Taxe | Statut de la période |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Oui | Oui | Oui | Non | Non | Code | Oui |
| SAP ECC | Oui | Oui | Oui | Non | Oui | Code et montant | Oui |
| SAP S/4HANA Cloud | Oui | Oui | Oui | Non | Oui | Non | Non |
| Oracle E-Business Suite | Oui | Oui | Oui | Oui | Oui | Non | Oui |
| Oracle Fusion | Oui | Oui | Oui | Oui | Oui | Non | Oui |
| Dynamics 365 Finance and Operations | Oui | Oui | Oui | Non | Non | Non | Oui |
| Business Central | Oui | Oui | Oui | Non | Oui | Non | Oui |
| Sage 100 | Non | Non | Non | Non | Non | Non | Clôturée dès la fin de la période |
| Sage Intacct | Oui | Oui | Oui | Oui | Oui | Non | Oui |
| QuickBooks Online | Oui | Oui | Oui | Non | Non | Non | La date de clôture des livres |
| Xero | Oui | Oui | Quand uniquement | Non | Non | Non | La date de verrouillage |
| Workday | Oui | Oui | Oui | Oui | Oui | Code et montant | Oui |
| NetSuite | Oui | Oui | Oui | Non | Non | Non | Oui |

SAP S/4HANA Cloud lit qui a saisi un journal et ce qu'il contrepasse à partir du service Journal Entry, Sage Intacct à partir des lots de journaux, et Oracle E-Business Suite lit l'approbateur à partir de `GL_JE_BATCHES`. Une connexion qui ne peut pas les lire laisse ces colonnes vides.

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
  - [Sage 100](/fr/guides/connections/sage-100/)
  - [Sage Intacct](/fr/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/fr/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/fr/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/fr/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/fr/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/fr/guides/connections/anaplan/#anaplan-comme-source-pour-data-foundation)
