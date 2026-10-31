---
title: "TM1 : lire une dimension"
description: Lisez une hiérarchie IBM TM1 / Planning Analytics — éléments, liens parent/enfant et attributs d'éléments — dans une dimension PlaidCloud, en accès direct au cloud via REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## Description

Lit une hiérarchie d'une dimension IBM **TM1 / Planning Analytics** via votre [connexion TM1](/fr/guides/connections/tm1/) et la charge dans une dimension PlaidCloud. Les éléments, les liens parent/enfant et les attributs d'éléments de la hiérarchie TM1 sont d'abord placés en table intermédiaire sous forme de lignes parent/enfant, puis la dimension PlaidCloud est construite à partir de cette table intermédiaire — avec le même chargement que celui de l'étape Dimension Load de PlaidCloud, si bien qu'une hiérarchie TM1 arrive exactement comme une hiérarchie construite à la main ou issue de toute autre source externe.

Cette étape apparaît dans le menu des étapes sous **IBM TM1 / Planning Analytics**.

L'étape accède à TM1 **en accès direct au cloud** via son API REST — aucun agent sur site n'intervient. Consultez [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) pour la voie sur site.

## Configuration

### Source TM1

| Champ | Obligatoire | Remarques |
|---|---|---|
| Connexion TM1 | Oui | La [connexion TM1](/fr/guides/connections/tm1/) à utiliser pour la lecture. |
| Environnement | Oui | L'environnement de la connexion. |
| Base de données | Oui | La base de données TM1 (instance) à lire. Par défaut, la Base de données par défaut de la connexion si elle est définie. |
| Dimension TM1 | Oui | La dimension TM1 à lire. Détectée en direct depuis la base de données connectée, ou saisie à la main. |
| Hiérarchie TM1 | Non | La hiérarchie au sein de la dimension. Détectée en direct une fois la dimension choisie, ou saisie à la main. Laissez vide pour lire la hiérarchie propre (implicite) de la dimension, que TM1 nomme d'après la dimension. |
| Table intermédiaire | Oui | La table dans laquelle arrivent les lignes brutes parent/enfant/attribut avant que la dimension PlaidCloud en soit construite. |

Une fois une dimension et une hiérarchie choisies, le formulaire indique quels attributs d'éléments TM1 deviendront des **alias** PlaidCloud et lesquels des **propriétés**, selon le type d'attribut propre à TM1 (`Alias` ou `Numeric`/`String`). Le type TM1 propre à chaque élément (Numeric, String ou Consolidated) devient aussi une propriété, nommée `tm1_element_type`.

### Dimension PlaidCloud cible

| Champ | Obligatoire | Remarques |
|---|---|---|
| Spécifier la dimension dynamiquement | L'un des deux | Nom de la dimension cible, pouvant contenir des jetons `{variable}` résolus à l'exécution. Sélectionné par défaut. |
| Utiliser une dimension spécifique | L'un des deux | Choisissez plutôt une dimension PlaidCloud existante dans l'arborescence. |
| Hiérarchie alternative | Non | Une clé de hiérarchie alternative PlaidCloud dans laquelle charger. Laissez vide pour charger la hiérarchie principale. |

Le chargement dans une hiérarchie alternative est validé avant toute écriture : une hiérarchie alternative PlaidCloud ne peut pas changer le parent d'un nœud qui existe déjà dans la hiérarchie principale de la dimension, et une hiérarchie alternative TM1 partage par définition ses éléments avec la hiérarchie principale de TM1, ce qui est donc la forme normale pour cette option, et non un cas limite. Si le parent d'une ligne analysée existe déjà dans la hiérarchie principale de la dimension cible, l'étape échoue d'emblée, avant toute modification de la table intermédiaire, en nommant les parents en conflit.

## Ce que cette étape ne peut pas représenter

| Limitation | Signification |
|---|---|
| Les éléments à parents multiples sont refusés | Un nœud de dimension PlaidCloud a exactement un parent par hiérarchie. Un élément TM1 placé sous deux consolidations de la même hiérarchie ne peut pas être chargé : l'étape échoue avec une erreur nommée listant chaque élément fautif et ses parents, plutôt que d'abandonner silencieusement l'élément de la première consolidation. Lisez le cumul alternatif comme une dimension PlaidCloud distincte, ou résolvez d'abord la double filiation dans TM1. |
| Les poids de consolidation ne portent qu'un signe | Un lien PlaidCloud porte un indicateur de consolidation (`+`, `-` ou `~`), pas un coefficient. Le poids TM1 `0` devient `~` (le membre ne se cumule pas dans son parent) ; un poids négatif devient `-` ; un poids positif devient `+` ; un poids absent (la valeur par défaut de TM1) est traité comme `+`. Un **poids fractionnaire ou multiplicateur — 0.5, 2.0 — ne peut pas être représenté** : il arrive sous la forme d'un simple `+` et le multiplicateur est perdu. Cela est compté et nommé, et non passé sous silence : l'avertissement d'étape de l'exécution indique combien de liens sont concernés et les liste sous la forme `parent -> child (weight)`, par exemple `Total Revenue -> Product A (0.5)`, dans la limite de 10, avec « (and N more) » au-delà. Un lien racine (sans parent) est nommé `(root)` plutôt que laissé vide. Un poids présent mais non numérique est refusé d'emblée plutôt que deviné. |
| Pas de détection via un agent | Cette étape fonctionne uniquement en accès direct au cloud — consultez [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) pour lire un serveur TM1 que le cloud ne peut pas atteindre. |

## Voir aussi

- [Se connecter à TM1 (guide)](/fr/guides/connections/tm1/) — crée la connexion.
- [Connecteur TM1](/fr/reference/connectors/rest/tm1/) — référence des champs de connexion, y compris la voie par agent sur site.
- [TM1 : interroger un cube](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — lit les données d'un cube, en accès direct au cloud.
- [TM1 : interroger un cube (agent)](/fr/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — lit les données d'un cube via un agent PlaidLink sur site.
- [Dimension Load](/fr/reference/workflow-steps/dimensions/dimension-load/) — le mécanisme de chargement de dimension sur lequel s'appuie cette étape.
- [Étapes IBM TM1 / Planning Analytics](/fr/reference/workflow-steps/ibm-planning-analytics/)
