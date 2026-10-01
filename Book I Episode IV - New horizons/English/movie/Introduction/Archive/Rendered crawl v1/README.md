# Opening crawl — rendered preview v1

Silent picture preview: 1920 × 1080, 24 fps, 2 minutes 6 seconds.

Includes black opening, fixed starfield, receding title, and all 165 narration words on one continuous perspective plane. Gold lettering is typeset once; it is not generated anew per frame.

Timing is provisional. Bee’s voice, intake of breath, music, and final audio mix are not included. Retiming should follow the approved voice recording. The final text fades into stars, leaving the background available for the next sequence.

Editable source: narration.txt, render.py, timing.json. Reference images: starfield.png and text-plane.png. The renderer uses Python, Pillow, NumPy and FFmpeg; run render.py from any directory after installing those dependencies. Run with --stills to export inspection frames. Rendering uses Arial Bold from macOS.
