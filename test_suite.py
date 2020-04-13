"""
File: test_suite.py
Date: 4.13.2020
Author: Kyle Lanier

Porpose:
This file is used to import all unittest files to be executed
by the Execute unittests and coverage report build process as
defined in .github workflows pythonapp.yml

This also serves a a singular point of entry for debugging
all unittests. Set your breakpoints within your unittest
file, then come back to this file to execute in debug mode
to step into your breakpoints.

Process:
For every new unittest test file created in the unit_tests
directory, add the respective import statement below. Unittest
main will then execute all unittest modules imported within
this file.

"""
from unittest import main
from unit_tests.test_pysqllite import TestPySQLLite  # noqa: F401


main(exit=False)
