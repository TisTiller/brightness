import os
from PIL import Image
import numpy as np
import base64

files = os.listdir()
files.remove(__file__)

print(files)
print(f"Number of files: {len(files)}")
for x in files:
    try:
        with open(x, "rb") as img_file:
            img1 = base64.b64encode(img_file.read()).decode('utf-8')

        for y in files:
            if x == y:
                continue
            try:
                with open(y, "rb") as img_file_:
                    img2 = base64.b64encode(img_file_.read()).decode('utf-8')

                if img1 == img2:
                    os.remove(y)
                    print(f"{x} = {y}")

            except IndexError:
                print("End.")

            except FileNotFoundError:
                pass
            except IsADirectoryError:
                pass
    except FileNotFoundError:
        pass
    except IsADirectoryError:
        pass