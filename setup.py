import setuptools

setuptools.setup(
    name='compscifirebase',                           # should match the package folder
    packages=['compscifirebase'],                     # should match the package folder
    version='0.0.1',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Computer Science Firebase Package',
    author='Eoin Gallen',
    author_email='egallen@sainteunans.com',
    url='https://github.com/MrGallen/firebase-compsci', 
    install_requires=['requests>=2.19.1',
        'requests_toolbelt>=0.7.1',
        'gcloud>=0.18.3',
        'oauth2client>=4.1.2',
        'python-jwt>=2.0.1',
        'pycryptodome>=3.6.4', 'sseclient'],                  # list all packages that your package uses
    keywords=["pypi", "compscifirebase", "tutorial"], #descriptive meta-data
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