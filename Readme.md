# Review Extractor

## Overview

The Review Extractor is a web application that extracts customer reviews from product pages using dynamic CSS identification and browser automation. The backend is powered by Flask and Playwright, while the frontend is built with React.

## Features

- Extracts reviews from various product pages.
- Utilizes a Large Language Model (LLM) to dynamically identify CSS selectors for reviews.
- Handles pagination to ensure all reviews are retrieved.
- Provides a simple React frontend to interact with the API.

## Project Structure

```
GOMARBLE_ASSIGNMENT/
│
├── venv/                      # Virtual environment
├── backend/
│   ├── Server.py              # Flask server
│   ├── Scraper.py             # Review extraction logic
│   └── llm_helper.py          # LLM integration for CSS selector identification
├── review_extractor/
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   └── Review_Extractor.jsx # Review extraction component
│   └── public/
│       └── index.html         # HTML entry point
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js and npm
- Google Cloud account for LLM API access

### Backend Setup

1. **Clone the repository** and navigate to the project directory.

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install  # To install browser binaries
   ```

4. **Configure Google Cloud**:
   - Set up your Google Cloud credentials and ensure the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set.

5. **Run the Flask server**:
   ```bash
   python backend/Server.py
   ```

### Frontend Setup

1. **Navigate to the `review_extractor` directory**:
   ```bash
   cd review_extractor
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

3. **Start the React development server**:
   ```bash
   npm start
   ```

## Usage

- Access the React frontend at `http://localhost:3000`.
- Enter a product page URL to extract reviews.
- The extracted reviews will be displayed in the frontend.

## Configuration

- Ensure your Google Cloud credentials are correctly configured.
- Adjust the CSS selectors in `Scraper.py` as needed for different websites.

## Troubleshooting

- **Rate Limit Errors**: If you encounter rate limit errors, consider implementing retry logic or upgrading your API plan.
- **Selector Issues**: If reviews are not being extracted, verify the CSS selectors and adjust them as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of Playwright and Flask for their excellent tools.
- Special thanks to Google Cloud for providing the LLM API.