from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#Set Here Default Parameters
		switchParameters= {}
		hostParameters= {}
		linkHSParameters= {}
		linkSSParameters= {}
		#Add Switches
		s0 = self.addSwitch('s0',**switchParameters)
		s1 = self.addSwitch('s1',**switchParameters)
		s2 = self.addSwitch('s2',**switchParameters)
		s3 = self.addSwitch('s3',**switchParameters)
		s5 = self.addSwitch('s5',**switchParameters)
		s6 = self.addSwitch('s6',**switchParameters)
		s7 = self.addSwitch('s7',**switchParameters)
		s8 = self.addSwitch('s8',**switchParameters)
		s9 = self.addSwitch('s9',**switchParameters)
		s10 = self.addSwitch('s10',**switchParameters)
		s11 = self.addSwitch('s11',**switchParameters)
		s12 = self.addSwitch('s12',**switchParameters)
		s13 = self.addSwitch('s13',**switchParameters)
		s15 = self.addSwitch('s15',**switchParameters)
		s16 = self.addSwitch('s16',**switchParameters)
		s17 = self.addSwitch('s17',**switchParameters)
		#Add 1 hosts to each switch
		h0 = self.addHost('h0',**hostParameters)
		h1 = self.addHost('h1',**hostParameters)
		h2 = self.addHost('h2',**hostParameters)
		h3 = self.addHost('h3',**hostParameters)
		h4 = self.addHost('h4',**hostParameters)
		h5 = self.addHost('h5',**hostParameters)
		h6 = self.addHost('h6',**hostParameters)
		h7 = self.addHost('h7',**hostParameters)
		h8 = self.addHost('h8',**hostParameters)
		h9 = self.addHost('h9',**hostParameters)
		h10 = self.addHost('h10',**hostParameters)
		h11 = self.addHost('h11',**hostParameters)
		h12 = self.addHost('h12',**hostParameters)
		h13 = self.addHost('h13',**hostParameters)
		h14 = self.addHost('h14',**hostParameters)
		h15 = self.addHost('h15',**hostParameters)
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0',**linkHSParameters)
		lhs1 = self.addLink('s1','h1',**linkHSParameters)
		lhs2 = self.addLink('s2','h2',**linkHSParameters)
		lhs3 = self.addLink('s3','h3',**linkHSParameters)
		lhs4 = self.addLink('s5','h4',**linkHSParameters)
		lhs5 = self.addLink('s6','h5',**linkHSParameters)
		lhs6 = self.addLink('s7','h6',**linkHSParameters)
		lhs7 = self.addLink('s8','h7',**linkHSParameters)
		lhs8 = self.addLink('s9','h8',**linkHSParameters)
		lhs9 = self.addLink('s10','h9',**linkHSParameters)
		lhs10 = self.addLink('s11','h10',**linkHSParameters)
		lhs11 = self.addLink('s12','h11',**linkHSParameters)
		lhs12 = self.addLink('s13','h12',**linkHSParameters)
		lhs13 = self.addLink('s15','h13',**linkHSParameters)
		lhs14 = self.addLink('s16','h14',**linkHSParameters)
		lhs15 = self.addLink('s17','h15',**linkHSParameters)
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s12',**linkSSParameters)
		lss1 = self.addLink('s0','s13',**linkSSParameters)
		lss2 = self.addLink('s1','s16',**linkSSParameters)
		lss3 = self.addLink('s2','s8',**linkSSParameters)
		lss4 = self.addLink('s3','s16',**linkSSParameters)
		lss5 = self.addLink('s5','s12',**linkSSParameters)
		lss6 = self.addLink('s6','s16',**linkSSParameters)
		lss7 = self.addLink('s7','s13',**linkSSParameters)
		lss8 = self.addLink('s8','s13',**linkSSParameters)
		lss9 = self.addLink('s9','s13',**linkSSParameters)
		lss10 = self.addLink('s9','s10',**linkSSParameters)
		lss11 = self.addLink('s11','s12',**linkSSParameters)
		lss12 = self.addLink('s11','s16',**linkSSParameters)
		lss13 = self.addLink('s13','s17',**linkSSParameters)
		lss14 = self.addLink('s15','s16',**linkSSParameters)
		
topos = { 'KentmanJul2005': ( lambda: MininetNX() ) }