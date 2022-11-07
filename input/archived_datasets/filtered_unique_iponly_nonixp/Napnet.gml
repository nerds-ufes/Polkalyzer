graph [
  DateObtained "14/01/11"
  GeoLocation "USA"
  GeoExtent "Country"
  Customer 0
  Network "NapNet"
  IX 0
  Provenance "Secondary"
  Note "ATM only? No information"
  Source "http://www.nthelp.com/images/napnet.jpg"
  Version "1.0"
  Type "COM"
  LastAccess "14/01/11"
  Access 0
  Layer "IP"
  Classification ""
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 0
  Commercial 0
  NetworkDate "2011-01"
  label "napnet"
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
    label "San Jose"
    Latitude 37.33939
    Country "United States"
    Longitude -121.89496
  ]
  node [
    id 2
    label "Minneapolis"
    Latitude 44.97997
    Country "United States"
    Longitude -93.26384
  ]
  node [
    id 3
    label "Chicago"
    Latitude 41.85003
    Country "United States"
    Longitude -87.65005
  ]
  node [
    id 4
    label "Vienna"
    Latitude 38.90122
    Country "United States"
    Longitude -77.26526
  ]
  node [
    id 5
    label "Dallas"
    Latitude 32.78306
    Country "United States"
    Longitude -96.80667
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
    LinkLabel "45 Mbps DS-3"
    LinkNote "45 Mbps "
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
