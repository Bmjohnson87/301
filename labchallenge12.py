#  Imports the requests
import requests

# For user input
#  Imports the getpass function to hide user input for the HTTP method selection
from getpass import getpass


def main():
    # Prompt for URL and HTTP method
    # Prompts the user to enter the destination URL and stores it in the url variable
    url = input("Enter destination URL: ")
    http_method = getpass("Select HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

    # Validate input
    # Defines a list of valid HTTP methods
    valid_methods = ("GET", "POST", "PUT", "DELETE", "HEAD", "PATCH", "OPTIONS")
    if http_method not in valid_methods:
        print("Invalid HTTP method. Please try again.")
        exit()

    # Build request details
    # Checks if the user-selected method is valid
    request_info = {
        "method": http_method,
        "url": url,
        "headers": requests.utils.default_headers(),
    }

    # Print request information and confirm
    #
    print(f"\n{request_info['method']} request to: {request_info['url']}")
    print(f"Headers: {request_info['headers']}")

    confirm = input("Proceed? (y/n): ").lower()
    if confirm != "y":
        print("Aborting...")
        exit()

    # Send request and handle response
    try:
        response = requests.request(**request_info)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit()

    # Translate and print status code
    status_messages = {
        200: "OK",
        400: "Bad Request",
        401: "Unauthorized",
        404: "Not Found",
        500: "Internal Server Error",
    }
    print(f"\nStatus code: {response.status_code} - {response.reason}")
    print(f"Plain text: {status_messages.get(response.status_code, response.reason)}")

    # Print response headers
    print("\nResponse headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
