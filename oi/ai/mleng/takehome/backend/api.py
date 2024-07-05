import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

from oi.ai.mleng.takehome.pipeline.model import MarineAnimalClassifier
from oi.ai.mleng.takehome.pipeline.preprocessing import ImagePreprocessor

# Instantiate the classifier
preprocessor = ImagePreprocessor()
classifier = MarineAnimalClassifier(preprocessor)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Marine Animal Classifier API"}


@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)) -> JSONResponse:
    # Save file
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(file.file.read())

    # Perform prediction
    class_idx: int = classifier.predict(temp_file_path)
    return JSONResponse(content={"class_index": class_idx})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
