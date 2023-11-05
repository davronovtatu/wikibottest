"""
Python tashqi kutubxonalari haqida
pypi.org

wikipedia,googletranslate,requests

"""


# import requests
# import wikipedia
#
#
#pip install wikipedia

# while True:
#     text=input("Matn kiriting dasturni to'xtatish uchun (exit):")
#     if text.lower()=='exit':
#         break
#     else:
#         wikipedia.set_lang('uz')
#         data=wikipedia.summary(text,sentences=3)
#         print(data)
# print("Dastur to'xtatildi !!!")


#pip install googletrans==4.0.0-rc1
# from googletrans import Translator
# translator = Translator()
#
#
# while True:
#     text=f" soz yuboring dasturni to'xtatish uchun (exit) :"
#     data=input(text)
#     if data.lower()=='exit':
#         break
#     else:
#         txt=translator.translate(data,dest='en')
#         print(txt.text)
# print("Dastur to'xtadi")



"""requests moduli"""
# import requests
#
# # Veb-saytdan ma'lumot olish uchun HTTP GET so'rovini yuborish
# response = requests.get('https://api.github.com/events')
#
# # So'rov natijasini tekshirish
# if response.status_code == 200:
#     # Ma'lumotlarni JSON formatida olish
#     events = response.json()
#     # Birinchi elementni konsolga chiqarish
#     print(events[0])
# else:
#     print(f'Xatolik yuz berdi: {response.status_code}')


"""API haqida ma'lumot """
#https://cbu.uz/uz/arkhiv-kursov-valyut/json/
# Valyutalar kursi ma'lumotlari lug'at ko'rinishida
# valyuta_kurslari = [
#     {"Ccy": "USD", "Rate": "12240.01", "Diff": "-8.99", "Date": "03.11.2023"},
#     {"Ccy": "EUR", "Rate": "13003.79", "Diff": "82.32", "Date": "03.11.2023"},
#     # Qolgan valyutalar ma'lumotlari...
# ]
#
# # Har bir valyuta kursi uchun konsolga chiroyli chiqarish
# for valyuta in valyuta_kurslari:
#     print(f"{valyuta['Ccy']} kursi: {valyuta['Rate']} so'm. "
#           f"O'zgarish: {valyuta['Diff']} so'm. "
#           f"Sana: {valyuta['Date']}")
#
# # Konsolga chiqariladigan ma'lumotlarni chiroyli formatlash uchun f-string formatidan foydalanilgan.
