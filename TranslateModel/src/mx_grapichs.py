import matplotlib.pyplot as plt
import re

# Dosya adını belirtin
file_name = 'model/mx-1.0.6/cikti4.txt'

# Dosyayı okuyun
with open(file_name, 'r',encoding="utf-8") as file:
    content = file.read()

# Loss ve Valid_Ppl değerlerini tutmak için boş listeler oluşturun
loss_values = []
valid_ppl_values = []

# Çıktıyı satır satır ayırın
lines = content.strip().split('\n')

# Her satırı inceleyerek loss ve valid_ppl değerlerini ayıklayın
for line in lines:
    loss_match = re.search(r'Loss: (\d+\.\d+)', line)
    valid_ppl_match = re.search(r'Valid_Ppl: (-?\d+\.\d+)', line)
    if loss_match and valid_ppl_match:
        loss_values.append(float(loss_match.group(1)))
        valid_ppl_values.append(float(valid_ppl_match.group(1)))

# Grafik çizimi için epoch sayılarını oluşturun
epochs = list(range(1, len(loss_values) + 1))

# Loss ve Valid_Ppl değerlerini içeren grafikleri çizin
plt.figure(figsize=(10, 6))
plt.plot(epochs, loss_values, label='Loss')
plt.plot(epochs, valid_ppl_values, label='Valid_Ppl')
plt.xlabel('Epoch')
plt.ylabel('Value')
plt.title('Loss and Valid_Ppl Over Epochs')
plt.legend()
plt.grid(True)
plt.savefig('loss_valid_ppl_graph4.png')  # Grafik dosyasının adını istediğiniz gibi belirleyebilirsiniz
plt.show()
