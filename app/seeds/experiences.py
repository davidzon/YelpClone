from app.models import db, Experience
from datetime import datetime

def seed_experiences():
    experiences = [
        Experience(creator_id=1, title="Hike to Eagle Rock", description="A moderately challenging hike with stunning views", location="Topanga, CA", category="Hiking", price=0.0),
        Experience(creator_id=1, title="Sunset Kayaking", description="Paddle through a serene river while watching the sunset", location="Bend, OR", category="Adventure", price=45.0),
        Experience(creator_id=1, title="Underground Comedy Night", description="Stand-up comedy from up-and-coming performers", location="Chicago, IL", category="Entertainment", price=12.0),
        Experience(creator_id=1, title="Rock Climbing at Joshua Tree", description="Test your skills on desert boulders and cliffs", location="Joshua Tree, CA", category="Adventure", price=20.0),
        Experience(creator_id=1, title="Overnight Camping in Yosemite", description="Spend a night under the stars in California's famous national park", location="Yosemite, CA", category="Nature", price=30.0),
        Experience(creator_id=1, title="Mountain Biking Moab", description="Ride legendary trails with stunning desert backdrops", location="Moab, UT", category="Adventure", price=25.0),
        Experience(creator_id=1, title="Surfing in Santa Cruz", description="Catch waves with locals on California's coast", location="Santa Cruz, CA", category="Water Sports", price=35.0),
        Experience(creator_id=1, title="Live Rock Concert", description="Enjoy music at a legendary open-air amphitheater", location="Red Rocks, CO", category="Entertainment", price=50.0),
        Experience(creator_id=1, title="Skydiving San Diego", description="Take the leap and enjoy scenic views of the coast", location="San Diego, CA", category="Extreme", price=150.0),
        Experience(creator_id=1, title="Scuba Diving in Key Largo", description="Explore vibrant coral reefs in crystal-clear waters", location="Key Largo, FL", category="Water Sports", price=100.0),

        Experience(creator_id=2, title="Napa Valley Wine Tasting", description="Sip world-renowned wines in the California countryside", location="Napa Valley, CA", category="Food & Drink", price=60.0),
        Experience(creator_id=2, title="Interactive Cooking Class", description="Learn to prepare gourmet dishes from a professional chef", location="New York, NY", category="Food & Drink", price=55.0),
        Experience(creator_id=2, title="Old Town History Walk", description="Learn about the city's history with a walking tour", location="Boston, MA", category="History", price=15.0),
        Experience(creator_id=2, title="Smithsonian Museum Tour", description="Explore the wonders of science and culture", location="Washington, DC", category="Education", price=0.0),
        Experience(creator_id=2, title="Paint and Sip Night", description="Unleash your inner artist while enjoying wine", location="Brooklyn, NY", category="Art", price=35.0),
        Experience(creator_id=2, title="Morning Yoga Retreat", description="Stretch and relax with sunrise yoga in nature", location="Sedona, AZ", category="Wellness", price=20.0),
        Experience(creator_id=2, title="Karaoke Night", description="Show off your voice with friends at a lively bar", location="Las Vegas, NV", category="Entertainment", price=10.0),
        Experience(creator_id=2, title="Ski Day at Tahoe", description="Shred powder and enjoy alpine views", location="Lake Tahoe, CA", category="Adventure", price=80.0)
    ]

    db.session.add_all(experiences)
    db.session.commit()

def undo_experiences():
    db.session.execute("DELETE FROM experiences")
    db.session.commit()
