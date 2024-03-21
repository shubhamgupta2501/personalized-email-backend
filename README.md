# Personalized Email Outreach Backend

Welcome to the backend of the "Personalized Email Outreach" project. This backend is built using FastAPI and serves as the communication layer between the user interface and the OpenAI GPT-3 model to generate personalized email content.

## Prerequisites

Before setting up and running the backend, please ensure that you have the following prerequisites installed on your system:

- [Python](https://www.python.org/) (3.7+)
- [Pip](https://pip.pypa.io/en/stable/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Langchain](https://pypi.org/project/langchain/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Your OpenAI API key

## Setup Instructions

Follow these steps to set up and run the backend locally:

1. **Clone the Repository:**

   Clone this GitHub repository to your local machine:

   ```shell
   git clone https://github.com/shubhamgupta2501/personalized-email-backend.git `

1.  Navigate to the Backend Directory:

    Change your current directory to the backend folder:

    shellCopy code

    `cd personalized-email-backend`

2.  Create a Virtual Environment (Optional):

    It's recommended to create a virtual environment to manage project dependencies:

    shellCopy code

    `python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate`

3.  Install Dependencies:

    Install the required Python packages using pip:

    shellCopy code

    `pip install -r requirements.txt`

4.  Environment Variables:

    Create a `.env` file in the backend directory and add your OpenAI API key as follows:

    makefileCopy code

    `OPENAI_API_KEY=your-api-key`

5.  Run the Backend:

    Start the FastAPI backend with the following command:

    shellCopy code

    `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

    The backend will be accessible at `http://localhost:8000`.

6.  CORS Configuration (Optional):

    By default, the backend allows communication from `http://localhost:8000`. If you want to change the allowed origins, update the CORS middleware settings in `main.py`.

API Endpoint
------------

The backend provides a single API endpoint for generating personalized emails:

-   POST /generate-email: Send a POST request with a JSON body containing your email prompt. The backend will communicate with GPT-3 and return the generated email content.

Deployment
----------

To deploy the backend on a server, you can use AWS Lambda, AWS Fargate, or any preferred cloud hosting service. Make sure to adjust the CORS settings to allow your frontend domain when deploying to production.

For more detailed information on the frontend setup and deployment, please refer to the [project's frontend README](https://github.com/shubhamgupta2501/personalized-email-frontend).

License
-------

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.
