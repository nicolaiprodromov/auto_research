# Tavily Search Project

This project is a Python application that utilizes the Tavily API to search the internet for specified terms. It provides a simple interface for users to input search queries and retrieve results.

## Project Structure

```
tavily-search-project
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── tavily_client.py
│   └── config.py
├── tests
│   ├── __init__.py
│   └── test_tavily_client.py
├── .github
│   └── workflows
│       └── tavily_search.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/tavily-search-project.git
   cd tavily-search-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your environment variables by copying `.env.example` to `.env` and adding your Tavily API key.

## Usage

To run the application, execute the following command:
```
python src/main.py
```

You will be prompted to enter a search term. The application will then use the Tavily API to search for the term and display the results.

## Testing

To run the tests, use the following command:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

This project uses the Tavily API for internet searching. For more information, visit [Tavily API Documentation](https://tavily.com/docs).