from setuptools import setup

LONG_DESCRIPTION = open('README.rst').read()

setup(
    name="VoiceCoding",
    version="1.0.0",
    packages=["voice_coding"],
    license="MIT",
    description="Coding in Python using your voice",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/michaelpri10/VoiceCoding",
    author="Michael Prieto (michaelpri10)",
    author_email="michaelpri10@gmail.com",
    install_requires=["SpeechRecognition", "pyaudio"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Code Generators"
    ],
    entry_points={
        'console_scripts': [
            'voice_coding = voice_coding.voice_coding:main',
        ],
    }
)
