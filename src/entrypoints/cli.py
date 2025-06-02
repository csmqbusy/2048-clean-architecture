from src.entrypoints.di.cli.facade import Dependencies, dependencies_facade


def start_cli_app():
    """
    Initializes and starts the 2048 CLI application.
    Creates all necessary dependencies and executes the main game loop.
    """
    deps: Dependencies = dependencies_facade()

    return deps.game_loop.execute()
