---
title: Exécuter un workflow
description: Exécutez un workflow PlaidCloud manuellement ou à la demande, suivez l'état de chaque étape, et suspendez, arrêtez ou reprenez une exécution là où elle s'est interrompue.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Vous pouvez lancer l'exécution complète d'un workflow en cliquant sur l'icône d'exécution dans la hiérarchie **Workflows**, ou en sélectionnant **Run All** dans le menu **Actions** d'un workflow donné.



Vous pouvez aussi cliquer sur le bouton **Toggle Start/Stop** en haut de la table des workflows. Ce bouton à bascule arrête un workflow en cours d'exécution ou démarre un workflow.

Si vous cliquez sur **Exécuter** pour un workflow déjà en cours d'exécution, PlaidCloud vous en informe au lieu de lancer une seconde exécution.

## Choisir un mode de comptabilisation

Chaque exécution porte un mode de comptabilisation ERP. Pour en choisir un dans PlaidCloud, utilisez **Exécuter avec le mode d'écriture** dans le menu contextuel d'un workflow, ou le bouton de mode d'exécution du canevas du workflow ; **Démarrer le workflow** ou **Exécuter le workflow** seul demande le mode Réel, toujours soumis au plafond du projet décrit plus bas. Vous pouvez aussi choisir le mode lorsque vous lancez une exécution via l'API d'exécution ou l'assistant.

| Mode | Ce qui se passe |
|---|---|
| Réel | Les étapes de comptabilisation écrivent exactement comme elles l'ont toujours fait. C'est la valeur par défaut. |
| Simulation | Chaque étape de comptabilisation ERP construit et valide exactement ce qu'elle comptabiliserait, puis ne valide rien et ne contacte jamais l'ERP. Les écritures qui auraient été comptabilisées sont enregistrées dans l'[historique des écritures ERP](/fr/guides/connections/erp-post-history/), marquées comme simulées, afin que vous puissiez les examiner avant une exécution réelle. |
| Désactivé | Les étapes de comptabilisation sont entièrement ignorées. |

Un projet porte également son propre plafond de mode de comptabilisation, défini via l'API du projet ou l'assistant par tout membre disposant d'un accès en écriture à un projet déverrouillé. Le plafond ne rend jamais une exécution que plus sûre, jamais plus permissive : le mode effectif d'une exécution est le plus restrictif entre le mode que vous avez choisi et le plafond du projet. Ainsi, un projet plafonné à Simulation reste simulé même si vous lancez l'exécution en mode Réel.

Un [événement planifié](/fr/administration/scheduled-events/event-scheduler/#mode-décriture-erp) conserve son propre mode de comptabilisation : une planification définie sur Simulation s'exécute donc en simulation à chaque déclenchement.

Le mode se propage à tout ce que l'exécution touche. Un sous-workflow, une macro, ainsi qu'une étape **Run Model**, **Conditional Run Model** ou **Loop Model** héritent tous du mode de l'exécution parente, de même qu'une exécution que vous [reprenez](#suspendre-arrêter-et-reprendre) après un arrêt : une exécution simulée ne peut comptabiliser réellement nulle part en son sein.

:::caution
Les étapes de comptabilisation SAP, de pièce jointe SAP et de RFC SAP générique n'effectuent pas de test à blanc. En mode Simulation ou Désactivé, elles sont purement ignorées, car les indicateurs de test propres à SAP ouvrent tout de même une vraie connexion à SAP : ignorer l'étape est le seul moyen d'éviter qu'une exécution simulée n'atteigne SAP.
:::

:::note
Une étape de comptabilisation ERP individuelle porte également son propre paramètre Validate Only (intitulé Preview ou Test Only Mode sur certaines étapes), indépendant du mode de comptabilisation de l'exécution décrit ci-dessus. L'éditeur d'étape l'enregistre toujours explicitement. Une configuration d'étape écrite autrement (API REST, MCP ou import d'un bundle de workflow) qui omet totalement ce paramètre a désormais aussi pour valeur par défaut un aperçu plutôt qu'une comptabilisation réelle.
:::

## Autoriser le projet à comptabiliser

Une exécution de workflow comptabilise dans un ERP en tant que projet, et non en tant que la personne qui l'a lancée. Avant qu'une exécution puisse comptabiliser, le projet a besoin d'une autorisation pour chaque connexion et chaque environnement ERP utilisés par ses étapes de comptabilisation. Sans autorisation, l'étape échoue avec le message « This project isn't authorized to post to connection … », qui nomme la connexion et l'environnement. Les étapes **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** et **Call SAP RFC** n'en ont pas besoin.

Pour autoriser un projet, ouvrez sa page d'accueil et sélectionnez **Autorisations d'écriture ERP** sous **Écriture ERP**. Chaque ligne représente une connexion dans un environnement. Cochez **Autorisé** pour permettre au projet de comptabiliser à cet endroit, ou décochez-la pour l'en empêcher. **Autorisé par** et **Autorisé le** indiquent qui a autorisé en dernier et quand.

- Le bouton est affiché aux Architectes du projet et aux administrateurs de l'espace de travail, mais seul un Architecte peut modifier une autorisation, et uniquement tant que le projet est déverrouillé. Un administrateur de l'espace de travail qui n'est pas Architecte peut d'abord s'ajouter comme Architecte.
- Sélectionner une ligne pour autoriser ou effacer une autorisation ne recharge pas la liste : la position de défilement et le tri de colonne que vous avez choisi restent en place. La fenêtre peut être redimensionnée, et la remarque sur les projets publics s'affiche en entier.
- Pour autoriser une connexion, vous devez aussi disposer vous-même d'un accès en écriture à celle-ci : vous en êtes propriétaire, ou elle est partagée avec vous nommément ou via l'un de vos groupes de sécurité. Une connexion définie sur **Tous les membres de l'espace de travail** ne compte pas.
- Un projet défini sur **Tous les membres de l'espace de travail** est autorisé comme n'importe quel autre. Chaque membre en est Architecte ; tout membre disposant d'un accès en écriture à une connexion peut donc autoriser le projet pour celle-ci. Une fois autorisé, tout membre peut comptabiliser sur cette connexion depuis les workflows du projet, et la fenêtre l'indique au-dessus de la grille.
- Un projet copié, ou créé à partir d'une archive de projet, démarre sans aucune autorisation. Autorisez la copie avant qu'elle ne comptabilise.

## Suivre l'état d'une étape

Pendant l'exécution d'un workflow, chaque étape affiche une icône d'état indiquant où elle en est, ainsi que la durée écoulée depuis son démarrage. Survolez l'icône pour afficher le message correspondant.

| État | Signification |
|---|---|
| En attente | L'étape est en file d'attente et n'a pas encore démarré. |
| En cours | L'étape est en cours de traitement, et sa durée augmente au fil du temps. |
| Terminée | L'étape s'est terminée avec succès. |
| Avertissement | L'étape s'est terminée, mais a signalé un point à consulter dans le [journal du workflow](/fr/guides/workflows/viewing-workflow-log/). |
| Erreur | L'étape a échoué. Consultez [Gérer les erreurs d'étape](/fr/guides/workflows/managing-step-errors/). |
| Ignorée | L'étape a été passée : elle est désactivée, ou ses conditions d'exécution n'étaient pas remplies. Consultez [Ignorer des étapes dans un workflow](/fr/guides/workflows/skip-steps-in-a-workflow/). |
| Poursuivie | L'étape a échoué mais est configurée pour continuer malgré l'erreur ; le workflow a donc poursuivi. Consultez [Continuer malgré une erreur](/fr/guides/workflows/continue-on-error/). |
| Arrêtée | L'exécution a été arrêtée avant que l'étape puisse se terminer. |
| Abandonnée | L'exécution de l'étape a été interrompue ; elle ne se terminera donc jamais. Reprenez l'exécution, ou relancez le workflow. |

Une vue de workflow ouverte s'actualise d'elle-même au fil de l'exécution, de sorte que les états affichés restent à jour sans recharger la page.

### Étapes abandonnées

Une étape est marquée comme **abandonnée** lorsque ce qui l'exécutait a disparu en cours d'exécution, le plus souvent parce que quelqu'un a appuyé sur **Arrêter**, ou parce qu'une maintenance de la plateforme a interrompu l'exécution. La durée de l'étape cesse d'augmenter et l'infobulle d'état explique ce qui s'est passé.

Une étape abandonnée ne s'est pas terminée et n'a produit aucune sortie. Ce n'est pas une étape lente, et ce n'est pas un problème lié à vos données ou à votre configuration.

Pour reprendre le travail, vous pouvez soit [**Reprendre**](#suspendre-arrêter-et-reprendre) l'exécution (l'étape abandonnée s'exécute de nouveau), soit relancer tout le workflow. Les deux options sont sûres.

### Étapes interrompues

Si le serveur qui exécute une étape est perdu en cours d'exécution, PlaidCloud relance automatiquement l'étape lorsqu'il est sûr de la répéter : une étape qui remplace sa sortie aboutit au même résultat qu'une seule exécution propre, vous n'avez donc rien à vérifier.

Une étape qui ne peut pas être répétée en toute sécurité n'est pas relancée. Elle échoue une fois avec un message **interrompu**, car l'exécuter une seconde fois pourrait dupliquer ce que la première tentative a déjà écrit. Les étapes qui écrivent des sorties avec `{date}` dans le nom ou le chemin sont considérées comme non sûres à répéter, puisqu'une nouvelle exécution pourrait tomber à une date différente. Pour récupérer, vérifiez dans la cible de l'étape ce que la première tentative a écrit, nettoyez-la si nécessaire, puis [relancez l'étape](/fr/guides/workflows/running-one-step-in-a-workflow/) ou **Reprenez** l'exécution.

## Suspendre, arrêter et reprendre

Pendant qu'un workflow s'exécute, vous pouvez le **Suspendre** : les étapes en cours se terminent et les nouvelles étapes attendent. Vous pouvez aussi l'**Arrêter** : cela annule les étapes en file d'attente ainsi que tous les travaux d'import ou d'export encore en cours.

**Reprendre** relance une exécution suspendue, arrêtée ou en échec là où elle s'était interrompue, au lieu de repartir de zéro. Cette action est disponible dès que la dernière exécution d'un workflow s'est terminée dans un état suspendu, arrêté ou en erreur.

Ce que signifie « là où elle s'était interrompue » dépend du mode d'exécution du workflow :

| Exécution | À la reprise |
|---|---|
| Série | Redémarre à l'étape qui s'exécutait lorsque l'exécution s'est terminée, et continue à partir de là. Si cette étape se trouve dans un groupe, Reprendre relance l'ensemble du groupe de premier niveau qui la contient : les étapes du groupe déjà terminées avec succès sont laissées de côté, les autres s'exécutent, et l'exécution se poursuit après le groupe. |
| Parallèle | Relance chaque étape qui ne s'était pas encore terminée avec succès, et laisse de côté les étapes terminées. |
| Avancée (graphe) | Relance le nœud qui a échoué et tout ce qui attend encore après lui, et laisse de côté les nœuds terminés. |

Les étapes qui appellent un autre workflow (**Run Model**, **Conditional Run Model** et **Loop Model**) reprennent le workflow qu'elles appellent au lieu de le redémarrer, quel que soit le nombre de niveaux d'imbrication. Une étape de boucle reprend l'itération qui a été interrompue et saute les itérations déjà terminées.

Lorsque vous reprenez un workflow exécuté en tant qu'**enfant imbriqué** d'un autre (un workflow invoqué par une étape **Run Model** d'un parent), PlaidCloud propose **Reprendre depuis le début de la chaîne**. Reprendre l'enfant seul ne peut pas poursuivre l'orchestration du parent ; cette option reprend donc le parent de premier niveau, la racine de la chaîne, et poursuit toute la chaîne là où elle s'était arrêtée. Reprendre un workflow de premier niveau reste inchangé. Le début de la chaîne est résolu au sein du même projet : une chaîne qui traverse un autre projet reprend depuis le début de la partie située dans le projet.

Reprendre poursuit toujours l'exécution **d'origine**. Cette action relance chaque étape de cette exécution qui ne s'est pas terminée avec succès (une étape en échec ou abandonnée est relancée, et non considérée comme terminée), et relancer une étape individuelle de son côté entre-temps ne change pas ce que Reprendre relancera ensuite.

Une exécution reprise est enregistrée comme une **nouvelle exécution** dans l'historique du workflow, ne contenant que les étapes qu'elle a relancées. L'exécution d'origine conserve sa propre entrée d'historique.

:::note
Une étape de boucle fait correspondre ses itérations terminées d'après les valeurs de leurs variables. Si les données sur lesquelles la boucle itère ont changé entre l'exécution d'origine et la reprise, les itérations qu'elle ne parvient plus à faire correspondre sont relancées au lieu d'être ignorées.
:::
