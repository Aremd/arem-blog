---
title: "La cohérence est un bien rare"
subtitle: "Aragon, Twyne, et la couche manquante des organisations décentralisées"
description: "Après le hack Kelp et le freeze Arbitrum, le débat se polarise entre centralisation d'urgence et impuissance de principe. Une troisième voie existe."
date: 2026-05-02
slug: coherence-bien-rare
translationKey: coherence-rare-good
categories:
  - DeFi
  - Governance
tags:
  - decentralization
  - governance
  - DAO
  - AI
  - coordination
image: cover.png
---

Le 18 avril 2026, un attaquant a drainé 116 500 rsETH du bridge cross-chain de [Kelp DAO](https://kelpdao.xyz/), soit environ 292 millions de dollars.

Pas à cause d'un bug. À cause d'une décision restée invisible.

Kelp avait choisi une configuration DVN 1-of-1, un seul vérificateur, [malgré les recommandations explicites](https://layerzero.network/blog/kelpdao-incident-statement) de son propre fournisseur d'infrastructure. Ce choix n'a fait l'objet d'aucune proposal, d'aucun débat public, d'aucune trace antérieure à l'incident.

Deux jours plus tard, le [Security Council d'Arbitrum gèle 71 millions de dollars](https://www.coindesk.com/tech/2026/04/22/inside-the-usd71-million-freeze-on-arbitrum-that-has-the-crypto-world-questioning-what-decentralization-really-means).

Le débat s'installe immédiatement. D'un côté, ceux pour qui cet épisode prouve que rien n'est réellement décentralisé. De l'autre, ceux pour qui une intervention d'urgence face à un acteur étatique est non seulement légitime, mais nécessaire.

Les deux positions sont cohérentes. Les deux passent à côté du problème.

Parce que ce qui s'est joué ici ne commence ni avec le hack, ni avec le freeze.

Il commence au moment où une décision structurante peut être prise sans être vue.

> ***La DeFi ne casse pas à cause d'un mauvais code.***
>
> ***Elle casse parce que certaines décisions restent invisibles jusqu'à ce qu'il soit trop tard.***

Et tant que ces décisions resteront invisibles, chaque crise continuera de pousser l'écosystème vers un arbitrage impossible entre centralisation d'urgence et impuissance de principe.

---

## Ce qui devient rare

Les organisations décentralisées ont résolu deux problèmes majeurs. Elles savent agréger du capital avec une efficacité inédite. Elles savent agréger des préférences à travers des mécanismes de vote sophistiqués.

Mais elles n'ont presque rien construit pour une troisième agrégation, pourtant décisive : celle du travail intelligent dans la durée.

Ce travail existe partout. Il prend la forme de recherches, de discussions, d'arbitrages techniques, de désaccords, d'intuitions. Il circule dans des canaux multiples, puis disparaît. Chaque nouvelle session recommence là où la précédente s'était arrêtée sans laisser de trace exploitable.

L'intelligence est produite. Elle n'est pas cumulée.

Ce défaut est longtemps resté invisible, pour une raison simple : l'intelligence était rare.

Ce n'est plus le cas.

L'IA a fait basculer l'intelligence du côté de l'abondance. Ce qui devient limitant n'est plus la production d'analyse ou de code. C'est la capacité à faire tenir ensemble ce qui a été produit.

> ***L'intelligence devient abondante. La cohérence est son goulot d'étranglement.***

Cela apparaît sous des formes différentes mais convergentes. [Aragon](https://blog.aragon.org/) observe que [le volume de décisions croît plus vite que l'attention disponible](https://blog.aragon.org/beyond-proposals-pt-i-automation-and-the-art-of-not-governing/). [Twyne](https://x.com/twynexyz/status/2047302119737196838) constate l'absence de mémoire cumulative et de continuité dans le travail des agents.

Trois constats. Une même limite.

**La coordination permet de distribuer des tâches. Elle ne permet pas de produire une continuité.**

Et dans cet écart se joue une transformation plus profonde. Si une décision structurante peut être prise sans être visible, sans être documentée, sans être opposable, alors le système dans lequel elle s'inscrit n'est pas décentralisé au sens fort.

> ***Nous n'avons pas décentralisé le pouvoir. Nous avons décentralisé son interface.***

Ce déplacement produit des effets très concrets. Il favorise ceux qui contrôlent le contexte, ceux qui détiennent la mémoire informelle, ceux qui peuvent agir sans rendre leurs décisions lisibles.

Kelp n'est pas une anomalie.

C'est un système qui révèle son fonctionnement réel au moment où il échoue.

---

## Aragon, l'art de ne pas gouverner

Dans ce paysage, Aragon propose l'une des architectures les plus avancées.

Leur point de départ est clair : les frameworks de gouvernance onchain, dans leur forme actuelle, n'ont pas permis aux organisations d'agir avec précision. La réponse consiste à déplacer la primitive centrale. Ce n'est plus la proposal qui structure le système, mais la permission.

Avec [OSx](https://blog.aragon.org/the-future-of-governance-is-modular-2/), la gouvernance devient une architecture de droits. Les capacités sont définies explicitement, puis distribuées et combinées à travers des modules.

Le pas décisif apparaît avec la notion de *policy*. Les proposals sont réservées aux décisions véritablement nouvelles. Tout le reste, paiements récurrents, allocations prévisibles, configurations duplicables, est codifié sous forme de règles exécutables.

La formule d'Evan Aronson l'illustre avec précision : *« Policy design is an art of not governing. »*

Il ne s'agit pas de réduire la gouvernance, mais de la déplacer. Une décision n'est plus un événement ponctuel. Elle devient une règle opposable, exécutable sans intervention continue. J'ai déjà travaillé cette intuition philosophiquement dans [un article sur le doux pouvoir](https://arem.blog/fr/post/le-doux-pouvoir/) ; Aronson en donne ici la formulation technique.

Avec [*Linked Accounts*](https://blog.aragon.org/introducing-linked-accounts/), Aragon pousse plus loin cette logique en rendant explicite la finalité des flux. La structure organisationnelle cesse d'être implicite. Elle devient lisible au sein du système lui-même.

Ce travail est considérable. Il introduit une forme de lisibilité qui faisait défaut.

Mais cette lisibilité opère dans un cadre déterministe. Elle suppose que les actions pertinentes peuvent être anticipées, que les règles peuvent être définies à l'avance, que les comportements peuvent être bornés.

Ce qui échappe à ce cadre reste hors champ. Les arbitrages techniques en amont, les décisions informelles, la production de sens, tout ce qui ne se stabilise pas sous forme de règle demeure invisible.

> ***Aragon rend les décisions exécutables. Il ne rend pas leur formation visible.***

---

## Twyne root-archetype, la grammaire des agents

C'est précisément sur ce terrain qu'intervient *root-archetype*, la couche de gouvernance d'agents que l'équipe de Twyne utilise en interne et a publiée sous licence ouverte.

Avec [*root-archetype*](https://github.com/0xTwyne/root-archetype), l'approche consiste à introduire, au-dessus du code applicatif, un référentiel qui ne produit rien directement, mais qui définit les conditions de production elles-mêmes. Rôles, mémoire, protocoles de transmission, contraintes partagées : tout ce qui permet de donner une forme à la continuité du travail.

Le geste est simple. Ses effets sont profonds.

Une session ne repart plus de zéro. Le contexte est transmis. La connaissance cesse de s'évaporer entre les contributions.

> ***L'intelligence commence à se composer.***

Publié sous licence ouverte, ce modèle a vocation à devenir une primitive. Il propose une grammaire minimale à partir de laquelle un écosystème peut se structurer.

La symétrie avec Aragon est claire. Aragon codifie la décision côté capital. Twyne root-archetype codifie la grammaire du travail côté agents. L'un structure ce qui est décidé, l'autre structure ce qui rend la décision possible.

Mais aucun des deux ne rend visible la manière dont ces deux dimensions interagissent.

Twyne lui-même, le protocole de délégation de crédit que cette équipe construit, illustre d'ailleurs précisément pourquoi cette couche manque. La sécurité d'une primitive de crédit dépend de décisions amont, choix de paramètres, sélection d'oracles, configuration des vérificateurs, exactement le type de décisions qui, lorsqu'elles restent invisibles, deviennent les conditions d'une sortie brutale plus tard. Ce qui s'est joué chez Kelp est de cette nature précise, et c'est ce qui rend la question de leur lisibilité non théorique.

---

## La couche manquante

C'est à ce point que le problème devient lisible.

Ni Aragon, ni Twyne root-archetype ne rendent visible la manière dont décision, capital et production s'articulent dans le temps.

C'est précisément cette invisibilité qui a rendu possible Kelp.

Ce qui manque n'est pas un outil supplémentaire. C'est une couche.

Un système capable de rendre visibles les décisions avant qu'elles ne produisent des effets irréversibles.

On peut la nommer simplement : un *Organizational Observability Layer*.

Une telle couche ne se contente pas de tracer des outputs. Elle représente le fonctionnement réel d'une organisation. Elle relie les acteurs, humains et agents, les tâches, les dépendances, les points de décision. Elle conserve la mémoire des choix, des alternatives, des désaccords. Elle formalise la transmission. Elle expose les contraintes. Elle maintient une [attention transversale](https://arem.blog/fr/post/vigilance-transversale/).

> ***Rendre visible le fonctionnement réel d'un système devient une capacité stratégique.***

Aujourd'hui, contribuer signifie souvent ajouter du travail. Dans une organisation dotée d'une telle couche, **contribuer signifie modifier un état partagé.**

C'est ce qui transforme une succession d'initiatives en un processus cumulatif.

Cela permet de distinguer clairement deux notions souvent confondues. La coordination répond à la question de savoir *qui fait quoi*. La cohérence répond à une question plus exigeante : **le système, dans son ensemble, fait-il encore sens ?**

Les outils actuels améliorent la première. La seconde reste largement à construire.

---

## La fausse alternative

Le débat ouvert après le freeze d'Arbitrum révèle les limites de l'état actuel.

Faut-il intervenir ou non ? Faut-il accepter une centralisation d'urgence ou maintenir une fidélité stricte au principe ?

Ces questions sont légitimes. Mais elles arrivent trop tard.

Elles supposent que l'incident a eu lieu et qu'il faut choisir entre deux options imparfaites. Elles ne questionnent pas ce qui a rendu cet incident possible.

Si la configuration DVN avait été rendue visible, documentée, contestable avant son implémentation, le choix aurait pu être différent. Ou assumé. Ou encadré.

Dans tous les cas, il aurait été inscrit dans un espace commun.

> ***Chaque incident de ce type est d'abord un échec de visibilité avant d'être un échec de sécurité.***

Reconnaître cela ne supprime pas le risque, mais déplace le terrain sur lequel il doit être traité.

La décentralisation ne se joue plus uniquement dans la capacité à réagir. Elle se joue dans la capacité à rendre visibles les décisions avant qu'elles ne deviennent irréversibles.

C'est une troisième voie. Pas un compromis, mais un changement.

---

## La pente naturelle

Construire une telle couche implique des tensions réelles.

Une formalisation excessive peut rigidifier le système. Une représentation trop propre peut masquer des désalignements si elle ne fait pas une place explicite au désaccord.

Mais le risque le plus structurant est ailleurs.

Toute couche de lisibilité crée une asymétrie. Celui qui voit plus que les autres dispose d'un avantage. Sans mécanisme explicite, cette asymétrie tend vers la capture : par une équipe centrale, par un fournisseur, par un acteur externe.

> ***Ce qui n'est pas tenu comme un commun devient un point de contrôle.***

Maintenir une couche de cohérence comme un bien partagé est le seul régime qui ne se met pas en place spontanément. Tous les autres émergent sans effort.

---

## Implication politique

**La cohérence n'est pas un problème technique. C'est un choix politique.**

Elle détermine qui peut voir, qui peut comprendre, qui peut contester. Aujourd'hui, ces dimensions restent largement implicites, et donc contrôlées par défaut par ceux qui occupent déjà une position centrale.

Cela interpelle notre vigilance, comme je le proposais déjà dans [la grammaire publique du risque](https://arem.blog/fr/post/public-grammar-of-risk/).

S'engager dans un protocole ne devrait pas se limiter à évaluer son code, sa tokenomics ou sa gouvernance formelle. Il devrait inclure une question plus simple et plus exigeante : *comment les décisions structurantes sont-elles rendues visibles ?*

C'est cette dimension qui a fait défaut chez Kelp. Et c'est elle qui déterminera la robustesse des systèmes à venir.

---

## Pour finir

Aragon et Twyne root-archetype ont posé des briques essentielles.

L'un sur la décision et le capital.

L'autre sur la production et la mémoire.

Mais la couche qui permettrait de les articuler reste à construire.

Sans elle, chaque crise continuera de forcer un choix entre centralisation et impuissance.

Avec elle, les décisions structurantes deviennent visibles avant d'être irréversibles.

> ***Nous n'avons pas échoué à construire des systèmes décentralisés.***
>
> ***Nous avons échoué à les rendre lisibles.***

C'est cette lisibilité, cette cohérence, qui devient aujourd'hui le véritable enjeu, et qui reste à inventer.
