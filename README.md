#  Neo-Brutalist Number Guessing Game

A modern, highly responsive web application built with Python and Flask. The game challenges players to guess a randomly generated number between 1 and 100 within 5 attempts, offering a dynamic fallback hint system if they run out of tries.

---

##  Live Demo / Preview
* **Core Paradigm:** Object-Oriented State Management & Server-Side Routing
* **Interface Style:** Playful Neo-Brutalist Aesthetic

---

##  Tech Stack & AI Attribution

This project is a hybrid build that demonstrates both core computer science algorithmic foundations and the effective use of AI as an engineering force multiplier.

* **Core Game Logic (100% Manual):** I designed and implemented the underlying game algorithms, conditional evaluation ranges, and session state architecture in Python.
* **Web Scaffolding & Styling (AI-Assisted):** I utilized generative AI to scaffold the initial Flask boilerplate routing code (`@app.route`) and the basic HTML layout. 
* **Integration & Security Refactoring (Manual):** I manually audited and refactored the AI-generated output to implement secure session key environment variables (`os.urandom`), strict input type safety (`try-except` blocks), responsive CSS layouts without fragile structural selectors, and full web accessibility standards.

---

##  Key Technical Features

### 1. Robust Server-Side State Management
Instead of relying on fragile client-side JavaScript that can be easily manipulated in the browser console, this application leverages cryptographically signed Flask cookies via `flask.session` to securely persist user attempts, hints, and target numbers across HTTP requests.

### 2. Defensive Input Validation
To prevent server crashes caused by bad or empty user payloads, the backend handles type conversions defensively. String inputs from forms are validated before arithmetic manipulation to ensure stability.

### 3. Accessible HTML5 & Maintainable CSS
* **A11y Compliant:** Implements explicit, screen-reader friendly utility classes (`.visually-hidden`) for all form fields.
* **Component-Driven Styles:** Avoids brittle layout selectors like `:nth-of-type` in favor of modular CSS classes, ensuring the interface remains visually stable when elements dynamically render based on game state.

---

##  Installation & Local Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd Number-Guessing-Game
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install flask
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0`.

---

##  Academic Integrity Statement
This project was built as a personal learning initiative to explore web micro-frameworks and frontend integration. All algorithmic comparison logic, game loop architecture, and bug fixes were completed manually to reinforce concepts of Object-Oriented design and data processing learned in university coursework.
