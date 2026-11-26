---
title: Exécuter un workflow
description: Exécutez un workflow PlaidCloud manuellement ou à la demande, suivez l'état de chaque étape, puis suspendez, arrêtez ou reprenez une exécution là où elle s'était interrompue.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Vous pouvez lancer l'exécution complète d'un workflow en cliquant sur l'icône d'exécution dans la hiérarchie **Workflows**, ou en sélectionnant **Run All** dans le menu **Actions** d'un workflow donné.



Vous pouvez également cliquer sur le bouton **Toggle Start/Stop** en haut de la table des workflows. Ce bouton à bascule arrête un workflow en cours d'exécution ou démarre un workflow.

Si vous cliquez sur **Exécuter** pour un workflow déjà en cours d'exécution, PlaidCloud vous en informe au lieu de lancer une seconde exécution.

## Choisir un mode d'écriture

Chaque exécution porte un mode d'écriture ERP. Pour en choisir un dans PlaidCloud, utilisez **Exécuter avec le mode d'écriture** dans le menu contextuel d'un workflow, ou le bouton de mode d'exécution sur le canevas du workflow. Un simple **Démarrer le workflow** ou **Exécuter le workflow** demande le mode Réel, toujours soumis au plafond du projet décrit plus bas. Vous pouvez aussi choisir le mode au lancement d'une exécution via l'API d'exécution ou l'assistant.

| Mode | Ce qui se passe |
|---|---|
| Réel | Les étapes d'écriture comptabilisent exactement comme elles l'ont toujours fait. C'est le mode par défaut. |
| Simulation | Chaque étape d'écriture ERP construit et valide exactement ce qu'elle comptabiliserait, puis ne valide rien et ne contacte jamais l'ERP. Les écritures qui auraient été comptabilisées sont enregistrées pour que vous puissiez les examiner avant d'exécuter en mode Réel : celles d'une étape **Comptabiliser des documents** dans le [Registre des écritures](/fr/guides/connections/posting-register/) sous **Serait comptabilisé** (consultez [Comptabiliser des documents dans les systèmes ERP](/fr/guides/connections/post-documents/)), celles de l'étape de comptabilisation propre à un système dans l'[historique des écritures ERP](/fr/guides/connections/erp-post-history/), marquées comme simulées. |
| Désactivé | Les étapes d'écriture sont ignorées en totalité. |

Un projet porte également son propre plafond de mode d'écriture, défini via l'API du projet ou l'assistant par tout membre disposant d'un accès en écriture à un projet déverrouillé. Le plafond ne peut que rendre une exécution plus sûre, jamais plus permissive : le mode effectif d'une exécution est le plus restrictif entre le mode que vous avez choisi et le plafond du projet. Un projet plafonné à Simulation reste donc simulé, même si vous lancez l'exécution en mode Réel.

Un [événement planifié](/fr/administration/scheduled-events/event-scheduler/#mode-décriture-erp) conserve son propre mode d'écriture : une planification réglée sur Simulation s'exécute donc en simulation à chaque déclenchement.

Le mode se propage à tout ce que l'exécution touche. Un sous-workflow, une macro et une étape **Run Model**, **Conditional Run Model** ou **Loop Model** héritent tous du mode de l'exécution parente, tout comme une exécution que vous [reprenez](#suspendre-arrêter-et-reprendre) après un arrêt : une exécution simulée ne peut comptabiliser réellement nulle part à l'intérieur d'elle-même.

:::caution
Les étapes d'écriture SAP, de pièce jointe SAP et d'appel RFC SAP générique n'effectuent pas de test à blanc. En mode Simulation ou Désactivé, elles sont purement ignorées, car les indicateurs de test propres à SAP ouvrent tout de même une vraie connexion à SAP : ignorer l'étape est le seul moyen de garantir qu'une exécution simulée n'atteint jamais SAP.
:::

:::note
Chaque étape d'écriture ERP porte également son propre paramètre Validate Only (intitulé Aperçu ou Test Only Mode sur certaines étapes), indépendant du mode d'écriture de l'exécution décrit ci-dessus. L'éditeur d'étape l'enregistre toujours explicitement. Une configuration d'étape rédigée autrement (API REST, MCP ou import d'un bundle de workflow) qui omet entièrement ce paramètre prend désormais aussi par défaut un aperçu plutôt qu'une écriture réelle. L'étape **Comptabiliser des documents** n'a pas de tel paramètre : le mode de l'exécution et le mode propre à son système décident si elle comptabilise : consultez [Comptabiliser des documents dans les systèmes ERP](/fr/guides/connections/post-documents/).
:::

## Autoriser le projet à comptabiliser

Une exécution de workflow comptabilise dans un ERP en tant que projet, et non en tant que personne qui l'a lancée. Avant qu'une exécution puisse comptabiliser, le projet a besoin d'une autorisation pour chaque connexion et chaque environnement ERP utilisés par ses étapes d'écriture. Sans autorisation, l'étape échoue avec le message « This project isn't authorized to post to connection … », qui nomme la connexion et l'environnement. Les étapes **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** et **Call SAP RFC** n'en ont pas besoin.

Pour autoriser un projet, ouvrez sa page d'accueil et sélectionnez **Autorisations d'écriture ERP** sous **Écriture ERP**. Chaque ligne correspond à une connexion dans un environnement. Cochez **Autorisé** pour permettre au projet de comptabiliser à cet endroit, ou décochez-le pour l'en empêcher. **Autorisé par** et **Autorisé le** indiquent qui a autorisé la connexion en dernier et quand.

- Le bouton est affiché aux Architectes du projet et aux administrateurs de l'espace de travail, mais seul un Architecte peut modifier une autorisation, et seulement tant que le projet est déverrouillé. Un administrateur de l'espace de travail qui n'est pas Architecte peut d'abord s'ajouter lui-même comme Architecte.
- Sélectionner une ligne pour autoriser ou retirer une autorisation ne recharge pas la liste : la position de défilement et le tri de colonne que vous avez choisi sont conservés. La fenêtre peut être redimensionnée, et la remarque sur les projets publics s'affiche en entier.
- Pour autoriser une connexion, vous devez aussi disposer vous-même d'un accès en écriture à celle-ci : vous en êtes propriétaire, ou elle est partagée avec vous nommément ou via l'un de vos groupes de sécurité. Une connexion définie sur **Tous les membres de l'espace de travail** n'est pas prise en compte.
- Un projet défini sur **Tous les membres de l'espace de travail** est autorisé comme n'importe quel autre. Chaque membre en est Architecte : tout membre disposant d'un accès en écriture à une connexion peut donc autoriser le projet à l'utiliser. Une fois le projet autorisé, n'importe quel membre peut comptabiliser sur cette connexion à partir des workflows du projet, et la fenêtre l'indique au-dessus de la grille.
- Une nouvelle copie privée, créée avec des données de table ou des membres de dimension, conserve les autorisations de la source que vous pourriez accorder vous-même, et arrive en mode Simulation si la source était en mode Réel. Voir [Autorisations d'écriture ERP dans la copie](/fr/guides/projects/managing-projects/#autorisations-décriture-erp-dans-la-copie). Toute autre copie, ou un projet créé à partir d'une archive de projet, démarre sans aucune autorisation. Autorisez-le avant qu'il comptabilise.

## Suivre l'état d'une étape

Pendant l'exécution d'un workflow, chaque étape affiche une icône d'état indiquant où elle en est, ainsi que depuis combien de temps elle s'exécute. Survolez l'icône pour afficher le message correspondant.

| État | Signification |
|---|---|
| En attente | L'étape est en file d'attente et n'a pas encore démarré. |
| En cours | L'étape est en train de s'exécuter et sa durée augmente au fil du temps. |
| Terminée | L'étape s'est terminée avec succès. |
| Avertissement | L'étape s'est terminée, mais a signalé un point qui mérite d'être lu dans le [journal du workflow](/fr/guides/workflows/viewing-workflow-log/). |
| Erreur | L'étape a échoué. Voir [Gérer les erreurs d'étape](/fr/guides/workflows/managing-step-errors/). |
| Ignorée | L'étape a été passée : elle est désactivée, ou ses conditions d'exécution n'étaient pas remplies. Voir [Ignorer des étapes dans un workflow](/fr/guides/workflows/skip-steps-in-a-workflow/). |
| Poursuivie | L'étape a échoué mais est configurée pour continuer en cas d'erreur, de sorte que le workflow a poursuivi. Voir [Continuer en cas d'erreur](/fr/guides/workflows/continue-on-error/). |
| Arrêtée | L'exécution a été arrêtée avant que l'étape puisse se terminer. |
| Abandonnée | L'exécution de l'étape a été interrompue et ne se terminera jamais. Reprenez l'exécution ou relancez le workflow. |

Une vue de workflow ouverte s'actualise d'elle-même à mesure que l'exécution progresse : les états affichés restent à jour sans recharger la page.

### Étapes abandonnées

Une étape est marquée **abandonnée** lorsque ce qui l'exécutait a disparu en cours d'exécution, le plus souvent parce que quelqu'un a appuyé sur **Arrêter**, ou parce qu'une maintenance de la plateforme a interrompu l'exécution. La durée de l'étape cesse d'augmenter et l'infobulle d'état explique ce qui s'est passé.

Une étape abandonnée ne s'est pas terminée et n'a produit aucune sortie. Ce n'est pas une étape lente, et ce n'est pas un problème lié à vos données ou à votre configuration.

Pour reprendre le travail, vous pouvez soit [**Reprendre**](#suspendre-arrêter-et-reprendre) l'exécution, auquel cas l'étape abandonnée est exécutée de nouveau, soit relancer le workflow entier. Les deux options sont sûres.

### Étapes interrompues

Si le serveur qui exécute une étape est perdu en cours d'exécution, PlaidCloud réexécute automatiquement l'étape lorsqu'il est sûr de la répéter : une étape qui remplace sa sortie aboutit au même résultat qu'une seule exécution propre, et vous n'avez donc rien à vérifier. Le journal de l'étape affiche un avertissement à l'endroit où commence la seconde tentative : « Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start. »

Une étape qui ne peut pas être répétée sans risque n'est pas réexécutée. Elle échoue une seule fois avec un message **Interrompu**, car l'exécuter une seconde fois pourrait dupliquer ce que la première tentative a déjà écrit. Les étapes qui écrivent des sorties dont le nom ou le chemin contient `{date}` ou `{date_iso}` sont considérées comme non sûres à répéter, puisqu'une réexécution pourrait tomber à une autre date. Pour récupérer, vérifiez dans la cible de l'étape ce que la première tentative a écrit, nettoyez-la si nécessaire, puis [réexécutez l'étape](/fr/guides/workflows/running-one-step-in-a-workflow/) ou **Reprenez** l'exécution.

### Étapes qui ne démarrent jamais

Pendant qu'une étape attend un worker, son message d'état indique « Waiting for a worker… N min. No import worker has picked this step up yet. » (le type de worker correspond à l'étape, par exemple import ou export). Le message disparaît dès que le travail démarre.

Si le job d'une étape ne peut jamais démarrer, l'étape échoue en indiquant la raison au lieu d'attendre indéfiniment :

| Cause | Échoue après environ |
|---|---|
| Aucun worker ne prend en charge le job d'une étape d'importation ou de dimension | 40 minutes |
| Le pod de l'étape reste bloqué à l'état Pending | 20 minutes |
| L'image de l'étape ne peut pas être récupérée | 5 minutes |
| Aucun pod n'est créé pour l'étape | 20 minutes |
| Aucun runner ne prend en charge une synchronisation de connecteur (Singer) | 30 minutes |

Le message de synchronisation de connecteur nomme la synchronisation. Si un worker a démarré le job puis a disparu, l'étape échoue également, avec un message indiquant que le worker s'est arrêté. Les messages d'importation et de dimension indiquent « Use Run from here to retry. »

### Exécutions qui ne répondent plus

Une exécution ne reste jamais **En cours d'exécution** une fois que le travail qui la sous-tend a disparu. Si le serveur qui exécute le workflow est perdu, l'exécution se termine en échec. Une exécution peut durer au plus 12 heures : une exécution encore en cours à ce moment-là échoue avec le message « Run failed: still running at the 12-hour limit. Re-run the workflow. »

## Run Insight

Run Insight montre où une exécution d'un workflow a passé son temps, et quelles étapes ont pris plus ou moins de temps que d'habitude. Il juge chaque étape par rapport à ses propres exécutions récentes, de sorte qu'une étape toujours lente n'est pas signalée.

### Ouvrir Run Insight

- Sur le canevas, cliquez sur **Historique** dans la barre d'outils. Voir [Concepteur visuel de workflow](/fr/guides/workflows/advanced-workflows/).
- Dans l'onglet **Workflows**, sélectionnez un workflow et choisissez **Run Insight** dans le menu **Actions** ou dans le menu contextuel.
- Sur l'Accueil, choisissez **Ouvrir la dernière exécution** sur une carte de workflow.
- Dans la boîte de dialogue de l'historique des exécutions, choisissez une exécution dans la table **Exécutions** avec **Ouvrir dans Insight**, ou ouvrez sa ligne.
- Dans un message Weave intégré à l'application concernant une exécution lente, cliquez sur **Ouvrir l'exécution**. Voir [Être prévenu à la fin d'une exécution](/fr/guides/ai-assistant/weave-findings/#être-prévenu-à-la-fin-dune-exécution).

La boîte de dialogue s'intitule **Historique des exécutions** — nom du workflow. Son commutateur **Insight** | **Exécutions** bascule entre cette vue et la table des exécutions passées. L'historique d'exécution d'une étape, ouvert depuis l'Inspecteur, n'affiche que la table.

### Lire le titre et la liste d'attention

Le titre donne le résultat de l'exécution en une ligne : **Durée :** *durée*, **En cours depuis** *durée* tant qu'elle s'exécute, **Arrêté après** *durée* pour une dernière exécution arrêtée, ou **Échec dans** *workflow*, le workflow où elle a échoué. Une phrase en dessous dit ce qui ressort, comme les étapes plus lentes que d'habitude, le temps passé à attendre, ou le fait que chaque étape ayant un historique s'est exécutée dans sa plage habituelle. En dessous viennent l'heure de début, le nombre de workflows et d'étapes et, lorsque l'historique de certaines étapes est trop court pour être jugé, leur nombre. Lorsque quelque chose mérite un coup d'œil, *N* **à examiner** apparaît à côté du titre.

Une bande des exécutions récentes se trouve à côté du titre, avec une légende au-dessus. Chaque barre est une exécution, aussi haute que sa durée, et le jour n'est indiqué que là où il change. Cliquez sur une exécution de la bande pour l'ouvrir. Un chapeau rouge et un ✕ marquent une exécution échouée, et un contour en pointillés marque une exécution qui a exécuté moins d'étapes que la plupart des exécutions récentes, car elle ne peut pas être comparée à une exécution complète.

**Points d'attention** liste, dans cet ordre, d'abord les échecs, puis le temps au-delà de l'habituel, puis l'attente. Chaque élément est une carte avec son nom, le temps perdu ou **Échec**, son emplacement, et une barre de son temps où le gris est dans l'habituel et l'ambre au-delà, et la barre d'un échec est rouge. Une étape enregistrée depuis sa dernière exécution porte une étiquette **Enregistré le** *date*. Cliquez sur une carte pour la sélectionner dans la vue ; la carte sélectionnée est mise en évidence.

### Flux, chronologie et table

L'en-tête au-dessus de la vue contient le nom du workflow, puis **Comparer à**, puis **Vue**, dont les boutons **Flux**, **Chronologie** et **Table** choisissent la vue, et le bouton Actualiser à droite.

| Vue | Ce qu'elle montre |
|---|---|
| **Flux** | Des blocs dont la hauteur est le temps. L'ambre est le temps au-delà de l'habituel d'une étape. Un bloc non ouvert qui contient un échec affiche ✕ et un contour rouge. Un bloc échoué ou sélectionné trop court pour être nommé est dessiné plus haut, et la légende indique qu'il n'est alors pas à l'échelle. Lorsqu'une étape a appelé d'autres workflows, une tranche **Surcoût d'appel** est le temps propre de l'étape en dehors de ces workflows. Lorsqu'aucune étape ne s'exécutait, une tranche **En attente** montre l'écart ; un workflow exécuté en parallèle n'en dessine pas. |
| **Chronologie** | L'heure de l'horloge depuis le début de l'exécution. Un contour en pointillés indique la durée du bloc dans l'exécution comparée. |
| **Table** | Tout dans l'ordre des appels, avec les colonnes **Nom**, **Cette exécution**, **Habituellement**, **Supplément**, **Exécution comparée** et **Statut**. |

Un workflow qui a appelé d'autres workflows les affiche à l'intérieur de lui. Double-cliquez sur un bloc de workflow, ou choisissez **Zoom avant**, pour travailler à l'intérieur, et utilisez le fil d'Ariane au-dessus de la vue pour revenir. Lorsque plusieurs étapes dans les temps sont côte à côte, **Flux** les replie en un seul bloc *N* **dans les temps** ; cliquez dessus, ou cliquez sur **Afficher les** *nombre* **blocs** à droite du fil d'Ariane, pour les ouvrir ; le nombre est celui de tous les blocs de la vue. **Replier les blocs dans les temps** les replie de nouveau, et le bouton n'apparaît que lorsque quelque chose peut se replier.

Sélectionnez un bloc pour voir son panneau de détail. Il affiche le nom et l'emplacement du bloc, une pastille de statut avec l'une des marques ci-dessous, et des lignes pour ce qui s'applique parmi **Cette exécution**, **Habituellement**, **Historique**, **Au-delà de l'habituel** et **Exécution comparée**. Une courbe de tendance suit : pour le workflow propre à l'exécution, ses dernières exécutions complètes, avec cette exécution en point lorsqu'elle s'est terminée ; pour une étape ayant une plage habituelle, cette plage sous forme de bande avec cette exécution en point. Des notes expliquent la marque, et les boutons sont **Afficher dans son workflow**, **Afficher ses étapes** ou **Zoom avant**, **Ouvrir le workflow** et **Afficher le journal d'exécution**. **Ouvrir le workflow** ouvre le workflow sur le canevas et **Afficher le journal d'exécution** ouvre son [journal](/fr/guides/workflows/viewing-workflow-log/).

### Ce que signifient les marques

| Marque | Signification |
|---|---|
| **Échec** | Une étape s'est terminée par une erreur. Le panneau affiche son message, sauf si votre rôle ne peut pas voir le nom de l'étape. |
| **Plus lent que d'habitude** | L'étape a pris plus de temps que sa plage habituelle. |
| **Lent sur toute la durée** | Chaque étape du workflow a été à peu près aussi lente, ce qui désigne quelque chose que tout le workflow partage plutôt qu'une seule étape. Ses étapes affichent **Part d'un ralentissement général**. |
| **Avec étapes lentes** | Un workflow avec des **Étapes lentes à l'intérieur**. |
| **Dans les temps** | L'étape s'est exécutée dans sa plage habituelle. |
| **Plus rapide** | L'étape s'est exécutée plus vite que sa plage habituelle. |
| **Historique insuffisant** | L'étape ne s'est pas exécutée assez souvent pour avoir une plage habituelle, elle n'est donc pas jugée. |
| **Erreur, poursuivie** | L'étape a échoué mais est configurée pour [poursuivre en cas d'erreur](/fr/guides/workflows/continue-on-error/). |
| **Ignoré** | L'étape a été sautée. |
| **En cours d'exécution** | L'étape n'est pas terminée. |

Une étape dont les exécutions récentes étaient déjà lentes ou varient beaucoup peut ne pas être signalée. Une exécution de fin de période, comparée à des jours ordinaires, peut apparaître plus lente sur toute la durée. Une ancienne exécution arrêtée apparaît comme une exécution courte, pas comme arrêtée.

Le panneau peut aussi expliquer une marque. **En attente** est le temps pendant lequel aucune étape ne s'exécutait, donc aucune étape n'en est responsable. Sur une étape plus lente que d'habitude, **Lignes écrites** compare sa sortie à son compte habituel, et est omis lorsque la sécurité au niveau des lignes filtre ce que vous pouvez lire, et **Enregistré depuis sa dernière exécution** indique que l'étape a été enregistrée après son exécution précédente et avant le début de celle-ci ; l'enregistrement montre une sauvegarde, pas ce qui a changé. **Travail différent** compte les étapes qui ne se sont pas exécutées et les étapes qui se sont exécutées sans historique, mesurées par rapport à l'historique de chaque étape ou, lorsque vous comparez avec une autre exécution, par rapport à cette exécution. **Exécuté en parallèle** signifie que les parties du workflow se sont exécutées en même temps, de sorte que leurs durées s'additionnent à plus que l'horloge. **Appelant incertain** signifie que l'historique ne peut pas montrer quelle étape a appelé un workflow. **Nom masqué** marque une étape ou un workflow dont votre rôle ne peut pas voir le nom, affiché comme **Étape masquée** ou **Workflow masqué**.

### Comparer à

**Comparer à** définit ce par rapport à quoi une exécution est mesurée. Son bouton de menu affiche le choix : **Habituel**, **Habituel + exécution précédente** ou **Habituel + exécution du** suivi de l'heure de début de l'exécution choisie. **Habituel** utilise les exécutions récentes de chaque étape. **Habituel + exécution précédente** et **Habituel + une exécution choisie** ajoutent aussi le temps de cette exécution pour chaque étape, que la **Chronologie** contourne et que la **Table** affiche sous **Exécution comparée**. **Habituel + une exécution choisie** ouvre une liste des exécutions récentes où choisir.

### Un workflow à l'intérieur d'une exécution plus grande

Lorsque vous ouvrez un workflow qu'un autre workflow a appelé, Insight n'affiche que la part de l'exécution qui revient à ce workflow. **Ouvrir toute l'exécution** fait passer la même boîte de dialogue au workflow qui a démarré l'exécution.

### Exécutions en cours

Une exécution encore en cours est relue toutes les 30 secondes tant que la boîte de dialogue est visible. Votre zoom, votre sélection et votre vue restent inchangés. Quitter Insight pour **Exécutions** arrête les mises à jour, et revenir à Insight relit l'exécution et les reprend. Le bouton Actualiser, les flèches circulaires à droite de l'en-tête, recharge l'exécution depuis zéro, réinitialise le zoom et la sélection, et replie de nouveau les blocs dans les temps.

### Pour les assistants IA et l'API REST

Le même profil est disponible en dehors de la boîte de dialogue :

- REST : `GET /rest/v1/analyze/workflow/run-insight` avec `project_id` et `workflow_id`. `run_id` choisit l'exécution (la dernière si omis), et `baseline` vaut `typical`, `previous` ou `run:<id>`.
- MCP : `workflow_describe` avec `include=['run_insight']`, et `run_id` et `baseline` facultatifs.

Chaque workflow et chaque étape revient avec son temps, sa place dans l'exécution, un verdict par rapport à son propre historique, et les raisons. Une exécution qui n'existe pas, ou qui n'a aucune ligne d'étape, ne renvoie aucun profil et un avertissement au lieu d'une erreur.

## Suspendre, arrêter et reprendre

Pendant l'exécution d'un workflow, vous pouvez le **Suspendre**, de sorte que les étapes en cours se terminent et que les nouvelles étapes attendent, ou l'**Arrêter**, ce qui annule les étapes en file d'attente ainsi que, en quelques secondes, les jobs d'importation ou d'exportation encore en cours, ainsi que la requête d'entrepôt qu'une exportation était en train de lire. Les étapes d'importation et de dimension encore en file d'attente sont annulées proprement, afin de ne pas retarder les importations et chargements de dimension suivants dans l'espace de travail. L'arrêt interrompt aussi les synchronisations de connecteur (Singer) du workflow, en file d'attente ou en cours, de sorte qu'une synchronisation ne continue pas de s'exécuter après l'arrêt du workflow.

Dès que vous appuyez sur **Arrêter**, un job d'importation ou d'exportation en cours ne lance aucune nouvelle écriture : une exportation n'envoie aucun fichier et une importation ne charge aucune table. Une écriture déjà en cours se termine d'abord, de sorte qu'aucun fichier, aucune table et aucune dimension ne reste à moitié écrit. Une exportation de plusieurs fichiers, ou une exportation de plusieurs tables, conserve les fichiers qu'elle avait déjà écrits. Une exportation CSV de plusieurs fichiers arrêtée en cours de route a déjà vidé son dossier, de sorte que le dossier ne contient que ces fichiers et aucun fichier d'une exécution précédente. Un chargement de dimension et une exportation vers MongoDB ou Kafka écrivent au fur et à mesure, de sorte que ceux qui ont commencé vont jusqu'au bout. Une étape **Importer depuis SQL** ou **Importer les tables de base de données externe** s'arrête une fois que sa base de données source a renvoyé ce qu'elle lisait, car PlaidCloud n'annule pas la requête de la source. Sur Databend, une exportation que Databend écrit lui-même dans votre compte de documents est une seule écriture, de sorte qu'elle va jusqu'au bout et écrit son fichier.

Une macro peut s'exécuter à plusieurs endroits à la fois, appelée par d'autres workflows ou par une étape **Macro : exécution parallèle**. Arrêter la macro arrête toutes ses copies en cours d'exécution. Arrêter une seule copie n'arrête que cette copie et ce qu'elle a lancé, et laisse le workflow qui l'a appelée continuer de s'exécuter, tout comme une étape **Macro Concurrent** qui abandonne une copie qui ne répond plus. Une macro qui ne s'exécute qu'au sein d'autres workflows apparaît comme **En cours d'exécution** dans la liste des workflows, avec **Arrêter** disponible, et son ouverture affiche l'état, l'heure de début et l'heure de fin de chaque étape lors de sa dernière exécution.

**Reprendre** relance une exécution suspendue, arrêtée ou en échec là où elle s'était interrompue, au lieu de repartir de zéro. L'action est disponible chaque fois que la dernière exécution d'un workflow s'est terminée à l'état suspendu, arrêté ou en erreur.

Ce que signifie « là où elle s'était interrompue » dépend de la manière dont le workflow s'exécute :

| Exécution | À la reprise |
|---|---|
| Série | Redémarre à l'étape qui s'exécutait à la fin de l'exécution, puis continue à partir de là. Si cette étape se trouve dans un groupe, Reprendre relance l'ensemble du groupe de premier niveau qui la contient : les étapes du groupe déjà terminées avec succès sont laissées de côté, les autres sont exécutées, et l'exécution se poursuit après le groupe. |
| Parallèle | Réexécute chaque étape qui ne s'était pas encore terminée avec succès et laisse de côté les étapes terminées. |
| Avancée (graphe) | Réexécute le nœud en échec et tout ce qui attend encore après lui, et laisse de côté les nœuds terminés. |

Les étapes qui appellent un autre workflow (**Run Model**, **Conditional Run Model** et **Loop Model**) reprennent le workflow qu'elles appellent au lieu de le redémarrer, quel que soit le nombre de niveaux d'imbrication. Une étape de boucle reprend l'itération qui avait été interrompue et saute les itérations déjà terminées.

Lorsque vous reprenez un workflow qui s'est exécuté comme **enfant imbriqué** d'un autre (appelé par une étape **Run Model** d'un parent), PlaidCloud propose **Reprendre depuis le début de la chaîne**. Reprendre l'enfant seul ne peut pas poursuivre l'orchestration du parent. Cette option reprend donc le parent de niveau supérieur, c'est-à-dire la racine de la chaîne, et poursuit toute la chaîne là où elle s'était arrêtée. La reprise d'un workflow de niveau supérieur reste inchangée. Le début de la chaîne est déterminé au sein du même projet : une chaîne qui passe dans un autre projet reprend depuis le début de la portion située dans le projet.

Reprendre poursuit toujours l'exécution **d'origine**. Il réexécute chaque étape de cette exécution qui ne s'est pas terminée avec succès (une étape en échec ou abandonnée est réexécutée, et non considérée comme terminée), et réexécuter entre-temps une étape individuelle seule ne change pas ce que Reprendre prendra en charge ensuite. Cela vaut aussi pour un workflow enfant : si vous avez réexécuté seule l'une de ses étapes, la reprise du parent exécute quand même tout ce qu'il restait à l'enfant, et pas seulement cette étape.

Une exécution reprise est enregistrée comme une **nouvelle exécution** dans l'historique des exécutions du workflow, et ne contient que les étapes qu'elle a réexécutées. L'exécution d'origine conserve sa propre entrée d'historique. Lorsqu'une même exécution appelle plusieurs fois le même workflow enfant, chaque appel dispose de sa propre entrée dans l'historique des exécutions de l'enfant. Les itérations d'une étape de boucle comptent comme un seul appel.

:::note
Une étape de boucle fait correspondre ses itérations terminées selon les valeurs de leurs variables. Si les données sur lesquelles la boucle itère ont changé entre l'exécution d'origine et la reprise, les itérations qu'elle ne peut plus faire correspondre sont réexécutées au lieu d'être sautées.
:::
