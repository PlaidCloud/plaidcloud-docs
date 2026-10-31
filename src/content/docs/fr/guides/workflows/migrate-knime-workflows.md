---
title: Migrer des workflows KNIME
description: Convertissez un workflow KNIME (.knwf) ou un groupe de workflows (.knar) en workflows avancés PlaidCloud depuis l'application Analyze, l'API REST ou un agent IA connecté par MCP, liez ses entrées et ses connexions, puis lisez le rapport de conversion.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloud remplace KNIME sans changement de fonctionnement. 98,5 % des configurations de nœuds KNIME se convertissent intégralement, et 205 des 207 types de nœuds principaux sont Full (pris en charge intégralement) : chacun devient des étapes de workflow PlaidCloud standard qui accomplissent le travail du nœud. Le convertisseur transforme une archive de workflow KNIME en workflows avancés exécutables, conserve le graphe d'origine et renvoie un rapport de conversion qui nomme tout ce que vous devez définir. La [matrice de conversion KNIME](/fr/reference/knime-conversion-matrix/) répertorie chaque nœud.

La conversion ne lit que l'archive que vous indiquez. Elle ne contacte jamais le système dans lequel un nœud KNIME lit ou écrit des données.

La conversion est une opération ponctuelle. Convertir de nouveau la même archive crée de nouveaux workflows, et les modifications que vous avez apportées dans PlaidCloud ne sont jamais fusionnées avec un export ultérieur.

## Ce que PlaidCloud crée

- Un workflow avancé pour chaque workflow KNIME. Un fichier `.knwf` donne un workflow, et un fichier `.knar` en donne un pour chaque workflow du groupe.
- Chaque nœud KNIME devient l'étape de workflow, la variable de projet ou l'objet de canevas correspondant, avec les relations amont et aval préservées. Les métanœuds et les composants sont aplatis dans le workflow, de sorte que leurs nœuds s'exécutent comme des étapes ordinaires.
- Les variables de flux, ainsi que les nœuds Configuration et Widget, deviennent des variables de projet qui contiennent leurs valeurs par défaut. Les commutateurs et les boucles dont les valeurs sont connues au moment de la conversion sont élagués et développés en étapes qui s'exécutent.
- Les langages d'expression de KNIME (Expression, String Manipulation, Math Formula, Column Expressions et Rule Engine) sont convertis en expressions PlaidCloud.
- Les fichiers de données fournis dans l'archive sont téléversés dans un dossier `knime/` du compte de documents par défaut du projet, un dossier par workflow, et les lecteurs convertis les y importent.
- Les vues, les graphiques et les gestionnaires de couleurs n'ont aucun effet sur les données. Ils sont ignorés et répertoriés dans le rapport de conversion.

## Avant de commencer

1. Exportez le workflow depuis KNIME Analytics Platform sous la forme d'un fichier `.knwf`. Pour convertir plusieurs workflows à la fois, exportez leur groupe de workflows sous la forme d'un fichier `.knar`. Conservez les fichiers utilisés par vos lecteurs dans le dossier `data` du workflow afin qu'ils soient fournis dans l'archive.
2. Téléversez l'archive dans un [compte de documents](/fr/guides/documents/adding-accounts/) que vous pouvez lire. Dans l'application Analyze, **Parcourir** dans la fenêtre d'importation la téléverse depuis votre ordinateur.
3. Choisissez le projet PlaidCloud qui doit recevoir les workflows. Vous devez être Architecte ou Gestionnaire du projet, et le projet doit avoir un compte de documents par défaut.
4. Notez les tables, les fichiers et les connexions PlaidCloud que les lecteurs et les nœuds connecteurs du workflow doivent utiliser. Consultez [Lier les sources](#lier-les-sources).

## Convertir un workflow

Effectuez la conversion depuis l'application Analyze, l'API REST ou un agent IA connecté par MCP. L'API REST et l'outil MCP acceptent les mêmes champs ; la fenêtre accepte ceux qu'elle affiche.

### Application Analyze

1. Ouvrez **Analyze** et choisissez **Outils → Importer un workflow KNIME**.
2. Sous **Importer la source et la cible**, choisissez le **Projet cible** et l'**Archive KNIME (.knwf ou .knar)** dans un compte de documents. Sélectionnez **Parcourir** pour téléverser l'archive depuis votre ordinateur.
3. Sous **Préfixes d'objets**, définissez éventuellement le **Préfixe de workflow**, le **Préfixe d'étape** et le **Préfixe de table**. Le préfixe de table correspond par défaut au nom du workflow.
4. Sous **Liaisons de source (facultatif)**, liez éventuellement un lecteur à une table existante du projet cible : sélectionnez **Ajouter**, puis saisissez le **Lecteur KNIME** (son identifiant de nœud, tel que `12:3`, son nom de nœud ou son nom de fichier) et l'**ID de la table**. Pour lier des connexions, des documents ou des tables d'autres projets, utilisez l'API REST ou l'outil MCP. Consultez [Lier les sources](#lier-les-sources).
5. Sélectionnez **Importer**.

La fenêtre affiche la progression pendant la conversion de l'archive, puis le rapport de conversion : le nombre d'étapes (**Étapes**, **Confiance élevée**, **Moyenne**, **Faible** et **Non convertis**), les nœuds qui n'ont pas pu être convertis et les étapes en aval, les conversions partielles, les avertissements, les fichiers sources à téléverser et les nœuds sans étape. Lorsqu'une conversion n'appelle aucune vérification, la fenêtre l'indique et se ferme d'elle-même.

### Champs

| Champ | Obligatoire | Fonction |
| --- | --- | --- |
| `source_account_id` | Oui | Compte de documents qui contient l'archive KNIME. |
| `source_file_path` | Oui | Chemin du fichier `.knwf` ou `.knar` dans ce compte. |
| `project_id` | Oui | Projet dans lequel les workflows sont créés. |
| `workflow_prefix` | Non | Préfixe ajouté aux noms de workflow. |
| `step_prefix` | Non | Préfixe ajouté aux noms d'étape. |
| `table_prefix` | Non | Préfixe ajouté aux noms de table. Correspond par défaut au nom du workflow. Un préfixe qui réutiliserait le nom d'une table existante est refusé avant toute création. Pour un fichier `.knar`, le préfixe de chaque workflow est suivi du nom de ce workflow. |
| `source_bindings` | Non | Lie les lecteurs et les nœuds connecteurs à des données et à des connexions que vous possédez déjà, dans la limite de 500 entrées. Consultez [Lier les sources](#lier-les-sources). |

### REST

Envoyez les champs sous forme de corps JSON à :

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

Un agent IA connecté par MCP appelle l'outil `knime_convert` avec les mêmes champs. Consultez [Agents IA (MCP)](/fr/integrations/ai-coding-agents/) pour connecter un agent. L'outil modifie votre projet ; vérifiez donc l'appel avant de l'approuver.

## Lier les sources

Utilisez `source_bindings` pour diriger un lecteur KNIME vers des données qui existent déjà dans PlaidCloud plutôt que vers la copie de l'archive. Une clé est un identifiant de nœud (tel que `12:3`), un nom de nœud, un chemin de fichier fourni (tel que `data/sales.csv`) ou un nom de fichier ; la première correspondance dans cet ordre l'emporte. Une valeur est l'une des suivantes :

- Un identifiant `analyzetable_` pour une table du projet cible. La table remplace le lecteur.
- `{"project": "<project id>", "table": "<table id>"}` pour une table d'un autre projet que vous pouvez lire. Le lecteur devient une étape [Import Project Table](/fr/reference/workflow-steps/import/import-project-table/) qui la copie. Le projet source doit partager la lecture avec le projet cible, sinon l'étape émet un avertissement. Une table régie par un accès aux lignes est refusée.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` pour un document que vous pouvez lire. Le lecteur l'importe.
- `{"connection": "<connection id>"}` pour un nœud connecteur de base de données ou REST. Les étapes converties s'exécutent sur cette connexion.

La fenêtre de l'application Analyze lie les lecteurs aux tables du projet cible par ID de table. Liez les connexions, les documents et les tables d'autres projets via l'API REST ou l'outil MCP.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

Une table liée qui n'existe pas, ou une clé qui ne correspond à aucun lecteur, génère un avertissement. Les liaisons appliquées, avec les noms de leur projet et de leur table, sont répertoriées dans le rapport de conversion sous `bindings`.

### Entrées non liées

Un lecteur dont le fichier ne figure pas dans l'archive lit `inputs/<file name>` dans le dossier du workflow du compte de documents par défaut, et le rapport de conversion répertorie le chemin sous `missing_inputs` avec un avertissement. Téléversez le fichier à cet emplacement et exécutez le workflow. Tant que le fichier n'y est pas, l'importation se termine avec un avertissement et crée une table vide, et le workflow continue.

## Identifiants et connexions

Les identifiants KNIME ne sont jamais migrés. Chaque étape qui se connecte à un autre système lit ses identifiants depuis une connexion PlaidCloud ou une variable de projet que vous définissez, et l'avertissement de l'étape dans le rapport de conversion indique lesquels.

| KNIME | Ce que vous définissez |
| --- | --- |
| Connecteurs de base de données | Une connexion de base de données : liez-la avec `{"connection": "<id>"}` ou sélectionnez-la dans l'étape. |
| Nœuds REST et de service web qui se connectent | Une [connexion REST](/fr/reference/connectors/rest/generic-rest/) : liez-la avec `{"connection": "<id>"}` ou sélectionnez-la dans l'étape. |
| Speech Recognizer (IBM Watson) | Une connexion REST dont l'URL de base est l'URL du service Watson que nomme l'avertissement, avec l'utilisateur `apikey` et votre clé d'API comme identifiants de connexion Basic. Liez-la au nœud. |
| Email Connector, avec Email Reader ou Email Mover | Une variable de projet qui contient le mot de passe du serveur de messagerie, avec le nom indiqué par l'avertissement. L'hôte et l'utilisateur proviennent d'Email Connector. |
| Excel Reader ou Excel Writer avec un mot de passe de classeur | Une variable de projet qui contient le mot de passe, avec le nom indiqué par l'avertissement. |
| Connecteurs et authentificateurs LLM | Une connexion LLM sur l'étape IA. |

Consultez [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/) pour définir des variables de projet.

## Lire le rapport de conversion

La fenêtre de l'application Analyze affiche le rapport de conversion à la fin de l'importation, et les réponses REST et MCP le contiennent. Lisez-le avant d'exécuter les workflows.

- `summary` compte les étapes créées et combien ont été mappées avec une confiance élevée, moyenne ou faible.
- `warnings` répertorie chaque avertissement avec son nœud, son étape et l'action à effectuer, y compris chaque identifiant ou connexion à définir.
- `missing_inputs` répertorie les chemins de documents où téléverser les fichiers des entrées non liées.
- `bindings` répertorie les liaisons appliquées.
- `table_prefix` est le préfixe utilisé. Pour un fichier `.knar`, `workflows` répertorie chaque workflow avec son propre préfixe.
- `uploaded_files`, à côté du rapport, répertorie les fichiers fournis qui ont été téléversés dans le compte de documents par défaut.
- `dropped_tools` répertorie les vues et les graphiques qui ont été ignorés.

## Espaces réservés

Un nœud sans chemin de conversion reste sur le canevas sous la forme d'un espace réservé nommé. L'espace réservé transmet ses données et émet un avertissement avec le nom du nœud KNIME, et chaque étape en aval est signalée dans le rapport, de sorte qu'un résultat manquant n'est jamais silencieux. Reconstruisez la fonctionnalité avec une étape standard lorsque son résultat compte.

## Exécuter le workflow converti

1. Ouvrez le nouveau workflow dans le projet.
2. Définissez les variables de projet et les connexions que nomment les avertissements.
3. Téléversez les fichiers des entrées non liées vers les chemins indiqués sous **Fichiers sources à téléverser** dans la fenêtre, ou dans `missing_inputs`.
4. [Exécutez le workflow](/fr/guides/workflows/run-a-workflow/) et vérifiez la table de sortie de chaque étape.

## Cas particuliers

Ce sont les seules différences connues avec KNIME.

- **Crosstab.** Se convertit en [Table: Pivot](/fr/reference/workflow-steps/tables/table-pivot/) (étape). Quelques combinaisons de paramètres donnent des résultats qui diffèrent de ceux de KNIME.
- **Loop End (Column Append).** Se convertit en [Table : jointure interne](/fr/reference/workflow-steps/tables/table-inner-join/). Quelques combinaisons de paramètres donnent des résultats qui diffèrent de ceux de KNIME.
- **Tirages aléatoires.** Row Sampler, Table Partitioner et Equal Size Sampling effectuent le tirage aléatoire propre à KNIME avec [Table: KNIME Random Sample](/fr/reference/workflow-steps/tables/table-knime-random-sample/) (étape), de sorte qu'un nœud avec une graine sélectionne les mêmes lignes que dans KNIME. Le tirage accepte une table de 10 000 000 de lignes au plus ; une table plus grande fait échouer l'étape.

## Guides associés

- [Matrice de conversion KNIME](/fr/reference/knime-conversion-matrix/)
- [Connexion REST](/fr/reference/connectors/rest/generic-rest/)
- [Ajouter des comptes de documents](/fr/guides/documents/adding-accounts/)
- [Gérer les variables de workflow](/fr/guides/workflows/manage-workflow-variables/)
- [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/)
