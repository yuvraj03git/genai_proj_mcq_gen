from setuptools import find_packages,setup



setup(
 
 name='mcqgenerator',
 version='0.0.1',
 author='Yuvraj Shivam',
 author_email="iib2021006@iiita.ac.in",
 install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
 packages=find_packages()

)