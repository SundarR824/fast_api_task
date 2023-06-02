import pathlib
import sys
cr_path = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(cr_path))

print(f"{cr_path}\\chromedriver\\chromedriver.exe")
