from setuptools import setup, find_packages

NOME = 'jogos'
VERSION = 0.1


setup(
    name=NOME,
    version=VERSION,
    install_requires=[
        'click',
        'pygame',
        'pygame_gui'
    ],
    packages=find_packages(),
    include_package_data = True,
    entry_points={
        'gui_scripts': [
            'roda = jogos.__main__:main'
        ]
    }
)
