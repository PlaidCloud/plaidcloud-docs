---
title: Exécuter un workflow
description: Exécutez un workflow PlaidCloud manuellement ou à la demande, suivez l'état de chaque étape, puis suspendez, arrêtez ou reprenez une exécution là où elle s'est interrompue.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Vous pouvez lancer l'exécution complète d'un workflow en cliquant sur l'icône d'exécution dans la hiérarchie **Workflows**, ou en sélectionnant **Run All** dans le menu **Actions** d'un workflow donné.



Vous pouvez également cliquer sur le bouton **Toggle Start/Stop** en haut de la table des workflows. Ce bouton arrête un workflow en cours d'exécution ou démarre un workflow.

Si vous cliquez sur **Exécuter** pour un workflow déjà en cours d'exécution, PlaidCloud vous l'indique au lieu de lancer une seconde exécution.

## Choisir un mode de comptabilisation

Chaque exécution porte un mode de comptabilisation ERP. Pour en choisir un dans PlaidCloud, utilisez **Exécuter avec le mode d'écriture** dans le menu contextuel d'un workflow, ou le bouton de mode d'exécution sur le canevas du workflow. Les commandes **Démarrer le workflow** et **Exécuter le workflow** demandent le mode Live, toujours soumis au plafond du projet décrit ci-dessous. Vous pouvez aussi choisir le mode au démarrage d'une exécution via l'API d'exécution ou l'assistant.

| Mode | Ce qui se passe |
|---|---|
| Live | Les étapes de comptabilisation comptabilisent exactement comme elles l'ont toujours fait. C'est le mode par défaut. |
| Simulate | Chaque étape de comptabilisation ERP construit et valide exactement ce qu'elle comptabiliserait, puis ne valide rien et ne contacte jamais l'ERP. Les écritures qui auraient été comptabilisées sont consignées dans l'[historique des comptabilisations ERP](/fr/guides/connections/erp-post-history/), marquées comme simulées, afin que vous puissiez les examiner avant une exécution en mode Live. |
| Off | Les étapes de comptabilisation sont ignorées complètement. |

Un projet possède également son propre plafond de mode de comptabilisation, défini via l'API de projet ou l'assistant par tout membre disposant d'un accès en écriture à un projet déverrouillé. Le plafond ne peut que rendre une exécution plus sûre, jamais plus permissive : le mode effectif d'une exécution est le plus restrictif entre le mode que vous avez choisi et le plafond du projet. Un projet plafonné à Simulate reste donc simulé, même si vous démarrez l'exécution en mode Live.

Un [événement planifié](/fr/administration/scheduled-events/event-scheduler/#mode-décriture-erp) conserve son propre mode de comptabilisation : une planification définie sur Simulate s'exécute donc en simulation à chaque déclenchement.

Le mode se propage à tout ce que l'exécution touche. Un sous-workflow, une macro, ainsi que les étapes **Run Model**, **Conditional Run Model** et **Loop Model** héritent tous du mode de l'exécution parente, tout comme une exécution que vous [reprenez](#suspendre-arrêter-et-reprendre) après un arrêt : une exécution simulée ne peut comptabiliser réellement nulle part en son sein.

:::caution
Les étapes de comptabilisation SAP, de pièce jointe SAP et de RFC SAP générique n'exécutent pas de simulation à blanc. Sous Simulate ou Off, elles sont purement et simplement ignorées, car les indicateurs de test propres à SAP ouvrent tout de même une connexion réelle à SAP : ignorer l'étape est le seul moyen pour qu'une exécution simulée n'atteigne jamais SAP.
:::

:::note
Une étape de comptabilisation ERP possède aussi son propre paramètre Validate Only (intitulé Preview ou Test Only Mode sur certaines étapes), indépendant du mode de comptabilisation de l'exécution décrit ci-dessus. L'éditeur d'étape l'enregistre toujours explicitement. Une configuration d'étape écrite autrement (API REST, MCP ou importation d'un bundle de workflow) qui omet complètement ce paramètre prend désormais aussi par défaut un aperçu plutôt qu'une comptabilisation réelle.
:::

## Autoriser le projet à comptabiliser

Une exécution de workflow comptabilise dans un ERP en tant que projet, et non en tant que la personne qui l'a lancée. Avant qu'une exécution puisse comptabiliser, le projet a besoin d'une autorisation pour chaque connexion ERP et chaque environnement utilisés par ses étapes de comptabilisation. Sans autorisation, l'étape échoue avec le message « This project isn't authorized to post to connection … », qui nomme la connexion et l'environnement. Les étapes **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** et **Call SAP RFC** n'en ont pas besoin.

Pour autoriser un projet, ouvrez sa page d'accueil et sélectionnez **Autorisations d'écriture ERP** sous **Écriture ERP**. Chaque ligne correspond à une connexion dans un environnement. Cochez **Autorisé** pour permettre au projet de comptabiliser à cet endroit, ou décochez-le pour l'en empêcher. **Autorisé par** et **Autorisé le** indiquent qui a autorisé en dernier et quand.

- Le bouton est affiché aux Architectes du projet et aux administrateurs de l'espace de travail, mais seul un Architecte peut modifier une autorisation, et uniquement tant que le projet est déverrouillé. Un administrateur de l'espace de travail qui n'est pas Architecte peut d'abord s'ajouter lui-même comme Architecte.
- Sélectionner une ligne pour autoriser ou retirer une autorisation ne recharge pas la liste : la position de défilement et le tri de colonne que vous avez choisi restent en place. La fenêtre peut être redimensionnée, et la remarque sur les projets publics s'affiche en entier.
- Pour autoriser une connexion, vous devez également disposer vous-même d'un accès en écriture à celle-ci : vous en êtes propriétaire, ou elle est partagée avec vous nommément ou via l'un de vos groupes de sécurité. Une connexion définie sur **Tous les membres de l'espace de travail** ne compte pas.
- Un projet défini sur **Tous les membres de l'espace de travail** s'autorise comme n'importe quel autre. Chaque membre en est Architecte ; tout membre disposant d'un accès en écriture à une connexion peut donc autoriser le projet pour celle-ci. Une fois le projet autorisé, n'importe quel membre peut comptabiliser sur cette connexion depuis les workflows du projet, et la fenêtre l'indique au-dessus de la grille.
- Un projet copié, ou créé à partir d'une archive de projet, démarre sans aucune autorisation. Autorisez la copie avant qu'elle ne comptabilise.

## Suivre l'état d'une étape

Pendant l'exécution d'un workflow, chaque étape porte une icône d'état indiquant où elle en est, ainsi que depuis combien de temps elle s'exécute. Survolez l'icône pour afficher le message qui s'y rattache.

| État | Signification |
|---|---|
| En attente | L'étape est en file d'attente et n'a pas encore démarré. |
| En cours d'exécution | L'étape est en cours de traitement, et sa durée s'incrémente au fil du temps. |
| Terminée | L'étape s'est terminée avec succès. |
| Avertissement | L'étape s'est terminée, mais a signalé un point qui mérite d'être lu dans le [journal du workflow](/fr/guides/workflows/viewing-workflow-log/). |
| Erreur | L'étape a échoué. Consultez [Gérer les erreurs d'étape](/fr/guides/workflows/managing-step-errors/). |
| Ignorée | L'étape a été passée : elle est désactivée, ou ses conditions d'exécution n'étaient pas remplies. Consultez [Ignorer des étapes dans un workflow](/fr/guides/workflows/skip-steps-in-a-workflow/). |
| Poursuivie | L'étape a échoué mais est configurée pour continuer en cas d'erreur ; le workflow a donc poursuivi son cours. Consultez [Continuer en cas d'erreur](/fr/guides/workflows/continue-on-error/). |
| Arrêtée | L'exécution a été arrêtée avant que l'étape puisse se terminer. |
| Abandonnée | L'exécution de l'étape a été interrompue ; elle ne se terminera donc jamais. Reprenez l'exécution, ou réexécutez le workflow. |

Une vue de workflow ouverte s'actualise d'elle-même au fil de l'exécution, de sorte que les états affichés restent à jour sans recharger la page.

### Étapes abandonnées

Une étape est marquée comme **abandonnée** lorsque ce qui l'exécutait a disparu en cours d'exécution, le plus souvent parce que quelqu'un a appuyé sur **Arrêter**, ou parce qu'une maintenance de la plateforme a interrompu l'exécution. La durée de l'étape cesse de croître et l'infobulle d'état explique ce qui s'est passé.

Une étape abandonnée ne s'est pas terminée et n'a produit aucune sortie. Ce n'est pas une étape lente, et ce n'est pas un problème lié à vos données ou à votre configuration.

Pour reprendre le travail, vous pouvez soit [**Reprendre**](#suspendre-arrêter-et-reprendre) l'exécution (l'étape abandonnée s'exécute à nouveau), soit réexécuter l'ensemble du workflow. Les deux options sont sans risque.

### Étapes interrompues

Si le serveur qui exécute une étape est perdu en cours d'exécution, PlaidCloud réexécute automatiquement l'étape lorsqu'il est sûr de la répéter : une étape qui remplace sa sortie aboutit au même résultat qu'une seule exécution propre, vous n'avez donc rien à vérifier.

Une étape qui ne peut pas être répétée en toute sécurité n'est pas réexécutée. Elle échoue une seule fois avec un message **interrompu**, car l'exécuter une seconde fois pourrait dupliquer ce que la première tentative a déjà écrit. Les étapes qui écrivent des sorties dont le nom ou le chemin contient `{date}` sont considérées comme non sûres à répéter, car une nouvelle exécution pourrait tomber à une date différente. Pour récupérer, vérifiez dans la cible de l'étape ce que la première tentative a écrit, nettoyez-la si nécessaire, puis [réexécutez l'étape](/fr/guides/workflows/running-one-step-in-a-workflow/) ou **Reprendre** l'exécution.

### Étapes qui ne démarrent jamais

Si aucun worker ne prend en charge le job d'une étape d'importation ou de dimension dans un délai d'environ 40 minutes, l'étape échoue au lieu d'afficher **En cours d'exécution** jusqu'au délai d'expiration de 24 heures. Si un worker a démarré le job puis a disparu, l'étape échoue également, avec un message indiquant que le worker s'est arrêté. Les deux messages indiquent « Use Run from here to retry. » (**Exécuter à partir d'ici** pour réessayer).

## Suspendre, arrêter et reprendre

Pendant l'exécution d'un workflow, vous pouvez le **Suspendre**, de sorte que les étapes en cours se terminent et que les nouvelles étapes attendent, ou l'**Arrêter**, ce qui annule les étapes en file d'attente ainsi que tous les jobs d'importation ou d'exportation encore en cours. Les étapes d'importation et de dimension encore en file d'attente sont annulées proprement, afin de ne pas retarder les importations et chargements de dimensions suivants dans l'espace de travail.

**Reprendre** relance une exécution suspendue, arrêtée ou en échec là où elle s'était interrompue, au lieu de repartir de zéro. Cette commande est disponible dès que la dernière exécution d'un workflow s'est terminée dans un état suspendu, arrêté ou en erreur.

Ce que signifie « là où elle s'était interrompue » dépend de la façon dont le workflow s'exécute :

| Exécution | À la reprise |
|---|---|
| Série | Redémarre à l'étape qui s'exécutait à la fin de l'exécution, puis continue à partir de là. Si cette étape se trouve dans un groupe, la reprise reprend l'ensemble du groupe de premier niveau qui la contient : les étapes du groupe déjà terminées avec succès sont laissées de côté, les autres s'exécutent, et l'exécution se poursuit après le groupe. |
| Parallèle | Réexécute chaque étape qui ne s'était pas encore terminée avec succès, et laisse de côté les étapes terminées. |
| Avancée (graphe) | Réexécute le nœud qui a échoué et tout ce qui l'attend encore, et laisse de côté les nœuds terminés. |

Les étapes qui appellent un autre workflow (**Run Model**, **Conditional Run Model** et **Loop Model**) reprennent le workflow qu'elles appellent au lieu de le redémarrer, quel que soit le nombre de niveaux d'imbrication. Une étape de boucle reprend l'itération qui a été interrompue et ignore les itérations déjà terminées.

Lorsque vous reprenez un workflow exécuté en tant qu'**enfant imbriqué** d'un autre (un workflow invoqué par une étape **Run Model** d'un parent), PlaidCloud propose **Reprendre depuis le début de la chaîne**. Reprendre l'enfant seul ne peut pas poursuivre l'orchestration du parent ; cette option reprend donc le parent de premier niveau, c'est-à-dire la racine de la chaîne, et poursuit toute la chaîne là où elle s'était arrêtée. La reprise d'un workflow de premier niveau reste inchangée. Le début de la chaîne est résolu au sein du même projet : une chaîne qui traverse un autre projet reprend depuis le début de la partie située dans le projet.

La reprise poursuit toujours l'exécution **d'origine**. Elle réexécute chaque étape de cette exécution qui ne s'est pas terminée avec succès (une étape en échec ou abandonnée est réexécutée, et non considérée comme terminée), et réexécuter entre-temps une étape individuelle de son côté ne change pas ce que la reprise prendra en charge ensuite.

Une exécution reprise est consignée comme une **nouvelle exécution** dans l'historique d'exécution du workflow, ne contenant que les étapes qu'elle a réexécutées. L'exécution d'origine conserve sa propre entrée d'historique.

:::note
Une étape de boucle fait correspondre ses itérations terminées d'après leurs valeurs de variables. Si les données sur lesquelles la boucle itère ont changé entre l'exécution d'origine et la reprise, les itérations qu'elle ne peut plus faire correspondre sont réexécutées plutôt qu'ignorées.
:::
