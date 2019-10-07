# Description:
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
  rv = 'http://'
  rvs = 'https://'
  rvw = 'http://www.'
  rvws = 'https://www.'
  www = 'www.'
  
       
  if rvws in url:
    res = url.replace(rvws, '')
    if '.' in res:
      idx = res.index('.')
      return res[0:idx]
      
  if rvs in url:
    res = url.replace(rvs, '')
    if '.' in res:
      idx = res.index('.')
      return res[0:idx]

  if rvw in url:
    res = url.replace(rvw, '')
    if '.' in res:
      idx = res.index('.')
      return res[0:idx]
  
  if www in url:
    res = url.replace(www, '')
    if '.' in res:
      idx = res.index('.')
      return res[0:idx]
  
  if rv in url:
    res = url.replace(rv, '')
    if '.' in res:
      idx = res.index('.')
      return res[0:idx]
  
  if rv not in url or www not in url or rvw not in url or rvws not in url or rvs not in url:
    if '.' in url:
      idx = url.index('.')
      return url[0:idx]
      