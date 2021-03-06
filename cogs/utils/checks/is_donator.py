from discord.ext.commands import CheckFailure, Context, check


class IsNotDonator(CheckFailure):
    '''Catch-all for not donating errors'''
    pass


class IsNotPatreon(IsNotDonator): pass
class IsNotPaypal(IsNotDonator): pass


async def is_patreon_predicate(bot, user):
    '''Returns True if the user is a Patreon sub'''

    support_invite = await bot.fetch_invite(bot.config['guild'])
    support_guild = support_invite.guild 
    patreon_sub_role = support_guild.get_role(bot.config['patreon_sub_role'])
    try:
        if patreon_sub_role in support_guild.get_member(user.id).roles:
            return True
    except Exception:
        pass
    return False


def is_patreon():
    '''The check to make sure that a given author is a Patreon sub'''

    async def predicate(ctx:Context):
        if await is_patreon_predicate(ctx.bot, ctx.author):
            return True 
        raise IsNotPatreon()
    return check(predicate)
