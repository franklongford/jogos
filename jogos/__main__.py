import click


@click.command()
@click.argument(
    'jogo', required=True, default=None
)
def main(jogo):

    if jogo == 'aliens':
        from pygame.examples.aliens import main
    elif jogo == 'stars':
        from pygame.examples.stars import main
    else:
        return
    main()


if __name__ == '__main__':
    main()
