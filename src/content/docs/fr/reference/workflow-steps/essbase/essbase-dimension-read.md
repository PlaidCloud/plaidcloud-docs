---
title: "Essbase : lire une dimension"
description: Lisez le plan d'une dimension Oracle Essbase dans la hiérarchie principale d'une dimension PlaidCloud, en accès direct au cloud, en refusant nommément tout membre partagé, de type étiquette seule, Dynamic Calc ou attribut, ainsi que tout ce que le plan ne peut pas représenter.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## Description

Lit le plan d'une dimension d'un cube Oracle **Essbase** via votre [connexion Oracle Essbase](/fr/guides/connections/essbase/) et le charge dans la **hiérarchie principale** d'une dimension PlaidCloud.

Cette étape apparaît dans le menu des étapes sous **Oracle Essbase**.

L'étape accède à Essbase **en direct dans le cloud** par son API REST : il n'existe aucun chemin par agent local pour cette étape, ni de variante distante.

## Configuration

### Source Essbase

| Champ | Obligatoire | Remarques |
|---|---|---|
| Connexion | Oui | La [connexion Oracle Essbase](/fr/guides/connections/essbase/) par laquelle lire. |
| Application | Oui | L'application Essbase à lire. Le sélecteur liste les applications que le compte de service de la connexion peut voir ; si la connexion définit une application par défaut, elle est présélectionnée. |
| Cube (base de données) | Oui | Le cube de l'application choisie dont lire le plan. |
| Dimension | Oui | La dimension Essbase dont lire le plan. |

### Dimension PlaidCloud cible

| Champ | Obligatoire | Remarques |
|---|---|---|
| Dimension cible | Oui | La dimension PlaidCloud dans laquelle le plan est chargé. |

## Ce que cette étape ne peut pas représenter

| Limite | Signification |
|---|---|
| Membres partagés | Un membre partagé réutilise les données d'un autre membre sous un second parent. Un nœud de dimension PlaidCloud n'a qu'un seul parent ; un membre partagé est donc refusé nommément plutôt que chargé en double ou ignoré en silence. Lisez le cumul principal comme une dimension PlaidCloud distincte : le second parent d'un membre partagé ne peut pas être représenté ici. |
| Membres de type étiquette seule | Un membre de type étiquette seule sert à la navigation et ne contient jamais de données propres. Il est refusé nommément plutôt que chargé comme un membre ordinaire dont rien en aval n'attend qu'il soit vide. |
| Membres Dynamic Calc | La valeur d'un membre Dynamic Calc est calculée à la volée par Essbase et jamais stockée. Cette étape lit la structure du plan, pas des données calculées ; un membre Dynamic Calc est donc refusé nommément plutôt que chargé comme s'il s'agissait d'un membre stocké. |
| Dimensions d'attributs | Une dimension d'attributs classe les membres d'une dimension de base ; ce n'est pas une hiérarchie de faits à part entière. Sa lecture est refusée d'emblée ; lisez plutôt la dimension de base. |
| Opérateurs de consolidation non représentables | Une arête PlaidCloud porte un indicateur de consolidation (`+`, `-` ou `~`). Les opérateurs `+` et `-` d'Essbase s'y rapportent directement. `*`, `/` et `%` ne peuvent pas être représentés par un simple signe de cumul : un membre qui en utilise un est refusé nommément plutôt que chargé avec un signe erroné. |
| Plans dépassant le plafond de membres | Un plan de dimension de plus de **5 000 membres au total** est refusé plutôt que chargé partiellement, l'erreur indiquant le nombre constaté et le plafond. Lisez un niveau moins profond de la hiérarchie, ou une sous-arborescence plus petite, pour passer sous la limite. |

## Voir aussi

- [Se connecter à Oracle Essbase (guide)](/fr/guides/connections/essbase/) — créez la connexion.
- [Connecteur Oracle Essbase](/fr/reference/connectors/erp/oracle-essbase/) — référence des champs de connexion.
- [Essbase : interroger un cube](/fr/reference/workflow-steps/essbase/essbase-query/) — exécute une requête MDX en direct sur un cube, en accès direct au cloud.
- [Étapes Oracle Essbase](/fr/reference/workflow-steps/essbase/)
