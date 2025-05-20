# RandomQuoteGenerator

A simple Python command-line application that fetches and displays a random quote, its author, and category from the [API Ninjas Quotes API](https://api-ninjas.com/api/quotes).

## Features

*   Fetches a random quote from an external API.
*   Displays the quote, author, and category.
*   Securely manages API keys using environment variables.
*   Basic error handling for API requests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.7+
*   pip (Python package installer)
*   Git (for cloning the repository)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/jakubrobaszek/RandomQuoteGenerator
    cd RandomQuoteGenerator
    ```

2.  **Create and activate a virtual environment (recommended):**
    *   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    *   Sign up for a free API key at [API Ninjas](https://api-ninjas.com/register).
    *   Once you have your key, create a `.env` file in the root of the project directory by copying `.env_example`:
        ```bash
        cp .env_example .env
        ```
    *   Open the `.env` file and add your API key:
        ```
        api_key="YOUR_API_NINJAS_KEY_HERE"
        ```
        **Important:** Do NOT commit your `.env` file to version control. It's already included in the `.gitignore` file.

## Usage

Once the setup is complete, you can run the script from your terminal:

```bash
python main.py
```

## Why I Coded This
1. Working with External APIs (requests, authentication - by key)
2. Data Handling (JSON)
3. Enviroment Management and Security (.env, .gitignore)
4. Dependency Management (requirements.txt by pip freeze)
