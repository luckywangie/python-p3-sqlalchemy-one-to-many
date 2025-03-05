#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()

    # Query a game and its associated reviews
    game = session.query(Game).first()
    print(f'Game: {game}')
    print('Reviews:')
    for review in game.reviews:
        print(f'- {review}')
