# Copyright (C) 2024 University of Münster
# elabftw-usersync is free software; you can redistribute it and/or modify it under the terms of the MIT License; see LICENSE file for more details.
"""This module provides a class for interacting with an ElabFTW server."""

import sys
import requests
import json


class ElabFTW:
    """Class for interacting with an ElabFTW server."""

    session = None
    host_url = None

    def __init__(self, host_url, apikey, user_agent_string="elabftw_api_access"):
        """
        Initialize an instance of the ElabFTW class.

        Args:
            host_url (str): The URL of the ElabFTW server.
            apikey (str): The API key used for authentication.

        """
        print("Initializing ElabFTW class with user_agent_string: " + user_agent_string)
        # normalize self.host_url to remove everything after the last TLD ending
        # e.g. https://elabftw.example.com/login -> https://elabftw.example.com
        self.host_url = host_url.rsplit("/", 1)[0]
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": apikey, "User-Agent": user_agent_string}
        )
        self.all_users = None
        self.user_data_list = None

    def check_connection(self):
        """Check if the connection to ElabFTW is working.

        Return True if the connection is working, otherwise raises a critical error and exits the script.
        """
        try:
            resp = self.session.get(self.host_url + "/api/v2/info")
        except requests.exceptions.ConnectionError:
            print("Error connecting to ElabFTW: Connection refused")
            sys.exit(1)
        else:
            if resp.status_code != 200:
                print(
                    "Error connecting to ElabFTW: "
                    + str(resp.status_code)
                    + " "
                    + resp.text
                )
                sys.exit(1)
            else:
                return f"Connection to ElabFTW at {self.host_url} successful"

    def get_ressources(self):
        """Get all items from the ElabFTW server.

        Returns:
            list: A list of dictionaries containing the items.
        """
        resp = self.session.get(self.host_url + "/api/v2/items")
        return resp.json()

    def get_ressource_categories(self):
        """Get all categories from the ElabFTW server.

        Returns:
            list: A list of dictionaries containing the categories.
        """
        resp = self.session.get(self.host_url + "/api/v2/items_types")
        return resp.json()

    def create_ressource(
        self, category_id=None, tags=None, title=None, body=None, metadata=None
    ):
        """
        Create a new item on the ElabFTW server.

        Args:
            category_id (int, optional): The category ID of the item to be created.
            tags (list, optional): A list of tags for the item to be created.

        Returns:
            dict: A dictionary containing the data of the created item.
        """
        item_data = {"category_id": 0, "tags": []}

        if category_id is not None:
            item_data["category_id"] = category_id
        if tags is not None:
            item_data["tags"] = tags

        resp = self.session.post(self.host_url + "/api/v2/items", json=item_data)
        if resp.status_code == 201:
            id = int(resp.headers["location"].split("/")[-1])
            html_url = (f"{self.host_url}database.php?mode=view&id={id}",)
            metadata_json = json.dumps(metadata)

            data = {"title": title, "body": body, "metadata": metadata_json}

            if self.update_ressource(id, data):
                print(f"Item created: {html_url}")
                return id
        else:
            print(f"Error creating item: {resp.text}")
            return None

    def update_ressource(self, item_id, item_data):
        """
        Update an existing item on the ElabFTW server.

        Args:
            item_id (int): The ID of the item to be updated.
            item_data (dict): A dictionary containing the data of the item to be updated. Allowed keys are:
                - title (str)
                - body (str)
                - tags (list)
                - etc.

        Returns:
            dict: A dictionary containing the data of the updated item.
        """
        url = f"{self.host_url}/api/v2/items/{item_id}"
        resp = self.session.patch(url, json=item_data)
        return resp.json()
