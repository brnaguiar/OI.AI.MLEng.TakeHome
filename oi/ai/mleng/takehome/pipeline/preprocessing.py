import torchvision.transforms as transforms
from PIL import Image


class ImagePreprocessor:
    def __init__(self):
        self.transform = transforms.Compose(
            [
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

    def __call__(self, image_path):
        image = Image.open(image_path)
        image = self.transform(image)
        return image.unsqueeze(0)  # Add batch dimension
