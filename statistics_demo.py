import numpy as np

# 0-dan 99-a qədər təsadüfi 50 ədəd
massiv = np.random.randint(0, 100, 50)

en_boyuk = np.max(massiv)  # Maksimum dəyər
en_kicik = np.min(massiv)  # Minimum dəyər
orta = np.mean(massiv)     # Orta (average) dəyər
standart_kenarlasma = np.std(massiv)  # Standart kənarlaşma

print(f"Massiv: {massiv}")
print(f"Ən böyük dəyər: {en_boyuk}")
print(f"Ən kiçik dəyər: {en_kicik}")
print(f"Orta dəyər: {orta:.2f}")
print(f"Standart kənarlaşma dəyər: {standart_kenarlasma:.2f}")
