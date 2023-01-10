from logfile import logclass
class TestDemo(logclass):
    def test_inside_class(self):
        log = self.getthelogs()
        log.info("This is My First test case")
        log.info("test case is not starting ")

        if 'sohail' in 'sohailbadeghar':
            assert True
            log.info("test case is passed")
        else:
            log.error("test case is Fail")
            assert False