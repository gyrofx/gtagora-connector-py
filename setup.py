import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gtagora-connector",
    version="0.0.1",
    author="Felix Eichenberger, Martin Bührer",
    author_email="felix.eichenberger@gyrtools.com, martin.buehrer@gyrotools.com",
    description="The Agora Connector for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gyrotools/gtagora",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests>=2.0',
    ],
    python_requires='>=3.6.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
