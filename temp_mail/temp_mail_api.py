import requests


class TempUserEmail:
    email_api_url = "https://post-shift.ru/api.php"
    hash_value = "0f750fb4ceae7eae0615360ae1155869"

    def create_email_box(self):
        response = requests.get(self.email_api_url, params={'action': 'new', 'hash': self.hash_value}, verify=False)
        json_response = response.json()
        return json_response

    def get_mails_list(self, key: str):
        response = requests.get(self.email_api_url, params={'action': 'getlist', 'hash': self.hash_value, 'key': key}, verify=False)
        json_response = response.json()
        return json_response

    def get_first_mail(self, mail_list):
        return mail_list[0]

    def get_mail_msg(self, mail_id: int, key: str):
        response = requests.get(self.email_api_url, params={'action': 'getmail', 'hash': self.hash_value,
                                                            'key': key, 'id': mail_id}, verify=False)
        json_response = response.json()
        return json_response['message']
