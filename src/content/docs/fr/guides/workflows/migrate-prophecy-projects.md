---
title: Migrer des projets Prophecy
description: Convertissez l'export d'un projet Prophecy en workflows PlaidCloud depuis l'application Analyze, l'API REST ou un agent IA connecté via MCP, liez ses jeux de données et ses connexions, puis lisez le rapport de conversion.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

PlaidCloud remplace Prophecy à l'identique. Chaque gem Prophecy se convertit en étapes de workflow PlaidCloud natives qui accomplissent le travail du gem : le convertisseur crée un workflow pour chaque pipeline Spark et un pour le projet SQL, associe chaque gem à une étape de workflow, à une variable de projet ou à un objet du canevas, conserve le graphe d'origine et renvoie un rapport de conversion. Les quelques comportements qu'un workflow converti ne reproduit pas de lui-même sont décrits dans [Cas particuliers](#cas-particuliers).

La conversion lit uniquement l'export que vous lui indiquez. Elle ne contacte jamais le système depuis lequel un jeu de données Prophecy lit ou vers lequel il écrit, et elle n'exécute jamais le code du projet.

La conversion est une opération ponctuelle. Convertir à nouveau le même projet crée de nouveaux workflows et de nouvelles tables, et les modifications que vous avez apportées dans PlaidCloud ne sont jamais fusionnées avec un export ultérieur.

## Ce que PlaidCloud crée

- Chaque gem Prophecy devient l'étape de workflow correspondante, avec ses relations amont et aval préservées.
- Les paramètres Prophecy deviennent des variables de projet, et les références qui y sont faites dans les paramètres des gems sont réécrites selon la syntaxe de variable de PlaidCloud. Vous pouvez remplacer les valeurs des paramètres lors de la conversion.
- Chaque jeu de données lu par un gem devient une étape d'importation, ou lit une table ou un document existant, selon la façon dont vous le liez.
- Chaque job Prophecy ou planification de pipeline SQL devient un [événement planifié](/fr/administration/scheduled-events/) sur le workflow converti, activé lorsqu'il l'est dans Prophecy. Consultez [Planifications](#services-et-contrôle).
- Les scripts, instructions SQL, macros et autre code de projet arrivent dans des étapes qui portent ce code. Consultez [Code du projet dans les étapes](#code-du-projet-dans-les-étapes).
- Un gem personnalisé, y compris un gem Gem Builder, exécute le code que l'export contient pour lui dans une étape Python. Consultez [Code du projet dans les étapes](#code-du-projet-dans-les-étapes).
- Un gem Pivot avec une condition HAVING ou une colonne de toutes les valeurs se convertit, tout comme les types de tri et de déduplication proposés par Prophecy.
- Les expressions sont converties en supposant le comportement de Spark SQL pour la gestion des valeurs nulles, la division entière et les conversions implicites. Vérifiez les résultats là où ces comportements diffèrent sur votre moteur PlaidCloud.

## Avant de commencer

1. Exportez le projet depuis Prophecy sous forme de fichier `.zip`, ou exportez un seul pipeline, modèle ou sous-graphe sous forme de fichier `.json`.
2. Téléversez le fichier vers un [compte de documents](/fr/guides/documents/adding-accounts/) que vous pouvez lire.
3. Choisissez le projet PlaidCloud qui doit recevoir les workflows. Vous devez disposer d'un accès en écriture à ce projet.
4. Décidez d'où sont lus les fichiers des jeux de données non liés. Choisissez un compte de documents et un dossier de base.

## Convertir le projet

Lancez la conversion depuis l'application Analyze, l'API REST ou le catalogue d'outils MCP. Les trois acceptent les mêmes champs.

### Application Analyze

1. Ouvrez **Analyser** et choisissez **Tools → Importer un projet Prophecy**.
2. Choisissez le **Projet cible**, le **Projet Prophecy (.zip ou .json)** que vous avez téléversé vers un compte de documents, et l'**Emplacement des fichiers sources**, c'est-à-dire le compte de documents et le dossier de base depuis lesquels les fichiers des jeux de données non liés sont lus.
3. Sous **Noms d'objets et options**, définissez si vous le souhaitez des préfixes de workflow, d'étape et de table, choisissez le **Type de workflow** et indiquez si les composants non convertis doivent être importés comme espaces réservés en transit.
4. Sous **Source Bindings and Parameters**, liez si vous le souhaitez un jeu de données à une table existante en saisissant le nom du jeu de données et l'ID de la table, et remplacez des paramètres Prophecy par leur nom. Pour lier des connexions, utilisez l'API REST ou l'outil MCP. Consultez [Lier des connexions](#lier-des-connexions).
5. Sélectionnez **Importer**.

La fenêtre affiche la progression pendant que l'outil lit le projet, analyse les pipelines, les associe aux opérations PlaidCloud et crée les workflows, les tables et les étapes. Une fois l'opération terminée, la fenêtre affiche le rapport de conversion : nombre d'étapes par niveau de confiance, avertissements, conversions partielles, espaces réservés non convertis, composants exclus et fichiers sources à téléverser.

### Champs

L'API REST et l'outil MCP acceptent ces champs.

| Champ | Obligatoire | Rôle |
| --- | --- | --- |
| `source_account_id` | Oui | Compte de documents qui contient l'export Prophecy. |
| `source_file_path` | Oui | Chemin, dans ce compte, du `.zip` du projet ou d'un fichier `.json` de pipeline, de modèle ou de sous-graphe. |
| `project_id` | Oui | Projet dans lequel les workflows sont créés. |
| `document_account_id` | Oui | Compte de documents depuis lequel lisent les jeux de données non liés. |
| `document_account_path` | Oui | Dossier de base, dans ce compte, pour les jeux de données non liés. Une valeur vide ou `/` désigne la racine du compte, et un `/` initial est ignoré. Les chemins contenant `..` ou des segments commençant par un point, des accolades, une lettre de lecteur ou un schéma d'URL, ou des caractères de contrôle sont refusés. |
| `workflow_prefix` | Non | Préfixe ajouté aux noms de workflow. |
| `step_prefix` | Non | Préfixe ajouté aux noms d'étape. |
| `table_prefix` | Non | Préfixe ajouté aux noms de table. Par défaut, le nom du workflow lui-même. Un préfixe qui réutiliserait le nom d'une table existante est refusé avant toute création. Le préfixe utilisé est indiqué dans le rapport de conversion. |
| `workflow_type` | Non | `advanced` (par défaut) dispose le graphe sur le canevas DAG. `standard` produit une liste d'étapes en série. |
| `source_bindings` | Non | Lie des jeux de données et des opérations à des données existantes. Consultez [Lier des sources](#lier-des-sources). |
| `connection_bindings` | Non | Lie les bases de données, les stockages de fichiers, les API REST et la messagerie qu'un projet utilise à des connexions PlaidCloud et à des comptes de documents. Consultez [Lier des connexions](#lier-des-connexions). |
| `parameters` | Non | Remplace des paramètres Prophecy. Consultez [Paramètres](#paramètres). |
| `allow_unconverted_placeholders` | Non | Détermine le comportement d'un espace réservé à l'exécution. Consultez [Espaces réservés pour les gems non convertis](#espaces-réservés-pour-les-gems-non-convertis). |

### REST

Envoyez les champs sous forme de corps JSON à :

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

Vous avez besoin du rôle `analyze.workflow.write`.

### MCP

Un agent IA connecté via MCP appelle l'outil `prophecy_convert` avec les mêmes champs. Consultez [Agents IA (MCP)](/fr/integrations/ai-coding-agents/) pour connecter un agent. L'outil modifie votre projet ; examinez donc l'appel avant de l'approuver.

## Lier des sources

Un export Prophecy décrit l'origine de ses données, mais ne contient ni données ni identifiants. Utilisez `source_bindings` pour relier chaque jeu de données à des données que vous possédez déjà dans PlaidCloud. La clé est le nom du jeu de données tel que l'indique le rapport de conversion. La valeur est soit :

- Un identifiant `analyzetable_` pour une table du projet cible. Le workflow converti lit directement cette table.
- Un objet avec `account`, `path` et, éventuellement, `sheet`, pour lire un fichier depuis un compte de documents.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Une liaison que vous ne pouvez pas lire est refusée. Une clé qui ne correspond à aucun jeu de données est signalée par un avertissement. La fenêtre Analyze lie les jeux de données à des tables ; utilisez l'API REST ou l'outil MCP pour lier un jeu de données à un fichier de documents.

### Jeux de données non liés

Un jeu de données sans liaison devient une étape d'importation sans données pour l'instant, et le rapport de conversion contient un avertissement à son sujet. L'étape lit depuis :

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Téléversez le fichier à cet emplacement, puis exécutez le workflow. Tant que le fichier n'y est pas, l'étape d'importation se termine par un avertissement et crée une table vide, et le workflow se poursuit. Le rapport indique chaque chemin sous **Fichiers sources à téléverser**.

### Lier les opérations sur les tables et les fichiers

Les gems qui modifient des tables ou des fichiers, tels que Table Operations (mise à jour, suppression, drop) et File Operation (copie), n'agissent que sur les données créées par la conversion. Pour qu'un gem agisse sur des données qui existent déjà, liez-les avec une clé de la forme `operation:<pipeline>/<id>`, où `<pipeline>` est le nom du pipeline et `<id>` l'identifiant du gem. Le rapport de conversion indique la clé de chaque gem concerné.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

Une opération destructive sur une table ou un fichier ne s'exécute que si vous la liez. Sans liaison, un gem Table Operations agit sur une table écrite par un autre gem du même projet, et devient sinon un espace réservé qui indique sa clé. Un gem File Operation copie depuis son propre dossier intermédiaire. Rien en dehors des tables et dossiers propres à la conversion n'est modifié, sauf si vous le liez.

## Lier des connexions

Un projet Prophecy accède à des bases de données, des stockages de fichiers, des API REST et des serveurs de messagerie par des connexions. L'export contient les noms des connexions, mais aucun identifiant ; utilisez donc `connection_bindings` pour relier chacune d'elles à une connexion PlaidCloud ou à un compte de documents que vous possédez déjà. Le rapport de conversion répertorie chaque clé dans sa section de liaisons.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

Une clé est de l'une des formes suivantes :

| Clé | Lie | Valeur |
| --- | --- | --- |
| `connection:<name>` | La connexion Prophecy qu'un gem ou un jeu de données de base de données désigne. Une seule liaison sert tous les gems de cette connexion. Un gem qui ne désigne aucune connexion utilise `connection:<pipeline>/<gem id>`, et un jeu de données de base de données utilise `connection:<dataset name>`. | Un identifiant de connexion PlaidCloud : une connexion de base de données (BigQuery et SAP HANA compris), une connexion MongoDB ou Apache Kafka, une connexion Salesforce pour les lectures et écritures Salesforce, une connexion Tableau pour un gem Tableau, une connexion REST pour Azure Cosmos DB, Pinecone, Power BI et les écritures Smartsheet et Slack, ou une connexion reposant sur Singer pour les lectures Smartsheet, Slack et Iceberg. Un identifiant de compte de documents pour un gem File Storage ou Directory. |
| `operation:<pipeline>/<gem id>` | Un gem REST qui envoie autre chose que GET, HEAD ou OPTIONS, et chaque gem Email. | Un identifiant de connexion. Pour REST, une connexion REST qui détient l'identifiant. |

La liaison vaut consentement pour les gems qui modifient des éléments en dehors de la conversion :

- Une requête REST susceptible de modifier ce que l'API détient, et un e-mail qui atteint de vraies personnes, ne se convertissent en étapes fonctionnelles que si vous liez leur clé `operation:`. Sans liaison, le gem devient un espace réservé qui indique la clé.
- Un compte de documents lié à un gem File Storage ou Directory permet aux étapes de ce gem d'écrire, de supprimer ou de déplacer des fichiers dans ce compte.
- Une requête GET, HEAD ou OPTIONS part telle que le gem l'envoie. Sans liaison, elle n'a aucun identifiant tant que vous ne sélectionnez pas une connexion REST sur l'étape convertie.

Un jeu de données de base de données ou un gem External Table sans liaison se convertit en une étape qui indique sa clé et attend que vous sélectionniez une connexion, et le rapport contient un avertissement. Convertissez à nouveau avec la clé liée, ou sélectionnez la connexion sur l'étape. Une liaison dont l'identifiant correspond à un mauvais type de stockage pour ses gems, ou que vous ne pouvez pas utiliser, est refusée. Une clé qui ne correspond à rien est signalée par un avertissement.

## Paramètres

`parameters` remplace des paramètres Prophecy lors de la conversion :

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` désigne une instance de configuration. `values` sont du texte, des nombres ou des booléens. L'entrée d'un pipeline remplace les valeurs du projet entier pour ce pipeline. Le rapport répertorie les paramètres utilisés et ceux qui ont été renommés pour respecter les noms de variables de PlaidCloud.

## Lire le rapport de conversion

La réponse contient le rapport de conversion. Lisez-le avant d'exécuter les workflows.

| Section | Ce qu'elle vous indique |
| --- | --- |
| Résumé | Combien d'étapes se sont converties avec un niveau de confiance élevé, moyen ou faible, et combien ne se sont pas converties. |
| Avertissements | Tout ce que le convertisseur a supposé, approximé ou ignoré, y compris les jeux de données non liés et les clés de liaison qui ne correspondaient à rien. |
| Conversions partielles | Les étapes qui se convertissent mais diffèrent du gem par un mode ou une option. Chacune comporte une note sur ce qu'il faut vérifier. |
| Espaces réservés non convertis | Les gems sans équivalent PlaidCloud, avec la raison. |
| Composants exclus | Les gems qui ne portent aucun travail en propre, comme les marqueurs de limite de flux de contrôle, et l'étape qui a absorbé chacun d'eux. |
| Fichiers sources à téléverser | Le chemin de documents depuis lequel lit chaque jeu de données non lié. |
| Workflows | Le workflow créé pour chaque pipeline, dans l'ordre d'exécution. Un pipeline que le convertisseur a refusé est signalé. |

Le rapport indique aussi le préfixe de table utilisé et les paramètres appliqués. Une étape sur laquelle le convertisseur n'est pas certain est convertie selon la lecture la plus probable et s'accompagne d'une note dans le rapport. Vérifiez ces étapes par rapport à votre sortie Prophecy.

## Code du projet dans les étapes

Les projets Prophecy contiennent du code : gems Script, instructions SQL, macros, entrées dynamiques, appels de procédures stockées et gems personnalisés. Le convertisseur n'exécute pas ce code. Il le place dans une étape :

- Le SQL est traduit dans le dialecte SQL de votre tenant et placé dans une étape SQL, les entrées du gem étant disponibles sous les noms avec lesquels la requête les lit.
- Les scripts Python sont placés dans une étape Python, avec l'accès aux tables réécrit. Un script qui appelle des méthodes de DataFrame Spark conserve ces appels et les exécute dans l'étape.
- Un gem personnalisé, y compris un gem Gem Builder, exécute dans une étape Python le code PySpark que l'export de son pipeline contient pour lui.
- Une macro d'un package dbt connu devient les étapes standard qui font ce que fait la macro. Une macro de votre propre projet, ou d'un package inclus dans l'export, est lue et convertie elle aussi, y compris les blocs if et for, set, les filtres, les macros imbriquées et la répartition par adaptateur.
- Une fonction d'agrégation Python définie par l'utilisateur dans un gem Aggregate s'exécute dans une étape Python pour chaque groupe.

Chaque étape qui contient du code de projet reçoit un avertissement, tout comme le SQL traduit. Examinez le code de chacune de ces étapes avant d'exécuter le workflow. Le convertisseur retient tout ce qui ressemble à un identifiant dans les chaînes et commentaires du code ; ajoutez donc les identifiants à une connexion et non au code.

## Espaces réservés pour les gems non convertis

Un gem que le convertisseur ne peut pas reproduire est créé sous la forme d'une étape d'espace réservé qui porte le nom du gem. En voici des exemples : un gem personnalisé dont le code ne figure pas dans l'export, et un gem qui modifie des données en dehors de la conversion, comme une requête REST susceptible de modifier des données, un Email ou une opération sur une table ou un fichier, lorsque vous n'avez pas lié sa clé `operation:`. Un jeu de données de base de données ou un External Table sans connexion liée n'est pas un espace réservé : il se convertit en une étape qui attend que vous sélectionniez une connexion. Par défaut, un espace réservé échoue lorsque le workflow l'atteint, afin qu'une exécution ne puisse pas déclarer un succès pour un travail qui n'a pas eu lieu.

Définissez `allow_unconverted_placeholders` sur `true` (dans la fenêtre, **Importer les composants non convertis comme espaces réservés en transit**) pour importer chaque espace réservé comme une étape en transit. L'exécution se poursuit alors au-delà de celui-ci et la sortie de l'espace réservé est son entrée. Le rapport dénombre les espaces réservés en transit et répertorie leurs étapes. Reconstruisez la fonctionnalité avec une étape native lorsque son résultat compte.

## Exécuter les workflows convertis

1. Ouvrez les nouveaux workflows dans le projet. Le rapport les répertorie dans l'ordre d'exécution.
2. Définissez les variables de projet issues des paramètres Prophecy.
3. Téléversez les fichiers des jeux de données non liés vers les chemins indiqués dans le rapport.
4. Examinez les étapes qui contiennent du code de projet.
5. Exécutez les workflows et examinez la table de sortie de chaque étape.

Les événements planifiés créés à partir des planifications Prophecy sont activés lorsqu'ils l'étaient dans Prophecy ; ils commencent donc à exécuter les workflows convertis selon leur planification. Pour examiner d'abord les workflows, désactivez les événements dans [Événements planifiés](/fr/administration/scheduled-events/) et activez-les lorsque vous êtes prêt.

## Ce qui se convertit

Chaque gem Prophecy se convertit intégralement en étapes natives, variables de projet, événements planifiés ou objets du canevas, avec les options qu'il propose. La [matrice de conversion Prophecy](/fr/reference/prophecy-conversion-matrix/) répertorie chaque gem avec l'étape PlaidCloud en laquelle il se convertit, et les [Cas particuliers](#cas-particuliers) énumèrent les quelques comportements à vérifier ; le rapport de conversion nomme chacun d'eux là où il se présente.

### Déplacement de données

| Capacité | Mode de conversion |
| --- | --- |
| Modes d'écriture | Les modes d'écriture des cibles se convertissent en étapes de la plateforme : SCD2 avec les stratégies de contrôle et d'horodatage (la stratégie d'horodatage date chaque version à partir de la colonne que désigne `scd2.updatedAtColumn` du gem), fusion (merge), `replaceWhere` et `insertInto`. Une fusion applique les expressions SET par colonne de ses clauses de mise à jour sur correspondance et d'insertion sans correspondance ; une clause qui ne définit aucune colonne prend toutes les colonnes de la ligne entrante. Une première exécution sur une cible vide écrit toutes les lignes, comme le font dbt et Delta. La première exécution n'exige aucune table préalable, y compris pour un pipeline qui lit un jeu de données qu'il écrit aussi, sauf si l'export n'indique pas quelles colonnes ce jeu de données comporte : créez alors la table avant la première exécution. Les exécutions suivantes appliquent le filtre incrémental ou la condition de fusion. Les modes `error` et `ignore` vérifient avec la [condition d'existence de table](/fr/guides/workflows/step-conditions/#conditions-dexistence-de-table). |
| Time travel | Une source de table Delta ou de catalogue qui lit une version antérieure de sa table, par `versionAsOf` ou `timestampAsOf`, lit cette version depuis Databricks via la connexion que vous liez. |
| Diffusion en continu | Les sources et cibles de diffusion en continu s'exécutent en traitement par lots planifié. Le puits de diffusion remplace sa table au lieu d'y ajouter des lignes, de sorte qu'une nouvelle exécution ne duplique jamais de lignes. Planifiez le workflow pour récupérer les données nouvellement arrivées. |
| Bases de données | Les gems JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA et External Table lisent et écrivent via la connexion PlaidCloud que vous liez. Un jeu de données BigQuery est lu avec l'[étape Importer depuis SQL](/fr/reference/workflow-steps/import/import-sql/) et écrit avec l'étape [Export External Database Tables](/fr/reference/workflow-steps/export/export-external-tables/) sur une [connexion BigQuery](/fr/reference/connectors/google/big-query/). Une table SAP HANA écrite dans l'un des modes de fusion du gem HANA, y compris SCD2 et les modes de suppression, est préparée à côté de la cible puis fusionnée dans celle-ci sur la clé primaire de la cible ou sur les colonnes de fusion du gem ; une cible manquante est d'abord créée. |
| MongoDB et Kafka | Un jeu de données MongoDB est lu avec l'[étape Importer depuis MongoDB](/fr/reference/workflow-steps/import/import-mongodb/), filtre ou pipeline d'agrégation compris, et une lecture qui ne déclare aucune colonne les prend dans les premiers documents, comme le fait le connecteur Spark. Une écriture utilise l'[étape Exporter vers MongoDB](/fr/reference/workflow-steps/export/export-mongodb/) dans le mode d'écriture correspondant : `update` met à jour les champs du document correspondant ou en insère un, `ignore` n'écrit que tant que la collection ne contient aucun document, et `error` interrompt l'exécution lorsqu'elle en contient un. Une source Kafka lit ses topics entre les offsets de début et de fin avec l'[étape Importer depuis Kafka](/fr/reference/workflow-steps/import/import-kafka/), et une cible Kafka envoie chaque ligne avec l'[étape Exporter vers Kafka](/fr/reference/workflow-steps/export/export-kafka/). Un jeu de données Kafka qui se connecte avec `OAUTHBEARER` utilise la [connexion OAuth](/fr/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) de la connexion Kafka que vous liez, car l'export ne contient aucun identifiant. |
| Azure Cosmos DB | Une lecture envoie la requête du jeu de données, ou lit tous les documents, avec l'[étape Requête REST](/fr/reference/workflow-steps/general/rest-request/) sur une connexion REST avec authentification Cosmos DB, et suit l'en-tête de continuation de page en page. Une écriture envoie une requête par ligne selon la stratégie d'écriture du gem : écrasement, ajout, suppression ou correctif (patch). Une ligne qui porte l'ETag de son document n'est remplacée ou supprimée que si le document n'a pas changé depuis, et une ligne que le conteneur refuse pour ce motif, ou pour un document manquant ou existant, est ignorée, comme le fait le connecteur Spark. Le mode `ignore` n'écrit que tant que le conteneur ne contient aucun document. |
| Salesforce | Une lecture utilise l'[étape Salesforce : interroger un objet](/fr/reference/workflow-steps/salesforce/query-salesforce-object/), enregistrements supprimés et archivés compris lorsque le gem les demande. Une écriture insère, met à jour, fait un upsert ou supprime, avec une requête par ligne ; un upsert fait la correspondance sur le champ d'identifiant externe du gem, `Id` s'il n'en désigne aucun. |
| Smartsheet, Slack et Pinecone | Une lecture Smartsheet d'une feuille nommée avec des colonnes déclarées récupère la feuille via votre connexion REST et produit une ligne pour chaque ligne de la feuille, une colonne pour chaque colonne déclarée. Les autres lectures Smartsheet, ainsi que les lectures Slack et Iceberg, utilisent l'[étape Import Singer Source](/fr/reference/workflow-steps/import/import-singer/). Une écriture Smartsheet ajoute les lignes à la feuille nommée, et un écrasement supprime d'abord les lignes de la feuille. Une écriture Slack publie un message pour chaque ligne, et un message que Slack refuse fait échouer l'étape. Un index Pinecone est lu sous la forme de ses vecteurs et de leurs métadonnées, et une écriture fait un upsert des lignes sous forme de vecteurs. |
| Tableau et Power BI | Tableau et Tableau Write publient l'entrée sous forme d'extrait Hyper via l'[étape Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/) sur la connexion Tableau que vous liez. Power BI Write envoie les entrées vers un jeu de données Power BI en mode push via une connexion REST avec OAuth 2.0, en retrouvant l'espace de travail par son nom et en créant le jeu de données s'il est nouveau. |
| Formats de fichier | CSV, JSON, Parquet, Avro, Excel, XML, largeur fixe et ORC via l'[étape Importer ORC](/fr/reference/workflow-steps/import/import-orc/). Les options de format sont associées, ou marquées comme neutres lorsqu'elles ne modifient aucune ligne : la fenêtre d'heure de modification d'une lecture Avro, l'encodage EBCDIC d'un fichier à largeur fixe, les enregistrements d'en-tête et de fin et les enregistrements sans saut de ligne, la correspondance de feuilles et le mot de passe d'une lecture Excel, les options de guillemets d'une écriture CSV, et une écriture Excel avec une feuille par valeur. Les fichiers texte compressés sont lus et écrits avec gzip, Deflate (zlib), Zstandard, LZ4, Snappy et LZO ; un fichier compressé est lu lorsque son nom se termine par l'extension de son codec. Les fichiers chiffrés sont déchiffrés et chiffrés sur place. Consultez [Fichiers chiffrés](#fichiers-chiffrés). |
| File Operation | Copy et Move se convertissent en [Document : copier un fichier](/fr/reference/workflow-steps/document/copy-document-file/) ou en Copy Directory sur le dossier que vous liez, en ne conservant que les fichiers dont le nom correspond au `filenameRegex` du gem, et en conservant le chemin de chaque fichier sous le dossier source lorsque le gem est récursif. |
| Directory | Liste les fichiers du dossier de documents lié avec l'[étape Liste du répertoire](/fr/reference/workflow-steps/document/directory-listing/), dans les colonnes du gem. Avec l'option de nom de feuille activée, chaque classeur Excel donne une ligne par feuille et son `sheet_name` ; les autres fichiers donnent une ligne avec un `sheet_name` vide. |

### Colonnes et lignes

| Gem ou fonction | Mode de conversion |
| --- | --- |
| Surrogate Key | Les clés se poursuivent à partir d'une table qui conserve la dernière clé émise, comme le fait le fichier de clés du gem. Tous les gems qui désignent le même fichier de clés partagent cette table, de sorte que leurs clés ne se chevauchent jamais. Une exécution sans ligne la laisse telle quelle, et les clés partent de la valeur initiale tant qu'aucune exécution n'en a émis. |
| Column Parser, XML Parse, analyse JSON | Le texte XML et JSON est analysé avec les étapes [Analyse XML](/fr/reference/workflow-steps/tables/table-xml-parse/) et [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/), qui lisent chaque champ à partir du texte de l'élément, d'un attribut ou d'un élément enfant. Un XML analysé sans schéma prend le type de chaque champ dans les données, comme le fait `schema_of_xml` de Spark. |
| Règles métier | Une règle métier de projet appelée dans une expression se convertit en mêmes conditions, avec un `CASE` pour chaque colonne qu'elle définit. |
| Conversions de type (casts) | Une conversion de texte en décimal ou en entier long suit exactement Spark : les espaces et caractères de contrôle autour du nombre sont supprimés, un décimal est arrondi à la valeur supérieure à partir de la moitié, selon son échelle, et un texte qui n'est pas un nombre, ou une valeur hors limites, devient nul. |
| Dates et heures | Les formats de date et d'heure sont écrits pour le moteur de votre espace de travail, Databend compris, et `window()` place chaque horodatage dans sa fenêtre bascule, alignée comme Spark l'aligne. |
| Sorties d'itérateur | Un Table Iterator ou While Iterator dont les colonnes de sortie ne sont connues qu'à l'exécution rassemble les lignes de chaque passage par position avec l'étape [Table : union complète](/fr/reference/workflow-steps/tables/table-union-all/#correspondance-des-colonnes), chaque colonne étant élargie à un type que tous les passages respectent, comme Prophecy empile les passages. |
| Data Encoder/Decoder AES | S'exécute sur tous les moteurs. La clé, ainsi que le vecteur d'initialisation et les données supplémentaires lorsque le gem les désigne, proviennent des variables de workflow `aes_key`, `aes_iv` et `aes_aad`, que vous définissez. |
| Hachage Data Masking | Calcule les mêmes valeurs que le `hash()` de Spark. |
| Buffer, Simplify, Heat Map | Buffer trace un coin arrondi avec le même nombre de segments que Prophecy, Simplify supprime les mêmes sommets, et Heat Map additionne la chaleur dans des hexagones H3 à la résolution du gem, une chaleur décimale restant décimale. |

### Services et contrôle

| Gem | Mode de conversion |
| --- | --- |
| Pipeline | Exécute le pipeline qu'il désigne avec un [Workflow Loop](/fr/reference/workflow-steps/workflow-control/workflow-loop/), une fois pour chaque ligne d'entrée (une fois lorsqu'il n'y a pas d'entrée, jamais lorsqu'il n'y a aucune ligne), chaque paramètre étant défini à partir d'une constante, d'une colonne de la ligne ou d'une expression portant sur celle-ci. Chaque exécution a lieu même si une précédente échoue, et la sortie du gem comporte une ligne pour chaque exécution avec son statut, son message et ses heures, comme Prophecy les enregistre. |
| Planifications | Un job Prophecy ou une planification de pipeline SQL devient un [événement planifié](/fr/administration/scheduled-events/) nommé `Prophecy <name>` sur le workflow converti, activé sauf s'il est désactivé dans Prophecy. Un job Spark se convertit ainsi lorsqu'il exécute un pipeline converti sans remplacement de configuration ni condition d'exécution. |
| Script | Un script Python est placé dans une étape Python. Une valeur que le script définit sur `Config` devient une variable de workflow que les étapes suivantes lisent, réinitialisée à la valeur du pipeline au début de chaque exécution, comme l'est le `Config` de Prophecy. |
| REST API, REST API Enrich | Étapes [Requête REST](/fr/reference/workflow-steps/general/rest-request/), une requête pour chaque ligne d'entrée, qui conservent une réponse d'erreur comme le fait Prophecy. Enrich lit aussi le statut, la raison et l'URL finale. Une requête qui attend un résultat asynchrone interroge jusqu'à ce que la réponse indique qu'il est prêt. |
| Stored Procedure | Un gem qui transmet des arguments appelle sa procédure avec l'étape [Exécution à distance : SQL](/fr/reference/workflow-steps/agent/agent-remote-execution-of-sql/#exécuter-une-instruction-une-fois-par-ligne) une fois pour chaque ligne d'entrée, chaque argument étant lié depuis sa colonne comme paramètre. Un gem sans argument l'appelle une fois via un agent. Choisissez la connexion ou l'agent sur l'étape convertie. |
| Email, Email Data | Étape [Notify Via Email](/fr/reference/workflow-steps/notifications/notify-via-email/) avec Cc, Bcc, Reply-To et un message pour chaque ligne lorsqu'un champ est lu depuis une colonne. |
| OpenAI, Bedrock, SageMaker Endpoint | Étape [Text: NLP (AI)](/fr/reference/workflow-steps/text-documents/nlp-ai/) sur la connexion LLM de votre espace de travail. Les embeddings OpenAI et Bedrock utilisent la tâche Embed, qui nécessite une connexion compatible OpenAI ou Azure OpenAI ; une connexion Anthropic est refusée. |
| Pinecone Lookup | Une requête REST pour chaque ligne. |
| Data Quality Check, Deequ, Soda | Les contrôles s'exécutent dans l'entrepôt de données et écrivent la table de résultats. Un Data Quality Check n'interrompt l'exécution que si le gem définit `minFailedChecks` ou une action postérieure `fail_pipeline` ; sinon, la table de résultats répertorie les échecs. Deequ et Soda n'interrompent jamais l'exécution. Un contrôle de longueur minimale ou maximale sur une colonne numérique mesure le nombre en tant que texte. Les contrôles Soda se convertissent à partir du YAML du projet, y compris les valeurs manquantes, invalides et valides, les statistiques, les longueurs, les percentiles, les doublons entre colonnes, la fraîcheur, les lignes en échec et vos propres requêtes de métrique. |
| ToDo | Déclenche une erreur qui nomme l'outil d'origine et le message lorsque l'exécution l'atteint. |

### Fichiers chiffrés

Un gem File Storage qui lit un fichier chiffré se convertit en [Document : déchiffrer un fichier](/fr/reference/workflow-steps/document/encrypt-decrypt-file/), qui déchiffre le fichier dans un dossier dédié avant que l'importation ne le lise ; la copie déchiffrée est ensuite supprimée. Un gem qui écrit un fichier chiffré exporte dans ce dossier, puis chiffre le fichier à sa place avec Document : chiffrer un fichier. Les fichiers AES et Blowfish et les classeurs Excel protégés par mot de passe sont pris en charge.

L'export ne contient jamais de clé ; les étapes converties la lisent donc depuis une variable de workflow : `aes_key` pour une clé AES ou Blowfish, et `xlsx_password` pour un mot de passe de classeur. Définissez la variable avant d'exécuter le workflow, et donnez-lui une clé destinée uniquement à ces fichiers. Les champs de clé et de mot de passe n'acceptent qu'une référence de variable, de sorte qu'une clé n'est jamais saisie dans une étape.

## Cas particuliers

Ce sont les comportements qu'un workflow converti ne reproduit pas de lui-même. Le rapport de conversion nomme chacun d'eux là où il se présente.

- **Code ou données absents de l'export** : un gem Gem Builder ou un autre gem personnalisé dont le code ne figure pas dans l'export, et un appel à une macro d'un package dbt que l'export omet, deviennent une étape qui indique ce qui manque ; exportez le projet avec le code de ses pipelines et ses packages dbt, ou reconstruisez la logique dans une étape Python ou SQL. Les gems Ab Initio Error Detection et MTime transmettent leur entrée telle quelle, car la règle qu'ils appliquent ne figure pas dans l'export. Les contrôles Soda lus depuis un fichier extérieur au projet, ainsi que ceux qui comparent avec des analyses antérieures ou avec un autre jeu de données, ou qui testent un format que Soda nomme, n'ont aucune ligne dans la table de résultats ; calculez-les dans une étape ultérieure.
- **Résultats connus seulement à l'exécution du pipeline** : un gem REST API qui aplatit sa réponse place toute la réponse dans une seule colonne lorsque rien ne déclare les noms de champs, ce que seule une exécution révèle ; extrayez les champs dont vous avez besoin dans une étape ultérieure. Une macro dbt qui interroge l'entrepôt de données pendant la compilation de dbt devient une étape qui la nomme ; remplacez la requête par les valeurs qu'elle renvoie. Un gem Spark StoredProcedure s'exécute, mais ses valeurs OUT ne sont pas renvoyées ; la sortie est constituée des colonnes transmises. `input_file_name()` renvoie une chaîne vide sur une source de table ou Delta, qui n'a aucun fichier à nommer, et `hash()` / `xxhash64()` dans un agrégat, une fenêtre ou un gem à plusieurs entrées sont calculés par l'entrepôt de données et peuvent donc différer de ceux de Spark.
- **Valeurs écrites dans une étape lors de la conversion du projet** : une valeur de paramètre contenant un guillemet, une barre oblique inverse ou une accolade, une valeur de pipeline qu'une étape SQL lit, et la base de données qu'une opération de table Delta désigne par configuration sont écrites dans l'étape comme valeurs fixes ; modifier la variable de workflow ne les change donc pas. Modifiez l'étape lorsque la configuration change.
- **Code Scala** : un script Scala, une expression Scala ou une fonction définie par l'utilisateur ou fonction d'agrégation Scala devient une étape qui la nomme ; réécrivez-la en SQL ou en Python.
- **Connexion Kafka Kerberos** : une source ou une cible Kafka qui se connecte avec Kerberos (GSSAPI) se convertit sans le nom de service Kerberos ni le mécanisme de connexion ; définissez-les sur la connexion PlaidCloud.
- **Diffusion en continu** : les sources, cibles et pipelines de diffusion en continu s'exécutent comme des workflows par lots sur les données présentes au moment de l'exécution ; planifiez le workflow pour qu'il s'exécute aussi souvent que nécessaire.
- **Composants de job** : un job Spark convertit son unique pipeline et sa planification ; ses autres composants, ses conditions d'exécution et ses remplacements de configuration ne sont pas convertis.
- **Appels peu courants** : une fonction d'agrégation définie par l'utilisateur appelée depuis un rollup ou une fenêtre, et une macro dbt qui utilise Jinja au-delà de if, for, set et des filtres courants, deviennent une étape qui nomme le gem ; appelez la fonction depuis un gem Aggregate, ou intégrez la macro directement.

## Guides associés

- [Migrer des analyses Savant](/fr/guides/workflows/migrate-savant-analyses/)
- [Migrer des workflows Alteryx](/fr/guides/workflows/migrate-alteryx-workflows/)
- [Ajouter des comptes de documents](/fr/guides/documents/adding-accounts/)
- [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/)
- [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/)
