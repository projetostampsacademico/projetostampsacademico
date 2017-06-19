<?php
class SeleniumTest extends PHPUnit_Extensions_Selenium2TestCase {
	private $server;
	private $port;
	private $browser;
	private $url;

	protected function setUp() {
		
		$this->server = getenv('SERVER');
		$this->port = getenv('PORT');
		$this->browser = getenv('BROWSER');
		$this->url = getenv('URL');

		$this->setHost($this->server);
		$this->setPort((int)$this->port);
		$this->setBrowser($this->browser);
		$this->setBrowserUrl($this->url);
		
	/* 	
	 	$this->setDesiredCapabilities(array(
				'applicationCacheEnabled'=>false,
				'rotatable'=>false,
				'mobileEmulationEnabled'=>false,
				'networkConnectionEnabled'=>false,
				'takesHeapSnapshot'=>true,
				'pageLoadStrategy'=>'normal',
				'databaseEnabled'=>false,
				'handlesAlerts'=>true,
				'hasTouchScreen'=>false,
				'platform'=>'LINUX',
				'browserConnectionEnabled'=>false,
				'nativeEvents'=>true,
				'acceptSslCerts'=>true,
				'locationContextEnabled'=>true,
				'webStorageEnabled'=>true,
				'takesScreenshot'=>true,
				'javascriptEnabled'=>true,
				'cssSelectorsEnabled'=>true
		));
	*/
		 
	}

	function testUm() {
		$this->assertTrue(true);
	}

	function testDois() {
		$this->assertTrue(true);
	}

	public function tearDown() {
		$this->stop();
	}
}
?>
