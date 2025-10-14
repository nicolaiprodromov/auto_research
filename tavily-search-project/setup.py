from setuptools import setup, find_packages

setup(
    name='tavily-search-project',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project to search the internet using the Tavily API',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',  # Assuming the Tavily API client uses requests
        'python-dotenv',  # For loading environment variables from .env files
        'pytest'  # For testing
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)