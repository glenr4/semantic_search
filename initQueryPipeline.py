import os

from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import BM25Retriever
from haystack.nodes import TransformersReader
from haystack.pipelines import ExtractiveQAPipeline
from fileUtils import setWorkingToCurrentFile
from pipelineUtils import set_pipelines


def initQueryPipeline():
    setWorkingToCurrentFile()

    # Get the host where Elasticsearch is running, default to localhost
    host = os.environ.get("ELASTICSEARCH_HOST", "localhost")
    document_store = ElasticsearchDocumentStore(
        host=host, username="", password="", index="document")

    # Retrieval pipeline
    retriever = BM25Retriever(document_store=document_store)
    reader = TransformersReader(
        model_name_or_path="./roberta-base-squad2", tokenizer="./roberta-base-squad2")
    pipe = ExtractiveQAPipeline(reader, retriever)

    set_pipelines('queryPipeline', pipe)
