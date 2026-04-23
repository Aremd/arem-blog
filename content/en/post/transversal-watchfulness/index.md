---
title: "Transversal Watchfulness"
description: "What DeFi still does not fund"
date: 2026-04-23
slug: transversal-watchfulness
tags:
  - DeFi
  - Governance
  - Philosophy
  - Public Goods
toc: true
image: cover.png
draft: false
---

A crisis reveals what an economy is willing to pay for—and what it leaves out of the frame. DeFi's April 2026 sequence—the USR depeg and the Kelp exploit—brought into view a structural asymmetry that few analyses have taken the time to name.

Days before Kelp DAO, a depeg hit the stablecoin USR. Users who were alerted early enough got out. That early signal came from [Pharos Watch](https://pharos.watch/), a stablecoin observatory launched two months earlier by an independent developer, self-funded, who recently opened a [public donation page](https://pharos.watch/) simply to keep the project running.

That observation raises a question Kelp only made sharper: **who pays for DeFi to keep making sense of itself?**

## What protocols fund—and what they don't

The picture is more nuanced than it first appears.

Over the past two or three years, DeFi has learned to fund part of its own security layer. [LlamaRisk](https://www.llamarisk.com/) has been an Aave service provider since 2024, with an annual budget of around one million dollars in AAVE, vested against KPIs. [Chaos Labs](https://chaoslabs.xyz/) operates under a similar model. These are professional risk providers, paid by the very DAOs they analyze.

Since February 2026, the Ethereum Foundation has structured a [partnership with the Security Alliance (SEAL)](https://radar.securityalliance.org/protecting-ethereum-users-with-the-ef/) to fund a security engineer dedicated to combating drainers. The [ETH Rangers](https://blog.ethereum.org/en/2026/04/16/eth-rangers-recap) program, which closed in April 2026, funded six months of stipends for seventeen security researchers working on public goods.

Serious startups exist as well. [Blockaid](https://www.blockaid.io/), which published Kelp's technical post-mortem and an open-source DVN audit script, raised 83 million dollars from Ribbit Capital, Google Ventures, Sequoia, and Greylock. Its clients include Coinbase, MetaMask, and Uniswap.

Some core contributors, [banteg](https://github.com/banteg) among them—whose reading of LayerZero's deployment code became a reference during the crisis—draw salaries from major protocols.

So the ecosystem has learned to pay some of its watchers. But it pays them conditionally—and that condition draws a sharp line.

## Servile watchfulness, transversal watchfulness

Every paid structure mentioned above shares one defining property: **it serves an identified payer.**

LlamaRisk looks at Aave because Aave is paying. Chaos Labs follows the same logic. Blockaid protects Coinbase and MetaMask under commercial contracts. SEAL operates with targeted sponsorship from the Ethereum Foundation. The work these actors do is serious and valuable. That does not make them independent observers. **Their mandate is defined by whoever signs the check.**

Alongside this servile watchfulness runs another function, rarer and more exposed: **transversal watchfulness**. The kind that observes several competing protocols without belonging to any of them. That maps the system as a whole rather than acting as a vendor to a single actor. That can call out a problem affecting a potential payer without jeopardizing its own economic survival.

The distinction is easy to state: **servile watchfulness serves an identified payer. Transversal watchfulness observes the whole without belonging to any. The first is funded. The second is not.**

Two structures carry this function almost alone in 2026.

[Pharos Watch](https://pharos.watch/), mentioned above, tracks 205 stablecoins across every major chain. Its founder, [TokenBrice](https://x.com/TokenBrice), recently stated publicly that he funds the tool out of pocket and is aiming to transition to community funding via [Giveth](https://giveth.io/) by the end of 2026.

[DeFiScan](https://www.defiscan.info/), maintained by the [DeFi Collective](https://deficollective.org/), produces an independent evaluation of DeFi protocol decentralization based on a formalized framework. It operates as a non-profit, funded through Giveth and open contributions.

To these, add a handful of researcher-practitioners who publish analysis alongside their primary engagements, and a scattered layer of independent editorial observers.

This transversal layer is structurally fragile. It rests on the personal persistence of a few founders. By definition, it cannot sell services to what it observes without becoming servile itself. And the ecosystem has yet to build mechanisms capable of funding it without capturing it.

## What Weick called *sensemaking*

In the 1970s and 1980s, organizational sociologist [Karl Weick](https://en.wikipedia.org/wiki/Karl_E._Weick) studied collective disasters—the Mann Gulch fire of 1949, the Bhopal catastrophe of 1984—to understand why groups facing ambiguous situations lose their ability to act coherently. His answer fits in one word: *sensemaking*. **Organizational survival under stress depends less on computational power than on the capacity to build a plausible shared understanding of what is happening.**

Weick showed that this function is not automatic. It requires structures capable of producing shared meaning independently of the particular interests of the actors involved. These are the structures that make collective sensemaking possible.

Pharos, DeFiScan, SEAL, banteg, Tay, ZachXBT, LlamaRisk, editorial observers—each contributes to that function. Their coexistence, their ability to read one another, and the fact that their outputs are publicly verifiable make convergence toward a plausible shared account possible.

When these structures are missing, collectives move through crises blindly—not because information is absent, but because **no one is responsible for making it collectively intelligible.**

DeFi is, by design, a high-ambiguity environment: opaque composability, hidden dependencies, a proliferation of actors, no central authority. It requires *sensemaking* more than most technical ecosystems. And yet **the economic structure it has built rewards the production of complexity handsomely, and the production of shared understanding barely at all.**

The tension has been articulated recently by others. [Gitcoin](https://gitcoin.co/), which has carried the question of public goods funding in the Ethereum ecosystem for years, integrated *sensemaking* into its grants architecture starting in 2025. Their formulation, in [recent research](https://gitcoin.co/research/collective-intelligence-protocols-for-thinking-together), goes further: *when AI extends mediation from what we see to how we reason, the risk becomes existential*. They pose the question at a civilizational scale. It arises at DeFi scale with the same force—only closer to home.

What both traditions converge on, each in its own way, is the same reality: **a collective capacity to understand does not emerge on its own.** **It requires dedicated actors, maintained capabilities, stable funding**—and, crucially, **structural independence from the interests being observed.** Without these, there is no shared understanding. There are only competing narratives.

## The funding blind spot

Once the frame is set, the problem facing post-Kelp DeFi comes into focus. It is not that DeFi lacks watchfulness. It has developed plenty. It is that no **mechanism exists to fund its transversal layer.**

When Aave pays LlamaRisk a million dollars a year, it pays for risk analysis on Aave. That is legitimate and useful. But no one, in that equation, is paying LlamaRisk to publicly say something that might embarrass Aave when the moment calls for it. No one is paying for an independent structure to observe Aave *and* its competitors with the same lens. **No one is paying to map dependencies that cut across protocols without belonging to any of them.**

The standard objection to publicly funding this kind of function is that it would create political dependency. It would not. [L2Beat](https://l2beat.com/), for years, has served as a reference for evaluating Ethereum rollups without being captured by any of them—precisely because it built structural independence: diversified funding, transparent methodology, and a stable team. That model exists. It is simply not generalized.

The standard libertarian objection—*users who need this information should pay for it*—runs into a well-known economic constraint: information goods behave like public goods (non-rivalrous, partially non-excludable), which prevents markets from producing them efficiently on their own. No one pays for watchfulness while it exists. Everyone regrets it once it disappears.

It must also be acknowledged that the ecosystem can coordinate when incentives align. [Fluid](https://fluid.instadapp.io/)'s response—together with [Lido](https://lido.fi/), [ether.fi](https://ether.fi/), [1inch](https://1inch.io/), and [KyberNetwork](https://kyber.network/)—to unblock aWETH positions stuck on Aave post-Kelp, processing more than 400 million dollars within hours, is a recent example. That operational coordination is real and valuable. It does not solve the problem raised here. Fluid coordinated with Lido because their users overlapped and their commercial interests converged. No one, in that configuration, was tasked with holding a perspective that might have challenged any of the parties. **Coordination under aligned incentives works. Watchfulness without an economic mandate remains orphaned.**

## What this concretely asks for

A sustainable DeFi—one that lasts a decade rather than a cycle—will have to consolidate mechanisms that are only just beginning to emerge.

**For mature DAOs.** Aave, Uniswap, Lido, Sky sit on treasuries in the hundreds of millions of dollars. Setting aside a fixed fraction—well below one percent—as an endowment for public intelligibility infrastructure, with no service counterpart and no contractual capture, would be a technically trivial move. It has not yet been seriously put on the table.

**For the commercial actors who depend on them.** The emerging intelligence layers selling DeFi attention—dashboards, institutional analytics, paid risk platforms—all rely on public sources (DeFiLlama, DeFiScan, Pharos, independent analysis blogs). In other ecosystems, it is standard practice to reinvest a fraction of revenue into upstream public goods. In DeFi, this norm remains informal at best.

**For public goods funding programs.** [Gitcoin Grants](https://grants.gitcoin.co/), [Optimism RetroPGF](https://app.optimism.io/retropgf), [Octant](https://octant.app/) exist—but are underutilized for transversal intelligibility infrastructure. Coordinating one or more dedicated rounds around this category would have outsized impact.

A concrete example is emerging right now, covering part of that terrain. [TheDAO Security Fund](https://thedao.fund/), endowed with 170 million dollars, launched its first round via [Giveth](https://giveth.io/) on April 21, 2026, with 500 ETH in matching funds for Ethereum and L2 security projects. **Its announced scope** (incident response, security research, on-chain investigation, security tooling, threat intelligence) **covers the defensive layer of transversal watchfulness. It does not cover the analytical and editorial layer that produces meaning outside of incidents**: independent mapping, non-technical observatories, public critical analysis. Still, this marks a first: a public goods funding mechanism explicitly targeting part of this space. Pharos and DeFiScan are eligible. Editorial observers likely are not. The signal matters: the ecosystem is beginning to acknowledge that it must fund what it does not directly consume.

**For users.** Pharos has a Giveth page. DeFiScan as well. SEAL accepts donations. Those who rely on these resources daily can support them directly—not as charity, but as informed self-interest. If these structures disappear, users will be left navigating only protocol-aligned narratives.

**For the ecosystem as a whole.** Cite your sources. Tag contributors. Acknowledge dependencies. Publicly recommend the free tools you rely on. Less material than the other levers, but not trivial. Recognition sustains volunteer motivation and helps lay the groundwork for a more formalized economy of attribution.

A sixth lever deserves to be made explicit. The coming temptation will be to outsource to artificial intelligence what humans have so far provided for free. *Why fund Pharos when an LLM can scrape and summarize peg data?* That logic accelerates the devaluation of functions whose value lies precisely in their human, situated, independent nature. An LLM can process data. It cannot hold a public position against the interests of a protocol it does not understand. Confusing the two will degrade DeFi's epistemic layer more reliably than any exploit.

## To close

A sustainable DeFi is not the one with the most sophisticated protocols. It is the one in which the collective capacity to understand what is happening is funded as seriously as the capacity to generate yield. That is not the case today. This gap is a systemic risk no dashboard currently measures.

The structures carrying this function—Pharos, DeFiScan, independent researcher-practitioners, and editorial observers such as the one behind this piece—will not hold indefinitely without material support. Every founder who burns out, every researcher who shifts to paid work, every independent observer who shuts down their blog creates another blind spot.

The question raised by the April 2026 events is not whether DeFi will survive Kelp or USR.

**It is whether DeFi will equip itself with the material means to keep making sense of itself.**

Without those means, the next crises will be navigated blindly—not for lack of tools, but for lack of people still holding them.
