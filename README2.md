**🎬 TMDB Stand Alone Flask App**
```
This is a simple Flask web application that interacts with The Movie Database (TMDB) API to display:
	•	🏆 The most popular movies sorted by vote count.
	•	🌟 The most popular actors, sorted by the number of movies they’ve appeared in.
⸻
1. 🚀 ##Features
	•	/popular-movies — Lists popular movies sorted by number of votes.
	•	/top-actors — Lists popular actors sorted by how many movies they’ve acted in. Supports pagination via query parameter actors_per_page.
⸻
2. 📦 ##Requirements
	•	Python 3.7+
	•	Flask
	•	requests
	•	pandas 
 3. 🛠 ##How to Run
	1.	Clone the repository or copy the code into a Python file (e.g., app.py).
	2.	Make sure you have Python installed and dependencies installed.
	3.	Run the app:👉 python3 app.py
	The server will start at:👉 http://localhost:8080
 ⸻
4. 🌐 ##Endpoints
	/popular-movies
	•	Method: GET
	•	Description: Returns an HTML page listing popular movies and their vote counts.
	•	Example: http://localhost:8080/popular-movies
⸻
	/top-actors
	•	Method: GET

	•	Description: Returns an HTML page listing popular actors and how many movies they’ve appeared in.

	•	Query Parameter:

	•	actors_per_page (optional): Number of actors per page (default is 20). Pagination is handled manually for /top-actors, but the output is combined into a single HTML page.

	•	Example: http://localhost:8080/top-actors?actors_per_page=10
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**🐳 Docker Setup**

```
1. ✅ Prerequisites
	•	Make sure Docker is installed on your system.
2. 📁 Project Structure
Your project directory should look like this:
        .
	├── app.py
	├── requirements.txt
	└── Dockerfile```
4. 📦 Build the Docker Image:👉 
   docker build -t tmdb-flask-app .
5. 🚀 Run the Container:👉  
   docker run -p 8080:8080 tmdb-flask-app
6. Visit app at http://localhost:8080/top-actors
```
