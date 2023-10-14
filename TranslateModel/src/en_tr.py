import pickle
from utils import to_tensor, generate_attention_map, beam_search
from models import Seq2Seq
from vocab import Vocab, Vocabularies
from nltk.tokenize import RegexpTokenizer
import os
#python test.py --model_file experiments/08_23_2023_23_21_16/improved_model.bin --valid_data valid_tokenized.tr valid_tokenized.en
puncts_except_apostrophe = '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
TOKENIZE_PATTERN = fr"[{puncts_except_apostrophe}]|\w+|['\w]+"
tokenizer = RegexpTokenizer(pattern=TOKENIZE_PATTERN)

MODEL_PATH = "model.bin"
VOCAB_FILE = "vocabs.pkl"
def Translate(sentence):
    model = Seq2Seq.load("TranslateModel/model/mx-1.0.6/model.bin")
    model.device = "cpu"
    text_input = sentence
    tokenized_sent = tokenizer.tokenize(text_input)
    hypothesis = beam_search(model, [tokenized_sent], beam_size=1, max_decoding_time_step=70)[0]
    for idx, hyp in enumerate(hypothesis):
        return ' '.join(hyp.value)