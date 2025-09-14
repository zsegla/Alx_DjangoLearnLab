# Permissions and Groups Setup Guide

## Custom Permissions

- The `Book` model in `bookshelf/models.py` defines custom permissions:
  - `can_view`: Can view book
  - `can_create`: Can create book
  - `can_edit`: Can edit book
  - `can_delete`: Can delete book

## Groups

- Create groups (Editors, Viewers, Admins) in the Django admin site.
- Assign the above permissions to each group as needed:
  - **Editors**: `can_edit`, `can_create`, `can_view`
  - **Viewers**: `can_view`
  - **Admins**: All permissions

## Views

- Views in `bookshelf/views.py` are protected with `@permission_required` decorators for each action.
- Example: Only users with `bookshelf.can_edit` can access the edit view.

## Testing

- Assign users to groups via the admin site.
- Log in as different users to verify access control for each view.

## Notes

- Permissions are enforced using Django's built-in decorators.
- You can further customize group/permission assignment in the admin or via scripts.
