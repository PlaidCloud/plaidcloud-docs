---
title: Panel Studio
description: "Créez, modifiez, prévisualisez et publiez des applications Panel sans quitter PlaidCloud — puis restaurez une version antérieure, consultez l'utilisation et la rapidité de l'application, configurez des alertes et des synthèses, listez-la dans la galerie et épinglez-la sur l'accueil."
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio est l'éditeur d'applications Panel intégré à PlaidCloud. Il affiche les fichiers de l'application à côté d'un éditeur, construit un aperçu privé que vous pouvez ouvrir et publie l'application lorsque vous êtes prêt. Vous n'avez pas besoin d'un dépôt git pour commencer.

## Ouvrir Panel Studio

- Sur le tableau **Accueil** d'un projet, choisissez **Ouvrir dans Studio** sur une application Panel.
- Dans **Mes applications Panel**, choisissez **Ouvrir dans Studio** sur la ligne d'une application.

Pour démarrer une nouvelle application, choisissez **Nouvelle application Studio**. C'est le premier bouton de la barre d'outils **Mes applications Panel**, et il figure dans la zone **Applications Panel** de l'onglet **Accueil** d'un projet. Pour construire à partir d'une table, sélectionnez-la dans l'onglet **Tables** du projet et choisissez **Créer une application Panel**.

## Créer une application

La boîte de dialogue **Nouvelle application Studio** vous propose cinq points de départ :

| Partir de | Vous obtenez |
|---|---|
| **Application vierge** | Une application minimale avec un `app.py` et un `requirements.txt`. |
| **À partir d’une table** | Une application construite sur la table que vous sélectionnez. |
| **À partir d’une vue** | La même, construite sur une vue du projet. |
| **À partir d’une autre application Studio** | Une copie de l'une de vos applications Studio. |
| **À partir de la galerie** | Une copie d'une application que votre espace de travail a listée dans la [galerie d'applications](/fr/guides/panel-apps/gallery/). |

Nommez l'application, sélectionnez son **Projet** et choisissez **Créer**. Studio ouvre la nouvelle application avec ses fichiers listés à gauche. Pour une table ou une vue, l'invite de Weave pour construire la première page de l'application est prête à être envoyée. Consultez [Créer une application Panel](/fr/guides/panel-apps/creating/).

## Modifier

Sélectionnez un fichier dans la liste pour le modifier dans l'éditeur. Listez vos dépendances Python dans `requirements.txt`, un paquet par ligne. Elles sont installées lors de la compilation de l'application.

Choisissez **Demander à Weave** pour que Weave écrive ou modifie l'application à votre place. Consultez [Créer des applications Panel avec Weave](/fr/guides/panel-apps/build-with-weave/).

## Enregistrer, prévisualiser et publier

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Enregistrer conserve un brouillon que vous seul voyez. Aperçu construit une copie privée du brouillon pour l'éditeur. Publier remplace l'application en ligne après votre confirmation." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Enregistrer</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">brouillon uniquement</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Aperçu</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">éditeur uniquement</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publier</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">l'application en ligne</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Vos modifications n'atteignent les lecteurs que lorsque vous publiez.</figcaption>
</figure>

### Enregistrer

**Enregistrer** stocke vos modifications sous forme de brouillon. L'application en ligne ne change pas et personne d'autre ne voit le brouillon.

### Aperçu

**Aperçu** construit votre brouillon enregistré sous forme de copie privée et l'ouvre. Seuls les éditeurs de l'application peuvent ouvrir un aperçu.

- Un aperçu est supprimé après 24 heures sans enregistrement.
- Un espace de travail peut avoir jusqu'à 10 aperçus à la fois.
- Enregistrez de nouveau et choisissez **Aperçu** pour voir vos dernières modifications.

### Publier

**Publier** remplace l'application en ligne par votre brouillon enregistré. Cela nécessite l'autorisation de modification sur le projet de l'application, et Studio vous demande d'abord de confirmer.

Si quelqu'un d'autre a publié une modification après l'ouverture de l'application, Studio signale un conflit au lieu d'écraser son travail. Rechargez l'application, reportez vos modifications et publiez de nouveau.

## Statut de compilation et erreurs

L'onglet **Créer** affiche le statut de la dernière compilation et se met à jour pendant son déroulement. Lorsqu'une compilation échoue, l'onglet liste chaque erreur avec son fichier et son numéro de ligne, afin que vous puissiez aller directement à la ligne concernée. Les problèmes de dépendances dans `requirements.txt` s'accompagnent d'une indication pour les corriger.

Les erreurs et avertissements sont aussi signalés sur leurs lignes dans l'éditeur, de sorte que vous voyez un problème là où il se trouve.

Pour connaître la signification de chaque statut une fois l'application publiée, consultez [Utiliser une application Panel](/fr/guides/panel-apps/using/#état-de-génération-applications-serveur).

## Historique et restauration

L'onglet **Historique** liste chaque version publiée de l'application, de la plus récente à la plus ancienne, avec son statut de compilation. Choisissez **Charger plus** pour voir les versions plus anciennes.

Pour revenir à une version antérieure, choisissez **Restaurer** sur celle-ci et confirmez. La version restaurée devient l'application en ligne et est recompilée. Votre brouillon non enregistré n'est pas perdu : il reste dans le brouillon et passe en ligne par-dessus la version restaurée lors de votre prochaine publication. Si l'application correspond déjà à cette version, Studio l'indique et ne change rien. Si quelqu'un a publié pendant que vous restauriez, Studio ne restaure rien et vous demande de réessayer.

## Analyses

L'onglet **Analyses** montre comment les gens utilisent l'application et sa rapidité de réponse. Choisissez les 7, 14 ou 30 derniers jours.

| Section | Affiche |
|---|---|
| **Vues par jour** | Combien de fois l'application a été ouverte chaque jour. |
| **Chargement de page** | Le temps de chargement médian, et le temps que 95 pour cent des chargements ne dépassent pas, d'après les chargements de pages de la période. |
| **Requêtes les plus lentes** | Les requêtes les plus longues, avec leur fréquence d'exécution et leurs temps médian, haut et maximal. |
| **Erreurs** | Ce qui s'est mal passé pendant la période, par type d'erreur et par endroit de l'application où cela s'est produit. |

Lorsqu'une période contient plus d'activité que les Analyses ne peuvent en lire, elles indiquent que les chiffres sont partiels. Lorsque des chargements de page dépassent le [budget de performance](/fr/guides/panel-apps/app-kit/#budgets-de-performance) de l'application, les Analyses vous avertissent du nombre de chargements concernés et des requêtes lentes. Les Analyses n'affichent jamais les données qu'une requête a renvoyées ni les noms des personnes qui ont ouvert l'application.

Ces deux onglets nécessitent que l'application soit affectée à un projet ; une application non affectée affiche une invite pour l'affecter.

## Alertes et synthèses

Choisissez **Alertes et synthèses** pour configurer des notifications qui surveillent un nombre dans les données de l'application et vous avertissent lorsqu'il franchit une limite, ou qui envoient une synthèse selon une planification. Consultez [Alertes et synthèses](/fr/guides/panel-apps/alerts-and-digests/).

## Lister une application dans la galerie

Choisissez **Galerie…** dans Studio. Choisissez **Lister dans la galerie** pour lister l'application comme modèle à partir duquel toute personne qui peut consulter son projet peut créer sa propre application, ou **Retirer de la galerie** pour la retirer. Le bouton est disponible pour les applications qui appartiennent à un projet. Vous devez disposer d'un accès en modification au projet. Consultez [La galerie d'applications](/fr/guides/panel-apps/gallery/).

## Épingler sur l'accueil

Choisissez **Épingler à l’accueil** pour ajouter l'application au tableau **Accueil** du projet, et **Détacher de l’accueil** pour la retirer.

## Supprimer une application

La suppression d'une application Panel vous demande d'abord de confirmer. Dans **Mes applications Panel**, utilisez l'icône **moins** sur la ligne de l'application. L'annulation de la publication demande également une confirmation.

## Étapes suivantes

- [Créer des applications Panel avec Weave](/fr/guides/panel-apps/build-with-weave/) — décrivez l'application et approuvez la modification exacte.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) — les composants qu'utilisent les points de départ de Studio à partir d'une table ou d'une vue.
- [Alertes et synthèses](/fr/guides/panel-apps/alerts-and-digests/) — avertissez les gens lorsqu'un nombre franchit une limite, ou selon une planification.
- [La galerie d'applications](/fr/guides/panel-apps/gallery/) — partagez une application comme point de départ pour d'autres.
- [Utiliser une application Panel](/fr/guides/panel-apps/using/) — journaux, utilisation et recompilations après la publication.
