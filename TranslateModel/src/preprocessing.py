import re

def delete_empty_lines(train_en, train_tr):
  """Deletes empty lines from the train.en and train.tr datasets."""

  with open(train_en, "r",encoding="utf-8") as f_en, open(train_tr, "r",encoding="utf-8") as f_tr:
    en_lines = f_en.readlines()
    tr_lines = f_tr.readlines()

  for i in range(len(en_lines)):
    if en_lines[i] == "\n" or tr_lines[i] == "\n":
      en_lines[i] = ""
      tr_lines[i] = ""

  with open(train_en, "w",encoding="utf-8") as f_en, open(train_tr, "w",encoding="utf-8") as f_tr:
    for line in en_lines:
      f_en.write(line)
    for line in tr_lines:
      f_tr.write(line)

def delete_long_sentences(train_en, train_tr, max_words=20):
  """Deletes sentences longer than max_words words from the train.en and train.tr datasets."""

  with open(train_en, "r",encoding="utf-8") as f_en, open(train_tr, "r",encoding="utf-8") as f_tr:
    en_lines = f_en.readlines()
    tr_lines = f_tr.readlines()

  for i in range(len(en_lines)):
    en_words = en_lines[i].split()
    tr_words = tr_lines[i].split()

    if len(en_words) > max_words or len(tr_words) > max_words:
      en_lines[i] = ""
      tr_lines[i] = ""

  with open(train_en, "w",encoding="utf-8") as f_en, open(train_tr, "w",encoding="utf-8") as f_tr:
    for line in en_lines:
      f_en.write(line)
    for line in tr_lines:
      f_tr.write(line)

def main():
  """Deletes empty lines and sentences longer than 20 words from the train.en and train.tr datasets."""

  train_en = "cleaned_eng.txt"
  train_tr = "cleaned_tr.txt"

  delete_long_sentences(train_en, train_tr, max_words=20)
  delete_empty_lines(train_en, train_tr)
  

if __name__ == "__main__":
  main()