import torchvision as transforms
from PIL import Image


class ImagePreprocessor:
    """
    A class used to preprocess images for input into a neural network.

    The ImagePreprocessor class utilizes a sequence of transformations to
    resize, crop, normalize, and convert an image to a tensor suitable
    for model input.

    Attributes
    ----------
    transform : torchvision.transforms.Compose
        A composed transform that includes resizing to 256x256, \
                center cropping to 224x224, converting to a tensor, \
                and normalizing with mean and standard deviation values.

    Methods
    -------
    __init__():
        Initializes the ImagePreprocessor with the required transformations.

    __call__(image_path: str) -> torch.Tensor:
        Opens the image from the given path, applies the transformations, \
                and returns the processed image tensor
        with an added batch dimension.
    """

    def __init__(self):
        """
        Initializes the ImagePreprocessor with
            a series of image transformations.

        The transformations applied are:
        1. Resize the image to 256x256 pixels.
        2. Center crop the image to 224x224 pixels.
        3. Convert the image to a PyTorch tensor.
        4. Normalize the image tensor using mean = \
                [0.485, 0.456, 0.406] and std = [0.229, 0.224, 0.225].
        """
        self.transform = transforms.transforms.Compose(
            [
                transforms.transforms.Resize(256),
                transforms.transforms.CenterCrop(224),
                transforms.transforms.ToTensor(),
                transforms.transforms.Normalize(
                    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
                ),
            ]
        )

    def __call__(self, image_path):
        """
        Opens an image, applies the defined transformations,
            and returns a processed tensor.

        Parameters
        ----------
        image_path : str
            The file path to the image to be processed.

        Returns
        -------
        torch.Tensor
            The transformed image tensor with an added batch dimension.
        """
        image = Image.open(image_path)
        image = self.transform(image)
        return image.unsqueeze(0)  # Add batch dimension
