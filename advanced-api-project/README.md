# Book API Documentation

## Endpoints

### GET /books/
- Lists all books
- No authentication required
- Optional query parameter: `author` for filtering

### POST /books/create/
- Creates a new book
- Requires authentication
- Required fields: `title`, `author`

### GET /books/<id>/
- Retrieves a specific book by ID
- No authentication required

### PUT/PATCH /books/<id>/update/
- Updates a specific book
- Requires authentication and ownership (or admin status)

### DELETE /books/<id>/delete/
- Deletes a specific book
- Requires authentication and ownership (or admin status)

## Permissions
- Read operations: Open to all
- Write operations: Require authentication
- Update/Delete: Only allowed by book owner or admin users