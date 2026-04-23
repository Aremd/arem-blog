---
title: "3. La DeFi, laboratoire de la délégation"
description: "Pourquoi la DeFi est l’un des premiers lieux où la question de la délégation doit être pensée avec rigueur."
slug: "defi-laboratoire-de-la-delegation"
tags:
  - AI
  - DeFi
  - Web3
  - Sovereignty
  - Agents
toc: false
translationKey: "series-self-custody-part3"
categories:
  - Série
image: "cover.png"
date: "2026-04-13T13:00:00+00:00"
---

*Dans cette série : [Self-custody, mais jusqu’où ?](/fr/post/self-custody-mais-jusquou/)*

## En DeFi, une idée devient vite une autorisation, une gestion du risque ou une signature.

C’est ce qui fait de la DeFi un terrain d'expérimentations.

Dans bien des environnements numériques, on peut encore vivre longtemps dans l’ambiguïté. Les gestes restent diffus, les conséquences se répartissent, les erreurs se rattrapent. En DeFi, beaucoup moins. Entre une lecture du marché, une recommandation, un clic, une approbation et une exécution, la distance est courte.

Un dashboard n’est donc pas seulement une interface. Il peut orienter une lecture. Un wrapper n’est pas seulement un service. Il peut reformuler la perception du risque. Un agent n’est pas seulement un assistant. Il peut surveiller, proposer, préparer, déclencher, voire exécuter dans certaines bornes.

C’est pourquoi la DeFi voit plus tôt que d’autres secteurs ce que devient la délégation lorsqu’elle cesse d’être un confort abstrait pour prendre la forme de permissions réelles.

## Le protocole ne résume plus le système

On parle encore volontiers de « risque protocolaire », comme si le protocole suffisait à décrire l’objet.

Ce n’est plus vrai.

Entre l’utilisateur et le protocole s’intercale désormais tout un environnement logiciel : interfaces spécialisées, dashboards, wrappers, copilotes, outils treasury, couches de recherche, outils de monitoring, services de coordination, parfois déjà agents d’exécution.

Il ne s’agit pas de soupçonner indistinctement tous ces objets. Il s’agit de comprendre qu’ils déplacent la carte de la confiance. *Même lorsqu’un protocole de base est robuste, l’environnement qui l’entoure peut devenir le lieu principal où se rejoue le problème : ce que l’on voit, ce que l’on comprend, ce que l’on croit comprendre, ce que l’on est poussé à faire.*

## Ce que l’IA change au contexte

Le changement n’est pas seulement conceptuel. Il est matériel.

L’IA abaisse fortement le coût de production des couches logicielles qui se branchent autour des protocoles : dashboards, assistants, wrappers, outils d’analyse, micro-services, couches d’orchestration. Des builders shipent plus vite, testent plus vite, itèrent plus vite. Dans certains cas, c’est une excellente nouvelle.

Mais le coût de la vérification, de la qualification et de la bonne intégration ne baisse pas au même rythme.

Le problème n’est donc pas que des outils soient développés avec l’aide de l’IA. Le problème commence lorsque la baisse du coût de production d’un service n’est pas accompagnée d’une baisse équivalente du coût de sa compréhension, de son contrôle et de son intégration prudente.

*Nous n’avons alors pas seulement plus de software.
Nous avons plus de surfaces de confiance à évaluer, sans avoir les outils pour le faire.*

## Vibe coding : loin du scandale, un révélateur

Le terme a parfois servi de raccourci polémique. Il vaut mieux le manier avec précision.

Tout code assisté par IA n’est pas du *vibe coding* au sens fort. Tout outil construit rapidement n’est pas pour autant peu sérieux. Et il serait absurde d’accuser sans preuve un dashboard, un service ou un projet donné.

Ce que le phénomène rend visible est plus structurel : un milieu où l’on peut produire très vite des couches d’accès, d’analyse, d’orientation et parfois déjà d’exécution ; un milieu où l’apparence de fluidité peut progresser plus vite que la capacité collective à juger ce qui a été réellement relu, compris, cerné et assumé.

Le sujet n’est donc pas la faute morale du builder.
Le sujet est l’accélération du contexte dans lequel l’utilisateur doit discerner.

## Deux protocoles pour rendre le problème visible

[Money League](https://league.money/) et [Polaris](https://polarisfinance.io/) n’ont pas été retenus ici comme deux protocoles « à suivre » de plus, ni comme des objets déjà stabilisés.

Il s’agit, dans les deux cas, de protocoles encore en cours de maturation, dont les formes publiques peuvent évoluer. Ils sont donc mobilisés ici avec prudence, à partir de leur présentation actuelle, comme deux figures provisoires plus que comme deux modèles figés. Polaris, notamment, pourrait tout à fait rencontrer plus explicitement la question de la couche agentique.

Ces deux protocoles sont utiles à notre propos parce qu’ils rendent visible, sous deux formes très différentes, une même question.

Money League se présente comme une infrastructure permissionless pour lancer et coordonner des stablecoins décentralisés, avec une architecture modulaire, des incitations mutualisées et, surtout, une thèse explicite sur l’*agentic money* : marchés prédictifs dans la boucle monétaire, preuve de compétence des agents, agents comme stabilisateurs, horizon d’une économie inter-agents réglée par des actifs pleinement onchain.

Polaris, de son côté, se présente comme un *stablecoin operating system* onchain, immutable et trustless, centré sur un cœur monétaire fortement borné, des mécanismes de yield internes et une logique d’extension modulaire.

L’intérêt du rapprochement tient à cet écart. Money League permet de penser jusqu’où l’agentivité peut remonter dans l’infrastructure monétaire. Polaris rappelle qu’avant toute montée en puissance du système, il faut encore décider ce qui doit rester borné, lisible et politiquement supportable.

## Money League : pousser plus loin l’horizon agentique

Money League est précieux parce qu’il pousse très loin une hypothèse que beaucoup préfèrent encore traiter comme périphérique : la couche agentique peut remonter jusqu’à la monnaie elle-même.

Dans son imaginaire public, les agents ne restent pas à la marge. Ils entrent dans la boucle de stabilisation, de prévision, de coordination et de gestion. Sa force est de rendre visible cet horizon sans détour. Sa limite, au regard de notre question, est qu’il dit davantage sur la souveraineté du système que sur la souveraineté pratique de celui qui délègue.

## Polaris : rappeler la question de la constitution

Polaris est, de ce point de vue, un contrepoint utile.

Son intérêt public ne tient pas d’abord à une agentivité spectaculaire, mais à une architecture plus constitutionnelle : un cœur immuable, un stewardship limité, un petit nombre de paramètres ajustables dans des limites codées.

Sa force est de rappeler qu’un système ne devient pas plus légitime parce qu’il automatise davantage. Il devient plus lisible lorsqu’il sait distinguer ce qu’il doit déléguer, ce qu’il peut ajuster, et ce qu’il doit soustraire à la variation ordinaire.

## Ce qu’ils montrent ensemble

Pris ensemble, ces deux cas rendent visible une tension que la DeFi rencontrera de plus en plus souvent : jusqu’où laisser monter l’agentivité, et à partir de quel point faut-il, au contraire, renforcer la constitution du système ?

Ce n’est déjà plus une simple question d’UX.
C’est une question monétaire, institutionnelle et opérationnelle.

## Morin : aucune limitation locale n’abolit le problème du système

C’est ici que [Morin](https://archive.mcxapc.org/docs/apc/0901montuori.pdf) nous aide à éviter deux naïvetés symétriques.

La première consisterait à croire que plus de design, plus de limitations et plus de permissions explicites suffisent à résoudre le problème.

La seconde, à l’inverse, serait de conclure que tout devient aussitôt suspect dès qu’une couche supplémentaire apparaît.

Morin oblige à tenir ensemble deux vérités.

Oui, il faut des limites.
Oui, il faut des permissions bornées.
Oui, il faut des architectures lisibles.

Mais aucune borne locale, aucun module élégant, aucune preuve ponctuelle d’intégrité ne supprime l’écologie de l’action. Un système peut être bien conçu localement et produire malgré tout des effets d’ensemble inattendus : comportements mimétiques, routines de surconfiance, dépendances nouvelles, coordination procyclique, incitations mal lues, angles morts collectifs.

La question n’est donc pas seulement : l’action était-elle autorisée ?
Elle est aussi : que produit la multiplication de ces actions dans un milieu peuplé d’outils, de dashboards, d’agents et d’utilisateurs qui ne voient pas tous le même monde ?

## La vérifiabilité : aide précieuse, pas substitut au discernement

Il est normal que les appels à une *sovereign AI* ou à une *verifiable AI* rencontrent un écho dans le monde web3. Ils parlent une langue familière : contrôle, intégrité, preuves, réduction de la confiance aveugle.

Cette direction est importante. Elle peut rendre certaines délégations plus lisibles, plus attestables, plus contenues.

Mais il faut maintenir une hiérarchie des problèmes.

La vérifiabilité ne remplace pas le bon sens. Elle ne décide pas, à notre place, ce qu’il fallait déléguer. Elle ne garantit pas que les effets d’ensemble seront désirables.

Les preuves, les logs, les limites, les politiques d’action et les primitives cryptographiques peuvent améliorer l’intégrité de certaines opérations. Elles ne dispensent ni de définir le mandat, ni d’assumer les limites, ni de répondre des usages.

<style>
.arem-card{background:var(--card-bg,#f2f3f5);border-radius:14px;padding:30px 26px 22px;font-family:inherit;width:100%;margin:28px 0 22px;border:1px solid var(--card-border,rgba(0,0,0,.08))}
.arem-card-title{font-size:1.1em;font-weight:700;color:var(--card-text,#1a2332);letter-spacing:-.01em;line-height:1.2;margin-bottom:6px}
.arem-card-sub{font-size:.95em;color:var(--card-muted,#556070);line-height:1.5;margin-bottom:18px}
.arem-card-sep{height:1px;background:var(--card-sep,rgba(0,0,0,.1));margin-bottom:18px}
.arem-card-list{display:flex;flex-direction:column;gap:10px}
.arem-card-item{padding:12px 16px;border-radius:10px;background:var(--card-item-bg,#ffffff);border:1px solid var(--card-border,rgba(0,0,0,.08))}
.arem-card-item-title{font-size:.95em;font-weight:700;color:var(--card-text,#1a2332);margin-bottom:5px}
.arem-card-item-text{font-size:.95em;line-height:1.6;color:var(--card-muted,#556070)}
html[data-scheme="dark"] .arem-card{--card-bg:#141c23;--card-border:rgba(255,255,255,.06);--card-text:#e8f0f8;--card-muted:#7a9ab0;--card-sep:rgba(255,255,255,.08);--card-item-bg:#0f1419}
</style>

<div class="arem-card">
  <div class="arem-card-title">Contrôle, intégrité, mesure</div>
  <div class="arem-card-sub">Ce qui monte aujourd’hui dans le monde web3 n’est pas illégitime. Il faut simplement garder l’ordre des problèmes.</div>
  <div class="arem-card-sep"></div>
  <div class="arem-card-list">
    <div class="arem-card-item">
      <div class="arem-card-item-title">Sovereign AI</div>
      <div class="arem-card-item-text">Traite la question du contrôle : où tourne le système, qui dépend de qui, quelles données sortent, quelles permissions sont engagées.</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">Verifiable AI</div>
      <div class="arem-card-item-text">Traite la question de l’intégrité : ce qui peut être attesté, relu, prouvé ou reconstitué.</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">Mais la mesure reste décisive</div>
      <div class="arem-card-item-text">Aucune de ces deux directions ne dispense de traiter la vraie question : que déléguer, à quelles limites, et avec quelle possibilité de reprise en main ? Les mathématiques et la cryptographie peuvent rendre certaines opérations plus attestables ; elles ne remplaceront ni le jugement, ni la responsabilité, ni l’écologie de l’action.</div>
    </div>
  </div>
</div>

<div class="arem-card">
  <div class="arem-card-title">Grille minimale pour évaluer un outil DeFi assisté ou agentique</div>
  <div class="arem-card-sub">Avant d’utiliser un dashboard, un wrapper, un copilote, un agent ou un service tiers, il vaut la peine de passer l’objet au filtre suivant.</div>
  <div class="arem-card-sep"></div>
  <div class="arem-card-list">
    <div class="arem-card-item">
      <div class="arem-card-item-title">1. Nature de l’objet</div>
      <div class="arem-card-item-text">S’agit-il d’un protocole, d’une interface, d’un outil tiers, d’un agent, ou simplement d’une couche de visualisation ?</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">2. Niveau d’intervention</div>
      <div class="arem-card-item-text">Informe-t-il, recommande-t-il, prépare-t-il une action, ou agit-il réellement ?</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">3. Permissions</div>
      <div class="arem-card-item-text">A-t-il accès à un wallet, à des messages, à des données privées, à des automatisations, à une exécution onchain, à des appels externes ?</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">4. Bornes</div>
      <div class="arem-card-item-text">Quelles sont les limites explicites : montants, types d’actions, confirmations, délais, whitelist, sandbox, périmètre fonctionnel ?</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">5. Vérifiabilité</div>
      <div class="arem-card-item-text">Qu’est-ce qui peut être relu, compris, audité ou reconstitué ?</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">6. Réversibilité</div>
      <div class="arem-card-item-text">Peut-on couper l’outil sans perdre l’accès au protocole, au risque de base ou à sa capacité d’action essentielle ?</div>
    </div>
    <div class="arem-card-item">
      <div class="arem-card-item-title">7. Responsabilité</div>
      <div class="arem-card-item-text">Qui assume quoi : le protocole, le builder de l’outil, l’opérateur, l’utilisateur ? Si cette réponse reste floue, la confiance l’est aussi.</div>
    </div>
  </div>
</div>

## Ce que cette série voulait montrer

Le parcours peut se résumer simplement.

Le monde crypto a appris à défendre ses actifs contre la capture. Il découvre maintenant qu’il doit apprendre à défendre avec la même rigueur son attention, son discernement, son organisation et sa capacité d’agir.

Le problème ne se résout ni par la nostalgie ni par l’accélération pure.

Il demande des protocoles plus lisibles, des outils mieux bornés, des architectures moins magiques, des builders plus responsables, et des utilisateurs moins enclins à confondre puissance nouvelle et abdication discrète.

Il demande aussi une chose plus difficile : accepter qu’aucune preuve locale, qu’aucune automatisation élégante, qu’aucune intégrité cryptographique ponctuelle ne remplacera jamais entièrement la sagesse sur les effets d’ensemble.

C’est sans doute là que se joue la suite la plus sérieuse de la promesse de la crypto.

*Il ne s'agit pas seulement protéger ce que nous possédons.
Mais apprendre à ne pas céder trop vite ce qui nous permet encore d’agir.*
