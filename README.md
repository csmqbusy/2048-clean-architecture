# 🎮 2048 Game (Clean Architecture)

A minimal and extensible terminal-based implementation of the classic [2048 game](https://en.wikipedia.org/wiki/2048_(video_game)) written in **Python 3.13** using **Clean Architecture** principles — with no external dependencies.

<img width="280" alt="CLI 2048" src="https://github.com/user-attachments/assets/4b5e436d-2310-4cdd-a05f-1e6351fa5903" />


## 📦 Project Structure

The architecture follows the Dependency Rule:

```
domain <- application <- presentation
```

Each layer depends only on higher-level layers, not on outer ones:

- **Domain**: Business logic and entities (`Board`, `Game`, `TileSpawner`)
- **Application**: Use cases and application logic (`GameUseCase`)
- **Presentation**: Presenters and Views — currently implemented for **UNIX CLI** (Linux/macOS)

Additionally:

- **Entrypoints**: Contains **Dependency Injection (DI)** configuration and application entrypoint for CLI version
- **Infrastructure**: Placeholder for external integrations (currently unused)

## 🚀 Getting Started

### Prerequisites

- Python >= 3.13 (no external libraries required)

### Installation

Clone the repository:

```bash
git clone https://github.com/csmqbusy/2048-clean-architecture.git
cd 2048-clean-architecture
```

Set up a virtual environment (recommended):

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

Or if you using `uv`:

```bash
uv sync
```

Run the application:

```bash
python src/main.py
```

## 🧱 Clean Architecture Layers

```text
src/
├── domain/
│   └── Core business logic (entities, interfaces)
├── application/
│   └── Use cases and interface ports
├── presentation/
│   └── CLI presenter and view
├── entrypoints/
│   └── CLI entrypoint with Dependency Injection
```

Each layer communicates only with the inner layer via clearly defined interfaces.

## 🖥️ CLI Interface

Currently supports **UNIX CLI** (Linux/macOS).  
Easily extensible to other platforms (e.g., GUI, Web) by implementing the existing interfaces in `application.ports`.

## ✅ Features

- Fully working 2048 logic
- Clean and testable architecture
- Easy to extend (new UI, AI player, etc.)
- No external dependencies

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute it with attribution.
