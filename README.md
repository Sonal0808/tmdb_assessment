**🎬 TMDB Stand Alone Flask App**
```
This is a simple Flask web application that interacts with The Movie Database (TMDB) API to display:
	•🏆 The most popular movies sorted by vote count.
	•🌟 The most popular actors, sorted by the number of movies they’ve appeared in.

1. 🚀 Features
	•/popular-movies — Lists popular movies sorted by number of votes.
	•/top-actors — Lists popular actors sorted by how many movies they’ve acted in. Supports pagination via query parameter actors_per_page.

2. 📦 Requirements
	•Python 3.7+
	•Flask
	•requests
	•pandas 
 3. 🛠 How to Run
	1.Clone the repository or copy the code into a Python file (e.g., app.py).
	2.Make sure you have Python installed and dependencies installed.
	3.Run the app:👉 python3 app.py
	The server will start at:👉 http://localhost:8080

4. 🌐 Endpoints
	/popular-movies
	•Method: GET
	•Description: Returns an HTML page listing popular movies and their vote counts.
	•Example: http://localhost:8080/popular-movies

	/top-actors
	•Method: GET
	•Description: Returns an HTML page listing popular actors and how many movies they’ve appeared in.
	•Query Parameter:
	•actors_per_page (optional): Number of actors per page (default is 20). Pagination is handled manually for /top-actors, but the output is combined into a single HTML page.
	•Example: http://localhost:8080/top-actors?actors_per_page=10
```
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**🐳 Docker Setup**
Docker helps to containarise and run applications wiht all dependencies and can be shipped to any machine.
```
1. ✅ Prerequisites
	•Make sure Docker is installed on your system.
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
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**🐳 GitHub Workflow: docker-build.yml**
```
Why Workflow ?

Although I can run this Flask app manually or inside a Docker container on my local machine, I created this GitHub Actions workflow for a few key reasons:

✅ Automation & Consistency
By using a workflow, I ensure that every time I push to the main branch:
	•The app is built inside a Docker container
	•The container is run
	•The /top-actors endpoint is tested for availability
This eliminates human error and guarantees that each deployment or update passes a basic functionality check.

🧪 Quick Feedback Loop
Instead of manually spinning things up to verify changes, this workflow automatically tests that the app starts up and responds correctly. If something breaks, I get feedback immediately after a push.

🖥️ Why a Self-Hosted Runner?
I chose a self-hosted runner for a few reasons:
	•I needed access to resources or configurations that GitHub-hosted runners don’t allow (run on my local host to test the webapp).
	•I wanted more control over the environment and caching to reduce cold starts.

📦 What This Workflow Does
Here’s what the docker-build.yml workflow accomplishes:
	1.Checks out the code
	2.Sets up Docker Buildx (for advanced Docker builds)
	3.Builds the Docker image tagged my-flask-app
	4.Runs the container, mapping port 8080
	5.Waits for the app to start up (simple sleep command)
	6.Tests the app using a curl call to ensure /top-actors responds successfully
        7.It does not stop the container as I want it to run so we can test.
```
Use the below runner config from the repo to setup a self-hosted runner:
```
Create a Directory for the Runner - mkdir actions-runner && cd actions-runner 
Download the Latest Runner Package - curl -o actions-runner.tar.gz -L https://github.com/actions/runner/releases/latest/download/actions-runner-osx-x64-2.308.0.tar.gz 
Extract the Installer - tar xzf ./actions-runner.tar.gz 
Configure the Runner - ./config.sh --url https://github.com/Sonal0808/tmdb_assessment --token BREWOER55SJ4M6BNXHIQNCDH6LPKK 
Start the Runner - ./run.sh
```
