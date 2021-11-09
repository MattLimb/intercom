import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intercom",
    version="0.3.0",
    author="Matt Limb",
    author_email="matt.limb17@gmail.com",
    description="Track open source software releases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MattLimb/intercom",
    packages=setuptools.find_packages(),
    install_requires=[
        "click>=7.1.2",
        "PyGithub>=1.53",
        "python-gitlab>=2.5.0",
        "PyYAML==6.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
