import setuptools


with open("README.md") as f:

    readme = f.read()

with open("LICENSE.txt") as f:

    license = f.read()

packages = setuptools.find_packages(exclude = ("tests",))

print("Found packages " + str(packages))

setuptools.setup(
    name = "package",
    version = "0.1.0a0",
    packages = packages,
    description = "A minimal example of a Python package",
    long_description = readme,
    license = license,
    author = "Alexander G. Zimmerman",
    author_email = "zimmerman@aices.rwth-aachen.de",
)
