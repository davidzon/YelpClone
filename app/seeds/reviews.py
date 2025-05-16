from app.models import db, Review

def seed_reviews():
    reviews = [
        Review(user_id=2, experience_id=1, rating=5, review="A peaceful trail with breathtaking views of the sunset."),
        Review(user_id=3, experience_id=1, rating=4, review="Great for a short adventure. Some rocky spots, but enjoyable."),

        Review(user_id=1, experience_id=2, rating=5, review="Tranquil and perfect for beginners. Loved every moment on the water."),
        Review(user_id=3, experience_id=2, rating=4, review="Nice paddling trip. Scenic, but bring bug spray."),

        Review(user_id=1, experience_id=3, rating=4, review="Small venue but intimate and full of laughs."),
        Review(user_id=2, experience_id=3, rating=5, review="Amazing energy! Discovered a new favorite comedian."),

        Review(user_id=2, experience_id=4, rating=5, review="Challenging and rewarding climb with amazing desert views."),
        Review(user_id=3, experience_id=4, rating=4, review="Rough terrain, but a great experience for climbers."),

        Review(user_id=1, experience_id=5, rating=5, review="The night sky was magical. A true camping gem."),
        Review(user_id=2, experience_id=5, rating=4, review="Peaceful site, great facilities, but a bit crowded."),

        Review(user_id=1, experience_id=6, rating=5, review="Epic ride with jaw-dropping views. Will be back."),
        Review(user_id=3, experience_id=6, rating=4, review="Tough trails, but an unforgettable adventure."),

        Review(user_id=2, experience_id=7, rating=5, review="Caught perfect waves. Instructors were very helpful."),
        Review(user_id=3, experience_id=7, rating=4, review="Fun surf spot with good vibes and clean water."),

        Review(user_id=1, experience_id=8, rating=5, review="Sound and lights were phenomenal. Truly iconic venue."),
        Review(user_id=2, experience_id=8, rating=4, review="Loved the music. Parking could be better though."),

        Review(user_id=1, experience_id=9, rating=5, review="Unforgettable rush. The views were incredible mid-jump."),
        Review(user_id=3, experience_id=9, rating=4, review="Heart-pounding thrill! Wish it lasted longer."),

        Review(user_id=2, experience_id=10, rating=5, review="Saw so many fish and the coral was vibrant."),
        Review(user_id=1, experience_id=10, rating=4, review="Clear water and calm currents made it ideal."),

        Review(user_id=2, experience_id=11, rating=5, review="Tasted the best wines of my life. Great hosts."),
        Review(user_id=3, experience_id=11, rating=4, review="Beautiful scenery and great reds."),

        Review(user_id=1, experience_id=12, rating=5, review="Chef was amazing. Learned so much while having fun."),
        Review(user_id=3, experience_id=12, rating=4, review="Interactive and delicious. The risotto was my favorite."),

        Review(user_id=1, experience_id=13, rating=5, review="Great history lessons delivered with personality."),
        Review(user_id=2, experience_id=13, rating=4, review="Enjoyable and informative. Learned a lot about Boston."),

        Review(user_id=3, experience_id=14, rating=5, review="So much to see! Plan for a full day."),
        Review(user_id=1, experience_id=14, rating=4, review="Loved the exhibits. Great for kids and adults alike."),

        Review(user_id=2, experience_id=15, rating=5, review="Such a fun evening! Loved my painting and the wine."),
        Review(user_id=3, experience_id=15, rating=4, review="Laughed a lot and actually created something pretty good."),

        Review(user_id=1, experience_id=16, rating=5, review="Peaceful and rejuvenating. Sunrise was stunning."),
        Review(user_id=2, experience_id=16, rating=4, review="Felt refreshed. Wish the session was a bit longer."),

        Review(user_id=3, experience_id=17, rating=5, review="Fun crowd and great playlist."),
        Review(user_id=1, experience_id=17, rating=4, review="Sang my heart out. Drinks were reasonably priced."),

        Review(user_id=2, experience_id=18, rating=5, review="Perfect snow and fast lifts. Loved every second."),
        Review(user_id=3, experience_id=18, rating=4, review="Great slopes but the lines were long mid-day."),
    ]

    db.session.add_all(reviews)
    db.session.commit()

def undo_reviews():
    db.session.execute("DELETE FROM reviews")
    db.session.commit()
