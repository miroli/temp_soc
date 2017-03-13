"""
How an end-user would use a scraper.
"""

from SOC import SOC

soc = SOC()
abortions = soc.get('Aborter')
resultset = abortions.fetch({
    'distribution': 'none',
    'region': 'Sweden',
    'measure': 'count',
    'year': 2014,
    'age': '20-24'
})

print(resultset)
