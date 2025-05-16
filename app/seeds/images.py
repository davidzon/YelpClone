from app.models import db, Image

def seed_images():
    images = [
    Image(experience_id=1, user_id=1, url="https://images.pexels.com/photos/450062/pexels-photo-450062.jpeg?cs=srgb&dl=pexels-tirachard-kumtanom-112571-450062.jpg&fm=jpg", caption="Group of hikers silhouetted against a vibrant sunset"),
    Image(experience_id=1, user_id=2, url="https://images.pexels.com/photos/1365425/pexels-photo-1365425.jpeg?cs=srgb&dl=pexels-sanmane-1365425.jpg&fm=jpg", caption="Group of hikers trekking on a rugged mountain trail"),
    Image(experience_id=1, user_id=3, url="https://images.pexels.com/photos/236973/pexels-photo-236973.jpeg?cs=srgb&dl=pexels-pixabay-236973.jpg&fm=jpg", caption="Two women hiking on a scenic mountain trail"),

    Image(experience_id=2, user_id=1, url="https://images.pexels.com/photos/1036864/pexels-photo-1036864.jpeg?cs=srgb&dl=pexels-alexander-bobrov-390088-1036864.jpg&fm=jpg", caption="Three kayakers paddle through pristine turquoise waters"),
    Image(experience_id=2, user_id=2, url="https://images.pexels.com/photos/1761282/pexels-photo-1761282.jpeg?cs=srgb&dl=pexels-jake-pnw-1761282.jpg&fm=jpg", caption="Man kayaking down a waterfall in a lush forest"),
    Image(experience_id=2, user_id=3, url="https://images.pexels.com/photos/1497587/pexels-photo-1497587.jpeg?cs=srgb&dl=pexels-spencergurley-1497587.jpg&fm=jpg", caption="Group kayaking on a picturesque lake surrounded by rocky terrain and pine trees"),

    Image(experience_id=3, user_id=1, url="https://images.pexels.com/photos/10078868/pexels-photo-10078868.jpeg?cs=srgb&dl=pexels-zaid-mohammed-86842527-10078868.jpg&fm=jpg", caption="Man holding a microphone doing stand-up comedy on stage"),
    Image(experience_id=3, user_id=2, url="https://images.pexels.com/photos/1840320/pexels-photo-1840320.jpeg?cs=srgb&dl=pexels-teemu-r-555088-1840320.jpg&fm=jpg", caption="Microphone on stage with red lighting"),
    Image(experience_id=3, user_id=3, url="https://images.pexels.com/photos/713149/pexels-photo-713149.jpeg?cs=srgb&dl=pexels-monica-713149.jpg&fm=jpg", caption="Dimly lit stage with red curtains and audience silhouettes"),

    Image(experience_id=4, user_id=1, url="https://images.pexels.com/photos/3077882/pexels-photo-3077882.jpeg?cs=srgb&dl=pexels-1585669-3077882.jpg&fm=jpg", caption="Silhouette of a rock climber scaling a steep cliff at sunset"),
    Image(experience_id=4, user_id=2, url="https://images.pexels.com/photos/946337/pexels-photo-946337.jpeg?cs=srgb&dl=pexels-rodrigo-342429-946337.jpg&fm=jpg", caption="Man bouldering on a steep rock face"),
    Image(experience_id=4, user_id=3, url="https://images.pexels.com/photos/1263924/pexels-photo-1263924.jpeg?cs=srgb&dl=pexels-char-528970-1263924.jpg&fm=jpg", caption="Two climbers atop a dramatic cliff with a stunning ocean view"),

    Image(experience_id=5, user_id=1, url="https://images.pexels.com/photos/1687845/pexels-photo-1687845.jpeg?cs=srgb&dl=pexels-xue-guangjian-815005-1687845.jpg&fm=jpg", caption="Tents on a grassy mountain ridge at sunrise"),
    Image(experience_id=5, user_id=2, url="https://images.pexels.com/photos/45241/tent-camp-night-star-45241.jpeg?cs=srgb&dl=pexels-pixabay-45241.jpg&fm=jpg", caption="A glowing yellow tent under a star-filled night sky"),
    Image(experience_id=5, user_id=3, url="https://images.pexels.com/photos/1752951/pexels-photo-1752951.jpeg?cs=srgb&dl=pexels-bianca-gasparoto-834990-1752951.jpg&fm=jpg", caption="Roasting marshmallows over a campfire at night"),

    Image(experience_id=6, user_id=1, url="https://images.pexels.com/photos/90454/pexels-photo-90454.jpeg?cs=srgb&dl=pexels-irenelasus-90454.jpg&fm=jpg", caption="Mountain biker kicking up dust on a forest trail"),
    Image(experience_id=6, user_id=2, url="https://images.pexels.com/photos/71104/utah-mountain-biking-bike-biking-71104.jpeg?cs=srgb&dl=pexels-pixabay-71104.jpg&fm=jpg", caption="Cyclist performs a daring jump off a rocky ledge"),
    Image(experience_id=6, user_id=3, url="https://images.pexels.com/photos/2248713/pexels-photo-2248713.jpeg?cs=srgb&dl=pexels-fr3nks-2248713.jpg&fm=jpg", caption="Cyclist with mountain bike silhouetted on a hilltop at sunset"),

    Image(experience_id=7, user_id=1, url="https://images.pexels.com/photos/4944677/pexels-photo-4944677.jpeg?cs=srgb&dl=pexels-n-voitkevich-4944677.jpg&fm=jpg", caption="Female surfer carrying her surfboard into the sea"),
    Image(experience_id=7, user_id=2, url="https://images.pexels.com/photos/4944687/pexels-photo-4944687.jpeg?cs=srgb&dl=pexels-n-voitkevich-4944687.jpg&fm=jpg", caption="Surfer heading into the water with her board"),
    Image(experience_id=7, user_id=3, url="https://images.pexels.com/photos/416676/pexels-photo-416676.jpeg?cs=srgb&dl=pexels-pixabay-416676.jpg&fm=jpg", caption="Surfer riding a massive turquoise wave"),

    Image(experience_id=8, user_id=1, url="https://images.pexels.com/photos/1763075/pexels-photo-1763075.jpeg?cs=srgb&dl=pexels-sebastian-ervi-866902-1763075.jpg&fm=jpg", caption="Rock band performing live with enthusiastic audience and vibrant lights"),
    Image(experience_id=8, user_id=2, url="https://images.pexels.com/photos/976866/pexels-photo-976866.jpeg?cs=srgb&dl=pexels-joshsorenson-976866.jpg&fm=jpg", caption="Energetic crowd at a live concert with hands raised"),
    Image(experience_id=8, user_id=3, url="https://images.pexels.com/photos/995301/pexels-photo-995301.jpeg?cs=srgb&dl=pexels-joshsorenson-995301.jpg&fm=jpg", caption="Close-up of a drummer performing on stage"),

    Image(experience_id=9, user_id=1, url="https://images.pexels.com/photos/70361/california-parachutists-skydivers-flares-70361.jpeg?cs=srgb&dl=pexels-pixabay-70361.jpg&fm=jpg", caption="Skydivers performing aerial stunts with colorful smoke trails"),
    Image(experience_id=9, user_id=2, url="https://images.pexels.com/photos/2379020/pexels-photo-2379020.jpeg?cs=srgb&dl=pexels-didsss-2379020.jpg&fm=jpg", caption="Tandem skydivers mid-air against a clear blue sky"),
    Image(experience_id=9, user_id=3, url="https://images.pexels.com/photos/122829/pexels-photo-122829.jpeg?cs=srgb&dl=pexels-erikscheel-122829.jpg&fm=jpg", caption="Silhouette of a skydiver descending against a vibrant sunset sky"),

    Image(experience_id=10, user_id=1, url="https://images.pexels.com/photos/1645028/pexels-photo-1645028.jpeg?cs=srgb&dl=pexels-richard-segal-732340-1645028.jpg&fm=jpg", caption="Scuba diver photographing a sea turtle up close"),
    Image(experience_id=10, user_id=2, url="https://images.pexels.com/photos/1540108/pexels-photo-1540108.jpeg?cs=srgb&dl=pexels-freestockpro-1540108.jpg&fm=jpg", caption="Group of scuba divers exploring a colorful coral reef with fish"),
    Image(experience_id=10, user_id=3, url="https://images.pexels.com/photos/4666754/pexels-photo-4666754.jpeg?cs=srgb&dl=pexels-eliannedipp-4666754.jpg&fm=jpg", caption="Scuba diver silhouetted in a sunlit underwater cavern"),

    Image(experience_id=11, user_id=1, url="https://images.pexels.com/photos/696219/pexels-photo-696219.jpeg?cs=srgb&dl=pexels-helenalopes-696219.jpg&fm=jpg", caption="Group of adults enjoying a wine tasting in a warm social setting"),
    Image(experience_id=11, user_id=2, url="https://images.pexels.com/photos/39605/wineglass-wine-glass-wine-tasting-39605.jpeg?cs=srgb&dl=pexels-pixabay-39605.jpg&fm=jpg", caption="A wine glass with red wine at an outdoor tasting event"),

    Image(experience_id=12, user_id=3, url="https://images.pexels.com/photos/31094829/pexels-photo-31094829.jpeg?cs=srgb&dl=pexels-pedrofurtadoo-31094829.jpg&fm=jpg", caption="Chef using tongs to flambé a dish on the stove"),
    Image(experience_id=12, user_id=1, url="https://images.pexels.com/photos/5593704/pexels-photo-5593704.jpeg?cs=srgb&dl=pexels-rdne-5593704.jpg&fm=jpg", caption="A mother helps children make dough together in a fun cooking session"),

    Image(experience_id=13, user_id=2, url="https://images.pexels.com/photos/15297163/pexels-photo-15297163.jpeg?cs=srgb&dl=pexels-gizem-ozkan-332280659-15297163.jpg&fm=jpg", caption="Group of tourists walking near an old historical building"),
    Image(experience_id=13, user_id=3, url="https://images.pexels.com/photos/3354600/pexels-photo-3354600.jpeg?cs=srgb&dl=pexels-yuliya-kosolapova-1535772-3354600.jpg&fm=jpg", caption="Group of people standing under a scenic stone archway in a European city"),

    Image(experience_id=14, user_id=1, url="https://images.pexels.com/photos/22668091/pexels-photo-22668091.jpeg?cs=srgb&dl=pexels-airamdphoto-22668091.jpg&fm=jpg", caption="Visitors explore a grand museum hall with dinosaur and elephant exhibits"),
    Image(experience_id=14, user_id=2, url="https://images.pexels.com/photos/26734301/pexels-photo-26734301.jpeg?cs=srgb&dl=pexels-artur-stec-26039050-26734301.jpg&fm=jpg", caption="Art enthusiasts explore a modern exhibition in a historic building"),

    Image(experience_id=15, user_id=3, url="https://images.pexels.com/photos/6925184/pexels-photo-6925184.jpeg?cs=srgb&dl=pexels-pavel-danilyuk-6925184.jpg&fm=jpg", caption="Women engaged in a lively painting session in a decorated art studio"),
    Image(experience_id=15, user_id=1, url="https://images.pexels.com/photos/6925360/pexels-photo-6925360.jpeg?cs=srgb&dl=pexels-pavel-danilyuk-6925360.jpg&fm=jpg", caption="Three women enjoy a creative painting class together"),

    Image(experience_id=16, user_id=2, url="https://images.pexels.com/photos/31743028/pexels-photo-31743028.jpeg?cs=srgb&dl=pexels-yogavidyamandiram-31743028.jpg&fm=jpg", caption="Adults practicing yoga on mats in a group class setting"),
    Image(experience_id=16, user_id=3, url="https://images.pexels.com/photos/29720736/pexels-photo-29720736.jpeg?cs=srgb&dl=pexels-fbyf-studio-1601304170-29720736.jpg&fm=jpg", caption="Group of women practicing yoga in a bright, sunlit studio"),

    Image(experience_id=17, user_id=1, url="https://images.pexels.com/photos/10078868/pexels-photo-10078868.jpeg?cs=srgb&dl=pexels-zaid-mohammed-86842527-10078868.jpg&fm=jpg", caption="Man singing into a microphone on stage at a karaoke night"),
    Image(experience_id=17, user_id=2, url="https://images.pexels.com/photos/1840320/pexels-photo-1840320.jpeg?cs=srgb&dl=pexels-teemu-r-555088-1840320.jpg&fm=jpg", caption="Microphone on stage ready for a karaoke performance"),

    Image(experience_id=18, user_id=3, url="https://images.pexels.com/photos/175845/pexels-photo-175845.jpeg?cs=srgb&dl=pexels-tom-fisk-175845.jpg&fm=jpg", caption="Two skiers on a snowy mountain slope during a sunny day"),
    Image(experience_id=18, user_id=1, url="https://images.pexels.com/photos/3462586/pexels-photo-3462586.jpeg?cs=srgb&dl=pexels-daniel-frank-3462586.jpg&fm=jpg", caption="Skiers enjoying a winter day on the slopes"),
    ]


# seed_images.py


    db.session.add_all(images)
    db.session.commit()

def undo_images():
    db.session.execute("DELETE FROM images")
    db.session.commit()
