# Case Lock

Date: 2026-03-14 12:07 PM America/New_York

## Decision

The final four case-study cities remain:
- **Singapore** — near compute / high AI
- **Seoul** — near compute / low AI in the delivered overlay
- **Ho Chi Minh City** — far compute / high AI
- **Lagos** — far compute / low AI / priority-city case

No replacement is justified at this stage.

## Operational thresholds used for case locking

These thresholds are for **StoryMap legibility**, not as formal model cutoffs:
- **Near compute:** <= 250 km to nearest cloud region
- **Far compute:** >= 1,000 km to nearest cloud region
- **High AI:** >= upper quartile of AI-linked-city works (**138** recent works)
- **Low AI:** <= lower quartile of AI-linked-city works (**16** recent works) or zero observed works in the delivered overlay

Project-wide reference values from the rebuilt atlas:
- median AI-linked-city distance = **236.9 km**
- median AI-linked-city works = **49**

## City-by-city lock evidence

| City | Country | Distance to nearest region (km) | Recent AI works | AI institutions | Population | Locked quadrant |
|---|---|---:|---:|---:|---:|---|
| Singapore | Singapore | 4.1 | 1072 | 4 | 5,745,000 | near compute / high AI |
| Seoul | Korea, South | 1.3 | 10 | 1 | 21,794,000 | near compute / low AI |
| Ho Chi Minh City | Vietnam | 1096.8 | 373 | 2 | 13,312,000 | far compute / high AI |
| Lagos | Nigeria | 3842.6 | 0 | 0 | 15,279,000 | far compute / low AI |


## Why no replacement was made

- **Singapore** remains the strongest “alignment” case in the rebuilt atlas.
- **Seoul** remains a strong exception case because it is extremely near compute while underperforming in the delivered research overlay.
- **Ho Chi Minh City** remains a clear “beats-the-pattern” case with distance above the far-compute threshold but AI activity well above the high-AI threshold.
- **Lagos** remains one of the clearest stacked-disadvantage / priority-city cases, with no observed works in the delivered overlay and very weak compute proximity.

## Refresh note before final publication

Before live StoryMap publication, do one manual current-footprint sanity check against current official provider region inventories. If a major new full cloud region has opened in any of the locked cities, revisit the lock. Local zones / edge POPs alone are **not** sufficient to replace the baseline repo’s full-region logic unless the final submission explicitly changes the definition of compute access.
