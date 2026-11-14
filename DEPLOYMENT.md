# Deployment Instructions

This document explains how to deploy this SpeedPy Base64 Tool application.

## GitHub Repository

The source code is hosted at:
https://github.com/appliku/speedpy-base64-tool

## Deployment with Appliku

To deploy this application to Appliku, you'll need to:

1. **Ensure you have the necessary permissions** on the appliku team
2. **Create an application manually through the Appliku dashboard** or use the CLI:

### Using the Appliku CLI (if permissions are available):

```bash
# Create application from GitHub repository
appliku apps create github \
  -t appliku \
  -n base64tool \
  -b master \
  --cluster 1 \
  appliku/speedpy-base64-tool
```

### Manual Deployment Steps:

1. Log in to the Appliku dashboard at https://dashboard.appliku.com
2. Navigate to your team (appliku)
3. Click "Create Application"
4. Select "From GitHub"
5. Choose repository: `appliku/speedpy-base64-tool`
6. Set application name: `base64tool`
7. Set branch: `master` 
8. Select cluster (or server) - use the Hetzner box if available
9. Complete the setup

## Configuration Requirements

The application requires the following environment variables to be configured:

- `SECRET_KEY` (required)
- `DATABASE_URL` (automatically provided by Appliku)
- `REDIS_URL` (automatically provided by Appliku) 
- `ALLOWED_HOSTS` (automatically configured from domains)
- `ADMIN_URL` (set to a secure path like `/admin/`)
- `EMAIL_PROVIDER` (configure your email provider)
- `DEFAULT_FROM_EMAIL` (set to your sending address)

## Docker Configuration

This project uses the standard SpeedPy Docker configuration:

- Uses Python 3.14 with uv for dependency management
- Node.js 25.6 for frontend builds
- PostgreSQL database (automatically configured via DATABASE_URL)
- Redis cache (automatically configured via REDIS_URL)
- Tailwind CSS compilation

## Deployment Process

After creating the application, follow these steps:

1. **Initial deployment**: Push to GitHub master branch triggers automatic deployment
2. **Environment variables**: Configure necessary environment variables in the Appliku dashboard
3. **Domain configuration**: Add custom domains if needed
4. **Database migration**: Run migrations after deployment (if needed)
5. **Testing**: Verify the application is accessible

## Development Setup

For local development, you can use:

```bash
# Run the development server
./run_dev_server.sh

# Or directly with Django
python manage.py runserver 0.0.0.0:8000
```

The application will be accessible at http://localhost:8000/ and will work with your Tailscale network.