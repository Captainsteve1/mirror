import cloudscraper

from bot2.helpers.functions import api_checker


async def telegraph_paste(res):
    dom = await api_checker()
    api = f"{dom}/paste"
    client = cloudscraper.create_scraper(allow_brotli=False)
    try:
        resp = client.post(api, json={"type": "telegraph_paste", "text": res})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link!"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]
