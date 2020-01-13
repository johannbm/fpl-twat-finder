import aiohttp
import asyncio
from fpl import FPL

async def get_leauge_standings(leauge_id):
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login()
        classic_league = await fpl.get_classic_league(leauge_id)
        standings = await classic_league.get_standings()
    return  standings