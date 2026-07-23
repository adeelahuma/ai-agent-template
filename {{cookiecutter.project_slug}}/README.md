# AI Agent Application

A modular, production-grade LangGraph agent application.

## Project Architecture

```text
├── config/                 # Application configuration & Pydantic settings
│   └── settings.py         # Loads environment variables from .env
├── src/                    # Primary source code
│   ├── agent/              # LangGraph core logic
│   │   ├── state.py        # TypedDict state definitions
│   │   ├── nodes.py        # LLM & task node functions
│   │   ├── edges.py        # Conditional routing functions
│   │   └── graph.py        # Graph assembly & compilation
│   ├── services/           # External API & REST integration wrappers
│   │   └── {search}_service.py
│   └── tools/              # Agent tool interfaces exposed to LLMs
│       ├── base.py         # Exporter combining all active tools
│       └── custom_tool.py  # Custom tool implementation
├── tests/                  # Unit and integration test suites
│   └── test_custom_tools.py
├── .env.example            # Template for environment variables
├── .gitignore              # Files excluded from source control
├── pyproject.toml          # Poetry dependency & project management | Generated via `poetry init`
└── main.py                 # Application entry point

```

## Additional Notes

 - Rename .env.example to .env and add environmnet varibales, API keys etc and update settings.py file for the key names 

 - To create environment and install dependencies from poetry.lock file
   > poetry install 

 - To add a dependency 
   > poetry add pydantic 
     
 - To activate environment 
   > source $(poetry env info --path)/bin/activate

- To Run the application  
   > poetry run python main.py 

- To Run Tests
   > poetry run pytest   