from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#Add Switches
		s0 = self.addSwitch('s0')
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		#Add 2 hosts to each switch
		h1 = self.addHost('h1')
		h2 = self.addHost('h2')
		h3 = self.addHost('h3')
		h4 = self.addHost('h4')
		h5 = self.addHost('h5')
		h6 = self.addHost('h6')
		h7 = self.addHost('h7')
		h8 = self.addHost('h8')
		h9 = self.addHost('h9')
		h10 = self.addHost('h10')
		h11 = self.addHost('h11')
		h12 = self.addHost('h12')
		#Add a link of hosts and switch
		self.addLink('s0','h1')
		self.addLink('s0','h2')
		self.addLink('s1','h3')
		self.addLink('s1','h4')
		self.addLink('s2','h5')
		self.addLink('s2','h6')
		self.addLink('s3','h7')
		self.addLink('s3','h8')
		self.addLink('s4','h9')
		self.addLink('s4','h10')
		self.addLink('s5','h11')
		self.addLink('s5','h12')
		#Add a link of switches of original topology
		self.addLink('s0','s1')
		self.addLink('s0','s2')
		self.addLink('s0','s4')
		self.addLink('s0','s5')
		self.addLink('s1','s2')
		self.addLink('s1','s4')
		self.addLink('s1','s5')
		self.addLink('s2','s4')
		self.addLink('s2','s5')
		self.addLink('s3','s4')
		self.addLink('s4','s5')
		
topos = { 'Dataxchange': ( lambda: MininetNX() ) }