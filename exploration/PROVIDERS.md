# Provider Capabilities

## Music Providers

### Google Lyria (`google/lyria.py`)
- **Type**: Instrumental Music
- **Vocals/Lyrics**: No support.
- **Key Features**:
  - Real-time streaming generation.
  - BPM (Beats Per Minute) control.
  - Temperature control for generation randomness.
  - "Weighted prompt" support.

### MiniMax via AIMLAPI (`aimlapi/minimax.py`)
- **Type**: Music with Vocals
- **Vocals/Lyrics**: **Supported.** Can accept lyrics with structure tags.
- **Key Features**:
  - Reference audio support for style transfer.
  - Non-English vocal support.
  - High-quality output.

## Video Providers

### Google Veo (`google/veo.py`)
- **Type**: Text-to-Video & Image-to-Video
- **Image-to-Video**: **Supported.**
- **Key Features**:
  - Fast generation (~30 seconds).
  - Multiple aspect ratios (16:9, 9:16, 1:1).
  - Supports "fast" and "standard" models.

### KlingAI (`kling/direct.py`)
- **Type**: High-Quality Video
- **Image-to-Video**: **Supported.**
- **Key Features**:
  - Highest quality video generation (v2.1-master model).
  - Longer generation time (5-14 minutes).
  - Supports "std" and "pro" modes.

## Summary

| Feature | Lyria (Google) | MiniMax (AIMLAPI) | Veo (Google) | Kling (KlingAI) |
| :--- | :---: | :---: | :---: | :---: |
| **Content Type** | Music (Instr.) | Music (Vocals) | Video | Video |
| **Lyrics/Vocals** | ❌ | ✅ | N/A | N/A |
| **Image-to-Video**| N/A | N/A | ✅ | ✅ |
| **Speed** | Fast | Standard | Fast | Slow (High Quality) |
