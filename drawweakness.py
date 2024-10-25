import httpx
import numpy as np
import asyncio

deck_id = 4327199
all_basic_weaknesses = [['Amnesia', '01096', 'Core Set', 'https://arkhamdb.com/card/01096'], ['Paranoia', '01097', 'Core Set', 'https://arkhamdb.com/card/01097'], ['Haunted', '01098', 'Core Set', 'https://arkhamdb.com/card/01098'], ['Psychosis', '01099', 'Core Set', 'https://arkhamdb.com/card/01099'], ['Hypochondria', '01100', 'Core Set', 'https://arkhamdb.com/card/01100'], ['Mob Enforcer', '01101', 'Core Set', 'https://arkhamdb.com/card/01101'], ['Silver Twilight Acolyte', '01102', 'Core Set', 'https://arkhamdb.com/card/01102'], ['Stubborn Detective', '01103', 'Core Set', 'https://arkhamdb.com/card/01103'], ['Indebted', '02037', 'The Dunwich Legacy', 'https://arkhamdb.com/card/02037'], ['Internal Injury', '02038', 'The Dunwich Legacy', 'https://arkhamdb.com/card/02038'], ['Chronophobia', '02039', 'The Dunwich Legacy', 'https://arkhamdb.com/card/02039'], ['Overzealous', '03040', 'The Path to Carcosa', 'https://arkhamdb.com/card/03040'], ['Drawing the Sign', '03041', 'The Path to Carcosa', 'https://arkhamdb.com/card/03041'], ['The Thing That Follows', '03042', 'The Path to Carcosa', 'https://arkhamdb.com/card/03042'], ['Dark Pact', '04038', 'The Forgotten Age', 'https://arkhamdb.com/card/04038'], ['Doomed', '04040', 'The Forgotten Age', 'https://arkhamdb.com/card/04040'], ['The 13th Vision', '05041', 'The Circle Undone', 'https://arkhamdb.com/card/05041'], ['The Tower • XVI', '05042', 'The Circle Undone', 'https://arkhamdb.com/card/05042'], ['Self-Centered', '06035', 'The Dream-Eaters', 'https://arkhamdb.com/card/06035'], ['Kleptomania', '06036', 'The Dream-Eaters', 'https://arkhamdb.com/card/06036'], ['Narcolepsy', '06037', 'The Dream-Eaters', 'https://arkhamdb.com/card/06037'], ['Your Worst Nightmare', '06038', 'The Dream-Eaters', 'https://arkhamdb.com/card/06038'], ['Accursed Follower', '07038', 'The Innsmouth Conspiracy', 'https://arkhamdb.com/card/07038'], ['Dread Curse', '07039', 'The Innsmouth Conspiracy', 'https://arkhamdb.com/card/07039'], ['Day of Reckoning', '07040', 'The Innsmouth Conspiracy', 'https://arkhamdb.com/card/07040'], ['Arm Injury', '08130', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08130'], ['Leg Injury', '08131', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08131'], ['Panic', '08132', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08132'], ['Stupor', '08133', 'Edge of the Earth Investigator Expansion', 'https://arkhamdb.com/card/08133'], ['Lurker in the Dark', '09124', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09124'], ['Quantum Paradox', '09125', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09125'], ['Pay Your Due', 
'09126', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09126'], ['Ectoplasmic Horror', '09127', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09127'], ['Underprepared', '09128', 'The Scarlet Keys Investigator Expansion', 'https://arkhamdb.com/card/09128'], ['Maimed Hand', '10135', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10135'], ['Back Injury', '10136', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10136'], ['The Silver Moth', '10137', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10137'], ['Vow of Drzytelech', '10138', 'The Feast of Hemlock Vale Investigator Expansion', 'https://arkhamdb.com/card/10138'], ['Through the Gates', '51011', 'Return to the Dunwich Legacy', 'https://arkhamdb.com/card/51011'], ['Unspeakable Oath', '52011', 'Return to the Path to Carcosa', 'https://arkhamdb.com/card/52011'], ['Unspeakable Oath', '52012', 'Return to the Path to Carcosa', 'https://arkhamdb.com/card/52012'], ['Unspeakable Oath', '52013', 'Return to the Path to Carcosa', 'https://arkhamdb.com/card/52013'], ['Dendromorphosis', '53012', 'Return to the Forgotten Age', 'https://arkhamdb.com/card/53012'], ['Offer You Cannot Refuse', '53013', 'Return to the Forgotten Age', 'https://arkhamdb.com/card/53013'], ['Damned', '54014', 'Return to the Circle Undone', 'https://arkhamdb.com/card/54014'], ['The Devil • XV', '54015', 'Return to the Circle Undone', 'https://arkhamdb.com/card/54015'], ['Self-Destructive', '60104', 'Nathaniel Cho', 'https://arkhamdb.com/card/60104'], ['Obsessive', '60204', 'Harvey Walters', 'https://arkhamdb.com/card/60204'], ['Reckless', '60304', 'Winifred Habbamock', 'https://arkhamdb.com/card/60304'], ['Nihilism', '60404', 'Jacqueline Fine', 'https://arkhamdb.com/card/60404'], ['Atychiphobia', '60504', 'Stella Clark', 'https://arkhamdb.com/card/60504']]
class_expansions = ['The Forgotten Age', 'The Dream-Eaters', 'Return to the Forgotten Age', 'Stella Clark', 'The Scarlet Keys Investigator Expansion', 'Winifred Habbamock', 'Core Set', 'The Circle Undone', 'Harvey Walters', 'Return to the Dunwich Legacy', 'The Dunwich Legacy', 'Edge of the Earth Investigator Expansion', 'Return to the Path to Carcosa', 'The Feast of Hemlock Vale Investigator Expansion', 'Jacqueline Fine', 'Nathaniel Cho', 'Return to the Circle Undone', 'The Innsmouth Conspiracy', 'The Path to Carcosa']

async def get_deck():
    async with httpx.AsyncClient(base_url="https://arkhamdb.com/") as client:
        decklist = await client.get(f"/api/public/deck/{deck_id}.json?_format=json")
    if decklist.status_code == 200:
        return decklist.json()
    else:
        return 'Failed'

async def load_weakness():
    decklist = await get_deck()
    weaknesses_dict = decklist['slots']
    weaknesses = []
    for value in weaknesses_dict.items():
        weaknesses.append(value[0])
    return weaknesses

async def filtered_weaknesses():
    weaknesses = await load_weakness()
    weakness_name_id_set_link = [[]]
    for name in weaknesses:
        async with httpx.AsyncClient(base_url="https://arkhamdb.com/") as client:
            card = await client.get(f"api/public/card/{name}.json?_format=json")
        if card.status_code == 200:
            temp = []
            temp.append((card.json())['name'])
            temp.append((card.json())['code'])
            temp.append((card.json())['pack_name'])
            temp.append((card.json())['url'])
            weakness_name_id_set_link.append(temp)
        else:
            return 'Failed'  
    return weakness_name_id_set_link  

async def draw_weakness_values(draws):
    weakness = await load_weakness()
    drawn = np.random.choice(np.arange(0, len(weakness) + 1), size=draws, replace=False)
    cards = []
    for d in drawn:
        cards.append(weakness[d])
    return cards
    
async def load_drawn_cards(draws):
    cards = await draw_weakness_values(draws)
    names = []
    for c in cards:
        async with httpx.AsyncClient(base_url="https://arkhamdb.com/") as client:
            card = await client.get(f"api/public/card/{c}.json?_format=json")
        if card.status_code == 200:
            names.append(card.json())
        else:
            return 'Failed'
    return names

async def load_names(draws):
    cards = await load_drawn_cards(draws)
    card_name = []
    for card in cards:
        card_name.append(card['name'])
    return card_name

async def load_weburl(draws):
    cards = await load_drawn_cards(draws)
    card_urls = []
    for card in cards:
        card_urls.append(card['url'])
    return card_urls

def filter_expansion():
    basic_weaknesses = [card for card in all_basic_weaknesses if card[2] in class_expansions]
    return basic_weaknesses

def draw(cards, players):
    playercards = []
    drawn = np.random.choice(np.arange(0, len(all_basic_weaknesses)), size=cards*players, replace=False)
    for player in range(players):
        temp = []
        for card in range(cards):
            draw = drawn[(player * cards) + card]
            temp.append(all_basic_weaknesses[draw])
        playercards.append(temp)
    return playercards
        




if __name__ == "__main__":
    print("Welcome to weakness selector, do you wish to use all campaigns, including return to's?")
    a = input("Type yes or y to accept, or anything else to filter something out:")
    if (a.lower() != "y") or (a.lower() != "yes"):
        print("Please select which campaigns to not include")
        print("Available campaigns pool:")
        for camp in range(len(class_expansions)):
            print(f'{camp}. ' + class_expansions[camp])
        r = input("Format is 1,2,3,4,5,6,7,8,9...: ")
        remove = r.split(',')
        rem = [int(a) for a in remove]
        rem.sort()
        rem.reverse()
        for item in rem:
            class_expansions.pop(item)
        all_basic_weaknesses = filter_expansion()
    print("How many weaknesses do you wish to draw, and for how many players?")
    weak = input("Format is 3,2: ")
    weak = weak.split(",")
    cards = int(weak[0])
    players = int(weak[1])
    card_draw = draw(cards,players)
    for player in range(players):
        print(f'Player {player + 1}  :  {card_draw[player]}')
    










