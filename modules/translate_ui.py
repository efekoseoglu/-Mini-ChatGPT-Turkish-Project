from utilsx import to_tensor, generate_attention_map, beam_search
from modelsx import Seq2Seq
from vocab import Vocab, Vocabularies
from nltk.tokenize import RegexpTokenizer
import gradio as gr
from modules import shared, ui
from modules.utils import gradio
from langdetect import detect

puncts_except_apostrophe = '!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~'
TOKENIZE_PATTERN = fr"[{puncts_except_apostrophe}]|\w+|['\w']+"
en_tr = Seq2Seq.load("TranslateModel/model/mx-1.0.6/model.bin")
en_tr.device = "cpu"
tr_en = Seq2Seq.load("TranslateModel/model/mx-1.0.5/model.bin")
tr_en.device = "cpu"
tokenizer = RegexpTokenizer(pattern=TOKENIZE_PATTERN)

# Gradio UI oluşturma işlevi
def create_ui():
    with gr.Tab('Ceviri', elem_id='ceviri-tab'):
        with gr.Column():
            with gr.Row():
                shared.gradio['ceviri-textbox'] = gr.Textbox(value='', label='Cümle', lines=3)
                shared.gradio['ceviri-dropdown'] = gr.Dropdown(choices=["tr_en", "en_tr"], label='Model Seçimi')
                shared.gradio['ceviri-button'] = gr.Button('Çevir')
        with gr.Column():
            shared.gradio['ceviri_sonucu'] = gr.Textbox(lines=3, label='Çeviri Sonucu')

def Translate(sentence_en, model):
    if not sentence_en:
        return ""  # Boş giriş için boş bir çıktı döndürün
    tokenized_sent = tokenizer.tokenize(sentence_en)
    if detect(sentence_en)=='en' and model=="tr_en":
        return sentence_en
    elif detect(sentence_en)=='tr' and model=="en_tr":
        return sentence_en
    if model == "en_tr" :
        model = en_tr
    else:
        model = tr_en
    hypothesis = beam_search(model, [tokenized_sent], beam_size=1, max_decoding_time_step=70)[0]
    # Tüm olası çevirileri birleştirip döndürün
    for idx, hyp in enumerate(hypothesis):
        return ' '.join(hyp.value)
translated_text=""
# Olay işleyicileri oluşturma işlevi
def create_event_handlers():
    def translate_and_update_output(result):
        # Çeviriyi output_textbox'a yazdır
        shared.gradio['ceviri_sonucu'].value=result
    inputs = ('ceviri-textbox', 'ceviri-dropdown')  # inputs ve outputs burada tanımlanıyor
    outputs = ('ceviri_sonucu')
    
    shared.gradio['ceviri-button'].click(
        lambda x: x, gradio('ceviri-textbox')).then(
        Translate, gradio(inputs), gradio(outputs)).then(
        translate_and_update_output, gradio(outputs)).then(
        ui.gather_interface_values, gradio(shared.input_elements), gradio('interface_state')).then(
        lambda: None, None, None, _js=f'() => {{{ui.audio_notification_js}}}')

