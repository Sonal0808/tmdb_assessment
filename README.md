This is a simple Python application containerized using Docker.  
It is designed to work with a **self-hosted GitHub Actions runner**, which will build and run the app, making the web page accessible.

2. Set Up the Self-Hosted Runner: This project utilizes a self-hosted GitHub Actions runner to automate workflows.
   Create a Directory for the Runner - mkdir actions-runner && cd actions-runner
   Download the Latest Runner Package - curl -o actions-runner.tar.gz -L https://github.com/actions/runner/releases/latest/download/actions-runner-osx-x64-2.308.0.tar.gz
   Extract the Installer - tar xzf ./actions-runner.tar.gz
   Configure the Runner - ./config.sh --url https://github.com/Sonal0808/tmdb_assessment --token BREWOER55SJ4M6BNXHIQNCDH6LPKK
   Run the Runner - ./run.sh

3. Docker Deployment - docker build -t tmdb-assessment-app
   Run the Docker Container- docker run -d --name tmdb-assessment-container -p 8080:8080 tmdb-assessment-app
   Access the application at http://127.0.0.1:8080/top-actors

4. Flask Application Persistence: The app.py is configured to keep the Flask server running continuously to ensure the web application remains accessible. The typical stop command has been commented out to prevent the server from terminating.
   
5.Workflow Automation: With the self-hosted runner set up, any changes pushed to the repository will trigger the GitHub Actions workflow, automating the deployment process. 

  
