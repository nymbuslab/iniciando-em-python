import datetime

agora = datetime.datetime.now()

print(f"Hoje é {agora.day:02d}/{agora.month:02d}/{agora.year}")
print(f"Agora sào {agora.hour:02d}:{agora.minute:02d}")
if agora.hour <= 11:
  print("Bom dia")
elif agora.hour <= 17:
  print("Boa Tarde")
else:
  print("Boa noite!")

