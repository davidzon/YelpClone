# TryThis!

## Live Site
🌐 [https://trythis-pq3i.onrender.com/]

## Backend Repository
🛠 [https://github.com/davidzon/YelpClone]   [_Fullstack Repo: Backend & Frontend_]


## Summary
TryThis! is a full-stack Yelp-style clone that empowers users to discover and review unique experiences. Users can create businesses, leave reviews, upload images, and explore curated experiences by price, category, and location. With polished modals and dynamic search, TryThis! brings local exploration to life.



## 🔧 Features

- 🔐 User authentication with session persistence
- 🏢 Create, edit, and delete your own experiences
- 📸 Upload and remove images from experiences
- 💬 Leave, edit, and delete reviews
- 🧠 Dynamic search by name, category, or price
- 🌍 Explore page with all experiences
- 🧾 Personalized “My Experiences” dashboard
- ✅ Modal confirmations for delete actions
- 📦 Toast notifications for UX feedback
- 🔍 Client-side and backend filtering
- 🖼 Image modal viewer with delete support
- 🎨 Responsive design using CSS modules

---

## ⚙️ Technologies Used

- **Frontend**: React, Vite, Toastify, CSS Modules
- **Backend**: Python, Flask, SQLAlchemy, Flask-Migrate, Flask-Login
- **Database**: PostgreSQL (prod), SQLite (dev)
- **Authentication**: Flask-Login session management
- **Deployment**: Docker, Render

---

## 📁 Redux Store Shape

```js
{
  session: {
    user: {
      id,
      username,
      email
    }
  }
}
```

---

## 📂 API Routes

### Auth
- `GET /api/auth/` — restore session
- `POST /api/auth/login` — log in
- `POST /api/auth/signup` — sign up
- `POST /api/auth/logout` — log out

### Users
- `GET /api/users/:id` — user profile

### Experiences
- `GET /api/experiences/` — all experiences w/ query filters
- `GET /api/experiences/current` — current user’s experiences
- `GET /api/experiences/:id` — single experience w/ images
- `POST /api/experiences/` — create new experience
- `PUT /api/experiences/:id` — edit experience
- `DELETE /api/experiences/:id` — delete experience

### Reviews
- `GET /api/reviews/experience/:id` — get reviews for experience
- `POST /api/reviews/` — create review
- `PUT /api/reviews/:id` — update review
- `DELETE /api/reviews/:id` — delete review

### Images
- `POST /api/images/` — upload image
- `DELETE /api/images/:id` — delete image

---

## 🎨 Frontend Routes

- `/` — Homepage (review feed)
- `/login` — Login modal
- `/signup` — Signup modal
- `/create` — Create experience form
- `/explore` — Browse all experiences
- `/my-experiences` — User dashboard for created listings
- `/experiences/:id` — Experience detail w/ images & reviews
- `/experiences/:id/edit` — Edit form for your listing

---

## 🧠 Technical Highlights

- ✅ Secure CSRF cookie handling across environments
- ✅ Search intelligently handles strings and exact number price matches
- ✅ Toast notifications after each user interaction
- ✅ Responsive auto-rotating image slideshow on create page
- ✅ Reusable confirmation modals
- ✅ Auto-hiding dropdowns and smooth profile menu animation
- ✅ Full support for user image management per experience

---

## 🗃 Database Schema

- **User**: id, username, email, hashed_password
- **Experience**: id, creator_id, title, description, location, category, price
- **Review**: id, user_id, experience_id, rating, review, created_at
- **Image**: id, user_id, experience_id, url, caption

```
User (1) ──< (many) Experience
User (1) ──< (many) Review
User (1) ──< (many) Image
Experience (1) ──< (many) Review
Experience (1) ──< (many) Image
```

---

## 🛠 Installation & Setup

### 1. Clone and install dependencies
```bash
git clone https://github.com/your-username/trythis.git
cd trythis
pipenv install
pipenv shell
npm install --prefix react-vite
```

### 2. Configure your .env and .flaskenv
```
# .env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///dev.db
SCHEMA=try_this_schema

# .flaskenv
FLASK_APP=app
FLASK_DEBUG=true
FLASK_RUN_PORT=8000
FLASK_ENV=development
```

### 3. Migrate and seed the database
```bash
flask db upgrade
flask seed all
```

### 4. Build frontend & run dev server
```bash
cd react-vite
npm run build
cd ..
flask run
```

---

## 📦 Deployment (Render)

- Run `npm run build` in `react-vite/`
- Commit and push all changes
- In Render:
  - Create a PostgreSQL instance
  - Add environment variables:
    - `SECRET_KEY`
    - `FLASK_ENV=production`
    - `FLASK_APP=app`
    - `SCHEMA=try_this_schema`
    - `DATABASE_URL` (from PostgreSQL)
- Deploy with Dockerfile config

---

## 🙏 Acknowledgments

- App Academy for their structure and curriculum
- Toastify for the clean feedback system
- All contributors of Flask and React for open-source libraries

---
