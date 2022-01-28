import requests

class API:
    def get_video_shows(self, api_key):
        headers = {'user-agent': 'Giant_Backlog'}
        response = requests.get(
            (
                f'https://www.giantbomb.com/api/video_shows/?api_key={api_key}&format=json'
                f'&field_list=id,guid,deck,title,premium,api_videos_url'
            ),
            headers=headers
        )
        
        return response