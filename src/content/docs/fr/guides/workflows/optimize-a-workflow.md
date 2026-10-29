---
title: Optimiser un workflow
description: Accélérez l'exécution d'un workflow avancé en reconstruisant ses dépendances à partir de la lignée des données et en fusionnant les chaînes d'étapes d'extraction, chaque fusion étant vérifiée sur vos données avant d'être appliquée.
sidebar:
  order: 19.6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/optimize-a-workflow.md
---

**Optimiser** examine un workflow avancé et propose des modifications qui accélèrent son exécution. Vous voyez chaque modification avant que quoi que ce soit ne se produise, vous choisissez celles que vous voulez et vous pouvez annuler le résultat plus tard.

Optimiser fonctionne sur les workflows avancés (DAG). Pour un workflow standard, choisissez d'abord **Convertir en avancé...** ; voir [Workflows avancés](/fr/guides/workflows/advanced-workflows/#choisir-le-type-de-workflow).

## Optimiser un workflow

1. Dans la liste **Workflows**, faites un clic droit sur un workflow avancé et choisissez **Optimiser…**. Le workflow ne doit être ni en cours d'exécution ni en pause, et vous devez disposer d'un accès en écriture.
2. La fenêtre **Optimiser le workflow** affiche un titre tel que *34 étapes → 30 étapes · 12 étapes peuvent s'exécuter en parallèle*. Lorsque le workflow a un historique d'exécution, elle ajoute *~11 s plus rapide par exécution*.
3. Sous le titre figure une ligne par modification, chacune avec une case à cocher, les étapes concernées, ce qu'elle implique pour le workflow et le temps qu'elle fait gagner, mesuré comme la variation du temps d'exécution réel. Toutes sont cochées ; décochez celles dont vous ne voulez pas.
4. Une liste **Optimisation impossible** nomme les étapes qu'Optimiser a laissées de côté et la raison précise pour chacune ; voir [Pourquoi une étape ne peut pas être optimisée](#pourquoi-une-étape-ne-peut-pas-être-optimisée).
5. Choisissez **Appliquer N modifications**.

Si le workflow n'a plus rien à améliorer, la fenêtre l'indique.

## Les deux types de modification

### Reconstruire les dépendances à partir de la lignée des données

Optimiser lit les tables que chaque étape lit et écrit, puis redessine les connexions de sorte qu'une étape n'attende que les étapes dont elle utilise les tables. Les étapes qui ne partagent aucune table s'exécutent en parallèle.

- Une étape n'attend plus les étapes sans rapport avec elle ; elle ne s'arrête donc plus lorsqu'une étape sans rapport échoue. Un échec se propage le long des nouvelles dépendances.
- Une exécution partielle par plage d'étapes, comme **Exécuter à partir d'ici**, suit les nouvelles dépendances.
- Le serveur limite toujours le nombre d'étapes exécutées simultanément.
- Les étapes qui désignent leurs tables par nom ou par chemin sont comprises de la même façon que celles qui utilisent des identifiants de table. Un nom doit correspondre à exactement une table du projet ; un nom qui correspond à plusieurs tables, une référence qui utilise une variable et une table d'un autre projet ne peuvent pas être tracés.
- Une étape désactivée ne porte jamais d'ordre et n'est pas comptée parmi les étapes pouvant s'exécuter en parallèle.
- Optimiser écarte cette modification tant qu'une planification ou un autre workflow exécute une plage des étapes de ce workflow.

### Fusionner une chaîne d'étapes d'extraction en une seule

Une chaîne d'étapes Extract Data, chacune lisant la table écrite par la précédente, devient une seule étape qui lit la première source et écrit le dernier résultat.

Chaque fusion est vérifiée avant d'être appliquée. Optimiser exécute les étapes d'origine et l'étape fusionnée sur vos données actuelles dans des tables temporaires, et compare les deux résultats ligne à ligne. Il n'applique la fusion que si elles sont identiques. Votre workflow et ses tables ne sont pas touchés pendant la vérification.

- Un renommage suivi d'un filtre, par exemple une étape Select suivie d'un filtre, peut fusionner en une seule étape.
- Lorsqu'une chaîne entière ne peut pas fusionner, Optimiser propose la plus longue partie qui le peut.
- Les tables situées au milieu d'une chaîne fusionnée ne sont plus écrites par le workflow. Elles sont conservées, non supprimées, et la modification les nomme.
- Une fusion dont les résultats diffèrent, ou qui ne peut pas être vérifiée, n'est pas appliquée, et les résultats en indiquent la raison. Les fusions nécessitent une table source contenant des données.

## Pourquoi une étape ne peut pas être optimisée

Chaque ligne de **Optimisation impossible** nomme sa propre cause :

| Cause | Signification |
|---|---|
| Agrégations | L'étape résume des lignes ; elle ne peut donc pas se fondre dans une étape voisine. |
| Deux filtres | Une chaîne comportant deux filtres ne peut pas devenir une seule étape. |
| Filtre sur un nombre flottant susceptible d'être arrondi | La fusion pourrait changer les lignes retenues ; le filtre reste donc où il est. |
| Étape qui exécute du code utilisateur | Les expressions, scripts et étapes similaires ne peuvent pas être vérifiés comme équivalents. |
| Table lue par plusieurs étapes | La table située au milieu de la chaîne est nécessaire ailleurs. |
| Étape désactivée | Une étape désactivée n'est pas fusionnée et ne porte pas d'ordre. |
| Membre d'un conteneur d'exécution | Les étapes d'un conteneur d'exécution s'exécutent comme un tout. |
| Nombre de lignes indisponible | Le nombre de lignes de la table source ne peut pas être lu, même en direct ; la fusion ne peut donc pas être dimensionnée pour la vérification. |
| Table non identifiable | Le nom de table de l'étape ne correspond à aucune table ou à plusieurs, utilise une variable ou pointe vers un autre projet. |
| Sécurité au niveau des lignes ou table trop grande | La table est régie par la sécurité au niveau des lignes, ou est trop grande pour être vérifiée automatiquement. |

Les conteneurs visuels, qui ne font que regrouper des étapes sur le canevas, n'empêchent pas une fusion. Lorsqu'une fusion retire des étapes de l'un d'eux, l'étape fusionnée prend leur place et un conteneur laissé vide est supprimé. Annuler restaure exactement la disposition.

## Suivre la progression

Après l'application, **Optimisation du workflow** affiche la phase : *Vérification (3 exécutions sur 6)...*, *Comparaison des résultats...* et *Application...*. Une fois terminé, les résultats listent ce qui est **Appliqué**, y compris le nombre de lignes sur lesquelles chaque fusion a été vérifiée, et ce qui est **Non appliqué**, avec une raison pour chaque élément.

Si le workflow a changé pendant la vérification par Optimiser, les modifications concernées sont ignorées et la fenêtre indique leur nombre. Si une application échoue, le workflow est restauré dans l'état où il se trouvait avant.

Une exécution qui démarre pendant la validation des modifications est retardée un instant, et non abandonnée.

## Annuler une optimisation

Faites un clic droit sur le workflow et choisissez **Annuler l'optimisation…**, ou utilisez **Annuler l'optimisation** dans les résultats. Confirmez, et les étapes, les paramètres et la disposition du workflow reviennent à leur état d'avant l'optimisation. Les modifications que vous avez apportées au workflow depuis sont perdues.

L'annulation nécessite des points de restauration, qui ne sont pas disponibles sur tous les tenants. Un tenant qui en est dépourvu ne peut pas appliquer d'optimisation.

## Optimiser via l'API et les assistants IA

Optimiser est également disponible via l'API REST et via l'outil `workflow_optimize` pour les assistants IA, avec les mêmes étapes d'aperçu, d'application et d'annulation.

## Étapes suivantes

- [Workflows avancés](/fr/guides/workflows/advanced-workflows/) : le canevas, les connexions et les contrôles d'exécution
- [Contrôler l'exécution en parallèle](/fr/guides/workflows/controlling-parallel-execution/) : exécuter des étapes en même temps
- [Exécuter un workflow](/fr/guides/workflows/run-a-workflow/) : exécuter un workflow de bout en bout
