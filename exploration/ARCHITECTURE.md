# Codebase Architecture

## Package Structure
The `ai-content` package is organized into the following main modules within `src/ai_content/`:

- **cli/**: Contains the command-line interface implementation using `typer`. The entry point `main.py` defines commands like `music` and `video`.
- **config/**: Handles configuration loading and environment settings.
- **core/**: Core abstractions including the `ProviderRegistry` and `GenerationResult` classes. This creates a unified interface for different AI providers.
- **integrations/**: Specific integrations with external services or libraries (e.g., `media` likely handles file processing).
- **pipelines/**: Orchestration logic for complex workflows. It includes `music.py` and `video.py` pipelines, which likely wrap the provider calls and handle additional processing or multi-step generations. `base.py` defines `PipelineResult` to aggregate outputs.
- **presets/**: Contains pre-configured styles for music and video generation (`music.py`, `video.py`).
- **providers/**: Implementations of specific AI provider APIs.
- **utils/**: Utility functions for file handling, lyrics parsing, etc.

## Provider Organization
Providers are organized by vendor in the `src/ai_content/providers/` directory:
- **aimlapi/**: Clients for AIMLAPI services (e.g., `minimax.py` for music).
- **google/**: Google Cloud Vertex AI/Gemini integrations (e.g., `lyria.py` for music, `veo.py` for video, `imagen.py`).
- **kling/**: KlingAI integration (`direct.py`).

Each provider implements a common interface (likely defined in `core/provider.py`) and registers itself using the `@ProviderRegistry.register_{type}` decorator as seen in the implementation files.

## Pipelines
The `pipelines/` directory serves to abstraction generation workflows.
- **Purpose**: It standardizes the execution flow, error handling, and result aggregation for different content types.
- **Base Pipeline**: `base.py` defines `PipelineResult` and `PipelineConfig`, allowing pipelines to track success/failure, execution time, and output files in a consistent manner.
- specific pipelines like `music` and `video` likely manage the specific parameters and provider interactions for those content types.
