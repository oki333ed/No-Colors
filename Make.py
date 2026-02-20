import os
from PIL import Image

EXCLUDED = {
    "GJ_GameSheet02.png",
    "GJ_GameSheet02-hd.png",
    "GJ_GameSheet02-uhd.png",
    "pack.png"
}

folder = os.getcwd()

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    if (
        os.path.isfile(filepath) and
        filename.lower().endswith(".png") and
        filename not in EXCLUDED
    ):
        try:
            img = Image.open(filepath).convert("RGBA")

            gray = img.convert("L")

            if "A" in img.getbands():
                alpha = img.split()[-1]
                gray = Image.merge("LA", (gray, alpha)).convert("RGBA")
            else:
                gray = gray.convert("RGBA")

            gray.save(filepath)
            print(f"Make: {filename}")

        except Exception as e:
            print(f"Error {filename}: {e}")

print("End!")