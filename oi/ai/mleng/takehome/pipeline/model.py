import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

from oi.ai.mleng.takehome.pipeline.preprocessing import ImagePreprocessor


class MarineAnimalClassifier:
    def __init__(self, preprocessor: ImagePreprocessor = ImagePreprocessor()):
        self.model = models.resnet50(
            weights=models.ResNet50_Weights.IMAGENET1K_V2
        )
        self.model.eval()  # Set the model to evaluation mode

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        self.model.to(self.device)
        self.preprocessor = preprocessor

    def predict(self, image_path: str):
        """
        Predict the class of the given image.

        Args:
            image_path (str): Path to the image file.

        Returns:
            int: Predicted class index.
        """
        image = self.preprocessor(image_path).to(self.device)

        # Perform the prediction
        with torch.no_grad():
            outputs = self.model(image)
            _, predicted = outputs.max(1)

        # Return the predicted class index
        return predicted.item()
