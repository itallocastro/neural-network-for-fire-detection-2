import sys
from setuptools import setup

setup(
        name="TF Fire Detection",
        version="1.0",
        packages=["firedetection"],
        author="Jeferson Fernando",
        author_email="jfss@ic.ufal.br",
        description="Fire detection with webcam image.",
        license="MIT",
        keywords= "opencv",
        url="",
        entry_points = {"console_scripts":["firedetection = firedetection.main:main"]},
        )
