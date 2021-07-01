import setuptools

setuptools.setup(
    name="broker_json",
    version="0.1",
    license="bsd-3-clause",
    author="Vlad Grigorescu",
    author_email="vlad@es.net",
    description="Utilities to convert between Broker data types and JSON",
    url="https://github.com/grigorescu/broker-to-json",
    download_url="https://github.com/grigorescu/broker-to-json/archive/v_01.tar.gz",
    packages=setuptools.find_packages(),
    include_package_data=True,
    keywords = ["zeek", "broker"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
  ],
)
