"""
File: analyze_coverage.py
Date: 4.13.2020
Author: Kyle Lanier

Porpose:
This file is an abstraction from the .github workflows pythonapp.yml
and its purpose is to consolidate unittest as well as code coverage
processes.

This file can be executed directly in order to analyze coverage
for new development prior to the submission of pull or
merge requests.

Process:
First we import the necessary modules, then we use the coverage
module to execute all unittests where in doing so statements
will be evaluated for code coverage. A .coverage report is then
generated and converted into a bage for use within the README
which displays on github. After the badge is generated the
unnecessary .coverage report is removed.

"""
import os

if __name__ == '__main__':
    os.system('pip install coverage')
    os.system('pip install coverage-badge')

    print('\nExecuting Test Driven Development UnitTests\n')
    os.system('coverage run test_suite.py')

    print('\nExecuting Coverage Report\n')
    os.system('coverage report -m --omit=*\\__init__.py')
    os.system(f"coverage-badge -o {os.path.join('resources', 'coverage.svg')} -f")
    os.system('coverage erase')

    # print('\nExecuting Sphinx Document Generation\n')
    # os.system('pip install sphinx')
    # os.system(f"sphinx-apidoc -o {os.path.join('sphinx')} .")
    # os.system(f"sphinx-build -b html {os.path.join('sphinx')} {os.path.join('sphinx', '_build')}")
