from setuptools import setup, find_packages

setup(
    name="phonetracer",
    version="2.1",
    packages=find_packages(),
    install_requires=[
        'phonenumbers>=8.12.0',
    ],
    entry_points={
        'console_scripts': [
            'phonetracer=phonetracer.cli:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="OSINT phone number tracing tool",
    license="MIT",
    keywords="phone number tracing osint",
    url="https://github.com/yourusername/PhoneTracer",
)
