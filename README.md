# personalized-email-backend

Prerequisites
Before setting up and running the backend, please ensure that you have the following prerequisites installed on your system:

Python (3.7+)
Pip
FastAPI
Langchain
python-dotenv
Your OpenAI API key
Setup Instructions
Follow these steps to set up and run the backend locally:

Clone the Repository:

Clone this GitHub repository to your local machine:

shell
Copy code
git clone https://github.com/shubhamgupta2501/personalized-email-backend.git
Navigate to the Backend Directory:

Change your current directory to the backend folder:

shell
Copy code
cd personalized-email-backend
Create a Virtual Environment (Optional):

It's recommended to create a virtual environment to manage project dependencies:

shell
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
Install Dependencies:

Install the required Python packages using pip:

shell
Copy code
pip install -r requirements.txt
Environment Variables:

Create a .env file in the backend directory and add your OpenAI API key as follows:

makefile
Copy code
OPENAI_API_KEY=your-api-key
Run the Backend:

Start the FastAPI backend with the following command:

shell
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
The backend will be accessible at http://localhost:8000.

CORS Configuration (Optional):

By default, the backend allows communication from http://localhost:8000. If you want to change the allowed origins, update the CORS middleware settings in main.py.

API Endpoint
The backend provides a single API endpoint for generating personalized emails:

POST /generate-email: Send a POST request with a JSON body containing your email prompt. The backend will communicate with GPT-3 and return the generated email content.
