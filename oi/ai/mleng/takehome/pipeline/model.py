import torch
import torchvision as models

from oi.ai.mleng.takehome.pipeline.preprocessing import ImagePreprocessor


class MarineAnimalClassifier:
    """
    A class used to classify images of marine animals using a pre-trained \
            ResNet-50 model.

    The MarineAnimalClassifier class initializes a ResNet-50 model \
            pre-trained on the ImageNet dataset, sets it to evaluation mode, \
            and uses a specified preprocessor to prepare images for \
            classification.

    Attributes
    ----------
    model : torch.nn.Module
        The pre-trained ResNet-50 model for image classification.
    device : torch.device
        The device (CPU or CUDA) on which the model is run.
    preprocessor : ImagePreprocessor
        An instance of the ImagePreprocessor class for image preprocessing.

    Methods
    -------
    __init__(preprocessor: ImagePreprocessor = ImagePreprocessor()):
        Initializes the MarineAnimalClassifier with a pre-trained ResNet-50 \
                model and the specified image preprocessor.

    predict(image_path: str) -> int:
        Predicts the class index of the given image.
    """

    def __init__(self, preprocessor: ImagePreprocessor = ImagePreprocessor()):
        """
        Initializes the MarineAnimalClassifier with a pre-trained ResNet-50 \
                model and the specified image preprocessor.

        Parameters
        ----------
        preprocessor : ImagePreprocessor, optional
            An instance of the ImagePreprocessor class (default is \
                    ImagePreprocessor()).
        """
        self.model = models.models.resnet50(
            weights=models.models.ResNet50_Weights.IMAGENET1K_V2
        )
        self.model.eval()  # Set the model to evaluation mode

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        self.model.to(self.device)
        self.preprocessor = preprocessor

    def predict(self, image_path: str) -> int:
        """
        Predicts the class of the given image.

        This method preprocesses the image using the specified preprocessor,
        performs the prediction using the ResNet-50 model, and returns the
        predicted class index.

        Parameters
        ----------
        image_path : str
            Path to the image file.

        Returns
        -------
        int
            Predicted class index.
        """
        image = self.preprocessor(image_path).to(self.device)

        # Perform the prediction
        with torch.no_grad():
            outputs = self.model(image)
            _, predicted = outputs.max(1)

        # Return the predicted class index
        return predicted.item()
