from app.models import db, Experience
from datetime import datetime

def seed_experiences():
    experiences = [
        Experience(creator_id=1, title="Hike to Eagle Rock", description="A moderately challenging hike with stunning views.", location="Topanga, CA", category="Hiking", price=0.0),
        Experience(creator_id=2, title="Brooklyn Food Market", description="Sample food from over 40 local vendors.", location="Brooklyn, NY", category="Food", price=15.00),
        Experience(creator_id=3, title="Sunset Kayaking", description="Paddle through a serene river while watching the sunset.", location="Bend, OR", category="Adventure", price=45.00),
        Experience(creator_id=1, title="LA Art Walk", description="Self-guided tour through the LA arts district.", location="Los Angeles, CA", category="Art", price=0.00),
        Experience(creator_id=2, title="Underground Comedy Night", description="Stand-up comedy from up-and-coming performers.", location="Chicago, IL", category="Entertainment", price=12.00),
        Experience(creator_id=3, title="Taco Truck Tour", description="Follow the best taco trucks in Austin.", location="Austin, TX", category="Food", price=25.00),
        Experience(creator_id=1, title="Stargazing in Joshua Tree", description="View the Milky Way in a dark-sky park.", location="Joshua Tree, CA", category="Nature", price=5.00),
        Experience(creator_id=2, title="Golden Gate Sunrise Run", description="Run across the Golden Gate bridge during sunrise.", location="San Francisco, CA", category="Fitness", price=0.00),
        Experience(creator_id=3, title="Mural Tour of Wynwood", description="Explore Miami’s street art on foot.", location="Miami, FL", category="Art", price=10.00),
        Experience(creator_id=2, title="Oregon Coast Lighthouse Loop", description="Drive to and hike around iconic lighthouses.", location="Florence, OR", category="Scenic Drive", price=0.00),
    ]
    db.session.add_all(experiences)
    db.session.commit()

def undo_experiences():
    db.session.execute("DELETE FROM experiences")
    db.session.commit()
