graph [
  DateObtained ""
  GeoLocation "Fife and Tayside, UK"
  GeoExtent "Region"
  Customer 0
  Network "FatMan"
  IX 0
  Provenance "Primary"
  Note "ATM-based - JANET local provider"
  Source "http://www.fatman.net.uk/"
  Version "1.0"
  Type "REN"
  LastAccess "21/01/11"
  Access 0
  Layer "IP"
  Classification "Backbone  "
  Creator "Topology Zoo Toolset"
  DateType "Current"
  Transit 0
  Backbone 1
  Commercial 0
  NetworkDate "2011-01"
  label "fatman"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Glasgow"
    Internal 1
    Latitude 55.86515
    Country "United Kingdom"
    type "Orange Node"
    Longitude -4.25763
  ]
  node [
    id 1
    label "Leeds"
    Internal 1
    Latitude 53.79648
    Country "United Kingdom"
    type "Orange Node"
    Longitude -1.54785
  ]
  node [
    id 2
    label "RNEP1"
    Internal 1
    Latitude 56.5
    Country "United Kingdom"
    type "Purple Node"
    Longitude -2.96667
  ]
  node [
    id 3
    label "RNEP2"
    Internal 1
    Latitude 56.5
    Country "United Kingdom"
    type "Purple Node"
    Longitude -2.96667
  ]
  node [
    id 4
    label "University of Abertay Dundee"
    Internal 1
    type "Blue Node"
  ]
  node [
    id 5
    label "University of Dundee"
    Internal 1
    type "Blue Node"
  ]
  node [
    id 6
    label "University of St Andrews"
    Internal 1
    type "Blue Node"
  ]
  node [
    id 7
    label "Elmwood College"
    Internal 1
    type "Green Node"
  ]
  node [
    id 8
    label "Dundee College"
    Internal 1
    type "Green Node"
  ]
  node [
    id 9
    label "Angus College"
    Internal 1
    type "Green Node"
  ]
  node [
    id 10
    label "Kirkcaldy"
    Internal 1
    Latitude 56.11667
    Country "United Kingdom"
    type "Purple Node"
    Longitude -3.16667
  ]
  node [
    id 11
    label "UoD Fife Campus"
    Internal 1
    type "Blue Node"
  ]
  node [
    id 12
    label "Carnegie College"
    Internal 1
    type "Green Node"
  ]
  node [
    id 13
    label "Adam Smith College"
    Internal 1
    type "Green Node"
  ]
  node [
    id 18
    label ""
    hyperedge 1
    Internal 1
  ]
  node [
    id 19
    label "Janet and Internet"
    Internal 0
  ]
  node [
    id 20
    label "Janet and Internet"
    Internal 0
  ]
  edge [
    source 0
    target 1
    LinkLabel "Orange Link"
  ]
  edge [
    source 0
    target 3
    LinkLabel "Orange/Purple Link"
  ]
  edge [
    source 0
    target 20
    LinkLabel "Orange Link"
  ]
  edge [
    source 1
    target 2
    LinkLabel "Orange/Purple Link"
  ]
  edge [
    source 1
    target 19
    LinkLabel "Orange Link"
  ]
  edge [
    source 2
    target 3
    LinkLabel "Purple Link"
  ]
  edge [
    source 2
    target 4
    LinkLabel "Blue Link"
  ]
  edge [
    source 2
    target 5
    LinkLabel "Blue Link"
  ]
  edge [
    source 2
    target 6
    LinkLabel "Blue Link"
  ]
  edge [
    source 2
    target 7
    LinkLabel "Green Link"
  ]
  edge [
    source 2
    target 8
    LinkLabel "Green Link"
  ]
  edge [
    source 2
    target 9
    LinkLabel "Green Link"
  ]
  edge [
    source 2
    target 18
  ]
  edge [
    source 3
    target 4
    LinkLabel "Blue Link"
  ]
  edge [
    source 3
    target 5
    LinkLabel "Blue Link"
  ]
  edge [
    source 3
    target 6
    LinkLabel "Blue Link"
  ]
  edge [
    source 3
    target 18
    LinkLabel "Purple Link"
  ]
  edge [
    source 10
    target 18
    LinkLabel "Purple Link"
  ]
  edge [
    source 10
    target 11
    LinkLabel "Blue Link"
  ]
  edge [
    source 10
    target 12
    LinkLabel "Green Link"
  ]
  edge [
    source 10
    target 13
    LinkLabel "Green Link"
  ]
]
