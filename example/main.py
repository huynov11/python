from user import User
from user_manager import UserManager

# Using class UserManager
user_manager = UserManager()

# Create user
user1 = User(1, "Nguyen Van A", "2000-05-20", "1234567890", "nguyenvana@gmail.com")
user2 = User(2, "Nguyen Van b", "2001-08-30", "9876543210", "nguyenvanb@gmail.com")

# Add user to UserManager
user_manager.add_user(user1)
user_manager.add_user(user2)

# Show all infor of user
user_manager.display_all_users()

# Update infor of user
user_manager.update_user(2, "Nguyen Van B", "2001-08-30", "9876543210", "nguyenvanb@gmail.com")

# Show all infor of user
user_manager.display_all_users()
