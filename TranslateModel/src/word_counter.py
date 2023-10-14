import matplotlib.pyplot as plt
from collections import Counter
import string

def read_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    return sentences

def calculate_word_counts(sentences):
    word_counts = [len(sentence.split()) for sentence in sentences]
    return word_counts

def plot_histogram(data, title):
    plt.hist(data, bins=20, edgecolor='black')
    plt.xlabel('Kelime Sayısı')
    plt.ylabel('Cümle Sayısı')
    plt.title(title)
    plt.grid(True)
    plt.show()

# Dosya yolları
data_files = {
    'train': {
        'en': 'train_tokenized.en',
        'tr': 'train_tokenized.tr'
    },
    'valid': {
        'en': 'valid_tokenized.en',
        'tr': 'valid_tokenized.tr'
    },
    'test': {
        'en': 'test_tokenized.en',
        'tr': 'test_tokenized.tr'
    }
}

for split, languages in data_files.items():
    for lang, file_path in languages.items():
        sentences = read_sentences(file_path)
        word_counts = calculate_word_counts(sentences)
        title = f'{split.capitalize()} Set - {lang.upper()} - Kelime Sayısı Dağılımı'
        plot_histogram(word_counts, title)
# Tüm diller için kelime sayılarını depolamak için bir sözlük oluşturun

data_file = 'cleaned_tr.txt'

# Tüm cümleleri birleştirin
with open(data_file, 'r', encoding='utf-8') as file:
    all_sentences = ' '.join(file.readlines())

# Noktalama işaretlerini kaldırın
all_sentences = all_sentences.translate(str.maketrans('', '', string.punctuation))

# Boşluklara göre kelimeleri ayırın
words = all_sentences.split()

# Kelime sıklıklarını sayın
word_counts = Counter(words)

# En sık geçen kelimeleri alın
most_common_words = word_counts.most_common()

# Sonuçları bir metin dosyasına yazın
output_file = 'most_common_words_tr.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write('[Kelime]  [Kaç Defa Geçtiği]\n')
    for word, count in most_common_words:
        file.write(f'{word}  {count}\n')    