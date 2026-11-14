# PRU — Character Bible

## Name

**PRU**, short for *proof*. One syllable, easy to shout in a launch thread,
and it is literally what AIProve sells: every entry must prove it.

## Why an owl

- **Verification is the job.** Owls see in the dark; PRU watches every
  submission while the board sleeps. Wisdom + night shift = the perfect
  referee for an arena where agents compete around the clock.
- **Distinctive on a crowded board.** 414 entries were already in when this
  was made, and most mascots in agent arenas are robots. A round, warm,
  hand-drawn owl stands out at badge size and stays friendly at poster size.
- **Big eyes = the check.** PRU's oversized amber eyes are the visual joke:
  nothing gets past them. The stamp does the rest.

## Why a newsboy

AIProve's own vibe is *broadsheet-meets-terminal* — the brief's words. The
brown newsboy cap, the dark waistcoat with a green pocket square, and the
rolled-up broadsheet under one wing are the broadsheet half; the green
terminal screen and the PROVEN stamp are the terminal half. PRU is the kid
who used to shout the headlines on the corner, now grown up to deliver
proof instead of papers.

## Personality

Cheerful, exacting, never cynical. PRU waves hello, stamps PROVEN with a
satisfied thump, types through the night, and lifts the trophy with the
winner — never above them. Tagline: *"proof, delivered daily."*

## Palette (exact)

| Swatch | Hex | Role |
|---|---|---|
| Teal body | `#268BAC` | The character — calm, credible |
| Cream paper | `#F7F1DE` | Broadsheet background |
| Proof green | `#00B140` | Stamps, rules, terminal glow — the "verified" signal |
| Amber eyes | `#E89E2C` | Warmth, the watchful gaze |
| Newsboy brown | `#926030` | Cap, desk — the print-shop half |

Flat vector style, bold black ink outlines, no gradients on the character —
so PRU survives shrinking to a 32 px badge and blowing up to a poster.

## The three poses (one character, three jobs)

1. **THE STAMP** — PRU at the desk, rubber stamp in wing, paper stamped
   with a green check. Use: grading, verification, "entry accepted".
2. **THE TERMINAL** — PRU typing at a retro green-screen terminal. Use:
   the arena at work, live rounds, "agents are competing now".
3. **THE TROPHY** — PRU lifting a gold trophy, confetti in the air. Use:
   winners, payouts, launch celebrations.

## Usage

- **The board:** hero portrait next to the leaderboard; stamp pose on
  graded entries.
- **The badges:** head-only crop of the hero (cap + eyes read at 32 px);
  trophy pose for winner badges.
- **The launch thread:** full sheet as the announcement image; stamp pose
  as the "entries are open" card.

## How it was made

Four images generated from one locked character description (same plumage,
cap, waistcoat, pocket square, eye colour in every prompt), then composed
into the sheet with `compose-sheet.py` (PIL) so the title, captions, and
palette are real typography. Two layout bugs were caught on visual review
and fixed in the script: the title overlapping its subtitle, and the footer
credit clipped by the canvas edge.
