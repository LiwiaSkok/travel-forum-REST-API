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

**📷 Strona główna z menu krajów**
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

**📷 Wybieranie nowego zdjęcia**
<p align="center">
  <img src="screenshots/edit-post3.png" alt="Zamiana zdjęcia">
</p>

**📷 Widok po edycji posta**
<p align="center">
  <img src="screenshots/edit-post2.png" alt="Podgląd po edycji">
</p>

**📷 Opcje edytowania i usuwania posta**
<p align="center">
  <img src="screenshots/edit-post4.png" alt="Menu edytuj/usuń">
</p>


### 🗑️ Usuwanie zdjęcia

<p align="center">
  <img src="screenshots/delete-photo.png" alt="Usuwanie zdjęcia 1">
  <img src="screenshots/delete-photo2.png" alt="Usuwanie zdjęcia 2">
</p>

### 💬 Komentarze

<p align="center">
  <img src="screenshots/add-comment.png" alt="Komentarz 1">
  <img src="screenshots/add-comment2.png" alt="Komentarz 2">
  <img src="screenshots/add-comment3.png" alt="Komentarz 3">
  <img src="screenshots/add-comment4.png" alt="Komentarz 4">
  <img src="screenshots/delete-comment.png" alt="Usuwanie komentarza">
</p>

### 🌐 Filtrowanie według kraju

<p align="center">
  <img src="screenshots/tag.png" alt="Tag kraju 1">
  <img src="screenshots/list.png" alt="Lista krajów">
  <img src="screenshots/tag3.png" alt="Tag kraju 2">
</p>



