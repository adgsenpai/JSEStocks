from setuptools import setup, find_packages

setup(
    #metadata here
    name="mymodule",
    version="0.0.1",
    author="Ashlin Darius Govindasamy",
    author_email="adg@adgstudios.co.ZA",
    url="https://www.adgstudios.co.za",
    description="templete for module generation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #license here
    license='MIT', 
    #modules here
    install_requires=["numpy"]
)
