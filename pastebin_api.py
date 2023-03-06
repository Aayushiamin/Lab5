import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = '9afaEHHVU4wyEEv1PjQRCMUQG2PRZhJR'

def main():
    paste_url = post_new_paste('whatever paste', 'a bunch of crap')
    pass


def post_new_paste(title, body_text, expiration='1M', listed=True):
    """ Creates a new public PasteBin paste 

    Args: 
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): How long the paste will last. (see https://pastebin.com/doc_api) Defaults to '10M'
        Listed (bool, optional): Whether the paste is listed or not. Defaults to True.

    Returns:
        str: URL of the new paste. None if unsuccessful.
    
    """
    # Create Dictionary of Parameter Values
    params = {

        
        'api_dev_key': DEVELOPER_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1

    }

    # Send the POST requests to the PAsteBin API 
    print("posting new paste to pasteBin...", end='')

    resp_msg = requests.post(API_POST_URL, data=params)


    # Check if paste was created successfully or not 
    if resp_msg.status_code == requests.codes.ok:
        print('Success')
        print(f"URL of new paste: {resp_msg.text}")
        return resp_msg.text

    else:
        print("Failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == "__main__":
    main()