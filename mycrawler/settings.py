# mycrawler/settings.py

FEEDS = {
    'quotes.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
        'fields': None,
        'indent': 4,
    },
}

LOG_LEVEL = 'INFO'
