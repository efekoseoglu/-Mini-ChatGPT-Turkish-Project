from utilsx import beam_search
from modelsx import Seq2Seq
from vocab import Vocab, Vocabularies
from nltk.tokenize import RegexpTokenizer
puncts_except_apostrophe = '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
TOKENIZE_PATTERN = fr"[{puncts_except_apostrophe}]|\w+|['\w]+"
tokenizer = RegexpTokenizer(pattern=TOKENIZE_PATTERN)

MODEL_PATH = "model.bin"
VOCAB_FILE = "vocabs.pkl"
def Translate_en(sentence):
    model = Seq2Seq.load("TranslateModel/model/mx-1.0.6/model.bin")
    model.device = "cpu"
    text_input = sentence
    tokenized_sent = tokenizer.tokenize(text_input)
    hypothesis = beam_search(model, [tokenized_sent], beam_size=1, max_decoding_time_step=70)[0]
    for idx, hyp in enumerate(hypothesis):
        return ' '.join(hyp.value)