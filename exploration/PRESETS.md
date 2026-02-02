# System Presets

## Music Presets
Located in `src/ai_content/presets/music.py`. Defined as `MusicPreset` objects.

| Preset Name | BPM | Mood | Description |
| :--- | :--- | :--- | :--- |
| **jazz** | 95 | nostalgic | Smooth Jazz Fusion, walking bass, mellow sax. |
| **blues** | 72 | soulful | Delta Blues, bluesy guitar arpeggio, raw emotion. |
| **ethiopian-jazz**| 85 | mystical | Ethio-Jazz, Masenqo strings, syncopated rhythms. |
| **cinematic** | 100 | epic | Epic Orchestral, sweeping strings, Hans Zimmer style. |
| **electronic** | 128 | euphoric | Progressive House, driving bass, synth arpeggios. |
| **ambient** | 60 | peaceful | Ethereal pads, weird textures, Brian Eno style. |
| **lofi** | 85 | relaxed | Lo-fi Hip-Hop, vinyl crackle, dusty drums. |
| **rnb** | 90 | sultry | Contemporary R&B, smooth synth pads. |
| **salsa** | 180 | fiery | Cuban Salsa Dura, driving tumbao piano. |
| **bachata** | 130 | romantic | Dominican Bachata, requinto guitar. |
| **kizomba** | 95 | sensual | Angolan Kizomba, deep electronic bass. |

## Video Presets
Located in `src/ai_content/presets/video.py`. Defined as `VideoPreset` objects.

| Preset Name | Aspect Ratio | Duration | Description |
| :--- | :---: | :---: | :--- |
| **nature** | 16:9 | 5s | Majestic lion, documentaries style. |
| **urban** | 21:9 | 5s | Cyberpunk Tokyo, neon-lit streets. |
| **space** | 16:9 | 5s | Astronaut in observation deck, Interstellar style. |
| **abstract** | 1:1 | 5s | Flowing liquid metal, iridescent reflections. |
| **ocean** | 16:9 | 5s | Turquoise ocean waves, underwater shot. |
| **fantasy** | 21:9 | 5s | Ancient dragon soaring, high fantasy. |
| **portrait** | 9:16 | 5s | Close-up fashion portrait, studio lighting. |

## Adding a New Preset
To add a new preset:
1. Open `src/ai_content/presets/music.py` or `video.py`.
2. Define a new constant using the config class (e.g., `MY_STYLE = MusicPreset(...)`).
3. Add the new constant to the list in `MUSIC_PRESETS` or `VIDEO_PRESETS` dictionary comprehension at the bottom of the file.
