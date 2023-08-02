# Problem Seti 2, adamAsmaca.py
# İsim:
# Ortak çalışanlar:
# Harcanan zaman:

# Adam Asmaca Oyunu
#------------------------------------
# Yardımcı kod
# Bu yardımcı kodu anlamanıza gerek yok,
# ama fonksiyonları nasıl kullanacağını bilmeniz gerekecek
# (dökümanları okuduğunuzdan emin olun!)
import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    """
    Geçerli kelimelerin bir listesini döndürür.
    Kelimeler küçük harf dizileridir.
    
     Kelime listesinin boyutuna bağlı olarak,
     bu fonksiyonun tamamlanması biraz zaman alabilir.
    """
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime döndürür
    """
    return random.choice(wordlist)

# yardımcı kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden erişilebilmesi için
# kelime listesini değişken kelime listesine yükleyin
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime;
    tüm harflerin küçük olduğunu varsayar
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi);
     tüm harflerin küçük olduğunu varsayar
     returns: boolean, secret_word'ün tüm harfleri letter_guessed içindeyse True;
     Aksi takdirde yanlış
    '''
    sonuc=True
    for i in secret_word:
        if i not in letters_guessed:
           sonuc=False
           break
    return sonuc
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, kullanıcının tahmin ettiği kelime
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: harflerden, alt çizgilerden (_) ve şu ana kadar secret_word
     içindeki hangi harflerin tahmin edildiğini gösteren boşluklardan oluşan dize.
    '''
    sonuc=''
    for a in secret_word:
        if a not in letters_guessed:
            sonuc+='_'
        else:
            sonuc+=a
    return sonuc

# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN




def get_available_letters(letters_guessed):
    '''
    letter_guessed: şimdiye kadar hangi harflerin tahmin edildiği (harflerin listesi)
    returns: dize (harfler), hangi harflerin henüz tahmin edilmediğini temsil eden harflerden oluşur.
    '''
    sonuc=string.ascii_lowercase
    for i in letters_guessed:
                l=sonuc.find(i)
                sonuc=sonuc[:l]+sonuc[l+1:]		
    return sonuc
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN

    

def adamAsmaca(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyununu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini
        ve kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır

     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve
        kullanıcının henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir mektup yazdığından emin olmayı unutmayın!
    
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    sWord=secret_word.lower()
    print("Adam Asmaca oyununa hoş geldiniz!")
    print(str(len(sWord)) + " harf uzunluğunda bir kelime düşünüyorum.")
    letters_guessed=[]
    mistakes_made=0
    available_letters=get_available_letters(letters_guessed)    
    print('-'*13)
    print(str(6 - mistakes_made) + " tahmininiz kaldı")
    print("Kullanılabilir Harfler: "+available_letters)
    guessed_so_far=''
    warning_count=4
    while mistakes_made < 6:
       my_guess1 = input("Lütfen bir harf tahmin edin: ")
       my_guess=my_guess1.lower()
       
       if my_guess in secret_word:
          if my_guess in letters_guessed:
              warning_count -= 1
              if warning_count == 0:
                mistakes_made += 1
                warning_count = 4
                print("Hata! Bu harfi zaten tahmin ettin. Hiçbir uyarınız kalmadığından bir tahmininizi kaybedersiniz:"+ guessed_so_far)
              else:
                print("Hata! Bu harfi zaten tahmin ettin. " + str(warning_count-1) + " uyarınız kaldı: " + guessed_so_far)
          else:
              letters_guessed.append(my_guess)
              guessed_so_far=get_guessed_word(sWord, letters_guessed)
              print("İyi tahmin: "+ guessed_so_far)
       else:
          if my_guess in letters_guessed:
              warning_count -= 1
              if warning_count == 0:
                mistakes_made += 1
                warning_count = 4
                print("Hata! Bu harfi zaten tahmin ettin. Hiçbir uyarınız kalmadığından bir tahmininizi kaybedersiniz:"+ guessed_so_far)
              else:
                print("Hata! Bu harfi zaten tahmin ettin. " + str(warning_count-1) + " uyarınız kaldı: " + guessed_so_far)
          else:
              mistakes_made += 1
              letters_guessed.append(my_guess)
              guessed_so_far=get_guessed_word(sWord, letters_guessed)
              print("Hata! O harf bu kelimede yok: "+ guessed_so_far)

       if guessed_so_far.count('_') == 0:
          break
           
       print('-'*13)
       if mistakes_made < 6:
          print(""+str(6-mistakes_made)+" tahmininiz kaldı")
          available_letters=get_available_letters(letters_guessed)    
          print("Kullanılabilir Harfler: "+available_letters)
       
    if guessed_so_far.count('_') == 0:
        print("Tebrikler kazandın!")
    else:
        print("Üzgünüm, tahminleriniz tükendi. Kelime başkaydı.")



# Adam asmaca işlevinizi tamamladığınızda, dosyanın
#en altına gidin ve test edilecek ilk iki satırın yorumunu kaldırın
# (ipucu: kendi testinizi yaparken kendi secret_word'ünüzü
# seçmek isteyebilirsiniz)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    other_word: string, normal İngilizce kelime
    returns: boolean, True, eğer my_word'ün tüm gerçek harfleri other_word'ün karşılık gelen harfleriyle eşleşiyorsa veya harf özel sembol _ ise ve my_word ile other_word aynı uzunluktaysa; Aksi takdirde False:
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    my_word = my_word.replace(' ', '')

    if len(my_word) == len(other_word):
        hidden_letters = []
        for i,c in enumerate(my_word):
            if c == other_word[i]:
                continue
            elif c == '_':
                hidden_letters.append(other_word[i])
            else:
                return False
        for hidden_letter in hidden_letters:
            if hidden_letter in my_word:
                return False
            
        return True
    else:
        return False
    pass



def show_possible_matches(my_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geçerli tahmini
    returns: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen
        her kelimeyi yazdırmalıdır.
    adamAsmaca ile bir harf tahmin edildiğinde, o harfin gizli kelimede
        geçtiği tüm pozisyonların ortaya çıktığını unutmayın.
    Bu nedenle, gizli harf(_ ) zaten ortaya çıkmış olan kelimedeki
     harflerden biri olamaz.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    pass



def adamAsmaca_ipuclu(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     Etkileşimli bir Adam Asmaca oyunu başlatır.
    
     * Oyunun başında, kullanıcıya secret_word'ün kaç harf içerdiğini ve
        kaç tahminle başladığını bildirin.
      
     * Kullanıcı 6 tahminle başlamalıdır
    
     * Her turdan önce kullanıcıya kaç tahmin kaldığını ve kullanıcının
        henüz tahmin etmediği harfleri göstermelisiniz.
    
     * Kullanıcıdan tur başına bir tahmin vermesini isteyin.
        Kullanıcının bir harf tahmin ettiğini kontrol ettiğinizden emin olun.
      
     * Kullanıcı, her tahminden hemen sonra tahminlerinin bilgisayarın
        kelimesinde görünüp görünmediği hakkında geri bildirim almalıdır.

     * Her tahminden sonra, o ana kadar kısmen tahmin edilen kelimeyi
         kullanıcıya göstermelisiniz.
      
     * Tahmin sembolü * ise, kelime listesindeki mevcut tahmin edilen
        kelimeyle eşleşen tüm kelimeleri yazdırın.
    
     Problem yazımında detaylandırılan diğer sınırlamaları takip eder.
    '''
# BURAYA KODUNUZU GİRİN VE "pass"ı SİLİN
    pass



# adamAsmaca_ipuclu işlevinizi tamamladığınızda, yukarıdaki adam asmaca
# fonksiyonunu çalıştırmak için kullanılan benzer iki satırı yorumlayın ve
# ardından bu iki satırın yorumunu kaldırın ve test etmek için bu dosyayı çalıştırın!
# İpucu: Test ederken kendi secret_word'ünüzü seçmek isteyebilirsiniz.


if __name__ == "__main__":
    # pass

    # 2. bölümü test etmek için yukarıdaki pass satırında # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin
    
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)

###############
    
# 3. bölümü test etmek için yukarıdaki satırlarlarda yeniden # işaretini kullanın ve aşağıdaki iki satırda # işaretini silin

    #secret_word = choose_word(wordlist)
    #adamAsmaca_ipuclu(secret_word)
