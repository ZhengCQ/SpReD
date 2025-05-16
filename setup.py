from setuptools import setup, find_packages

setup(
    name='spred',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='Splicing-regulatory Driver Genes Identification Tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/asge-demo',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'click',
        'pandas',
        'numpy',
        'scipy',
        'statsmodels',
    ],
    entry_points={
        'console_scripts': [
            'spred=spred.main:cli'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
