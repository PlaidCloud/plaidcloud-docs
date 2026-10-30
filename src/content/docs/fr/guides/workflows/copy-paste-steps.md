---
title: "Copier et coller des étapes"
description: Copiez et collez des étapes de workflow entre les workflows PlaidCloud pour réutiliser les configurations d'étapes et accélérer le développement de vos workflows.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/copy-paste-steps.md
---

## Copier des étapes


Il est souvent utile de copier des étapes plutôt que de repartir de zéro à chaque fois. PlaidCloud permet de copier des étapes au sein d'un workflow, d'un workflow à l'autre, et même vers d'autres projets. Vous pouvez sélectionner plusieurs étapes à copier en une seule fois. Sélectionnez les étapes du workflow dans la hiérarchie, puis cliquez sur le bouton **Copier la sélection** en haut de la table.



Les étapes sélectionnées sont alors placées dans le presse-papiers et peuvent être collées dans le workflow actuel ou dans un autre.

Le presse-papiers est conservé dans votre navigateur ; il survit donc au rechargement de la page et il est partagé par tous les onglets PlaidCloud que vous avez ouverts. Copiez depuis un projet dans un onglet, passez à un projet dans un autre onglet, puis collez-y. Il n'est pas partagé entre différents navigateurs, entre des navigateurs sur des machines différentes, ni avec d'autres personnes, et le changement d'espace de travail le vide.

Un seul presse-papiers dessert tous les endroits où vous copiez une étape (la table des étapes, l'ancienne table à laquelle vous accédez en maintenant Ctrl (ou Cmd) enfoncée lors de l'ouverture d'un workflow, et le canevas du workflow avancé) : vous pouvez donc copier depuis n'importe lequel et coller dans n'importe lequel. Copiez quelques étapes depuis une table et collez-les sur un canevas avancé, ou l'inverse ; il s'agit du même presse-papiers.



Copier une étape crée une étape dupliquée dans le projet : une nouvelle étape, avec sa propre configuration, indépendante de l'originale.

Une étape ne peut apparaître qu'une seule fois dans la structure d'un workflow donné. **Ajouter à la fin** et **Insérer** collent toujours un nouveau doublon, et ne rencontrent donc jamais ce cas. Coller une *référence* à une étape que vous avez déjà placée (voir **Coller en tant qu'étape liée** ci-dessous) est différent : il s'agit de la même étape ; la coller dans un workflow qui la contient déjà, y compris celui d'où vous l'avez copiée, est donc refusé avec un message qui nomme l'étape. Liez-la plutôt dans un *autre* workflow.



## Coller des étapes


Après avoir sélectionné les étapes à copier et les avoir placées dans le presse-papiers, vous pouvez les coller dans le même workflow ou dans un autre, même dans un autre projet. Deux options s'offrent à vous pour coller les étapes dans le workflow :


* Ajouter à la fin du workflow
* Insérer après la dernière ligne sélectionnée

L'option d'ajout à la fin place simplement les étapes à la fin du workflow sélectionné. L'option d'insertion place les étapes copiées après la ligne sélectionnée. Notez que si plusieurs étapes ont été copiées dans le presse-papiers depuis plusieurs zones d'un workflow, elles seront collées dans l'ordre, mais sans l'information de hiérarchie imbriquée qu'elles avaient lors de la copie. Le collage produit une liste plate d'étapes à insérer uniquement. Cela peut être inattendu, mais c'est plus sûr que de recréer dans le workflow cible toute la structure de répertoires qui existait dans le workflow source.


## Coller en tant qu'étape liée


**Coller → Add Linked Steps (Advanced)** place la *même* étape dans le workflow cible plutôt qu'une copie. Les deux emplacements correspondent à une seule et même étape : modifiez-la dans l'un ou l'autre workflow et les deux changent, car il n'y a qu'une seule étape à modifier.


Une étape liée ne peut être collée que dans le projet d'où elle a été copiée. Une liaison est un second emplacement d'une étape qu'un projet possède ; elle n'a donc aucun sens en dehors de ce projet. Si vous collez dans un autre projet, PlaidCloud refuse et vous invite à utiliser **Ajouter à la fin** ou **Insérer** à la place, qui copient les étapes dans le projet cible comme des étapes à part entière.

Une étape liée ne peut pas non plus être placée dans un workflow qui la contient déjà, car cela ferait la même étape deux fois dans la structure d'un workflow, ce que PlaidCloud refuse. Ce cas se présente surtout si une opération de liaison semble échouer et que vous la relancez : la première tentative a en fait abouti, et la seconde est refusée plutôt que de corrompre le workflow. L'erreur nomme l'étape afin que vous puissiez confirmer qu'elle s'y trouve déjà.


## Copier et coller sur le canevas avancé


Dans un workflow avancé, vous pouvez copier et coller des étapes directement sur le canevas avec le clavier, et les liens entre elles sont conservés.


Sélectionnez les étapes souhaitées (tracez un cadre autour d'elles, ou cliquez sur l'une puis cliquez avec Maj ou Ctrl/Cmd pour en ajouter d'autres) et appuyez sur **Ctrl/Cmd+C**. Passez au workflow dans lequel vous les voulez, dans ce projet ou dans un autre, pointez l'endroit où elles doivent aller, puis appuyez sur **Ctrl/Cmd+V**. Les étapes sont copiées avec leur disposition d'origine et restent sélectionnées pour que vous puissiez les faire glisser à leur place. Vous pouvez aussi effectuer ces deux opérations sans le clavier. Faites un clic droit sur une zone vide du canevas et choisissez **Copy N Steps** (affiché lorsque des étapes sont sélectionnées) ou **Paste N Steps Here** (affiché lorsque le presse-papiers contient des étapes) ; les étapes collées se placent là où vous avez cliqué. Lorsque le presse-papiers contient des étapes, la barre d'outils affiche « N steps from *workflow* » avec un bouton **Coller** qui colle au milieu de la partie du canevas que vous regardez.


**Un groupe est collé en tant que groupe.** Cliquez sur l'en-tête d'un groupe : le groupe et toutes ses étapes sont sélectionnés ensemble ; copiez, et le cadre du groupe et ses membres sont collés ensemble. Un cadre de sélection tracé autour d'un groupe entier le sélectionne de la même manière.


**Les liens entre les étapes copiées sont conservés ; les liens vers des étapes que vous n'avez pas copiées ne le sont pas.** Une étape de votre sélection qui était alimentée par une étape que vous avez laissée de côté arrive sans ce lien entrant, car il n'y a rien à l'autre extrémité à quoi se connecter. Le collage vous prévient lorsque cela se produit, de sorte qu'une connexion perdue n'est jamais silencieuse.


**Coller dans le même workflow** décale légèrement les copies pour qu'elles ne se placent pas exactement sur les originales. Coller dans un workflow qui n'est pas avancé (une table d'étapes ordinaire) supprime la disposition du canevas et les liens, et ajoute simplement les étapes ; le collage vous en informe.


**Un collage volumineux est effectué automatiquement par lots.** Rien n'est plafonné et rien n'est silencieusement abandonné : un collage de centaines d'étapes affiche simplement sa progression au fil de son traitement, et vous pouvez l'annuler. Si un collage ne peut pas se terminer, les étapes déjà ajoutées sont supprimées pour que vous ne vous retrouviez pas avec un workflow à moitié collé ; dans le cas rare où certaines ne peuvent pas être supprimées automatiquement, le message l'indique et précise combien il en reste, plutôt que d'annoncer une annulation complète.


**Pour annuler un collage,** appuyez sur **Ctrl/Cmd+Z** juste après : les étapes collées sont supprimées. Dès qu'un collaborateur a modifié le workflow, ou que vous l'avez rechargé, cette annulation en une étape s'efface plutôt que de risquer de supprimer un travail qui n'est plus seulement le vôtre.


Les étapes sont copiées en tant que nouvelles étapes à part entière. Coller la *même* étape à plusieurs endroits (le comportement des étapes liées décrit plus haut) est une action de la table des étapes ; sur le canevas, utilisez **Ajouter une étape** pour placer une référence dans un workflow qui ne contient pas déjà cette étape.
