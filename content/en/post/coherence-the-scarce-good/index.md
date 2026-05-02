---
title: "Coherence is the scarce good"
subtitle: "Aragon, Twyne, and the missing layer of decentralized organizations"
description: "After the Kelp hack and the Arbitrum freeze, the debate has hardened into a false choice between emergency centralization and principled inaction. There is a third path."
date: 2026-05-02
slug: coherence-the-scarce-good
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

On April 18, 2026, an attacker drained 116,500 rsETH from the cross-chain bridge of [Kelp DAO](https://kelpdao.xyz/). Roughly $292 million.

Not because of a bug. Because of a decision that stayed invisible.

Kelp had chosen a 1-of-1 DVN configuration, a single verifier, [against the explicit recommendations](https://layerzero.network/blog/kelpdao-incident-statement) of its own infrastructure provider. That choice never made it into a proposal, a public debate, or any record before the incident happened.

Two days later, [Arbitrum's Security Council froze $71 million](https://www.coindesk.com/tech/2026/04/22/inside-the-usd71-million-freeze-on-arbitrum-that-has-the-crypto-world-questioning-what-decentralization-really-means).

The debate started immediately. On one side, those who saw this as proof that nothing in crypto is truly decentralized. On the other, those who saw an emergency intervention against a state-level actor as not just legitimate but necessary.

Both positions are coherent. Both miss the point.

Because what happened here doesn't begin with the hack. It doesn't begin with the freeze either.

It begins at the moment a structuring decision can be made without ever being seen.

> ***DeFi doesn't break because of bad code.***
>
> ***It breaks because some decisions stay invisible until it's too late.***

And as long as those decisions stay invisible, every crisis will keep pushing the ecosystem toward an impossible choice between emergency centralization and principled inaction.

---

## What becomes scarce

Decentralized organizations have solved two major problems. They aggregate capital with unprecedented efficiency. They aggregate preferences through sophisticated voting mechanisms.

But they have built almost nothing for a third aggregation, even though it may be the most decisive: the aggregation of intelligent work over time.

That work exists everywhere. It takes the form of research, discussions, technical trade-offs, disagreements, intuitions. It flows through multiple channels and then disappears. Each new session starts where the previous one left off, with no usable trace in between.

Intelligence gets produced. It doesn't accumulate.

This flaw stayed invisible for a long time, for a simple reason: intelligence used to be scarce.

It isn't anymore.

AI has tipped intelligence into abundance. What's now in short supply isn't analysis or code. It's the capacity to hold together what's already been produced.

> ***Intelligence is becoming abundant. Coherence is the bottleneck.***

This shows up in different but converging diagnoses. [Aragon](https://blog.aragon.org/) observes that [the volume of decisions grows faster than available attention](https://blog.aragon.org/beyond-proposals-pt-i-automation-and-the-art-of-not-governing/). [Twyne](https://x.com/twynexyz/status/2047302119737196838) points at the absence of cumulative memory and continuity in the work of agents.

Three observations. One shared limit.

**Coordination distributes tasks. It doesn't produce continuity.**

And in that gap, something deeper is shifting. If a structuring decision can be made without being visible, without being documented, without being challengeable, then the system that contains it is not decentralized in any strong sense.

> ***We didn't decentralize power. We decentralized its interface.***

This shift produces very concrete effects. It favors those who control the context, those who hold informal memory, those who can act without making their decisions legible.

Kelp is not an anomaly.

It's a system revealing how it actually worked, at the moment it failed.

---

## Aragon, the art of not governing

In this landscape, Aragon offers one of the most advanced architectures.

Their starting point is clear: onchain governance frameworks, in their current form, have not given organizations a reliable way to act with precision. Their answer is to shift the central primitive. The proposal is no longer what structures the system. The permission is.

With [OSx](https://blog.aragon.org/the-future-of-governance-is-modular-2/), governance becomes an architecture of rights. Capabilities are defined explicitly, then distributed and recombined through modules.

The decisive step comes with the notion of *policy*. Proposals are reserved for genuinely new decisions. Everything else, recurring payments, predictable allocations, repeatable configurations, is codified as executable rules.

Evan Aronson's formula puts it precisely: *"Policy design is an art of not governing."*

This isn't about reducing governance. It's about relocating it. A decision is no longer a one-off event. It becomes a rule that's both binding and executable, with no need for ongoing intervention. I've worked through this intuition philosophically in [an earlier piece on gentle power](https://arem.blog/en/post/le-doux-pouvoir/); Aronson gives it its technical form.

With [*Linked Accounts*](https://blog.aragon.org/introducing-linked-accounts/), Aragon pushes the logic further by making the purpose of fund flows explicit. Organizational structure stops being implicit. It becomes legible inside the system itself.

This work is substantial. It introduces a kind of legibility that was missing.

But that legibility operates in a deterministic frame. It assumes the relevant actions can be anticipated, that rules can be defined in advance, that behaviors can be bounded.

Anything that escapes that frame stays out of view. Upstream technical trade-offs, informal decisions, the ongoing production of meaning, anything that doesn't stabilize into a rule remains invisible.

> ***Aragon makes decisions executable. It does not make their formation visible.***

---

## Twyne root-archetype, the grammar of agents

This is where *root-archetype* steps in, the agent governance layer Twyne uses internally and has released under an open license.

With [*root-archetype*](https://github.com/0xTwyne/root-archetype), the move is to introduce, on top of application code, a layer that produces nothing directly but defines the conditions of production themselves. Roles, memory, handoff protocols, shared constraints. Everything that gives shape to continuity in collaborative work.

The gesture is simple. Its effects run deep.

A session no longer starts from scratch. Context carries over. Knowledge stops evaporating between contributions.

> ***Intelligence starts to compose itself.***

Released under an open license, this model is meant to become a primitive. It offers a minimal grammar from which an ecosystem can structure itself.

The symmetry with Aragon is clear. Aragon codifies decision on the capital side. Twyne root-archetype codifies the grammar of work on the agent side. One structures what gets decided, the other structures what makes decision possible.

But neither of them makes visible how those two dimensions interact.

Twyne itself, the credit-delegation primitive the team is building, illustrates precisely why this layer is missing. The safety of a credit primitive depends on upstream decisions: parameter choices, oracle picks, verifier setups. Exactly the kind of decisions that, when they stay invisible, become tomorrow's exit conditions. What happened at Kelp is of that exact nature, which is what makes the legibility question anything but theoretical.

---

## The missing layer

This is where the problem becomes legible.

Neither Aragon nor Twyne root-archetype makes visible how decision, capital, and production hold together over time.

That invisibility is exactly what made Kelp possible.

What's missing isn't another tool. It's a layer.

A system that makes structuring decisions visible before they produce irreversible effects.

We can name it plainly: an *Organizational Observability Layer*.

A layer of this kind doesn't just trace outputs. It represents how an organization actually functions. It connects actors, human and agent, with their tasks, their dependencies, their decision points. It holds the memory of choices, alternatives, disagreements. It formalizes handoffs. It exposes constraints. It sustains a [transversal watchfulness](https://arem.blog/en/post/transversal-watchfulness/).

> ***Making the actual functioning of a system visible is becoming a strategic capability.***

Today, contributing too often means just adding work. In an organization with such a layer, **contributing means modifying a shared state.**

It's what turns a succession of initiatives into a cumulative process.

It also clarifies a distinction that often gets blurred. Coordination answers *who does what*. Coherence answers a more demanding question: **does the system, as a whole, still make sense?**

Current tools improve the first. The second still has to be built.

---

## The false alternative

The debate that opened after the Arbitrum freeze reveals exactly where we are.

Should we intervene or not? Should we accept emergency centralization, or hold strict fidelity to principle?

The questions are legitimate. They just arrive too late.

They assume the incident has happened and that we now have to pick between two flawed options. They never ask what made the incident possible in the first place.

Had Kelp's DVN configuration been visible, documented, challengeable before it shipped, the choice could have been different. Or owned. Or constrained.

In any of those cases, it would have lived in a shared space.

> ***Every incident of this kind is a failure of visibility before it is a failure of security.***

Recognizing this doesn't remove the risk. It moves the ground on which the risk has to be addressed.

Decentralization no longer plays out solely in the ability to react. It plays out in the ability to make decisions visible before they become irreversible.

That's a third path. Not a compromise. A reframing.

---

## The natural slope

Building such a layer comes with real tensions.

Over-formalization can rigidify the system. A too-clean representation can hide misalignment, unless it makes explicit room for dissent.

But the deeper risk lies elsewhere.

Any layer of legibility creates an asymmetry. Whoever sees more than others has an advantage. Without an explicit mechanism, that asymmetry drifts toward capture: by a central team, by a vendor, by an external actor.

> ***What isn't held as a commons becomes a point of control.***

Holding a coherence layer as shared infrastructure is the only regime that doesn't take care of itself. Every other regime emerges without effort.

---

## A political stake

**Coherence is not a technical problem. It is a political choice.**

It determines who can see, who can understand, who can challenge. Today, those dimensions stay largely implicit, and therefore default-controlled by whoever already occupies a central position.

This is a call on our vigilance, in the same direction I proposed in [a public grammar of risk](https://arem.blog/en/post/public-grammar-of-risk/).

Engaging with a protocol shouldn't be limited to assessing its code, its tokenomics, or its formal governance. It should include a simpler, more demanding question: *how are structuring decisions made visible?*

That is the dimension Kelp lacked. And it is the dimension that will determine how robust the systems to come actually turn out to be.

---

## To close

Aragon and Twyne root-archetype have laid down essential bricks.

One on decision and capital.

The other on production and memory.

But the layer that would let those two articulate is still to be built.

Without it, every crisis will keep forcing a choice between centralization and powerlessness.

With it, structuring decisions become visible before they become irreversible.

> ***We haven't failed to build decentralized systems.***
>
> ***We have failed to make them legible.***

That legibility, that coherence, is what is now genuinely at stake. And what remains to be invented.
