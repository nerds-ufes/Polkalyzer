graph [
  DateObtained "2/01/11"
  GeoLocation "Serbia, Montenegro"
  GeoExtent "Country+"
  Network "TelecomSerbia"
  Provenance "Unknown"
  Access 0
  Source "http://chaisuk.wordpress.com/2008/09/21/internet-technology-nonviolent-struggle-serbia3/"
  Version "1.0"
  DateType "Historic"
  Type "COM"
  Backbone 0
  Commercial 0
  label "TelecomSerbia"
  Customer 0
  IX 0
  LastAccess "2/01/11"
  Layer "IP"
  Classification ""
  Creator "Topology Zoo Toolset"
  Developed 0
  Transit 0
  NetworkDate "2005"
  Testbed 0
  SvnVersion 8123
  node [
    id 0
    label "Novi Sad"
    Country "Serbia"
    Longitude 19.83694
    Latitude 45.25167
    type "GSR12410"
  ]
  node [
    id 1
    label "Belgrade"
    Country "Serbia"
    Longitude 20.46513
    Latitude 44.80401
    type "GSR12410"
  ]
  node [
    id 2
    label "Kragujevac"
    Country "Serbia"
    Longitude 20.91667
    Latitude 44.01667
    type "GSR12410"
  ]
  node [
    id 3
    label "Nis"
    Country "Serbia"
    Longitude 21.90333
    Latitude 43.32472
    type "GSR12410"
  ]
  node [
    id 4
    label "Krusevac"
    Country "Serbia"
    Longitude 21.33389
    Latitude 43.58
    type "GSR12410"
  ]
  node [
    id 5
    label "Podgorica"
    Country "Montenegro"
    Longitude 19.26361
    Latitude 42.44111
    type "GSR12410"
  ]
  edge [
    source 0
    target 1
    LinkLabel "DTP-Ring 2.5 Gbit/s"
  ]
  edge [
    source 0
    target 5
    LinkLabel "DTP-Ring 2.5 Gbit/s"
  ]
  edge [
    source 1
    target 2
    LinkLabel "DTP-Ring 2.5 Gbit/s"
  ]
  edge [
    source 2
    target 3
    LinkLabel "DTP-Ring 2.5 Gbit/s"
  ]
  edge [
    source 3
    target 4
    LinkLabel "DTP-Ring 2.5 Gbit/s"
  ]
  edge [
    source 4
    target 5
    LinkLabel "DTP-Ring 2.5 Gbit/s"
  ]
]
