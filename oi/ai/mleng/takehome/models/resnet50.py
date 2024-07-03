import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

model = models.resnet50(pretrained=True)
model.eval()  # Set the model to evaluation mode

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), # Pre-defined ImageNet parameters
])

def predict(image_path):
    image = Image.open(image_path)
    image = preprocess(image)
    image = image.unsqueeze(0)  # Add batch dimension

    # Perform the prediction
    with torch.no_grad():
        outputs = model(image)
        _, predicted = outputs.max(1)

    # Map the predicted index to the class name
    class_idx = predicted.item()
    return class_idx
