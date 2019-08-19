from pkg_resources import parse_requirements
from setuptools import setup


def parse_requirements_from_file(path):
    """Yield each requirement from file at `path` as ``str``."""
    with open(path) as file:
        for pkg in parse_requirements(file):
            yield str(pkg)

setup(
    use_scm_version=True,
    install_requires=parse_requirements_from_file(
        'requirements/install.txt'
    ),
    tests_require=parse_requirements_from_file(
        'requirements/tests.txt'
    ),
    setup_requires=[*parse_requirements_from_file(
        'requirements/setup.txt'
    )]
)
