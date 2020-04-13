import os

if __name__ == '__main__':
    os.system('pip install coverage')
    os.system('pip install coverage-badge')
    
    print('\nExecuting Test Driven Development UnitTests\n')
    os.system('coverage run test_suite.py')
    
    print('\nExecuting Coverage Report\n')
    os.system('coverage report -m --omit=*\\__init__.py')
    os.system(f"coverage-badge -o {os.path.join('documents', 'coverage.svg')} -f")
    os.system('coverage erase')
