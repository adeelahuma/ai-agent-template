# {{ cookiecutter.project_name }}

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Poetry](https://img.shields.io/badge/Poetry-1.8%2B-orange)
![LangChain](https://img.shields.io/badge/LangChain-LangGraph-green)

A modular, production-ready AI agent starter built with LangChain and LangGraph.

## Features

- A structured agent workflow powered by LangGraph
- Typed state management for agent execution
- Extensible tool integration for custom capabilities
- Environment-based configuration with Pydantic settings
- Poetry-based dependency and environment management

## Project Structure

```text
├── config/
│   └── settings.py         # Environment configuration and secrets
├── src/
│   ├── agent/              # LangGraph orchestration and workflow nodes
│   │   ├── state.py        # Shared state definitions
│   │   ├── nodes.py        # Node implementations
│   │   ├── edges.py        # Routing and conditional transitions
│   │   └── graph.py        # Graph construction and compilation
│   ├── services/           # External service integrations
│   └── tools/              # Agent tool definitions and helpers
│       ├── base.py
│       └── custom_tool.py
├── tests/                  # Unit and integration tests
├── main.py                 # Application entry point
├── pyproject.toml          # Poetry project configuration
└── README.md               # Project overview and usage
```

## Prerequisites

- Python 3.11+
- Poetry
- An API provider or local model endpoint configured in your environment

## Setup

1. Install dependencies:

   ```bash
   poetry install
   ```

2. Create a local environment file:

   ```bash
   cp .env.example .env
   ```

3. Update your environment variables and model settings in the configuration module.

4. Start the application:

   ```bash
   poetry run python main.py
   ```

## Development Commands

- Run tests:

  ```bash
  poetry run pytest
  ```

- Add a dependency:

  ```bash
  poetry add <package-name>
  ```

- Activate the Poetry environment:

  ```bash
  poetry shell
  ```

## Configuration

The project uses environment variables through Pydantic settings. Update the values in your `.env` file and the related settings class to match your provider and model choices.

## Notes

This starter is intended as a foundation for building more advanced LangChain and LangGraph applications, including tool calling, multi-step reasoning, and external service integrations.