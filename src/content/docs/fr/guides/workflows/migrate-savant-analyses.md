---
title: Migrer des analyses Savant
description: Convertissez l'export d'une analyse Savant Labs en workflow avancé PlaidCloud depuis l'application Analyze, l'API REST ou un agent IA connecté via MCP, liez ses sources, puis lisez le rapport de conversion.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

PlaidCloud remplace Savant à l'identique. Chaque agent, expression et paramètre Savant se convertit vers PlaidCloud et s'exécute. Le convertisseur transforme l'export d'une analyse Savant Labs en workflow avancé exécutable : il associe chaque agent Savant à une étape de workflow, à une variable de projet ou à un objet du canevas, conserve le graphe d'origine et renvoie un rapport de conversion qui nomme tout ce qu'il n'a pas pu convertir.

La conversion lit le fichier d'export que vous lui indiquez ainsi que les en-têtes des fichiers que vous liez à ses sources. Elle ne contacte jamais le système auquel une source ou une destination Savant se connecte.

## Ce que PlaidCloud crée

- Chaque agent Savant devient l'étape de workflow correspondante, avec ses relations amont et aval préservées. La [matrice de conversion Savant](/fr/reference/savant-conversion-matrix/) répertorie chaque agent et son niveau de correspondance.
- Les paramètres d'analyse Savant deviennent des variables de projet, et les références qui y sont faites dans les paramètres des agents sont réécrites selon la syntaxe de variable de PlaidCloud.
- Les notes et les groupes arrivent sur le canevas sous forme de notes et de groupes.
- Chaque source devient une étape d'importation, ou lit une table existante, selon la façon dont vous la liez.
- Chaque type d'agent Savant se convertit intégralement : chaque option a une correspondance. Une configuration sur laquelle Savant lui-même échoue ou qu'il ne documente pas arrive sous forme d'étape d'espace réservé nommée. Consultez [Espaces réservés pour les configurations non converties](#espaces-réservés-pour-les-configurations-non-converties).

## Avant de commencer

1. Exportez l'analyse depuis Savant avec **Exporter en JSON**.
2. Téléversez le fichier `.json` vers un [compte de documents](/fr/guides/documents/adding-accounts/) que vous pouvez lire.
3. Choisissez le projet PlaidCloud qui doit recevoir le workflow. Vous devez disposer d'un accès en écriture à ce projet.
4. Choisissez un compte de documents et un dossier de base depuis lesquels les fichiers sources de l'analyse seront lus.

## Convertir une analyse

Lancez la conversion depuis l'application Analyze, l'API REST ou le catalogue d'outils MCP. Les trois acceptent les mêmes champs.

### Application Analyze

1. Ouvrez **Analyser** et choisissez **Tools → Importer une analyse Savant**.
2. Choisissez le **Projet cible** et le **Fichier d'export Savant (.json)** que vous avez téléversé vers un compte de documents.
3. Sélectionnez **Charger les sources**. La fenêtre répertorie chaque nœud source de l'export.
4. Pour relier une source à des données que vous possédez déjà, sélectionnez-la et choisissez **Lier…**. Choisissez **Table du projet** pour lire une table du projet cible, ou **Document** pour lire un fichier depuis un compte de documents (avec un nom de feuille facultatif pour Excel). Choisissez **Dissocier** pour supprimer une liaison.
5. Sous **Répertoire des sources non liées**, choisissez le compte de documents et le dossier de base depuis lesquels les fichiers des sources non liées sont lus.
6. Sous **Options de conversion**, choisissez le **Type de workflow** et indiquez s'il faut **Autoriser les espaces réservés non convertis**. Sous **Préfixes d'objets**, définissez si vous le souhaitez des préfixes de workflow, d'étape et de table.
7. Sélectionnez **Convertir**.

Une fois la conversion terminée, la fenêtre affiche le rapport de conversion : le nom du workflow et le préfixe de table, les avertissements, un tableau des chemins de documents où téléverser les fichiers des sources non liées, et les étapes à examiner. Si la liste des sources ne peut pas être chargée, ajoutez une ligne pour chaque source avec son identifiant de nœud et l'identifiant `analyzetable_` de la table à lier.

### Champs

L'API REST et l'outil MCP acceptent ces champs.

| Champ | Obligatoire | Rôle |
| --- | --- | --- |
| `source_account_id` | Oui | Compte de documents qui contient l'export Savant. |
| `source_file_path` | Oui | Chemin de l'export dans ce compte. |
| `project_id` | Oui | Projet dans lequel le workflow est créé. |
| `document_account_id` | Oui | Compte de documents depuis lequel lisent les sources non liées. |
| `document_account_path` | Oui | Dossier de base, dans ce compte, pour les sources non liées. Une valeur vide ou `/` désigne la racine du compte, et un `/` initial est ignoré. Les chemins contenant `..` ou des segments commençant par un point, des accolades, une lettre de lecteur ou un schéma d'URL, ou des caractères de contrôle sont refusés. |
| `workflow_prefix` | Non | Préfixe ajouté aux noms de workflow. |
| `step_prefix` | Non | Préfixe ajouté aux noms d'étape. |
| `table_prefix` | Non | Préfixe ajouté aux noms de table. Par défaut, le nom du workflow lui-même. Un préfixe qui réutiliserait le nom d'une table existante est refusé avant toute création. Le préfixe utilisé est indiqué dans le rapport de conversion. |
| `workflow_type` | Non | `advanced` (par défaut) dispose le graphe sur le canevas DAG. `standard` produit une liste d'étapes en série. |
| `source_bindings` | Non | Lie des sources à des données existantes. Consultez [Lier des sources](#lier-des-sources). |
| `destination_bindings` | Non | Oriente les destinations vers un compte de documents, une table de connexion, une feuille Google Sheets, une source de données Tableau, un canal Slack ou des destinataires d'e-mail. REST et MCP uniquement. Consultez [Destinations](#destinations). |
| `api_bindings` | Non | Indique où va l'URL relative d'un agent API : une URL de base ou une connexion REST. REST et MCP uniquement. Consultez [Lier des requêtes API](#lier-des-requêtes-api). |
| `allow_unconverted_placeholders` | Non | Détermine le comportement d'un espace réservé à l'exécution. Consultez [Espaces réservés pour les configurations non converties](#espaces-réservés-pour-les-configurations-non-converties). |

### REST

Envoyez les champs sous forme de corps JSON à :

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

Pour répertorier les nœuds sources d'un export avant de construire `source_bindings`, envoyez `source_account_id` et `source_file_path` à :

```text
POST /rest/v1/analyze/savant/sources
```

Chaque entrée de la réponse contient le `node_id`, le `name` et le `connector` de la source.

### MCP

Un agent IA connecté via MCP appelle l'outil `savant_convert` avec les mêmes champs. Consultez [Agents IA (MCP)](/fr/integrations/ai-coding-agents/) pour connecter un agent. L'outil modifie votre projet ; examinez donc l'appel avant de l'approuver.

## Liaisons au moment de la conversion

Un export Savant ne contient ni données, ni identifiants, ni connexions ; trois paramètres de conversion le relient donc aux vôtres. Chacun est une table de correspondance entre un identifiant ou un nom de nœud Savant et une cible, et une liaison que vous ne pouvez pas utiliser fait refuser l'ensemble de la conversion avant toute création.

| Paramètre | Lie | Section |
| --- | --- | --- |
| `source_bindings` | Des agents source à des tables ou des fichiers | [Lier des sources](#lier-des-sources) |
| `destination_bindings` | Des agents de destination à un fichier, une table, une feuille, une source de données Tableau, un canal Slack ou un e-mail | [Destinations](#destinations) |
| `api_bindings` | Des agents API ayant une URL relative à une URL de base ou à une connexion REST | [Lier des requêtes API](#lier-des-requêtes-api) |

## Lier des sources

Un export Savant décrit l'origine de ses données, mais ne contient ni données ni identifiants. Utilisez `source_bindings` pour relier chaque source à des données que vous possédez déjà dans PlaidCloud. La clé est l'identifiant de nœud, l'identifiant de jeu de données ou le nom de la source. La valeur est soit :

- Un identifiant `analyzetable_` pour une table du projet cible. Le workflow converti lit directement cette table.
- Un objet avec `account`, `path` et, éventuellement, `sheet`, pour lire un fichier depuis un compte de documents.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Une liaison que vous ne pouvez pas lire est refusée. Une clé qui ne correspond à aucune source est signalée par un avertissement.

Le chemin d'un fichier source dans l'export peut commencer par `/` ou traverser des dossiers préfixés d'un point tels que `.archive`, et il se convertit. Une source qui lit du XML convertit le texte XML, et une source de document XML porte aussi les colonnes de contexte de fichier de Savant.

### Sources non liées

Une source sans liaison devient une étape d'importation sans données pour l'instant, et le rapport de conversion contient un avertissement à son sujet. L'étape lit depuis :

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Téléversez le fichier à cet emplacement, puis exécutez le workflow. Tant que le fichier n'y est pas, l'étape d'importation se termine par un avertissement et crée une table vide, et le workflow se poursuit.

## Conversion des agents

La plupart des agents se convertissent en l'étape que vous construiriez à la main ; la [matrice de conversion Savant](/fr/reference/savant-conversion-matrix/) répertorie chaque agent. Les agents suivants demandent une attention particulière.

| Agent Savant | En quoi il se convertit | Points d'attention |
| --- | --- | --- |
| Infer Agent (`gen_ai`, et `service` hérité avec un service LLM) | Une étape [AI/NLP](/fr/reference/workflow-steps/text-documents/nlp-ai/) avec la tâche **Invite**. L'invite s'exécute une fois par ligne sur les champs d'entrée, et la réponse arrive dans une colonne **AI Answer** à côté de chaque colonne d'entrée. Une limite de lignes devient **Nb max. de lignes**, et une source vide déclenche un avertissement et écrit une table vide. **Max New Rows** ne répond qu'aux lignes nouvelles et conserve les réponses des exécutions précédentes. | Un LLM répond ; la sortie n'est donc jamais identique à l'octet près à celle de Savant et peut varier d'une exécution à l'autre. Chaque appel a un coût. Consultez [Fournisseurs d'IA](#fournisseurs-dia). Un lot qui échoue conserve ses lignes avec une réponse vide et déclenche un avertissement. |
| Vision Agent (`vision`) | Une étape [Document Read Blob](/fr/reference/workflow-steps/text-documents/document-blob-extract/), puis [Image OCR](/fr/reference/workflow-steps/text-documents/image-ocr/), puis la tâche **Invite** d'AI/NLP. Chaque document est envoyé au fournisseur sous forme d'image ou de PDF lorsque celui-ci accepte ce type et cette taille. Sinon, l'étape envoie la couche de texte du PDF, ou le texte issu de l'OCR. | Mêmes réserves sur les LLM que pour l'Infer Agent. Des documents entiers quittent PlaidCloud pour le fournisseur, et la conversion déclenche un avertissement. Les fichiers TIFF et BMP sont envoyés sous forme de texte OCR, et il n'existe aucun paramètre de taille maximale de document. Un document introuvable est ignoré et l'étape signale son chemin par un avertissement. |
| API Agent (`apiService`, et `service` hérité avec un service API) | Une étape [Requête REST](/fr/reference/workflow-steps/general/rest-request/) qui envoie une requête par ligne d'entrée, puis une jointure de retour qui conserve toutes les lignes d'entrée. Le corps brut de la réponse arrive dans une colonne de texte, avec une colonne de statut à côté. Un quota par période devient un **Req/s max.** fractionnaire. Une URL relative est jointe à l'URL de base ou à la connexion REST que vous liez avec `api_bindings`. Un hôte, un port ou un chemin provenant d'un champ de la ligne est renseigné ligne par ligne. La pagination par URL suivante, en-tête Link, décalage (offset) et numéro de page est suivie, et une valeur de pagination (début, taille de page ou nom de paramètre) peut provenir d'un champ d'entrée ou d'un paramètre. | Une méthode autre que GET s'exécute sur le système réel une fois par ligne d'entrée à chaque exécution du workflow ; confirmez donc la cible avant la première exécution. Les requêtes non-GET ne sont pas relancées automatiquement. Une requête en échec reste sous forme de ligne avec son statut. Une requête qui transporte un identifiant ne peut pas tirer son hôte d'un champ de la ligne. Les identifiants sont traités comme décrit dans [Étapes API avec identifiants](#étapes-api-avec-identifiants). |
| Recursion Agent (`hierarchy`) | Une étape [Hierarchy Closure](/fr/reference/workflow-steps/tables/table-hierarchy-closure/) qui remonte la chaîne des parents de chaque ligne à n'importe quelle profondeur, puis agrège chaque nœud sur les identifiants de son chemin jusqu'à la racine, lui-même compris. Elle écrit Depth et Path. Une ligne dont le parent est vide, ou qui se désigne elle-même comme parent, est une racine. | Une boucle dans les identifiants parents s'arrête au nœud répété et conserve tous les ancêtres qui le précèdent. Les lignes ayant plusieurs parents conservent chacune leurs propres valeurs. |
| Search and Replace (`search_replace`) | Une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) qui applique chaque règle dans l'ordre aux colonnes de texte choisies, avec ou sans distinction de casse, mot entier ou non. Chaque règle s'exécute dans son mode : remplacer le texte trouvé, remplacer toute la cellule si elle contient le texte, remplacer toute la cellule si elle correspond exactement, ou ajouter à la cellule. | Les règles sont du texte littéral, pas des motifs. |
| Split (`split`) | Une étape [Split Text](/fr/reference/workflow-steps/tables/table-split-text/). Elle fractionne en colonnes ou en lignes sur un séparateur littéral de longueur quelconque, et détermine le nombre de colonnes à partir des données à l'exécution du workflow. | Aucun. |
| Time Series (`rollup`) | Une étape Table Extract qui regroupe selon une expression de période, avec une étape [Period Spine](/fr/reference/workflow-steps/tables/table-period-spine/), une anti-jointure et une union qui complètent par des zéros les périodes sans enregistrement. | Les enregistrements dont la date est NULL sont exclus. La trame de périodes s'arrête à 100 000 périodes. |
| Format (`format`) | Une étape Table Extract avec les renommages, changements de type, masquages et remplissages, ou une étape [Promote Header](/fr/reference/workflow-steps/tables/table-promote-header/) pour remplacer les noms par une ligne. | Un remplissage sur une colonne qui n'est pas de type texte convertit la valeur par défaut vers le type de la colonne. Promouvoir un en-tête sur une source qui ne déclare aucune colonne lit toutes les colonnes, pour les fichiers CSV, Excel, XLS, JSON, Parquet et Avro. Consultez [Fichiers sans colonnes déclarées](#fichiers-sans-colonnes-déclarées). |
| Spatial Match Agent (`spatial_match`) | Une étape [Spatial Match (executor)](/fr/reference/workflow-steps/spatial/spatial-match-executor/) pour intersects, within, contains, touches, crosses, overlaps, equals et disjoint, avec plusieurs règles combinées ; Jointure croisée pour une correspondance croisée ; [Rechercher le plus proche](/fr/reference/workflow-steps/spatial/spatial-find-nearest/) pour une correspondance au plus proche. | Une correspondance au plus proche classe et filtre selon la distance orthodromique, comme le fait Savant. Une règle de proximité combinée à d'autres règles trouve d'abord les enregistrements les plus proches, puis applique les autres règles : avec AND, le résultat conserve les enregistrements qui satisfont toutes les règles, et avec OR, il réunit les enregistrements les plus proches et ceux que les autres règles retiennent. Une règle de proximité sans nombre ni distance maximale conserve l'unique enregistrement le plus proche. Une correspondance par distance maximale se convertit aussi, en kilomètres lorsque la règle ne donne pas d'unité, et mesure la distance géodésique entre n'importe quelles géométries, pas seulement des points. Une géométrie qui ne peut pas être analysée donne NULL ou aucune correspondance, avec un avertissement. |
| Spatial Summarize Agent (`spatial_summarize`) | [Combinaison spatiale](/fr/reference/workflow-steps/spatial/spatial-combine/) pour l'union, l'intersection et l'emprise (bounding box), ainsi que [Spatial Centroid](/fr/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/fr/reference/workflow-steps/spatial/spatial-point-to-line/) et [Spatial Line to Polygon](/fr/reference/workflow-steps/spatial/spatial-line-to-polygon/) pour le centre géométrique et la construction de lignes ou de polygones. | Un polygone construit à partir de moins de 3 points est un polygone vide. |
| Destination Agent (`destination`) | Une étape d'export vers la cible que vous liez, ou une table ou un fichier du projet si vous n'en liez pas. Consultez [Destinations](#destinations). | Consultez [Cas particuliers](#cas-particuliers). |

`GEO_POINT`, `GEO_TYPE` et `GEO_SPATIAL_DISTANCE` se convertissent en expressions. Une modification dont toute l'expression est une autre fonction `GEO_*`, telle que `GEO_AREA` ou `GEO_UNION`, se convertit en l'étape spatiale correspondante, y compris [Spatial Info](/fr/reference/workflow-steps/spatial/spatial-info/). La géométrie circule sous forme de texte WKT. `GEO_AREA`, `GEO_PERIMETER` et `GEO_SPATIAL_DISTANCE` en miles utilisent le mile terrestre (statute mile).

Une source qui lit des fichiers binaires, comme les documents qu'un agent Vision lit, se convertit en une extraction de document du document lié, ou du fichier attendu au chemin des sources non liées.

## Fournisseurs d'IA

Un agent Infer ou Vision se convertit en une étape AI/NLP qui utilise une connexion LLM. Le convertisseur prend en charge Anthropic, OpenAI, Gemini, Azure OpenAI, Grok et GitHub Models.

- Le convertisseur choisit la connexion correspondant au fournisseur et au modèle que désigne l'agent, parmi les connexions LLM que l'utilisateur qui importe peut voir. Il n'en nomme jamais une que l'utilisateur ne peut pas voir. Via un assistant IA (MCP), il s'agit des connexions que l'utilisateur de l'assistant peut voir.
- Lorsque le fournisseur n'a aucune connexion visible, ou que le fournisseur de Savant n'a aucun équivalent dans PlaidCloud (une API de modèle hébergée dans le cloud ou un fournisseur avec clé personnelle de l'espace de travail Savant), l'étape utilise la connexion par défaut de l'espace de travail si l'utilisateur peut la voir. Sinon, elle laisse la connexion vide, et l'étape utilise la connexion par défaut de l'espace de travail à son exécution. Le rapport de conversion avertit dans les deux cas ; choisissez donc une connexion sur l'étape si une autre doit répondre.

## Destinations

Une destination Savant écrit la table qu'elle reçoit vers la cible que vous liez. Liez les destinations avec `destination_bindings` dans le corps REST ou l'appel MCP. La clé est l'identifiant ou le nom de nœud de la destination. La fenêtre Analyze ne lie pas les destinations ; une destination convertie à partir de là écrit donc le résultat non lié décrit sous [Destinations non liées](#destinations-non-liées).

| Cible | Liaison | Résultat |
| --- | --- | --- |
| Compte de documents | `{account, path[, file_name]}` | Un fichier CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF ou Tableau Hyper, selon le type de destination. Vous avez besoin de l'autorisation d'écriture du stockage de documents sur le compte. |
| Table sur une connexion | `{connection, table[, schema, replace]}` | Une étape [Export: External Database Tables](/fr/reference/workflow-steps/export/export-external-tables/). Vous avez besoin de l'autorisation d'écriture sur la connexion. Remplacer la table exige `replace: true`. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}`, ou `{connection, spreadsheet_id[, sheet_name, replace]}` | Une étape [Export to Google Spreadsheet](/fr/reference/workflow-steps/export/export-to-google-spreadsheet/) sur une connexion Google Sheets. L'onglet est par défaut celui que désigne la destination, sinon `Sheet1`. Une destination qui remplace les lignes de la feuille vide l'onglet ; elle exige donc `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | Un extrait Tableau Hyper écrit dans le dossier du compte, puis une étape [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/) sur une [connexion Tableau](/fr/reference/connectors/collaboration/tableau/). Remplacer la source de données, ou modifier ses lignes sur des clés de correspondance, exige `replace: true`. |
| Slack | `{connection[, channel]}` | Le CSV est écrit dans un compte de documents, puis une étape [Notify via Slack](/fr/reference/workflow-steps/notifications/notify-via-slack/) le téléverse dans le canal. La connexion nécessite un jeton de bot, et le canal doit être un identifiant de canal, pris dans la liaison ou, à défaut, dans l'export. |
| E-mail | `{email_to: [...]}`, et `email_export_recipients: true` pour utiliser aussi les destinataires que l'export répertorie | Le CSV est envoyé par e-mail en pièce jointe. Vous avez besoin de l'autorisation d'écriture d'e-mail. |

Une connexion Sheets, Tableau ou Slack est vérifiée comme une connexion de table : vous devez pouvoir la voir et détenir l'autorisation d'écriture sur la connexion, faute de quoi la conversion est refusée.

### Modes d'écriture

- Une destination de fichier ou de table qui ajoute des lignes relit le fichier précédent et le réécrit avec les nouvelles lignes. Elle n'écrase jamais.
- Une destination upsert, update ou groupReplace fusionne sur les clés de correspondance de la destination. Un fichier ou une table est relu puis réécrit, et une source de données Tableau voit ses lignes correspondantes modifiées sur place.
- L'ajout et la fusion fonctionnent aussi sur des fichiers existants fractionnés par valeur, sans en-tête (les lignes correspondent par position), des fichiers Excel ancrés à une cellule en haut à gauche, et des fichiers dans un jeu de caractères autre qu'UTF-8. Un fractionnement relit le fichier dans lequel chaque valeur est écrite et fusionne à l'intérieur de celui-ci, en laissant les autres fichiers tels quels.
- Une destination Tableau associe les modes de Savant aux six modes de [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/#modes) : append et insert ajoutent des lignes, replace écrase, et upsert, update et groupReplace font la correspondance sur des clés. Un mode qui modifie des données existantes ne publie que lorsque la liaison indique `replace: true` ; sinon, la destination publie une nouvelle source de données et le rapport le signale.
- Une destination avec un encodage de sortie écrit le fichier dans ce jeu de caractères Java. Un caractère que le jeu ne contient pas est écrit sous la forme `?`, comme le fait Savant. Les alias Java, CESU-8 et les formes avec marque d'ordre des octets (BOM) sont acceptés. Quelques jeux de caractères rares (par exemple `x-ISCII91` ou `JIS_X0212`) ne peuvent pas être écrits ; le fichier est alors écrit en UTF-8 et le rapport avertit. Un fractionnement dans un jeu de caractères autre qu'UTF-8 convertit le dossier.
- Les noms de fichiers d'export doivent rester à l'intérieur du dossier lié.

### Ce que les appelants IA peuvent lier

Une conversion via un assistant IA (MCP) lie les mêmes formes, avec certains éléments retenus, chacun accompagné d'un avertissement qui nomme l'élément :

| Retenu | Ce qui se passe à la place |
| --- | --- |
| `replace` sur une table, une feuille ou une source de données Tableau | Une destination qui ajoute des lignes continue d'ajouter à sa table ou sa feuille liée. Une destination qui remplace écrit un CSV. Une destination Tableau publie une nouvelle source de données. |
| Destinataires d'e-mail | Un CSV est écrit à la place de l'e-mail. |
| Slack | Un CSV est écrit à la place de la publication Slack. |

Lancez la conversion depuis l'application Analyze ou l'API REST, ou connectez-vous vous-même plutôt que par un assistant, pour lier ces éléments.

### Destinations non liées

Une destination sans liaison écrit son équivalent PlaidCloud et avertit **Destination target unbound**, en nommant la cible d'origine. La conversion ne contacte jamais le système cible.

| Destination | Résultat |
| --- | --- |
| Cible de base de données, d'entrepôt de données ou SaaS (Oracle, base de données générique, Looker Studio, NetSuite, SAP, et Google Sheets, Tableau ou Slack sans connexion liée) | Une table du projet, nommée d'après le nœud de destination. |
| Stockage de fichiers (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | Le fichier, dans le type de fichier de la destination, dans un dossier de documents sous le compte que vous avez indiqué pour les sources non liées. Le dossier reproduit le dossier cible. Les identifiants et les jetons de partage sont retirés du chemin. |
| E-mail | Un CSV, dans le compte de documents que vous avez indiqué pour les sources non liées. |

L'avertissement vous indique ce qu'il faut lier pour atteindre la vraie cible. Une destination dont la liaison est inutilisable écrit un CSV et avertit **Fallback, target not written**, avec la cible d'origine dans le message ; vérifiez ce CSV avant de vous y fier. Une destination CSV simple écrit son propre fichier.

### Destinations fractionnées

Une destination qui écrit un fichier, un sous-dossier ou un onglet par valeur d'un champ fractionne les fichiers CSV, Excel, Parquet et PDF ainsi que les onglets Google Sheets.

- **Parquet et PDF.** Un fichier par valeur.
- **Google Sheets.** Un onglet par valeur.
- **Modèle.** Un classeur modèle sert de base au classeur de chaque valeur. Un modèle manquant déclenche un avertissement et le classeur est écrit sans lui.
- **Valeurs NULL.** Une valeur de fractionnement NULL est écrite dans son propre fichier ou onglet, et non ignorée.
- **Un champ absent de l'entrée.** Un fractionnement, ou un tri, sur un champ que l'entrée ne contient pas est refusé en le nommant, car Savant échoue dessus.
- **Un `/` ou un `\` dans une valeur.** Une valeur de fractionnement qui contient une barre oblique ou une barre oblique inverse ne peut pas servir de nom de fichier ou d'onglet ; elle est donc assainie. Une valeur modifiée reçoit un suffixe fixe de six caractères, `-` suivi des six premiers caractères du hachage MD5 de la valeur, placé avant l'extension du fichier. Les valeurs qui n'ont pas besoin de modification conservent leur nom.

### Valeurs exportées et ordre des lignes

- **Nombres et booléens simples.** Les exports CSV, TSV et TXT écrivent les nombres sous forme de nombres simples et les booléens sous la forme `true` et `false`, sans `+00:00` sur les horodatages.
- **Ordre des lignes stable.** Une destination qui trie écrit le même ordre de lignes à chaque exécution : les égalités sont départagées de la même façon à chaque fois, et les routes de fractionnement et de parties trient aussi. Les cibles Parquet, Google Sheets, Tableau et table ne conservent aucun ordre de lignes.

### Options Excel

Une destination Excel associe ces options :

- **Onglet par valeur de champ.** Chaque valeur du champ devient une feuille. Les valeurs vides vont dans `Sheet1`, et les feuilles dont les noms entrent en collision reçoivent un suffixe numérique.
- **Format depuis un modèle.** Chaque exécution copie d'abord `<name>_template.xlsx` depuis le même dossier par-dessus le classeur, puis écrit dedans, de sorte que le classeur est toujours remplacé. Si le modèle est absent, la copie déclenche un avertissement et le classeur est écrit sans lui.
- **Cellule en haut à gauche.** Les lignes sont écrites dans le classeur à partir de cette cellule.
- **Mode `create`.** Chaque exécution écrit le fichier selon le mode d'écriture de la destination.

## Lier des requêtes API

Un agent API dont l'URL est relative, comme `/v2/customers`, n'a aucun hôte vers lequel envoyer. Liez-en un avec `api_bindings`. La clé est l'identifiant ou le nom du nœud API, ou `*` pour tous les nœuds API sans liaison propre. La valeur est l'une des suivantes :

- Une URL de base, sous forme de chaîne ou de `{"base_url": "https://host/path"}`. L'URL relative lui est jointe. L'URL doit être `http` ou `https` avec un hôte public, et ne comporter ni utilisateur, ni requête, ni fragment.
- `{"connection": "<REST connection id>"}`. La requête va vers l'hôte de cette [connexion REST](/fr/reference/connectors/rest/generic-rest/) et transporte ses identifiants. Vous avez besoin de l'autorisation d'écriture sur la connexion, et celle-ci doit être une connexion REST que vous pouvez voir.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

Une clé sans correspondance est un avertissement, et une liaison que vous ne pouvez pas utiliser est refusée. Une URL relative sans liaison reste un espace réservé nommé.

Pour un assistant IA (MCP) sans autorisation d'écriture sur la connexion, une liaison de connexion est ignorée avec un avertissement, et l'URL relative qu'elle aurait jointe reste un espace réservé. Liez une URL de base, ou lancez la conversion depuis l'application Analyze ou l'API REST.

Un hôte, un port ou un chemin provenant d'un champ d'entrée n'a besoin d'aucune liaison. Il est renseigné ligne par ligne, chaque valeur étant vérifiée au moment de son utilisation, et le rapport répertorie les hôtes qu'une ligne peut nommer. Une requête qui transporte un identifiant ne peut pas tirer son hôte d'un champ de la ligne : envoyer un identifiant vers un hôte choisi par les données est refusé.

La pagination se convertit aussi. Une URL de page suivante dans la réponse, un en-tête `Link`, un décalage (offset) et un numéro de page deviennent chacun un mode de pagination de l'étape [Requête REST](/fr/reference/workflow-steps/general/rest-request/), qui lit toutes les pages. Une valeur de pagination peut provenir d'un champ d'entrée (`{{Field}}`) ou d'un paramètre (`{{Param}}`), et une valeur écrite sous forme de texte numérique tel que `10.0` est lue comme un nombre.

## Étapes API avec identifiants

Un identifiant dans les en-têtes, le chemin d'URL, la requête ou le corps d'un agent API est déplacé vers une connexion REST PlaidCloud que l'importation crée. L'étape Requête REST fait référence à cette connexion, de sorte que l'identifiant ne figure jamais dans l'étape.

- La réponse répertorie les connexions que l'importation a créées ou réutilisées sous `connections`, et le rapport d'importation les nomme. Importer à nouveau la même analyse réutilise la même connexion au lieu d'en créer une autre.
- Les identifiants présents dans les informations utilisateur de l'URL et dans les en-têtes vont dans les champs d'authentification propres à la connexion ou dans ses en-têtes par défaut. Les secrets du chemin, de la requête et du corps sont stockés chiffrés sur la connexion et renseignés à l'exécution, uniquement pour les requêtes vers l'hôte `https` de cette connexion.
- Un point de terminaison `http://` non chiffré n'est pas converti avec ses identifiants. L'identifiant est omis et le rapport de conversion avertit qu'il n'a pas été copié.
- L'importation via un assistant IA (MCP) ne crée pas de connexions. Les identifiants sont omis et un avertissement le signale. Importez plutôt depuis l'application Analyze ou l'API REST, ou ajoutez l'identifiant à une connexion REST à la main et sélectionnez-la sur l'étape.
- Un utilisateur sans autorisation d'écriture sur la connexion obtient le même résultat : identifiants omis et avertissement.
- Seul un emplacement d'identifiant d'API déplace un paramètre vers une connexion. Un paramètre de pipeline utilisé dans un en-tête, une requête, un chemin ou un corps à l'endroit où va un identifiant d'API est déplacé vers les `secret_values` chiffrés de la connexion, et l'étape y fait référence via la connexion. Il n'est jamais créé comme variable de workflow, quel que soit son nom.
- Tout autre paramètre dont le nom contient un mot secret (tel que `password`, `token`, `secret` ou `key`, `key` faisant exception après un mot de données comme `sort` ou `partition`) devient une variable de workflow à valeur vide, avec un avertissement. Un nom tel que `api_key_2` est également vidé. Définissez la valeur sur la variable de projet après l'importation.
- Un paramètre nommé d'après un nombre ou une limite, tel que `max_tokens`, conserve sa valeur.
- Un secret saisi dans une formule, un filtre ou une valeur de remplacement est omis de l'étape et le rapport de conversion avertit. Un chemin, une URL et un condensat hexadécimal de 40 ou 64 caractères sont conservés, sauf si une partie d'entre eux ou un nom secret indique le contraire. Les liens de partage de dossier et les adresses e-mail des destinataires n'apparaissent jamais dans les avertissements ni les notes.
- Une réponse qui renvoie un identifiant en écho est stockée telle que reçue. Traitez la table de sortie d'une telle requête comme sensible.

## JWT_ENCODE

`JWT_ENCODE` se convertit en une étape [JWT Encode](/fr/reference/workflow-steps/tables/table-jwt-encode/). Une clé de signature littérale va dans une connexion dédiée liée à l'étape, et le jeton est signé à l'exécution, de sorte que la clé n'apparaît jamais dans la configuration de l'étape. Via un assistant IA, ou sans autorisation d'écriture sur la connexion, la clé est omise, le jeton est NULL, et un avertissement vous invite à importer à nouveau avec l'autorisation de créer des connexions.

## Promouvoir une ligne de données en en-têtes de colonne

Un agent Format réglé sur **replace names with row** se convertit en une étape [Promote Header](/fr/reference/workflow-steps/tables/table-promote-header/). À l'exécution, la ligne choisie, comptée à partir de 1, devient les noms de colonne et est supprimée. Une source qui ne porte aucun ordre d'enregistrement reçoit une note, car la ligne qui nomme les colonnes peut changer d'une exécution à l'autre. Une colonne que cette ligne nomme mais qu'aucune étape ultérieure ne mentionne n'est pas reportée au-delà d'une étape qui liste les colonnes qu'elle lit.

## Fichiers sans colonnes déclarées

Une source sans colonnes déclarées conserve ces colonnes :

- Une source CSV, TSV ou TXT liée à l'importation conserve toutes les colonnes de l'en-tête du fichier.
- Tout autre type de fichier, et toute source non liée, ne conserve que les colonnes que les étapes ultérieures nomment, et le rapport de conversion avertit.
- Un en-tête promu sur une telle source lit toutes les colonnes, pour les fichiers CSV, Excel, XLS, JSON, Parquet et Avro.

Lorsqu'une telle source n'alimente qu'un en-tête promu, l'importation est une étape [Import Delimited](/fr/reference/workflow-steps/import/import-delimited/) qui lit toutes les colonnes par position. Une étape qui exporte ou joint après un en-tête promu reporte toutes les colonnes que la table possède à l'exécution (consultez **Reporter aussi les colonnes nommées à l'exécution** dans [Table Extract](/fr/reference/workflow-steps/tables/table-extract/)).

## Comportements à connaître

Ces conversions se comportent comme suit.

| Agent | Comportement |
| --- | --- |
| Blend (`blend`) | Jointures sur des prédicats combinés par OR, contains et is-part-of. Les blends « externe excluant l'interne » et les sorties sans correspondance se convertissent en flux de jointure correspondants. Pour tout opérateur, la clé en double du côté droit est retirée de la sortie. |
| Dedupe (`deduplicate`) | Conserve le premier enregistrement par clé dans chaque groupe **Regrouper par**. L'indicateur de doublons marque chaque membre d'un groupe de doublons, et les doublons peuvent aussi être routés vers un second flux. Avec une seule sortie connectée, il se comporte comme Savant. |
| Summarize (`summarize`) | Les agrégats de fenêtre ajoutent l'agrégat à chaque ligne au lieu de réduire les groupes. |
| Sample (`sample`) | N premières lignes, par groupe ou globalement, un pourcentage ou un nombre de lignes aléatoire, ou une ligne sur N. |
| Time Series (`rollup`) | Périodes de jour, semaine, mois, trimestre, année et décennie entre les dates de début et de fin facultatives, par groupe. Les périodes mensuelles sont libellées `YYYY-MM`, et les périodes sans enregistrement apparaissent avec des zéros. Les enregistrements dont la date est NULL sont exclus. |
| Pivot (`pivot`) | COUNT compte les lignes. |
| XML (`xml`) | SELECT extrait des éléments, les chemins peuvent porter des espaces de noms, et TO_JSON convertit le XML en JSON. Tout chemin XPath 1.0 se convertit, y compris les prédicats, les tests d'attribut, les jokers et les fonctions telles que `count()`, `name()` et `contains()`, et l'étape [Analyse XML](/fr/reference/workflow-steps/tables/table-xml-parse/) le lit comme du XPath. Avec `processNs` désactivé, les noms sont comparés littéralement, préfixe compris. Un fichier XML manquant au moment de la conversion résout son élément racine à l'exécution du workflow. |
| JSON (`json`) | Aplatit en colonnes larges. Un texte qui n'est pas du JSON valide donne NULL, et les tableaux ressortent sous forme de texte. |
| Split (`split`) | Fractionne en colonnes ou en lignes, le nombre de colonnes étant lu dans les données à chaque exécution du workflow. |

Ces fonctions d'expression suivent les résultats de Savant :

| Fonction | Comportement |
| --- | --- |
| `DATE_DIFF` | Les semaines et les trimestres sont comptés comme le fait Savant. |
| `PAD` | Ne tronque pas une valeur plus longue que la largeur cible. |
| `+` sur du texte | Concatène du texte. Une colonne issue d'une source sans types déclarés est lue comme un nombre, de sorte que `+` additionne, et une note le signale. |
| Fractionner en lignes | Conserve les morceaux vides sous forme de lignes. |
| `LAST` sans tri | Renvoie la dernière ligne dans l'ordre d'arrivée des lignes, avec une note indiquant que l'entrepôt de données ne garantit pas cet ordre. |
| `JOIN_STR` | Joint un nombre fractionnaire tel que Savant l'écrit, sans remplissage de zéros à la fin. |
| `JSON_FORMAT` | Met le JSON en forme lisible ; sur Snowflake, il écrit le JSON de façon compacte sur une seule ligne. |
| `JSON_SET` | Conserve l'ordre des clés de Savant. |
| `GREATEST` et `LEAST` | Ignorent les arguments NULL. Le résultat n'est NULL que lorsque tous les arguments sont NULL. |
| `ROUNDUP` | Arrondit au pas entier supérieur, de sorte qu'un nombre négatif est arrondi vers zéro : -1,5 devient -1. `ROUNDDOWN` est inchangé. |
| `DURING_DAYLIGHT_SAVING` et `DURING_STANDARD` | NULL en entrée donne NULL en sortie. |
| `TO_TEXT` avec un format de date | Lit les jetons de format comme Savant. `YYYY`, `w` et `u` sont l'année, la semaine et le jour de la semaine ISO, et une lettre de fuseau ou d'ère est écrite comme pour une heure UTC. |
| `TO_TEXT` et sortie de nombre en texte | Écrit des nombres simples tels que `12`, et non `12.0000000000`. |
| `TO_TEXT` avec un motif numérique | Met en forme comme le fait un `DecimalFormat` Java, avec arrondi à la valeur paire la plus proche (half to even), motifs scientifiques tels que `##0.##E0` compris. |
| `TO_TEXT` et analyse de date avec un format par ligne | Lit le format dans chaque ligne. |
| Jetons de date de fraction de seconde, de mois abrégé à une lettre et de semaine | Se convertissent. Les jetons de semaine sont lus comme des semaines ISO. |
| Années à deux chiffres (`yy`, `y`) | Lues dans une fenêtre de 80 ans en arrière et de 20 ans en avant à partir de l'année en cours. |
| `REGEX_MATCH` | Une correspondance partielle : le motif correspond n'importe où dans le texte, et non au texte entier. |

`TO_TEXT` et les formats de date se convertissent dans une étape [Text Function](/fr/reference/workflow-steps/tables/table-text-function/). Une modification qui ne porte que ses étapes compilées, sans expression, se convertit en ces étapes appliquées dans l'ordre, chacune alimentant la suivante, et le rapport de conversion indique l'ordre supposé. Le convertisseur refuse en les nommant les éléments sur lesquels Savant lui-même échoue ou qui n'ont rien à convertir, et l'étape devient un espace réservé : une fonction d'agrégat ou de fenêtre simple dans une expression Transform ou Filter (dans un calcul ou un Summarize, elle se convertit), `HASH` avec un algorithme littéral autre que `md5` ou `sha1`, une construction d'expression régulière que PlaidCloud ne sait pas lire (une classe dans une classe, une intersection de classes ou une propriété `\p{}` inconnue), une modification Transform sans expression ni étapes compilées (comme une modification Copilot qui n'a que son invite), un chemin XML qui n'est pas du XPath 1.0, et une requête API qui transporte un identifiant et tire son hôte d'un champ de la ligne. La [matrice de conversion Savant](/fr/reference/savant-conversion-matrix/#refus-nommés) les répertorie chacun avec sa raison.

Des fonctions d'expression se convertissent aussi pour `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, les fonctions d'heure d'été (`DST`) et les fonctions d'expression régulière qui prennent une n-ième correspondance. `DAY_OF_WEEK` numérote le dimanche 7, et `DAY_NAME` renvoie le nom du jour.

## Lire le rapport de conversion

La réponse contient le rapport de conversion : un résumé du nombre d'étapes converties avec un niveau de confiance élevé, moyen ou faible et du nombre d'étapes non converties, ainsi que les avertissements et les nœuds que le convertisseur a absorbés dans d'autres. Lisez-le avant d'exécuter le workflow. Il nomme chaque espace réservé, chaque source non liée et chaque liaison sans correspondance, ainsi que le préfixe de table utilisé.

## Espaces réservés pour les configurations non converties

Une configuration que le convertisseur ne peut pas reproduire est créée sous la forme d'une étape d'espace réservé qui porte le nom de l'agent, et le rapport de conversion la nomme. Un espace réservé apparaît pour une construction que le convertisseur refuse en la nommant (consultez la [matrice de conversion Savant](/fr/reference/savant-conversion-matrix/#refus-nommés)) ou que l'export ne décrit pas complètement, comme une configuration d'API manquante. Par défaut, un espace réservé échoue lorsque le workflow l'atteint, afin qu'une exécution ne puisse pas déclarer un succès pour un travail qui n'a pas eu lieu.

Définissez `allow_unconverted_placeholders` sur `true` pour importer chaque espace réservé comme une étape en transit. L'exécution se poursuit alors au-delà de celui-ci et la sortie de l'espace réservé est son entrée. Reconstruisez la fonctionnalité avec une étape native lorsque son résultat compte.

## Exécuter le workflow converti

1. Ouvrez le nouveau workflow dans le projet.
2. Définissez les variables de projet issues des paramètres Savant.
3. Téléversez les fichiers des sources non liées vers les chemins indiqués dans le rapport.
4. Exécutez le workflow et examinez la table de sortie de chaque étape.

## Cas particuliers

Ce sont les seules différences connues par rapport à Savant. Le rapport de conversion nomme chacune de celles qui s'appliquent.

- **Formats de date.** `TO_DATE` ou `TO_DATETIME` avec un format contenant un littéral `[`, `]`, `'`, `\` ou `^`, sur un texte qu'il lit en 9999-12-30 ou 9999-12-31, dépasse le dernier horodatage que l'entrepôt de données peut contenir, et le rapport avertit.
- **Paramètres secrets.** Un paramètre dont le nom contient un mot secret, ou dont la valeur ressemble à un identifiant, devient une variable de projet à valeur vide, par conception. Définissez la valeur dans la variable.
- **Paramètres non déclarés.** Un paramètre qu'un nœud utilise et que l'export ne déclare pas arrive sous forme de variable de projet à valeur vide.
- **`JSON_FORMAT` sur Snowflake.** Il écrit le JSON de façon compacte sur une seule ligne.
- **Ordre des lignes.** Les cibles Parquet, Google Sheets, Tableau et table triées ne conservent aucun ordre de lignes.
- **Google Sheets et Tableau.** Publier vers l'un ou l'autre exige que son compte soit lié via `destination_bindings`.

## Guides associés

- [Matrice de conversion Savant](/fr/reference/savant-conversion-matrix/)
- [Connexion REST](/fr/reference/connectors/rest/generic-rest/)
- [Ajouter des comptes de documents](/fr/guides/documents/adding-accounts/)
- [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/)
- [Étape AI/NLP](/fr/reference/workflow-steps/text-documents/nlp-ai/)
- [Étape Requête REST](/fr/guides/workflows/rest-request-step/)
- [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/)
