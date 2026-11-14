# SpeedPy Base64 Tool

This is a customized SpeedPy project that replaces the default welcome page with a simple Base64 encoder/decoder tool.

## Features

- Simple two-textarea interface for Base64 encoding and decoding
- Encode text to Base64 format
- Decode Base64 back to plain text
- Clear functionality to reset the form
- Responsive design using SpeedPy UI components
- Real-time conversion with AJAX requests

## Usage

1. Enter text in the input textarea
2. Click "Encode to Base64" to convert to Base64 format
3. Click "Decode from Base64" to convert back to plain text
4. Use "Clear All" to reset both textareas

## Running the Development Server

To make the development server accessible via tailnet or other networks, use:

```bash
./run_dev_server.sh
```

Or run directly with:
```bash
python manage.py runserver 0.0.0.0:8000
```

This will bind the server to all network interfaces, making it accessible from external networks.

## Deployment

This project is ready for deployment to Appliku with the following configuration:

### GitHub Repository
The source code is hosted at: https://github.com/appliku/speedpy-base64-tool

### Deployment Process
To deploy this application to Appliku:

1. **GitHub Setup**: The repository is already configured and pushed to GitHub
2. **Application Creation**: Create a new application in Appliku dashboard:
   - Select "From GitHub"
   - Repository: `appliku/speedpy-base64-tool`
   - Branch: `master`
   - Application name: `base64tool`
3. **Environment Configuration**: Set required environment variables:
   - `SECRET_KEY` (required)
   - `ADMIN_URL` (e.g., `/admin/`)
   - `EMAIL_PROVIDER` (configure your email provider)
   - `DEFAULT_FROM_EMAIL` (set to your sending address)

### Docker Configuration
This project uses the standard SpeedPy Docker configuration:
- Python 3.14 with uv for dependency management
- Node.js 25.6 for frontend builds
- PostgreSQL database (automatically configured via DATABASE_URL)
- Redis cache (automatically configured via REDIS_URL)
- Tailwind CSS compilation

### Deployment Scripts
- `run_dev_server.sh` - Run development server on all interfaces
- `deploy_to_appliku.sh` - Helper script for deployment preparation

## Project Structure Changes

The following changes were made to the original SpeedPy structure:

### Views
- Added `Base64ToolView` in `mainapp/views/base64_tool.py`
- Modified `WelcomeToSpeedPyView` in `mainapp/views/welcome.py` to use a simplified welcome page
- Added `DemoWelcomeView` in `mainapp/views/demo_welcome.py` for future demo functionality

### Templates
- Created `templates/mainapp/base64_tool.html` for the main Base64 tool interface
- Created `templates/mainapp/simple_welcome.html` for the simplified welcome page
- Created `templates/mainapp/welcome_demo.html` for the original welcome page (can be restored)

### URLs
- Updated `mainapp/urls.py` to include the Base64 tool URL pattern
- Updated `project/urls.py` to make the Base64 tool the default page

## Customization Options

To restore the original SpeedPy welcome page, you can:

1. Replace the `WelcomeToSpeedPyView` in `mainapp/views/welcome.py` with the original version
2. Update the URL configuration in `project/urls.py` to point back to the demo welcome view:
   ```python
   path("", views.DemoWelcomeView.as_view(), name="welcome"),
   ```
3. Or modify `templates/mainapp/simple_welcome.html` to include links to the various SpeedPy features

## API Endpoints

The Base64 tool also provides a JSON API for programmatic access:

- POST `/base64-tool/` with JSON body:
  ```json
  {
    "action": "encode|decode",
    "text": "your text here"
  }
  ```

Response will be:
```json
{
  "result": "encoded or decoded text",
  "action": "encode|decode"
}
```

## Development

To run the development server:
```bash
./run_dev_server.sh
```

The Base64 tool will be available at the root URL (http://localhost:8000/).

For access via tailnet, you can use:
```bash
# First run the server with network binding
./run_dev_server.sh

# Then in another terminal, set up a tunnel (if using tailscale)
tailscale up
```

For access via tailnet, you can use:
```bash
# First run the server with network binding
./run_dev_server.sh

# Then in another terminal, set up a tunnel (if using tailscale)
tailscale up
```