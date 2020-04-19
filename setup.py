import setuptools

setuptools.setup(
    name="broker_json",
    version="0.1",
    author="Vlad Grigorescu",
    author_email="vlad@es.net",
    description="Utilities to convert between Broker data types and JSON",
    packages=setuptools.find_packages(),
    include_package_data=True,
)