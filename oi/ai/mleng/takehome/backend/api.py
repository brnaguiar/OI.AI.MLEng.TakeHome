import os
import tempfile

import aiohttp
import hydra
import uvicorn
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from hydra.core.config_store import ConfigStore

from oi.ai.mleng.takehome.backend.frontend import (
    get_prediction_html,
    get_root_html,
)
from oi.ai.mleng.takehome.config.config import Files
from oi.ai.mleng.takehome.pipeline.model import MarineAnimalClassifier
from oi.ai.mleng.takehome.pipeline.postprocessing import ClassLoader
from oi.ai.mleng.takehome.pipeline.preprocessing import ImagePreprocessor

cs = ConfigStore.instance()
cs.store(name="files_config", node=Files)


hydra.initialize(version_base=None, config_path="../../../../../conf")
cfg = hydra.compose(config_name="application.yaml", return_hydra_config=True)

preprocessor = ImagePreprocessor()
classifier = MarineAnimalClassifier(preprocessor)
postprocessor = ClassLoader(cfg.files.data.labels).load_data()

app = FastAPI()


@app.get("/")
async def read_root():
    return HTMLResponse(content=get_root_html())


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
    return HTMLResponse(content=get_prediction_html(prediction, url))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
