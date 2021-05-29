import click


@click.command()
@click.argument(
    'jogo', required=True, default=None
)
def main(jogo):

    if jogo == 'alienigenas':
        from pygame.examples.aliens import main
    elif jogo == 'estrelas':
        from pygame.examples.stars import main
    elif jogo == 'formiga':
        from jogos.formiga import main
    else:
        return
    main()


if __name__ == '__main__':
    main()
