graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Customer 0
  Network "GetNet"
  IX 0
  Provenance "Secondary"
  Note "No contemporary info. Was an ISP in 97 with reach but now appears to be Phoenix only? No buyout info"
  Source "http://www.nthelp.com/images/getnet.jpg"
  Version "1.0"
  Type "COM"
  LastAccess "14/01/11"
  Access 1
  Layer "IP"
  Classification "Access"
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 0
  Commercial 0
  NetworkDate "2011-01"
  label "getnet"
  Testbed 0
  Developed 1
  SvnVersion 8123
  node [
    id 0
    label "Seattle"
    Latitude 47.60621
    Country "United States"
    Longitude -122.33207
  ]
  node [
    id 1
    label "Santa Clara"
    Latitude 37.35411
    Country "United States"
    Longitude -121.95524
  ]
  node [
    id 2
    label "Phoenix"
    Latitude 33.44838
    Country "United States"
    Longitude -112.07404
  ]
  node [
    id 3
    label "Tucson"
    Latitude 32.22174
    Country "United States"
    Longitude -110.92648
  ]
  node [
    id 4
    label "Washington, DC"
    Latitude 38.89511
    Country "United States"
    Longitude -77.03637
  ]
  node [
    id 5
    label "Baltimore"
    Latitude 39.29038
    Country "United States"
    Longitude -76.61219
  ]
  node [
    id 6
    label "Pittsburgh"
    Latitude 40.44062
    Country "United States"
    Longitude -79.99589
  ]
  edge [
    source 0
    target 1
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 1
    target 2
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 1
    target 4
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 1
    target 6
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 2
    target 3
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 2
    target 4
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 4
    target 5
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
  edge [
    source 5
    target 6
    LinkType "DS-3"
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
  ]
]
