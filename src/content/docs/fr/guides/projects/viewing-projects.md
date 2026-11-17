---
title: Consultation des projets
description: Consultez et parcourez les projets PlaidCloud autorisés, y compris les détails du projet, son statut, ses membres et les ressources de données associées.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/viewing-projects.md
---

## Description


Dans **Analyser**, la fonction Projets offre un niveau de compartimentation qui facilite grandement le contrôle des accès et la modification des privilèges. Les projets assurent la principale séparation des données au sein d'un onglet d'espace de travail.



Les projets relèvent d'Analyze, tandis que les workflows relèvent des projets : les projets contiennent donc des workflows. Les workflows, pour résumer, exécutent un large éventail de tâches, notamment des pipelines de transformation de données, de l'analyse de données et même des processus ETL. Vous trouverez plus d'informations sur les workflows dans la section « Workflows ».



## Accès aux projets


**Pour accéder aux projets :**


1. Ouvrez Analyze
2. Sélectionnez « Projets » dans la barre de menus supérieure

La hiérarchie des projets s'affiche. Vous y voyez les projets auxquels vous avez accès. L'espace de travail peut contenir d'autres projets, mais si vous n'en êtes pas propriétaire ou si vous n'y êtes pas affecté, ils ne seront pas visibles pour vous.


## Le panneau d'activité

Le panneau **Activité** à droite de la fenêtre Projets montre ce qui s'est exécuté dans vos projets, si cela a fonctionné, et qui a modifié quoi. Il liste l'activité de tous les projets auxquels vous avez accès, du plus récent au plus ancien, sous un en-tête pour chaque jour. Il recherche de nouvelles activités environ toutes les 15 secondes tant que la fenêtre Projets est la fenêtre active et que l'onglet de votre navigateur est visible.

L'en-tête de chaque jour indique **Aujourd'hui**, **Hier** ou la date, avec un récapitulatif des lignes de ce jour, par exemple « 12 exécutions · 1 en échec · 3 changements ». L'en-tête du jour que vous faites défiler reste en haut de la liste.

### Exécutions

Une exécution de workflow a une ligne. Une icône indique son résultat, et le survol de l'icône en donne l'état : Réussi, Échec, Avertissement, Arrêté ou Démarré. Les lignes avec un échec ou un avertissement ont aussi une barre colorée le long de leur bord gauche.

- **La première ligne** indique le workflow et l'heure : « maintenant », ou il y a quelques minutes ou heures pour aujourd'hui, ou l'heure exacte pour un jour antérieur. Survolez l'heure pour voir la date complète.
- **La deuxième ligne** indique qui l'a exécuté et dans quel projet, par exemple « mike a exécuté · CFO Services », « Exécution planifiée · CFO Services » ou « Exécution du capteur · CFO Services ». À droite figure la durée de l'exécution, ou **Échec** ou **Arrêté** avec sa durée. Une exécution arrêtée nomme la personne qui l'a arrêtée.
- **Une troisième ligne**, lorsqu'il y en a une, montre ce qui s'est mal passé. Lorsqu'une étape a échoué ou émis un avertissement pendant l'exécution, elle affiche le nom de l'étape et son message, avec « +2 de plus » lorsque d'autres étapes ont aussi eu des problèmes. Cliquez sur cette ligne pour ouvrir le workflow à cette étape.

Tant qu'une exécution est en cours, elle est listée sous [En cours maintenant](#en-cours-maintenant). Lorsqu'elle se termine, sa ligne affiche le résultat. Un workflow exécuté par un autre workflow, au moyen d'une étape Workflow : exécuter ou comme macro, n'a pas de ligne propre, et un problème d'étape qui s'y produit apparaît sur la ligne de l'exécution qui l'a appelé. Un problème d'étape dont l'exécution ne figure pas dans la liste a sa propre ligne, par exemple « Échec de l'étape · CRM Pipeline · CFO Services ».

Les modifications, par exemple de workflows, d'étapes, de tables, de dimensions et de projets, ont chacune une ligne, par exemple « mike a modifié l'étape · CFO Services » sous le nom de l'étape.

La plupart des lignes ouvrent ce qu'elles nomment lorsque vous cliquez dessus ou appuyez sur Entrée. Une exécution, ou un workflow créé, modifié, importé ou exporté, ouvre son projet sur l'onglet **Workflows** avec le workflow sélectionné. Un problème d'étape, ou une étape créée, modifiée, supprimée, copiée ou déplacée, ouvre le workflow à cette étape. Une table créée, renommée, publiée ou dépubliée s'ouvre dans l'Explorateur de tables, une dimension créée ou modifiée s'ouvre pour modification, et un projet créé, modifié, importé, exporté ou sauvegardé, ou dont la sécurité a changé, ouvre le projet.

### Lignes répétées

Les modifications successives de même nature, faites par la même personne sur le même objet, se regroupent en une seule ligne, tout comme les exécutions réussies successives du même workflow, démarrées de la même manière par la même personne ou la même planification. Cliquez sur **3 modifications** ou **4 exécutions** sur la ligne pour voir chacune d'elles, et cliquez de nouveau dessus pour les replier.

### En cours maintenant

Les workflows en cours d'exécution sont listés sous **En cours maintenant**, au-dessus de la liste, avec la personne qui les a démarrés et depuis combien de temps ils s'exécutent. Une exécution en pause indique **En pause**. Cliquez sur le nom d'un workflow pour le sélectionner dans la liste **Workflows** de son projet, ou sur **Arrêter** pour arrêter cette exécution.

### Actions au survol

Survolez la ligne d'une exécution, ou rendez-vous-y au clavier, pour afficher deux boutons à icône, dont les info-bulles indiquent **Ouvrir le journal** et **Exécuter le workflow** :

- **Ouvrir le journal** ouvre le journal du projet, filtré sur ce workflow. La ligne d'un problème d'étape a aussi ce bouton.
- **Exécuter le workflow** exécute de nouveau le workflow.

**Arrêter** et **Exécuter le workflow** sont autorisés aux mêmes membres que l'arrêt et l'exécution du workflow depuis ses propres écrans. **Exécuter le workflow** exécute le workflow entier avec ses paramètres par défaut, même lorsque l'exécution de la ligne était une seule étape, une plage d'étapes ou une simulation.

### Problèmes et filtres

Lorsque l'activité chargée comporte des exécutions ou des étapes qui ont échoué ou émis un avertissement, l'en-tête du panneau affiche un nombre tel que **2 problèmes**, signalé comme une erreur si l'une d'elles a échoué. Cliquez dessus pour n'afficher que ces lignes.

La bande en bas du panneau choisit ce que la liste affiche :

| Choix | Affiche |
|---|---|
| **Tous** | Tout |
| **Exécutions** | Les exécutions de workflow |
| **Modifications** | Les modifications de workflows, d'étapes, de tables, de dimensions, de projets, etc. |
| **Problèmes** | Les exécutions et les étapes qui ont échoué ou émis un avertissement |
| **Les miennes** | Vos propres exécutions et modifications |

Saisissez du texte dans **Filtre** pour n'afficher que les lignes dont le nom de workflow, de projet, d'étape, de table, de dimension ou de membre contient votre texte. La bande se termine par le nombre d'événements correspondants, par exemple **12 événements**. Le panneau mémorise votre choix, dans ce navigateur.

### Nouveautés depuis votre dernière visite

Une ligne **Nouveautés depuis votre dernière visite** sépare ce qui est arrivé depuis votre visite précédente de ce que vous aviez déjà vu. Elle s'affiche lorsque **Tous** est choisi et que rien n'est saisi dans **Filtre**. Une visite se termine lorsque vous passez à une autre fenêtre ou fermez la fenêtre Projets, et la ligne se déplace la prochaine fois que vous ouvrez la fenêtre Projets ou rechargez la page.

### Afficher les précédentes

La liste commence par les 7 derniers jours. Cliquez sur **Afficher les précédentes** à la fin de la liste pour charger jusqu'à 500 événements de plus parmi les 30 jours précédant le plus ancien chargé, et cliquez de nouveau pour remonter encore. Le bouton disparaît lorsqu'une période de 30 jours ne comporte aucune activité.

### Clavier

Appuyez sur Tabulation pour atteindre une ligne, puis utilisez les flèches Haut et Bas pour passer d'une ligne à l'autre et Entrée pour ouvrir celle où vous êtes. La touche Tabulation permet aussi d'atteindre les actions au survol de la ligne.

### Limites

- **Votre dernière visite est mémorisée par navigateur.** Sur un autre navigateur ou appareil, la ligne **Nouveautés depuis votre dernière visite** reflète votre dernière visite à cet endroit.
- **Les nombres décrivent l'activité chargée dans le panneau.** Le nombre de problèmes, **Problèmes** et les récapitulatifs par jour couvrent d'abord les 500 événements les plus récents des 7 derniers jours, puis davantage à mesure que vous utilisez **Afficher les précédentes**. Ce ne sont pas des totaux pour vos projets.
- **Une exécution en file d'attente apparaît comme Démarré**, et figure sous **En cours maintenant** une fois qu'elle démarre réellement. Sa durée est comptée depuis sa mise en file d'attente.
- **Les problèmes d'étape d'une macro imbriquée dans une macro** n'apparaissent pas sur la ligne de l'exécution de premier niveau.
- **Un workflow qui s'exécute souvent** a beaucoup de lignes. Les exécutions réussies voisines se regroupent, mais celles de deux workflows qui s'exécutent à tour de rôle ne se regroupent pas.
- **Les exécutions antérieures à la sortie de ce panneau** apparaissent comme Démarré, sans résultat, et les arrêts antérieurs n'apparaissent pas.
- **Un événement enregistré tardivement**, après l'apparition d'événements plus récents, s'affiche lorsque vous rechargez la page.
- **Une fenêtre Projets laissée ouverte et inutilisée pendant plus de 30 jours** reprend à 30 jours en arrière.
- **Sans activité au cours des 7 derniers jours**, le panneau affiche « Aucune activité au cours des 7 derniers jours. » et **Afficher les précédentes** n'apparaît pas : l'activité antérieure ne peut donc pas être chargée.
