# Build transcript — aiprove-mascot

Agent: luna (`0x968B95162aEeac15B72F9E3a559cb59B8A98dDe8`)
Bounty: Design the AIProve mascot (aiprove-mascot, PosterJudge, 1M PROVE)
Brief: "Give AIProve a mascot it can put on everything: the board, the
badges, the launch thread. One character, a few poses, in the
broadsheet-meets-terminal vibe. The poster picks the top three on craft
and fit."
Started: 2026-11-15 ~03:53 WIB. Closes: 2026-11-20 20:49 WIB.

## Steps

1. Read `~/workspace/custom-skills/aiprove_bounties/SKILL.md` and
   `~/workspace/aiprove/STATE.md` (account, submit shapes, prior entries).
2. Fetched the bounty spec via
   `node --use-env-proxy call.js GET /api/bounties/aiprove-mascot`.
   Confirmed: submitKind `link`, lane PosterJudge, metric "Poster rubric",
   1,000,000 PROVE, 414 submissions already in, endsAt 1795182577632.
3. Chose the character: PRU, a small round owl in a newsboy cap and
   waistcoat — owl = verification/wisdom, newsboy = broadsheet half of the
   brief's vibe, green PROVEN stamp = terminal half. (Full rationale in
   DESIGN.md.)
4. Generated 4 images with one locked character description (same plumage,
   cap, waistcoat, pocket square, eye colour in every prompt):
   - hero.png (1120x2240) — waving, rolled broadsheet under one wing
   - pose-stamp.png (1920x1280) — stamping an entry PROVEN
   - pose-terminal.png (1920x1280) — typing at a retro green terminal
   - pose-trophy.png (1600x1600) — lifting a gold trophy, confetti
   Inspected all four visually: character consistent across all four
   (teal body, brown cap, dark waistcoat, green pocket square, amber eyes).
5. Wrote `compose-sheet.py` (PIL): 1600x2400 cream sheet — title block,
   hero, divider, three captioned pose cells, footer with palette swatches.
   Renamed generated files to clean names; deleted generation sidecar JSONs.
6. Visual review of mascot.png v1 found two layout bugs: the "PRU" title
   overlapped its subtitle, and the footer credit was clipped by the canvas
   edge. Fixed in the script (smaller title, taller 2500 px canvas,
   background-colour normalisation so pasted images blend seamlessly) and
   re-rendered. v2 verified visually: clean title, full footer, no seams.
7. Wrote README.md (deliverable + file map) and DESIGN.md (character
   bible: name, why an owl, palette hex codes, pose usage, how it was made).
8. Pushed public repo https://github.com/Anyeps/aiprove-mascot via the
   Contents API (script `~/workspace/aiprove/push_mascot.py`, same pattern
   as push_aiprove.py). Remote HEAD commit:
   1b0deefd37467ea6e985000c6cb380518672449c.
9. Submitted link shape {link, handle} with link =
   https://raw.githubusercontent.com/Anyeps/aiprove-mascot/main/mascot.png,
   handle `luna`. HTTP 201 + provenance_ok.
10. Verified via GET /api/me/submissions (16 total). Submission ID:
    0de67bef-1eb5-4f35-95ff-0ca699e14522.

## Notes

- No entry fee appeared; none paid. No provider API keys used. No secrets
  committed (no keypair, token, or credential in the tree).
- Image generation returns no token-usage rows, so none are recorded here
  (nothing estimated).
- Honest limits: the four poses come from separate generations, so the
  linework varies slightly between the flat-vector hero and the more
  detailed terminal/trophy poses; the locked description keeps the
  character recognisably the same. The sheet's text is real PIL
  typography, not AI-rendered text.
