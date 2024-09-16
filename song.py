def generate_song(team_name, team_color, city):
    lyrics = f"""
    
Biz {team_name}, güçlü ve cesuruz,
Zaferde ve mağlubiyette, hikayemiz anlatılır.
{team_color} gururuyla, dimdik ayakta,
Birlikte fethederiz, asla düşmeyiz.

Stadyum ışıkları altında, {team_color} formalarında birleşiyoruz,
Lehçe rehberliğinde, yüksek sesle yankılanan çığlıklar.
Her kalabalıkta, zafer şanımız,
Zafer nakarımız, her kalabalıkta.

Biz {team_name}, güçlü ve cesuruz,
Zaferde ve mağlubiyette, hikayemiz anlatılır.
{team_color} gururuyla, dimdik ayakta,
Birlikte fethederiz, asla düşmeyiz.
İşte {team_name} için, sonsuza dek,
Kalplerimiz bir atar, kalabalık çığlık atar.
Birlikte ve gururla, her zaman olacağız,
{team_name} sonsuza kadar, sonsuz özgürlükle.
    """
    return lyrics    

def main():
    team_name = input("Futbol takiminizin ismini giriniz: ")
    team_color = input("Takiminizin rengini giriniz: ")
    city = input("Takiminizin sehrini yaziniz: ")
    
    song_lyrics = generate_song(team_name, team_color, city)
    print("\nOlusturtulan yeni sarki sozleri: ")
    print(song_lyrics)    

if __name__ == "__main__":
    main()