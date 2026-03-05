from pyats import aetest

class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect(self, testbed):
        device = testbed.devices['R1']
        device.connect()
        self.parent.parameters['device'] = device

class TestShowVersion(aetest.Testcase):
    @aetest.test
    def run_show_version(self, device):
        output = device.execute('show version')
        print(f"\n--- Show Version Output ---\n{output}")
        
        if output:
            self.passed("Successfully retrieved show version output")
        else:
            self.failed("Failed to get output from device")

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect(self, device):
        device.disconnect()
