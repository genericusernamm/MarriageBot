from random import choice

from discord.ext.commands import Cog

from cogs.utils.custom_bot import CustomBot


class DisownRandomText(Cog):

    def __init__(self, bot:CustomBot):
        self.bot = bot


    @staticmethod
    def valid_target(instigator, target):
        '''
        '''

        if target:
            return choice([
                f"Oof, {target.mention}, {instigator.mention} doesn't seem to want you any more...",
                f"Well, {instigator.mention}, say goodbye to {target.mention}.",
                f"Might be good news for you, {target.mention}, but you're finally free of {instigator.mention}.",
            ])
        return choice([
            "One child down, the rest to go.",
            "A sad day when a parent disowns their child...",
            "I'm sure this is very emotional for you. I'm sorry for your loss.",
        ])


    @staticmethod 
    def invalid_target(instigator, target):
        '''
        '''

        return choice([
            "They aren't your child...",
            "Have you considered disowning someone who's *actually* your child?",
            "Strangely enough you can only disown *your* children.",
        ])


def setup(bot:CustomBot):
    x = DisownRandomText(bot)
    bot.add_cog(x)
