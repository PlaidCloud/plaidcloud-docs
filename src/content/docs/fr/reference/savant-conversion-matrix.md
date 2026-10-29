---
title: Matrice de conversion Savant
description: Comment PlaidCloud convertit les analyses Savant Labs en workflows avancés natifs, avec le niveau de mappage de chaque agent et les quelques cas limites nommés.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

PlaidCloud convertit les analyses Savant Labs en workflows avancés natifs. L'importeur
associe chaque agent Savant à une étape de workflow, une variable de projet ou un
objet du canevas, de sorte qu'un workflow converti s'exécute en mode cloud natif.

Pour lancer une conversion, consultez [Migrer des analyses Savant](/fr/guides/workflows/migrate-savant-analyses/).

Chaque agent a un niveau de mappage. **Complet** signifie que chaque option de l'agent
dispose d'un mappage valide vers une étape PlaidCloud. Les constructions refusées par leur nom sont listées
sous Refus nommés.

Les connecteurs de systèmes externes sont **connectés, et non convertis** : consultez
[Connexion à des systèmes externes](#connexion-à-des-systèmes-externes).

## Agents pris en charge

Les 33 agents sont convertis au niveau Complet.

| Agent | Niveau | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Agent Adapter (`adapter`) | Complet | Étape de sélection et de projection du schéma | Renomme, change le type et ordonne les champs. |
| Agent API / Infer (service hérité) (`service`) | Complet | Identique à l'agent API ou Infer, selon serviceType | Un LLMService est converti comme l'agent Infer et un APIService comme l'agent API ; un serviceType manquant ou mal orthographié est déduit des clés du nœud, avec un avertissement. |
| Agent API (`apiService`) | Complet | Table Extract, [Requête REST](/fr/reference/workflow-steps/general/rest-request/) et une jointure gauche pour rattacher le résultat | Une requête GET, POST, PUT, PATCH ou DELETE par ligne d'entrée ; le corps brut de la réponse est placé dans une colonne de texte, les erreurs HTTP restent des lignes, chaque ligne d'entrée est conservée, et un quota par période devient un nombre fractionnaire de requêtes par seconde. Une URL relative est complétée par l'URL de base de ses api_bindings ou par l'hôte de la connexion REST ; un hôte, un port ou un chemin issu d'un champ de la ligne est substitué ligne par ligne ; la pagination par URL suivante, en-tête Link, décalage et page est prise en charge, y compris lorsque le début, la taille de page ou le nom du paramètre est défini à partir d'un champ de la ligne. |
| Agent Blend (`blend`) | Complet | [Jointure interne](/fr/reference/workflow-steps/tables/table-inner-join/), [Jointure externe](/fr/reference/workflow-steps/tables/table-outer-join/), [Anti-jointure](/fr/reference/workflow-steps/tables/table-anti-join/) | Fusions interne, gauche, droite, complète, anti-jointure et externe excluant l'interne, conditions jointes par OR, « contient » et « fait partie de », avec des flux de lignes correspondantes et non correspondantes ; les colonnes que seul un pivot ou une analyse nomme à l'exécution sont conservées. |
| Agent Dedupe (`deduplicate`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec lignes distinctes | Conserve le premier enregistrement pour chaque clé, au sein des groupes Regrouper par, et dirige les doublons vers un second flux ou les signale. |
| Agent Destination (`destination`) | Complet | [Exportation : CSV](/fr/reference/workflow-steps/export/export-to-csv/), [Exportation : Excel](/fr/reference/workflow-steps/export/export-to-excel/), Exportation : Parquet, JSON, Avro ou XML, [Export to PDF](/fr/reference/workflow-steps/export/export-to-pdf/), [Exportation : Tableau Hyper](/fr/reference/workflow-steps/export/export-hyper/) avec [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/fr/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/fr/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/fr/reference/workflow-steps/notifications/notify-via-slack/), ou e-mail | Écrit via destination_bindings vers un compte de documents (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF ou .hyper Tableau, dans n'importe quel jeu de caractères Java, y compris les alias, CESU-8 et les formes avec marque d'ordre des octets ; un caractère absent du jeu de caractères est écrit sous la forme ?), une table de connexion, une feuille Google Sheets, une source de données Tableau ou un canal Slack, ou vers des destinataires d'e-mail. Une destination non liée écrit à la place une table de projet ou un fichier de documents (voir « Destination dans PlaidCloud » ci-dessous). Un fichier, un sous-dossier ou un onglet par valeur de champ découpe les fichiers CSV, Excel, Parquet et PDF ainsi que les onglets Google Sheets ; un modèle initialise chaque classeur d'un découpage. Les options Excel sont mappées : les valeurs vides vont dans `Sheet1`, les noms de feuille en conflit reçoivent un suffixe, `formatFromTemplate`, `topLeftCell` et le mode `create`. Les modes Append, upsert, update et groupReplace fusionnent sur les clés de correspondance (un fichier ou une table est relu puis réécrit ; un découpage relit le fichier dans lequel chaque valeur de l'exécution est écrite et fusionne à l'intérieur, en laissant les autres fichiers en l'état ; Tableau met à jour ses lignes sur place). Les colonnes que seules les données nomment (celles d'un en-tête promu, les valeurs d'un pivot, les clés d'un JSON ou d'un XML analysé) sont écrites à côté des colonnes connues par chaque exportation et chaque écriture de table, triées et découpées, puis ajoutées ou fusionnées dans une table, ou dans un fichier relu avec toutes ses colonnes. |
| Agent Explode (`explode`) | Complet | [Jointure croisée](/fr/reference/workflow-steps/tables/table-cross-join/) | Effectue une jointure croisée entre un petit côté et le flux principal. |
| Agent Filter (`filter`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression de filtre | Répartit les enregistrements, par assistant ou par expression, entre les chemins vrai et faux. |
| Filter Pushdown (`pdfilter`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression de filtre | Filtre côté base de données, converti comme Filter. |
| Agent Format (`format`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec renommage de colonnes, ou Promote Header | Masque, change le type, renomme et remplit les champs identifiés par leur nom (contient, commence par, finit par) ou parce qu'ils sont vides ; un remplissage écrit sa valeur par défaut dans toute colonne dont le type accepte cette valeur (texte, nombre, date). La promotion de la ligne d'en-tête et la détection des valeurs vides s'exécutent à l'exécution dans l'étape Promote Header, et un en-tête promu lit toutes les colonnes de son fichier. |
| Agent Fuse (`fuzzy_match`) | Complet | [Fuzzy Match](/fr/reference/workflow-steps/tables/table-fuzzy-match/), entre un Union All et deux jointures | Empile les deux entrées, fait correspondre les enregistrements sur les champs clés avec un seuil de similarité de 80, puis rejoint les deux côtés avec un score de confiance. |
| Group (`group`) | Complet | Conteneur du canevas | Conservé comme organisation du workflow. |
| Agent Infer (`gen_ai`) | Complet | Tâche d'invite [AI/NLP](/fr/reference/workflow-steps/text-documents/nlp-ai/) | L'invite s'exécute ligne par ligne sur les champs d'entrée, via la connexion LLM visible correspondant au fournisseur et au modèle de Savant ; la réponse est placée dans une colonne AI Answer à côté de chaque colonne d'entrée. rowLimit plafonne le nombre de lignes traitées par exécution et conserve les réponses antérieures : une ligne déjà traitée (même invite, même modèle et mêmes valeurs d'entrée) garde sa réponse, et seules les lignes sans réponse comptent dans la limite. |
| Agent JSON (`json`) | Complet | [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/) | Aplatit un champ JSON en colonnes à clés pointées, ou éclate un tableau en une ligne par élément ; les clés sont lues dans les données à l'exécution. |
| Agent Notes (`notes`) | Complet | Annotation du canevas | Conservé comme contexte du workflow. |
| Agent Pivot (`pivot`) | Complet | [Pivot](/fr/reference/workflow-steps/tables/table-pivot/) | Transforme des lignes en colonnes avec agrégation. |
| Agent Recursion (`hierarchy`) | Complet | Hierarchy Closure, [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) et [Jointure multi-tables](/fr/reference/workflow-steps/tables/table-multi-table-join/) | Parcourt une arborescence parent/enfant à n'importe quelle profondeur, en agrégeant chaque nœud sur les identifiants de son chemin jusqu'à la racine, lui-même inclus, et écrit Depth et Path ; une boucle s'arrête au nœud répété. |
| Agent Sample (`sample`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une limite de lignes | Conserve les N premières lignes, éventuellement par groupe, un pourcentage aléatoire ou N lignes aléatoires, ou une ligne sur N. |
| Search and Replace (`search_replace`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec des expressions de remplacement imbriquées, réparties en plusieurs étapes | Règles de recherche/remplacement (contient ou correspond ; remplacer ou ajouter), avec ou sans respect de la casse, mot entier ou non, appliquées dans l'ordre sur les champs de texte choisis, ou sur tous les champs de texte si aucun n'est nommé. |
| Agent Source (`source`) | Complet | Étapes d'importation liées par `source_bindings` ([Importation : CSV](/fr/reference/workflow-steps/import/import-csv/), [Importation : Excel](/fr/reference/workflow-steps/import/import-excel/), [Importation : SQL](/fr/reference/workflow-steps/import/import-sql/)) ou une table existante | Lit la table ou le document lié ; une source non liée crée une importation vide et un avertissement. Un texte XML lit son document via Importer depuis XML (une source non liée lit savant/<workflow>/<name>.xml). Une source liée à un document XML écrit aussi les autres colonnes de l'exportation : une colonne de nom ou de chemin de fichier issue du document, le reste vide. Une source placée sous un Format qui promeut une ligne d'en-tête lit par position toutes les colonnes de son fichier CSV, Excel (y compris Excel 97 .xls), JSON, Parquet ou Avro. |
| Agent Spatial Match (`spatial_match`) | Complet | [Spatial Match (executor)](/fr/reference/workflow-steps/spatial/spatial-match-executor/), [Jointure croisée](/fr/reference/workflow-steps/tables/table-cross-join/) ou [Rechercher le plus proche](/fr/reference/workflow-steps/spatial/spatial-find-nearest/) | Correspondances par intersection, inclusion (within), contient, touche, croise, chevauche, égale, disjoint et correspondances multirègles and/or, distance géodésique entre n'importe quelles géométries (points, lignes, polygones : la distance minimale sur une sphère de 6 371 km), N plus proches selon cette même distance avec une distance maximale (une règle de plus proche voisin seule n'écrit aucune colonne Distance, comme Savant n'en écrit aucune ; combinée à d'autres règles en plus proche puis filtre, les jointures AND et les unions OR, chaque règle de plus proche voisin ajoute sa propre colonne Distance), et Cross, avec des flux de lignes correspondantes et non correspondantes. |
| Agent Spatial Summarize (`spatial_summarize`) | Complet | [Combinaison spatiale](/fr/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid et étapes de point vers ligne | Union, intersection, rectangle englobant, un ou plusieurs centres géométriques, et constructions de polylignes ou de polygones, par groupe avec un tri facultatif. |
| Agent Split (`split`) | Complet | Split Text, ou [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec des colonnes split_part | Découpe un champ de texte selon un séparateur littéral de longueur quelconque en lignes ou en colonnes, avec suppression des espaces et conservation de l'original ; le nombre de colonnes est lu dans les données à l'exécution. |
| Découper la sortie (`outlet`) | Complet | Lien du workflow | Dirige une sortie nommée vers ses consommateurs. |
| Agent Stack (`multi_stack`) | Complet | [Union All](/fr/reference/workflow-steps/tables/table-union-all/) | Empile un nombre quelconque d'entrées par nom ou par position. |
| Agent Summarize (`summarize`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec agrégation | Regroupe et agrège, y compris premier/dernier selon un tri déterministe et agrégats de fenêtre ligne par ligne (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec agrégation | Agrégation côté base de données, convertie comme Summarize. |
| Text (`text`) | Complet | Annotation du canevas | Conservé comme contexte du workflow. |
| Agent Time Series (`rollup`) | Complet | Agrégation [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) sur une expression de tranche de période, Period Spine, [Anti-jointure](/fr/reference/workflow-steps/tables/table-anti-join/) et [Union All](/fr/reference/workflow-steps/tables/table-union-all/) | Cumule les enregistrements par jour, semaine, mois, trimestre, année ou décennie entre des dates de début et de fin facultatives, par groupe, en excluant les dates NULL et en remplissant de zéros les périodes vides. |
| Agent Transform (`edit`) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec des expressions de colonne | Colonnes calculées, changements de type et calculs de fenêtre (lag, lead, somme cumulée, numéro de ligne, remplissage vers l'avant et vers l'arrière), évalués dans l'ordre. Une modification qui ne porte que ses étapes compilées est convertie en ces étapes appliquées dans l'ordre, chacune alimentant la suivante. |
| Agent Unpivot (`unpivot`) | Complet | [Melt](/fr/reference/workflow-steps/tables/table-melt/) | Convertit des colonnes en lignes sous forme de paire nom/valeur. |
| Agent Vision (`vision`) | Complet | [Image OCR](/fr/reference/workflow-steps/text-documents/image-ocr/), puis la tâche d'invite [AI/NLP](/fr/reference/workflow-steps/text-documents/nlp-ai/) | Chaque document est envoyé au fournisseur sous forme d'image ou de PDF lorsque celui-ci accepte ce type et cette taille, sinon sa couche de texte PDF ou son texte OCR est envoyé ; la réponse à l'invite est placée dans une colonne AI Answer. |
| Agent XML (`xml`) | Complet | [Analyse XML](/fr/reference/workflow-steps/tables/table-xml-parse/) | Sélectionne des éléments, extrait les valeurs et attributs enfants dans des colonnes, ou convertit XML vers JSON ; un chemin simple //a/b est converti comme auparavant et tout autre chemin XPath 1.0 (prédicats, tests d'attributs, caractères génériques, fonctions telles que count(), name() et contains()) est évalué comme XPath, avec prise en charge des espaces de noms ou tel qu'écrit. |

Les variantes de câblage, de canevas et de pushdown (Découper la sortie, Group, Text, Filter Pushdown, Summarize Pushdown) sont des types de nœuds Savant sans article d'agent propre dans le centre d'aide ; chacune est convertie comme l'agent qu'elle reproduit.

Un identifiant de connexion dans une requête de l'agent API n'est jamais copié dans une étape de workflow. Sur https, il est déplacé vers une connexion REST ; sur http, sans l'autorisation d'écrire des connexions, ou lors d'une conversion effectuée via MCP, il est retenu avec un avertissement. C'est voulu et cela n'abaisse pas le niveau.

Deux limites de destination n'abaissent pas le niveau. Quelques jeux de caractères rares (par exemple `x-ISCII91` ou `JIS_X0212`) ne peuvent pas être écrits ; le fichier est alors écrit en UTF-8 et la conversion émet un avertissement. Une publication Tableau qui fusionne sur des clés exige `replace: true` dans sa liaison de destination ; sans cela, la conversion émet un avertissement et publie une nouvelle source de données, ce qui échoue lors d'une exécution où il en existe déjà une.

## Refus nommés

Huit constructions sont refusées par leur nom plutôt que converties. Aucune n'abaisse le niveau d'un agent.

| Construction | Raison du refus |
| --- | --- |
| Une requête de l'agent API qui porte un identifiant et tire son hôte d'un champ d'entrée | Chaque ligne pourrait envoyer l'identifiant à un hôte choisi par les données. La requête devient un espace réservé nommé. Une requête sans identifiant, et un identifiant sur un hôte fixe, sont convertis. |
| Une modification Transform sans expression ni étapes compilées, comme une modification Copilot qui ne contient que son invite | Il n'y a rien à convertir : une invite n'est pas une formule. Une modification avec des étapes compilées est convertie. |
| Une construction d'expression régulière dans une expression Transform ou Filter que PlaidCloud ne peut pas lire : une classe dans une classe, une intersection de classes (`&&`) ou une propriété `\p{}` inconnue | L'étape devient un espace réservé nommé qui refuse de s'exécuter. |
| Une fonction d'agrégation ou de fenêtre dans une expression Transform ou Filter | Savant lui-même échoue à l'exécution. Comme calcul Transform ou dans un Summarize, elle est convertie. |
| `HASH` dans une expression Transform ou Filter avec un algorithme littéral autre que `md5` ou `sha1` | Savant lui-même échoue (l'algorithme est `md5` ou `sha1`). Un algorithme lu dans une colonne est converti et donne NULL pour toute autre valeur. |
| Un tri de destination sur une colonne que son entrée ne contient pas | Savant lui-même échoue à l'exécution. |
| Un fichier, sous-dossier, onglet ou feuille de calcul de destination par valeur d'une colonne que son entrée ne contient pas | Savant lui-même échoue à l'exécution. |
| Un chemin de l'agent XML qui n'est pas du XPath 1.0 | Savant ne peut pas l'exécuter non plus. |

Une URL d'API relative est convertie lorsque vous liez une URL de base ou une connexion REST avec `api_bindings` ; consultez [Liaisons au moment de la conversion](/fr/guides/workflows/migrate-savant-analyses/#liaisons-au-moment-de-la-conversion).

## Langage d'expression

Les fonctions et opérateurs d'expression Savant sont convertis en expressions PlaidCloud. Niveau : **Complet**. Chaque fonction et chaque format est converti, y compris `TO_TEXT` avec un motif numérique, un format connu seulement ligne par ligne, les jetons de date pour les fractions de seconde, les semaines, les trimestres et les fuseaux, les années à deux chiffres et les constructions d'expressions régulières Java. Les fonctions GEO_* présentes n'importe où dans une expression s'exécutent dans des étapes spatiales associées. Les exceptions sont les [refus nommés](#refus-nommés).

Cas limites connus : `TO_DATE` ou `TO_DATETIME` avec un format contenant un littéral `[`, `]`, guillemet, barre oblique inverse ou `^`, sur un texte qui se lit comme 9999-12-30 ou 9999-12-31, ce qui dépasse le dernier horodatage que l'entrepôt peut contenir ; la conversion émet un avertissement.

## Formats d'exportation

Le chargeur accepte toutes les formes d'exportation Savant — à plat, encapsulée dans un modèle, enregistrement serveur, enveloppe de recette, encapsulée dans un tableau, précédée d'un BOM et alias de types hérités — et les normalise en un seul modèle. Niveau : **Complet**.

## Paramètres d'analyse

Les paramètres d'analyse Savant sont convertis en variables de workflow, et les références qui y sont faites dans les configurations de nœuds sont réécrites dans la syntaxe de variable de PlaidCloud. Les formes de paramètres en liste, en dictionnaire et avec alias sont toutes chargées. Niveau : **Complet**.

Cas limites connus : un paramètre dont le nom contient un mot secret ou dont la valeur ressemble à un identifiant devient une variable à valeur vide, avec un avertissement. Un paramètre utilisé par un nœud mais que l'exportation ne déclare pas devient une variable à valeur vide, avec un avertissement.

## Connexion à des systèmes externes

Les connecteurs Savant sont des cibles de source et de destination, et non des étapes, et une exportation ne contient ni jeux de données ni identifiants. PlaidCloud accède à ces systèmes par une connexion plutôt que par un nœud sur le canevas.

| Savant | Destination dans PlaidCloud |
| --- | --- |
| Connecteur source | `source_bindings` associe le nœud ou le jeu de données Savant à une table PlaidCloud ou à un fichier de documents, lu par l'étape d'importation correspondante ; une source non liée émet un avertissement et ne traite rien |
| Destination : CSV, Excel et autres formats de fichier | Une étape d'exportation ([Exportation : CSV](/fr/reference/workflow-steps/export/export-to-csv/), [Exportation : Excel](/fr/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/fr/reference/workflow-steps/export/export-to-pdf/)) |
| Destination : Google Sheets, Tableau, Slack | [Export to Google Spreadsheet](/fr/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/) ou [Notify via Slack](/fr/reference/workflow-steps/notifications/notify-via-slack/), via une connexion que vous liez avec `destination_bindings` |
| Destination : cible non liée de base de données, d'entrepôt ou SaaS (Oracle, base de données générique, Looker Studio, NetSuite, SAP, ainsi que Google Sheets, Tableau ou Slack sans connexion liée) | Une table de projet portant le nom du nœud de destination, avec un avertissement indiquant la cible d'origine |
| Destination : cible non liée de système de fichiers (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | Le fichier, dans le type de fichier de la destination, dans un dossier de documents qui reproduit le dossier cible, avec un avertissement. Les identifiants et jetons de partage sont retirés du chemin du dossier |
| Destination : e-mail non lié | Un CSV avec un avertissement |
| Destination : liaison inutilisable | Un CSV avec un avertissement indiquant la cible d'origine |

La conversion ne contacte jamais le système source ni le système de destination.
