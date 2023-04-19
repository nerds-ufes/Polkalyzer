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
		s4 = self.addSwitch('s4',**switchParameters)
		s5 = self.addSwitch('s5',**switchParameters)
		s6 = self.addSwitch('s6',**switchParameters)
		s7 = self.addSwitch('s7',**switchParameters)
		s8 = self.addSwitch('s8',**switchParameters)
		s9 = self.addSwitch('s9',**switchParameters)
		s10 = self.addSwitch('s10',**switchParameters)
		s11 = self.addSwitch('s11',**switchParameters)
		s12 = self.addSwitch('s12',**switchParameters)
		s13 = self.addSwitch('s13',**switchParameters)
		s14 = self.addSwitch('s14',**switchParameters)
		s15 = self.addSwitch('s15',**switchParameters)
		s16 = self.addSwitch('s16',**switchParameters)
		s17 = self.addSwitch('s17',**switchParameters)
		s18 = self.addSwitch('s18',**switchParameters)
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
		h16 = self.addHost('h16',**hostParameters)
		h17 = self.addHost('h17',**hostParameters)
		h18 = self.addHost('h18',**hostParameters)
		#Add a link of hosts and switch
		lhs0 = self.addLink('s0','h0',**linkHSParameters)
		lhs1 = self.addLink('s1','h1',**linkHSParameters)
		lhs2 = self.addLink('s2','h2',**linkHSParameters)
		lhs3 = self.addLink('s3','h3',**linkHSParameters)
		lhs4 = self.addLink('s4','h4',**linkHSParameters)
		lhs5 = self.addLink('s5','h5',**linkHSParameters)
		lhs6 = self.addLink('s6','h6',**linkHSParameters)
		lhs7 = self.addLink('s7','h7',**linkHSParameters)
		lhs8 = self.addLink('s8','h8',**linkHSParameters)
		lhs9 = self.addLink('s9','h9',**linkHSParameters)
		lhs10 = self.addLink('s10','h10',**linkHSParameters)
		lhs11 = self.addLink('s11','h11',**linkHSParameters)
		lhs12 = self.addLink('s12','h12',**linkHSParameters)
		lhs13 = self.addLink('s13','h13',**linkHSParameters)
		lhs14 = self.addLink('s14','h14',**linkHSParameters)
		lhs15 = self.addLink('s15','h15',**linkHSParameters)
		lhs16 = self.addLink('s16','h16',**linkHSParameters)
		lhs17 = self.addLink('s17','h17',**linkHSParameters)
		lhs18 = self.addLink('s18','h18',**linkHSParameters)
		#Add a link of switches of original topology
		lss0 = self.addLink('s0','s1',**linkSSParameters)
		lss1 = self.addLink('s0','s2',**linkSSParameters)
		lss2 = self.addLink('s1','s3',**linkSSParameters)
		lss3 = self.addLink('s2','s4',**linkSSParameters)
		lss4 = self.addLink('s2','s7',**linkSSParameters)
		lss5 = self.addLink('s3','s5',**linkSSParameters)
		lss6 = self.addLink('s3','s6',**linkSSParameters)
		lss7 = self.addLink('s4','s8',**linkSSParameters)
		lss8 = self.addLink('s4','s10',**linkSSParameters)
		lss9 = self.addLink('s5','s11',**linkSSParameters)
		lss10 = self.addLink('s9','s10',**linkSSParameters)
		lss11 = self.addLink('s11','s18',**linkSSParameters)
		lss12 = self.addLink('s11','s12',**linkSSParameters)
		lss13 = self.addLink('s11','s13',**linkSSParameters)
		lss14 = self.addLink('s12','s14',**linkSSParameters)
		lss15 = self.addLink('s14','s15',**linkSSParameters)
		lss16 = self.addLink('s15','s16',**linkSSParameters)
		lss17 = self.addLink('s16','s17',**linkSSParameters)
		
topos = { 'Aarnet': ( lambda: MininetNX() ) }