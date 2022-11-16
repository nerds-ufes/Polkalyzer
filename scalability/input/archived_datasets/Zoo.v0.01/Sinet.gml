graph [
  DateObtained "22/10/10"
  GeoLocation "Japan"
  GeoExtent "Country"
  SvnVersion 8043
  Customer 0
  Network "Sinet"
  Classification "Backbone"
  Creator "Topology Zoo Toolset"
  LastAccess "3/08/10"
  Transit 0
  Backbone 1
  Commercial 0
  Layer "IP"
  NetworkDate "C"
  Access 0
  Source "http://www.sinet.ad.jp/topology"
  Version "1.0"
  Testbed 0
  Developed "developed"
  label "Sinet"
  Type "REN"
  node [
    id 0
    label "Sapporo DC"
    type "Core Node"
  ]
  node [
    id 1
    label "Sendai DC"
    type "Core Node"
  ]
  node [
    id 2
    label "Fukuoka DC"
    type "Core Node"
  ]
  node [
    id 3
    label "Hiroshima DC"
    type "Core Node"
  ]
  node [
    id 4
    label "Matsuyama DC"
    type "Core Node"
  ]
  node [
    id 5
    label "Osaka DC"
    type "Core Node"
  ]
  node [
    id 6
    label "Kyoto DC"
    type "Core Node"
  ]
  node [
    id 7
    label "Nagoya DC"
    type "Core Node"
  ]
  node [
    id 8
    label "Kanazawa DC"
    type "Core Node"
  ]
  node [
    id 9
    label "Tsukuba DC"
    type "Core Node"
  ]
  node [
    id 10
    label "Tokyo DC2"
    type "Core Node"
  ]
  node [
    id 11
    label "Tokyo DC1"
    type "Core Node"
  ]
  node [
    id 12
    label "Tokyo DC3"
    type "Core Node"
  ]
  edge [
    source 0
    target 8
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 0
    target 1
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 1
    target 9
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 2
    target 3
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 2
    target 4
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 3
    target 6
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 4
    target 5
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 5
    target 6
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 5
    target 7
    LinkSpeed "40"
    LinkLabel "40Gbps"
    LinkSpeedUnits "G"
  ]
  edge [
    source 6
    target 8
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 7
    target 11
    LinkSpeed "40"
    LinkLabel "40Gbps"
    LinkSpeedUnits "G"
  ]
  edge [
    source 8
    target 10
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 9
    target 11
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 10
    target 11
    LinkLabel "10-20Gbps"
  ]
  edge [
    source 10
    target 12
    LinkLabel "1-20Gbps"
  ]
]
