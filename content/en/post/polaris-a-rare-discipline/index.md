---
title: "Polaris: A Rare Discipline"
slug: "polaris-a-rare-discipline"
description: "Polaris inherits from Liquity and corrects its own latent capture channel before deployment. An observational note on a rare gesture, and on what remains to be seen."
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

A DeFi protocol is rarely judged on its presentation, but almost always on how it performs under stress. There is, however, a category of intermediate situations — prior to deployment — that are worth highlighting because they are rare: a team formulates, challenges, and corrects its own architecture *before* a governance issue forces it to do so (such as an attack, an attempt to hijack governance, or governance inertia). Polaris has just completed this review. [Polaris](https://polarisfinance.io/) is a pre-launch decentralized stablecoin protocol, inheriting from the Liquity lineage and proposing a stewardship architecture in place of conventional governance. This article aims to describe the review in detail, identify what it brings to the table, and outline what remains to be observed to ensure the promise is fulfilled.

## A Legacy

Polaris isn't starting from scratch, and its quality stems in part from the rigor with which the protocol addresses this legacy. The core engineering team is the development team behind Liquity v1 and v2 — the team that secured over $2 billion in TVL without a single exploit, through Luna, FTX, and SVB. The initial research was developed at Liquity AG by Robert Lauko, now a Research Advisor. Laurens Kessenich (PhD in Physics from ETH Zurich) leads protocol architecture and modeling. Robert Mullins, after building the business development team at Jumper/LI.FI, leads operations and partnerships. Brice brings his accumulated experience from Liquity, ParaSwap, the DeFi Collective, DeFiScan, Pharos Watch, and Aave's GHO Liquidity Committee — where he had flagged structural conflicts of interest to the community two years prior. This lineage is not an argument from authority; it is a foundation. It gives the project a point of reference with past failures that few protocols can draw upon so explicitly.

In [*Path to the North Star*](https://polarisfinance.io/blog/path-to-the-north-star/), Brice traces the lineage of decentralized stablecoins: SAI, DAI, LUSD, BOLD, and now pUSD. Each link in the chain has learned something that the next one tries not to repeat. Wisdom is the prerequisite for ambition: one does not propose a new architecture without having understood *why* the previous ones failed. This approach — understanding failures before proposing solutions — is what sets Polaris apart from yet another pre-launch project, and what makes its current move worth watching.

## A Discipline

On March 3, 2026, Polaris published [*Stewardship, not Governance*](https://polarisfinance.io/blog/stewardship-not-governance/). The article brings together two things: a direct critique of the state of DeFi governance in 2026 — *"there is no defending governance in 2026"* — and the proposal of a third way between pure non-governance à la Liquity v1 and professionalized governance à la Aave. The core of the protocol is immutable. A limited stewardship layer governs what cannot be automated or purely incentivized: admission to StablecoinOS, CDP parameterization, treasury positions, and — a crucial point at this stage — a *gauge emissions* budget of 25% of POLAR over four years, voted on per epoch.

Five weeks later, on April 13, [*Sustaining the Ecosystem: pETH & pUSD Flows*](https://polarisfinance.io/blog/polaris-flows/) opens with this sentence: *"we went back to the drawing board."* The admission is explicit. The team saw, within its own architecture, that the *gauge emissions* channel — even when carefully configured, even when bounded by stewardship — inherited the *"governance picks winners failure mode"* that stewardship was precisely meant to avoid. This is a complete overhaul of the incentive layer, which removes *gauges*, *bribes*, and *weight wars* and replaces them with a contract-enforced mechanism for self-distribution in hard assets.

The technical elegance is real and reveals discipline. A team that sees a latent capture channel in its own architecture, articulates it publicly, and eliminates it at the cost of a pre-deployment overhaul is doing something that neither Maker, nor Aave, nor most established protocols do. The capacity for self-restraint is likely, in 2026, the rarest quality in DeFi. It is not verified by pre-launch promises; it is verified by what is left out.

## What Flows is Changing

Four elements are being overhauled simultaneously, and it is their combination that gives the system its value.

The game's currency is changing. Incentives are no longer distributed as governance tokens (POLAR) but as hard assets (pETH and pAssets) derived directly from the protocol's revenue. The consequence is political rather than merely economic: there is no longer a governance instrument to monetize, so no more trading of governance tokens is possible. The capture token has been removed. Any new issuance of POLAR now requires a pETH burn via the conversion mechanism, which closes the economic loop upon itself.

The allocation logic reverses the incentive structure. Allocation shifts from a vote per epoch to a self-executing formula: the share of Flow received by a contract is equal to its share of whitelisted pETH or pUSD. Integrators no longer lobby for incentives; they attract users to increase their share. The system rewards *"capture and usage"* rather than *"lobbying, visibility, and vested interests"*. This reversal is not cosmetic: it changes who speaks, who holds sway, and what the public conversation around the protocol is made of.

In concrete terms: under the gauge model standardized by Curve — and replicated by Polaris's Stewardship v1 — a third-party protocol seeking emissions must accumulate veTokens, rent votes via Convex, or pay bribes on Votium or Hidden Hand. An entire political economy has developed around this — BD teams specializing in lobbying, dashboards tracking profitability per bribe, and voter alliances. Under Flows, these layers disappear by design: an integrator seeking a significant share cannot buy or lobby for it; they must attract users, because their share is mechanically proportional to their share of whitelisted pETH or pUSD. The public conversation shifts from "who votes for whom" to "who offers the best experience."

The scope of stewardship shrinks radically. Under normal conditions — and this is the key point — *"stewards have nothing to do."* Only three moments call for their intervention: admission to the whitelist, adjusting the *weight* during a revenue-share negotiation, and removing a disloyal actor. Residual power is extremely limited, and it no longer has a continuous channel for extraction. The burden on stewards shifts from an obligation of constant presence — which produces the spiral of exhaustion documented in most DAOs — to an event-based presence.

Founder dilution becomes automatic. POLAR generation is now entirely tied to the pETH→POLAR conversion, at a self-regulating rather than fixed rate. The more the protocol grows, the more the team is diluted. This asymmetry is explicitly acknowledged: *"either it works, founders get diluted; no traction, no dilution."* With a structural nuance: each unit of dilution corresponds to a concrete improvement in the protocol — pETH burned, floor price raised, ETH released as yield. This is what distinguishes Flows from traditional issuance models, where token inflation and protocol health are decoupled. Here, dilution is not a cost to bear in order to make the system work — it is a sign that it is working.

Taken together, these four shifts eliminate several channels of capture simultaneously. And they demonstrate something worth noting in a broader debate: it *is possible* to substantially reduce a protocol's governance without falling into pure ungovernance. Polaris offers an alternative to radical ungovernance, accepting a minimal layer of orchestration.

## What Remains to Be Observed

Rigorous observation involves identifying where capture (which never disappears) has shifted. *After* deployment, not before.

**The whitelist as a point of residual power.** Brice acknowledges this in Flows: *"Whitelists can be lobbied without vigilance. Any system with a human-controlled whitelist is subject to influence."* The power to admit or reject an integrator remains a real power. When asked about the initial composition of the Flow whitelist, the team clarified that the first wave would be limited to pETH-side pUSD/pGOLD CDPs and the pUSD/pGOLD-side Stability Pool — an internal bootstrap with no third-party admission at launch. This configuration eliminates the most obvious gray area of a stewardship deployment by not involving any discretionary admission decisions at launch. The question will therefore arise starting with the *first* third-party integrator vote.

The team highlighted two points on this subject. First, post-bootstrap admission will operate *"through case law and process"*, without a predefined framework. This is defensible — a rigid, predefined framework is itself susceptible to capture, and case law allows for learning on a case-by-case basis — but it means that the initial votes will set a precedent. Whoever steers them will have a lasting influence. On the other hand, and this is a stated principle, *"responsible disclosure should happen on any proposal"*: a clear commitment to publish any relevant links in voting proposals. This commitment is worth a great deal if upheld. It is missing in most established DAOs today.

**The declarative obligation of revenue-share commitments.** The *Deceiver* scenario — an integrator who negotiates a weight of 1.0 in exchange for a revenue share, then fails to honor the commitment — is addressed through social expulsion, not cryptographic enforcement. The team's response is straightforward: *"declarative, enforced by stewardship kicking out violating actors."* The guarantee is social and economic, not technical: an ejected *Deceiver* loses permanent access to Flow, which is a high cost for a temporary gain. This is defensible — demanding a cryptographic guarantee here would amount to demanding something that neither Aave, Maker, nor Liquity provide — but it depends entirely on the vigilance of the stewards and the existence of community dashboards to detect breaches quickly. To be documented over time.

**Stress management.** The hardcoded minimum of 30% allocated to the Stability Pool is fair: this is what maintains solvency. When asked about the course of action to take when a stress event mechanically compresses pUSD Flows for all recipients, the team clarified a point worth mentioning: there is no manual override. *"No manual override is needed to face it"* — the SP-first allocation is automatic; the compression of other allocations is a direct consequence of the drop in revenue, and the stewards have no button to press in real time. The system manages the crisis through its very structure, not through human decision-making. This is conceptually more radical than it seems, and it aligns with the *Structure Over Trust* doctrine: under stress, stewards aren't asked to arbitrate — we arbitrated at deployment by hardcoding the minimum SP, and the mechanics do the rest.

The role of stewardship under stress thus shifts from arbitration to learning: *"we're definitely keen on learning from such episodes and helping the stewardship to step up from one to the next"*. The relevant question is no longer *"how will discretion be exercised?"* but *"how does the experience of one episode inform the next?"*. A system of documented lessons learned — what the trigger conditions revealed, how the integrators were informed, what worked or didn't work in communication — remains a useful subject for longitudinal observation, without this time carrying the enforceable nature of a discretion review.

**Dilution contingent on success.** The founders' programmed dilution mechanism is elegant, but conditional: *"either it works, founders get diluted; no traction, no dilution."* If the volume of pETH→POLAR conversions stagnates, dilution stagnates as well. The initial concentration does not dissipate according to a schedule — it dissipates through flow. This does not invalidate anything, but it means that the effective decentralization of governance remains a *hypothesis to be validated over time*, not an ex ante guarantee. The team is considering a periodic report — monthly or quarterly — on stewardship activity, and explicitly lists the metrics to track: number of vePOLAR lockers, percentage of delegated votes, percentage of active votes, concentration. This is exactly the type of data that external cross-sectional observation can capture and codify over time.

## Why the Team's Approach Matters Beyond Polaris

Regardless of what Polaris becomes on mainnet — and there will be stressful periods; there always are — the act of self-correction from Stewardship v1 to Flows is, in itself, a contribution to the ecosystem. It demonstrates that a DeFi team can formulate, challenge, and correct its own architecture *before* it is put to the test by market forces. That may not sound like much; in practice, it's a quality few projects have demonstrated. Maker didn't do it. Neither did Aave. Most established protocols wait for an event to reveal a flaw before naming it — and then the urgency of the rescue overshadows all reflection. Polaris does the opposite: it names, it corrects, it publishes, even before anything is launched.

If Polaris fails tomorrow, the gesture remains valid. If Polaris succeeds, the gesture becomes a lesson. In both cases, what deserves to be documented *now* is not a bet on the outcome, but the discipline that makes the outcome observable. The quality of an architecture is not measured by the absence of residual tensions — there are always some. It is measured by the precision with which these tensions are named by those who build them, and by the clarity they offer to those who observe them.

Structurally, this is the same movement that has occupied me since [*Coherence is the Scarce Good*](/en/post/coherence-the-scarce-good/): what matters is not the verdict, but the grammar that makes the verdict possible. Polaris has just written a page of that grammar. It remains to be seen whether the writing holds up under pressure.

---

*Observational article. No position held in Polaris as of the date of publication. Testnet 2, which carries the Flows architecture, was [launched on May 7, 2026](https://x.com/polarisfinance_/status/2052025595068813485). Monitoring will continue in the coming months, as the protocol approaches the mainnet and the first stewardship votes take place.*
