import geo 
ip = geo.getIp()
print(ip)

country = geo.getCountry(ip, 'plain')
print(country)

country = geo.getCountry(ip, 'json')
print(country)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpDetails('192.168.43.1')
geo.showCountryDetails('192.168.43.1')