from setuptools import setup
import os

VERSION = "0.0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-kepler-map",
    description="Datasette plugin that shows a map for any data with latitude/longitude columns using the Kepler Library",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/dav43/datasette-kepler-map",
    project_urls={
        "Issues":https://github.com/dav43/datasette-kepler-map/issues",
        "CI": "https://github.com/dav43/datasette-kepler-map/actions",
        "Changelog": "https://github.com/dav43/datasette-kepler-map/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_kepler_map"],
    entry_points={"datasette": ["cluster_map = datasette_kepler_map"]},
    package_data={
        "datasette_kepler_map": [
            "static/*.js",
            "static/*.css",
        ]
    },
    install_requires=["datasette>=0.54", "datasette-leaflet>=0.2.2"],
    extras_require={
        "test": ["pytest", "pytest-asyncio", "httpx", "sqlite-utils", "nest-asyncio"],
        "playwright": ["pytest-playwright"],
    },
)
