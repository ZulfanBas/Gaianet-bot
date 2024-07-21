# GaiaNet API Interaction Program

This program allows users to ask questions to the GaiaNet AI assistant and save the responses to a file.

## Requirements

- Python 3.x
- `requests` library

You can install the required library using pip:

```sh
pip install requests
```

## Usage

1. Clone the repository:

```sh
git clone https://github.com/ZulfanBas/Gaianet-bot/
cd Gaianet-bot
```

2. Run the program:

```sh
python ask_question.py
```

3. Enter your question when prompted. The response from the GaiaNet API will be saved to a file named `response.txt`.

## Example

```sh
Enter your question: What is the capital of France?
Response saved to response.txt
```

The response file `response.txt` will contain:

```
The capital of France is Paris.
```

## Troubleshooting

- Ensure you have an active internet connection.
- Check the API endpoint and payload structure if you encounter issues.
- Make sure you have the necessary permissions to write to the file system.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to modify the code and contribute to this project by creating pull requests. Happy coding!
