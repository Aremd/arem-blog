---
title: "La vigilance transversale"
description: "Ce que la DeFi ne finance pas"
date: 2026-04-23
slug: vigilance-transversale
tags:
  - DeFi
  - Governance
  - Philosophy
  - Public Goods
toc: true
image: cover.png
draft: false
---

Une crise révèle ce qu'une économie choisit de financer et ce qu'elle laisse hors champ. La séquence d'avril 2026 en DeFi, dépeg USR, exploit Kelp, a mis en lumière une asymétrie structurelle que peu d'analyses ont nommée.

Quelques jours avant Kelp DAO, un dépeg du stablecoin USR a touché l'écosystème. Les utilisateurs alertés à temps ont pu sortir leurs positions. L'alerte précoce est venue de [Pharos Watch](https://pharos.watch/), un observatoire des stablecoins lancé deux mois plus tôt par un développeur indépendant, financé sur ses fonds personnels, qui a récemment ouvert une [page de dons publique](https://pharos.watch/) pour se maintenir.

Cette observation ouvre une question que Kelp n'a fait que renforcer : **qui paie pour que la DeFi puisse continuer à se comprendre elle-même ?**

## Ce que financent les protocoles, et ce qu'ils ne financent pas

La réponse est plus nuancée qu'on ne pourrait le croire.

La DeFi a appris, depuis deux ou trois ans, à financer une partie de sa propre sécurité. [LlamaRisk](https://www.llamarisk.com/) est service provider d'Aave depuis 2024, avec un budget annuel autour d'un million de dollars en AAVE, vesté contre KPIs. [Chaos Labs](https://chaoslabs.xyz/) opère sur le même modèle. Ce sont des risk providers professionnels, payés par les DAOs qu'ils analysent.

La Fondation Ethereum, de son côté, a structuré depuis février 2026 un [partenariat avec la Security Alliance (SEAL)](https://radar.securityalliance.org/protecting-ethereum-users-with-the-ef/) pour financer un ingénieur sécurité dédié à la lutte contre les drainers. Le programme [ETH Rangers](https://blog.ethereum.org/en/2026/04/16/eth-rangers-recap), clos en avril 2026, avait distribué six mois d'allocation à dix-sept chercheurs sécurité travaillant sur des biens publics.

Les startups sérieuses existent aussi. [Blockaid](https://www.blockaid.io/), qui a publié le post-mortem technique de Kelp et un script d'audit DVN open source, a levé 83 millions de dollars auprès de Ribbit Capital, Google Ventures, Sequoia et Greylock. Ses clients s'appellent Coinbase, MetaMask, Uniswap.

Certains core contributors, comme [banteg](https://github.com/banteg), dont l'analyse du code de déploiement LayerZero a servi de référence pendant la crise, sont salariés de protocoles majeurs.

L'écosystème DeFi a donc appris à payer une partie de ses vigiles. Mais il les paie de façon conditionnelle, et cette condition dessine un angle précis.

## Vigilance servile versus vigilance transversale

Toutes les structures rémunérées mentionnées partagent une propriété commune : **elles servent un payeur identifié**.

LlamaRisk analyse Aave parce qu'Aave le paie pour cela. Chaos Labs aussi. Blockaid protège Coinbase et MetaMask sous contrat commercial. SEAL bénéficie d'un sponsorship ciblé de l'Ethereum Foundation. Ces acteurs font un travail sérieux et utile. Ils ne sont pas pour autant des points de vue extérieurs. **Leur mandat est défini par celui qui signe.**

À côté de cette vigilance servile existe une autre fonction, plus rare et plus exposée : **la vigilance transversale**. Celle qui regarde plusieurs protocoles concurrents sans appartenir à aucun. Celle qui produit une cartographie de l'ensemble sans être le fournisseur d'un acteur particulier. Celle qui peut pointer du doigt un problème chez un payeur potentiel sans mettre en péril sa propre existence économique.

La distinction peut se formuler simplement : **une vigilance servile sert un payeur identifié. Une vigilance transversale regarde l'ensemble sans appartenir à aucun. La première est financée. La seconde ne l'est pas.**

Deux structures incarnent cette fonction de manière quasi-unique en 2026.

[Pharos Watch](https://pharos.watch/), déjà mentionné, qui suit 205 stablecoins à travers toutes les chaînes majeures. Son fondateur, [TokenBrice](https://x.com/TokenBrice), a récemment expliqué publiquement qu'il finance l'outil sur ses propres fonds et qu'il vise un financement communautaire via [Giveth](https://giveth.io/) d'ici fin 2026.

[DeFiScan](https://www.defiscan.info/), maintenu par le [DeFi Collective](https://deficollective.org/), qui produit une évaluation indépendante de la décentralisation des protocoles DeFi selon un framework formalisé. Structure non-profit, financée via Giveth et une logique de contribution ouverte.

À cela s'ajoutent une poignée de chercheurs-praticiens individuels qui produisent de l'analyse publique en marge de leurs engagements principaux, et un tissu diffus d'observateurs éditoriaux indépendants.

Cette couche transversale est structurellement fragile. Elle repose sur la persistance personnelle de quelques fondateurs. Elle ne peut pas, par définition, vendre ses services à l'objet qu'elle observe sans devenir elle-même servile. Et l'écosystème n'a pas encore construit de mécanismes pour la financer sans la capturer.

## Ce que Weick appelait *sensemaking*

Dans les années 1970 et 1980, le sociologue des organisations [Karl Weick](https://en.wikipedia.org/wiki/Karl_E._Weick) a étudié les désastres collectifs, l'incendie de Mann Gulch en 1949, la catastrophe de Bhopal en 1984, pour comprendre ce qui fait qu'un groupe, face à une situation ambiguë, perd sa capacité à agir de façon cohérente. Sa conclusion tient dans un mot : *sensemaking*. **La survie des organisations sous stress dépend moins de leur capacité de calcul que de leur capacité à construire ensemble une compréhension plausible de ce qui leur arrive.**

Weick a montré que cette fonction n'est pas automatique. Elle suppose des structures qui produisent du sens partagé, indépendamment des intérêts particuliers des parties : ce sont les structures qui permettent à cette construction collective d'avoir lieu. Pharos, DeFiScan, SEAL, banteg, Tay, ZachXBT, LlamaRisk, les observateurs éditoriaux ; chacun contribue. Leur coexistence, leur capacité à se lire mutuellement, leurs outputs publics vérifiables, rendent possible la convergence vers un récit plausible. Quand ces structures manquent, les collectifs traversent leurs crises à l'aveugle, non parce que les informations sont absentes, mais parce que **personne n'est chargé de les rendre communes.**

La DeFi est, par construction, un environnement de forte ambiguïté : composabilité opaque, dépendances cachées, multiplication des acteurs, absence d'autorité centrale. Elle a besoin de *sensemaking* plus que la plupart des écosystèmes techniques. Et pourtant, **l'économie qu'elle a bâtie rémunère abondamment la production de complexité et très peu la production de sens partagé.**

Cette tension a été formalisée récemment par d'autres. [Gitcoin](https://gitcoin.co/), qui porte depuis des années la question du financement des biens publics dans l'écosystème Ethereum, a intégré le mot *sensemaking* dans son architecture de grants à partir de 2025. Leur formulation, dans une [recherche publiée récemment](https://gitcoin.co/research/collective-intelligence-protocols-for-thinking-together), va plus loin : *when AI extends mediation from what we see to how we reason, the risk becomes existential*. Ils posent la question à l'échelle civilisationnelle ; elle se pose à l'échelle DeFi avec la même acuité, juste plus près de nous.

Ce que ces deux traditions nomment, chacune à sa manière, c'est la même réalité : **une capacité collective de comprendre ne se produit pas spontanément**. **Elle suppose des acteurs dédiés, des compétences entretenues, un financement stable**, et, c'est le point crucial, une **indépendance structurelle vis-à-vis des intérêts observés**. Sans cela, il n'y a plus de compréhension partagée. Il y a des récits en concurrence.

## L'angle mort du financement

Une fois ce cadre posé, le problème de la DeFi post-Kelp apparaît clairement. Ce n'est pas qu'elle manque de vigilance, elle en a même développé beaucoup. C'est qu'elle n'a pas de **mécanisme pour financer la fraction transversale** de cette vigilance.

Quand Aave paie LlamaRisk un million de dollars par an, c'est pour que LlamaRisk produise des analyses de risque sur Aave. C'est légitime et utile. Mais personne, dans cette équation, ne paie pour que LlamaRisk puisse, au besoin, dire publiquement quelque chose qui dérange Aave. Personne ne paie pour qu'une structure indépendante regarde Aave *et* ses concurrents avec le même œil. **Personne ne paie pour cartographier les dépendances qui traversent plusieurs protocoles sans appartenir à aucun.**

L'argument classique contre le financement public de ce type de fonction est qu'il créerait une dépendance politique. C'est faux. [L2Beat](https://l2beat.com/), pendant des années, a servi de référence pour évaluer les rollups Ethereum sans être capturé par aucun d'eux, précisément parce qu'il a construit une indépendance structurelle, financements diversifiés, méthodologie publique, équipe stable. C'est un modèle qui existe. Il n'est simplement pas généralisé.

L'argument libertarien classique, *les utilisateurs qui ont besoin de cette information n'ont qu'à la payer*, se heurte à un problème économique bien connu : les biens d'information ont des propriétés de bien public (non-rivalité, non-exclusion partielle) qui empêchent leur production par le marché seul. Personne ne paie pour la vigilance tant qu'elle existe encore. Tout le monde la regrette quand elle disparaît.

Il faut reconnaître que l'écosystème sait coordonner quand les incentives s'alignent. La réponse de [Fluid](https://fluid.instadapp.io/), conjointement avec [Lido](https://lido.fi/), [ether.fi](https://ether.fi/), [1inch](https://1inch.io/) et [KyberNetwork](https://kyber.network/), pour débloquer les positions aWETH coincées sur Aave post-Kelp, plus de 400 millions de dollars traités en quelques heures, en est un exemple récent. Cette capacité de coordination opérationnelle est réelle et précieuse. Mais elle ne résout pas le problème posé ici. Fluid s'est coordonné avec Lido parce que leurs utilisateurs étaient communs et leurs intérêts commerciaux convergents. Personne, dans cette équation, n'était chargé de porter un point de vue qui aurait dérangé l'un des participants. **La coordination sous incentives alignés fonctionne. La vigilance qui s'exerce sans mandat économique reste orpheline.**

## Ce que cela demande concrètement

La DeFi durable, celle qui tiendra une décennie plutôt qu'un cycle, devra consolider des mécanismes qui commencent à peine à émerger.

**Pour les DAOs matures.** Aave, Uniswap, Lido, Sky disposent de trésoreries qui se comptent en centaines de millions de dollars. Consacrer un pourcentage fixe, inférieur à un pour cent, à une dotation pour l'infrastructure d'intelligibilité publique, sans contrepartie de service, sans captation contractuelle, serait un geste techniquement trivial. Il n'a pas encore été posé sérieusement.

**Pour les acteurs commerciaux qui en dépendent.** Les intelligence layers émergents qui vendent de l'attention DeFi, les dashboards institutionnels, les plateformes de risk management payantes consomment tous les sources publiques (DeFiLlama, DeFiScan, Pharos, les blogs d'analyse indépendante). Une norme professionnelle, reverser un pourcentage à ces sources, existe déjà dans certains écosystèmes open source. Elle n'est pas formalisée en DeFi.

**Pour les programmes de public goods funding.** [Gitcoin Grants](https://grants.gitcoin.co/), [Optimism RetroPGF](https://app.optimism.io/retropgf), [Octant](https://octant.app/) existent. Ils sont sous-utilisés pour les infrastructures d'intelligibilité DeFi transversale. Une coordination explicite d'un ou plusieurs rounds autour de cette catégorie aurait un impact disproportionné.

Un exemple concret s'ouvre précisément ces jours-ci, sur une fraction de ce périmètre. [TheDAO Security Fund](https://thedao.fund/), doté de $170M au total, lance son premier round via [Giveth](https://giveth.io/) le 21 avril 2026, 500 ETH en matching pool sur les projets de sécurité Ethereum et L2. **Le périmètre annoncé** (incident response, security research, on-chain investigation, security tooling, threat intelligence) **couvre la couche techniquement défensive de la vigilance transversale. Il ne couvre pas la couche analytique et éditoriale qui produit du sens hors incident** : cartographies indépendantes, observatoires non techniques, analyse critique publique. Mais c'est la première fois qu'un mécanisme de public goods funding cible explicitement une partie de ce territoire. Pharos et DeFiScan y sont éligibles ; les observateurs éditoriaux probablement pas. Le signal reste important : l'écosystème commence à reconnaître qu'il doit financer ce qu'il ne consomme pas directement.

**Pour les utilisateurs.** Pharos a ouvert un Giveth. DeFiScan aussi. SEAL accepte des donations. Ceux qui bénéficient quotidiennement de ces ressources peuvent les soutenir directement, pas par charité, par intérêt bien compris. Si ces structures disparaissent, les utilisateurs se retrouvent seuls face aux récits intéressés des protocoles.

**Pour l'ensemble de l'écosystème.** Citer ses sources. Tagger les comptes. Reconnaître les contributions. Recommander publiquement les outils gratuits dont on dépend. Moins matériel que les autres leviers, mais non négligeable, la reconnaissance nourrit la motivation des contributeurs volontaires et pose les bases d'une économie de la considération qui peut se formaliser plus tard.

Il faut ajouter un sixième levier, plus implicite mais décisif. La tentation, dans les années qui viennent, sera de confier à l'intelligence artificielle ce que des humains faisaient gratuitement. *Pourquoi financer Pharos quand un LLM peut scraper et résumer les pegs ?* Cette logique accélère la dévaluation de fonctions qui, précisément, tirent leur valeur de leur caractère humain, situé, indépendant. Un LLM peut analyser des données. Il ne peut pas tenir une position publique contre les intérêts d'un protocole qu'il ne connaît pas. La confusion entre les deux appauvrit la DeFi plus sûrement que ne l'a fait Kelp.

## Pour conclure

Une DeFi durable n'est pas celle des protocoles les plus sophistiqués. C'est celle où la capacité collective de comprendre ce qui s'y passe est aussi solidement financée que la capacité de produire du rendement. Aujourd'hui elle ne l'est pas. Ce décalage est un risque systémique qu'aucun indicateur ne mesure.

Les structures qui tiennent actuellement cette fonction, Pharos, DeFiScan, les chercheurs-praticiens indépendants, les observateurs éditoriaux dont la présente contribution fait partie, ne tiendront pas indéfiniment sans reconnaissance matérielle. Chaque fondateur volontaire qui abandonne, chaque chercheur qui pivote vers un emploi rémunéré, chaque observateur indépendant qui ferme son blog est un point de cécité supplémentaire pour l'écosystème.

La question posée par les deux épisodes d'avril 2026 n'est pas de savoir si la DeFi survivra à Kelp ou à USR. **C'est de savoir si elle se dotera des moyens matériels de continuer à se comprendre elle-même.** Sans ces moyens, les prochains incidents seront traversés à l'aveugle, non parce que les outils manquent, mais parce que personne ne les aura plus tenus.
