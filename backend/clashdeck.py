import requests
from bs4 import BeautifulSoup
import sys
from time import time

def get_deck(player: str, trophies: int):
    url = f'https://royaleapi.com/player/search/results?q={player}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    players = soup.find_all('tr')
    for player in players:
        player_tag = player.find(class_='player_tag').text.strip('#')
        deck_url = f'https://royaleapi.com/player/{player_tag}/decks'
        deck_page = requests.get(deck_url, headers=headers)
        deck_soup = BeautifulSoup(deck_page.content, 'html.parser')
        try:
            player_profile_header_container = deck_soup.find_all(class_='player__profile_header_container')[0]
        except IndexError:
            continue
        items = player_profile_header_container.find_all(class_='item')
        player_trophies = int(items[0].text.split('/')[0])
        if player_trophies == trophies:
            deck_cards = deck_soup.find_all(class_='deck_card')[:8]
            deck = []
            for card in deck_cards:
                card_url = card['src']
                card_name = card_url.split('/')[-1].split('.')[0].replace('-', ' ').title()
                deck.append({'card_name': card_name, 'card_url': card_url})
            return deck
    return None    

if __name__ == '__main__':
    try:
        player = sys.argv[1]
        trophies = int(sys.argv[2])
    except Exception:
        print('Usage: python3 clashdeck.py <player> <trophies>')
        sys.exit(0)

    start = int(time()*1000)
    deck = get_deck(player, trophies)
    print(f'Time: {(int(time()*1000) - start)/1000}s')

    if deck is None:
        print('No player found')
        sys.exit(0)
    for card in deck:
        print(f"{card['card_name']}: {card['card_url']}")