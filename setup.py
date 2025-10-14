from setuptools import setup, find_packages

setup(
    name='automate-research',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project with API clients and research automation workflows',
    packages=find_packages(include=['clients', 'clients.*', 'workflows', 'workflows.*']),
    install_requires=[
        'requests',
        'python-dotenv',
        'pytest',
        'openai>=1.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)