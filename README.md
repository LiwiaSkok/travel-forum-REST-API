# 🌍 Razem Przez Świat – Travel Forum

> **Aplikacja webowa** do dzielenia się wspomnieniami z podróży.  
> Umożliwia tworzenie i przeglądanie postów z komentarzami, lajkami i filtrowaniem po kraju.  
> Udostępnia również pełne **REST API** w formacie **JSON**.

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

> Przykładowe zrzuty ekranu z aplikacji:

### 🏠 Strona główna – lista postów + menu krajów
![](screenshots/home-page3.png)

### ➕ Dodawanie posta
![](screenshots/add-post.png)  
![](screenshots/add-post2.png)  
![](screenshots/add-post3.png)

### ✏️ Edycja posta
![](screenshots/edit-post.png)  
![](screenshots/edit-post3.png)  
![](screenshots/edit-post2.png)  
![](screenshots/edit-post4.png)

### 🗑️ Usuwanie zdjęcia
![](screenshots/delete-photo.png)  
![](screenshots/delete-photo2.png)

### 💬 Komentarze
![](screenshots/add-comment.png)  
![](screenshots/add-comment2.png)  
![](screenshots/add-comment3.png)  
![](screenshots/add-comment4.png)  
![](screenshots/delete-comment.png)

### 🌐 Filtrowanie według kraju
![](screenshots/tag.png)  
![](screenshots/list.png)   
![](screenshots/tag3.png)


