graph [
  DateObtained "21/10/10"
  GeoLocation "Japan, USA"
  GeoExtent "Country+"
  SvnVersion 8043
  Customer 1
  Network "IIJ"
  Classification "Backbone Customer Transit?"
  Creator "Topology Zoo Toolset"
  LastAccess "3/08/10"
  Transit 0
  Backbone 1
  Commercial 0
  Layer "IP"
  NetworkDate "22/10/10"
  Access 0
  Source "http://www.iij.ad.jp/en/network/backbone/index.html"
  Version "1.0"
  Testbed 0
  Developed "developed"
  label "IIJ"
  Type "COM"
  node [
    id 0
    label "Chiba"
    Internal 1
  ]
  node [
    id 1
    label "Tokyo"
    Internal 1
  ]
  node [
    id 2
    label "Toyama"
    Internal 1
  ]
  node [
    id 3
    label "Kanazawa"
    Internal 1
  ]
  node [
    id 4
    label "Hamamatsu"
    Internal 1
  ]
  node [
    id 5
    label "Osaka"
    Internal 1
  ]
  node [
    id 6
    label "Okayama"
    Internal 1
  ]
  node [
    id 7
    label "Hiroshima"
    Internal 1
  ]
  node [
    id 8
    label "Okinawa"
    Internal 1
  ]
  node [
    id 9
    label "Sappora DC"
    Internal 1
  ]
  node [
    id 10
    label "Sendai DC"
    Internal 1
  ]
  node [
    id 11
    label "Saitama DC"
    Internal 1
  ]
  node [
    id 12
    label "Tokyo DC1"
    Internal 1
  ]
  node [
    id 13
    label "Tokyo DC2"
    Internal 1
  ]
  node [
    id 14
    label "Shibuya DC"
    Internal 1
  ]
  node [
    id 15
    label "Ikekuboro DC"
    Internal 1
  ]
  node [
    id 16
    label "Nerima DC"
    Internal 1
  ]
  node [
    id 17
    label "Yokohama DC1"
    Internal 1
  ]
  node [
    id 18
    label "Yokohama DC2"
    Internal 1
  ]
  node [
    id 19
    label "Nagoya DC"
    Internal 1
  ]
  node [
    id 20
    label "Kyoto DC"
    Internal 1
  ]
  node [
    id 21
    label "Shinsaibashi DC"
    Internal 1
  ]
  node [
    id 22
    label "Fukuoka DC"
    Internal 1
  ]
  node [
    id 23
    label "Newyork DC"
    Internal 1
  ]
  node [
    id 24
    label "PaloAlto DC"
    Internal 1
  ]
  node [
    id 25
    label "San Jose DC"
    Internal 1
  ]
  node [
    id 26
    label "LA DC"
    Internal 1
  ]
  node [
    id 27
    label "Ashburn DC"
    Internal 1
  ]
  node [
    id 28
    label "Equinix exchange"
    Internal 0
  ]
  node [
    id 29
    label "dix-ie"
    Internal 0
  ]
  node [
    id 30
    label "JPNAP Tokyo 1"
    Internal 0
  ]
  node [
    id 31
    label "China"
    Internal 0
  ]
  node [
    id 32
    label "JPNAP Osaka"
    Internal 0
  ]
  node [
    id 33
    label "JPNAP Tokyo 2"
    Internal 0
  ]
  node [
    id 34
    label "NYIIX"
    Internal 0
  ]
  node [
    id 35
    label "PAIX"
    Internal 0
  ]
  node [
    id 36
    label "LAIIX"
    Internal 0
  ]
  edge [
    source 0
    target 1
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 0
    target 14
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 1
    target 2
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 1
    target 4
    LinkType "STM-1"
    LinkLabel "STM-1"
  ]
  edge [
    source 1
    target 5
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 1
    target 9
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 1
    target 10
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 1
    target 11
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 1
    target 12
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 1
    target 13
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 1
    target 14
    LinkSpeed "10"
    LinkSpeedUnits "G"
    LinkLabel "10GEx24"
    LinkNote "Ex24"
  ]
  edge [
    source 1
    target 14
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 1
    target 15
    LinkSpeed "10"
    LinkSpeedUnits "G"
    LinkLabel "10Gex12"
    LinkNote "ex12"
  ]
  edge [
    source 1
    target 17
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 1
    target 18
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 1
    target 19
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 1
    target 21
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 1
    target 25
    LinkType "STM-64"
    LinkLabel "STM-64x4"
    LinkNote "x4"
  ]
  edge [
    source 1
    target 29
    LinkSpeed "11"
    LinkLabel "11Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 1
    target 30
    LinkSpeed "30"
    LinkLabel "30Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 2
    target 3
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 3
    target 21
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 4
    target 19
    LinkType "STM-1"
    LinkLabel "STM-1"
  ]
  edge [
    source 5
    target 32
    LinkSpeed "40"
    LinkLabel "40Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 5
    target 6
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 5
    target 7
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 5
    target 14
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 5
    target 15
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 5
    target 19
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 5
    target 20
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 5
    target 21
    LinkSpeed "10"
    LinkSpeedUnits "G"
    LinkLabel "10GEx8"
    LinkNote "Ex8"
  ]
  edge [
    source 5
    target 22
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 5
    target 26
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 5
    target 31
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 6
    target 21
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 7
    target 21
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 8
    target 22
    LinkType "STM-4"
    LinkLabel "STM-4x2"
    LinkNote "x2"
  ]
  edge [
    source 9
    target 14
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 10
    target 14
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 11
    target 14
    LinkType "STM-4"
    LinkLabel "STM-4x2"
    LinkNote "x2"
  ]
  edge [
    source 12
    target 14
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 13
    target 14
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 14
    target 15
    LinkSpeed "10"
    LinkSpeedUnits "G"
    LinkLabel "10GEx12"
    LinkNote "Ex12"
  ]
  edge [
    source 14
    target 16
    LinkSpeed "10"
    LinkSpeedUnits "G"
    LinkLabel "10GEx4"
    LinkNote "Ex4"
  ]
  edge [
    source 14
    target 17
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 14
    target 18
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 14
    target 19
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 14
    target 21
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 14
    target 26
    LinkType "STM-64"
    LinkLabel "STM-64x2"
    LinkNote "x2"
  ]
  edge [
    source 15
    target 33
    LinkSpeed "10"
    LinkLabel "10Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 20
    target 21
    LinkType "STM-4"
    LinkLabel "STM-4"
  ]
  edge [
    source 21
    target 22
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 23
    target 25
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 23
    target 26
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 23
    target 27
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 23
    target 34
    LinkSpeed "10"
    LinkLabel "10Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 23
    target 35
    LinkSpeed "10"
    LinkLabel "10Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 24
    target 25
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 24
    target 26
    LinkType "STM-16"
    LinkLabel "STM-16"
  ]
  edge [
    source 25
    target 26
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 25
    target 27
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 25
    target 28
    LinkSpeed "10"
    LinkLabel "10Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 26
    target 36
    LinkSpeed "1"
    LinkLabel "1Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 26
    target 27
    LinkType "STM-64"
    LinkLabel "STM-64"
  ]
  edge [
    source 26
    target 28
    LinkSpeed "10"
    LinkLabel "10Gb/s"
    LinkSpeedUnits "G"
  ]
  edge [
    source 27
    target 28
    LinkSpeed "10"
    LinkLabel "10Gb/s"
    LinkSpeedUnits "G"
  ]
]
