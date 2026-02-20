import os
from PIL import Image, ImageSequence

folder_path = os.getcwd()

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".webp"):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    frames = []
                    durations = []

                    is_animated = getattr(img, "is_animated", False)

                    if is_animated:
                        for frame in ImageSequence.Iterator(img):
                            if frame.mode in ("RGBA", "LA"):
                                alpha = frame.getchannel("A")
                                bw = frame.convert("L")
                                bw = Image.merge("LA", (bw, alpha))
                            else:
                                bw = frame.convert("L")

                            frames.append(bw)
                            durations.append(frame.info.get("duration", 100))

                        frames[0].save(
                            file_path,
                            save_all=True,
                            append_images=frames[1:],
                            duration=durations,
                            loop=img.info.get("loop", 0),
                            format="WEBP"
                        )
                    else:
                        if img.mode in ("RGBA", "LA"):
                            alpha = img.getchannel("A")
                            bw = img.convert("L")
                            bw = Image.merge("LA", (bw, alpha))
                        else:
                            bw = img.convert("L")

                        bw.save(file_path, "WEBP")

                print(f"Make: {filename}")

            except Exception as e:
                print(f"Error {filename}: {e}")

print("End!")