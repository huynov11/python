# User Management System

This project demonstrates a simple user management system implemented in Python. It consists of three main files: `user.py`, `user_manager.py`, and `main.py`.

## user.py

The `user.py` file defines the `User` class, which represents a user in the system. It contains the following attributes:

- `id`: Unique identifier of the user.
- `name`: Name of the user.
- `birthday`: Birthday of the user.
- `phone`: Phone number of the user.
- `email`: Email address of the user.

The `User` class also provides getter and setter methods for accessing and modifying these attributes.

## user_manager.py

The `user_manager.py` file contains the `UserManager` class, responsible for managing a collection of user objects. It provides the following functionalities:

- Adding a user to the user collection.
- Removing a user from the user collection.
- Displaying information of all users in the collection.
- Updating user information based on the user ID.

The `UserManager` class utilizes the `User` class to create, modify, and display user objects.

## main.py

The `main.py` file serves as the entry point of the user management system. It demonstrates how to use the `User` and `UserManager` classes to perform various operations. In the example provided, it creates instances of `User` objects, adds them to the `UserManager`, updates user information, and displays user details.

## Getting Started

To run the user management system, follow these steps:

1. Ensure that you have Python installed on your system.
2. Download or clone the project files to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the `main.py` file using the command `python main.py`.
5. Observe the output in the console, which shows the user management system in action.

Feel free to explore and modify the code in the respective files to suit your needs.

## License

This project is licensed under the [MIT License](LICENSE), which allows you to use, modify, and distribute the code freely.