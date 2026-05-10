import requests

def get_user_data(user_id):

    # No timeout — can hang forever

    response = requests.get(f"http://api.example.com/users/{user_id}")

    

    # No error handling

    data = response.json()

    

    # No validation of response

    return data["user"]["profile"]["details"]

def send_notification(user_id, message):

    try:

        response = requests.post(

            "http://api.example.com/notify",

            data={"user": user_id, "msg": message}

        )

    except:

        # Swallowing all exceptions silently

        pass

def bulk_fetch_users(user_ids):

    results = []

    for uid in user_ids:

        # No rate limiting — hammers the API

        results.append(get_user_data(uid))

    return results
