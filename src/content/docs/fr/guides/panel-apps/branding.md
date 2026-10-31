---
title: Image de marque du projet et projets des applications
description: Définissez une fois les couleurs de marque et un logo pour un projet afin que toutes les applications Panel qu'il contient soient cohérentes, et affectez des applications Panel à un projet lors de leur publication ou ultérieurement.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/branding.md
---

Une application Panel appartient à un projet. Le projet joue deux rôles pour l'application : c'est là qu'elle lit ses tables par défaut, et il contient les couleurs et le logo qu'elle arbore. Définissez l'image de marque une seule fois et toutes les applications du projet la reprennent.

## Appliquer une image de marque à un projet

1. Ouvrez le projet et accédez à son onglet **Accueil**.
2. Dans le groupe **Panel App Branding**, cliquez sur **Edit Branding**.
3. Définissez les couleurs de votre choix. Cliquez sur une pastille pour choisir une couleur, ou saisissez une valeur hexadécimale telle que `#0078d4`.
4. Choisissez éventuellement un logo.
5. Vérifiez l'**Aperçu**, puis cliquez sur **Enregistrer**.

Seuls les Gestionnaires et les Architectes peuvent enregistrer l'image de marque. Les autres membres du projet voient le formulaire en lecture seule.

**Reset to default** efface toutes les couleurs et le logo. L'enregistrement remplace l'image de marque entière : une couleur laissée vide revient donc à la valeur PlaidCloud par défaut.

### Couleurs

| Paramètre | Ce qu'il colore |
|---|---|
| **Brand** | Les boutons, l'onglet actif, les poignées de curseur et les autres contrôles principaux. |
| **Brand accent** | Les accents secondaires. |
| **Brand hover** | Un contrôle principal lorsque le pointeur le survole. |
| **Brand pressed** | Un contrôle principal lorsqu'il est enfoncé. |
| **Header background** | La barre d'en-tête de l'application. |
| **Header text** | Le titre et le nom d'utilisateur dans l'en-tête. |
| **Link** | Les liens. |
| **Text on brand** | Le texte placé sur un contrôle aux couleurs de la marque. |

Ces huit paramètres sont les seuls disponibles. Les couleurs doivent être des valeurs hexadécimales à 3 ou 6 chiffres. Les surfaces, le texte courant et les bordures conservent l'apparence PlaidCloud en mode clair comme en mode sombre : une image de marque ne peut donc pas rendre une application illisible.

### Logo

Le logo est une image provenant d'un [compte de documents](/fr/guides/documents/) de l'espace de travail du projet.

1. Téléversez l'image dans un dossier nommé `branding` à la racine du compte de documents.
2. Dans **Edit Branding**, choisissez le **Compte de documents**, puis l'image sous **Image in the branding/ folder**.

Le logo peut être un fichier PNG, JPEG, GIF, WebP ou SVG d'au plus 512 Ko. Il apparaît sur le côté droit de l'en-tête de l'application. L'image doit se trouver directement dans `branding/` ou dans un dossier qu'il contient, et toute personne qui enregistre l'image de marque doit pouvoir lire le compte.

### Quand les modifications apparaissent

Une application lit son image de marque au démarrage de la session d'un lecteur. Les modifications enregistrées apparaissent la prochaine fois que quelqu'un ouvre l'application ou la recharge.

## Affecter une application à un projet

### Lors de la publication

La boîte de dialogue **Publier une application Panel serveur** comporte un sélecteur **Projet** sous **Paramètres du répertoire**. Choisissez le projet auquel appartient l'application. Vous devez avoir accès au projet pour y publier. Le projet est figé une fois l'application publiée ; pour déplacer une application, utilisez **Affecter** comme décrit ci-dessous.

Une application publiée avec un projet lit par défaut les tables de ce projet : `table("sales")` n'a donc besoin d'aucun argument de projet.

### Pour les applications existantes

1. Ouvrez **Mes applications Panel**.
2. Cliquez sur l'icône **Affecter** sur la ligne de l'application à déplacer.
3. Choisissez le **Projet** et cliquez sur **À examiner**.
4. Lisez le résultat. Il énumère les membres de l'espace de travail qui peuvent ouvrir l'application aujourd'hui mais ne sont pas membres du projet.
5. Cliquez sur **Affecter**.

L'examen ne modifie rien. La colonne **Projet** de **Mes applications Panel** indique le projet de chaque application.

### Accès

Aujourd'hui, le projet ne change pas qui peut ouvrir une application : les lecteurs qui pouvaient ouvrir l'application auparavant le peuvent toujours. À terme, l'accès à une application suivra l'appartenance à son projet, ce qui explique pourquoi **À examiner** énumère les membres qui ne sont pas dans le projet, afin que vous puissiez d'abord les y ajouter.

## Étapes suivantes

- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) : les composants qui utilisent votre image de marque.
- [Créer une application Panel](/fr/guides/panel-apps/creating/) : publiez une application dans un projet.
