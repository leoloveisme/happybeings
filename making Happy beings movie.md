# Making the Happy Beings Movie — AI Tool Notes

Notes on the AI video/audio tool stack for producing the Happy Beings movie,
researched September 2026. Pricing and model rankings shift fast — treat this
as a snapshot to re-check periodically, not a permanent answer.

## Video generation stack

**Kling 3.0 — workhorse** \- Cheapest credible option: ~$0.10/sec, roughly $0.84
for a 10-second clip with audio. - Native synced audio. - **Elements 3.0**:
upload up to 4 reference images per generation and tag them as
characters/objects/scenes; the model holds that identity consistent across
separate clips. This is the key feature for Happy Beings specifically —
recurring characters (An Var, Chen, Olga, Ya Sha, Col An, Sai Ya, etc.) need to
stay recognizable across many scenes, and both genderless and gendered XYZ
beings need to render correctly and consistently. Feeding it our existing
character reference photos (`Book I Episode IV - New horizons/photos/`) as
Elements input avoids the model defaulting to conventionally gendered features
the way a text-only prompt would.

**Runway Gen-4.5 + Aleph — fixing/editing existing shots** \- Video-to-video
editing: prompt an edit directly onto footage that's already generated, rather
than regenerating from scratch. - This is the right tool for cleanup fixes —
e.g. the duplicate-spaceship issue found in the existing test footage (two
identical ships stacked over the planet; only one should be there). - Pricing:
Standard $12–15/mo; Unlimited $76–95/mo for heavy use.

**Veo 3.1 — hero shots only** \- Strongest physical-world realism and native
audio; best for space/spaceship/flight sequences where the extra cost is worth
it. - ~$0.15/sec+, so reserve for a handful of key cinematic beats rather than
the whole film.

**Excluded: Sora 2** — OpenAI deprecated it April 26, 2026, with the API shutting
down September 24, 2026. Not viable for a long-running project.

## Music & audio stack

**Suno v5.5** — $10/mo Pro (Premier $30/mo) - Best quality/vocal realism overall;
handles both instrumental score and full songs with vocals. - Risk:
commercial-license lawsuits are unsettled (a Munich court ruled against Suno,
July 31, 2026). Worth weighing against Happy Beings being GPL/free-forever.

**ElevenLabs Music** — from $6/mo - Clean commercial licensing secured before
launch — the safer pick if unencumbered rights matter more than the last bit of
quality. - Also the standard choice for character voice synthesis/cloning if
dialogue is AI-voiced rather than performed live.

**Udio** \- Standout feature: inpainting — regenerate one section of a track
without redoing the whole thing. - Downloads currently paused pending its
co-licensed UMG/Warner/Merlin/Kobalt platform.

## Content-policy gap: nudity

Kling, Veo, Runway, and Sora all enforce strict no-nudity content policies.
This directly conflicts with the project's stated creative approach (per 
`happy_beings_context.md`: "a lot of nudity in books and eventual film"; XYZ
beings don't wear clothes).

None of the mainstream AI video tools above will generate nudity directly. The
existing test footage (body-painted actors, e.g. the three XYZ beings in a
field) suggests the practical route is already in use: **live-action/practical
shoots for scenes requiring nudity, AI generation for everything else** (space,
ships, environments, clothed Earth scenes). This split needs to be made
explicit per-scene, since it determines which tool applies where.

## Cost reality check

Raw generation cost on Kling 3.0's cheaper tier works out to roughly: - $0.84
per 10-second clip (with audio) → **~$5/minute** \- ~$0.10/sec → **~$6/minute**

That's the cost of *generating* footage, not the cost of a *finished, usable*
minute. First-pass clips routinely need 2-4 regenerations before a shot is a
keeper (character drift, camera glitches, wrong object counts like the
duplicate-spaceship case). Realistic budget: **~$15-25 in generation cost per
finished minute** until prompt/reference workflows are dialed in — savings come
from cutting retries, not from writing shorter prompts.

## Prompt discipline (this is where the savings actually come from)

Retries are the real cost driver, so the goal is consistency, not verbosity:

1.  **Lock a reusable description block per character** — write each recurring
    character's (An Var, Chen, Olga, Ya Sha, Col An, Sai Ya, etc.) canonical
    description once and paste it verbatim every time. Re-describing from
    memory each shot introduces wording drift ("blue-skinned" vs
    "azure-skinned") that reads as a different character to the model.
2.  **Prefer reference images (Elements) over text for appearance** — let Kling's
    Elements carry the visual identity; use the prompt text to direct
    action/camera instead of re-describing multi-armed, multi-headed, or
    color-shifting XYZ beings each time.
3.  **State exact counts and negatives explicitly** — "one spaceship" alone isn't
    enough; add "exactly one ship, no duplicate, no second ship" as an explicit
    negative constraint. This is exactly what would have prevented the
    duplicate-spaceship regeneration.
4.  **Specify camera and composition, not just content** — angle, distance,
    foreground/background, relative position of moons/planets. Ambiguity here
    causes "almost right" wasted regenerations.
5.  **Keep a running shot-list/prompt log per scene** — reuse prompts that
    worked, and log a one-line note on what went wrong for prompts that didn't.
    This compounds savings across the whole movie, not just one well-written
    prompt.

### Shot-list template

Use one row per shot; fill in as scenes get produced.


|Chapter/Scene|Shot description|Characters (Elements refs used)|Camera/composition notes|Prompt (final working version)|Tool|Attempts|Cost|Notes/failure modes avoided|
|-------------|----------------|-------------------------------|------------------------|------------------------------|----|--------|----|---------------------------|
|             |                |                               |                        |                              |    |        |    |                           |

## Sources (as of Sept 2026)

- 
  [Best AI Video Generator 2026: Veo 3.1 vs Sora 2 vs Kling](https://tech-insider.org/best-ai-video-generator-2026/)
- 
  [AI Video Tools May 2026 — Sora 2 vs Veo 3 vs Kling vs Runway Compared](https://www.toolcenter.ai/en/articles/ai-video-generation-tools-2026)
- 
  [Best AI Video Generators 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 vs Runway](https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026)
- 
  [AI Music Generation 2026: Suno, Udio, ElevenLabs Compared](https://www.digitalapplied.com/blog/ai-music-generation-platforms-suno-udio-elevenlabs-2026)
- 
  [Best AI Music Generators 2026: Suno v5 vs ElevenLabs vs Udio](https://www.teamday.ai/blog/best-ai-music-models-2026)
- 
  [AI Video Production in 2026: Character Consistency Finally Makes It Usable](https://codedesigns.eu/ai-video-production-in-2026-character-consistency-finally-makes-it-usable/)
- 
  [Which AI Video Model Keeps Characters Most Consistent in 2026?](https://www.elser.ai/blog/best-ai-video-model-character-consistency-2026)

