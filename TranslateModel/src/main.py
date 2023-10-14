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

def main():
    

    print("Available models:")
    model_files = [file for file in os.listdir("TranslateModel/model") ]
    for idx, model_file in enumerate(model_files):
        print(f"{idx + 1}. {model_file}")
    while True:
        try:
            choice = int(input("Select a model (enter the corresponding number): "))
            if 1 <= choice <= len(model_files):
                selected_model = model_files[choice - 1]
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
                print("Invalid input. Please enter a valid number.")
    with open(f"model/{selected_model}/vocabs.pkl", "rb") as f:
        vocabs = pickle.load(f)

    model = Seq2Seq.load(f"model/{selected_model}/model.bin")
    model.device = "cpu"
    while True:    
    
        text_input = input("Enter a sentence: ")
        if text_input=="quit":
            break
        tokenized_sent = tokenizer.tokenize(text_input)
        print("Tokenized input:", tokenized_sent)

        hypothesis = beam_search(model, [tokenized_sent], beam_size=3, max_decoding_time_step=70)[0]
        print("Hypothesis:")
        for idx, hyp in enumerate(hypothesis):
            print(f"{idx}: {' '.join(hyp.value)}, Score: {hyp.score:.2f}")
if __name__ == "__main__":
    main()
