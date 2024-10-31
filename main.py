import requests
import json

class NerimityBot:
    """
    NerimityBot API client for managing and controlling bots within Nerimity.
    """

    BASE_URL = "https://nerimity.com/api"
    
    def __init__(self, token: str):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def _request(self, method: str, endpoint: str, data=None):
        """Helper method to make an API request."""
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return None
        return response.json()

    # Server Management
    def get_server(self, server_id: str):
        """Retrieve server details."""
        return self._request("GET", f"servers/{server_id}")

    def create_channel(self, server_id: str, name: str, type: int):
        """Create a new channel in the specified server."""
        data = {"name": name, "type": type}
        return self._request("POST", f"servers/{server_id}/channels", data)

    def delete_channel(self, server_id: str, channel_id: str):
        """Delete a channel from the specified server."""
        return self._request("DELETE", f"servers/{server_id}/channels/{channel_id}")

    # Role Management
    def create_role(self, server_id: str, name: str, color: str = "#000000"):
        """Create a new role with a specified color."""
        data = {"name": name, "hexColor": color}
        return self._request("POST", f"servers/{server_id}/roles", data)

    def delete_role(self, server_id: str, role_id: str):
        """Delete a role from the server."""
        return self._request("DELETE", f"servers/{server_id}/roles/{role_id}")

    # Member Management
    def update_member_roles(self, server_id: str, user_id: str, role_ids: list):
        """Update roles of a member in the server."""
        data = {"roleIds": role_ids}
        return self._request("PATCH", f"servers/{server_id}/members/{user_id}", data)

    # Invite Management
    def create_invite(self, server_id: str):
        """Create an invite link for the server."""
        return self._request("POST", f"servers/{server_id}/invites")

    def delete_invite(self, server_id: str, code: str):
        """Delete an invite link from the server."""
        return self._request("DELETE", f"servers/{server_id}/invites/{code}")
