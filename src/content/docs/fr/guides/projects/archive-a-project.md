---
title: Archiver un projet
description: Archivez des projets PlaidCloud pour conserver le travail terminé, libérer des ressources de l'espace de travail et garder un environnement de projets propre.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/archive-a-project.md
---

## Créer une archive

Les projets contiennent normalement des processus et une logique critiques, qu'il est important d'archiver. Si vous devez un jour ramener le projet à un état précis, disposer d'archives est indispensable.

PlaidCloud vous permet d'archiver des projets à tout moment. La création d'archives complète le suivi intégré des points dans le temps de PlaidCloud en permettant de capturer des moments précis. Cela peut être particulièrement utile avant un changement important ou pour conserver l'état exact d'un environnement de production.

**Sauvegarde complète** : elle inclut toutes les tables de données d'un projet. L'archive peut être volumineuse, selon le volume de données du projet.

**Sauvegarde partielle** : elle peut être utilisée si toutes les données du projet peuvent être dérivées d'autres sources. Dans ce cas, il n'est pas nécessaire d'archiver les données du projet et de les conserver ailleurs. Les archives partielles font gagner du temps et de l'espace de stockage lors de la création de l'archive.

Pour archiver un projet :

1. Ouvrez Analyze
2. Sélectionnez l'onglet « Projets »
3. Sélectionnez le projet, puis choisissez **Exporter l'archive du projet** dans le menu **Actions** (ou faites un clic droit sur le projet et choisissez **Exporter l'archive du projet**)

La fenêtre indique dans sa barre de titre le projet qu'elle va archiver, ce qui vous permet de vérifier que vous avez choisi le bon avant de commencer.

### Pendant l'exécution de l'archive

La fenêtre d'exportation se ferme dès que PlaidCloud a accepté la demande, et une fenêtre de progression suit ensuite l'archive. Vous pouvez laisser cette fenêtre de progression ouverte pour surveiller l'archive, ou la reléguer en arrière-plan et continuer à travailler — l'archive s'exécute sur la plateforme dans les deux cas, et fermer la fenêtre de progression ne l'arrête pas.

Une notification vous indique comment elle s'est terminée : que l'archive a été écrite, quelles tables y figurent sans leurs données ou, en cas d'échec, pourquoi. Vous n'avez pas besoin de garder la fenêtre ouverte pour la recevoir.

:::note
L'archivage d'un projet volumineux peut prendre de quelques secondes à une heure, selon la quantité de données de table incluses. Une archive de longue durée est normale et ne signifie pas qu'un problème est survenu — attendez la notification plutôt que de lancer une seconde exportation, qui archiverait de nouveau le projet depuis le début.
:::

### Tables dont les données ne peuvent pas être incluses

Il arrive qu'une table listée dans un projet n'ait plus aucune donnée derrière elle — par exemple une table qui n'a jamais été générée, ou dont les données ont été supprimées en dehors du projet. L'archive est tout de même écrite : ces tables sont exclues des données de table, et l'exportation se termine par un message qui les nomme. Tout le reste — la configuration du projet, les workflows, les définitions de table et les données de toutes les autres tables — est archivé normalement.

L'archive consigne les tables qui y figurent sans leurs données, et sa restauration les nomme de nouveau à la fin au lieu de les présenter comme complètes. Une table dont la définition était encore lisible revient avec ses colonnes et sans lignes ; une table dont la définition avait elle aussi disparu revient sous la forme d'une entrée sans table derrière elle. Réexécutez le workflow qui génère une table pour la remplir.

:::note
Une archive planifiée consigne les tables ignorées dans le journal système au lieu de vous afficher un message, puisqu'aucun écran n'est là pour le montrer. Consultez le message d'exportation lorsqu'il est important de savoir quelles tables ont été incluses.
:::

### Si vous ne pouvez pas lire les tables du projet

La lecture des tables d'un projet est une autorisation distincte de la lecture du projet lui-même, et une archive dépend des deux. Si vous pouvez ouvrir un projet mais que vous n'avez pas l'accès en lecture aux tables, l'archive est tout de même écrite — elle ne contient simplement aucune donnée de table, ni aucune définition de table, puisque les deux dépendent de cette même autorisation. L'exportation se termine par un message nommant les tables exclues, identifiées par leurs identifiants internes plutôt que par leurs noms, car les noms proviennent des définitions que l'archive n'a pas incluses.

Une archive créée de cette façon est une copie de la configuration du projet — ses workflows, variables, dimensions, vues et dispositions, dans la mesure où vous avez le droit de lire chacun d'eux — et non de ses données. **Sa restauration ne recrée aucune table**, ce n'est donc pas une sauvegarde à partir de laquelle vous pouvez reconstruire les données du projet. Vérifiez le message d'exportation avant de vous y fier.

Contrairement aux tables décrites plus haut, réexécuter un workflow ne corrige pas cette situation — les données n'ont jamais été lues. Demandez à un administrateur de l'espace de travail de vous accorder l'accès en lecture aux tables du projet, puis créez de nouveau l'archive.

:::caution
Cela s'applique aussi aux archives planifiées, qui s'exécutent sous l'identité d'un membre particulier. Lorsque ce membre n'a pas l'accès en lecture aux tables, chaque archive produite par la planification ne contient que la configuration, et ce défaut est consigné dans le journal système sans être montré à personne. Si vous conservez des archives planifiées comme sauvegardes, vérifiez que le membre sous lequel elles s'exécutent peut lire les tables du projet.
:::

### Si le projet utilise l'accès aux lignes

La création d'une archive lit les tables du projet ; l'[accès aux lignes](/fr/administration/access/managing-security-groups-and-assignments/#gérer-laccès-aux-lignes) s'y applique donc comme à toute autre lecture. Sur chaque colonne de gouvernance, l'archive contient les lignes accordées à vos groupes. Lorsque vous n'avez aucune autorisation sur une colonne, le résultat dépend de la manière dont cette colonne a été déclarée : une colonne configurée pour refuser par défaut ne vous donne aucune ligne, une colonne déclarée pour tout autoriser par défaut reste non filtrée. Une table qui ne contient aucune des colonnes de gouvernance est archivée en entier, et un Architecte du projet archive toutes les lignes quelles que soient les autorisations. Une archive planifiée s'exécute sous l'identité propre du projet et non la vôtre ; elle archive donc toutes les lignes.

Une archive créée par un membre qui ne détient qu'une partie des autorisations est une copie partielle des données du projet, et une colonne configurée pour refuser par défaut signifie qu'une table peut revenir vide plutôt que simplement restreinte. La restauration d'une telle archive reconstruit le projet sans ces lignes, et rien dans la restauration ne le signale, car pour l'archive ces lignes n'ont jamais existé.

:::caution
Si vous avez besoin d'une archive à partir de laquelle reconstruire l'intégralité du projet, créez-la avec un membre qui lit le projet en entier.
:::

### Si l'exportation échoue

Une exportation qui échoue signale désormais l'échec. Auparavant, une archive pouvait être signalée comme terminée alors qu'elle n'avait pas été écrite, vous laissant découvrir plus tard l'absence du fichier — le plus souvent au moment de la restaurer. Une exportation en échec le dit maintenant ; considérez donc un succès signalé comme authentique et consultez le message pour tout ce qui signale une erreur. Il en va de même pour les autres types d'exportation, pas seulement les archives de projet.

## Restaurer une archive

Une fois que vous avez une archive, vous voudrez peut-être la restaurer. Vous pouvez restaurer une archive dans un nouveau projet ou dans un projet existant.

Pour restaurer une archive :

1. Ouvrez Analyze
2. Sélectionnez l'onglet « Projets »
3. Choisissez **Importer une archive de projet** dans le menu **Actions** (ou dans la barre d'outils) et sélectionnez l'archive à restaurer
4. Choisissez de **Créer un nouveau projet** ou d'**Importer dans un projet existant**, puis sélectionnez dans l'arborescence ce que vous voulez importer
5. Cliquez sur **Importer le projet**

L'importation s'exécute en arrière-plan. Une fenêtre de progression indique son avancement, et un message vous prévient à la fin, avec un e-mail également si des éléments ont été exclus. Si l'importation ne peut pas démarrer — parce que le projet choisi est verrouillé, par exemple —, la fenêtre reste ouverte et vous en indique la raison.

Une archive est vérifiée à son ouverture. Une archive contenant des éléments qu'une archive de projet ne contient jamais — un fichier qui atterrirait en dehors du dossier de l'archive, un lien qui pointe en dehors de celui-ci, ou des paramètres qui tentent de créer autre chose que des données simples — est refusée avant que quoi que ce soit en soit restauré.

Vous n'avez pas à importer toute l'archive. L'arborescence de sélection liste ce que contient l'archive par type — workflows, étapes, tables, dimensions, éditeurs de données, fonctions définies par l'utilisateur — et tout ce que vous cochez entraîne ses dépendances.

### Lorsqu'une partie de l'archive n'est pas importée

Une importation se poursuit lorsqu'une partie de l'archive ne peut pas être restaurée. Tant que l'archive peut être lue et que le projet lui-même peut être configuré, le projet est importé, et tout ce qui n'a pas pu être restauré est listé dans son résultat d'importation. Si l'archive ne peut pas être lue, ou si le projet lui-même ne peut pas être configuré, l'importation échoue et vous en indique la raison, et un nouveau projet est supprimé. Une importation dans un projet existant peut aussi s'arrêter avant d'être terminée. Tout ce qu'elle avait déjà restauré reste dans le projet. Le message et l'e-mail indiquent que l'importation s'est arrêtée, et le résultat d'importation précise quand et pourquoi, et liste ce qu'elle n'a pas pu restaurer jusque-là.

Lorsque des éléments ont été exclus, le message et l'e-mail de fin d'importation le signalent, et le message renvoie vers la fenêtre **Résultat de l'importation**. La fenêtre nomme chaque élément par type et par nom, indique la raison, et regroupe les éléments sous ces titres :

- **Non importé** — l'élément n'est pas dans le projet.
- **Créées sans données** — la table, la vue ou la dimension est dans le projet mais ne contient aucune donnée, car ses données n'ont pas pu être lues ou chargées.
- **Avertissements** — l'élément a été importé, mais il y a quelque chose à vérifier, comme des colonnes que l'entrepôt a converties vers les types de colonnes de la table.
- **Variables ayant conservé la valeur de ce projet** — le projet avait déjà une variable portant ce nom, qui a donc conservé sa propre valeur.

Les éléments les plus graves sont listés en premier, et la fenêtre l'indique lorsqu'il y en a plus que ce qu'elle affiche. Pour rouvrir la fenêtre plus tard, sélectionnez le projet dans l'onglet **Projets** et choisissez **Voir le résultat de l'importation ou de la copie** dans le menu **Actions**, ou faites un clic droit sur le projet.

Le résultat reste attaché au projet jusqu'à ce que quelqu'un l'ignore, ou qu'une importation ultérieure dans le même projet le remplace. Cliquez sur **Ignorer le résultat** pour le supprimer pour toutes les personnes qui peuvent ouvrir le projet ; rien ne change dans le projet. Ignorer le résultat nécessite un accès en modification au projet, et le projet ne doit pas être verrouillé.

### Importer dans un projet existant

Importer dans un projet existant ajoute du contenu au projet au lieu de le remplacer. Deux éléments déterminent ce qui se passe lorsque l'archive et le projet contiennent le même élément.

**Vous devez pouvoir modifier le projet cible.** Une importation dans un projet sur lequel vous n'avez aucun rôle est refusée, tout comme une importation dans un projet verrouillé pour empêcher les modifications — vérifié avant toute lecture ou écriture, de sorte qu'une importation refusée laisse le projet intact.

**Le projet conserve ses propres paramètres.** Son nom, son identifiant, son environnement de connexion aux données, ses valeurs de stockage par défaut, son compte de documents, son type d'accès, ses listes d'accès et ses autorisations d'accès aux lignes restent tels quels. Seul le contenu que vous avez sélectionné est importé.

Une étape définie sur **Par défaut du projet** reprend ce paramètre tel quel, et non un compte — une fois restaurée, elle utilise la valeur par défaut du projet, et non celle qu'il avait au moment de l'archivage.

### Éléments en double

Lorsqu'un élément entrant est le même qu'un élément déjà présent dans le projet, vous choisissez ce qui lui arrive :

- **Écraser les éléments en double avec les données entrantes** — la version de l'archive remplace celle du projet.
- **Créer une copie des éléments en double** — le projet conserve ce qu'il a, et l'élément entrant est ajouté à côté, avec ` copy` ajouté à son nom (et un compteur si ce nom est déjà pris). Cela s'applique aux workflows, étapes, tables, dimensions, éditeurs de données, vues et fonctions définies par l'utilisateur.

**Les variables de projet et de workflow font exception.** Une variable est identifiée par son nom ; il n'y a donc aucun moyen d'en ajouter une seconde copie sans la renommer en quelque chose que rien ne référence. Lorsque le projet définit déjà une variable que l'archive contient aussi, la valeur du projet est conservée et le résultat d'importation liste les variables laissées telles quelles. Si vous voulez la valeur de l'archive, définissez-la ensuite sur la variable.

À noter : cette correspondance se fait par identité, pas par nom. Un élément issu du même projet à l'origine — tout ce dont l'archive a été exportée, ou une copie de celui-ci — est reconnu comme le même élément. Deux éléments qui partagent simplement un nom sont traités comme des éléments différents, et les deux seront présents après l'importation.

### Si une table revient sans ses données

La restauration des données d'une table dépend de l'alignement de ses colonnes avec la table qui les reçoit — les mêmes noms dans le même ordre, car c'est ce sur quoi se base un chargement. Lorsqu'elles ne s'alignent pas, les données de cette table sont exclues et la table est listée dans le résultat d'importation sous **Créées sans données**, de la même façon qu'une table dont les données ne figuraient pas dans l'archive. Une différence de type stocké d'une colonne ne bloque pas à elle seule les données : elles sont chargées, et la table est listée sous **Avertissements** avec les colonnes que l'entrepôt a converties.

Une importation dont toutes les tables n'ont pas pu charger leurs données conserve tout de même le projet. Son message de fin indique qu'aucune donnée de table n'a pu être chargée, tout comme le résultat d'importation. Si une importation se termine avec tous les workflows, toutes les tables et toutes les dimensions en place, lisez son message de fin avant de supposer que les lignes ont suivi.

## Planification des archives

Les archives peuvent aussi servir de sauvegarde périodique de votre projet. PlaidCloud vous permet de gérer la planification des sauvegardes et de définir la durée de conservation des archives de sauvegarde selon ce qui est le plus pratique ou souhaité.

Comme toutes les modifications d'un projet sont suivies automatiquement, l'archivage n'est pas nécessaire pour revenir en arrière. Il fournit toutefois des instantanés précis de l'état du projet, souvent utiles à des fins de contrôle ou pour pouvoir revenir à un point connu.

Pour définir une planification d'archivage :

1. Ouvrez Analyze
2. Sélectionnez l'onglet « Projets »
3. Cliquez sur l'icône de sauvegarde
4. Choisissez un répertoire de destination dans un compte de **Document**
5. Choisissez la fréquence et la conservation des sauvegardes
6. Choisissez les éléments à sauvegarder
7. Cliquez sur « Mettre à jour »
