---
title: Applications Panel
description: "Créez et déployez des applications de données interactives HoloViz Panel dans PlaidCloud — sous forme d'applications statiques exécutées dans le navigateur ou d'applications côté serveur construites à partir d'un dépôt git."
sidebar:
  label: Applications Panel
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/index.md
---

Les applications Panel vous permettent de publier des applications [HoloViz Panel](https://panel.holoviz.org/) interactives — entrées paramétrées, graphiques en direct et tables de données intégrées — directement depuis PlaidCloud. Vous les gérez depuis l'écran **Mes applications Panel**, qui liste chaque application avec son environnement d'exécution, son statut de compilation et son URL.

Commencez dans [Panel Studio](/fr/guides/panel-apps/studio/) : choisissez **Nouvelle application Studio** pour construire une application dans PlaidCloud à partir d'une application vierge, d'une table, d'une vue ou de la galerie, sans dépôt à configurer. Pour des besoins sur mesure, publiez avec l'un des environnements d'exécution ci-dessous, indiqués dans la colonne **Exécution** :

- **WASM** — une application statique qui s'exécute entièrement dans le navigateur (Pyodide). Vous publiez un fichier HTML précompilé depuis un compte de documents. Il n'y a ni processus serveur ni rien à mettre à l'échelle ; elle est servie immédiatement.
- **Serveur** — une application construite à partir d'un dépôt git et exécutée côté serveur. Lors de la publication, PlaidCloud compile votre dépôt dans un conteneur qui reste inactif à zéro réplique, se réveille à la première requête vers son URL, sert l'application (mises à jour en direct comprises) et revient à zéro lorsqu'il est inactif. C'est le bon choix pour les applications qui nécessitent un environnement Python, du calcul côté serveur ou des bibliothèques qui ne peuvent pas s'exécuter dans le navigateur.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 250" role="img" aria-label="Les deux environnements d'exécution des applications Panel. Une application WASM est un fichier HTML précompilé servi directement au navigateur, sans serveur. Une application serveur est construite à partir d'un dépôt git dans un conteneur qui reste inactif à zéro réplique, se réveille à la première requête en une quinzaine de secondes, sert l'application et revient à zéro lorsqu'il est inactif." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pa-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="14" y="40" font-size="12" font-weight="700" fill="var(--sl-color-accent)">WASM</text>
  <rect x="70" y="24" width="150" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="49" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">fichier HTML précompilé</text>
  <path d="M220 45 L286 45" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="288" y="24" width="164" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="370" y="43" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">navigateur · Pyodide</text>
  <text x="370" y="58" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">servie immédiatement</text>
  <line x1="14" y1="96" x2="666" y2="96" stroke="var(--sl-color-gray-5)" stroke-dasharray="3 3" />
  <text x="14" y="146" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Serveur</text>
  <rect x="70" y="128" width="96" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="118" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">dépôt git</text>
  <path d="M166 149 L186 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="188" y="128" width="110" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="243" y="153" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">compiler le conteneur</text>
  <path d="M298 149 L318 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <rect x="320" y="128" width="120" height="42" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="380" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">inactif · 0 réplique</text>
  <text x="380" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">rien en cours</text>
  <path d="M440 149 L474 149" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pa-arrow)" />
  <text x="457" y="140" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">1re requête</text>
  <rect x="476" y="128" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="536" y="147" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">en service</text>
  <text x="536" y="162" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">réveil ~15 s</text>
  <path d="M536 170 C536 212 380 212 380 174" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#pa-arrow)" />
  <text x="458" y="206" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">retour à 0 lorsqu'inactif</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Deux environnements d'exécution : une application <strong>WASM</strong> est un fichier HTML précompilé servi directement au navigateur ; une application <strong>Serveur</strong> est construite depuis git, reste inactive à zéro, se réveille à la première requête (~15 s), sert l'application et revient à zéro.</figcaption>
</figure>

## Choisir un environnement d'exécution

| | WASM | Serveur |
|---|---|---|
| Source | Un fichier HTML publié | Un dépôt git (connexion, branche, point d'entrée) |
| S'exécute | Dans le navigateur | Côté serveur, avec retour à zéro |
| Idéal pour | Des tableaux de bord légers et autonomes | Des applications nécessitant du calcul serveur ou des bibliothèques Python complètes |
| Démarrage à froid | Aucun | La première requête démarre l'application (~15 secondes) |

## Étapes suivantes

- [Panel Studio](/fr/guides/panel-apps/studio/) — créez, modifiez, prévisualisez et publiez une application dans PlaidCloud, sans dépôt à configurer.
- [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/) — le parcours complet, du dépôt à une application servie, avec une connexion gérée sans identifiants.
- [Créer des applications Panel avec Weave](/fr/guides/panel-apps/build-with-weave/) — décrivez l'application et approuvez la modification exacte que Weave propose.
- [Créer une application Panel](/fr/guides/panel-apps/creating/) — démarrez une application Studio à partir d'une application vierge, d'une table ou de la galerie, ou publiez une application serveur depuis git ou une application WASM depuis un fichier.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) — créez des applications qui ont l'apparence de PlaidCloud, en thème clair et sombre, avec des filtres, des chiffres clés, une grille de données paginée côté serveur, des graphiques, des formulaires, des boutons d'exécution, des paramètres enregistrés et l'impression.
- [L'API de données pour les applications Panel](/fr/guides/panel-apps/data-api/) — filtrez, paginez, comptez et agrégez des tables sur le serveur.
- [Alertes et synthèses](/fr/guides/panel-apps/alerts-and-digests/) — recevez une notification push, un e-mail ou un message Slack ou Teams lorsqu'un nombre franchit une limite, ou une synthèse planifiée.
- [La galerie d'applications](/fr/guides/panel-apps/gallery/) — listez une application comme modèle et créez de nouvelles applications à partir des applications listées.
- [Identité visuelle du projet et projets d'applications](/fr/guides/panel-apps/branding/) — définissez des couleurs et un logo pour les applications d'un projet, et affectez des applications à des projets.
- [Utiliser une application Panel](/fr/guides/panel-apps/using/) — statut de compilation, ouverture de l'application, modification et suppression.
- [Créer un agent IA dans une application Panel](/fr/get-started/tutorials/panel-ai-agent/) — un tutoriel : donnez à un agent IA l'API REST comme outils, limitée aux propres autorisations du lecteur.
