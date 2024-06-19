class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, resolution):
        self.resolution = resolution


image = Image("100x100", "Image", "png")
print(image.__dict__)
image.resize("200x200")
print(image.__dict__)

