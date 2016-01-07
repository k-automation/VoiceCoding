try:
    from setuptools import setup
except:
    from distutils.core import setup

LONG_DESCRIPTION = open('README.md').read()

setup(
    name="VoiceCoding",
    version="1.0.0a1",
    packages=["voice_coding"],
    license="MIT",
    description="Coding in Python using your voice",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/michaelpri10/VoiceCoding",
    author="Michael Prieto (michaelpri10)",
    author_email="michaelpri10@gmail.com"
)
