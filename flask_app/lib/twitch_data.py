import requests
import json
import datetime as dt

URL = 'https://api.twitch.tv/helix/'

#토큰생성
def create_token(client_id,client_secret):
    response = requests.post(f'https://id.twitch.tv/oauth2/token?client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials&scope=openid')
    res_json = json.loads(response.text)
    return res_json['access_token'],res_json['token_type']

#토큰삭제
def delete_token(client_id,token):
    response = requests.post(f'https://id.twitch.tv/oauth2/revoke?client_id={client_id}&token={token}')
    return '토큰 삭제 완료'

#ranking 순으로 데이터 추출 최대 100개
def twitch_top(acc_token,client_id,cursor=''):
    headers = {'Authorization' : 'Bearer '+acc_token,'Client-Id': client_id}
    if cursor =='':
        response = requests.get(URL+'games/top',params={'first':100},headers=headers)
    else:
        response = requests.get(URL+'games/top',params={'first':100,'after':cursor},headers=headers)
    json_data = json.loads(response.text)
    rank_list = [x['name'] for x in json_data['data']]
    next_cur = json_data['pagination']['cursor']
    return rank_list,next_cur

#rank의 page 만큼 리스트 이름 추출(page당 100개)
def twitch_rank_list(acc_token,client_id,page):
    rank_list = []
    cur = ''
    for i in range(page):
        list, cur = twitch_top(acc_token,client_id,cursor=cur)
        rank_list +=list
    return rank_list

#rapid.api에서 데이터를 추출
def game_rank_data(name,year='',month=''):
    url = "https://twitch-game-popularity.p.rapidapi.com/game"
    querystring = {"name":name}
    headers = {
        "X-RapidAPI-Host": "twitch-game-popularity.p.rapidapi.com",
        "X-RapidAPI-Key": "5c8d862c36mshd2ccf7f496aff9fp1398f3jsncee357972ad5"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)
