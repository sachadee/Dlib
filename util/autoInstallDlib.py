import sys
import subprocess
import platform

def install_dlib():
    """
    Attempts to install Dlib using standard pip install first, 
    falling back to a specific wheel file if necessary.
    """
    print('Attempting to install Dlib...')
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'dlib'])
        print('Dlib installed successfully using standard pip install.')
        return True
    except subprocess.CalledProcessError as e:
        print(f'Standard pip install failed: {e}')
    
    versionA = platform.python_version().split('.')
    version_str = f"{versionA[0]}{versionA[1]}"
    wheel_url = f'https://github.com/sachadee/Dlib/raw/main/dlib-20.0.0-cp{version_str}-cp{version_str}-win_amd64.whl'
    
    try:
        print(f'Falling back to installing specific wheel: {wheel_url}')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', wheel_url])
        print('Dlib installed successfully using specific wheel file.')
        return True
    except subprocess.CalledProcessError as e:
        print(f'Dlib installation failed using both methods: {e}')
        return False


try:
    import dlib
    print(f'Dlib {dlib.__version__} already installed. Exiting script.')
    sys.exit(0) 

except ImportError:
    print(f'Dlib not found locally.')
    
    if install_dlib():
        try:
            import dlib
            print(f'Verification: Dlib {dlib.__version__} is now available.')
        except ImportError:
            print('Verification failed. Dlib might require a new script execution.')
            
    sys.exit(0)
