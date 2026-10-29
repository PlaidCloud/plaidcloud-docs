---
title: Connecteur Oracle Fusion
description: Configurez une connexion à Oracle Fusion Cloud dans PlaidCloud avec des identifiants OAuth2 pour importer des soldes du grand livre et des lots d'écritures via OData/BIP, et comptabiliser des écritures via FBDI.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## Documentation de l'API

Les références de l'[API REST (OData)](https://docs.oracle.com/en/cloud/saas/financials/) d'Oracle Fusion Cloud, ainsi que de [BI Publisher (BIP) et de l'import de données par fichier (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/), documentent les points de terminaison et la voie d'extraction/de chargement en masse qu'utilise ce connecteur.

## Fonctionnement de l'authentification

La connexion s'authentifie avec les informations d'identification client OAuth2 (ou les identifiants d'API en authentification de base que la sécurité de votre Fusion Cloud délivre aux utilisateurs d'intégration) auprès d'un utilisateur d'API dédié. Le rôle de cet utilisateur d'API détermine à la fois les entités du grand livre qu'il peut lire et les fonctions FBDI/GL Interface par lesquelles il peut comptabiliser.

## Configuration

| Champ | Type | Description |
|---|---|---|
| Nom | Texte | Nom d'affichage de cette connexion. |
| URL de l'instance | Texte | L'URL de votre instance Fusion Cloud, par ex. `https://yourorg.fa.us2.oraclecloud.com`. |
| ID client | Texte | L'ID client OAuth2 de l'utilisateur d'API (ou son nom d'utilisateur, en authentification de base). |
| Secret client | Texte | Le secret client OAuth2 de l'utilisateur d'API (ou son mot de passe, en authentification de base). Stocké chiffré. |

## Entités disponibles à l'import

Deux étapes d'import couvrent des volumes d'extraction différents, toutes deux sur `gl_balances` et `journal_batches` :

- **Import Fusion Entity** — un appel direct OData/BIP, pour une extraction courante et limitée.
- **Import Fusion Bulk Extract** — un travail d'export FBDI/BIP asynchrone, pour une extraction volumineuse.

Les deux prennent en charge les filtres de plage (`ge`/`le`) sur les champs de date, de période comptable et de solde/montant numérique, ainsi que les filtres d'égalité sur les champs discrets comme le grand livre ou la devise. Consultez [Import Fusion Entity](/fr/reference/workflow-steps/oracle-fusion/import-fusion-entity/) et [Import Fusion Bulk Extract](/fr/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) pour la référence complète des champs.

## Comptabilisation des écritures de journal

L'étape **Oracle Fusion: Post Journal Entry** comptabilise des lots de journaux du grand livre via le pipeline d'écriture ERP partagé de PlaidCloud : elle écrit le lot dans la table de transit GL_INTERFACE d'Oracle sous forme de fichier FBDI, soumet le travail ESS Journal Import Launcher et l'interroge jusqu'à un état terminal, puis confirme avant de signaler un lot comme comptabilisé. Une correction comptabilise une nouvelle écriture d'extourne, avec débit et crédit inversés, au lieu de modifier l'originale. Consultez [Oracle Fusion: Post Journal Entry](/fr/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) pour la référence des champs, et [Connect to Oracle Fusion](/fr/guides/connections/oracle-fusion/) pour la procédure complète de comptabilisation.

## Limitations connues

| Limitation | Ce que cela signifie |
|---|---|
| Latence des travaux ESS | Le Journal Import Launcher s'exécute comme un travail planifié, et non comme un appel synchrone : une exécution de comptabilisation prend nettement plus de temps qu'une écriture directe par API. |
| Latence de l'extraction en masse | `import_fusion_bulk_extract` attend un travail d'export FBDI/BIP — réservez-le aux extractions trop volumineuses pour la voie directe de `import_fusion_entity`. |
## Voir aussi

- [Connect to Oracle Fusion (guide)](/fr/guides/connections/oracle-fusion/) — pas à pas : créer la connexion, la tester, importer une entité et comptabiliser une écriture de journal.
- [Import Fusion Entity](/fr/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/fr/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/fr/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [Review ERP Post History](/fr/guides/connections/erp-post-history/)
