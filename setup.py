import setuptools

from pip.req import parse_requirements

with open("README.old.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DL-Art-School",
    packages=setuptools.find_packages(),
    version="0.0.1",
    author="James Betker",
    author_email="james@adamant.ai",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.ecker.tech/mrq/DL-Art-School",
    project_urls={},
    scripts=[],
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt', session='hack'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
