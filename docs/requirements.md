# Literary Blog Requirements (Updated)

## 1) Objective
Replace the current static blog (Hugo + Nginx) with a dynamic platform for literary dissemination, featuring Markdown article management, comments, a forum, user profiles, and centralized administration.

## 2) MVP Scope (Current Implementation)

Includes:
- Registration, login, logout, and basic user profile management.
- Article publication and management from the administration panel.
- Secure Markdown to HTML conversion.
- Article comments for authenticated users.
- Basic forum (threads + replies) with a sensitive content warning.
- User banning to prevent participation in the forum.
- Basic view count statistics per article.
- **Email notifications** for subscribers when new blog posts or forum threads are published.
- 'About Me' section detailing author information.

Does not include in MVP:
- Advanced reputation system (reactions, likes).
- Advanced search or content recommender.
- Advanced moderation (reports, queues, detailed auditing).

## 3) Technical Decisions

- Backend: `Django` (Python).
- Database: `SQLite3`.
- Frontend: `Django Templates + HTMX + Bootstrap`.
- Deployment: `Docker` container on an Ubuntu server.

Rationale (Beginner-friendly approach):
- Avoids the complexity of a SPA (React/Vue) for the initial project.
- Keeps logic on the server and minimizes manual JavaScript.
- Allows for progressive interactivity using HTMX.

## 4) Functional Requirements

### 4.1 Users and Authentication
- FR-USER-01: The system allows registration with a unique `username`, unique `email`, and password.
- FR-USER-02: The system allows login and logout.
- FR-USER-03: Users can edit their profile, including an avatar photo, biography, and notification preferences.
- FR-USER-04: The system prevents registration with duplicate emails.
- FR-USER-05: Banned users cannot create topics or reply in the forum.
- FR-USER-06: Users can opt-in to receive email notifications for new blog posts and forum threads.

### 4.2 Administration Panel
- FR-ADMIN-01: Admin panel access is available for administrative staff.
- FR-ADMIN-02: Admins can create articles with a title, Markdown content (including images), a featured image, and tags.
- FR-ADMIN-03: Admins can preview articles before publishing.
- FR-ADMIN-04: Admins can edit and delete articles.
- FR-ADMIN-05: Admins can view the view count per article.
- FR-ADMIN-06: Admins can ban and unban users (logging the reason in the `BanLog`).

Implementation Note:
- `Django Admin` is used as the base panel.
- The initial superuser is created using environment variables in the `.env` file during bootstrapping.

### 4.3 Main Blog
- FR-BLOG-01: The homepage lists published articles with their title, featured image, date, and author.
- FR-BLOG-02: The detail view shows content securely rendered from Markdown to HTML.
- FR-BLOG-03: Only authenticated users can comment on articles.
- FR-BLOG-04: Each comment displays the author, date, and content.
- FR-BLOG-05: Subscribers receive an email alert with the article link when a new post is published.

### 4.4 Forum
- FR-FORUM-01: Only authenticated users can create threads.
- FR-FORUM-02: Only authenticated users can reply to threads.
- FR-FORUM-03: A sensitive content warning and community guidelines are displayed before accessing the forum.
- FR-FORUM-04: Banned users are restricted from publishing in the forum.
- FR-FORUM-05: Subscribers receive an email alert when a new forum thread is created.

### 4.5 Markdown and Content Security
- FR-MD-01: Article content is written in Markdown.
- FR-MD-02: The system converts Markdown to HTML when displaying or publishing.
- FR-MD-03: The resulting HTML is sanitized to prevent XSS attacks.

### 4.6 Statistics
- FR-STATS-01: Every article detail view increments the view counter.
- FR-STATS-02: The administrator can query total views per article within the control panel.

## 5) Acceptance Criteria (Verifiable)

### 5.1 Registration and Authentication
- AC-01: Given an existing email, when trying to register with it, the system rejects the registration.
- AC-02: Given a valid user, when logging in, they gain access to their authenticated session.
- AC-03: Given an authenticated user, when logging out, the session is properly invalidated.

### 5.2 Article Administration
- AC-04: Given an admin, when creating an article with a title and content, the article can be published.
- AC-05: Given an existing article, when edited by an admin, changes are immediately reflected on the public view.
- AC-06: Given an article, when previewed, it displays the rendered HTML from Markdown before publishing.

### 5.3 Comments
- AC-07: Given an unauthenticated user, when attempting to comment, the system requires them to log in.
- AC-08: Given an authenticated user, when posting a comment, it appears alongside the author's name and date.

### 5.4 Forum and Banning
- AC-09: Given an unbanned authenticated user, when creating a forum thread, the thread is published.
- AC-10: Given a banned user, when attempting to create a thread or reply, the system blocks the action.
- AC-11: Given any user, when entering the forum for the first time in their session, they see the sensitive content warning.

### 5.5 Statistics
- AC-12: Given an article, when its detail view is opened, its view count increases by +1.
- AC-13: Given an admin in the panel, when viewing articles, they can see the accrued views per article.

## 6) Non-Functional Requirements

- NFR-01: Responsive interface (mobile, tablet, desktop).
- NFR-02: Data persistence using `SQLite3`.
- NFR-03: Backend framework: `Django`.
- NFR-04: Self-hosted deployment via `Docker` on Ubuntu Server.
- NFR-05: Backend form validation.
- NFR-06: Active CSRF protection on forms.
- NFR-07: Sanitization of HTML rendered from Markdown.

## 7) Roadmap & Phasing

### Phase 1 - MVP (Implemented)
- Users: Registration/login/logout/profile settings (including subscriptions).
- Blog: Listings + detail view + authenticated comments + email notifications.
- Admin: Article CRUD + Markdown preview.
- Forum: Threads/replies + sensitive warning + email notifications.
- Basic user banning (`BanLog`) and rudimentary view counters.
- "About Me" static integration.

### Phase 2 - Hardening
- Strengthen authentication tests, permissions, and critical flows.
- UX improvements (pagination and form feedback).
- Daily metrics for article visits.

### Phase 3 - Post-MVP
- Advanced moderation (reports, content hiding).
- Search and filtering by tags.
- Additional integrations (e.g., full email confirmation with secure links, external analytics).

## 8) Post-MVP Backlog (Prioritized)

- BL-01: Secure link email verification.
- BL-02: Password recovery flow via email.
- BL-03: Search functionality for articles and the forum.
- BL-04: advanced filtering by tags and authors.
- BL-05: Reporting system and advanced moderation tools.
- BL-06: Analytics dashboard featuring time series data.

## 9) Resolved Definitions for Current Version

To avoid implementation blocks, the following decisions were finalized:
- Email validation in MVP = email uniqueness check (though a boolean flag `is_email_verified` exists in the model).
- MVP Statistics = total view count per article only.
- MVP Banning = blocking write-access in the forum (create thread / reply).
- MVP Admin Panel = native `Django Admin`.
- **Added features over original MVP scope**: Email notifications for post publishing and forum topics are now fully functional functionalities based on user profile preferences.
