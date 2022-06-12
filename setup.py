import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r") as fh:
    long_description = fh.read()
des = long_description

setuptools.setup(
    name='firebase-compsci',                           # should match the package folder
    packages=['firebase-compsci'],                     # should match the package folder
    version='0.0.1',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Computer Science Firebase Package',
    long_description_content_type="text/markdown",
    long_description=des,              # loads your README.md
    author='Eoin Gallen',
    author_email='egallen@sainteunans.com',
    url='https://github.com/MrGallen/firebase-compsci', 
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "firebase-compsci", "tutorial"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/MrGallen/firebase-compsci/archive/refs/tags/setup.py.tar.gz",
)