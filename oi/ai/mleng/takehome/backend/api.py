import os
import tempfile

import aiohttp
import uvicorn
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse

from oi.ai.mleng.takehome.pipeline.model import MarineAnimalClassifier
from oi.ai.mleng.takehome.pipeline.postprocessing import ClassLoader
from oi.ai.mleng.takehome.pipeline.preprocessing import ImagePreprocessor

preprocessor = ImagePreprocessor()
classifier = MarineAnimalClassifier(preprocessor)
postprocessor = ClassLoader(
    "../../../../../data/labels/imagenet_class_index.json"
).load_data()

app = FastAPI()


@app.get("/")
def read_root():
    content2 = """
    <html>
        <head>
            <title>Marine Animal Predictor</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f2f9ff;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #003366;
                }
                form {
                    display: inline-block;
                    background-color: #fff;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }
                input[type="text"], input[type="submit"] {
                    margin: 5px;
                    padding: 10px;
                    border-radius: 5px;
                }
                input[type="text"] {
                    border: 1px solid #003366;
                }
                input[type="submit"] {
                    background-color: #003366;
                    color: #fff;
                    border: none;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #00509e;
                }
            </style>
        </head>
        <body>
            <h1>Marine Animal Predictor</h1>
            <form action="/predict/" method="post">
                <input name="url" type="text" placeholder="Enter image URL">
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content2)


@app.post("/predict/")
async def predict_image2(url: str = Form(...)) -> HTMLResponse:
    filename = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                temp_dir = tempfile.gettempdir()
                temp_file_path = os.path.join(temp_dir, filename)
                with open(temp_file_path, "wb") as f:
                    f.write(content)
            else:
                raise HTTPException(
                    status_code=response.status,
                    detail="Failed to download file",
                )

    # Perform prediction
    class_idx: int = classifier.predict(temp_file_path)

    prediction = postprocessor.get_animal_name_by_index(class_idx)
    content = f"""
    <html>
        <head>
            <title>Prediction Result</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #e0f7fa;
                    text-align: center;
                    padding: 50px;
                }}
                h1 {{
                    color: #003366;
                }}
                .result {{
                    display: inline-block;
                    background-color: #fff;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 5px;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                    border: 1px solid #003366;
                    border-radius: 5px;
                }}
                .prediction {{
                    margin-top: 10px;
                    font-size: 1.2em;
                    color: #003366;
                }}
            </style>
        </head>
        <body>
            <h1>It's a {prediction}!</h1>
            <div class="result">
                <img src="{url}" alt="Marine Animal Image">
            </div>
            <br>
            <a href="/">Go Back</a>
        </body>
    </html>
    <div class="prediction"></div>
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
