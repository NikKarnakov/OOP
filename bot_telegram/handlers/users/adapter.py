from transformers import GPT2Config
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

label2id = {
    "negative": 0,
    "positive": 1,
}
id2label = {
    0: "negative",
    1: "positive",
}


class AdapterML(object):
    def __init__(self, name_file_checkpoint):
        config = GPT2Config.from_pretrained(f"./{name_file_checkpoint}", label2id=label2id, id2label=id2label)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.tokenizer = GPT2Tokenizer.from_pretrained(f"./{name_file_checkpoint}")
        self.model = GPT2LMHeadModel.from_pretrained(f"./{name_file_checkpoint}", config=config).to(self.device)

    def generate(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt").to(self.device)
        self.model.eval()
        with torch.no_grad():
            out = self.model.generate(input_ids,
                                      do_sample=True,
                                      num_beams=2,
                                      temperature=1.5,
                                      top_p=0.9,
                                      max_length=100,
                                      )

        generated_text = list(map(self.tokenizer.decode, out))[0]
        return generated_text