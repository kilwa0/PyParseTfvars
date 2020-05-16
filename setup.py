from setuptools import setup

setup(
   name='PyParseTfvars',
   version='0.1',
   description="""
    Reads tfvars file and export
    value to be userd by python""",
   author='kilwa0',
   author_email='kilwacero@gmail.com',
   packages=['parsetfvars'],  # same as name
   install_requires=['re'],  # external packages as dependencies
)
