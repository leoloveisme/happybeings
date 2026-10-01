# Set up Git LFS for Happy Beings media, then begin movie/novel/screenplay collaboration

## Context
The user wants to start actively collaborating on the Happy Beings project across three fronts: the novel text, the screenplay text, and the "movie" (visual/video reference material for Book I: New Horizons). Before diving into content, they raised an infrastructure blocker: GitHub doesn't handle large binary files well, and their planned collaborative platform (Crowdly) isn't ready yet, so they asked how to version photos/video assets beyond plain git.

Investigation of the repo found:
- `Book I Episode IV - New horizons/video/` (48M, all `.mp4`, includes an `Archive/` subfolder) is **entirely untracked** — never committed.
- `Book I Episode IV - New horizons/photos/` (22M, `.jpg`/`.png`) is **already committed as regular git blobs** (37 tracked `.jpg` files alone). Current `.git` size is only 27M, current largest single file is 5.4M — well under GitHub's 50MB warning / 100MB hard limit.
- No `.gitattributes` file exists anywhere in the repo; `git-lfs` is not installed on this machine (available via Homebrew).
- The repo's root `.gitignore` only excludes `.crowdly/`. Several `.DS_Store` files (root, and inside `photos/` and its subfolders) are untracked and littering `git status`.
- Minor unrelated finding: the photos folder is tracked in git history under the capitalized path `Photos/` (e.g. `Book I Episode IV - New horizons/Photos/XYZ characters/An Var/an var.jpg`), while the actual folder on disk is lowercase `photos/`. This works locally today only because macOS's default case-insensitive filesystem masks the mismatch — `git status` shows no rename/discrepancy. It could bite on a case-sensitive clone (e.g. Linux CI) or on GitHub.com's rendering. Flagging this for the user's awareness; not fixing it as part of this plan unless they ask.

The user picked the **hybrid approach**: set up Git LFS now for current assets, and revisit external cloud storage only later if/when raw movie production files grow past what LFS's free quota can reasonably handle.

Given the current asset sizes are small and the repo/`.git` are small, this plan avoids any destructive history rewrite (no `git lfs migrate import` on the already-committed photos) — that would require a force-push to `origin` (`github.com:leoloveisme/happybeings`) and rewrites published history, which isn't warranted yet. Instead, LFS tracking is set up going forward so all new/modified media (starting with the currently-untracked `video/` folder) flows through LFS from the start.

## Approach

1. **Install Git LFS** via Homebrew (`brew install git-lfs`) and initialize it for this repo (`git lfs install`, which sets up the local git hooks — this is a one-time global + per-repo setup, non-destructive).

2. **Add a `.gitattributes` file** at the repo root declaring LFS tracking for binary media types used across all book folders (not just Book I, since other books will likely accumulate similar assets):
   ```
   *.mp4 filter=lfs diff=lfs merge=lfs -text
   *.mov filter=lfs diff=lfs merge=lfs -text
   *.jpg filter=lfs diff=lfs merge=lfs -text
   *.jpeg filter=lfs diff=lfs merge=lfs -text
   *.png filter=lfs diff=lfs merge=lfs -text
   ```
   This is forward-looking: it governs newly added/changed files, not history.

3. **Update root `.gitignore`** to add `.DS_Store` (currently several are untracked and would otherwise get accidentally committed).

4. **Commit the new `video/` folder through LFS**: since it's currently untracked, adding it after `.gitattributes` is in place means it goes straight into LFS as pointer files — no migration needed. Confirm with `git lfs ls-files` that the `.mp4`s land in LFS, and that `git status` is otherwise clean (modulo the `.DS_Store` files now ignored).

5. **Leave existing committed `photos/` history alone** for now (no `git lfs migrate import`, no force-push). Document in the commit/PR description that future edits to existing photos, or newly added photos, will automatically flow through LFS per the new `.gitattributes` rule. Mention to the user that a retroactive migration of the existing photo blobs into LFS is possible later, but requires a history rewrite + force-push and should be a separate, explicitly-approved step if the repo ever grows large enough to matter.

6. **Report the `Photos/`-vs-`photos/` case mismatch** to the user as an FYI (already done above) — no action unless requested.

7. Do not touch `Book VI`/`Book VII` (mostly stubs) or attempt any change to Books II–V content as part of this infra work.

## Critical files
- `.gitattributes` (new, repo root)
- `.gitignore` (repo root — add `.DS_Store`)
- `Book I Episode IV - New horizons/video/**` (currently untracked; first commit will go through LFS)
- No changes to any narrative/content `.md` files as part of this step — the novel/screenplay/movie collaborative writing work begins as a separate, ongoing conversational effort right after this infra step lands, not as a single upfront plan (that work is iterative: drafting and revising scenes together in `Book I .../English/novel/chapters/*.md` and `.../screenplay/chapters/*.md`, informed by the existing "Key Scenes to Develop" list in `happy_beings_context.md`).

## Verification
- `git lfs install` succeeds; `git lfs env` shows LFS configured for this repo.
- After staging the `video/` folder and any `.gitattributes`/`.gitignore` changes: `git lfs ls-files` lists all the `.mp4` files as LFS-tracked.
- `git status` is clean of `.DS_Store` noise.
- `git push` to `origin` succeeds without GitHub size warnings (all confirmed once user approves the push — pushing is a shared/visible action and will be confirmed separately, not assumed as part of "done").
