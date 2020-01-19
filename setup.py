from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='Penalty Kick Saver',
    version='1',
    packages=['Penalty_Kick_Saver'],
    url='',
    license='MIT',
    author='Dtji AppDev',
    author_email='dtjiappdev1999@gmail.com',
    description='This is a simple game where the player becomes the goalkeeper whose job is to save the penalty kick.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "Penalty Kick Saver=Penalty_Kick_Saver.penalty_kick_saver:main",
        ]
    }
)
