---
title: "Polaris : une discipline rare"
slug: "polaris-une-discipline-rare"
description: "Polaris hérite de Liquity et corrige son propre canal de capture latent avant déploiement. Note d'observation sur un geste rare, et sur ce qu'il reste à voir."
date: 2026-05-04
translationKey: polaris-rare-discipline
image: "cover.png"
categories:
  - Analysis
tags:
  - Polaris
  - Liquity
  - Governance
  - Stewardship
  - DeFi
  - Stablecoins
draft: false
---

Un protocole DeFi se juge rarement sur sa présentation, mais presque toujours sur son comportement en période de stress. Il existe toutefois une catégorie de situations intermédiaires, avant déploiement, qui méritent d'être identifiées car elles sont rares : une équipe formule, conteste et corrige sa propre architecture *avant* qu'un problème de gouvernance ne l'impose (attaque, tentative de capture de gouvernance, ou encore inertie de la gouvernance). Polaris vient de mener à bien cette révision. [Polaris](https://polarisfinance.io/) est un protocole de stablecoins décentralisés en pre-launch, qui hérite de la lignée Liquity et propose une architecture stewardship en lieu et place d'une gouvernance classique. Cet article vise à décrire la révision avec précision, à identifier ce qu'elle apporte et à esquisser ce qu'il reste à observer pour que la promesse tienne.

## Une lignée

Polaris ne part pas de zéro, et sa qualité tient en partie à la rigueur avec laquelle le protocole assume cette dette. L'équipe core engineering est l'équipe de développement de Liquity v1 et v2 — ceux qui ont sécurisé plus de 2 milliards de TVL sans aucun exploit, à travers Luna, FTX et SVB. La recherche initiale a été développée au sein de Liquity AG par Robert Lauko, désormais Research Advisor. Laurens Kessenich (PhD en physique de l'ETH Zurich) porte l'architecture protocolaire et la modélisation. Robert Mullins, après avoir construit le BD de Jumper/LI.FI, dirige les opérations et les partenariats. Brice apporte son retour d'expérience accumulé chez Liquity, ParaSwap, le DeFi Collective, DeFiScan, Pharos Watch et le GHO Liquidity Committee d'Aave — où il avait nommé deux ans avant la communauté des conflits d'intérêts structurels. Cette généalogie n'est pas un argument d'autorité, c'est un substrat. Elle donne au projet une surface de contact avec les échecs antérieurs que rares sont les protocoles à pouvoir convoquer aussi explicitement.

Dans [*Path to the North Star*](https://polarisfinance.io/blog/path-to-the-north-star/), Brice trace la lignée des stablecoins décentralisés : SAI, DAI, LUSD, BOLD, et maintenant pUSD. Chaque chaînon a appris quelque chose que le suivant essaie de ne pas répéter. La sagesse est la condition de l'ambition : on ne propose pas une nouvelle architecture sans avoir compris *pourquoi* les précédentes ont plié. Cette posture — comprendre les échecs avant de proposer — est ce qui distingue Polaris d'un énième projet pre-launch, et ce qui rend son geste actuel intéressant à observer.

## Une discipline

Le 3 mars 2026, Polaris publie [*Stewardship, not Governance*](https://polarisfinance.io/blog/stewardship-not-governance/). L'article réunit deux choses : une critique frontale de l'état des gouvernances DeFi en 2026 — *« there is no defending governance in 2026 »* — et la proposition d'une troisième voie entre l'ungouvernance pure à la Liquity v1 et la gouvernance professionnalisée à la Aave. Le cœur du protocole est immuable. Une couche stewardship circonscrite gouverne ce qui ne peut être ni automatisé ni purement incité : l'admission au StablecoinOS, la paramétrisation des CDP, les positions de trésorerie, et — point crucial à ce stade — un budget *gauge emissions* de 25 % de POLAR sur quatre ans, voté par époque.

Cinq semaines plus tard, le 13 avril, [*Sustaining the Ecosystem: pETH & pUSD Flows*](https://polarisfinance.io/blog/polaris-flows/) ouvre par cette phrase : *« we went back to the drawing board »*. L'aveu est explicite. L'équipe a vu, dans sa propre architecture, que le canal *gauge emissions* — même soigneusement configuré, même borné par stewardship — héritait du *« governance picks winners failure mode »* que stewardship était précisément censée éviter. C'est une refonte complète de la couche d'incitations, qui supprime *gauges*, *bribes* et *weight wars* et les remplace par un mécanisme contract-enforced d'auto-distribution en hard assets.

L'élégance technique est réelle et révèle une discipline. Une équipe qui voit un canal de capture latent dans sa propre architecture, qui le formule publiquement, et qui le supprime au prix d'une refonte avant déploiement, fait quelque chose que ni Maker, ni Aave, ni la plupart des protocoles établis ne font. La capacité d'auto-restriction est probablement, en 2026, la qualité la plus rare en DeFi. Elle ne se vérifie pas sur les promesses pre-launch ; elle se vérifie sur les renoncements.

## Ce que Flows modifie

Quatre éléments sont simultanément remaniés, et c'est leur composition qui fait la valeur du dispositif.

La devise du jeu change. L'incitation n'est plus distribuée en token de gouvernance (POLAR) mais en hard assets (pETH et pAssets) issus directement des revenus du protocole. La conséquence, plus qu'économique, est politique : il n'y a plus d'instrument de gouvernance à monnayer, donc plus de marché de bribes possible. La devise de capture a été supprimée. Toute nouvelle émission de POLAR exige désormais un burn pETH via le mécanisme de conversion, ce qui ferme la boucle économique sur elle-même.

La logique allocative inverse l'incitation. L'allocation passe d'un vote par époque à une formule auto-exécutée : la part du Flow reçue par un contrat est égale à sa part du pETH ou pUSD whitelisté. Les intégrateurs ne lobbyent plus pour obtenir des incentives ; ils attirent des utilisateurs pour augmenter leur part. Le système rétribue *« capture and usage »* plutôt que *« lobbying, visibility and vested interests »*. Cette inversion n'est pas cosmétique : elle modifie qui parle, qui pèse, et de quoi est faite la conversation publique autour du protocole.

Concrètement : sous le modèle des gauges qu'a normalisé Curve, et que le Stewardship v1 de Polaris reproduisait, un protocole tiers qui veut des émissions doit accumuler du veToken, louer du vote via Convex, ou verser des bribes sur Votium ou Hidden Hand. Une économie politique entière s'est développée autour — équipes BD spécialisées dans le lobbying, dashboards de profitabilité par bribe, alliances de votants. Sous Flows, ces couches disparaissent par construction : un intégrateur qui veut une part importante ne peut ni l'acheter ni la lobbyer ; il doit attirer des utilisateurs, parce que sa part est mécaniquement proportionnelle à sa part du pETH ou pUSD whitelisté. La conversation publique cesse de porter sur « qui vote pour qui » et porte sur « qui propose la meilleure expérience ».

Le scope stewardship se contracte radicalement. En régime normal, point décisif, *« stewards have nothing to do »*. Trois moments seulement appellent leur intervention : whitelist d'admission, réglage du *weight* lors d'une négociation de revenue-share, éviction d'un acteur déloyal. Le pouvoir résiduel est extrêmement circonscrit, et il n'a plus de canal d'extraction continu. La charge sur les stewards passe d'une obligation de présence permanente — qui produit la spirale d'épuisement documentée dans la plupart des DAOs — à une présence par événement.

La dilution des fondateurs devient mécanique. La génération de POLAR est désormais entièrement liée à la conversion pETH→POLAR, à un taux auto-régulé plutôt que fixe. Plus le protocole croît, plus l'équipe est diluée. Cette asymétrie est assumée explicitement : *« either it works, founders get diluted; no traction, no dilution »*. Avec une nuance structurelle : chaque unité de dilution correspond à une amélioration concrète du protocole — pETH brûlé, floor price relevé, ETH libéré en yield. C'est ce qui distingue Flows des modèles d'émission classiques, où inflation du token et santé du protocole sont découplées. Ici, la dilution n'est pas un coût à supporter pour faire fonctionner le système — elle est le signe qu'il fonctionne.

Pris ensemble, ces quatre déplacements suppriment plusieurs canaux de capture simultanément. Et ils démontrent quelque chose qui mérite d'être noté dans un plus large débat : il *est possible* de réduire substantiellement la gouvernance d'un protocole sans tomber dans l'ungouvernance pure. Polaris propose une alternative à la non-gouvernance radicale, et accepte une couche d'orchestration minimale.

## Ce qui reste à observer

La rigueur d'observation consiste à identifier où la capture (qui ne disparaît jamais) s'est déplacée. *Après* le déploiement, pas avant.

**La whitelist comme point de pouvoir résiduel.** Brice le reconnaît dans Flows : *« Whitelists can be lobbied without vigilance. Any system with a human-controlled whitelist is subject to influence. »* Le pouvoir d'admettre ou de refuser un intégrateur reste un pouvoir réel. Interrogée sur la composition initiale du Flow whitelist, l'équipe a précisé que la première vague serait limitée aux instances CDP pUSD/pGOLD côté pETH et au Stability Pool côté pUSD/pGOLD — un bootstrap interne sans admission tierce au démarrage. Cette configuration élimine la zone d'ombre la plus évidente d'un déploiement stewardship en ne mobilisant aucune décision discrétionnaire d'admission au lancement. La question se posera donc à partir du *premier* vote d'intégrateur tiers.

L'équipe a indiqué deux points sur ce sujet. D'une part, l'admission post-bootstrap fonctionnera *« par jurisprudence et processus »*, sans framework écrit ex ante. C'est défendable — un framework figé ex ante est lui-même capturable, et la jurisprudence permet d'apprendre cas par cas — mais cela signifie que les premiers votes feront précédent. Qui les pilote pèsera durablement. D'autre part, et c'est un acquis nommé, *« responsible disclosure should happen on any proposal »* : engagement clair à publier les liens éventuels dans les propositions de vote. Cet engagement vaut beaucoup s'il est tenu. Il manque dans la plupart des DAOs établies aujourd'hui.

**L'obligation déclarative des engagements de revenue-share.** Le scénario *Deceiver* — un intégrateur qui négocie un weight 1.0 contre un revenue-share, puis ne tient pas l'engagement — est traité par éviction sociale, pas par obligation cryptographique. La réponse de l'équipe est franche : *« declarative, enforced by stewardship kicking out violating actors »*. La garantie est sociale et économique, pas technique : un *Deceiver* éjecté perd l'accès permanent au Flow, ce qui constitue un coût élevé pour un gain transitoire. C'est défendable — exiger une garantie cryptographique ici reviendrait à exiger une chose que ni Aave, ni Maker, ni Liquity ne fournissent — mais cela dépend entièrement de la vigilance des stewards et de l'existence de dashboards communautaires pour détecter les manquements rapidement. À documenter dans le temps.

**La gestion sous stress.** Le minimum hardcodé de 30 % vers le Stability Pool est juste : c'est ce qui maintient la solvabilité. Interrogée sur la conduite à tenir quand un épisode de stress comprime mécaniquement les pUSD Flows pour tous les receveurs, l'équipe a précisé un point qui mérite d'être mentionné : il n'y a pas de levier manuel. *« No manual override is needed to face it »* — la part SP first est automatique, la compression des autres parts est la conséquence directe de la baisse des revenus, et les stewards n'ont pas de bouton à actionner en temps réel. Le système gère la crise par sa structure même, pas par décision humaine. C'est conceptuellement plus radical qu'il n'y paraît, et c'est aligné avec la doctrine *Structure Over Trust* : sous stress, on ne demande pas aux stewards d'arbitrer — on a arbitré au déploiement, en hardcodant le minimum SP, et la mécanique fait le reste.

Le rôle du stewardship sous stress se déplace donc de l'arbitrage vers l'apprentissage : *« we're definitely keen on learning from such episodes and helping the stewardship to step up from one to the other »*. La question d'observation pertinente n'est plus *« comment la discrétion sera-t-elle exercée ? »* mais *« comment l'expérience d'un épisode capitalise-t-elle pour le suivant ? »*. Une discipline de retours d'expérience documentés — ce que les conditions de déclenchement ont révélé, comment les intégrateurs ont été informés, ce qui a fonctionné ou pas dans la communication — reste une matière utile pour l'observation longitudinale, sans porter cette fois le caractère opposable d'une vérification de discrétion.

**La dilution conditionnelle au succès.** Le mécanisme de dilution programmée des fondateurs est élégant, mais conditionnel : *« either it works, founders get diluted; no traction, no dilution »*. Si le volume de conversions pETH→POLAR stagne, la dilution stagne aussi. La concentration initiale ne se résorbe pas par calendrier — elle se résorbe par flux. Cela n'invalide rien, mais cela signifie que la décentralisation effective de la gouvernance reste une *hypothèse à valider sur trajectoire*, pas une garantie ex ante. L'équipe envisage un rapport périodique — mensuel ou trimestriel — sur l'activité stewardship, et cite explicitement les indicateurs à suivre : nombre de vePOLAR lockers, pourcentage de votes délégués, pourcentage de votes actifs, concentration. C'est exactement le type de matière que l'observation transversale extérieure peut reprendre et codifier dans la durée.

## En quoi cette posture de l'équipe compte au-delà de Polaris

Indépendamment de ce que Polaris deviendra en mainnet — et il y aura des épisodes de stress, il y en a toujours — le geste de l'auto-correction Stewardship v1 → Flows constitue en soi un apport à l'écosystème. Une démonstration qu'une équipe DeFi peut formuler, contester et corriger sa propre architecture *avant* qu'elle ne soit testée par la captation. Cela ne paraît rien dit comme ça ; en pratique, c'est une qualité dont peu de projets ont fait preuve. Maker ne l'a pas fait. Aave non plus. La plupart des protocoles établis attendent qu'un événement révèle une faille pour la nommer — et alors l'urgence du sauvetage écrase toute réflexion. Polaris fait l'inverse : il nomme, il corrige, il publie, avant même que tout soit lancé.

Si Polaris défaille demain, le geste reste valide. Si Polaris réussit, le geste devient enseignement. Dans les deux cas, ce qui mérite d'être documenté *maintenant*, ce n'est pas un pari sur le résultat, c'est la discipline qui rend la suite observable. La qualité d'une architecture ne se mesure pas à l'absence de tensions résiduelles — il y en a toujours. Elle se mesure à la précision avec laquelle ces tensions sont nommées par ceux qui les construisent, et à la lisibilité qu'elles offrent à ceux qui les observent.

C'est, structurellement, le même mouvement que celui qui m'occupe depuis [*Coherence is the Scarce Good*](/fr/post/coherence-bien-rare/) : ce qui compte n'est pas le verdict, c'est la grammaire qui rend le verdict possible. Polaris vient d'écrire une page de cette grammaire. Reste à voir si l'écriture tient sous pression.

---

*Article d'observation. Pas de position détenue dans Polaris à la date de publication. Le testnet 2, qui porte l'architecture Flows, a été [lancé le 7 mai 2026](https://x.com/polarisfinance_/status/2052025595068813485). Le suivi continuera dans les mois qui viennent, à mesure que le protocole approche du mainnet et que les premiers votes stewardship interviendront.*
