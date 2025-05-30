# 🌍 Razem Przez Świat – Travel Forum

## 🌐 Opis aplikacji

**Razem Przez Świat** to aplikacja webowa służąca do dzielenia się wspomnieniami z podróży.

Pozwala użytkownikom:
- tworzyć i przeglądać posty z relacjami z różnych krajów,
- dodawać komentarze i lajki,
- filtrować posty według kraju.

Dodatkowo udostępnia **pełne REST API** do zarządzania postami w formacie **JSON**.

![logo](screenshots/logo1.png)

---

## 🚀 Demo

Zobacz aplikację w akcji:  
👉 **[https://travel-forum-rest-api-2.onrender.com/](https://travel-forum-rest-api-2.onrender.com/)**

---

## 📋 Spis treści

1. [🔥 Funkcjonalności](#-funkcjonalności)  
2. [🛠 Technologie](#-technologie)  
3. [🖼️ Ekrany aplikacji](#-ekrany-aplikacji)

---

## 🔥 Funkcjonalności

### 📝 Posty (CRUD)
- Dodawanie posta z:
  - tytułem
  - treścią
  - lokalizacją
  - wyborem kraju
  - 1–2 zdjęciami
- Edycja i usuwanie postów
- Możliwość usunięcia pojedynczego zdjęcia przy edycji

### 💬 Komentarze
- Dodawanie komentarzy pod postami
- Edycja i usuwanie komentarzy

### ❤️ Lajki
- Przycisk „❤️ Lubię to”
- Licznik lajków

### 🌍 Filtrowanie po kraju
- Rozwijane menu „Relacje z podróży” z ikonami flag
- Po kliknięciu – wyświetlanie postów z danego kraju

### 🔄 REST API (format JSON)
- wszystkie posty GET `/api/posts`  
  - pojedynczy post GET `/api/posts/<id>`  
  - tworzenie POST `/api/posts`  
  - aktualizacja PUT `/api/posts/<id>`  
  - usuwanie DELETE `/api/posts/<id>` 

---

## 🛠 Technologie

> **Backend:**  
> Python 3.9+  
> Flask  
> Flask-SQLAlchemy  
> Flask-Migrate (Alembic)  
> Flask-WTF  

> **Frontend:**  
> HTML5  
> CSS3  
> Bootstrap 5  

> **Baza danych:**  
> SQLite

---

## 🖼️ Ekrany aplikacji

### 🏠 Strona główna – lista postów

> Widok główny aplikacji z listą postów oraz możliwością filtrowania według kraju.

**📷 Strona główna**
<p align="center">
  <img src="screenshots/home-page3.png" alt="Strona główna">
</p>

---

### ➕ Dodawanie posta

> Formularz umożliwiający dodanie nowego wpisu z danymi i zdjęciami.

**📷 Pusty formularz dodawania posta**
<p align="center">
  <img src="screenshots/add-post.png" alt="Formularz dodawania nowego posta – pusty">
</p>

**📷 Wypełnianie formularza posta**
<p align="center">
  <img src="screenshots/add-post2.png" alt="Uzupełnianie danych posta">
</p>

**📷 Podgląd dodanego posta**
<p align="center">
  <img src="screenshots/add-post3.png" alt="Podgląd posta">
</p>

---

### ✏️ Edycja posta

> Możliwość zmiany tytułu, treści, lokalizacji, zdjęć oraz kraju.

**📷 Formularz edycji posta**
<p align="center">
  <img src="screenshots/edit-post1.png" alt="Formularz edycji posta">
</p>

**📷 Opcje edytowania i usuwania posta**
<p align="center">
  <img src="screenshots/edit-post2.png" alt="Zamiana zdjęcia">
</p>

**📷 Wybieranie nowego zdjęcia**
<p align="center">
  <img src="screenshots/edit-post3.png" alt="Podgląd po edycji">
</p>

**📷 Widok po edycji posta**
<p align="center">
  <img src="screenshots/edit-post4.png" alt="Menu edytuj/usuń">
</p>


### 🗑️ Usuwanie zdjęcia z posta

> Możesz usunąć zdjęcie lub zdjęcia z posta podczas edycji.

**📷 Obecne zdjęcie i opcja usunięcia**
<p align="center">
  <img src="screenshots/delete-photo.png" alt="Usuń zdjęcie 1">
</p>

**📷 Podgląd posta po usunięciu zdjęcia**
<p align="center">
  <img src="screenshots/delete-photo2.png" alt="Usuń zdjęcie 2">
</p>

---

### ❤️ Lajkowanie i 💬 komentowanie postów

> Użytkownicy mogą zostawiać komentarze i serduszka pod postami.

**📷 Post z komentarzem i 5 lajkami**
<p align="center">
  <img src="screenshots/add-comment.png" alt="Komentarz i lajk">
</p>

**📷 Formularz dodania komentarza oraz mini podgląd posta**
<p align="center">
  <img src="screenshots/add-comment2.png" alt="Lista komentarzy">
</p>

---

### 🗨️ Edycja komentarzy

> Sekcja komentarzy z możliwością dodania nowego wpisu.

**📷 Dodanie komentarzy które chcielibyśmy edytować**
<p align="center">
  <img src="screenshots/add-comment3.png" alt="Dodaj komentarz">
</p>

**📷 Menu opcji komentarza: edytuj lub usuń**
<p align="center">
  <img src="screenshots/add-comment4.png" alt="Komentarze użytkowników">
</p>

---

### ✏️ Edycja komentarza

> Komentarze można również edytować lub usunąć.

**📷 Formularz edycji komentarza**
<p align="center">
  <img src="screenshots/edit-comment.png" alt="Opcje komentarza">
</p>

**📷 Poprawione komentarze po użyciu opcji edytuj**
<p align="center">
  <img src="screenshots/edit-comment2.png" alt="Edytowanie komentarza">
</p>

---

### 🗑️ Usuwanie komentarza

> Komentarz można bezpiecznie usunąć jednym kliknięciem.

**📷 Przykład komentarza z danymi osobowymi i opcją usunięcia**
<p align="center">
  <img src="screenshots/delete-comment.png" alt="Usuwanie komentarza">
</p>

### 🌍 Filtrowanie postów po kraju

> Podczas dodawania posta użytkownik wybiera kraj z listy rozwijanej.  
> Wybrany kraj (np. **Włochy**) staje się tagiem przypisanym do posta i umożliwia późniejsze filtrowanie treści według państw.

**📷 Wybranie taga – np. Włochy – w formularzu dodania posta**
<p align="center">
  <img src="screenshots/tag.png" alt="Dropdown filtrujący posty po kraju">
</p>

> Umożliwia wybór konkretnego kraju, który chcesz obejrzeć – np. klikając „Włochy” zobaczysz tylko posty z tego kraju.

**📷 Rozwijane menu „Relacje z podróży” z ikonami flag**
<p align="center">
  <img src="screenshots/list.png" alt="Lista krajów – dropdown">
</p>

**📷 Przykład działania filtra – tylko posty z Włoch**
<p align="center">
  <img src="screenshots/tag3.png" alt="Widok z przefiltrowanymi postami z Włoch">
</p>



