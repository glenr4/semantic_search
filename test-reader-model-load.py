from haystack.nodes import TransformersReader
import os

print(os.getcwd())
print(__file__)
# print(os.path.dirname(__file__))
# os.chdir(os.path.dirname(__file__))
# print(os.getcwd())

# reader = FARMReader(model_name_or_path="./roberta-base-squad2", use_gpu=True)
reader = TransformersReader(
    model_name_or_path="./roberta-base-squad2", tokenizer="./roberta-base-squad2")
print("Finished")
