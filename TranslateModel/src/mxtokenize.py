import spacy
from nltk.tokenize import RegexpTokenizer

# Türkçe için tokenizer
puncts_except_apostrophe = '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
TOKENIZE_PATTERN = fr"[{puncts_except_apostrophe}]|\w+|['\w]+"
tr_regex_tokenizer = RegexpTokenizer(pattern=TOKENIZE_PATTERN)

# İngilizce için modeli yükle
en_nlp = spacy.load('en_core_web_sm')

def tokenize_and_save_nltk(input_file, output_file, tokenizer):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tokenized_lines = []

    for line in lines:
        tokenized_line = tokenizer(line)
        tokenized_lines.append(" ".join(tokenized_line))

    with open(output_file, 'w', encoding    ='utf-8') as f:
        f.write("\n".join(tokenized_lines))

def tokenize_and_save_spacy(input_file, output_file, tokenizer):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    tokenized_lines = []

    for line in lines:
        tokenized_line = tokenizer(line)
        tokenized_lines.append(" ".join([tok.text for tok in tokenized_line]))
    with open(output_file, 'w', encoding    ='utf-8') as f:
        f.write("".join(tokenized_lines))

# Türkçe metinleri tokenlere ayır ve kaydet
tokenize_and_save_nltk('train.tr', 'train_tokenized.tr', tr_regex_tokenizer.tokenize)
tokenize_and_save_nltk('valid.tr', 'valid_tokenized.tr', tr_regex_tokenizer.tokenize)
tokenize_and_save_nltk('test.tr', 'test_tokenized.tr', tr_regex_tokenizer.tokenize)


# İngilizce metinleri tokenlere ayır ve kaydet
tokenize_and_save_spacy('train.en', 'train_tokenized.en', en_nlp.tokenizer)
tokenize_and_save_spacy('valid.en', 'valid_tokenized.en', en_nlp.tokenizer)
tokenize_and_save_spacy('test.en', 'test_tokenized.en', en_nlp.tokenizer)

