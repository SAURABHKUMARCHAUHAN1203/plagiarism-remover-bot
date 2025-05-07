from transformers import pipeline, PegasusForConditionalGeneration, PegasusTokenizer, BartForConditionalGeneration, BartTokenizer
import openai
import logging
from typing import List
import language_tool_python

logger = logging.getLogger(__name__)

class ParaphraseEnsemble:
    def __init__(self):
        self.t5 = pipeline("text2text-generation", model="humarin/chatgpt_paraphraser_on_T5")
        self.pegasus_tokenizer = PegasusTokenizer.from_pretrained("tuner007/pegasus_paraphrase")
        self.pegasus_model = PegasusForConditionalGeneration.from_pretrained("tuner007/pegasus_paraphrase")
        self.bart_tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.bart_model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
        self.grammar_tool = language_tool_python.LanguageTool('en-US')
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def paraphrase_t5(self, text: str) -> str:
        return self.t5(text, max_length=len(text)+100)[0]['generated_text']

    def paraphrase_pegasus(self, text: str) -> str:
        inputs = self.pegasus_tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.pegasus_model.generate(**inputs, max_length=100)
        return self.pegasus_tokenizer.decode(outputs[0], skip_special_tokens=True)

    def paraphrase_bart(self, text: str) -> str:
        inputs = self.bart_tokenizer(text, return_tensors="pt", truncation=True)
        outputs = self.bart_model.generate(**inputs, max_length=100)
        return self.bart_tokenizer.decode(outputs[0], skip_special_tokens=True)

    def paraphrase_gpt(self, text: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Paraphrase this formally: {text}"}],
            temperature=0.7,
        )
        return response.choices[0].message.content

    def correct_grammar(self, text: str) -> str:
        return self.grammar_tool.correct(text)

    def ensemble_paraphrase(self, text: str) -> str:
        outputs = [
            self.paraphrase_t5(text),
            self.paraphrase_pegasus(text),
            self.paraphrase_bart(text),
            self.paraphrase_gpt(text)
        ]
        # Select the output with median length (often most balanced)
        outputs.sort(key=len)
        best_output = outputs[len(outputs)//2]
        return self.correct_grammar(best_output)
