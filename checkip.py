import os, sys, requests, re

def CheckIP(IP):
    url = 'https://checkip.thaiware.com/?ip=' + str(IP)
    source = requests.get(url).text
    ip1 = source.find('IP Address :</strong></td>') + 63
    ip2 = source[ip1:].find('</td>') + ip1
    print('IP address\n>>' + source[ip1:ip2])
    c1 = source.find('Country :</strong></td>') + 60
    c2 = source[c1:].find('</td>') + c1
    print('Country\n>>' + source[c1:c2])
    r1 = source.find('Region Name :</strong></td>') + 64
    r2 = source[r1:].find('</td>') + r1
    print('Region name\n>>' + source[r1:r2])
    ct1 = source.find('City Name :</strong></td>') + 62
    ct2 = source[ct1:].find('</td>') + ct1
    print('City name\n>>' + source[ct1:ct2])
    isp1 = source.find('ISP :</strong></td>') + 56
    isp2 = source[isp1:].find('</td>') + isp1
    print('ISP\n>>' + source[isp1:isp2])
    lat1 = source.find('Latitude :</strong></td>') + 61
    lat2 = source[lat1:].find('</td>') + lat1
    lat = source[lat1:lat2]
    long1 = source.find('Longitude :</strong></td>') + 62
    long2 = source[long1:].find('</td>') + long1
    long = source[long1:long2]
    print('Location\n>>' + lat + ' ' + long)
    locate = [lat,long]
    return locate

def DD_DMS(DD):
    DD = float(DD)
    M, S = divmod(DD*3600, 60)
    D, M = divmod(M, 60)
    DMS = (D, M, S)
    return DMS

def GMAP(dms_lat, dms_long):
    url = ("https://www.google.co.th/maps/place/{}%C2%B0{}'{}%22N+{}%C2%B0{}'{}%22E").format(int(dms_lat[0]), int(dms_lat[1]), dms_lat[2], int(dms_long[0]), int(dms_long[1]), dms_long[2])
    source = requests.get(url).text
    s1 = source.find('"E') + 5
    s2 = source[s1:].find("'") + s1
    print('Google Maps')
    return print(source[s1:s2])

def MAP(lat, long):
    m = requests.get("https://geocode.xyz/{},{}?json=1".format(lat, long))
    script = m.json()
    print('Geocode')
    return print(script['stnumber'], script['staddress'], script['city'], script['country'], script['postal'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('checkip.py [IP address]')
    else:
        IP = sys.argv[1]
        locate = CheckIP(IP)
        dms_lat = DD_DMS(locate[0])
        dms_long = DD_DMS(locate[1])
        print('N', dms_lat, 'E', dms_long)
        GMAP(dms_lat, dms_long)
        MAP(locate[0], locate[1])
