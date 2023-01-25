graph [
  DateObtained "22/03/11"
  GeoLocation "Europe"
  GeoExtent "Continent"
  Network "NORDU"
  Provenance "Primary"
  Access 0
  Source "https://wiki.nordu.net/display/NORDUwiki/The+History+of+NORDUnet"
  Version "1.0"
  DateType "Historic"
  Type "REN"
  Backbone 1
  Commercial 0
  label "nordu_1989"
  Customer 0
  IX 0
  LastAccess "22/03/11"
  Note "CERT + NEWS + DNS Speeds from 'The History of Nordunet', pg 45"
  Layer "IP"
  Classification "Backbone Customer? Transit?"
  Creator "Topology Zoo Toolset"
  Developed 1
  Transit 0
  NetworkDate "1989"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Trondheim"
    Country "Norway"
    Longitude 10.39506
    Internal 1
    Latitude 63.43049
  ]
  node [
    id 1
    label "Stockholm"
    Country "Sweden"
    Longitude 18.0649
    Internal 1
    Latitude 59.33258
  ]
  node [
    id 2
    label "Helsinki"
    Country "Finland"
    Longitude 24.93545
    Internal 1
    Latitude 60.16952
  ]
  node [
    id 3
    label "Copenhagen"
    Country "Denmark"
    Longitude 12.56553
    Internal 1
    Latitude 55.67594
  ]
  node [
    id 4
    label "Reykjavik"
    Country "Iceland"
    Longitude -21.89541
    Internal 1
    Latitude 64.13548
  ]
  node [
    id 5
    label "EUROPE"
    Internal 0
  ]
  node [
    id 6
    label "USA"
    Internal 0
  ]
  edge [
    source 0
    target 1
    LinkSpeed "64"
    LinkNote " it/s"
    LinkSpeedUnits "K"
    LinkLabel "64 Kbit/s"
    LinkSpeedRaw 64000.0
  ]
  edge [
    source 1
    target 2
    LinkSpeed "64"
    LinkNote " it/s"
    LinkSpeedUnits "K"
    LinkLabel "64 Kbit/s"
    LinkSpeedRaw 64000.0
  ]
  edge [
    source 1
    target 3
    LinkSpeed "64"
    LinkNote " it/s"
    LinkSpeedUnits "K"
    LinkLabel "64 Kbit/s"
    LinkSpeedRaw 64000.0
  ]
  edge [
    source 1
    target 5
    LinkSpeed "64"
    LinkNote " it/s"
    LinkSpeedUnits "K"
    LinkLabel "64 Kbit/s"
    LinkSpeedRaw 64000.0
  ]
  edge [
    source 1
    target 6
    LinkSpeed "64"
    LinkNote " it/s"
    LinkSpeedUnits "K"
    LinkLabel "64 Kbit/s"
    LinkSpeedRaw 64000.0
  ]
  edge [
    source 3
    target 4
    LinkLabel "9600 bit/s"
  ]
]
