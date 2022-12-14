# haystack/utils/export_utils.py

from typing import Dict


def filterAnswers(prediction: Dict):
    filtered_answers = []
    answers = prediction["answers"]

    for ans in answers:
        filtered_ans = {
            field: getattr(ans, field)
            for field in ["answer", "context", "score"]
            if getattr(ans, field) is not None
        }
        filtered_answers.append(filtered_ans)

    return filtered_answers
