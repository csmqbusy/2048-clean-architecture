from entrypoints.di.cli.facade import Dependencies, dependencies_facade


def start_cli_app():
    deps: Dependencies = dependencies_facade()

    return deps.game_loop.execute()
