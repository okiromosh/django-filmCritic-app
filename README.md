
# Film Critic
# Movie and Series Discussion Forum - Django App

This Django application facilitates discussions about movies and series by allowing users to create discussion rooms and participate in conversations. Users can create rooms, comment on discussions, view profiles, and manage their activities within the platform.

### Features:

1. **User Authentication:**
   - User login, registration, and logout functionalities.

2. **User Profiles:**
   - User-specific profiles displaying rooms created, comments made, and other activities.
   
3. **Room Management:**
   - Creation, viewing, and participation in discussion rooms.
   - Users can create new rooms and view existing discussion rooms.

4. **Comments and Messages:**
   - Ability to comment on existing discussion rooms.
   - Deleting comments made by the user.

### Views and Functions:

#### User Views
- `loginPage(request)`: Manages user login and prevents re-login for authenticated users.
- `registerPage(request)`: Handles user registration and redirects to the home page after successful registration.
- `logoutUser(request)`: Logs out the user and redirects to the home page.
- `userProfile(request, pk)`: Displays user profile, including created rooms, comments, and user activities.

#### Room Management
- `home(request)`: Displays movies, series rooms, and categories, along with comment counts.
- `room(request, pk)`: Manages room details, members, and comments.
- `createRoom(request)`: Handles the creation of new discussion rooms.
- `updateRoom(request)`: Functionality for updating discussion rooms.
- `deleteRoom(request)`: Functionality for deleting discussion rooms.

#### Messages/Comments View
- `deleteComment(request, pk)`: Deletes user comments and manages permission checks for comment deletion.

### Requirements:
- Ensure Django is installed and configured.
- Necessary models and forms (`Room`, `Comment`, `Category`) should be defined in the associated `models.py` and `forms.py`.

### Usage:

1. **Setup Environment:**
   - Install Django and configure the necessary models and forms.

2. **Integration:**
   - Integrate the provided views into your Django application's `views.py`.
   - Map the views to respective URLs for user access.

3. **Customization:**
   - Customize HTML templates for each view to align with your application design.

### Note:
- This script assumes the presence of specific models (`Room`, `Comment`, `Category`) within your Django application for proper functionality.
- Feel free to modify the views and functions to suit your application's specific requirements.

---
