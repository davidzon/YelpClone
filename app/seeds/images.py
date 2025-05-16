from app.models import db, Image

def seed_images():
    images = [
        Image(experience_id=1, user_id=1, url="https://images.unsplash.com/photo-1597600153404-54f3ecdecd37", caption="Eagle Rock views"),
        Image(experience_id=2, user_id=2, url="https://images.unsplash.com/photo-1514511544904-217c34d9c570", caption="Market variety"),
        Image(experience_id=3, user_id=3, url="https://images.unsplash.com/photo-1470770903676-69b98201ea1c", caption="Kayaking at sunset"),
        Image(experience_id=4, user_id=1, url="https://images.unsplash.com/photo-1533419026887-ec45d7c9f59b", caption="LA street art"),
        Image(experience_id=5, user_id=2, url="https://images.unsplash.com/photo-1553189190-9bc72d29b93b", caption="Comedy show venue"),
        Image(experience_id=6, user_id=3, url="https://images.unsplash.com/photo-1552332386-f8dd00dc4d95", caption="Taco trucks lined up"),
        Image(experience_id=7, user_id=1, url="https://images.unsplash.com/photo-1526304640581-d334cdbbf45e", caption="Starry night sky"),
        Image(experience_id=8, user_id=2, url="https://images.unsplash.com/photo-1509228627150-72c4fd0a3793", caption="Golden Gate sunrise"),
        Image(experience_id=9, user_id=3, url="https://images.unsplash.com/photo-1506084868230-bb9d95c24759", caption="Wynwood murals"),
        Image(experience_id=10, user_id=2, url="https://images.unsplash.com/photo-1482178099739-2d1a70b30b99", caption="Oregon lighthouse")
    ]
    db.session.add_all(images)
    db.session.commit()

def undo_images():
    db.session.execute("DELETE FROM images")
    db.session.commit()
