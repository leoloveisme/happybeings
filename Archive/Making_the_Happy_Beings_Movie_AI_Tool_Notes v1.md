# Making the Happy Beings Movie — AI Tool Notes

Notes on the AI video/audio tool stack for producing the Happy Beings movie, researched September 2026. Pricing and model rankings shift fast — treat this as a snapshot to re-check periodically, not a permanent answer.

## Video generation stack

**Kling 3.0 — workhorse**
- Cheapest credible option: ~$0.10/sec, roughly $0.84 for a 10-second clip with audio.
- Native synced audio.
- **Elements 3.0**: upload up to 4 reference images per generation and tag them as characters/objects/scenes; the model holds that identity consistent across separate clips. This is the key feature for Happy Beings specifically — recurring characters (An Var, Chen, Olga, Ya Sha, Col An, Sai Ya, etc.) need to stay recognizable across many scenes, and both genderless and gendered XYZ beings need to render correctly and consistently. Feeding it our existing character reference photos (`Book I Episode IV - New horizons/photos/`) as Elements input avoids the model defaulting to conventionally gendered features the way a text-only prompt would.

**Runway Gen-4.5 + Aleph — fixing/editing existing shots**
- Video-to-video editing: prompt an edit directly onto footage that's already generated, rather than regenerating from scratch.
- This is the right tool for cleanup fixes — e.g. the duplicate-spaceship issue found in the existing test footage (two identical ships stacked over the planet; only one should be there).
- Pricing: Standard $12–15/mo; Unlimited $76–95/mo for heavy use.

**Veo 3.1 — hero shots only**
- Strongest physical-world realism and native audio; best for space/spaceship/flight sequences where the extra cost is worth it.
- ~$0.15/sec+, so reserve for a handful of key cinematic beats rather than the whole film.

**Excluded: Sora 2** — OpenAI deprecated it April 26, 2026, with the API shutting down September 24, 2026. Not viable for a long-running project.

## Music & audio stack

**Suno v5.5** — $10/mo Pro (Premier $30/mo)
- Best quality/vocal realism overall; handles both instrumental score and full songs with vocals.
- Risk: commercial-license lawsuits are unsettled (a Munich court ruled against Suno, July 31, 2026). Worth weighing against Happy Beings being GPL/free-forever.

**ElevenLabs Music** — from $6/mo
- Clean commercial licensing secured before launch — the safer pick if unencumbered rights matter more than the last bit of quality.
- Also the standard choice for character voice synthesis/cloning if dialogue is AI-voiced rather than performed live.

**Udio**
- Standout feature: inpainting — regenerate one section of a track without redoing the whole thing.
- Downloads currently paused pending its co-licensed UMG/Warner/Merlin/Kobalt platform.

## Content-policy gap: nudity

Kling, Veo, Runway, and Sora all enforce strict no-nudity content policies. This directly conflicts with the project's stated creative approach (per `happy_beings_context.md`: "a lot of nudity in books and eventual film"; XYZ beings don't wear clothes).

None of the mainstream AI video tools above will generate nudity directly. The existing test footage (body-painted actors, e.g. the three XYZ beings in a field) suggests the practical route is already in use: **live-action/practical shoots for scenes requiring nudity, AI generation for everything else** (space, ships, environments, clothed Earth scenes). This split needs to be made explicit per-scene, since it determines which tool applies where.

## Sources (as of Sept 2026)

- [Best AI Video Generator 2026: Veo 3.1 vs Sora 2 vs Kling](https://tech-insider.org/best-ai-video-generator-2026/)
- [AI Video Tools May 2026 — Sora 2 vs Veo 3 vs Kling vs Runway Compared](https://www.toolcenter.ai/en/articles/ai-video-generation-tools-2026)
- [Best AI Video Generators 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 vs Runway](https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026)
- [AI Music Generation 2026: Suno, Udio, ElevenLabs Compared](https://www.digitalapplied.com/blog/ai-music-generation-platforms-suno-udio-elevenlabs-2026)
- [Best AI Music Generators 2026: Suno v5 vs ElevenLabs vs Udio](https://www.teamday.ai/blog/best-ai-music-models-2026)
- [AI Video Production in 2026: Character Consistency Finally Makes It Usable](https://codedesigns.eu/ai-video-production-in-2026-character-consistency-finally-makes-it-usable/)
- [Which AI Video Model Keeps Characters Most Consistent in 2026?](https://www.elser.ai/blog/best-ai-video-model-character-consistency-2026)
