graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Network "NapNet"
  Provenance "Secondary"
  Access 0
  Source "http://www.nthelp.com/images/napnet.jpg"
  Version "1.0"
  DateType "Current"
  Type "COM"
  Backbone 0
  Commercial 0
  label "napnet"
  Customer 0
  IX 0
  LastAccess "14/01/11"
  Note "ATM only? No information"
  Layer "IP"
  Classification ""
  Creator "Topology Zoo Toolset"
  Developed 1
  Transit 0
  NetworkDate "2011-01"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Seattle"
    Country "United States"
    Longitude -122.33207
    Latitude 47.60621
  ]
  node [
    id 1
    label "San Jose"
    Country "United States"
    Longitude -121.89496
    Latitude 37.33939
  ]
  node [
    id 2
    label "Minneapolis"
    Country "United States"
    Longitude -93.26384
    Latitude 44.97997
  ]
  node [
    id 3
    label "Chicago"
    Country "United States"
    Longitude -87.65005
    Latitude 41.85003
  ]
  node [
    id 4
    label "Vienna"
    Country "United States"
    Longitude -77.26526
    Latitude 38.90122
  ]
  node [
    id 5
    label "Dallas"
    Country "United States"
    Longitude -96.80667
    Latitude 32.78306
  ]
  edge [
    source 0
    target 1
  ]
  edge [
    source 0
    target 3
  ]
  edge [
    source 1
    target 3
  ]
  edge [
    source 1
    target 4
    LinkType "DS-3"
    LinkNote "45 Mbps "
    LinkLabel "45 Mbps DS-3"
  ]
  edge [
    source 2
    target 3
  ]
  edge [
    source 3
    target 4
  ]
  edge [
    source 3
    target 5
  ]
]
