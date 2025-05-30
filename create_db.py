from app import db, app, Post


with app.app_context():
    db.create_all()

    post1 = Post(
        title="Szukamy noclegu w Chorwacji",
        content="Cześć! Tu Marta i Dawid 😊 Podróżujemy budżetowo po Europie i w czerwcu planujemy odwiedzić Chorwację 🇭🇷 Szukamy niedrogiego noclegu – może być mały pokój, miejsce na namiot, a nawet kanapa u kogoś gościnnego. Może ktoś z Was ma coś do polecenia lub chciałby nas przygarnąć na noc czy dwie? 🙏 Mamy 28 i 30 lat, jesteśmy spokojni, pozytywnie nastawieni, lubimy poznawać nowych ludzi i nie potrzebujemy luksusów – wystarczy dach nad głową i dobra energia! 😄",
        location="Chorwacja",
        image="https://source.unsplash.com/800x400/?rome",
        image2="https://source.unsplash.com/800x400/?beach",
        likes=55
    )

    post2 = Post(
        title="Norwegia – fiordy",
        content="Natura i spokój.",
        location="Flåm, Norwegia",
        image="https://source.unsplash.com/800x400/?norway",
        likes=15
    )

    db.session.add(post1)
    db.session.add(post2)
    db.session.commit()

    print("✔️ Baza danych utworzona i wypełniona.")
