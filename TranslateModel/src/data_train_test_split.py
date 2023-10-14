import random

# Dosyaları oku
with open('data/cleaned_tr.txt', 'r', encoding='utf-8') as turkish_file:
    turkish_lines = turkish_file.readlines()

with open('data/cleaned_eng.txt', 'r', encoding='utf-8') as english_file:
    english_lines = english_file.readlines()

# Verileri karıştır
combined_data = list(zip(turkish_lines, english_lines))

random.shuffle(combined_data)

turkish_lines, english_lines = zip(*combined_data)
# Veriyi bölelim
train_ratio = 0.7
valid_ratio = 0.2
test_ratio = 0.1

train_index = int(len(turkish_lines) * train_ratio)
print(train_index)
valid_index = train_index + int(len(turkish_lines) * valid_ratio)
print(valid_index)

train_turkish = turkish_lines[:train_index]
train_english = english_lines[:train_index]
valid_turkish = turkish_lines[train_index:valid_index]
valid_english = english_lines[train_index:valid_index]
test_turkish = turkish_lines[valid_index:]
test_english = english_lines[valid_index:]

def write_to_file(lines, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)

write_to_file(train_turkish, 'train.tr')
write_to_file(train_english, 'train.en')
write_to_file(valid_turkish, 'valid.tr')
write_to_file(valid_english, 'valid.en')
write_to_file(test_turkish, 'test.tr')
write_to_file(test_english, 'test.en')
