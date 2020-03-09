import face_recognition
import os
import shutil

file_names = []
known_face_encodings = []

inputFilePath = 'TanimliYuzler/'
personDirectory = 'PersonDirectory/'
searchFolder = 'Resimler/'
count = 0
for sf in os.listdir(inputFilePath):
    if(os.path.isfile(os.path.join(inputFilePath,sf))):
        count += 1
if count < 0:
    print("Tanima islemi yapilacak klasorde resim bulunamadi! Lutfen Uygulama klasoru icerisine TanimliYuzler adinda bir klasor oldugunu ve icerisinde ayiklama yapilacak kisilere ait"
          " .jpg uzantili resimlerin bulundugunu kontrol ediniz.")
print("Toplam " , str(count) + " adet resim taranacak")
#klasörden tanımlanacak yüzleri ve dosya isimlerini topluyoruz
for file in os.listdir(inputFilePath):
      filename_w_ext = os.path.basename(file)
      filename,file_ext = os.path.splitext(filename_w_ext)
      file_image= face_recognition.load_image_file(inputFilePath + filename_w_ext)
      folder_face_encoding = face_recognition.face_encodings(file_image)[0]
      known_face_encodings.append(folder_face_encoding)
      file_names.append(filename)
      directory = personDirectory + filename + '/'
      #kişi için klasör yok ise oluştur
      if not os.path.exists(directory):
          os.makedirs(directory)
          print(filename + ' için klasör oluşturuldu...')


n = 0
while count > 0:
    for folder_face_encoding in known_face_encodings:
        ffname = file_names[n]
        n = n + 1
        print(ffname + " için tarama başladı")
        count = count - 1
        for search_file in os.listdir(searchFolder):
            sfnwe = os.path.basename(search_file)
            sfn,sfe = os.path.splitext(sfnwe)
            sfi = face_recognition.load_image_file(searchFolder + sfnwe)
            sfencoding = face_recognition.face_encodings(sfi)
            if sfencoding != []:
                result = face_recognition.compare_faces(folder_face_encoding,sfencoding,0.6)
                if result[0] == True:
                    source = searchFolder + sfnwe
                    dest = personDirectory + ffname + '/' + sfnwe
                    shutil.copy(source,dest)
                    print(ffname , " için resim bulundu ve kendi klasörüne kopyalandı." )

print("Tarama ve ayıklama işlemi sonlandı. Çıkmak için q ya basın!")



