# Running SpeedPy Base64 Tool with Tailnet Access

This document explains how to configure and run the SpeedPy Base64 tool so it's accessible via Tailnet.

## Prerequisites

1. You have a working SpeedPy installation
2. You have `tailscale` installed and configured on your machine
3. You have a Tailscale account and are logged in

## Running the Server

### Method 1: Using the provided script (Recommended)

```bash
# Make sure the script is executable
chmod +x run_dev_server.sh

# Run the development server
./run_dev_server.sh
```

This will start the Django development server on all network interfaces (`0.0.0.0:8000`), making it accessible from other devices on your network including via Tailscale.

### Method 2: Direct command

```bash
python manage.py runserver 0.0.0.0:8000
```

## Accessing via Tailnet

Once the server is running, you can access it through Tailscale:

1. The server will be accessible at `http://<your-machine-ip>:8000`
2. If you're using Tailscale's DERP infrastructure, you might also be able to reach it via:
   - `http://<your-tailscale-ip>:8000` (e.g., `http://100.100.100.100:8000`)
   - `http://<your-machine-name>.<your-tailscale-domain>:8000`

## Configuration Notes

The server is configured to:
- Listen on all network interfaces (`0.0.0.0`) 
- Use port 8000
- Be accessible from any IP address (important for Tailscale)

This configuration ensures that:
1. The application can be accessed locally via `localhost:8000`
2. The application can be accessed via your local network IP
3. The application is accessible through Tailscale

## Troubleshooting

If you're having trouble accessing the server:

1. **Check if it's running**: 
   ```bash
   ./run_dev_server.sh
   ```

2. **Verify port binding**:
   ```bash
   netstat -tlnp | grep :8000
   ```

3. **Check Tailscale status**:
   ```bash
   tailscale status
   ```

4. **Test local access first**:
   ```bash
   curl http://localhost:8000/
   ```

## Security Considerations

This development server is intended for local development and testing purposes. For production use, you should:

1. Use a proper web server (nginx/Apache) in front of Django
2. Configure HTTPS with a certificate
3. Set up proper authentication for external access
4. Consider using environment variables for sensitive configuration

The current setup is designed to work well for development and sharing with team members via Tailscale.