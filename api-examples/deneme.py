import asyncio
import html
import json
import sys
import websockets

# Websockets kütüphanesini içe aktarın.
try:
    import websockets
except ImportError:
    print("Websockets package not found. Make sure it's installed.")

# For local streaming, the websockets are hosted without ssl - ws://
HOST = 'localhost'
PORT = 5005
URI = f'ws://{HOST}:{PORT}/api/v1/stream'  # URI'yi güncelledik.

# For reverse-proxied streaming, the remote will likely host with ssl - wss://
# URI = 'wss://your-uri-here.trycloudflare.com/api/v1/stream'

async def run(user_input, history):
    request = {
        'prompt': user_input,
        'max_new_tokens': 250,
        'auto_max_new_tokens': False,
        'max_tokens_second': 0,
        'history': history,
        'mode': 'instruct',  # Valid options: 'chat', 'chat-instruct', 'instruct'
        'character': 'ChaTR',
        'instruction_template': 'Vicuna-v1.1',
        'your_name': 'You',
        'regenerate': False,
        '_continue': False,
        'chat_instruct_command': 'Continue the chat dialogue below. Write a single reply for the character "".\n\n',

        # Generation params
        'preset': 'None',
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.1,
        'typical_p': 1,
        'epsilon_cutoff': 0,
        'eta_cutoff': 0,
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': 1.18,
        'repetition_penalty_range': 0,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,
        'guidance_scale': 1,
        'negative_prompt': '',

        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': []
    }

    text_pieces = []  # Metin parçalarını saklamak için bir liste oluşturduk.

    async with websockets.connect(URI, ping_interval=None) as websocket:
        await websocket.send(json.dumps(request))

        while True:
            incoming_data = await websocket.recv()
            incoming_data = json.loads(incoming_data)

            if incoming_data['event'] == 'text_stream':
                text_pieces.append(html.unescape(incoming_data['text']))

            elif incoming_data['event'] == 'stream_end':
                # Metin parçalarını birleştirip temizleyin ve ekrana yazdırın.
                combined_text = ' '.join(text_pieces)
                cleaned_text = ' '.join(combined_text.split())  # Boşlukları temizleme
                print(cleaned_text)
                yield cleaned_text
                return

async def print_response_stream(user_input, history):
    async for _ in run(user_input, history):
        pass

if __name__ == '__main__':
    user_input = "Ankara nerededir"
    history = []  # Boş bir geçmişle başlayın.

    asyncio.run(print_response_stream(user_input, history))