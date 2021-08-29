from pathlib import Path
from PIL import Image
from random import choice

composition_order = ["background", "body", "face", "eyes", "hat", "chest", "arms"]
ASSETS = {
    "arms": list(Path.cwd().joinpath("./assets/arms").glob("**/*.PNG")),
    "background": list(Path.cwd().joinpath("./assets/background").glob("**/*.PNG")),
    "body": list(Path.cwd().joinpath("./assets/body").glob("**/*.PNG")),
    "chest": list(Path.cwd().joinpath("./assets/chest").glob("**/*.PNG")),
    "eyes": list(Path.cwd().joinpath("./assets/eyes").glob("**/*.PNG")),
    "face": list(Path.cwd().joinpath("./assets/face").glob("**/*.PNG")),
    "hat": list(Path.cwd().joinpath("./assets/hat").glob("**/*.PNG")),
}
img_composite = Image.new("RGBA", (2550, 3300))

for layer in composition_order:
    try:
        random_asset = choice(ASSETS.get(layer))
        with Image.open(random_asset) as im:
            img_composite = Image.alpha_composite(img_composite, im)
    except Exception as e:
        print("cannot open: ", layer)

img_composite.show()
