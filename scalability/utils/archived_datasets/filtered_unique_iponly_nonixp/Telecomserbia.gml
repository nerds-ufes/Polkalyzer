graph [
  DateObtained "2/01/11"
  GeoLocation "Serbia, Montenegro"
  GeoExtent "Country+"
  Customer 0
  Network "TelecomSerbia"
  IX 0
  Provenance "Unknown"
  Access 0
  Source "http://chaisuk.wordpress.com/2008/09/21/internet-technology-nonviolent-struggle-serbia3/"
  Version "1.0"
  Type "COM"
  LastAccess "2/01/11"
  Layer "IP"
  Classification ""
  Creator "Topology Zoo Toolset"
  DateType "Historic"
  Transit 0
  Backbone 0
  Commercial 0
  NetworkDate "2005"
  label "TelecomSerbia"
  Testbed 0
  Developed 0
  SvnVersion 8123
  node [
    id 0
    label "Novi Sad"
    Latitude 45.25167
    Country "Serbia"
    type "GSR12410"
    Longitude 19.83694
  ]
  node [
    id 1
    label "Belgrade"
    Latitude 44.80401
    Country "Serbia"
    type "GSR12410"
    Longitude 20.46513
  ]
  node [
    id 2
    label "Kragujevac"
    Latitude 44.01667
    Country "Serbia"
    type "GSR12410"
    Longitude 20.91667
  ]
  node [
    id 3
    label "Nis"
    Latitude 43.32472
    Country "Serbia"
    type "GSR12410"
    Longitude 21.90333
  ]
  node [
    id 4
    label "Krusevac"
    Latitude 43.58
    Country "Serbia"
    type "GSR12410"
    Longitude 21.33389
  ]
  node [
    id 5
    label "Podgorica"
    Latitude 42.44111
    Country "Montenegro"
    type "GSR12410"
    Longitude 19.26361
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
