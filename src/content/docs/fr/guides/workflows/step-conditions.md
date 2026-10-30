---
title: Exécution conditionnelle des étapes
description: Configurez l'exécution conditionnelle des étapes d'un workflow PlaidCloud pour contrôler quelles étapes s'exécutent selon les valeurs de variables et la logique.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/step-conditions.md
---

## Vue d'ensemble

Les étapes d'un workflow s'exécutent normalement dans l'ordre défini pour le workflow. Il est toutefois souvent utile de n'exécuter certaines étapes que si des conditions prédéfinies sont remplies. Grâce aux conditions d'étape, vous pouvez contrôler l'exécution selon les options suivantes :
 - Valeurs de variables
 - La table contient des lignes ou est vide
 - La table existe ou n'existe pas
 - Un fichier existe dans Document
 - Un fichier est absent dans Document
 - Résultat d'une requête sur une table
 - Conditions de date et d'heure remplies

Pour les comparaisons de variables ou de résultats de requête sur une table, vous pouvez utiliser les comparaisons suivantes :
 - Égal à
 - Différent de
 - Contient
 - Ne contient pas
 - Commence par
 - Se termine par
 - Supérieur à
 - Inférieur à
 - Supérieur ou égal à
 - Inférieur ou égal à

Il est aussi important de noter que vous pouvez définir plusieurs conditions qui doivent toutes être remplies pour que l'étape s'exécute. C'est un outil puissant pour contrôler précisément le moment où une étape doit s'exécuter.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="Une condition d'étape détermine si une étape s'exécute. Lorsque l'étape précédente se termine, la condition est vérifiée ; si elle est remplie, l'étape s'exécute, sinon l'étape est ignorée et le workflow passe à l'étape suivante." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">étape précédente</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">condition remplie ?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">variable · lignes · document existant</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">vrai</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">faux</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">l'étape s'exécute</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">étape ignorée</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">suivante</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Une condition filtre l'étape : remplie → l'étape s'exécute ; non remplie → elle est ignorée. Dans les deux cas, le workflow passe à l'étape suivante. Les conditions testent des variables, la présence de lignes dans une table ou l'existence d'un document.</figcaption>
</figure>

## Ajouter et contrôler des conditions

Pour activer et ajouter des conditions sur une étape :
1) Repérez l'étape sur laquelle vous souhaitez ajouter une condition
2) Faites un clic droit sur l'étape et choisissez **Modifier les détails de l'étape**, ou cliquez sur son icône d'engrenage et passez à l'onglet **Général**
3) Faites défiler jusqu'à la section **Vérifications de conditions**, en bas de l'onglet **Général**
4) Cochez la case **Vérifier les conditions avant l'exécution** pour activer la boîte de dialogue et ajouter des conditions.
5) Dans la section **Vérifications de conditions** à gauche, sélectionnez « + » pour ajouter une nouvelle condition
6) Ajoutez une condition depuis la section à onglets à droite
7) Répétez les étapes 5 et 6 autant de fois que nécessaire pour ajouter toutes vos conditions

## Voir les conditions sur le canevas visuel

Les conditions d'une étape sont visibles depuis le canevas visuel sans ouvrir l'étape. Le connecteur qui mène à une étape conditionnelle est en **pointillés** et porte un petit **bouclier** au niveau de sa pointe de flèche. Ce sont les pointillés que vous repérez lorsque vous avez assez dézoomé pour que le bouclier soit trop petit à distinguer.

Cliquez sur le bouclier pour ouvrir l'étape avec ses **Vérifications de conditions** déjà affichées à l'écran. Vous pouvez aussi faire un clic droit sur le connecteur et choisir **Modifier les conditions…**, ce qui produit le même résultat. Le bouclier sur la vignette de l'étape elle-même, en bas à gauche, continue de signaler l'étape comme conditionnelle comme il l'a toujours fait.

Deux cas n'affichent volontairement aucun bouclier sur une flèche :

- **Une étape sans connecteur entrant.** Une étape soumise à une date ou à une variable peut se trouver au début d'un workflow sans rien qui y mène. Il n'y a aucune flèche à marquer ; seul le bouclier de la vignette apparaît.
- **Une étape dans un groupe réduit.** Sa vignette est repliée dans celle du groupe, et la flèche s'ancre sur le groupe plutôt que sur l'étape ; la marquer attribuerait donc la condition au mauvais élément.

Une étape avec plusieurs connecteurs entrants reçoit un seul bouclier, et non un par flèche.

:::note
Ouvrir les conditions de cette manière amène aux vérifications de conditions pour les types d'étape qui utilisent le formulaire d'étape natif. Un type d'étape qui ouvre encore l'ancienne fenêtre de configuration l'ouvre en haut : les conditions y sont, mais sans défilement jusqu'à elles.
:::

### Ce que le bouclier indique vérifier

L'infobulle du bouclier liste ce que l'étape vérifie réellement, au lieu de vous dire
simplement qu'elle vérifie quelque chose :

```
Table Row Count (sales_2026) > 0 where region = 'EU'
Day of Week = Monday (UTC+2)
Project Variable (run_mode) = "full"
```

Jusqu'à trois vérifications sont listées, suivies du nombre des autres (*…and 2 more checks*), afin que
la liste reste lisible sur une étape comportant de nombreuses conditions. Le même résumé apparaît sur
le bouclier de la vignette de l'étape, qui est le seul dont dispose une étape sans connecteur entrant.

Sélectionner l'étape affiche la même liste dans la section **Conditions** du panneau
Inspecteur, qui est l'endroit le plus pratique pour en lire une longue.

Quelques points à connaître sur la formulation :

- **Les vérifications de jour et de mois s'affichent sous forme de noms**, et non des nombres enregistrés pour elles : *Jour de la semaine = lundi*, et non *Jour de la semaine = 3*.
- **Le fuseau horaire n'apparaît que s'il n'est pas UTC**, comme dans *(UTC+2)* ci-dessus.
- **Un filtre sur une vérification de table est affiché** après `where`, raccourci s'il est long.
- **Une comparaison agrégée l'indique** : *Valeur de requête (aggregated sales_2026.amount) >= 100* compare un total sur l'ensemble de la table, alors que *Valeur de requête (sales_2026.amount) >= 100* compare la valeur d'une seule ligne.
- **Une vérification de document affiche le chemin mais pas le compte.** Deux conditions vérifiant le même chemin dans des comptes de documents différents s'affichent de manière identique ; ouvrez l'étape pour les distinguer.
- **Une table choisie dans l'arborescence affiche son nom** lorsque le workflow lit ou écrit cette table quelque part. Sinon, la vérification est listée sans le nom de la table plutôt qu'avec un identifiant interne.


### Ce que la condition vous coûterait

Survolez le bouclier sans cliquer : le canevas entoure d'un contour en pointillés l'étape conditionnelle et tout ce qui se trouve en aval, c'est-à-dire les étapes qui ne s'exécuteraient pas si cette condition bloquait. Rien ne change ; éloignez le pointeur et la surbrillance disparaît. Les étapes *en amont* ne sont jamais mises en évidence : elles s'exécutent dans tous les cas.

C'est le même aperçu que celui fourni par la pastille **désactivée** d'un groupe désactivé, avec une différence de formulation qui compte. Un groupe désactivé est réellement hors service ; sa pastille indique donc combien d'étapes *seront* ignorées. Une condition n'est évaluée que lorsque l'exécution l'atteint ; le bouclier indique donc combien d'étapes *ne s'exécuteraient pas* **si** la condition bloquait. Il se peut très bien qu'elle laisse tout passer.

### Ce que le bouclier indique sur la dernière exécution

Le bouclier indique aussi ce qui s'est passé lors de l'exécution la plus récente, afin que vous puissiez retracer un flux terminé et voir où il s'est arrêté :

| Bouclier | Signification |
| --- | --- |
| Bouclier simple | L'étape est conditionnelle. Soit elle ne s'est pas encore exécutée, soit elle est en cours d'exécution. |
| Bouclier avec un **+** | L'étape s'est exécutée lors de la dernière exécution. |
| Bouclier avec un **−** | L'étape ne s'est pas exécutée lors de la dernière exécution. |

Les trois se distinguent par leur forme et non par leur couleur, et l'infobulle du bouclier détaille l'état en toutes lettres. Il se met à jour en direct pendant l'exécution d'un workflow ; vous n'avez donc pas besoin de recharger le canevas pour voir une exécution atteindre une condition.

:::caution
Un bouclier avec un **−** vous indique que l'étape ne s'est pas exécutée. Il ne vous dit pas *pourquoi*, et vous ne devez pas l'interpréter comme « la condition l'a bloquée ». Une étape est aussi enregistrée comme non exécutée lorsqu'elle est désactivée, lorsque son groupe est désactivé, lorsqu'une étape en amont a échoué, ou lorsqu'elle se trouvait hors du périmètre d'une exécution partielle. Le bouton **Afficher les journaux** de la barre d'outils ouvre le [journal d'exécution](/fr/guides/workflows/viewing-workflow-log/), qui indique la raison de chaque étape ignorée. Une étape retenue à un point d'arrêt est le seul cas délibérément exclu : elle conserve le bouclier simple, car la mettre en pause à cet endroit était votre décision et non un résultat de l'exécution.
:::


## Gérer les conditions

Vous pouvez ajouter autant de conditions que nécessaire dans la section **Vérifications de conditions**. En les ajoutant, il est judicieux de leur donner un nom explicite afin de les retrouver facilement par la suite.

Une fois une condition ajoutée, sélectionnez-la à gauche et ses critères d'évaluation deviennent modifiables à droite.

Pour renommer une condition, sélectionnez-la et modifiez le champ **Nom** en haut du panneau Configuration à droite, ou double-cliquez sur la condition dans la liste. Vous pouvez aussi faire un clic droit sur une condition pour accéder à **Renommer** et **Supprimer** ; **Supprimer** est également disponible via le bouton « − » au-dessus de la liste.

Une condition sans type de condition sélectionné (par exemple une condition reprise d'un ancien workflow ou d'un workflow importé) ne peut pas être évaluée. Elle est traitée comme non remplie, l'étape est donc ignorée, et le message de l'étape indique que la condition ne précise pas ce qu'il faut vérifier. Ouvrez la condition et choisissez ce qu'elle doit vérifier.


## Conditions de variable

Lors de la vérification de conditions de variable, la section **Value Check Parameters** doit être renseignée pour qu'une comparaison puisse être effectuée.

Dans **Variable or Table Field**, saisissez le nom de la variable. Sélectionnez un type de comparaison et saisissez une valeur de comparaison.


## Conditions de table de base

Si la condition vérifie si une table contient des lignes ou est vide, vous devez également définir la table dans l'onglet **Sélection des données de la table**.


## Conditions d'existence de table

Une condition d'existence de table exécute l'étape uniquement lorsque la table a été créée dans l'entrepôt, ou uniquement lorsqu'elle ne l'a pas été. Elle ne lit jamais les lignes de la table, et une table écrite avec zéro ligne existe. Un nom de table ne correspondant à aucune table du projet est considéré comme manquant. Utilisez-la pour construire une table à la première exécution et la laisser intacte ensuite, ou pour ignorer une étape qui lit une table qu'une étape précédente n'a peut-être pas créée.

Les deux types de vérification sont `radio_table_exists` et `radio_table_not_exists`. Choisissez la table de la même manière que pour une condition de table de base. Définissez la condition avec un assistant IA ou l'API REST ; l'onglet **Vérifications de conditions** ne la liste pas encore.

## Conditions de table avancées

Lors de l'utilisation de conditions de table avancées, la section **Value Check Parameters** doit être renseignée pour qu'une comparaison puisse être effectuée.

Dans **Variable or Table Field**, saisissez le nom du champ issu de la sélection de table. Sélectionnez un type de comparaison et saisissez une valeur de comparaison.

Dans l'onglet **Sélection des données de la table**, sélectionnez la table et complétez la section de mappage des données avec au moins le champ référencé pour la comparaison de la condition.

## Conditions de chemin de document

Si la condition vérifie si un fichier existe, vous devez choisir le compte de documents et indiquer le chemin du document à vérifier dans l'onglet **Chemin du document**. Un dossier à ce chemin est considéré comme manquant, car la vérification porte sur un fichier.

## Conditions de date et d'heure

Pour les sélections de date ou d'heure, vous pouvez ajouter plusieurs conditions si une combinaison de conditions est nécessaire. Par exemple, si vous souhaitez qu'une étape ne s'exécute que le lundi à 2 h 05, vous créeriez trois conditions :
 - Condition de jour de la semaine définie sur lundi (1)
 - Heure du jour définie sur 2
 - Minute de l'heure définie sur 5

### Décalage de fuseau horaire

Chaque condition de date et d'heure possède son propre **Décalage de fuseau horaire**, listé sous forme d'un décalage en heures entières, nommé d'après une zone représentative, par exemple *Eastern Time (US & Canada) (UTC -5)* ou *Asia/Tokyo (UTC +9)*. Les heures que vous saisissez sont comparées à l'horloge de cette zone.

Une nouvelle condition démarre avec le décalage signalé par votre navigateur ; dans la plupart des cas, vous pouvez donc le laisser tel quel. Définissez-le délibérément lorsque la planification relève d'un autre lieu que celui où vous vous trouvez, par exemple une clôture qui s'exécute selon l'horloge de l'équipe financière. Seules les heures entières sont disponibles ; un fuseau à la demi-heure comme l'Inde (UTC +5:30) doit donc être arrondi à l'heure entière la plus proche.

Une condition enregistrée avant l'entrée en vigueur de ce paramètre continue d'être évaluée par rapport à UTC jusqu'à ce que vous choisissiez un fuseau pour elle ; les conditions existantes se comportent donc exactement comme avant.

:::caution
Les conditions **Day of the week** comparent actuellement par rapport à UTC, quel que soit le décalage que vous choisissez. Si vous avez besoin qu'une condition de jour de la semaine tombe sur un jour précis dans un fuseau éloigné d'UTC, sachez qu'elle peut différer de votre jour local pendant plusieurs heures de part et d'autre de minuit.
:::

### Clôture financière Workday

Pour **Utiliser la clôture financière Workday**, le décompte commence à **0 pour le 1er du mois**, comme l'indique l'aide à côté du champ. Ainsi, une clôture qui a lieu le 5e jour du mois correspond à `4`, et non à `5`.

:::caution
Cette condition ne correspond actuellement jamais ; une étape protégée par celle-ci ne s'exécutera donc pas. Utilisez une condition **Day of the month** jusqu'à la résolution de ce problème. Les valeurs négatives, censées compter à rebours depuis la fin du mois, ne fonctionnent pas non plus.
:::

## Définir des conditions avec un assistant IA

Un assistant IA connecté à votre espace de travail peut ajouter et modifier les conditions d'une étape à votre place, que ce soit lors de la création de l'étape ou de la modification d'une étape existante. Tous les types de condition décrits plus haut lui sont accessibles, à l'exception de **Vérifier la clôture financière Workday** : un assistant peut l'écrire, mais elle ne correspond jamais ; l'assistant vous avertit donc au lieu de laisser passer cela inaperçu. Définissez celle-ci vous-même dans l'onglet **Conditions**.

Trois points fonctionnent différemment de la modification manuelle des conditions :

- **La liste entière est remplacée à chaque fois.** Si vous demandez l'ajout ou la modification d'une condition, l'assistant envoie la liste complète ; toute condition qu'il omet est donc supprimée. Si vous n'êtes pas certain qu'il les a toutes, demandez-lui de lister les conditions actuelles de l'étape avant d'écrire.
- **Une condition qui ne peut pas être évaluée est refusée.** Une condition qui ne précise pas ce qu'elle vérifie est rejetée au lieu d'être enregistrée, et l'étape conserve les conditions qu'elle avait déjà. Corrigez la demande et réessayez.
- **Une condition incomplète est enregistrée, avec un avertissement.** Une condition à laquelle il manque la valeur de comparaison, ou des conditions ajoutées sans que **Vérifier les conditions avant l'exécution** soit cochée, sont stockées et signalées sous forme d'avertissement. Ouvrez l'onglet **Conditions** et terminez-les, faute de quoi l'étape ne se comporte pas comme vous l'avez demandé.

Un assistant peut aussi définir le verrou de l'étape, sa visibilité dans les vues Gestionnaire et Explorateur, ses paramètres de nouvelle tentative, et l'étape vers laquelle aller en cas d'erreur.
