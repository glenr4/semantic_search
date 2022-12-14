# https://github.com/deepset-ai/haystack/blob/main/rest_api/rest_api/controller/search.py
# https: // fastapi.tiangolo.com/

from fastapi import FastAPI
import uvicorn
from haystack.pipelines.base import Pipeline
from pipelineUtils import get_pipelines
from initQueryPipeline import initQueryPipeline
from filterAnswers import filterAnswers

# Query Pipeline
initQueryPipeline()
queryPipeline: Pipeline = get_pipelines().get("queryPipeline", None)

# API
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test-query")
async def test_query():
    prediction = queryPipeline.run(
        query="Who is the father of Arya Stark?", params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
    )

    data = filterAnswers(prediction)

    return data


@app.post("/query")
async def query(question):
    prediction = queryPipeline.run(
        query=question, params={"Retriever": {
            "top_k": 10}, "Reader": {"top_k": 5}}
    )

    data = filterAnswers(prediction)

    return data

# For debugging
# https: // fastapi.tiangolo.com/tutorial/debugging /?h = debug
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
