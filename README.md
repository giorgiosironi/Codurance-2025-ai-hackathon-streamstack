# Codurance-2025-ai-hackathon-streamstack

Starter repository for the film and tv challenge based on a fictitious startup as part of the Codurance AI Hackathon

# Thoughts afterwards - Micheal

I am a lot more proud of the code produced in this task. I think I could have produced more with some AI assistance, but I trust more what I wrote, and I feel far more ownership over it.

## Screenshot

![Screenshot of final app](finalscreenshot.png)

# StreamStack

## Context

StreamStack is a new startup aiming to build a **community-driven platform** where users can review and rate Netflix shows and films.

They believe that while Netflix offers a vast catalogue of content, it lacks a **social layer** for discussion, recommendations, and authentic viewer feedback.

The first version of the platform will be a **simple web application** allowing users to:

- Browse Netflix titles
- View detailed information
- Leave ratings and written reviews

StreamStack is open to using any technology or framework (React, Vue, Angular, Django, Flask, Spring Boot, etc.).  
The only restriction: **no low-code or no-code tools** are allowed.

The **UI/UX is completely up to you**.  
They encourage creativity and want an intuitive, visually engaging interface that would appeal to TV and film enthusiasts.

To get started, StreamStack recommends using this open-source Netflix titles dataset from Kaggle:  
🔗 [Netflix Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows/data)

---

## Required Features

### 🎬 Title Catalogue Page

- Display a list of Netflix titles (films and series) with metadata such as **title**, **type**, and **release year**.
- Users should be able to **filter** by director and rating.
- Users should be able to **sort** by release year or title.

### 🔍 Title Detail Page

- Navigate to a detailed page when a title is clicked.
- Show **description**, **cast**, and additional metadata.
- Include a **reviews and ratings section**.

### ✍️ Add a Review

- Allow users to **submit a rating** (e.g., 1 to 5 stars) and a **written review** for any title.
- Assume **all users are anonymous** — no authentication is required.

### 🛠️ Backend API

- Implement a backend API to:
  - Serve the title data
  - Manage user reviews
- Load the Netflix dataset into a **local database** or **serve from memory**.

### 🎨 Frontend UI

- Build a **responsive, user-friendly** frontend.
- The design and styling are up to you — focus on **clarity and usability**.

### 📈 Review Aggregation

- For each title, **calculate and display the average user rating** based on submitted reviews.

### 🔎 Search Functionality

- Implement a **search bar** that lets users search titles by name or keyword.

---

## Additional Information

- Please **fork** the following GitHub repository: `Codurance-2025-ai-hackathon-streamstack` and commit your solution there.
- There is **no requirement to build a CI/CD pipeline**.
- **Local development** is sufficient — no deployment to an external environment is needed.
- **Code quality is important** to StreamStack.  
  Your solution should be **well-designed** and **written in a test-driven manner**.
