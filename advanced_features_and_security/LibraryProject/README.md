# Permissions & Groups Setup

## Custom Permissions
Defined in `bookshelf/models.py` under the `Book` model:

- can_view
- can_create
- can_edit
- can_delete

## Groups Created
1. **Viewers**
   - can_view

2. **Editors**
   - can_view
   - can_create
   - can_edit

3. **Admins**
   - can_view
   - can_create
   - can_edit
   - can_delete

## Views Enforcement
Permission checks implemented using `@permission_required` decorator in `bookshelf/views.py`.

## Testing
Create test users and assign groups via Django admin. Verify access using their login permissions.
