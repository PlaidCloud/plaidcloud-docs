---
title: Matrice de conversion Alteryx
description: Comment PlaidCloud convertit les outils Alteryx en étapes de workflow avancé natives, macros, variables et exécuteurs gérés, avec l'état de prise en charge de chaque outil.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloud convertit les workflows, applications et macros Alteryx en workflows
avancés natifs. L'importeur fait correspondre chaque outil Alteryx à une étape de workflow,
une construction de macro, une variable contrôlée, une opération sur fichier adossée aux documents ou un exécuteur
de tâche géré, de sorte qu'un workflow converti s'exécute en mode natif cloud, et non en émulation.

**Presque tous les outils Alteryx standard se convertissent intégralement.** L'état de prise en charge ci-dessous
est indiqué par outil :

- **Complet** : l'outil est converti en étape, macro, variable, artefact ou
  exécuteur géré PlaidCloud natif et exécute sa fonction. La plupart des outils sont dans ce cas.
- **Partiel** : l'outil est converti et s'exécute pour son usage courant, mais un
  *mode de fonctionnement* distinct de l'outil n'est pas encore reproduit. Cas rare.
- **Non pris en charge** : aucune conversion ; la fonctionnalité est reconstruite en mode natif.

Les connecteurs de systèmes externes (Salesforce, HTTP, Google Analytics, Cassandra,
e-mail, Hadoop, Spark, etc.) sont **connectés, et non convertis** ; voir
[Connexion aux systèmes externes](#connexion-aux-systèmes-externes).

## Prise en charge des outils

| Outil Alteryx | État | Équivalent PlaidCloud | Conversion |
| --- | --- | --- | --- |
| Action | Complet | Liaison de variable et configuration conditionnelle d'étape | Met à jour les paramètres des étapes en aval à partir des entrées de l'application convertie. |
| Analytic App interface (`.yxwz`) | Partiel | Interface « App Runner » Panel publiée | La disposition `<Questions>` de l'application est matérialisée en une application Panel opérationnelle qui collecte les saisies de l'utilisateur et pilote le workflow converti ; elle est publiée automatiquement lors de la conversion (une application sans widget de saisie est ignorée). Les types de questions courants (texte, numérique (Numeric Up Down), date, case à cocher, bouton radio, liste déroulante, zone de liste, arborescence, sélection de fichier et sélection de dossier) deviennent des widgets App Runner. Une question dont la valeur n'est liée à aucune variable de workflow est affichée avec une remarque visible, au lieu de collecter silencieusement une valeur inutile, et les types de questions moins courants sont signalés pour revue plutôt que matérialisés. Voir [Utiliser des applications Alteryx converties](/fr/guides/workflows/use-converted-alteryx-apps/#linterface-app-runner). |
| Append Fields | Complet | Transformation d'ajout de champs | Ajoute les champs d'un flux à un autre. |
| Auto Field | Complet | Transformation de dimensionnement automatique des champs | Conserve le dimensionnement déduit des champs. |
| AutoML | Complet | [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) | Fusionne les choix de méthode de modélisation, de cible et d'algorithmes candidats dans une étape ML Train, comme pour Classification et Regression. AutoML n'enregistre jamais quel algorithme candidat l'a emporté lors de l'exécution dans Alteryx ; la conversion retient donc le premier algorithme coché pris en charge par ML Train et signale ce choix. Comparez une étape AutoML convertie à vos propres résultats Alteryx. |
| Barcode | Complet | Exécuteur de codes-barres | Lit ou écrit des codes-barres dans la symbologie configurée. |
| Batch Macro | Partiel | Macro déployée sur sa table d'ancrage de contrôle | L'appelant exécute la macro entière une fois par enregistrement de son entrée de contrôle, en liant à chaque passage les paramètres de contrôle de l'intérieur de la macro. Cela inclut un paramètre de contrôle que l'appelant a renommé en libellé d'affichage lorsqu'un seul est en jeu, ainsi qu'une action `UpdateRawXml` qui réécrit la liste de champs d'un Select à partir d'une variable. Les cas dont la valeur par passage ne peut pas être reproduite de façon sûre échouent par défaut, avec leur nom, plutôt que d'être convertis à tort : un `UpdateRawXml` qui réécrit autre chose que la liste de champs d'un Select, et une action qui remplace par une variable l'intégralité de l'expression d'un Filter (sa syntaxe brute par passage serait mal évaluée). |
| Browse | Complet | Browse / passage direct | Conservé pour inspection, sans coût à l'exécution. |
| Buffer | Complet | [Spatial Buffer](/fr/reference/workflow-steps/spatial/spatial-buffer/) | Agrandit chaque géométrie d'une distance fixe. |
| Build Features | Partiel | [Build Features](/fr/reference/workflow-steps/tables/table-build-features/) | Convertit les primitives arithmétiques et d'interaction, l'extraction de parties de date, le regroupement par seuils explicites, la normalisation (z-score et min-max) et l'encodage one-hot. L'agrégation entre tables (Deep Feature Synthesis via l'onglet Manage Relationships), l'ACP, l'encodage cible et le regroupement automatique piloté par les données n'ont pas d'équivalent ; chacun est signalé par son nom dans le rapport de conversion plutôt qu'abandonné silencieusement. |
| Calgary Cross Count | Complet | Agrégat de [base de données Calgary](/fr/guides/workflows/migrate-alteryx-workflows/#bases-de-données-calgary) | Regroupe les champs indexés et compte les valeurs nommées de chaque champ personnalisé. |
| Calgary Cross Count Append | Complet | [Calgary Cross Count Append](/fr/guides/workflows/migrate-alteryx-workflows/#calgary-join-et-cross-count-append) | Fait correspondre chaque enregistrement en entrée à un index de valeurs, puis compte le nombre d'enregistrements de la base qui correspondent. |
| Calgary Input | Complet | Entrée de [base de données Calgary](/fr/guides/workflows/migrate-alteryx-workflows/#bases-de-données-calgary) | Lit la base de données en appliquant sa requête enregistrée comme filtre. |
| Calgary Join | Complet | [Calgary Join](/fr/guides/workflows/migrate-alteryx-workflows/#calgary-join-et-cross-count-append) | Fait correspondre chaque enregistrement à un index de valeurs de la base de données et conserve les enregistrements correspondants. |
| Calgary Loader | Complet | Écriture de [base de données Calgary](/fr/guides/workflows/migrate-alteryx-workflows/#bases-de-données-calgary) | Écrit la table de substitution à laquelle se lie chaque lecteur Calgary. |
| Centroid | Complet | Opération d'exécuteur Centroid | Réduit chaque géométrie à son point central, ajouté dans une colonne `Centroid`. |
| Check Box | Complet | Variable de workflow contrôlée | Convertit les choix par case à cocher de l'application en entrée contrôlée. |
| Classification | Complet | [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) | Fusionne la chaîne de modélisation assistée en une seule étape ML Train avec son algorithme, sa cible, ses caractéristiques et ses hyperparamètres. |
| Comment / Annotation / Link | Complet | Annotation du canevas | Conservé comme contexte du workflow. |
| Condition | Complet | Condition d'étape | Déclenche des avertissements, des erreurs ou des branches à partir d'une expression. |
| Control Parameter | Complet | Paramètre de contrôle de macro | Correspond aux paramètres de macro PlaidCloud. |
| Convex Hull | Complet | Opération d'exécuteur Convex Hull | Construit le plus petit polygone convexe englobant chaque géométrie, ajouté dans une colonne `ConvexHull`. |
| Create Points | Complet | [Table Extract](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) avec `geom_point` | Construit une géométrie de points à partir des colonnes de longitude et de latitude, en SQL. |
| Create Samples | Complet | Table Extract, un par sortie | Répartit l'entrée en Estimation, Validation et Holdout selon les pourcentages configurés. |
| Cross Tab | Complet | Transformation de tableau croisé / pivot | Pivote les lignes en colonnes pour toutes les méthodes d'agrégation et les totaux dérivés. |
| Data Cleansing | Complet | Transformation de nettoyage des données | Nettoie les espaces, les valeurs nulles, la ponctuation et la casse. |
| Date | Complet | Variable de workflow (date) | Émet des valeurs de date ISO pour les étapes et les conditions. |
| DateTime | Complet | Transformation de date/heure | Convertit l'analyse et la mise en forme des dates et des heures. |
| Detour | Complet | Routage de branche conditionnel | Convertit la sélection de route en conditions de DAG. |
| Detour End | Complet | Fusion de branches conditionnelles | Rejoint les branches sélectionnées de manière conditionnelle. |
| Directory | Complet | Liste de répertoire de documents | Liste les fichiers d'un chemin de documents. |
| Distance | Complet | [Table Extract](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) avec `ST_DISTANCE_SPHERE` | Distance géodésique et relèvement de point à point, en SQL. |
| Download | Complet | Étape [Requête REST](/fr/reference/workflow-steps/general/rest-request/) sur une connexion REST | Télécharge des données ou des artefacts externes ; affectez une connexion REST à l'étape convertie avant son exécution. |
| Drop Down | Complet | Variable de workflow contrôlée | Convertit les choix par liste déroulante de l'application en entrée contrôlée. |
| Dynamic Input | Partiel | Entrée de documents dynamique | Résout les motifs de fichiers et les entrées pilotées par variable à l'exécution. Une *ReadList* Excel (une feuille lue dans chaque classeur listé par un outil Directory, puis réunie par union) est convertie en lecture de feuille par glob de dossier lorsqu'un Filter en amont limite la feuille à un seul nom par correspondance exacte. Une feuille choisie par un filtre Contains, une inégalité ou un OR, ou une lecture portant sur plus d'une feuille, est refusée plutôt que de lire la mauvaise feuille. |
| Dynamic Rename | Complet | Transformation de renommage dynamique | Renomme les champs à partir de métadonnées ou de règles. |
| Dynamic Replace | Complet | Transformation de remplacement dynamique | Applique des règles de remplacement issues d'un second flux. |
| Dynamic Select | Complet | Transformation de sélection dynamique de champs | Sélectionne les champs par type, nom ou règle. |
| Error | Complet | Condition d'étape (erreur) | Convertit le comportement d'erreur configuré en conditions d'étape. |
| Feature Types | Complet | Configuration des caractéristiques de [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) | Reporte le rôle de modèle affecté à chaque champ dans l'étape ML Train fusionnée. |
| File Browse | Complet | Variable de fichier de documents contrôlée | Permet aux utilisateurs de choisir un fichier pour l'exécution d'une application convertie. |
| Filter | Complet | Transformation de filtre | Répartit les enregistrements par expression entre un chemin vrai et un chemin faux. |
| Fit | Complet | [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) | Absorbé dans l'étape ML Train fusionnée. |
| Folder Browse | Complet | Variable de dossier de documents contrôlée | Permet aux utilisateurs de choisir un dossier pour l'exécution d'une application convertie. |
| Formatted Excel output into a styled template | Partiel | Écriture Excel basée sur un modèle (étape [Export to Excel Sheets](/fr/reference/workflow-steps/export/export-to-excel-sheets/) pour plusieurs feuilles) | L'écriture dans un modèle mis en forme préserve la mise en forme du modèle : valeurs, formats numériques, polices, remplissages, bordures, cellules fusionnées et largeurs de colonnes sont reportés dans la feuille et la plage nommées. Cela couvre une feuille unique comme plusieurs sorties assemblées dans différentes feuilles d'un même classeur, remplies en un seul passage afin que les feuilles ne s'écrasent plus mutuellement. Un cas reste partiel : un modèle qui contient des tableaux croisés dynamiques ou des graphiques perd ces objets lors de l'écriture de ses feuilles. La sortie Excel simple (sans mise en forme) est Complète ; voir Output Data. |
| Formula | Complet | Transformation de formule | Convertit les expressions de champs en expressions ou en SQL PlaidCloud. |
| Fuzzy Match | Complet | Exécuteur de correspondance approximative | Fait correspondre selon des clés, des seuils et une revue des candidats. |
| Generalize | Complet | [Spatial Generalize](/fr/reference/workflow-steps/spatial/spatial-generalize/) | Simplifie la géométrie selon une tolérance, en préservant la topologie. |
| HTML | Complet | Texte de rapport / artefact HTML | Conserve le contenu comme sortie de rapport ou d'artefact. |
| Image Processing | Complet | Exécuteur de transformation d'image | Applique niveaux de gris, mise à l'échelle, recadrage et rotation dans l'ordre du canevas. |
| Image Profile | Complet | Exécuteur de profil d'image | Rapporte les dimensions, le mode, le format, les canaux et les statistiques de luminance. |
| Image to Text | Complet | Exécuteur OCR | Extrait le texte des images via un OCR géré. |
| Input Data | Complet | Entrée de fichier adossée aux documents | Charge les fichiers source `.yxdb`, `.dbf`, Excel et `.flat` à largeur fixe dans les données du workflow. |
| Insights | Complet | Tableau de bord / sortie d'artefact | Crée un artefact de revue natif cloud. |
| Interactive Chart | Complet | Artefact de graphique | Crée un artefact de graphique à partir des données converties. |
| Join | Complet | Transformation de jointure | Produit les flux joint, gauche seul et droit seul sur une clé à un ou plusieurs champs, ou par position. |
| Join Multiple | Complet | Transformation de jointure multiple | Joint plusieurs flux d'entrée. |
| Key/Value Pairs | Complet | [Text: NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) (tâche keyvalue) | Extrait des paires clé/valeur d'une colonne de texte via l'étape NLP AI reposant sur un LLM, avec clés candidates facultatives et correspondance approximative ou exacte. |
| Line To Polygon | Complet | Opération d'exécuteur Line To Polygon | Ferme chaque ligne en un anneau de polygone, ajouté dans une colonne `Polygon`. |
| List Box | Complet | Variable de workflow contrôlée | Convertit les sélections de liste de l'application en entrée contrôlée. |
| Location Optimizer | Partiel | [Optimiseur de localisation](/fr/reference/workflow-steps/optimization/location-optimizer/) | Convertit le cas linéaire de minimisation des distances (choisir K sites pour minimiser la distance totale ou pondérée jusqu'à la demande) en étape MIP p-médiane native. Un score à noyau gravitationnel, une macro de scoring sur mesure ou tout autre objectif de recherche de candidats est toujours refusé ; voir [Migrer des workflows Alteryx](/fr/guides/workflows/migrate-alteryx-workflows/#macros-dans-un-workflow-converti). |
| Macro calls | Complet | Appel de macro | Importe les sources de macros connues et fait correspondre les appels de macro aux étapes de macro PlaidCloud. |
| Macro Input / Macro Output | Complet | Port d'entrée / de sortie de macro | Correspondent directement aux ports de macro PlaidCloud. |
| Make Grid | Complet | [Spatial Make Grid](/fr/reference/workflow-steps/spatial/spatial-make-grid/) | Découpe une étendue en cellules carrées, une ligne par cellule. |
| Map | Complet | Artefact de carte | Crée un artefact de carte PlaidCloud. |
| Map Input | Complet | [Importation de fichier spatial](/fr/reference/workflow-steps/spatial/spatial-file-import/) | Lit les fichiers MapInfo, ESRI, KML et GeoJSON avec leurs fichiers annexes. |
| Master Selector | Partiel | Variable de workflow contrôlée et visibilité conditionnelle d'étape | Convertit les conditions d'affichage et de masquage des éléments d'interface de l'outil en visibilité conditionnelle d'étape. Convertit au mieux le sous-workflow que la sélection exécute ; la validation sur de vraies applications du tenant est encore en attente : vérifiez donc la cible d'exécution sélectionnée avant de vous y fier en production. |
| Message | Complet | Condition d'étape (message) | Émet un avertissement, un message ou une erreur de workflow à partir d'une condition. |
| Modeling | Complet | [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) | Fusionné dans l'étape ML Train avec le choix de modèle du pipeline. |
| Multi-Field Formula | Complet | Transformation de formule multi-champs | Applique une formule à plusieurs champs sélectionnés. |
| Multi-Row Formula | Complet | Transformation de formule de fenêtre / sensible aux lignes | Convertit la logique relative aux lignes en comportement de fenêtre, partitionné par Group By. |
| Named Entity Recognition (NER) | Complet | [Text: NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) (tâche ner) | Extrait des entités (personnes, organisations, lieux, dates, quantités ou liste de types personnalisée) d'une colonne de texte via l'étape NLP AI reposant sur un LLM. |
| Numeric Up Down | Complet | Variable numérique contrôlée | Convertit la saisie numérique de l'application en variable typée. |
| Output Data | Complet | Sortie vers documents / table | Écrit la sortie dans des documents ou des tables PlaidCloud, y compris des fichiers Parquet et Avro ; les sorties `.yxdb`, `.hyper` et `.dbf` sont écrites au format Parquet. |
| Overlay | Complet | [Traitement spatial](/fr/reference/workflow-steps/spatial/spatial-process/) | Intersecte, réunit ou découpe deux colonnes de géométrie. |
| PDF Input | Complet | Exécuteur d'extraction PDF | Extrait le texte ou les tables des PDF. |
| Point To Line | Complet | Opération d'exécuteur Point To Line | Relie les points de chaque groupe en une `SequenceLine` par groupe, ordonnée selon le champ de séquence. |
| Poly-Build | Complet | [Spatial Poly-Build](/fr/reference/workflow-steps/spatial/spatial-poly-build/) | Construit un polygone ou une enveloppe convexe par groupe de points. |
| Poly-Split | Complet | [Spatial Poly-Split](/fr/reference/workflow-steps/spatial/spatial-poly-split/) | Une ligne par sommet, polygone composant ou trou. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Complet | Artefacts de rapport | Convertissent le contenu, la mise en page et le rendu du rapport en sortie de rapport PlaidCloud. |
| POS Tagger | Complet | [Text: NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) (tâche pos) | Étiquette la nature grammaticale de chaque jeton d'une colonne de texte via l'étape NLP AI reposant sur un LLM. |
| Predict | Complet | [ML : scorer](/fr/reference/workflow-steps/machine-learning/ml-score/) | Évalue les données avec la table du modèle entraîné et ajoute une colonne de prédiction. |
| Radio Button | Complet | Variable de workflow contrôlée | Convertit les choix par bouton radio de l'application en entrée contrôlée. |
| Random % Sample | Complet | Table Extract (aléatoire) | Renvoie le nombre ou le pourcentage exact d'enregistrements demandé. |
| Record ID | Complet | Transformation d'identifiant de ligne | Ajoute un identifiant d'enregistrement déterministe du type et de la valeur de départ configurés, redémarrant à chaque groupe. |
| Redistribute | Complet | Opération d'exécuteur Redistribute | Réaffecte une mesure d'un ensemble de zones géographiques à un autre selon la surface de chevauchement, ajoutée dans une colonne `Redistributed`. |
| RegEx | Complet | Transformation d'expression régulière | Analyse, fait correspondre ou remplace du texte. |
| Regression | Complet | [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/) | Fusionne la chaîne de modélisation assistée en une seule étape ML Train. |
| Report Map | Complet | Artefact de rapport cartographique | Produit un artefact de carte / rapport natif cloud. |
| Run Command | Partiel | Étape [Requête REST](/fr/reference/workflow-steps/general/rest-request/) sur une connexion REST (`curl`/`wget` uniquement) | Convertit une ligne de commande `curl` ou `wget` en étape Requête REST. Les commandes d'interpréteur et de script (`cscript`, PowerShell, Python et similaires), l'automatisation COM d'Excel, les opérations sur le système de fichiers et les commandes opaques ou qui lancent des workflows sont signalées par leur nom pour revue manuelle plutôt que converties automatiquement. |
| Sample | Complet | Transformation d'échantillon | Conserve des enregistrements par nombre, pourcentage ou regroupement. |
| Select | Complet | Étape de sélection et de projection de schéma | Sélectionne, renomme, réordonne et retype les champs. |
| Smooth | Complet | [Spatial Smooth](/fr/reference/workflow-steps/spatial/spatial-smooth/) | Lisse chaque géométrie sur un nombre de passes donné. |
| Sort | Complet | Transformation de tri | Trie les enregistrements selon les champs et les sens configurés. |
| Spatial Info | Complet | [Spatial Info](/fr/reference/workflow-steps/spatial/spatial-info/) | Surface, longueur, centroïde et rectangle englobant sous forme de mesures géodésiques. |
| Spatial Match | Complet | [Correspondance spatiale](/fr/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/fr/reference/workflow-steps/spatial/spatial-match-executor/) | Convertit toutes les relations (Within, Contains, Intersects, Touches, Crosses, Overlaps et Centroid-In), évaluées dans la base de données ou dans le moteur de workflow. |
| Spatial Process | Complet | [Traitement spatial](/fr/reference/workflow-steps/spatial/spatial-process/) | Intersecte, réunit ou découpe des colonnes de géométrie. |
| Summarize | Complet | Transformation d'agrégation | Regroupe et agrège : somme, nombre, moyenne, minimum, maximum, médiane, mode, écart type, variance et nombre de valeurs distinctes. |
| Tab | Complet | Regroupement d'onglets d'application | Conservé comme structure de l'application convertie. |
| Test | Complet | Condition d'étape | Convertit les assertions de test en conditions d'étape. |
| Text Box | Complet | Variable de texte contrôlée | Convertit la saisie de texte de l'application en variable typée. |
| Text Input | Complet | Entrée de table en ligne | Crée des données en ligne pour le workflow. |
| Text Pre-processing | Complet | Exécuteur de prétraitement NLP | Normalise et prétraite le texte. |
| Text Summary | Complet | [Text: NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) (tâche summary) | Résume une colonne de texte en un nombre maximal de phrases configuré via l'étape NLP AI reposant sur un LLM. |
| Text To Columns | Complet | Transformation de scission en colonnes | Scinde le texte en champs ou en lignes. |
| Tile | Complet | Transformation de tuilage / regroupement | Affecte des groupes de tuiles selon une règle configurée. |
| Tool Container | Complet | Conteneur de canevas / groupe d'exécution | Conservé comme organisation du workflow. |
| Topic Modeling | Complet | Exécuteur de modélisation de sujets | Exécute la modélisation de sujets via un NLP géré. |
| Transformation | Complet | Étape de transformation | Convertit la logique de transformation en expressions ou en SQL PlaidCloud. |
| Transpose | Complet | Transformation de dépivotage | Convertit les colonnes en lignes sous forme de paire nom/valeur. |
| Tree | Complet | Variable de workflow contrôlée | Convertit la sélection d'arborescence de l'application en entrée contrôlée. |
| Union | Complet | Transformation d'union | Combine les flux par nom, par position ou selon des règles configurées. |
| Unique | Complet | Transformation de séparation unique / doublons | Sépare les premiers enregistrements uniques des doublons. |
| Visual Layout | Complet | Métadonnées de disposition du canevas | Conservé comme contexte de conception. |
| Word Cloud | Complet | Artefact de visualisation de texte | Crée un artefact de visualisation à partir de l'analyse de texte. |
| XML Parse | Complet | Transformation d'analyse XML | Extrait les champs XML dans les données du workflow. |
| Zero-shot Text Classification | Complet | [Text: NLP AI](/fr/reference/workflow-steps/text-documents/nlp-ai/) (tâche zeroshot) | Classe une colonne de texte selon une liste de libellés candidats propre à chaque ligne, à un ou plusieurs libellés, via l'étape NLP AI reposant sur un LLM. |
| Find Nearest | Complet | [Spatial Find Nearest](/fr/reference/workflow-steps/spatial/spatial-find-nearest/) | Jointure du voisin le plus proche classée par distance : en ligne droite, et plus proche en temps de trajet (classé en minutes sur un réseau routier) via le moteur de routage auto-hébergé de PlaidCloud. Temps de trajet activé par espace de travail. |
| Trade Area | Complet | [Spatial Trade Area](/fr/reference/workflow-steps/spatial/spatial-trade-area/) | Tampons concentriques dimensionnés en unités réelles : à rayon fixe, et zones de chalandise en temps de trajet (minutes sur un réseau routier) via le moteur de routage auto-hébergé. Temps de trajet activé par espace de travail. |
| Image Template | Complet | Opération d'exécuteur Image Template | Le mode manuel recadre l'image selon chaque région que vous dessinez sur le modèle. Le mode automatique détecte pour vous les régions de la page avec un modèle de mise en page ouvert standard et émet une ligne par région, chacune portant ses limites détectées et son niveau de confiance pour revue ; une page que le modèle ne peut pas lire avec confiance est signalée par son nom plutôt que recadrée. La détection ouverte standard peut différer de celle d'Alteryx : vérifiez les régions détectées, ou utilisez le mode manuel pour un contrôle exact. |
| Image Recognition | Complet | Exécuteur de reconnaissance d'image | Entraîne un classifieur d'images dans le workflow et lui soumet de nouvelles images, sur place : aucun compte externe et aucune donnée ne quitte PlaidCloud. Le classifieur est réentraîné plutôt que copié depuis Alteryx ; les résultats sont donc une approximation fidèle plutôt qu'une correspondance à l'identique, et l'entraînement s'exécute sur CPU. Activé par espace de travail. |
| Geocoder | Complet | Géocodeur auto-hébergé | Géocode des adresses en coordonnées et effectue le géocodage inverse de coordonnées en adresses avec le géocodeur propre à PlaidCloud : aucun compte externe, aucune donnée ne quitte PlaidCloud. Activé par espace de travail. |

Les widgets d'interface (listes déroulantes, zones de liste, cases à cocher, saisies
de texte, numériques et de date, sélecteurs de fichier et de dossier), les objets du canevas (commentaires, liens,
conteneurs) et les ports de macro sont tous convertis en variables contrôlées ou en
objets de canevas natifs. La disposition complète de l'interface d'une application Alteryx (la définition
`<Questions>` du fichier `.yxwz`) est également matérialisée en une interface « App
Runner » Panel publiée : la conversion de l'application produit donc un formulaire de saisie opérationnel qui
collecte les mêmes valeurs et pilote le workflow converti, et pas seulement
les variables contrôlées individuelles. Voir la ligne Analytic App interface ci-dessus et
[Utiliser des applications Alteryx converties](/fr/guides/workflows/use-converted-alteryx-apps/#linterface-app-runner).

**À propos de la sortie Excel.** Un classeur neuf simple (données écrites avec la mise en forme
par défaut) est converti intégralement. L'écriture dans un *modèle mis en forme*, qui remplit des feuilles
et des plages nommées tout en préservant leur mise en forme, est convertie pour une feuille unique
et pour plusieurs sorties assemblées dans différentes feuilles d'un même classeur
(l'étape [Export to Excel Sheets](/fr/reference/workflow-steps/export/export-to-excel-sheets/)
remplit toutes les feuilles en un seul passage). Les modèles qui contiennent des tableaux croisés dynamiques ou des graphiques
perdent ces objets lors de l'écriture de leurs feuilles ; la manipulation de fichiers au niveau des feuilles pilotée
par Run Command (Excel COM/VBS) est signalée par son nom pour revue manuelle plutôt que
convertie automatiquement.

## Couverture des outils spatiaux

Chaque outil de la palette **Spatial** d'Alteryx dispose d'une voie PlaidCloud, et chacune
de ces voies est une étape que vous pouvez aussi construire à la main : la conversion est un
confort, pas la seule voie d'entrée. Consultez les [étapes géospatiales](/fr/reference/workflow-steps/spatial/)
pour la référence complète et [Analyse géospatiale](/fr/guides/workflows/geospatial-analytics/)
pour savoir comment elles s'articulent.

| Outil spatial Alteryx | Voie PlaidCloud | S'exécute dans |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/fr/reference/workflow-steps/spatial/spatial-buffer/) | Moteur de workflow |
| Centroid | Opération d'exécuteur Centroid | Moteur de workflow |
| Convex Hull | Opération d'exécuteur Convex Hull | Moteur de workflow |
| Create Points | [Expression Table Extract](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) | Base de données |
| Distance | [Expression Table Extract](/fr/reference/workflow-steps/spatial/spatial-sql-recipes/) | Base de données |
| Find Nearest | [Spatial Find Nearest](/fr/reference/workflow-steps/spatial/spatial-find-nearest/) | Base de données ; service de routage pour le temps de trajet |
| Generalize | [Spatial Generalize](/fr/reference/workflow-steps/spatial/spatial-generalize/) | Moteur de workflow |
| Heat Map | [Heat Map (macro)](/fr/reference/workflow-steps/macros/macro-heat-map/) | Moteur de workflow |
| Line To Polygon | Opération d'exécuteur Line To Polygon | Moteur de workflow |
| Make Grid | [Spatial Make Grid](/fr/reference/workflow-steps/spatial/spatial-make-grid/) | Moteur de workflow |
| Point To Line | Opération d'exécuteur Point To Line | Moteur de workflow |
| Poly-Build | [Spatial Poly-Build](/fr/reference/workflow-steps/spatial/spatial-poly-build/) | Moteur de workflow |
| Poly-Split | [Spatial Poly-Split](/fr/reference/workflow-steps/spatial/spatial-poly-split/) | Moteur de workflow |
| Redistribute | Opération d'exécuteur Redistribute | Moteur de workflow |
| Smooth | [Spatial Smooth](/fr/reference/workflow-steps/spatial/spatial-smooth/) | Moteur de workflow |
| Spatial Info | [Spatial Info](/fr/reference/workflow-steps/spatial/spatial-info/) | Moteur de workflow |
| Spatial Match | [Correspondance spatiale](/fr/reference/workflow-steps/spatial/spatial-match/) | Base de données |
| Spatial Match : objet d'intersection, Unmatched | [Spatial Match (Intersect / Unmatched)](/fr/reference/workflow-steps/spatial/spatial-match-executor/) | Moteur de workflow |
| Spatial Process | [Traitement spatial](/fr/reference/workflow-steps/spatial/spatial-process/) | Moteur de workflow |
| Trade Area (rayon fixe + temps de trajet) | [Spatial Trade Area](/fr/reference/workflow-steps/spatial/spatial-trade-area/) | Moteur de workflow ; service de routage pour le temps de trajet |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/fr/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Moteur de workflow |
| Entrée de fichier spatial | [Importation de fichier spatial](/fr/reference/workflow-steps/spatial/spatial-file-import/) | Moteur de workflow |
| Summarize : SpatialObjCombine, SpatialObjConvexHull | [Combinaison spatiale](/fr/reference/workflow-steps/spatial/spatial-combine/) | Moteur de workflow |
| Report Map | [Report Map](/fr/reference/workflow-steps/reports/report-map/) | Moteur de workflow |

**Zones de chalandise et voisin le plus proche en temps de trajet.** Les anneaux de temps de trajet de Trade Area et le
classement en temps de trajet de Find Nearest s'exécutent sur le moteur de routage auto-hébergé de PlaidCloud
(isochrones de réseau routier et matrices de temps de trajet), et non sur une API tierce
hébergée : les coordonnées d'origine ne quittent donc jamais la plateforme. Le temps de trajet est activé par
espace de travail. Le routage et les zones en temps de trajet utilisent les données OpenStreetMap :
© les contributeurs d'OpenStreetMap, disponibles sous la [licence Open Database
(ODbL)](https://www.openstreetmap.org/copyright).

### Prérequis spatiaux connus

Les outils spatiaux eux-mêmes sont convertis ; il s'agit ici de prérequis portant sur les données d'entrée.

- **Le format GeoFile `.geo`.** Le GeoFile binaire propriétaire d'Alteryx ne dispose d'aucun
  lecteur ouvert : l'importation d'un tel fichier échoue donc par défaut, au lieu de planter à l'exécution. Dans Alteryx, réexportez la couche
  vers un format spatial standard (shapefile ou GeoJSON) et importez-la à la place ; les autres formats spatiaux
  ne sont pas concernés. Voir
  [Migrer des workflows Alteryx spatiaux](/fr/guides/workflows/migrate-spatial-alteryx-workflows/#regrouper-les-entrées-spatiales).
- **La mesure Peano key de Spatial Info.** Peano key est un index spatial propriétaire d'Alteryx
  sans spécification publique : un Spatial Info qui la demande
  ignore donc cette colonne et la nomme dans une remarque. Toutes les autres mesures de Spatial Info
  (surface, longueur, centroïde, rectangle englobant, type d'objet, nombre de parties et de points
  et extrémités) sont converties.
- **Coordonnées projetées de Create Points.** Create Points convertit directement
  les coordonnées de longitude/latitude en virgule flottante et en entier (×1 000 000).
  Les coordonnées déjà exprimées dans un système projeté doivent d'abord être reprojetées en longitude/latitude WGS84
  en amont, car le workflow n'enregistre pas la projection utilisée.

## Couverture des outils Calgary

Une base de données Alteryx Calgary (`.cydb`) est un stockage indexé propriétaire que PlaidCloud ne peut pas ouvrir. La conversion considère chacune comme représentant une table PlaidCloud ordinaire, nommée `calgary_<database name>`, de sorte que les outils qui s'appuient sur elle sont convertis en opérations de table ordinaires au lieu d'être purement refusés. Voir [Bases de données Calgary](/fr/guides/workflows/migrate-alteryx-workflows/#bases-de-données-calgary) pour le fonctionnement de la table de substitution, et [Calgary Join et Cross Count Append](/fr/guides/workflows/migrate-alteryx-workflows/#calgary-join-et-cross-count-append) pour les outils de correspondance d'index.

| Outil Alteryx Calgary | Voie PlaidCloud | Conversion |
| --- | --- | --- |
| Calgary Loader | Table Extract écrivant `calgary_<database>` | Oui, une fois la base de données nommée et si elle stocke au moins un champ de données. |
| Calgary Input | Entrée de documents dynamique lisant `calgary_<database>`, avec la requête enregistrée comme filtre | Oui, y compris une requête construite à partir d'un Or ou enveloppée dans un Not, et un filtre contains ou starts-with (reconstruit en SQL LIKE). Refus pour une requête de recherche spatiale et pour les limites Skip Records/Max Records. |
| Calgary Input (Count Only) / Calgary Cross Count | Transformation d'agrégation sur `calgary_<database>` | Oui, y compris un compartiment construit à partir d'un Or ou enveloppé dans un Not. Refus pour un croisement portant sur plus d'un champ personnalisé, et pour une lecture en count-only qui ne nomme aucune colonne à compter. |
| Calgary Join | Entrée de documents dynamique faisant correspondre chaque enregistrement de son entrée à `calgary_<database>` | Lorsque le champ entrant est une valeur simple mise en correspondance avec un index de valeurs, y compris en mode Count Only, qui compte les enregistrements de la base correspondant à chaque enregistrement en entrée, un enregistrement sans correspondance comptant zéro. Refus lorsque le champ est spatial (à reconstruire avec Spatial Match) ou que son type est non résolu, pour les Join à index par plage ou à sortie non appariée connectée, pour un Join qui ne nomme aucun champ de correspondance, et pour un Join dont rien n'est connecté à l'entrée. |
| Calgary Cross Count Append | Entrée de documents dynamique faisant correspondre chaque enregistrement, puis jointure avec comptage sur `calgary_<database>` | Lorsque le champ entrant est une valeur simple mise en correspondance avec un index de valeurs : il compte, pour chaque enregistrement en entrée, les enregistrements de la base correspondants, et un enregistrement sans correspondance compte zéro. Refus pour un index spatial ou non résolu (à reconstruire avec Spatial Match), une grille de comptage croisé à valeurs personnalisées, un index par plage et une correspondance qui ne nomme aucun champ. |

### Prérequis Calgary connus

La plupart sont des prérequis portant sur les données d'entrée plutôt que des limites de conversion.

- **Une correspondance sur index spatial doit être reconstruite avec Spatial Match.** Un Calgary Join ou Cross Count Append mis en correspondance avec un index spatial est refusé, avec le nom de la table de substitution : le workflow enregistre le nom de l'index mais pas s'il contient des valeurs ordinaires ou une géométrie spatiale, et une correspondance de valeurs (une jointure d'égalité) et une correspondance spatiale (point dans polygone) sont des opérations différentes. Exportez la base de données vers une table et reconstruisez la correspondance avec un Join (index de valeurs) ou un Spatial Match (index spatial).
- **Une lecture limitée par Skip Records ou Max Records nécessite un ordre explicite.** La table de substitution exportée ne conserve aucun ordre d'enregistrement : ajoutez donc une colonne d'ordre lors de l'exportation si vous devez prendre les N premiers ou derniers enregistrements par position.
- **Une base de données démographique ou de référence doit d'abord être chargée.** Une lecture Calgary effectuée avant le chargement de sa base de données s'arrête en nommant la table à construire. Le fichier `.cydb` lui-même ne dispose d'aucun lecteur ouvert : réexportez-le dans Alteryx (un Calgary Input vers un outil Output Data écrivant du CSV ou du Parquet) et importez-le comme table nommée ; voir [Bases de données .cydb (Calgary) illisibles](/fr/guides/workflows/troubleshoot-alteryx-imports/#bases-de-données-cydb-calgary-illisibles). C'est le cas courant des fichiers `.cydb` démographiques et de référence sous licence livrés avec Alteryx (Experian, Census et similaires) : aucun convertisseur ne peut reproduire ces données tierces ; apportez donc vos propres données de référence sous licence et chargez-les dans la table nommée, comme pour les données de référence du Geocoder.
- **Un Calgary Loader qui ne stocke aucun champ de données n'est pas converti**, car la table qu'il écrirait n'aurait aucune colonne.
- **Une grille de comptage croisé à valeurs personnalisées n'est pas encore convertie.** Un seul champ de comptage croisé simple est converti (il compte, pour chaque enregistrement en entrée, les enregistrements correspondants de la base), mais une grille de valeurs personnalisées *nommées* ajouterait une colonne de comptage par valeur, et Alteryx ne documente ni le nombre de ces colonnes ni leurs noms. Prévu pour une version future, en attente d'un export de référence permettant de déduire le contrat des colonnes.

Les requêtes de valeur, de plage, contains et starts-with sont toutes converties en filtre ; seule une requête de recherche spatiale, une opération d'index sans équivalent au niveau des colonnes, ne l'est pas.

## Connexion aux systèmes externes

Les points de terminaison de connecteurs d'Alteryx (Salesforce, HTTP, Google Analytics, Cassandra,
e-mail, Hadoop et Spark, dans les deux sens) ne sont pas convertis, car
PlaidCloud atteint ces systèmes par une connexion plutôt que par un
outil du canevas. Chacun est refusé avec son nom, et l'on indique où
le travail doit se faire :

| Outil Alteryx | Où cela se place dans PlaidCloud |
| --- | --- |
| Salesforce Input / Output | Une connexion **Salesforce** |
| Anaplan | Une connexion **Anaplan** |
| HTTP Input | Une étape **Requête REST** sur une connexion **REST** |
| Google Analytics Input | **Importation : source Singer** avec le tap Google Analytics |
| Cassandra Input | **Importation : source Singer** avec le tap Cassandra |
| Email Input | **Importation : source Singer** avec le tap GMail |
| Hadoop Input / Output | **Importation : SQL** / **Exportation : SQL** via une connexion Hive, Impala ou Presto |
| Spark Input / Output | **Importation : SQL** / **Exportation : SQL** via une connexion Databricks |

Quatre d'entre eux n'ont aucune voie d'écriture. PlaidCloud lit Google Analytics
et Cassandra mais n'y écrit jamais : un outil Google Analytics Output ou
Cassandra Output devient donc une étape **Exportation : SQL** vers une destination prise en charge.
L'e-mail n'est pas non plus une destination de données : **Notification : e-mail** envoie une
notification à des personnes, de sorte qu'un outil Email Output devient une étape d'exportation plus une
notification distincte. La connexion **Anaplan** est en lecture seule de la même
manière : elle lit une vue enregistrée, exécute une action d'exportation préexistante ou charge des
listes dans une dimension PlaidCloud, mais aucune étape PlaidCloud
n'écrit en retour dans Anaplan.

## Valider un workflow converti

Pour les workflows de production, validez les sorties converties par rapport aux sorties Alteryx de référence :
la validation PlaidCloud porte sur le schéma, le nombre de lignes et les valeurs des lignes,
et ignore l'ordre des lignes sauf si le workflow en dépend. Les opérations spécialisées
(spatial, correspondance approximative, OCR, NLP, reporting) s'exécutent par l'intermédiaire d'exécuteurs de
tâches gérés qui maintiennent le workflow natif cloud ; les pipelines d'apprentissage automatique
sont convertis en étapes natives [ML : entraîner un modèle](/fr/reference/workflow-steps/machine-learning/ml-train/)
et [ML : scorer](/fr/reference/workflow-steps/machine-learning/ml-score/).
Consultez [Migrer des workflows Alteryx](/fr/guides/workflows/migrate-alteryx-workflows/)
pour le guide complet d'importation et de validation.
