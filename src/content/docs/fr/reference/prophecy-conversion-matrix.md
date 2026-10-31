---
title: Matrice de conversion Prophecy
description: Comment PlaidCloud convertit les pipelines et les projets SQL Prophecy en étapes de workflow avancé natives, avec le statut de prise en charge de chaque gem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

PlaidCloud convertit les pipelines Spark et les projets SQL Prophecy en workflows
avancés natifs. L'importeur fait correspondre chaque gem Prophecy à une étape de workflow,
une variable de projet ou un objet du canevas, de sorte qu'un workflow converti s'exécute en mode cloud natif
plutôt que par émulation.

Chaque gem, connecteur et structure de projet est converti : **Complet** signifie que le gem
devient une étape, une variable ou un objet de canevas PlaidCloud natif qui accomplit le travail
du gem. Les quelques comportements qu'un workflow converti ne reproduit pas de lui-même
sont répertoriés dans [Cas limites connus](#cas-limites-connus), avec la marche à suivre
pour chacun.

Pour lancer une conversion, consultez [Migrer des projets Prophecy](/fr/guides/workflows/migrate-prophecy-projects/).

## Gems de pipeline Spark

### Source/Target

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Lookup | Complet | [Lookup](/fr/reference/workflow-steps/tables/table-lookup/) | Chaque appel de recherche devient une étape Lookup dans l'étape qui l'utilise ; une clé sans correspondance renvoie NULL, et une clé en double renvoie l'une de ses lignes. |
| Source | Complet | Étape d'importation choisie selon le format du jeu de données (consultez [Connecteurs](#connecteurs)) | Chaque Source devient une étape d'importation dans une table nommée d'après le jeu de données ; un format que le convertisseur ne reconnaît pas est lu comme un fichier CSV téléversé dans le dossier de documents du workflow, avec un avertissement. |
| Streaming Source | Complet | Même importation que la Source par lots | Les sources de streaming sont converties en une importation par lots ponctuelle, avec un avertissement. |
| Streaming Target | Complet | Chargement par ajout en lots | Les cibles de streaming sont converties en un ajout par lots, avec un avertissement. |
| Target | Complet | Étape d'exportation / de chargement de table choisie selon le format du jeu de données et writeMode | Chaque Target devient une étape de chargement ou d'exportation de table dans le mode d'écriture du gem : ajout, écrasement, fusion avec ses expressions SET, upsert, SCD2, replaceWhere et insertInto. |

### Prepare

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Data Cleansing | Complet | Expressions de colonne dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Convertit les options de remplissage des valeurs nulles, de suppression des espaces et de casse en expressions de colonne ; les colonnes nettoyées passent en dernier. |
| Sequence | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression de numéro de ligne | Ajoute une colonne de séquence à partir de la valeur de départ et de l'incrément. |
| Surrogate Key Generator | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression de numéro de ligne | Ajoute une clé séquentielle à partir de la valeur initiale ; les clés se poursuivent d'une exécution à l'autre grâce à une table qui conserve la dernière clé émise. |

### Transform

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Aggregate | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec agrégation ; [Pivot](/fr/reference/workflow-steps/tables/table-pivot/) lorsque le gem pivote | Regroupe et agrège, applique la condition HAVING et pivote en une colonne par valeur de pivot ; propagate-all conserve toutes les autres colonnes d'entrée. |
| Bulk Column Expressions | Complet | Développé en une expression par colonne dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Une expression par colonne listée dans une étape Table Extract ; la conversion avertit que la disposition du gem est supposée. |
| Bulk Column Rename | Complet | Renommage de colonnes dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Un renommage par colonne listée dans une étape Table Extract ; la conversion avertit que la disposition du gem est supposée. |
| Deduplicate | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec distinct ou un filtre sur le numéro de ligne | Conserve une ligne par clé : distincte, première ou dernière selon votre ordre de tri, quelconque, ou uniquement les clés qui n'apparaissent qu'une fois. |
| Dynamic Replace | Complet | Transformation de remplacement dynamique, configurée manuellement | Est converti en règles de remplacement sur la transformation de remplacement dynamique ; la conversion avertit que la disposition du gem est supposée. |
| Dynamic Select | Complet | Sélection de colonnes dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) résolue par type | Résout les colonnes par type au moment de la conversion en une sélection explicite. |
| Filter | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression de filtre | Est converti en une étape Table Extract avec une expression de filtre ; les conditions NULL éliminent la ligne. |
| Flatten Schema | Complet | [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/) et [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Aplatit les champs imbriqués en colonnes nommées avec le délimiteur du gem et déploie les tableaux en une ligne par élément. |
| Fuzzy Match | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) et [User Defined Transform](/fr/reference/workflow-steps/general/user-defined-transform/) | Apparie les enregistrements, note chaque champ de correspondance selon la méthode du gem, fait la moyenne des notes et conserve les paires égales ou supérieures à votre seuil. |
| Group By Rollup | Complet | Union d'étapes d'agrégation [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) par niveau de rollup | Développe le rollup en un agrégat par niveau de regroupement, réunis par union avec des sous-totaux NULL. |
| Limit | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une limite de lignes | Est converti en une limite de lignes ; les références de configuration deviennent des variables de projet. |
| Normalize | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression d'éclatement | Répète chaque enregistrement selon l'expression de longueur, calcule les colonnes de sortie pour chaque indice et s'arrête au premier indice où la condition de fin est remplie. |
| Order By | Complet | Tri sur une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Est converti en un tri avec les mêmes clés, le même sens et le même placement des valeurs nulles. |
| Reformat | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec expressions de colonne | Est converti en une étape Table Extract avec une expression par colonne de sortie ; les colonnes non listées sont supprimées. |
| Sample Rows | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une limite de lignes ou un échantillon aléatoire | Conserve une fraction ou un nombre aléatoire de lignes ; les lignes choisies diffèrent de l'exécution Spark, car l'échantillonnage est aléatoire. |
| Schema Transform | Complet | Chaîne d'étapes [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) appliquées dans l'ordre | Applique chaque opération dans l'ordre : ajouter ou remplacer une colonne, supprimer, renommer, ajouter si absente avec sa valeur par défaut, et ajouter une règle métier de projet. |
| Set Operation | Complet | [Union All](/fr/reference/workflow-steps/tables/table-union-all/) ; [Anti-jointure](/fr/reference/workflow-steps/tables/table-anti-join/) pour except ; [Jointure interne](/fr/reference/workflow-steps/tables/table-inner-join/) pour intersect | Union all empile les entrées ; except all et intersect all conservent le bon nombre de lignes en double. |
| TransposeAgg | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec agrégation | Convertit le regroupement, les agrégats et le pivot du gem sous forme d'Aggregate, avec un avertissement invitant à le vérifier. |
| Unpivot | Complet | [Melt](/fr/reference/workflow-steps/tables/table-melt/) | Empile les colonnes sélectionnées en colonnes de noms et de valeurs. |
| Watermark | Complet | Aucune étape nécessaire | Supprimé : une exécution par lots lit toutes les données présentes, il n'y a donc aucune limite de données tardives à appliquer. |
| Window Function | Complet | Expressions de fenêtre dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Ajoute des colonnes de fenêtre avec le partitionnement, l'ordre et le cadre du gem, en lignes ou en plage, avec des bornes non limitées, à la ligne courante ou décalées. |

### Join/Split

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Compare Columns | Complet | Jointure externe complète plus agrégats par colonne | Compare les colonnes par une jointure externe complète des données dépivotées, avec des décomptes de correspondances et de différences. |
| Join | Complet | [Jointure interne](/fr/reference/workflow-steps/tables/table-inner-join/), [Jointure multi-tables](/fr/reference/workflow-steps/tables/table-multi-table-join/), [Anti-jointure](/fr/reference/workflow-steps/tables/table-anti-join/) ou [Jointure croisée](/fr/reference/workflow-steps/tables/table-cross-join/) | Construit la jointure de chaque type (interne, gauche, droite, complète, semi, anti, croisée et naturelle) sur toute condition de jointure, applique la clause where et écrit la liste de sélection. |
| Repartition | Complet | Aucune étape nécessaire | Supprimé : PlaidCloud gère le partitionnement, de sorte que l'étape suivante lit directement la table en amont. |
| Row Distributor | Complet | Un filtre [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) par sortie | Est converti en un filtre par sortie ; des lignes peuvent atterrir dans plusieurs sorties. |

### Parse

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Column Parser | Complet | [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/) / [Analyse XML](/fr/reference/workflow-steps/tables/table-xml-parse/) | Est converti en une analyse JSON ou XML de la colonne nommée ; la conversion avertit que la disposition du gem est supposée. |

### Custom

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Complet | [User Defined Transform](/fr/reference/workflow-steps/general/user-defined-transform/) exécutant le code généré du gem | Le code PySpark généré du gem, issu de l'export du pipeline, s'exécute dans une étape Python, avec un avertissement invitant à le vérifier. |
| CustomReformatBitbucket | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Est converti comme le Reformat dont le gem porte les expressions, avec un avertissement invitant à le vérifier. |
| Data Quality Check | Complet | [Union All](/fr/reference/workflow-steps/tables/table-union-all/) d'une ligne de résultat par contrôle ; [Déclencher une erreur de workflow](/fr/reference/workflow-steps/workflow-control/raise-workflow-error/) pour s'arrêter en cas d'échec | Évalue chaque contrôle sur l'entrée et écrit une ligne de résultat par contrôle avec son statut et son message. Les données passent telles quelles, et l'exécution s'arrête lorsque le seuil d'échec du gem est atteint. |
| Deequ | Complet | Contrôles [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Transmet les données et construit la table des résultats de contraintes pour les règles isComplete, isUnique, isNonNegative et isContainedIn. |
| Delta Table Operations | Complet | [Table In-Place Delete](/fr/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/fr/reference/workflow-steps/tables/table-update/), [Table Drop](/fr/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/fr/reference/workflow-steps/tables/table-restore-timestamp/) | La suppression, la mise à jour, l'abandon et la restauration à un horodatage correspondent à des étapes de table ; optimize, vacuum et la restauration par version transmettent les données avec un avertissement. |
| Directory | Complet | [Liste du répertoire](/fr/reference/workflow-steps/document/directory-listing/) | Liste les fichiers du dossier de documents lié dans les colonnes du gem ; avec l'option de nom de feuille, chaque classeur produit une ligne par feuille. Un dossier manquant donne zéro ligne. |
| Email | Complet | [Notify Via Email](/fr/reference/workflow-steps/notifications/notify-via-email/) | Envoie l'e-mail, avec une pièce jointe de données facultative, via une connexion de messagerie liée. |
| Email Data | Complet | [Notify Via Email](/fr/reference/workflow-steps/notifications/notify-via-email/) | Envoie par e-mail les lignes d'entrée sous forme de table et transmet l'entrée sans modification. |
| File Operation | Complet | [Copy Document File](/fr/reference/workflow-steps/document/copy-document-file/) ou [Copy Document Directory](/fr/reference/workflow-steps/document/copy-document-directory/) | Copie, déplace ou synchronise des fichiers du dossier de documents lié vers le dossier de documents du workflow converti ; un déplacement supprime les fichiers sources. |
| Log | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Écrit la ligne d'événement du gem (heure, nom du gem, type d'événement et texte) dans sa table de sortie. |
| REST API Enrich | Complet | [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Appelle l'API une fois par ligne et ajoute les colonnes de la réponse. |
| Script | Complet | Étape Python avec réécriture de l'accès aux frames | Intègre le corps du script dans une étape python, avec l'accès aux data frames réécrit ; les corps Scala sont repris avec une remarque. |
| Soda Data Quality Check | Complet | Contrôles [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Construit la table des résultats de contrôle à partir des contrôles Soda. |
| SQL Statement | Complet | Étape SQL par onglet de sortie, texte traduit dans le dialecte du tenant | Intègre chaque onglet sous forme d'étape SQL avec les entrées liées comme tables temporaires ; traduit dans le dialecte du tenant. |
| Todo | Complet | [Déclencher une erreur de workflow](/fr/reference/workflow-steps/workflow-control/raise-workflow-error/) ou [Notify via Log](/fr/reference/workflow-steps/notifications/notify-via-log/) | Marque une logique encore à écrire : un message de journal lorsque rien ne la lit, ou une étape qui arrête l'exécution avec le message du gem lorsqu'une étape ultérieure en dépend. |

### Report

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Tableau | Complet | [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/) | Écrit une extraction Hyper et la publie vers la connexion Tableau liée. |

### ML/AI

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Bedrock | Complet | [Text NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) | Calcule les représentations vectorielles de la colonne de texte via la connexion IA de l'espace de travail. |
| OpenAI | Complet | [Text NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) | Répond à des questions ou calcule des représentations vectorielles de texte via la connexion IA de l'espace de travail. |
| Pinecone Lookup | Complet | [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Interroge l'index Pinecone pour chaque ligne et ajoute les colonnes pinecone_matches et pinecone_error. |
| SageMaker Endpoint | Complet | [Text NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) | Répond à des questions via la connexion IA de l'espace de travail. |
| Text Processing | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) pour le découpage en blocs ; [Requête REST](/fr/reference/workflow-steps/general/rest-request/) pour le web scraping | Le découpage en blocs devient une expression de blocs de caractères ; le web scraping récupère l'URL de chaque ligne et rattache le contenu de la page à la ligne. |

### Subgraph/Control

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Control Flow Input | Complet | Supprimé (simple marqueur de limite) | Supprimé ; il marque seulement la limite d'entrée du sous-workflow itérateur. |
| Control Flow Output | Complet | Supprimé (simple marqueur de limite) | Supprimé ; il marque seulement la limite de sortie du sous-workflow itérateur. |
| Subgraph (Basic) | Complet | Conteneur de canevas / workflow imbriqué à partir des processus en ligne | Convertit le graphe interne en ligne en un workflow imbriqué (ou en étapes intégrées) avec des paramètres de table en entrée et en sortie. |
| Table Iterator | Complet | [Workflow Loop](/fr/reference/workflow-steps/workflow-control/workflow-loop/) | Exécute le corps de la boucle une fois par ligne d'entrée, en définissant chaque valeur de configuration à partir de sa colonne, jusqu'à maxIteration. |
| While Iterator | Complet | [Workflow Loop](/fr/reference/workflow-steps/workflow-control/workflow-loop/) | Exécute le corps de la boucle une fois par passage, en transmettant le numéro d'itération, jusqu'à ce que le corps ne renvoie aucune ligne ou que le maximum du gem soit atteint. |

## Gems SQL / Analyst

### Source/Target

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Complet | Étape d'importation/exportation de données externes avec la connexion de base de données correspondante | Lit ou écrit une table dans une base de données externe via une connexion PlaidCloud. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Complet | Étapes d'importation/exportation de fichiers sur un compte de documents (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Lit ou écrit des fichiers dans un stockage cloud/SFTP avec union par caractères génériques, déclencheur, suppression/déplacement et options de chiffrement. |
| Model | Complet | Table de sortie de l'étape en amont | Lit un autre modèle comme la table produite par l'étape en amont référencée. |
| Seed | Complet | [Importation : CSV](/fr/reference/workflow-steps/import/import-csv/) | Le CSV de départ est importé dans une table PlaidCloud. |
| Source | Complet | Étape d'importation choisie selon le format du jeu de données (consultez [Connecteurs](#connecteurs)) | Chaque Source devient une étape d'importation dans une table nommée d'après le jeu de données ; un format que le convertisseur ne reconnaît pas est lu comme un fichier CSV téléversé dans le dossier de documents du workflow, avec un avertissement. |
| Target Model / Table (Target) | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/), [Upsert](/fr/reference/workflow-steps/tables/table-upsert/), [Copier la table](/fr/reference/workflow-steps/tables/table-copy/) et [Union All](/fr/reference/workflow-steps/tables/table-union-all/) | Écrit la sélection finale du modèle dans une table PlaidCloud en remplacement, ajout, upsert, suppression puis insertion, SCD2 ou remplacement par prédicat. |
| Upload Files | Complet | [Importation : CSV](/fr/reference/workflow-steps/import/import-csv/) | Les fichiers locaux téléversés deviennent une table via une étape d'importation. |

### Prepare

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Data Cleansing | Complet | Expressions de colonne dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Convertit les options de remplissage des valeurs nulles, de suppression des espaces et de casse en expressions de colonne ; les colonnes nettoyées passent en dernier. |
| Data Masking | Complet | Expressions de colonne pour le masquage de caractères ou le hachage | Masque ou hache les colonnes de chaîne sélectionnées sur place ou dans de nouvelles colonnes. |
| Find Duplicates | Complet | Expression de fenêtre de numéro de ligne plus filtre | Renvoie les lignes uniques, en double ou sélectionnées par nombre/position, par clé. |
| Generate Rows | Complet | Table de séquence jointe et filtrée par ligne d'entrée | Génère des lignes pour chaque ligne d'entrée à partir des expressions d'initialisation, de condition et de boucle. |
| Imputation | Complet | Agrégat plus jointure de retour et expression de colonne | Remplace les valeurs nulles ou sentinelles par la moyenne, la médiane, le mode ou une valeur fixe. |
| Multi-Column Edit | Complet | Expressions par colonne développées à partir du modèle | Applique un même modèle d'expression à chaque colonne sélectionnée. |
| Multi-Column Rename | Complet | Correspondance de renommage de colonnes sur une étape de sélection | Renomme les colonnes sélectionnées par préfixe, suffixe ou expression de nom. |
| Record ID | Complet | Expression de colonne de numéro de ligne ou d'uuid | Ajoute une colonne d'identifiant d'enregistrement UUID ou séquentiel. |
| Sample | Complet | Limite de lignes ou option d'échantillon sur l'extraction | Prend les premières, dernières, aléatoires, une sur N ou un pourcentage de lignes, globalement ou par groupe. |
| Tile | Complet | Expressions de fenêtre pour le numéro de tuile et la séquence | Attribue des numéros de tuile par somme égale, nombre, bandes d'écart type, valeurs distinctes ou seuils manuels. |

### Transform

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Aggregate | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec agrégation ; [Pivot](/fr/reference/workflow-steps/tables/table-pivot/) lorsque le gem pivote | Regroupe et agrège, applique la condition HAVING et pivote en une colonne par valeur de pivot ; propagate-all conserve toutes les autres colonnes d'entrée. |
| Count Records | Complet | Étape d'agrégation avec fonctions de comptage | Renvoie le nombre total, non nul ou distinct sous forme d'une seule ligne. |
| Data Encoder/Decoder | Complet | Expressions de colonne pour l'encodage et le décodage base64/hex | Encode ou décode les colonnes sélectionnées ; AES uniquement sur Databricks. |
| Deduplicate | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec distinct ou un filtre sur le numéro de ligne | Conserve une ligne par clé : distincte, première ou dernière selon votre ordre de tri, quelconque, ou uniquement les clés qui n'apparaissent qu'une fois. |
| Dynamic Select | Complet | Sélection de colonnes dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) résolue par type | Résout les colonnes par type au moment de la conversion en une sélection explicite. |
| Filter | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une expression de filtre | Est converti en une étape Table Extract avec une expression de filtre ; les conditions NULL éliminent la ligne. |
| Finance | Complet | Expression de colonne implémentant la fonction financière | Ajoute le résultat d'une fonction financière (FV, PV, NPV, IRR, ...) dans une nouvelle colonne. |
| Flatten Schema | Complet | [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/) et [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Aplatit les champs imbriqués en colonnes nommées avec le délimiteur du gem et déploie les tableaux en une ligne par élément. |
| Fuzzy Match | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) et [User Defined Transform](/fr/reference/workflow-steps/general/user-defined-transform/) | Apparie les enregistrements, note chaque champ de correspondance selon la méthode du gem, fait la moyenne des notes et conserve les paires égales ou supérieures à votre seuil. |
| Limit | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une limite de lignes | Est converti en une limite de lignes ; les références de configuration deviennent des variables de projet. |
| Order By | Complet | Tri sur une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Est converti en un tri avec les mêmes clés, le même sens et le même placement des valeurs nulles. |
| Pivot | Complet | [Pivot](/fr/reference/workflow-steps/tables/table-pivot/) | Transforme les valeurs de pivot sélectionnées en colonnes d'agrégats ; une liste de valeurs en mode Simple récupérée à la conception est convertie comme les valeurs listées. |
| Reformat | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec expressions de colonne | Est converti en une étape Table Extract avec une expression par colonne de sortie ; les colonnes non listées sont supprimées. |
| Running Total | Complet | Colonne d'expression de fenêtre à somme cumulée | Ajoute des sommes cumulées pour chaque colonne sélectionnée. |
| Snowflake Unpivot (third-party) | Complet | [Melt](/fr/reference/workflow-steps/tables/table-melt/) | Dépivote des colonnes via Snowflake UNPIVOT. |
| Transpose | Complet | [Melt](/fr/reference/workflow-steps/tables/table-melt/) | Empile les colonnes de données en colonnes de noms et de valeurs de type chaîne. |
| TransposeAgg | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec agrégation | Convertit le regroupement, les agrégats et le pivot du gem sous forme d'Aggregate, avec un avertissement invitant à le vérifier. |
| Unpivot | Complet | [Melt](/fr/reference/workflow-steps/tables/table-melt/) | Empile les colonnes de données en colonnes de noms et de valeurs. |
| Weighted Average | Complet | Étape d'agrégation avec expression de moyenne pondérée | Calcule une moyenne pondérée globale ou par groupe. |
| Window Function | Complet | Expressions de fenêtre dans une étape [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Ajoute des colonnes de fenêtre avec le partitionnement, l'ordre et le cadre du gem, en lignes ou en plage, avec des bornes non limitées, à la ligne courante ou décalées. |

### Join/Split

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Except | Complet | [Anti-jointure](/fr/reference/workflow-steps/tables/table-anti-join/) sur toutes les colonnes plus un [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) distinct | Conserve les lignes de la première entrée qui n'apparaissent dans aucune des autres entrées. |
| Intersect | Complet | [Jointure interne](/fr/reference/workflow-steps/tables/table-inner-join/) sur toutes les colonnes plus Distinct | Conserve les lignes présentes dans toutes les entrées. |
| Join | Complet | [Jointure interne](/fr/reference/workflow-steps/tables/table-inner-join/), [Jointure multi-tables](/fr/reference/workflow-steps/tables/table-multi-table-join/), [Anti-jointure](/fr/reference/workflow-steps/tables/table-anti-join/) ou [Jointure croisée](/fr/reference/workflow-steps/tables/table-cross-join/) | Construit la jointure de chaque type (interne, gauche, droite, complète, semi, anti, croisée et naturelle) sur toute condition de jointure, applique la clause where et écrit la liste de sélection. |
| Union | Complet | [Union All](/fr/reference/workflow-steps/tables/table-union-all/) | Empile les entrées par position, en supprimant les doublons lorsque le gem ne les conserve pas. |
| Union By Name | Complet | [Union All](/fr/reference/workflow-steps/tables/table-union-all/) | Devient un Union All qui aligne les colonnes par nom et remplit de NULL celles qui manquent. |

### Parse

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| JSON Parse | Complet | [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/) | Analyse une colonne de texte JSON en champs structurés. |
| Regex | Complet | Expressions regex dans une étape Table Extract / Transform | Remplace, analyse, fait correspondre ou découpe en jetons une colonne de texte avec une regex. |
| Text To Columns | Complet | Étapes de scission de colonne / d'éclatement avec délimiteur regex | Scinde une colonne délimitée en colonnes ou en lignes à l'aide d'un délimiteur regex. |
| XML Parse | Complet | [Analyse XML](/fr/reference/workflow-steps/tables/table-xml-parse/) | Analyse une colonne de texte XML en champs structurés. |

### Custom

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Directory | Complet | [Liste du répertoire](/fr/reference/workflow-steps/document/directory-listing/) | Liste les fichiers du dossier de documents lié dans les colonnes du gem ; avec l'option de nom de feuille, chaque classeur produit une ligne par feuille. Un dossier manquant donne zéro ligne. |
| DynamicInput | Complet | Étape SQL pour les modèles de requête ; boucle de workflow pour le mode multifichier | Le mode modèle de requête intègre le modèle sous forme d'étape SQL ; le mode multifichier est converti avec des hypothèses. |
| Email | Complet | [Notify Via Email](/fr/reference/workflow-steps/notifications/notify-via-email/) | Envoie l'e-mail, avec une pièce jointe de données facultative, via une connexion de messagerie liée. |
| RestAPI | Complet | [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Envoie une requête par ligne d'entrée avec votre URL, vos en-têtes, votre requête, votre corps et vos nouvelles tentatives, conserve la réponse et interroge une requête asynchrone jusqu'à son achèvement. Les identifiants proviennent de la connexion que vous liez. |
| Script | Complet | Étape Python avec réécriture de l'accès aux frames | Intègre le corps du script dans une étape python, avec l'accès aux data frames réécrit ; les corps Scala sont repris avec une remarque. |
| SQL Statement | Complet | Étape SQL par onglet de sortie, texte traduit dans le dialecte du tenant | Intègre chaque onglet sous forme d'étape SQL avec les entrées liées comme tables temporaires ; traduit dans le dialecte du tenant. |
| StoredProcedure | Complet | [Agent Remote Execution of SQL](/fr/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Appelle la procédure sur son entrepôt via la connexion que vous choisissez : une fois par ligne d'entrée avec chaque argument lié depuis sa colonne, ou une seule fois si elle ne prend aucun argument. Les colonnes d'entrée sont transmises. |
| Table Operations | Complet | [Table In-Place Delete](/fr/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/fr/reference/workflow-steps/tables/table-update/), [Table Drop](/fr/reference/workflow-steps/tables/table-drop/) | La mise à jour, la suppression et l'abandon correspondent à des étapes de table ; vacuum et optimize deviennent une optimisation de table ou une opération vide avec un avertissement. |
| ToDo | Complet | [Déclencher une erreur de workflow](/fr/reference/workflow-steps/workflow-control/raise-workflow-error/) ou [Notify via Log](/fr/reference/workflow-steps/notifications/notify-via-log/) | Marque une logique encore à écrire : un message de journal lorsque rien ne la lit, ou une étape qui arrête l'exécution avec le message du gem lorsqu'une étape ultérieure en dépend. |

### Spatial

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Buffer | Complet | [Spatial Buffer](/fr/reference/workflow-steps/spatial/spatial-buffer/) | Agrandit chaque géométrie de la distance configurée en miles ou en kilomètres. |
| CreatePoint | Complet | [Table Extract](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) avec `geom_point` | Construit une géométrie de point à partir de colonnes de longitude et de latitude. |
| Distance | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Calcule la distance, la direction cardinale et le relèvement entre deux points WKT. |
| FindNearest | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) avec une jointure croisée | Trouve les N points cibles les plus proches de chaque point source dans une distance maximale. |
| HeatMap | Complet | [Heat Map (macro)](/fr/reference/workflow-steps/macros/macro-heat-map/) | Répartit les points dans des hexagones H3 à la résolution du gem, diffuse la chaleur sur la distance de grille avec son atténuation, et fournit la densité et le contour de chaque hexagone. |
| PolyBuild | Complet | [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) et une étape Python | Construit du WKT de polygone ou de polyligne à partir de points ordonnés par groupe. |
| Simplify | Complet | [Spatial Generalize](/fr/reference/workflow-steps/spatial/spatial-generalize/) | Simplifie des géométries WKT avec une tolérance en miles/km. |
| SpatialMatch | Complet | [Correspondance spatiale](/fr/reference/workflow-steps/spatial/spatial-match/) | Fait correspondre des géométries source et cible par intersection/contenance/inclusion/contact/enveloppe. |

### Report

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| PowerBIWrite | Complet | [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Crée le jeu de données Power BI et y envoie les lignes via l'API REST de Power BI. |
| TableauWrite | Complet | [Publish to Tableau](/fr/reference/workflow-steps/export/export-to-tableau/) | Écrit une extraction Hyper et la publie vers la connexion Tableau liée. |
| Visualize | Complet | [Copier la table](/fr/reference/workflow-steps/tables/table-copy/) | Transmet les lignes sans modification ; construisez le graphique sous forme de tableau de bord PlaidCloud sur la même table. |

### Subgraph/Control

| Gem | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Condition | Complet | [Jointure croisée](/fr/reference/workflow-steps/tables/table-cross-join/) et [Table Extract](/fr/reference/workflow-steps/tables/table-extract/) | Évalue les conditions sur toute l'entrée et envoie chaque ligne vers la première sortie dont la condition est remplie, sinon vers la dernière sortie. |
| Macro | Complet | Étape SQL avec le corps de la macro développé | Intègre le corps de la macro sous forme d'étape SQL traduite dans le dialecte du tenant, avec les entrées liées comme tables temporaires. |
| Pipeline (trigger) | Complet | [Workflow Loop](/fr/reference/workflow-steps/workflow-control/workflow-loop/) | Exécute le pipeline nommé une fois par ligne d'entrée avec vos paramètres et votre condition de déclenchement, continue après une exécution en échec et renvoie une ligne par exécution. |
| Subgraph (Basic) | Complet | Conteneur de canevas / workflow imbriqué à partir des processus en ligne | Convertit le graphe interne en ligne en un workflow imbriqué (ou en étapes intégrées) avec des paramètres de table en entrée et en sortie. |

## Connecteurs

Les formats de jeu de données et les connecteurs sont des paramètres de source et de cible d'un gem, et non des gems. Chaque format est converti en l'étape d'importation ou d'exportation indiquée, et la conversion ne contacte jamais le système source ou cible.

| Format | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Avro | Complet | [Importation : Avro](/fr/reference/workflow-steps/import/import-avro/) ; [Exportation : Avro](/fr/reference/workflow-steps/export/export-to-avro/) | Lit et écrit des fichiers Avro. |
| BigQuery | Complet | Connexion à une base de données externe avec importation de table | Lit et écrit via une connexion. |
| Binary files | Complet | [Liste du répertoire](/fr/reference/workflow-steps/document/directory-listing/) avec contenu des fichiers ; [Exécuteur Alteryx](/fr/reference/workflow-steps/general/alteryx-executor/) pour écrire | Lit chaque fichier du dossier avec son chemin, son heure de modification, sa longueur et son contenu ; écrit le contenu de chaque ligne dans le fichier que nomme son chemin. |
| Catalog table | Complet | Liaison à une table PlaidCloud existante | Se lie à une table par son nom ; la lecture et tous les modes d'écriture sont convertis. |
| Cosmos DB | Complet | Importation et exportation : [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Lit et écrit les documents du conteneur via votre connexion Cosmos DB. |
| CSV | Complet | [Importation : CSV](/fr/reference/workflow-steps/import/import-csv/) ; Exportation : CSV | Lit et écrit des fichiers délimités avec les options d'en-tête, de séparateur, de guillemets, d'échappement et d'encodage. |
| Data Generator | Complet | [Table Faker](/fr/reference/workflow-steps/tables/table-faker/) | Génère les colonnes du jeu de données avec les mêmes types de fausses données. |
| DataHub table | Complet | [Importer depuis SQL](/fr/reference/workflow-steps/import/import-sql/) | Lit la table que nomme le jeu de données via votre connexion ; une écriture aboutit dans une table PlaidCloud. |
| Delta | Complet | Liaison à une table PlaidCloud existante | Lit et écrit la table dans tous les modes d'écriture ; la lecture d'une version antérieure passe par la connexion Databricks que vous liez. |
| Excel (XLSX) | Complet | Importation : Excel ; Exportation : Excel | Lit et écrit des feuilles et des plages de classeur. |
| Fixed format | Complet | Importation : [largeur fixe](/fr/reference/workflow-steps/import/import-fixed-width/) ; Exportation : [CSV](/fr/reference/workflow-steps/export/export-to-csv/) | Lit des fichiers à largeur fixe disposés d'après les largeurs de colonne du jeu de données ; écrit un fichier délimité. |
| Hive | Complet | Importation : [Importer depuis SQL](/fr/reference/workflow-steps/import/import-sql/) ; Exportation : [tables externes](/fr/reference/workflow-steps/export/export-external-tables/) | Lit et écrit la table via votre connexion Hive. |
| Iceberg | Complet | Liaison à une table PlaidCloud existante | Lit et écrit la table. |
| JDBC | Complet | Connexion à une base de données externe avec importation de table | Lit une table ou une requête et écrit en mode remplacement ou ajout via votre connexion ; une instruction postérieure à l'écriture s'exécute après l'écriture. |
| JSON | Complet | [Analyse JSON](/fr/reference/workflow-steps/tables/table-json-parse/) | Charge les enregistrements et aplatit les champs imbriqués. |
| Kafka | Complet | Importation : [Importer depuis Kafka](/fr/reference/workflow-steps/import/import-kafka/) ; Exportation : [Exporter vers Kafka](/fr/reference/workflow-steps/export/export-kafka/) | Lit un topic comme un lot de messages et écrit les lignes sous forme de messages. |
| MongoDB | Complet | Import : [MongoDB](/fr/reference/workflow-steps/import/import-mongodb/) ; Export : [MongoDB](/fr/reference/workflow-steps/export/export-mongodb/) | Lit et écrit la collection via votre connexion MongoDB. |
| ORC | Complet | Import : [ORC](/fr/reference/workflow-steps/import/import-orc/) ; Export : ORC | Lit et écrit des fichiers ORC. |
| Parquet | Complet | Importation : Parquet ; Exportation : Parquet | Lit et écrit des fichiers Parquet. |
| Pinecone | Complet | Importation et exportation : [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Lit les enregistrements d'un index et effectue l'upsert des lignes sous forme de vecteurs via l'API REST de Pinecone. |
| Redshift | Complet | Connexion à une base de données externe avec importation de table | Lit et écrit via une connexion. |
| Salesforce | Complet | Importation : [Salesforce : interroger un objet](/fr/reference/workflow-steps/salesforce/query-salesforce-object/) ; Exportation : [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Lit un objet ou une requête SOQL et écrit des enregistrements via votre connexion Salesforce. |
| Seed (inline) | Complet | [Importation : CSV](/fr/reference/workflow-steps/import/import-csv/) | Charge les lignes en ligne sous forme de table. |
| Slack | Complet | Importation : [Singer](/fr/reference/workflow-steps/import/import-singer/) ; Exportation : [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Lit les messages d'un canal et publie chaque ligne sous forme de message via votre connexion Slack. |
| Smartsheet | Complet | Importation et exportation : [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Lit et écrit les lignes de la feuille via votre connexion Smartsheet. |
| Snowflake | Complet | Connexion à une base de données externe avec importation de table | Lit et écrit via une connexion. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Complet | Étapes d'importation et d'exportation de fichiers sur un compte de documents | Lit et écrit le type de fichier ; les options sans équivalent PlaidCloud sont signalées. |
| Text | Complet | [Importation : CSV](/fr/reference/workflow-steps/import/import-csv/) en une seule colonne | Lit chaque ligne comme une colonne. |
| Web page | Complet | [Requête REST](/fr/reference/workflow-steps/general/rest-request/) | Lit la page située à l'URL du jeu de données dans une table. |
| XML | Complet | [Analyse XML](/fr/reference/workflow-steps/tables/table-xml-parse/) | Charge les enregistrements selon la balise de ligne. |

## Expressions et structure du projet

| Domaine | Statut | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Expressions | Complet | Expressions SQL Spark et d'entrepôt traduites fonction par fonction | Les fonctions et les opérateurs sont convertis en expressions PlaidCloud ; une fonction sans équivalent est signalée par son nom. |
| Project and graph structure | Complet | Chargeur de projet | Chaque forme d'export Prophecy est chargée et normalisée dans un modèle unique. |

## Cas limites connus

| Cas | Ce qui se passe |
| --- | --- |
| Code ou données absents de l'export | Un Gem Builder ou un autre gem personnalisé dont le code ne figure pas dans l'export, ainsi qu'un appel à une macro d'un package dbt que l'export omet, deviennent une étape qui nomme ce qui manque ; exportez le projet avec le code de son pipeline et ses packages dbt, ou reconstruisez la logique dans une étape Python ou SQL. Les gems Ab Initio Error Detection et MTime transmettent leur entrée, car la règle qu'ils appliquent ne figure pas dans l'export. Les contrôles Soda lus depuis un fichier extérieur au projet, ainsi que ceux qui comparent avec des analyses précédentes ou avec un autre jeu de données, ou qui testent un format que nomme Soda, n'ont pas de ligne dans la table des résultats ; calculez-les dans une étape ultérieure. |
| Résultats connus uniquement à l'exécution du pipeline | Un gem REST API qui aplatit sa réponse place toute la réponse dans une seule colonne lorsque rien ne déclare les noms de champs, ce que seule une exécution révèle ; extrayez les champs dont vous avez besoin dans une étape ultérieure. Une macro dbt qui interroge l'entrepôt pendant la compilation dbt devient une étape qui la nomme ; remplacez la requête par les valeurs qu'elle renvoie. Un gem Spark StoredProcedure s'exécute, mais ses valeurs OUT ne sont pas renvoyées ; la sortie correspond aux colonnes transmises. `input_file_name()` renvoie une chaîne vide sur une source de table ou Delta, qui n'a aucun fichier à nommer, et `hash()` / `xxhash64()` dans un agrégat, une fenêtre ou un gem à plusieurs entrées sont calculés par l'entrepôt, ils peuvent donc différer de ceux de Spark. |
| Valeurs écrites dans une étape lors de la conversion du projet | Une valeur de paramètre contenant un guillemet, une barre oblique inverse ou une accolade, une valeur de pipeline qu'une étape SQL lit, et la base de données qu'une opération de table Delta nomme par la configuration sont écrites dans l'étape comme valeurs fixes ; modifier la variable du workflow ne les change donc pas ; modifiez l'étape lorsque la configuration change. |
| Code Scala | Un script Scala, une expression Scala, ou une fonction définie par l'utilisateur ou une fonction d'agrégation Scala devient une étape qui la nomme ; réécrivez-la en SQL ou en Python. |
| Connexion Kerberos de Kafka | Une source ou une cible Kafka qui se connecte avec Kerberos (GSSAPI) est convertie sans le nom de service Kerberos ni le mécanisme de connexion ; définissez-les sur la connexion PlaidCloud. |
| Streaming | Les sources, cibles et pipelines de streaming s'exécutent sous forme de workflows par lots sur les données présentes au moment de leur exécution ; planifiez le workflow pour qu'il s'exécute aussi souvent que nécessaire. |
| Composants de job | Un job Spark est converti avec son unique pipeline et sa planification ; ses autres composants, ses conditions d'exécution et ses surcharges de configuration ne sont pas convertis. |
| Appels peu courants | Une fonction d'agrégation définie par l'utilisateur appelée depuis un rollup ou une fenêtre, et une macro dbt qui utilise Jinja au-delà de if, for, set et des filtres courants, deviennent une étape qui nomme le gem ; appelez la fonction depuis un gem Aggregate, ou intégrez la macro en ligne. |

## Valider un workflow converti

Comparez la sortie du workflow converti avec celle de votre propre pipeline Prophecy : schéma, nombre de lignes et valeurs des lignes. Ignorez l'ordre des lignes, sauf si le workflow en dépend.
