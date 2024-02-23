from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Prem',
    install_requires=["huggingface_hub","transformers","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)