# Aplikacja do Porównywania Plików Wideo

## Opis
Aplikacja służy do porównywania zgodności wideo i audio w dwóch plikach wideo. Umożliwia jednoczesne odtwarzanie dwóch plików wideo, co ułatwia analizę i porównanie ich zawartości.

## Funkcjonalność Początkowa
- **Odtwarzanie Wideo**
  - Dwa okna odtwarzania wideo, wyświetlające jednocześnie dwa pliki wideo.
  - Obsługiwane formaty: MP4, MOV, MXF.
- **Panel Sterowania**
  - Przyciski: Play, Pause, Stop.
- **Regulacja Głośności**
  - Oddzielna regulacja głośności dla każdego okna wideo.
- **Pasek Postępu Odtwarzania**
  - Pasek postępu z możliwością nawigacji po filmie.
- **Licznik Czasu**
  - Wyświetlanie aktualnego czasu odtwarzania w sekundach, z dokładnością do setnych części sekundy (0.01 s).

## Instalacja
1. Sklonuj repozytorium:
   ```sh
   git clone git@github.com:hury77/Equalizer_video.git
   ```
2. Przejdź do katalogu projektu:
   ```sh
   cd Equalizer_video
   ```
3. Zainstaluj zależności:
   ```sh
   pip install -r requirements.txt
   ```

## Uruchomienie
Aby uruchomić aplikację, wykonaj:
```sh
python src/main.py
```